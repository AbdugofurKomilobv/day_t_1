son1 = input('son1: ')
son2 = input('son2: ')
if not int(son2.isdigit() and son1.isdigit()):
    print('faqt raqam kiriting')
operator = input('+,*,/,-,: ')




if operator == '+':
    print(son1+son2)
elif operator == '/':
    print(son1/son2)
elif operator == '*':
    print(son1*son2)
elif operator == '-':
    print(son1-son2)
else:
    print('soz notogri belgi kiritdingiz')