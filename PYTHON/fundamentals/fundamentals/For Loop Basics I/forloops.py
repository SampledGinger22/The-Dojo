# #Basic
for x in range(151):
    print(x)

# #Multiples of Five
for y in range(5,1001,5):
    print(y)

#Counting, the Dojo Way
for x in range(1,101):
    if x % 10 == 0:
        x = "Coding Dojo"
        print(x)
    elif x % 5 == 0:
        x = "Coding"
        print(x)
    else: print(x)

#Whoa. That Sucker's Huge
x=0
for i in range(1,500001):
    if i%2==1:
        x=x+i
        ++i
print(x)

#Countdown by Fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
low_number=0
high_number=700
mult=3

for i in range(low_number,high_number):
    if i%mult==0:
        print(i)
    else: 
        ++i



