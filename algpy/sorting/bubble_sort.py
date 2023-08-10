def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    flag_already_sorted = True
    for k in range(n):
#        print("k =", k)
        for j in range(n - k - 1):
#            print("j =", j)
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j],list_to_sort[j+1] = list_to_sort[j+1],list_to_sort[j]
#                print(list_to_sort)
                flag_already_sorted = False
        if flag_already_sorted:
            break
