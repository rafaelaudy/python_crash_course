numbers = tuple(range(5))

for n in numbers:
    if (n == 2) or (n == 3):
        print("2 or 3")    
    elif n == 4:
        print("four")    
    else:
        print(n)

print(f"\nis 3 in numbers {3 in numbers}")
print(f"5 is not in numbers {5 not in numbers}")

empty_list = []
if empty_list:
    print("list has something")
else: 
    print("\nlist is empty")

if 1 in numbers:
    print("\n1 contained in numbers")