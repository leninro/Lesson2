age = int(input('How old are u?'))
def what_to_do(age):
    if  age <= 0: 
        return 'Ne nado Tak'
    elif 0 <= age <= 6:
        return 'Sad'
    elif 7 <= age <= 17:
        return 'School'
    elif 18 <= age <= 25:
        return 'Univer'
    else:
        return 'work wrok'

print(what_to_do(age))