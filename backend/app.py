
products = [
    ['apple', 10],
    ['orange', 5],
    ['banana', 12],
    ['date', 20],
    ['strawberry', 16]
]

print("قائمة المنتجات:")
for i in range(len(products)):
    print(i+1, products[i][0], "-", products[i][1], "$")

num = int(input("اختر رقم المنتج: "))


price = products[num-1][1]
total = price * 1.15

print("السعر شامل الضريبة 15% هو:", total, "$")
