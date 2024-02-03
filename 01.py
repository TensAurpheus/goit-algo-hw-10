import pulp as plp

prob = plp.LpProblem("Beverages", plp.LpMaximize)

x1 = plp.LpVariable("Lemonade", 0, None, cat=plp.LpInteger)
x2 = plp.LpVariable("Juice", 0, None, cat=plp.LpInteger)

prob += x1 + x2, "Quantity"

prob += 2 * x1 + x2 <= 100, "Water"
prob += x1 <= 50, "Sugar"
prob += x1 <= 30, "Lemon juice"
prob += 2 * x2 <= 40, "Fruit puree"

prob.solve()
print(f"Status: {plp.LpStatus[prob.status]}")
print(f"Lemonade = {plp.value(x1)}")  # x1.varValue
print(f"Juice = {plp.value(x2)}")
print(f"Total = {plp.value(prob.objective)}")