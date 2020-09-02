def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
x=int(input("enter 1st num : "))
y=int(input("enter 2nd num : "))
z=int(input("enter 3rd num : "))
print(sum(x, y, z))