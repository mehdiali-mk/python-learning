# Expression Execution.

a , b = 2, 3
txt = "M"
print(2 * txt * 3) # MMMMMM

a , b = "K", 3
txt = "M"
print((txt + a) * b) # MKMKMK

a , b = 2, 3
c = 4
print(a + b * c) # 14

a , b = 10, 5.0
c = a * b
print(c) # 50.0

a , b = 11, 5
c = a / b
print(c) # 2.2

a , b = 11.5 , 5
c = a // b
print(c) # 2.0

a , b = 11.5, -5
c = a // b
print(c) #- 3.0

a , b = 5 , 3
c = a % b
print(c) # 2

a , b = 5 , -3
c = a % b
print(c) # -1