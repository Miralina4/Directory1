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
