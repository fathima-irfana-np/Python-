# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12

arr =  [1,2,3,4,5,6,1]
k = 3

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
