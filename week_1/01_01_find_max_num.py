input = [3, 5, 6, 1, 2, 4]


# 1. 다른 숫자들과 비교하는 방식 : 3과 5를 비교 3이 작음 실패 -> 5와 3 비교 -> 5와 6 비교 -> ...
# 배열의 숫자를 하나씩 꺼내야하므로 : 반복문 사용
# 비교할 변수들을 꺼내기 위해 : 반복문 한 번 더 사용 (이중반복문)
# break 실패하면 다음 넘버로 넘어가게 됨
# else for 문이 다 끝나도록 한 번도 break 이 실행되지 않았다면 실행
def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
