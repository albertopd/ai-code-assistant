# [ERROR] SyntaxError: invalid syntax. Perhaps you forgot a comma?

employees = {"pam" 30,
             "jim": 28}

for name, age in employees.items():
    print(f"{name.capitalize()} is {age} years old.")