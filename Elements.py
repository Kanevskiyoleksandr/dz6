a = input('Введите число: ')
list = [int(x) for x in str(a)]
product = 0
for ele in range(0, len(list)):
    product = product + list[ele]
    print(product)