# 한쪽 끝으로 자료를 넣고, 반대쪽에서는 자료를 뺄 수 있는 선형구조 : First In First Out (FIFO)
# 놀이기구

# 순서대로 처리되어야 하는 일에 필요하기 때문.
# 주문이 들어왔을 때 먼저 들어온 순서대로 처리해야 할 때, 혹은 먼저 해야 하는 일들을 저장하고 싶을 때.
# 스택과 다르게 큐는 끝과 시작의 노드를 전부 가지고 있어야 하므로, self.head 와 self.tail 을 가지고 시작 !

# enqueue(data) : 맨 뒤에 데이터 추가하기
# dequeue() : 맨 앞의 데이터 뽑기
# peek() : 맨 앞의 데이터 보기
# isEmpty(): 큐가 비었는지 안 비었는지 여부 반환해주기

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():                 # 만약 비어있다면,
            self.head = new_node            # head 에 new_node를
            self.tail = new_node            # tail 에 new_node를 넣어준다.
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"        # 만약 비어있다면 에러!

        delete_head = self.head             # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next          # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.

        return delete_head.data             # 그리고 제거할 node 반환

    def peek(self):
        if self.is_empty():
            return "Queue is empty!"

        return self.head.data

    def is_empty(self):
        return self.list.head is None