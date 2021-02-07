input = 20

# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
# number 이하 소수를 찾아야하므로 2부터 number 까지의 숫자를 다 찾아야함 (0과 1은 소수가 될 수 없음)
# for n in range (2, number + 1) : # n <- 2 ~ number + 1  :  number+1에서 하나를 뗀 숫자인 number 까지 반복
def find_prime_list_under_number(number):
    prime_list = []
    for n in range (2, number + 1) : # n <- 2 ~ number + 1
        for i in range(2, n) :
            if n % i == 0: # 2부터 자기 자시보다 1 작은 수까지 전부 나눠봄, 나눠 떨어진다면 소수가 아니기 때문에 반복문을 중단하고 다음 n으로 넘어가게 됨.
                break
        else: # break 가 한 번도 발생하지 않닸다면 이 숫자를 prime list 에 추가
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)