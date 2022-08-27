

class Node:
    def __init__(self, key = None, value = None): #dummy node 생성
        self.key = key
        self.value = value
        self.next = self
        self.prev = self

    def __str__(self):
        return str(key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  #dummy node
        self.size = 0

    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
            return StopIterator

    def __str__(self):
        return "->".join(str(v) for v in self)

    def __len__(self):
        return self.size

    #splice 삽입 연산
    def splice(self, a, b, x): #a노드와 b노드 사이를 x노드 다음으로 삽입
        #기본
        ap = a.prev
        bn = b.next
        xn = x.next

        #cut -> 6개의 link를 바꾼다
        ap.next = bn
        bn.next = ap

        #insert
        x.next = a
        a.prev = x
        xn.prev = b
        b.next =

    #이동연산
    def moveAfter(self, a, x): #a노드를 x노드 다음으로 이동 (x -> a)
        splice(a, a, x)

    def moveBefore(self, a, x): #a노드를 x노드 이전으로 이동 (a -> x)
        splice(a, a, x.prev)

    #삽입연산
    def insertAfter(self, x, key): #x노드 뒤에 새 노드(key를 가짐)을 삽입 (x -> key)
        moveAfter(Node(key), x)

    def insertBefore(self, x, key): #x노드 앞에 새 노드(key를 가짐)을 삽입 (key -> x)
        moveBefore(Node(key), x)

    def pushFront(self, key):
        insertAfter(self.head, Node(key))

    def pushBack(self, key):
        insertBefore(self.head, Node(key))

    #탐색연산
    def search(self, key):
        v = self.head
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next
        return None

    #삭제연산
    def remove(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x

    def popFront(self):
        remove(head.next)

    def popBack(self):
        remove(head.prev)


    #기타연산
    def join(self, another_list):
        insertAfter(self, another_list)

    #def split(self, x):



