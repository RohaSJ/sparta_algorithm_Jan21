class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


# 링크드리스트에서 저장해놓은 값은 항상 헤드 밖에 없음. 6과 3만 알고 있음.
# 각 링크드 리스트의 헤드를 따라가면서, 자릿수에 맞게 더해주시면 됩니다!
# 이 때, 자릿수에 맞게 더하기 위해서는 총액에서 10을 곱한 다음에 현재 노드의 값을 더해주시면 됩니다!
# 현재 [6] → [7] → [8] 로 연결되어 있으니까 sum 이라는 변수에 0 을 저장한 다음에
# 0 * 10 + 6 을 하면 sum은 6이 됩니다.
# 그리고 6 * 10 + 7 을 하면 sum 은 67이 되고,
# 67 * 10 + 8 을 하면 sum 이 678 이 되어 올바른 값을 구할 수 있습니다!


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = 0
    head_1 = linked_list_1.head
    while head_1 is not None:
        sum_1 = sum_1 * 10 + head_1.data
        head_1 = head_1.next

    sum_2 = 0
    head_2 = linked_list_2.head
    while head_2 is not None:
        sum_2 = sum_2 * 10 + head_2.data
        head_2 = head_2.next

    return sum_1 + sum_2

#  코드를 보면 head_1, head_2 등 비슷한 변수도 많고 중복되는 로직이 많습니다!

def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)

    return sum_1 + sum_2
def _get_linked_list_sum(linked_list):
    sum = 0
    head = linked_list.head
    while head is not None:
        sum = sum * 10 + head.data
        head = head.next
    return sum

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
