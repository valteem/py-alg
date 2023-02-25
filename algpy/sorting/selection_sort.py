def selection_sort(list_to_sort):
    for k in range(0,len(list_to_sort) - 1):
        print(list_to_sort)
        elt_min = list_to_sort[k]
        num_min = k
        print(k, elt_min)
        for j in range(k + 1, len(list_to_sort)):
            if list_to_sort[j] < elt_min:
                elt_min = list_to_sort[j]
                num_min = j
        print(num_min, elt_min)
        del list_to_sort[num_min]
        print(list_to_sort)
        list_to_sort.insert(k, elt_min)
