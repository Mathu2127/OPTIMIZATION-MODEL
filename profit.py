max_profit = 0
best_x = 0
best_y = 0

for x in range(11):
    for y in range(11):
        if x + y <= 10:
            profit = 3*x + 2*y
            if profit > max_profit:
                max_profit = profit
                best_x = x
                best_y = y

print("x =", best_x)
print("y =", best_y)
print("Maximum Profit =", max_profit)
