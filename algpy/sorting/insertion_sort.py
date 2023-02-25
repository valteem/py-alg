def insertion_sort(list_to_sort):
    print(list(range(1, len(list_to_sort))))
    for k in range(1, len(list_to_sort)):
        curr_elt = list_to_sort[k]
        print("k = " + str(k) + " curr_elt = " + str(curr_elt))
        j = k
        while(j > 0 and list_to_sort[j-1] > curr_elt):
            print(list_to_sort)
            print("j = " + str(j) + " list_to_sort[j-1] = " + str(list_to_sort[j-1]))
            list_to_sort[j] = list_to_sort[j-1]
            print(list_to_sort)
            j -= 1
        list_to_sort[j] = curr_elt
        print(list_to_sort) 
