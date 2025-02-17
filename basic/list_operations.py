numbers = ['one', 'two', 'three', 'four', 'five']
print(numbers)
print(numbers[0])
print(numbers[0].title())
print(numbers[-1])
print(numbers[-2])

numbers.append('six')
numbers.insert(0, 'zero')

print(numbers)

del numbers[0]
last = numbers.pop()
first = numbers.pop(0)

print(first, numbers, last)

numbers.append('to remove')
numbers.append('to remove')
numbers.remove('to remove')
print(numbers)
numbers.remove('to remove')
print(numbers)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)

print(f"mutated sort {cars}")
print(f"sort without mutation {sorted(cars)}")

cars.reverse
print(f"reverse {cars}")
print(f"len {len(cars)}")

big_list = [v for v in range(0, 101)]
print(f"first 10: {big_list[0:10]}")
print(f"or first 10: {big_list[:10]}")
print(f"last 10: {big_list[91:]}")
print(f"set before last 10: {big_list[-15:-10]}")
print(f"second set of 5: {big_list[5:10]}")

list1 = list(range(10))
list3 = list1
print(list1)
list2 = list1[:]
list1.pop()
print(f"len list 1 {len(list1)}")
print(f"len list 2 {len(list2)}")
print(f"len list 3 {len(list3)}")
