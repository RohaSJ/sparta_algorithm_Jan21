input = [3, 5, 6, 1, 2, 4]


# 2. 지정 변수 : max_num 이라는 변수를 설정한 다음에 이 변수 가장 큰 녀석을 기록하도록 함\
# 3과 5 비교 5 기록 -> 5와 6 비교 6 기록 -> 6과 1 비교 ...
# max_num = array[0] -> 0번째 원소를 넣는 이유 : 배열에 임의의 숫자를 비교하면서 갈 거기 때문에 초기값을 설정해주는 것
def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num

    return max_num


result = find_max_num(input)
print(result)
