

class Heap:

    def __init__(self, L = []): #빈 리스트
        self.A = L
        self.make_heap()

    def __str__(self):
        return str(self.A)


    def make_heap(self, A):  #사실상 heapify_down 반복
        n = len(A)
        for k in range(n-1, -1, -1): #맨 마지막 인덱스, 0번 인덱스, -1씩 증가
            heapify_down(k, n) #heap성질을 만족하는 곳으로 보낸다  #k: 인덱스, n: heap 노드 갯수

    def heapify_down(self, k, n): #A[k]를 제자리로, n: heap 원소 갯수
        while A[k] != leaf_node:
            L = 2 * k + 1
            R = 2 * k + 2
            m = index_max(A[k], A[L], A[R]) #셋 중 큰 값
            if k != m: #지금 값이 index_max가 아니라면(자식 노드가 더 큰 값이라면)
                a = A[k]
                b = A[m]
                A[k] = b
                A[m] = a
                k = m  #지금 값이 가장 큰 값
                #즉, A[k] <-> A[m]
            else: #지금 값이 가장 큰 값
                break

    def find_max(self):
        return A[0]

    def delete_max(self):



