start_list = [123123,3,66,1,-500,-8,4,55,555,123]
#start_list = [1,2,3,4]
def bubble(list):
    change = False
    for x in range(0,len(list)-1):
        for iter in range(0,len(list)-1):
            print(iter)
            if list[iter] > list[iter+1]:
                list[iter], list[iter+1] = list[iter+1], list[iter]
                change = True
        print(list)
        if change == False: break

    #print(list)




val = bubble(start_list)

