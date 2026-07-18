import sys
num_of_tasks = 0
tasks = []
def main():
    while True:
        try:
            user_input = input(menu()).strip().lower()
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
        except ValueError:
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
        print("there is no tasks rn\n")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

def b():
    global num_of_tasks, tasks
    while True:       
        try:
            task = input("add task\n").strip()
            if not task:
                raise ValueError()
            tasks.append(task)
            num_of_tasks += 1
            break
        except Exception:
            ...

def c():
    global num_of_tasks, tasks
    while True:       
        try:
            if num_of_tasks == 0:
                print("there in no tasks to delete \n")
                break
            elif num_of_tasks == 1:
                task = int(input(f"""which one u want to delete?
                         (input 1 to delete the only task you have)"""))
                if not (1 <= task <= num_of_tasks):
                    raise ValueError()
            else:    
                task = int(input(f"""which one u want to delete?
                             input from 1 : {num_of_tasks}"""))
                if not (1 <= task <= num_of_tasks):
                    raise ValueError()
            tasks.pop((task - 1))
            num_of_tasks -= 1
            break
        except ValueError:
            print("please enter valid task")
    

if __name__ == "__main__":
    main()