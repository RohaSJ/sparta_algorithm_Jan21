input = "abcba"

def _is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False
    return True # 마지막까지 false 가 반환이 안 되었다면 true


# 재귀함수로 풀어보기 with 문자 슬라이 : 반복되는 구조로 문제가 점점 작아지는 것을 인식하고 그걸 함수로 해결하는 것
# 문자열 맨 뒤는 string[-1]
# 맨 앞뒤 검사를 했다면 is_palindrome(string[1:-1])로 축소가 될 수 있다.
# "소주만병만주소" 애서처럼 마지막에 한 글자가 남으면 회문이다 : "병" 한 글자 -> if len(string) <= 1
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]: # 탈출조건 1 : 맨 앞글자와 맨 뒤글자가 다르다면 false 탈출
        return False
    return is_palindrome(string[1:-1])

print(_is_palindrome(input))
print(is_palindrome(input))