# apply tax rate to list of prices

prices = [1.09, 2356, 57.84, 4.56, 6.78]
TAX_RATE = .08


def get_price_with_tax(price):
    return price * (1 + TAX_RATE)


list_comp_final_prices = [get_price_with_tax(i) for i in prices]
print(list_comp_final_prices)

final_prices = map(get_price_with_tax, prices)
# list(final_prices)


for price in final_prices:
    print(price)
print(final_prices)
