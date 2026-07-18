import sys
num_of_tasks = 0
tasks = []
def main():
    while True:
        try:
            user_input = input(menu()).split()[0].lower()
            if user_input not in ["a", "b", "c", "d"]:
                raise ValueError()
            elif user_input == "a":
                a()
            elif user_input == "b":
                b()
            elif user_input =="c":
                c()
            else:
                sys.exit()
        except Exception:
            print("please input valid choies")
    
    
    
def menu():
    return """What do you want to do?
(please input a, b, c or d)
a. View Tasks
b. Add Task
c. Delete Task
d. Exit\n"""
          
def a():
    global num_of_tasks, tasks
    if num_of_tasks == 0:
        print("there is no tasks rn")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def b():
    while True:       
        try:
            task = input("add task\n")
            if not task:
                raise ValueError()
            tasks.append(task)
            num_of_tasks += 1
        except Exception:
            ...

def c():
    ...

if __name__ == "__main__":
    main()