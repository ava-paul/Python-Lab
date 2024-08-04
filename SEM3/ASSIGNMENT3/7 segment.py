def print_segment(digit, size):
    # Define which segments are lit for each digit
    segments = {
        '0': [0, 1, 2, 4, 5, 6],
        '1': [2, 5],
        '2': [0, 2, 3, 4, 6],
        '3': [0, 2, 3, 5, 6],
        '4': [1, 2, 3, 5],
        '5': [0, 1, 3, 5, 6],
        '6': [0, 1, 3, 4, 5, 6],
        '7': [0, 2, 5],
        '8': [0, 1, 2, 3, 4, 5, 6],
        '9': [0, 1, 2, 3, 5, 6]
    }
    
    # Initialize the 8-segment display with empty spaces
    display = [' ' * (size + 2) for _ in range(2 * size + 3)]
    
    # Turn on the appropriate segments for the digit
    if 0 in segments[digit]:
        display[0] = ' ' + '-' * size + ' '
    if 1 in segments[digit]:
        for i in range(1, size + 1):
            display[i] = '|' + ' ' * size + '|'
    if 2 in segments[digit]:
        for i in range(1, size + 1):
            display[i] = ' ' * (size + 1) + '|'
    if 3 in segments[digit]:
        display[size + 1] = ' ' + '-' * size + ' '
    if 4 in segments[digit]:
        for i in range(size + 2, 2 * size + 2):
            display[i] = '|' + ' ' * size + '|'
    if 5 in segments[digit]:
        for i in range(size + 2, 2 * size + 2):
            display[i] = '|' + ' ' * (size + 1)
    if 6 in segments[digit]:
        display[2 * size + 2] = ' ' + '-' * size + ' '
    
    return display

def print_number(number, size):
    digits = str(number)
    # Initialize an empty display for the number
    display = ['' for _ in range(2 * size + 3)]
    
    # Construct the display for each digit and append it to the final display
    for digit in digits:
        segment_display = print_segment(digit, size)
        for i in range(2 * size + 3):
            display[i] += segment_display[i] + ' '
    
    # Print the final display
    for line in display:
        print(line)

# Taking user input
number = input("Enter the number: ")
size = int(input("Enter the size N: "))

# Print the number as an 8-segment display
print_number(number, size)
