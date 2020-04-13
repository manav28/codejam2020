def get_answer(n):
    if n <= 30:
        for row in range(1, n+1):
            print(row, 1)
        return
    n -= 30
    left = True
    row = 1
    end = 30
    while n:
        if n & 1:
            if left:
                for col in range(1, row+1):
                    print(row, col)
            else:
                for col in range(row, 0, -1):
                    print(row, col)
            left ^= True
        else:
            end -= 1
            if left:
                print(row, 1)
            else:
                print(row, row)
        n >>= 1
        row += 1
    for r in range(row, row+end):
        if left:
            print(r, 1)
        else:
            print(r, r)
    
tests = int(input())
for x in range(1, tests+1):
    N = int(input())
    print("Case #{}:".format(x))
    get_answer(N)