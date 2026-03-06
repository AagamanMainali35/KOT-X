def role_required(roles):
    def decorator(func):
        def logic(*args,**kwargs):
            print(args)
        return logic
    return decorator