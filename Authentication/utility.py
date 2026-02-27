# utility.py - SIMPLE password checker
import re

def check_pass(password):
    """
    Check if password has all required characters
    Returns: (is_valid , error_message)
    """
    # Check each requirement
    if not re.search(r'[A-Z]', password):
        return False, "Password needs an uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password needs a lowercase letter"
    
    if not re.search(r'[0-9]', password):
        return False, "Password needs a number"
    
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~]', password):
        return False, "Password needs a special character (!@#$ etc.)"
    
    if re.search(r'\s', password):
        return False, "Password cannot have spaces"
    
    # If all checks pass
    return True, "Password is valid"