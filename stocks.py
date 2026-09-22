import random

stocks = {
    "AAPL": [random.randint(201,501),random.randint(201,501)],
    "GOOGL": [random.randint(201,501),random.randint(201,501)],
    "MSFT": [random.randint(201,501),random.randint(201,501)],
    "AMZN": [random.randint(201,501),random.randint(201,501)],
    "META": [random.randint(201,501),random.randint(201,501)],
    "AVGO": [random.randint(201,501),random.randint(201,501)],
    "TSLA": [random.randint(201,501),random.randint(201,501)],
    "MU": [random.randint(201,501),random.randint(201,501)]

}



def calculate_loss(stock,purchase_price,current_price):
    total_loss = purchase_price - current_price
    if total_loss < 0:
        return f"YOU LOST {total_loss} on {stock}"
    else:
        return f"YOU MADE {total_loss} on {stock}"


for stock, price in stocks.items():
    print(f"STOCK: {stock} | PURCHASE PRICE: ${price[0]} | CURRENT PRICE: ${price[1]} ")
    calculate_loss(stock,{price[0]},{price[1]})

