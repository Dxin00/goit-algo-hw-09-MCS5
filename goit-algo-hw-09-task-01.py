import timeit

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    coin_count = [{} for _ in range(amount + 1)]
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_count[x] = coin_count[x - coin].copy()
                if coin in coin_count[x]:
                    coin_count[x][coin] += 1
                else:
                    coin_count[x][coin] = 1
    
    return coin_count[amount]

# Рандомні суми
test_amounts = [113, 93, 7, 100]

for amount in test_amounts:
    print(f"\nСума: {amount}")
    print(f"Жадібний алгоритм: {find_coins_greedy(amount)}")
    print(f"Динамічне програмування: {find_min_coins(amount)}")

large_amount = 10000

greedy_time = timeit.timeit(lambda: find_coins_greedy(large_amount), number=1000) / 1000

dp_time = timeit.timeit(lambda: find_min_coins(large_amount), number=1000) / 1000

print(f"\nПорівняння ефективності на сумі {large_amount}")
print(f"Жадібний алгоритм: час виконання = {greedy_time:.6f} секунд")
print(f"Динамічне програмування: час виконання = {dp_time:.6f} секунд")
