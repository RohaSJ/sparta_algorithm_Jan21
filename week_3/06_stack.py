# 한 쪽 끝으로만 자료를 넣고 뺄 수 있는 구조 / Last In First Out / LIFO
# 넣은 순서를 쌓아두고 있기 때문에, 그 순서가 필요한 경우가 있음.

# 빨래통

# push(data) : 맨 앞에 데이터 넣기
# pop() : 맨 앞의 데이터 뽑기
# peek() : 맨 앞의 데이터 보기 (see)
# isEmpty(): 스택이 비었는지 안 비었는지 여부 반환해주기
# 스택은 데이터 넣고 뽑는 걸 자주하는 자료 구조입니다! 삽입과 삭제가 잦음 (→ 링크드리스트)

# stack = [4] 에 3을 push 하면 [3] → [4] 가 되어야 합니다! (3이 4를 가리키도록 해야함)
#
# 링크드 리스트에서 새로운 head를 지정하려면, 새로운 값을 담은 새로운 노드를 만들고,
# 그 노드의 다음 노드를 현재의 head 로 지정하고, 그 노드를 head 로 정하면 됨.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):                 # 현재 [4] 밖에 없다면
        new_head = Node(value)             # [3] 을 만들고!
        new_head.next = self.head          # [3] -> [4] 로 만든다음에
        self.head = new_head               # 현재 head의 값을 [3] 으로 바꿔준다.
        return

    def pop(self):
        if self.is_empty():                  # 만약 비어있다면 에러!
            return "Stack is empty!"
        delete_head = self.head              # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next           # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head                   # 그리고 제거할 node 반환

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.head.data

    def is_empty(self):
        return self.head is None