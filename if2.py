def comparison(one, two):
    one = str(one)
    two = str(two)
    if type(one) == type(two) == str:
        return '0'
    elif one == two :
        return '1'
    elif len(one) >= len(two):
        return '2'
    elif len(one) <= len(two) and two == 'learn':
        return '3'
print(comparison(ads, afsf)