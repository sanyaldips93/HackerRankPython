def merge_the_tools(string, k):
    if(len(string)%k != 0):
        exit()
    else:
        L = []
        for i in range(0, len(string), k):
            L.append(''.join(list(dict.fromkeys(string[i:i+k]))))
        print('\n'.join(L))

if __name__ == '__main__':

    string, k = input(), int(input())
    merge_the_tools(string, k)


# S, N = input(), int(input())
# for part in zip(*[iter(S)] * N):
# asterisk unpacks a list. Example: print(*[1,2,3,4]) = print(1,2,3,4)
# [iter(s)]*n makes a list of n times the same iterator for s.
# Example: [[iter(s)]*3] = ([iter(s), iter(s), iter(s)])
# if s = 'abcdefghi', then zip(*[iter(s)]*3) will have the following effect:
# a,b,c,d,e,f,g,h,i  a,b,c,d,e,f,g,h,i  a,b,c,d,e,f,g,h,i
# ^                    ^                    ^
#       ^                    ^                    ^
#             ^                    ^                    ^
#     d = dict()
#     print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

