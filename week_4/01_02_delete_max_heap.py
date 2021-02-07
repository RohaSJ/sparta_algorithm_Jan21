# 최대 힙에서 원소를 삭제하는 방법은 최댓값, 루트 노드를 삭제하는 것
# 스택과 같이 맨 위에 있는 원소만 제거할 수 있고, 다른 위치의 노드를 삭제할 수는 없음
# 마찬가지로, 원소를 삭제할때도 힙의 규칙이 지켜져야함
# 1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
# 2. 맨 뒤에 있는 원소를 (원래 루트 노드)를 삭제한다. (반환해줘야하므로 어딘가에 저장을 해둬야함)
# 3. 변경된 노드 (원래 맨 끝에 있는 노드였기 때문에 작은 값일 것 하지만 제일 작은 값은 아)와 자식 노드들을 비교합니다.
# 3-1. 두 자식 중 더 큰 자식과 비교해서 더 크다면 자리를 바꿉니다.
# 4. 자식 노드 둘 보다 부모 노드가 크거나 가장 바닥에 도달하지 않을 때까지 3. 과정을 반복합니다.
# 5. 2에서 제거한 원래 루트 노드를 반환합니다.


class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break
# 맨 마지막 레벨의 맨 오른쪽 노드 = self.items[마지막 원소] = self.items[-1]
# 언제까지 ? 원래 마지막 노드였던 것이 자식 노드들보다 클 때 or 바닥에 닿았을 때 까지.
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1] # 맨 처음에 None 을 넣었기 때문에 루트노드가 self.items[1]이 될 수 있음.
        prev_max = self.items.pop() # pop : 제거 & 저장
        cur_index = 1 # 현재 head_node 가 1의 인덱스 이므로

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4] # 루트로드가 삭제되지 않았음
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]