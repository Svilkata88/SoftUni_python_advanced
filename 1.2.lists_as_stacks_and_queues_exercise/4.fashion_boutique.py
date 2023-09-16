# reading the inputs
box_of_clothes = [int(clothing_piece) for clothing_piece in input().split()]
rack_capacity = int(input())

# variables needed
racks = 0
free_space = rack_capacity

# logic
while box_of_clothes:
    if free_space >= box_of_clothes[-1]:
        free_space -= box_of_clothes.pop()
        if len(box_of_clothes) == 0:
            racks += 1
    else:
        racks += 1
        free_space = rack_capacity

# output
print(racks)