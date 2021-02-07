# 1단계 : [4, 6, 2, 9, 1] 4와 6과 2와 9와 1을 차례차례 비교,
# 그 중 가장 작은 1과 맨 앞 자리인 4를 교체.


#1번째 : [4, 6, 2, 9, 1]
#        4, 6, 2, 9, 1 중 최솟값 찾기!
#2번째 : [1, 6, 2, 9, 4]
#           6, 2, 9, 4 중 최솟값 찾기!
#3번째 : [1, 2, 6, 9, 4]
#              6, 9, 4 중 최솟값 찾기!
#4번째 : [1, 2, 4, 9, 6]
#                 9, 6 중 최솟값 찾기!

# Q. 여기서 왜 5 - 1 일까요? A. 맨 마지막 비교는 하지 않아도 되기 때문
# 위의 예시에서 4번째 비교를 하면 [1, 2, 4, 6, 9] 로 변경이 되는데, 굳이 9와 9를 비교할 필요가 없기 때문!

# array[i + j] -> 현재 시도해보고 있는 인덱스

# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 선택 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]


selection_sort(input)
print(input)

# 시간복잡도 : O(N^2)
