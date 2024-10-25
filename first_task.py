import time

print("Welcome!")
print("Your task defines you.")

tasks = []

while True:
    c = input("\nEnter 'exit' to stop the loop or press Enter to continue: ")
    if c == 'exit':
        break

    y = input("Enter your tasks separated by commas (at least four tasks):\n")
    tasks = [task.strip() for task in y.split(",")]
    
    if len(tasks) < 4:
        print("Please enter at least four tasks.")
        continue
    
    print("\nYour daily tasks are", tasks)

    while tasks:
        for i in range(len(tasks)):
            x = input(f"\nHave you completed the task '{tasks[i]}'? (Enter '1' for Yes, or 'exit' to quit): ")
            if x == 'exit':
                print("Exiting the application.")
                exit()
            
            if x == '1':
                print(f"You have successfully completed the task: '{tasks[i]}'")
                tasks.pop(i)
                time.sleep(1)
                break
            else:
                print("You should try to complete the task.")
                time.sleep(1)
        
        if tasks:
            print("Remaining tasks are:", tasks)
        else:
            print("All tasks completed! Great job!")
            break
