# Node 구현
class Node:
    def __init__(self, value, next):
        self.value = value
        self.value = next

# 링크드 리스트 구현
'''링크드 리스트는 Node 클래스, head, 그리고 current 개념으로 이루어진다.'''
class LinkedList(object):
    def __init__(self):
        self.head = None
    
    # 링크드리스트에 값 추가하기
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        
        else:
            current = self.head
            while(current.next): # current.next = None 이면 실행되지 않음.
                current = current.next
            current.next = new_node 

    # 링크드리스트에서 특정 인덱스에 위치한 값 꺼내기
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    
    # 특정 인덱스에 값 삽입하기
    def insert_at(self, idx, value):
        current = self.head
        new_node = Node(value)
        for _ in range(idx-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # 특정 인덱스에 위치한 값 삭제하기
    def remove(self, idx):
        current = self.head
        for _ in range(idx-1):
            current = current.next
        current.next = current.next.next

            

# 링크드 리스트 객체 생성
ll = LinkedList() 
'''
리스트 안에 어떤 노드도 없으니 
head는 none의 값을 가짐
ll.head = None
'''

# 이 링크드 리스트에 1의 값이 담긴 노드를 추가(생성)함.
ll.append(1)
'''
14행: new_node는 Node(1)이 생성됨과 동시에 참조함.
15 ~ 16행: ll.head = None 이므로 ll.head = new_node(=Node(1)) 임.
'''

# 그리고 링크드 리스트에 2의 값이 담긴 노드를 추가함.
ll.append(2)
'''
14행: new_node = Node(2)로 업데이트 됨.
15 ~ 16행: ll.head = Node(1) 이므로, else 구문으로 실행됨.
19행: current = ll.head(=Node(1)) 로 정의됨.
20행: current.next, 즉 Node(1).next가 None(False)이므로 실행되지 않음
22행: current.next = new_node가 됨. 즉 Node(1).next = Node(2)로 업데이트 됨.
'''

# 마지막으로 링크드 리스트에 3의 값이 담긴 노드를 추가함.
ll.append(3)
'''
14행 : new_node = Node(3)로 업데이트 됨.
15 ~ 16행: ll.head = Node(1) 이므로, else 구문으로 실행됨.
19행: current = Node(1) 임. head값이 Node(1) 이기 때문.
20행: current.next, 즉 Node(1).next = Node(2) (True) 이므로 실행됨.
21행: current 값이 current의 다음값으로 새롭게 정의됨. current = Node(2)
20 ~ 21행: current.next(Node(2).next)가 현재 None이므로, 실행 안됨.
22행: current.next = new_node가 됨. 즉 Node(2).next = Node(3)로 업데이트 됨.
'''