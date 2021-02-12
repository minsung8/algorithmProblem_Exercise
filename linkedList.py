class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):         ## 노드 추가
        if self.head == None:       ## 리스트의 처음 노드 생성이라면
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def getDataIndex(self, data):   ## 해당 데이터 index 구하기
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1

    def insertNodeAtIndex(self, idx, node):     ## 인덱스로 노드 삽입
        curn = self.head
        prevn = None
        cur_i = 0

        if idx == 0:        ## 맨 앞에 삽입
            if self.head:       ## 리스트의 첫번째 노드가 존재한다면
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:              
            while cur_i < idx:      ## 입력된 idx까지 해당 리스트
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn
                prevn.next = node
            else:
                return -1

    def deleteAtIndex(self, idx):       ## 해당 인덱스 노드 삭제
        curn_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next

        if idx == 0:                    ## 맨 처음 노드를 삭제할 경우
            self.head = nextn
        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = curn.next
                else:
                    break
                curn_i += 1

            if curn_i == idx:
                prevn.next = nextn
            else:
                return -1
    
    def print(self):                ## 해당 리스트 출력
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)


if __name__ =="__main__":
    ll = LinkedList()
    ll.append(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))
    ll.print()

    print(ll.getDataIndex(2))

    ll.insertNodeAtIndex(1, Node(4))
    ll.print()

    ll.deleteAtIndex(1)
    ll.print()

