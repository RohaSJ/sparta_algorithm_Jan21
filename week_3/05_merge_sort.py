# 분할 정복은 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음,
# 결과를 모아서 원래의 문제를 해결하는 전략.
# 이를 분할 정복, Divide and Conquer 라고 합니다.

# 이렇게 동일한 형태로 반복되는 경우에는 어떤 코드가 생각나나요?
# 바로 "재귀" 적인 코드가 떠오릅니다.
# 자기 자신을 포함하는 형식으로 함수를 이용해서 정의해보면,
# MergeSort(시작점, 끝점) 이라고 해볼게요.

# MergeSort**(0, N)** = Merge(MergeSort**(0, N/2)** + MergeSort**(N/2, N)**)
# 라고 할 수 있음. 즉, 0부터 N까지 정렬한 걸 보기 위해서는
# 0부터 N/2 까지 정렬한 것과 N/2부터 N까지 정렬한 걸 합치면 된다. 라는 개념

array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    print(array)
    print('left_arary', left_array)
    print('right_arary', right_array)
    return merge(merge_sort(left_array), merge_sort(right_array))


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!