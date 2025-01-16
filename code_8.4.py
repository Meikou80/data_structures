class Node:
    def __init__(self, name=""):
        self.next = None
        self.name = name

class LinkedList:
    def __init__(self):
        self.nil = Node()
        self.nil.next = self.nil
    
    #　ノードpの直後にノードvを挿入
    def insert(self, v, p=None):
        if p is None:
            p = self.nil
        v.next = p.next
        p.next = v
    
    # 連結リストの出力
    def print_list(self):
        cur = self.nil.next
        while cur != self.nil:
            print(cur.name, end=" -> ")
            cur = cur.next
        print()
    
if __name__ =="__main__":
    linked_list = LinkedList()
    names = ["tamachi", "takanawa_gateway", "shinagawa", "oosaki", "gotanda", "meguro"]
    
    for i, name in enumerate(names):
        node = Node(name)
        linked_list.insert(node)
        print(f"step {i}: ", end="")
        linked_list.print_list()