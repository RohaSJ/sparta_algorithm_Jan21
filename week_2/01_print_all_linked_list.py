# 링크드리스트 생김새 -> * train_compartments = ["기관실"] -> ["시멘트"] -> ["자갈"] -> ["밀가루"] -> ["우편"]
# 노드는 두가지 정보가 필요 : 1) 칸에 있는 데이터 2) 다음 칸이 무엇인지 포인터
# 즉, 두 가지 데이터를 가지고 있어야 하니까 클래스를 이용하면 됨 ! 한 번, 클래스로 묶어보겠습니다!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 3을 가진 Node 만들어보자
node = Node(3)
# 노드들을 더 만들어서 연결해보자
first_node = Node(4)
node.next = first_node


# print(node.next.data) -> 4 출


# 이 노드들을 일일이 계속 연결해주려면 변수를 지정하고 위와 같은 코드를 반복해야 하는데, 너무 번거롭습니다!
# 따라서 LinkedList 라는 클래스를 한 번 만들어볼게요! LinkedList 는 head node 만 딱 들고 있습니다.
# 기차를 다시 떠올려보면, 맨 앞 칸만 저장해두는 거에요. 다음 칸을 보기 위해서는 next를 통해서 다음 노드에 접근해야 합니다!
# 1) LinkdList 는 self.head 에 시작하는 노드를 저장한다. 2) 다음 노드를 보기 위해서는 각 노드의 next 를 조회해서 찾아가야 한다.

# * LinkedList - headnode *
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)  # head 에 시작하는 Node 연결 (해당 데이터를 들고있는 노드를 생성해서 넣어, 방금 생성한 이 노드가 헤드 노드로써 저장이 됨.)

    # linked_list = LinkedList(5)
    # print(linked_list.head.data)  # 현재 LinkedList 는 (5) 만 존재합니다!

    # 이번에는, LinkedList 의 맨 뒤에 새로운 Node 를 붙이는 append 함수를 만들어보겠습니다!
    # 현재 있는 노드의 가장 맨 뒤에 새로운 값을 가진 노드를 추가해주시면 됩니다! 그러기 위해서는 가장 맨 뒤의 노드까지 가야 합니다.
    # 맨 뒤의 노드까지 가기 위해서는 어떻게 해야 할까요? 현재 링크드 리스트는 다음과 같다고 합니다.
    # head
    # [3] → [5] → [6] → [8]
    # 바로, head 를 따라서 계속 이동해야 합니다! head 를 변경시킬 수는 없으니, cur 이라는 변수를 이용해볼게요
    # cur
    # [3] → [5] → [6] → [8] : cur = cur.next 을 하면 다음과 같이 한 칸 이동합니다.
    #       cur
    # [3] → [5] → [6] → [8] : cur = cur.next 또 하면?
    #             cur
    # [3] → [5] → [6] → [8]
    # 이걸 언제까지 반복할까요? 맨 뒤의 노드까지 라는 소리는 cur.next 가 None 이라는 것을 의미합니다.
    # 맨 마지막 노드는 다음 노드가 없으니까 아무것도 가리키지 않을테니까요!

    def append(self, data):
        cur = self.head
        while cur.next is not None:  # cur의 댜음이 끝에 갈 때까지 이
            cur = cur.next
        cur.next = Node(data)

    # linked_list = LinkedList(5)
    # linked_list.append(12) :
    # 이렇게 되면 5 -> 12 형태로 노드를 연결한 겁니다!
    # linked_list.append(8)
    # 이렇게 되면 5 -> 12 -> 8 형태로 노드를 연결한 겁니다!

    # 링크드 리스트 모든 원소 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


Linked_List = LinkedList(3)

Linked_List.append(4)
Linked_List.append(5)
Linked_List.print_all()


# print(Linked_List.head.data)
