# def reverse_string(Str1):
#         list1 = Str1.split(" ")
#         tuple1 = tuple(list1)
#         (var1, var2, var3, var4, var5) = tuple1
#         list2 = [var5, var4, var3, var2, var1]
#         sum = ""
#         for char in list2:
#             sum += char 
#         return sum    
# print(reverse_string("a b c d e"))

# list1 = [10,5,4,3,2]

# for passnum in range(len(list1)-1, 0,-1):
#     for i in range(passnum):
#         if list1[i] > list1[i+1]:
#             var = list1[i+1]
#             list1[i+1] = list1[i]
#             list1[i] = var
            
# print(list1)

#largest = int(raw_input())

#for i in range(largest, 0):
#    for j in range(1, 20):
#        if i % j == 0:
#            print("done\n")

k = 13195

for i in range(2, k+1):
    if k%i == 0:
        print(i) 
    else:
        pass





            







