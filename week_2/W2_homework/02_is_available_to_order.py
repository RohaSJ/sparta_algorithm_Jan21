shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# case 1
# 집합 사용하기 : 중복을 허용하지 않는 자료형태, set 사용
# a = set([1,2,3,4,1,2,3]) -> a 는 {1,2,3,4}복
# O(N) + 0(M) = O(M+N)

def _is_available_to_order(menus, orders):
    menus_set = set(menus)  # O(N)
    for order in orders:  # M번 반
        if order not in menus_set:  # O(1)
            return False
    return True


# case 2
# 이분탐색을 하기 위해서는 정렬이 꼭 필요함.
# O(N * logN) + O(M * logN) = O((N+M) * logN) -> 비효율적

def is_available_to_order(menus, orders):
    shop_menus.sort()  # 정렬의 시간 복잡도는 : 배열의 길이를 n이라고 한다면, O(N * logN)
    for order in orders:  # orders 길이를 M이라고 한다면 시간 복잡도는 : O(M * logN) // logN 은 is_existing_target_number_binary 의 시간 복잡
        if not is_existing_target_number_binary(order, shop_menus):  # (target, array) # 만약 하나도 존재하지 않는다면 false
            return False
    return True


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    # find_count = 0
    while current_min <= current_max:
        # find_count += 1
        if array[current_guess] == target:
            # print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_available_to_order(shop_menus, shop_orders)
result1 = _is_available_to_order(shop_menus, shop_orders)
print(result1)


# 결론 : 이분탐색법이 효율적인 방법이긴 하나, 경우에 따라서는 집합 자료구조를 쓸 때가 더 좋을 때도 있음.