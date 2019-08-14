"""
It is a data structure consisting of a collection of nodes which together represent a sequence.
In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence.
This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration
"""
class Node:
    def __init__(self,data):
        self.data = data       # given data
        self.next = None       # set next to None


class Linked_List:
    def __init__(self):
        self.Head = None       # Initialize Head to none

    def insert_tail(self, data):
        if(self.Head is None): self.insert_head(data)   # If this is first node, call insert_head
        else:
            temp = self.Head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(data)

    def insert_head(self, data):
        newNode = Node(data)  # create a new node
        if self.Head != None:
            newNode.next = self.Head  # link newNode to head
        self.Head = newNode  # make NewNode as Head

    def printList(self):  # print every node data
        temp = self.Head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def delete_head(self):  # delete from head
        temp = self.Head
        if self.Head != None:
            self.Head = self.Head.next
            temp.next = None
        return temp

    def delete_tail(self):  # delete from tail
        temp = self.Head
        if self.Head != None:
            if (self.Head.next is None):  # if Head is the only Node in the Linked List
                self.Head = None
            else:
                while temp.next.next is not None:  # find the 2nd last element
                    temp = temp.next
                temp.next, temp = None, temp.next  # (2nd last element).next = None and tamp = last element
        return temp

    def isEmpty(self):
        return self.Head is None  # Return if Head is none


def main():
    A = Linked_List()
    print("Inserting 1st at Head")
    a1 = input()
    A.insert_head(a1)
    print("Inserting 2nd at Head")
    a2 = input()
    A.insert_head(a2)
    print("\nPrint List : ")
    A.printList()
    print("\nInserting 1st at Tail")
    a3 = input()
    A.insert_tail(a3)
    print("Inserting 2nd at Tail")
    a4 = input()
    A.insert_tail(a4)
    print("\nPrint List : ")
    A.printList()
    print("\nDelete Head")
    A.delete_head()
    print("Delete Tail")
    A.delete_tail()
    print("\nPrint List : ")
    A.printList()

if __name__ == '__main__':
    main()



