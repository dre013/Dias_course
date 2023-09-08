def knapsack(v, w, n, W):
    if W < 0:
        return 0
    
    if n < 0 or W == 0 :
        return 0

    include =v[n]+ knapsack(v, w, n - 1, W - w[n])

    exclude = knapsack(v, w, n - 1, W)

    return max(include, exclude)


v = [20, 5, 10, 40, 15, 25]
w = [1,2,3,8,7,4]

W = 10

print('Knapsack value is', knapsack(v, w, len(v) - 1, W))