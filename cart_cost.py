def cart_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item["price"]*item["qty"]
    return total_cost

cart=[
    {"name":"apple","price":0.3,"qty":5},
    {"name":"orange","price":0.5,"qty":4},
    {"name":"guava","price":0.8,"qty":5}
]

print(cart_total_cost(cart))