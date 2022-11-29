#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
onumber = number
if number < 0:
    number = -1 * number
a = number % 10
if a > 5:
    print ("Last digit of " + str(onumber) + " is " + str(a) + " and is greater than 5")
elif a == 0:
    print ("Last digit of " + str(onumber) + " is " + str(a) + " and is 0")
else:
    print ("Last digit of " + str(onumber) + " is " + str(a) + " and is less than 6 and not 0")
