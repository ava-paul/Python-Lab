
lines = []
print("Enter lines of text. Press Enter on an empty line to finish:")
while True:
    line = input()
    if line:
        lines.append(line.upper())
    else:
        break
print("\nCapitalized lines:")
for line in lines:
    print(line)
