
import cvxpy as cp

# Decision variables
X = cp.Variable((7, 3), boolean=True)

# Train costs and capacities
cost = [[100, 110, 120], [110, 120, 125], [100, 115, 125],
        [150, 155, 165], [105, 120, 115], [130, 140, 145], [135, 145, 150]]
capacity = [[50, 50, 50], [60, 60, 60], [55, 55, 55],
            [70, 60, 65], [55, 40, 50], [60, 55, 60], [60, 55, 60]]

# Objective function
z = sum(cost[i][j] * X[i, j] for i in range(7) for j in range(3)) + \
    2 * sum(3 * 580 - sum(capacity[i][j] * X[i, j] for i in range(7)) for j in range(3))

# Constraints
constraints = []

# At least 5 trains must be in operation every hour
for j in range(3):
    constraints.append(cp.sum(X[:, j]) == 5)

# At least one train from Series A must be replaced each hour
for j in range(3):
    constraints.append(cp.sum(X[0:3, j]) <= 2)

# Each Series A train's working time must not exceed 2 hours
for i in range(3):
    constraints.append(cp.sum(X[i, :]) <= 2)

# The passenger demand of at least 250 people must be guaranteed every hour
for j in range(3):
    constraints.append(sum(capacity[i][j] * X[i, j] for i in range(7)) >= 250)

# Define and solve the problem
problem = cp.Problem(cp.Minimize(z), constraints)
problem.solve()

# Output results
print("Optimal value: ", problem.value)
for i in range(7):
    for j in range(3):
        print(f"X{i+1},{j+1} = {X[i, j].value}")
