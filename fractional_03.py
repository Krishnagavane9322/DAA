def fractional_knapsack():
  n = int(input("Enter number of items: "))

  weights = []

  values = []

  for i in range(n):
    w = float(input(f"Enter weight of item {i+1}: "))
    v = float(input(f"Enter value of item {i+1}: "))
    weights.append(w)
    values.append(v)

  capacity = float(input("Enter total capacity of knapsack: "))

  res = 0

  for pair in sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True):
    if capacity <= 0:
      break
    if pair[0] > capacity:
      res += capacity * (pair[1]/pair[0])
      capacity = 0
    else:
      res += pair[1]
      capacity -= pair[0]

  print("Maximum value that can be obtained:", res)

if __name__ == "__main__":
  fractional_knapsack()
