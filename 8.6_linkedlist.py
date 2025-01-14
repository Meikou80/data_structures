class Node:
    def __init__(self, name=""):
        self.prev = None
        self.next = None
        self.name = name

class LinkedList:
    def __init__(self):
        self.nil = Node()
        self.nil.prev = self.nil
        self.nil.next = self.nil

    #　ノードpの直後にノードvを挿入
    def insert(self, v, p=None):
        if p is None:
            p = self.nil
        v.next = p.next
        p.next.prev = v
        p.next = v
        v.prev = p

    # ノードvを削除
    def erase(self, v):
        if v == self.nil:
            return
        v.prev.next = v.next
        v.next.prev = v.prev
        
    # 連結リストの出力
    def print_list(self):
        cur = self.nil.next
        while cur != self.nil:
            print(cur.name, end=" -> ")
            cur = cur.next
        print()

if __name__ == "__main__":
    linked_list = LinkedList()
    names = ["tamachi", "takanawa_gateway", "shinagawa", "oosaki", "gotanda", "meguro"]
    
    takanawa_gateway = None
    for name in names:
        node = Node(name)
        linked_list.insert(node)
        if name == "takanawa_gateway":
            takanawa_gateway = node
            
    print("2024:", end="")
    linked_list.print_list()
    linked_list.erase(takanawa_gateway)
    print("2019:", end="")
    linked_list.print_list()