arr = list(map(int, input().split()))
arr.sort()
maxi = max(arr)
for i in range(len(arr)):
    print(arr[i])
    if maxi == arr[i]:
        maxi = arr[i-1]
        print(maxi)



