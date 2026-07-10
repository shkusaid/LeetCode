# _______________________ BRUTE FORCE APPROACH ______________________

# def shipping_capacity(weights, days):
#     def can_ship(weights , days, cap):
#         d = 1
#         current = 0
#         for w in weights:
#             if current + w > cap:
#                 current = w
#                 d += 1
#             else:
#                 current += w
#         return d <= days

#     low = max(weights)
#     high = sum(weights)
#     for cap in range(low , high + 1):
#         if can_ship(weights , days , cap):
#             return cap
#     return high

# __________________________ OPTIMAL APPROACH _____________________________

def shipping_capacity(weights, days):
    def can_ship(weights , days, cap):
        d = 1
        current = 0
        for w in weights:
            if current + w > cap:
                current = w
                d += 1
            else:
                current += w
        return d <= days

    low = max(weights)
    high = sum(weights)
    ans = 0
    while low <= high:
        cap = low + (high - low) // 2
        if can_ship(weights , days, cap):
            ans = cap
            high = cap - 1
        else:
            low = cap + 1
    return ans

weights = list(range(1 ,11))
print(shipping_capacity(weights , 5))