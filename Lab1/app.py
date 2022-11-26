import task1
import task2
import task3
import task4

while True:
    task = input("Please choose the task [1-4]: ")
    if task not in ["1","2","3","4"]:
        print("Task number should be in range 1-4!")
        continue
    print(f"You picked task {task}")
    match task:
        case "1":
            task1.run()
        case "2":
            task2.foo()
        case "3":
            task3.foo()
        case "4":
            task4.foo()
        case _:
            print("Something went wrong...")
    finish = input("Do you want to finish? [Y/N]: ").lower()
    print(finish)
    if finish == "y":
        break