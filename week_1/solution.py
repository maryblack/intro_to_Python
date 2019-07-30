import sys
digit_string = sys.argv[1]

def sum_in_str(input_str):
    sum = 0
    for symbol in input_str:
        if symbol.isdigit():
            sum += int(symbol)

    return sum

if __name__=="__main__":
    print(sum_in_str(digit_string))