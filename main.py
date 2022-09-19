class Node:
    def __init__(self, data, prev = None, next = None):
        self.item = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_emptylist(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("node inserted")
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.start_node
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.pref = temp

    def insert_before_item(self, pos, data):
        if self.head is None:
            print("List is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                if temp.item == pos:
                    break
                temp = temp.next
            if temp is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.next = temp
                new_node.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = new_node
                temp.prev = new_node

    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None;

    def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None

    def delete_element_by_value(self, pos):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            if self.head.item == pos:
                self.head = None
            else:
                print("Item not found")
            return

        if self.head.item == pos:
            self.head = self.head.next
            self.head.pref = None
            return

        temp = self.head
        while temp.next is not None:
            if temp.item == pos:
                break;
            temp = temp.next
        if temp.next is not None:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        else:
            if temp.item == pos:
                temp.pref.next = None
            else:
                print("Element not found")

    def replacement(self, index, element):
        if self.head is None:
            print("linked list is empty")
            return
        if index > (self.len_link() - 1):
            print("index is out of range")
            return
        temp = self.head
        count = 0
        while temp:
            if count == index:
                temp.item = element
                break
            temp = temp.next
            count += 1

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.item , " ")
                temp = temp.next
    def len_link(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def search_data(self, pos):
        count = 0
        temp = self.head
        while(temp != None):
            if (count == pos):
                return temp.item
            count = count + 1
            temp = temp.next
        return None

    def last_entry(self, list):
        temp = self.tail
        temp_second_list = list.tail
        index = self.len_link()
        while(temp_second_list != None):
            if (temp.item == temp_second_list.item):
                temp_second_list = temp_second_list.prev
            temp = temp.prev
            index = index - 1
        return index


    def delAll(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        while (self.head.next != None):
            if self.head.next is None:
                self.head = None
                return
            self.head = self.head.next
            self.start_prev = None
        print("The list is empty")


new_list = DoublyLinkedList()
# new_list.insert_in_emptylist(50)
# new_list.insert_at_start(10)
# new_list.insert_at_start(5)
# new_list.insert_at_start(18)
# new_list.insert_at_start(3)
new_list.insert_in_emptylist(2)
new_list.insert_at_start(1)
new_list.insert_at_start(2)
new_list.insert_at_start(1)
new_list.insert_at_start(2)
new_list.insert_at_start(1)
new_list.traverse_list()
print("First list")


# list12 = DoublyLinkedList()
# list12.insert_in_emptylist(2)
# list12.insert_at_start(1)

# print ("Second list")
# list12.traverse_list()

# print("after all")
# new_list.delAll()
# print("after")
# print(new_list.delAll())
# new_list.insert_before_item(18,50)
# new_list.traverse_list()
# print("Number of elements in the list")
# print("counter")
# print(new_list.len_link())

# print("The last entry is")
# thelast = new_list.last_entry(list12)
# print(thelast)
#
# print(new_list.search_data(5))
# new_list.reverse_el(1,2)
# print("after reverse")
#
# print(new_list.replacement(5,3))
# new_list.traverse_list()

# print(new_list.replacement(2))