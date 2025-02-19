people = []

for n in range(30):
    people.append({
        "id": n,
        "age": 0
    })

print(f"first 5: {people[:5]}")
print(f"total: {len(people)}")
