num1 = int(input('son1: '))
num2 = int(input('son2: '))
num3 = int(input('son3: '))
num4 = int(input('son4: '))

toq = []
juft = []

for num in [num1,num2,num3,num4]:
    if num % 2 == 0:
        juft.append(num)
    else:
        toq.append(num)

print(f"Juft{juft}")
print(f'toq {toq}')


