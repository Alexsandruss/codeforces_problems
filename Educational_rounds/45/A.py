n, m, a, b = map(int, input().split())
reminder = n % m
remove_cost = reminder*b
add_cost = (m-reminder)*a
if remove_cost < add_cost:
    print(remove_cost)
else:
    print(add_cost)