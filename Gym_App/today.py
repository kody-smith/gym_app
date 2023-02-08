from datetime import datetime 

# today = datetime.now()


# # Textual month, day and year	
# d2 = today.strftime("%B %d, %Y")
# print("d2 =", d2)

### Write function that can call day variable and modify it

day = 1

while True:
    if day == 1:
        print("day =", 1)
        day = 2
    elif day == 2:
        print("day =", 2)
        day = 3
    elif day == 3:
        print("day =", 3)
        day = 4
    elif day == 4:
        print("day =", 4)
        day = 5
    elif day == 5:
        print("day =", 5)
        day = 6
    elif day == 6:
        print("day =", 6)
        day = 7
    elif day == 7:
        print("day =", 7)
        day = 8
    elif day == 8:
        print("day =", 8)
        day = 1