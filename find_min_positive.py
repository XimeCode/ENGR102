# def find_min_positive(int_list):
#     min_pos = None

#     for num in int_list:
#         if num > 0:
#             if min_pos is None or num < min_pos:
#                 min_pos = num
#     return min_pos
#         # integers = int(ints)
        
    
#     return min

# yes = find_min_positive([-3,0,4,-1,2])
# print(yes)

#mutable - object that can be freely modified - list, dictionary, set 
mutable = ['a','b','c']
mutable[1] = 'x'
print(mutable)



#immutable - tuple (cannot modify), string
string = "123" 
string[0] = 1


mutable2 = ('a','b','c')
mutable2[1] = 'x'
print(mutable)
