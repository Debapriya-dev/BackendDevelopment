# my_list = [1,2,3]

# def add_to_list(item):
#     return my_list.append(item)

# add_to_list(4)
# print(my_list)

# #Let's change it in pure function.

# my_list = [1,2,3]

# def add_to_list(list, item):
#     new_list = list.copy
#     new_list.append(item)
#     return list

# new_list = add_to_list(my_list, 4)
# print(my_list)
# print(new_list)

#Le t's change it in pure function.

# str[start: stop: step]
# start and stop index and step is the jump or hop
trial = 'reversal'
new_trial = trial[::-1] #slice function
print(new_trial)

#string reversal with recursion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        print('string_reverse(str[1:] :: ',str[1:])
        print(' str[0]:: ', str[0]) 
        return string_reverse(str[1:]) + str[0]
    
str = 'care'
reversed = string_reverse(str)
print(reversed) 