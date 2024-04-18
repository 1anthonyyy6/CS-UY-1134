from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    copy_lst = DoublyLinkedList()
    for i in lnk_lst:
        copy_lst.add_last(i)
    return copy_lst

def deep_copy_linked_list(lnk_lst):
    copy_lst = DoublyLinkedList()
    for i in lnk_lst:
        if isinstance(i, int):
            copy_lst.add_last(i)
        else:
            copy_lst.add_last(deep_copy_linked_list(i))
    return copy_lst

def main():
    lnk_lst = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst.add_last(elem1)
    elem2 = 3
    lnk_lst.add_last(elem2)
    lnk_lst2 = deep_copy_linked_list(lnk_lst)
    e1 = lnk_lst.header.next
    e1_1 = e1.data.header.next
    e1_1.data = 10

    e2 = lnk_lst2.header.next
    e2_1 = e2.data.header.next
    print(e2_1.data)

#main()