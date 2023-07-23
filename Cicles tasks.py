flag = False
for i in range(26):
    for j in range(26):
        text = f"{chr(ord('a') + i)}{chr(ord('a') + j)}"
        if text == "ya":
            print(text)
            flag = True
            break
        print(text)
    if flag:
        break
    
    
saved_pwd = "right_password"
while input("Введите пароль для входа: ") != saved_pwd:
    pass
print("Пароль верный. Вход разрешён.")
#идентичный saved_pwd = "right_password"
#pwd = input("Введите пароль для входа: ")
#while pwd != saved_pwd:
#    pwd = input("Введите пароль для входа: ")
#print("Пароль верный. Вход разрешён.")
numbers = []
for i in range(10):
    numbers.append(int(input()))
print(numbers)
text = "Hey, world"
text_for_list = list(text)
print (text_for_list)
text_for_list [3] = "-"
print (''.join(text_for_list))
#add
lst = ['Преобразование','через','цикл', 3]

string = ''
for el in lst:
    #Добавляем к строке элемент списка
    string += str(el)
    #Добавляем к строке разделитель — в данном случае пробел
    string += ' '
print(string)