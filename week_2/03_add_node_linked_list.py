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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1

        return node # "index 번째 노드를 반환해보세요!"

# ["자갈"] -> ["밀가루"] -> ["우편"] : 흑연을 추가한다면
    # 1. 자갈 칸의 연결고리를 밀가루와 끊고 흑연 칸으로 연결하고, ["자갈"] -> ["흑연"]   ["밀가루"] -> ["우편"]
    # 2. 흑연 칸으로 연결고리를 밀가루 칸으로 연결합니다. ["자갈"] -> ["흑연"] -> ["밀가루"] -> ["우편"]

# index 에 자갈 칸을 하나의 변수로 저장하고! 끊은 밀가루 칸을 임시로 저장해 놔야 함.
# 따라서 next_node 라는 변수에 현재 노드와 연결된 노드를 (밀가루 -> 우편) 저장해두고 ! 흑연을 new_node 에 저장.

    # index.next = new_node
    # new_node.next = next_node

    # 1. 현재 노드의 다음 노드를 새로운 노드와 연결합니다.
    # 2. 새로운 노드의 다음 노드를 이전에 저장해둔 노드에 연결합니다.

    # Tip : 현재 노드를 구하기 위해서는 방금 만든 get_node 를 사용하면 됩니다!
    #       클래스 내부에 있는 다른 함수(메소드)를 부르기 위해서는, self.함수이름 으로 호출

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0: #head_node 를 new_node로 그냥 먼저 넣어버리면 안 됨. 이전에 있었던 헤드 노드들 전부 사라져버리기 때
            new_node.next = self.head #[6] -> [5]
            self.head = new_node #head > [6]
            return

        node = self.get_node(index)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# linked_list.print_all() # [5] -> [12] -> [8]

# [5] -> [6] -> [12] -> [8] 형태로 만들고 싶음
# node = self.get_node(index) 일 때는,
linked_list.add_node(1,6)
linked_list.print_all() # [5] -> [12] -> [6] -> [8] * index - 1로 지정해줘야하는 이유.


# 만약 index에 0이 입력된다면, get_node(-1) 이 호출되어서 원하지 않게 동작해버릴거에요!
# 따라서, 이런 경우는 예외처리를 따로 해주셔야 합니다. 만약 0번째에 노드를 넣고 싶다면 어떻게 해줘야 할까요?
# 새로운 노드의 next 를 현재 가지고 있는 head 에 연결하고, 우선 현재 가지고 있는 head 를 새로운 노드로 교체해주시면 됩니다!

    # if index == 0:
        # new_node.next = self.head
        # self.head = new_node
        # return





