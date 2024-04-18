from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(n1, n2, srt_lnk_lst1, srt_lnk_lst2):
        if n1.data is None and n2.data is not None:
            new_lst = DoublyLinkedList()
            while n2.data is not None:
                new_lst.add_last(n2.data)
                n2 = n2.next
        elif n1.data is not None and n2.data is None:
            new_lst = DoublyLinkedList()
            while n1.data is not None:
                new_lst.add_last(n1.data)
                n1 = n1.next
        else:
            if n1.data > n2.data:
                new_lst = merge_sublists(n1, n2.next, srt_lnk_lst1, srt_lnk_lst2)
                new_lst.add_first(n2.data)
            else:
                new_lst = merge_sublists(n1.next, n2, srt_lnk_lst1, srt_lnk_lst2)
                new_lst.add_first(n1.data)
        return new_lst
    
    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, srt_lnk_lst1, srt_lnk_lst2)

def main():
    lst1 = [1,3,5,6,8]
    lst2 = [2,3,5,10,15,18]
    lnk_lst1 = DoublyLinkedList()
    lnk_lst2 = DoublyLinkedList()
    for i in range(len(lst1)):
        lnk_lst1.add_last(lst1[i])
    for i in range(len(lst2)):
        lnk_lst2.add_last(lst2[i])
    print(lnk_lst1)
    print(lnk_lst2)
    lnk_lst3 = merge_linked_lists(lnk_lst1, lnk_lst2)
    print(lnk_lst3)

#main()