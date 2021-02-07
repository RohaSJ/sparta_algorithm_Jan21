# 재귀함수는 반드시 빠져나가는 지점을 명확하게 정해줘야 합니다.
# 그렇지 않으면 무한 루프에 빠져서 에러가 납니다.


def count_down(number):
    if number < 0:         # 만약 숫자가 0보다 작다면, 빠져나가자!
        return

    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)