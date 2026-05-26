def maxProfit(prices: list[int]) -> int:
    answer = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        answer = max(answer, profit)

    return answer

print(maxProfit([10,1,5,6,7,1]))