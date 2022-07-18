import re

f = open("file.txt", "r")
count = 0

for line in f:
    if re.search("ABC", line):
        print(f"X | {line}", end="")

    elif re.search("```", line):
        if count >= 1:
            break
        print(f"{line}", end="")
        count += 1
        
    else:
        print(f"0 | {line}", end="")
