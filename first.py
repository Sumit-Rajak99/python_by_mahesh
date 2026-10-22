# # a=10
# # a+5
# # print(a)


# data=[1,23,6,4,5,7,8,8,9,]
# print(data)
# print(data[3])
# print(sum(data))
# print(min(data))
# print(max(data))

# data[0]=data[0]+12 
# print(data[0])


# l1 = [1, 2, -3, 4, -5, 9]

# sum_index = {}
# curr_sum = 0
# max_len = 0
# start = -1
# end = -1

# for i in range(len(l1)):
#     curr_sum += l1[i]

#     if curr_sum == 0:
#         max_len = i + 1
#         start = 0
#         end = i

#     if curr_sum in sum_index:
#         length = i - sum_index[curr_sum]
#         if length > max_len:
#             max_len = length
#             start = sum_index[curr_sum] + 1
#             end = i
#     else:
#         sum_index[curr_sum] = i

# print( max_len)

l=[1,2,3,4,5]

# for i in range(len(l)):
#     print(i,end=" ")

# for i in l:
#     print(i,end=' ')

# s=[x*x for x in range(1,6)]
# print(s)

# t=(10,20,30,40)
# for i in range(len(t)):
#     print(t[-1])
    
    
    
# for i in t:
#     print(i(3))    
    
d={
    'x':x*x for x in range(1,7)
}    
print(d)