def exercise():
    count = 0
    while count < 4:
        count += 1
        user_input = f">>>{input()}"
        print(f"Var: {user_input} Type: {type(user_input)}")
    return user_input  # Optional return after the loop completes


# def exercise():
#     count = 0
#     while count < 4:
#         count += 1
#         user_input = input()
#         print(f"Var: {user_input} Type: {type(user_input)}")
#     return user_input  # Optional return after the loop completes
