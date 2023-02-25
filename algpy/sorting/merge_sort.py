def merge_lists(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    index1, index2,  = 0, 0
    list_merge = []
    while (len(list_merge) < len(list1) + len(list2)):
        print(list1[index1],list2[index2])
        if list1[index1] <= list2[index2]:
            list_merge.append(list1[index1])
            index1 += 1
        else:
            list_merge.append(list2[index2])
            index2 += 1
        print(list_merge)
        if index1 == len(list1):
            list_merge += list2[index2:]
            print("index1 full",list_merge)
            break
        if index2 == len(list2):
            list_merge += list1[index1:]
            print("index2 full", list_merge)
            break
    return list_merge
    

def merge_sort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort #nothing to sort here
    len_half = len(list_to_sort) // 2
    list1 = list_to_sort[:len_half]
    list2 = list_to_sort[len_half:]
    print(list1, list2)
    return(merge_lists(merge_sort(list1), merge_sort(list2)))
