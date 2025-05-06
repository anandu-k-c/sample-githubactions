# Sample script with issues for SonarQube analysis

def authenticate_user(username, password):
    if username == "admin" and password == "admin123":  # Hardcoded credentials (security issue)
        print("Access granted")
    else:
        print("Access denied")

def unused_function():
    unused_var = 42  # Unused variable (code smell)
    return

def complex_logic(n):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            result += i
        else:
            if i % 3 == 0:
                result -= i
            else:
                if i % 5 == 0:
                    result += i * 2
                else:
                    result += i
    return result

if __name__ == "__main__":
    authenticate_user("admin", "admin123")
    print("Complex result:", complex_logic(10))
