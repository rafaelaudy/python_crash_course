list = ['one', 'two', 'three', 'four', 'five']
print(list)
print(list[0])
print(list[0].title())
print(list[-1])
print(list[-2])

list.append('six')
list.insert(0, 'zero')

print(list)

del list[0]
last = list.pop()
first = list.pop(0)

print(first, list, last)

list.append('to remove')
list.append('to remove')
list.remove('to remove')
print(list)
list.remove('to remove')
print(list)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)

print(f"mutated sort {cars}")
print(f"sort without mutation {sorted(cars)}")

cars.reverse
print(f"reverse {cars}")
print(f"len {len(cars)}")



