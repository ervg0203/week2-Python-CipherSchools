# practice for loop
# ask user name and count each character
# "Harshit Vashishth"
# H : 1
# a : 1
# r : 1
# s : 1
# h : 1
# i : 1
# t : 1
#   : 1
# V : 1
name = input("enter your name : ")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]