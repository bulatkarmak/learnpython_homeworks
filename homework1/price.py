def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

price_tag = format_price(56.24)
print(price_tag)