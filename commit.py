#!/usr/bin/env python3
"""
Git Backdated Commit Script
Ask for author date, committer date, and commit message, then execute git commands
"""

import os
import subprocess
import sys
from datetime import datetime


def get_date_input(prompt):
    """Get date input from user with validation"""
    print(f"\n{prompt}")
    print("Format options:")
    print("  1. YYYY-MM-DD HH:MM:SS  (e.g., 2026-02-27 12:30:00)")
    print("  2. YYYY-MM-DD           (e.g., 2026-02-27) - time will be 12:00:00")
    print("  3. Relative              (e.g., '2 days ago', 'yesterday')")

    while True:
        date_str = input("Enter date: ").strip()

        if not date_str:
            print("Date cannot be empty!")
            continue

        # If just date provided, add default time
        if len(date_str) == 10 and date_str.count("-") == 2:
            date_str = f"{date_str} 12:00:00"

        return date_str


def run_command(command, shell=True):
    """Run a shell command and print output"""
    print(f"\n🔧 Running: {command}")
    try:
        result = subprocess.run(command, shell=shell, capture_output=True, text=True)
        if result.stdout:
            print("📤 Output:", result.stdout)
        if result.stderr:
            print("⚠️  Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    print("=" * 60)
    print("🚀 GIT BACKDATED COMMIT SCRIPT")
    print("=" * 60)

    # Check if we're in a git repository
    if not os.path.exists(".git"):
        print("❌ Not in a git repository! Run this script from your project root.")
        sys.exit(1)

    # Show current status
    run_command("git status")

    # Confirm staging all files
    print("\n" + "=" * 60)
    response = input("Do you want to stage ALL changes? (y/n): ").strip().lower()
    if response != "y":
        print("❌ Aborted.")
        sys.exit(0)

    # Step 1: git add .
    print("\n" + "=" * 60)
    print("📁 Step 1: Staging all files...")
    if not run_command("git add ."):
        print("❌ Failed to stage files")
        sys.exit(1)

    # Step 2: Get commit details
    print("\n" + "=" * 60)
    print("📝 Step 2: Enter commit details")

    # Get author date
    print("\n👤 AUTHOR DATE (when the work was done)")
    author_date = get_date_input("Enter author date:")

    # Get committer date
    print("\n🕒 COMMITTER DATE (when committing)")
    committer_date = get_date_input("Enter committer date:")

    # Get commit message
    print("\n💬 COMMIT MESSAGE")
    commit_message = input("Enter commit message: ").strip()
    while not commit_message:
        print("Commit message cannot be empty!")
        commit_message = input("Enter commit message: ").strip()

    # Show summary
    print("\n" + "=" * 60)
    print("📋 SUMMARY")
    print(f"Author Date:    {author_date}")
    print(f"Committer Date: {committer_date}")
    print(f"Commit Message: {commit_message}")
    print("=" * 60)

    # Confirm
    confirm = input("\nProceed with commit? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Aborted.")
        sys.exit(0)

    # Step 3: Create commit with backdated timestamps
    print("\n" + "=" * 60)
    print("✅ Step 3: Creating backdated commit...")

    # For Unix/Linux/Mac/Git Bash
    commit_cmd = f'GIT_AUTHOR_DATE="{author_date}" GIT_COMMITTER_DATE="{committer_date}" git commit -m "{commit_message}"'

    # Check if we're on Windows
    if sys.platform == "win32":
        # For Windows CMD
        commit_cmd = f'set GIT_AUTHOR_DATE={author_date} && set GIT_COMMITTER_DATE={committer_date} && git commit -m "{commit_message}"'

    if not run_command(commit_cmd):
        print("❌ Failed to create commit")
        sys.exit(1)

    # Step 4: Push to origin main
    print("\n" + "=" * 60)
    print("🚀 Step 4: Pushing to origin main...")

    push_confirm = input("Push to origin main? (y/n): ").strip().lower()
    if push_confirm == "y":
        if run_command("git push origin main"):
            print("✅ Successfully pushed!")
        else:
            print("❌ Push failed. You may need to push manually.")
    else:
        print("⏭️  Skipping push. Remember to push later!")

    # Step 5: Show final commit
    print("\n" + "=" * 60)
    print("📜 Final commit details:")
    run_command("git log -1 --pretty=fuller")

    print("\n" + "=" * 60)
    print("✅ Script completed!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Script interrupted by user")
        sys.exit(1)
