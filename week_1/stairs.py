import sys
digit_string = sys.argv[1]

num_of_stairs = int(digit_string)
for i in range(num_of_stairs):
    print(f'{" "*(num_of_stairs-(i + 1))}{"#"*(i + 1)}')