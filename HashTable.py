

class HashTable:

    def __init__(self):


    def find_slot(self, key):
        #key 값이 있으면 slot 번호 리턴
        #key 값이 없다면 key값이 삽입될 slot 번호 리턴
        i = f(key)
        start = i

        while(HashTable[i] == occupied) and (HashTable[i].key != key):
            i = (i + 1) % m  #다음칸 % m -> 가장 마지막 slot일 경우, (%slot갯수) 를 해주어 다시 0번째 slot으로 간다

            if i == start: #slot 칸들이 모두 차있는데, 내가 원하는 key값이 아닌 경우
                return "FULL"
        return i

    #삽입연산
    def set(self, key, value = None):
        i = find_slot(key)  # i == i or i == "FULL"
        if i == "FULL":  #꽉 차있는 경우 -> H 사이즈를 키운다
            return None
        if HashTable[i] == occupied:
            HashTable[i].value = value
        else:
            HashTable[i].key = key
            HashTable[i].value = value
        return key

    #탐색연산
    def search(self, key):
        i = find_slot(key)
        if i == "FULL":
            return None
        if HashTable[i] == occupied:
            return True
        else:
            return None

    #삭제연산
    def remove(self, key):
        i = find_slot(key)
        if HashTable[i] != occupied:  #slot에 값이 없는 경우
            return None
        j = i  #HashTable[i]은 빈 slot. HashTable[j]은 이사해야할 slot.

        while True:
            HashTable[i] == None
            while True:
                j = (j + 1)%m
                if HashTable[j] != occupied:
                    return key
                k = f(HashTable[j].key)
                if (k < i <= j):
                    break
            HashTable[i] = HashTable[j]
        i = j
