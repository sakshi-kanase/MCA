Correct_password = "python"
for attempt in range(1,4):
    password = input(("enter a password:"))
    if password == Correct_password:
        print("correct password")
        break
    else:
        print("not correct password")
else:
    print("you have 3 attempt")
