arr = [6, 4, 5, 6, 7, 8, 5, 2, 1, 4, 9, 2, 4, 7]
k = 13

l = 0
r = 0
sum = 0
max_len = 0

while r < len(arr):
    sum += arr[r]
    
    # shrink window if sum >= k
    while sum >= k :
        sum -= arr[l]
        l += 1

    # update max length
    max_len = max(max_len, r - l + 1)
    r += 1

print(max_len)
