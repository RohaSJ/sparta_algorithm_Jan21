class MaxHeap:
    def __init__(self):
        self.items = [None]

        # 새 노드를 맨 끝에 추가한다.
        # 지금 넣은 새 노드를 부모와 비교한다. 만약 부모보다 크다면 교체한다.
        # 이 과정을 꼭대기까지 반복한다.

    def insert(self, value):

        self.items.append(value)
        cur_index = len(self.items) - 1  # 인덱스를 알아야지 비교하면서 올라갈 수 있

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]: # 부모값보다 크다
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break



max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
