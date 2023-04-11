def Smallestonleft (arr,  n) : 
    stack = []
    result = [-1] * n
    for i in range(0,n-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result