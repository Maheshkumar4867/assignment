def findTriplets(arr, n):
    found_value = False
    for i in range(n - 1):


        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found_value = True
            else:
                s.add(arr[j])



arr = list(map(int,input().split()))
n = len(arr)
findTriplets(arr, n)