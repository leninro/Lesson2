while True:
    hello_user = input('How are u?')
    if hello_user == 'OK':
        print('nu OK')
        break


sk={"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}

while True:
    ask_user = input('ask me')
    if ask_user == 'Как дела!':
            print('Хорошо')
    elif ask_user == "Что делаешь?":
            print('Программирую')
            break
    else:
            print('ответь как надо ')