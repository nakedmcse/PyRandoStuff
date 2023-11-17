# Lambda vs Foreach
num = [1,2,3,4,5]

#foreach version
for i in num:
    if i%2==0:
        continue
    print(i**2,end=' ')

print()

#lambda version
list(map(lambda odd_square: print(odd_square**2,end=' ') if odd_square % 2 != 0 else None, num))

print()

#filtered list
print(list(filter(lambda x: x is not None,map(lambda odd_square: None if odd_square%2==0 else odd_square**2,num))))