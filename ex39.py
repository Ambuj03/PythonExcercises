import datetime
import time

now = datetime.datetime.now()

name = input("Enter you name ")
age = int(input("Enter you age "))

print("{} will turn 100 in {}".format(name,str(now.year - age + 100)))
