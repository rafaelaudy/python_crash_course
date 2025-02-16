magicians = ['alice', 'david', 'carolina']
for magician in sorted(magicians):
    print(f"magician: {magician.title()}")
    print("inside loop... \n")

print(f"outside!")


for number in range(1, 5):
    print(number)

for number in range(5):
    print(number)

print(list(range(5)))

even_numbers = list(range(2, 11, 2))
print(f"even numbers: {even_numbers}")


squares = []
for number in range(1,11): 
    squares.append(number**2)

print(squares)
print(f"min: {min(squares)}")
print(f"max: {max(squares)}")
print(f"sum: {sum(squares)}")