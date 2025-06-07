# son1 = input('son1: ')
# son2 = input('son2: ')
# if not son2.isdigit():
#     print('faqt raqam kiriting')
# operator = input('+,*,/,-,: ')




# if operator == '+':
#     print(son1+son2)
# elif operator == '/':
#     if son2 != "0":
#         print(son1 / son2)
#     else:
#         print(son1,"ni ",son2, 'ga bolib bolmaydi')
   
# elif operator == '*':
#     print(son1*son2)
# elif operator == '-':
#     print(son1-son2)
# else:
#     print('soz notogri belgi kiritdingiz')

# ===================================


# Ternar operatorlar
# bu bir qatorli kod sharlar if else da ishlaydi 
# age = 1

# print('siz voyaga yetgansiz' if age >= 18 else 'siz voyaga yetmagansiz')
# =============================================
# List
# friends = ['Ali','Komil','Bobir']
# print(friends)
# print(friends[-1])


# ===============


# List methodlar


items = ['Ali',True,12,False,[1,2,3]]


# .append(new_value) -> bu ro'yxat oxiriga malumot qoshish
# items.append(1)
# print(items)

# insert(index,value) -> royxat ichida istalgan joyga malumot qoshadi 

# items.insert(2,'akks')

#  .remove(value) -> Royxat ichidan qiymatni olib tashlaydi

# items.remove(True)
# print(items)


# .pop(value_index) -> Ro'yxat ichidan uzatilgan index raqam ostida yotgan qiymatni o'chiradi yani boshqa o'zgaruvchida saqlashi mumkin 
# ro'yxat ichidan qiymatni suguib olib moshqa o';zgaruvchiga saqalash mumkin
# delete_itme = items.pop(0)
# print(items,delete_itme)