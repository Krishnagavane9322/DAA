def n_queens():
    n = int(input("Enter the number of queens: "))

    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["0"] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "1"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "0"

    backtrack(0)

    print(f"\nsolutions for {n} queens problem:\n")

    for sol in res:
        for row in sol:
            print(row)
        print()
        
if __name__ == "__main__":
    n_queens()