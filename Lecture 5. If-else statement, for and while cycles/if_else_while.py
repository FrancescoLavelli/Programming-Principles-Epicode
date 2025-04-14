# user_logged_in = True
# user_status = "active" if user_logged_in else "inactive"    #Ternary Operator.
# if i write like that is like writing user_logged_in = true.

# Else after while si verifica solo se e quando il ciclo finisce naturalmente

import timeit
chores = ["Wash dishes", "Make bed", "Wash Teeth"]
# count = 0

# for chore in chores:
#     count += 1
#     print(f"#.{count} - {chore}")


# FUnction enumerate to do the above

# for id, chore in enumerate(chores, start=1):
#     print(id, chore)


def loop1():
    for seconds in range(10, 0, -1):
        print(seconds)


def loop2():
    seconds = 10
    while seconds > 0:
        print(seconds)
        seconds -= 1


time1 = timeit.timeit(stmt=loop1, number=10000)

time2 = timeit.timeit(stmt=loop2, number=10000)
print(f"For loop: {time1:.6f} seconds")
print(f"While loop: {time2:.6f} seconds")
#while loop i faster, ask professor
