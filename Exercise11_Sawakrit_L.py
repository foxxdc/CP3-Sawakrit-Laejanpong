Round = int(input("Insert your * Numbers :"))
space = " "

for x in range(Round):
    for y in range(x+1):
        x+=1
    print(space*(Round-(y+1))+(x*"*"))
