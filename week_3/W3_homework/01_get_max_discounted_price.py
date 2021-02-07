shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 오름차순 정렬 -> 배열.sort()
# 내림차순 정렬 -> 배열.sort(reverse=True)격
# user_coupons 의 개수와 shop_prices 개수가 다름 -> 따라서 아래와 같이 while 문과 인덱스를 사용해서 해결해야 함.


def get_max_discounted_price(prices, coupons):
    coupons.sort(reverse=True)
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.