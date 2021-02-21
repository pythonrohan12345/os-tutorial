import os

path = os.chdir("C:/Users/Rohan/python/os_tutorials")
raw = input("C:/Users/Rohan/python/os_tutorials> ")

if raw=="mkdir":
    make = input("What is folder name which you have create: ")
    raw_work = os.mkdir(make)