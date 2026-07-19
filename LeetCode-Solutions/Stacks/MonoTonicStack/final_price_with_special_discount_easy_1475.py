def final_price_with_discount(prices):
    n = len(prices)
    Stack = []
    for i in range(n):
        while Stack and prices[Stack[-1]] >= prices[i]:
            j = Stack.pop()
            prices[j] -= prices[i]
        Stack.append(i)
    return prices

prices = [8,4,6,2,3]
print(final_price_with_discount(prices))