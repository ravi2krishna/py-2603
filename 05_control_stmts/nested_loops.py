# Nested Loops 

# Generate Math tables 

# 1 X 1 - 1 X 2 - 1 X 3 - 1 X 4 - 1 X 5 ......
# 2 X 1 - 2 X 2 - 2 X 3 - 2 X 4 - 2 X 5 ......
# 3 X 1 - 3 X 2 - 3 X 3 - 3 X 4 - 3 X 5 ......
# .
# .

# Nested For Loop 
for outer in range(1,4):
    print(outer)
    print("----------")
    for inner in range(1,6):
        print(inner)
        
# Math Table with for 
for outer in range(1,4):
    for inner in range(1,6):
        print(f"{outer} * {inner} = {outer * inner} ")

# real world use case of nested loops 
colors = ["black","white","red"]
sizes = ["uk-6","uk-7","uk-8","uk-9"]

for color in colors:
    for size in sizes:
        print(color+"-----"+size)
        
        
# Math Table with while 
outer = 1
while outer < 4:
    inner = 1
    while inner < 6:
        print(f"{outer} * {inner} = {outer * inner} ")
        inner += 1
    outer += 1