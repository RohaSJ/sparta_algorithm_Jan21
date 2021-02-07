input = "hello my name is sparta"


# continue : 반복문의 다음 인덱스로 넘어가게 함
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


result = find_max_occurred_alphabet(input)
print(result)
