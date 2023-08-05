# def divide_by(a, b):
#     return a/b

# try:
#     ans = print(divide_by(40,0))
# except ZeroDivisionError as e:
#     print(e, "we cannot divide by zero")
#     print(e.__class__)
# except Exception as e:
#     print(e, "Something went wrong!")
try:
    with open('sample/test_write.txt', mode = 'w') as write_file:
         write_file.writelines(['this is a new file to write using python','\nAnother line!'])
except FileNotFoundError as e:
    print('ERROR', e)

    
# file = open('test.txt', mode='r')
# data = file.readline()
# print(data)
# file.close()

# with open('test.txt', mode = 'r') as file:
#     data = file.readline
#     print(data)
    
