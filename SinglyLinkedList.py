

class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):  #print(node)할 경우 출력할 문자열
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self): #generator
        v = self.head
        while v != None:
            yield v
            v = v.next

    def __str__(self):
        return "->".join(str(v) for v in self)

    def __len__(self):
        return self.size

    #삽입연산
    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = SinglyLinkedList.head
        SinglyLinkedList.head = new_node
        SinglyLinkedList.size += 1

    def pushBack(self, key):
        v = Node(key)
        if len(self) == 0:
            self.head = v
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = v
        self.size += 1


    #삭제연산
    def popFront(self):
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            del x
            self.size -= 1
            return key

    def popBack(self):
        if len(self) == 0:  #경우1: 빈 리스트인 경우
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:  #경우2: 리스트에 노드가 1개만 있는 경우
                self.head = None
            else:  #경우3: 리스트에 노드가 2개 이상인 경우
                prev.next = tail.next  #tail을 pop한다
            key = tail.key
            del tail
            self.size -= 1
            return key

    #탐색
    def search(self, key):
        v = self.head
        while v != None:
            if v.key = key:
                return v
            v = v.next
        return None

    #generator
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
        return StopIterator

    #삭제
    def remove(self, key):
        if len(self) == 0: #경우1: 빈 리스트인 경우
            return None
        else:
            v = self.head
            if v.next == None: #경우2: 노드 v가 head 노드인 경우
                popFront()
                self.size -= 1
            else: #경우3: 노트 v의 전 노드 w를 찾아 링크 수정
                w = v.prev
                w.next = v.next
                del v
                self.size -= 1
                return key
            