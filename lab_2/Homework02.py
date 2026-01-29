# TAMU GIS Programming - Homework 02
# Name: Anjan Tiwari
# Part 1 , Part 2 and Part 3
# Part 1 (30 pt)
# Multiply all list items together
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

product = 1
for n in part1:
    product = product * n

print("Part 1 product =", product)


# Part 2 (30 pt)
# Add all list items together
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

total = 0
for n in part2:
    total = total + n

print("Part 2 sum =", total)
# Part 3 (40 pt)
# Add only the EVEN numbers in the list
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]

even_sum = 0
for num in part3:
    if num % 2 == 0:      # if remainder is 0, it's even
        even_sum = even_sum + num

print("Part 3 even sum =", even_sum)
