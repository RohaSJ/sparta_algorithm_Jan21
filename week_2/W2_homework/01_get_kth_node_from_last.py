# 전체 길이를 알아내고, 그 길이 -K 만큼을 이동하면 뒤에서 k번째 만큼 이동할 수 있게 됨.


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

    # case 1 : LinkedList 길이 전부 알아내기 & 그 길이에서 k 만큼 뺀 길이만큼 이동

    def get_kth_node_from_last(self, k):
        length = 1  # 시작 노드의 길이. 즉 헤드 노드가 있기 때문에 걔의 길이를 처음에 포함시켜 주고자 1을 설명
        cur = self.head  # 노드를 이동하기 위한 새로운 변수

        while cur.next is not None:  # 반복문을 통해서 cur 변수를 끝까지 이동 시킴
            cur = cur.next
            length += 1
            # 반복문이 끝났다는 것은 끝에 도달했다는 의미
        end_length = length - k  # 뒤에서 k 만큼 떨어진
        cur = self.head  # 다시 self.head fmf current 변수에 담아서 cur 변수를 이동시켜서 k 번째 값을 찾도록 하기.
        for i in range(end_length):
            cur = cur.next
        return cur

    # case2 : 노드를 두개 잡아서, 첫번째 노드가 두번째 노드모다 K만큼 떨어지게 하고, 계속 한 칸씩 함께 이동 시킴.
    #         만약 두번째 노드가 끝에 도달하였다면 첫번째 노드는 끝에서 k만큼 떨어진 노드가 됨. -> 반환

    def _get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head
        for i in range(k):  # for문을 통해서 fast가 k만큼 거리를 떨어뜨릴 수 있음.
            fast = fast.next

        while fast is not None:  # fast 가 끝까지 이동하도록
            fast = fast.next
            slow = slow.next

        return slow  # 뒤에서 k만큼 떨어진 노드를 반환할 수 있게 됨.


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)
print(linked_list._get_kth_node_from_last(2).data)

# 두번 도는 것 보다 한 번 도는 것이 빠르기 때문에 개선한 코드가 빠를 것이다 라고 예상 할 수 있는데
# 시간 복잡도 측면에서 두 코드는 O(N) 0(N-L) 로 같음.
