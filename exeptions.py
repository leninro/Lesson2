while True:
    hello_user = input('How are u?')
    try:
        if hello_user == 'OK':
            print('nu OK')
    except KeyboardInterrupt:
        print('BY')
    break

def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(int(max_discount))
    try:
        if max_discount > 99:
            print("Ne na togo napal")
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError,TypeError):
            print('BY')
print(discounted(100,100))