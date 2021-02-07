# numbers = [1, 1, 1, 1, 1]
# target_number = 3

# 문제를 간결하게 만들어서 생각해보면 편함.
numbers = [2, 3, 1]
target_number = 0
# 규칙이 있을거라고 생각할 수 있으나, 규칙을 만들 수 없는 경우도 있음.
# 모든 경우의 수를 다 찾아서 확인해볼 것.
# +++ / ++-
# +-+ / +--
# -++ / -+-
# --+ / ---
# 앞에 두 가지를 고정하고 세번째가 두가지의 경우 수가 추가적으로 생김
# 즉, N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N-1 의 길이의 배열에서 더하거나 뺀 모든 경우의 수에서 ... 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 됨.

result = []  # 모든 경우의 수를 담기위한 변수


# 2,3,1 이 array 에 들어가면 하나하나 경우의 수를 추가해서 나가게 됨.
# current_index = 0 현재 인덱스 다음에 새로운 인덱스를 넣을지 말지에 따라서 새로운 경우의 수가 추가되는 것이기 때문에 현재 인덱스가 어디를 보고 있는지에 대한 인자를 넘겨주어야함
# current_sum = 0 -> 처음엔 아무것도 더하지 않았으니깐, 0
# all_ways = result = [] # 관리하기 위한 배열 / 처음에는 빈 배열 / current_index 가 맨 마지막에 다달았을 때 값을 추가해주게 됨
# numbers[current_index] : 현재 들어온 숫자

# 1. 모든 경우의 수를 출력하는 함수
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(numbers):  # current_index 가 맨 마지막에 다달았을 때 current_sum 값을 추가해주게 됨
        all_ways.append(current_sum)  # 한 칸 한 칸 갈 때마다 이 값을 플러스 할 건지 마이너스 할 건지 넘겨주기 때문에
        return
    get_all_ways_to_by_doing_plus_or_minus(
        array, current_index + 1, current_sum + numbers[current_index], all_ways
    )  # (array, 1, 0 + 2, all_ways)
    get_all_ways_to_by_doing_plus_or_minus(
        array, current_index + 1, current_sum - numbers[current_index], all_ways
    )  # (array, 1, 0 - 2, all_ways)


print(get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result))  # None
print(result)  # [6, 4, 0, -2, 2, 0, -4, -6]
