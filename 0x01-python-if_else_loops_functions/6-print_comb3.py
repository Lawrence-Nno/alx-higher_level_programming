#!/usr/bin/python3
for i in range(100):
    if i%10 > i//10 and i//10 >= 8:
        print(f"{i//10}{i%10}")
    elif i%10 > i//10:
        print(f"{i//10}{i%10}, ", end="")
