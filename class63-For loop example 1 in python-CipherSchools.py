# sum from 1 to 10
# 1 + 2 + 3 + 4 ........ 10
#
# total = 0 + 1 +2 +3 +4 ........+20
# for i in range(1,21):
#     total += i
# print(total)

n = int(input("Enter your number here: "))
total = 0
for i in range(1,n+1):
    total += i
print(total)