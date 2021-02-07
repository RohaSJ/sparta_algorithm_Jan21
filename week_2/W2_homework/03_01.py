numbers = [1, 1, 1, 1, 1]
target_number = 3
result_count = 0


# 모든 경우의 수 중에서 target 을 만족하는 경우가 몇 개인지 알고 싶으므로
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            global result_count  # 내부에서 함수 외부에 있는 변수를 사용하겠
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + numbers[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - numbers[current_index])


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0))  # None
print(result_count)  # 0 -> 파이썬의 콜바이 오브젝트 레퍼런스 개념 때문

# 함수에서 파라미터로 배열 같은 걸 넘겼을 때, result 배열에 append 를 하는게 함수 내부에서 호출이 가능함
# 하지만, 0 혹은 문자열, 캐릭터 같은 변하지 않는 타입인 프리미티브 타입 같은 경우는 파이썬 내부에서 파라미터로 넘기면 그 값을 복제해서 새로운 것을 생성
# 함수에서 외부의 변수를 변경해주고 싶다면 global 이라는 키워드를 사용해야함
