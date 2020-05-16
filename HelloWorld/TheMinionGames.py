string = input()
length_str = len(string)
vowels = ['A', 'E', 'I', 'O', 'U']
kevsc = 0
stusc = 0
for i in range(len(string)):
    if string[i] in vowels:
        kevsc += (len(string)-i)
    else:
        stusc += (len(string)-i)

if kevsc > stusc:
    print ("Kevin", kevsc)
elif kevsc < stusc:
    print ("Stuart", stusc)
else:
    print ("Draw")


# My previous solution
#
# def minion_game(string):
#     # your code goes here
#     length_str = len(string)
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     stulist = []
#     kevlist = []
#     for i in range(0, length_str):
#         if string[i] in vowels:
#             for j in range(length_str, i+1, -1):
#                 kevlist.append(string[i]+string[i+1:j])
#             kevlist.append(string[i])
#         if string[i] not in vowels:
#             for j in range(length_str, i+1, -1):
#                 stulist.append(string[i]+string[i+1:j])
#             stulist.append(string[i])
#     if len(stulist) > len(kevlist):
#         print('Stuart'+' '+str(len(stulist)))
#     elif len(stulist) < len(kevlist):
#         print('Kevin'+' '+str(len(kevlist)))
#     else:
#         print('Draw')
#
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)