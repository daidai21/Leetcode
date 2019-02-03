def eight_queen_question(arr=[None] * 8, n=0):
    if n == len(arr):
        print(arr)
        return 0
    for col in range(len(arr)):
        arr[n], flag = col, True
        for row in range(n):
            if arr[row] == col or abs(col - arr[row]) == n - row:
                flag = False
                break
        if flag:
            eight_queen_question(arr, n+1)


print(eight_queen_question())
