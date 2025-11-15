def solve_knapsack():
    n = int(input("Enter the number of items: "))
    val= []
    wt = []

    for i in range(n):
        v = int(input(f"Enter the value of item {i+1}: "))
        w = int(input(f"Enter the weight of item {i+1}: "))
        val.append(v)
        wt.append(w)

    W = int(input("Enter total capacity of knapsack: "))

    def knapsack(W,n):
        if n < 0 or W <= 0:
            return 0
        if wt[n] > W:
            return knapsack(W,n-1)
        else:
            return max(
                val[n] + knapsack(W-wt[n],n-1),
                knapsack(W,n-1)
            )

    print("Maximum value that can be obtained: ", knapsack(W,n-1))

if __name__ == "__main__":
    solve_knapsack()