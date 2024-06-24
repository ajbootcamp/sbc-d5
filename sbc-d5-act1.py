queue = []

while len(queue) < 5:
    stack = str(input("Please Enter a Number: "))
    queue.append(stack)

while True:
    user = int(input("1 - Add, 2 - Naa, 3 - Wala, 4 - Display\nPlease Enter a Command: "))
    print(f"You Entered: {user}")
    if user == 1:
        use = input("Please Enter a Number: ")
        queue.append(use)
        print(queue)
    elif user == 2: 
        queue.pop(0)
    elif user == 3:
        queue.pop()
        print(queue)
    elif user == 4:
        print(queue) 
    else:
        print("Invalid Command")