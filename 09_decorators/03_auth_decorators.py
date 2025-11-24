from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role == "admin":
            return func(user_role)
        raise Exception("Admin privileges required")
    return wrapper

@require_admin
def delete_user(user_role):
    print("User deleted")

# delete_user("developer")
delete_user("admin")
        