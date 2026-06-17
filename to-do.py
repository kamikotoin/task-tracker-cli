import json


class TodoList: 
    def __init__(self):
        with open("tasks.json", "r") as f:
            content = f.read()
            if not content:  # file exists but is empty
                self.tasks = []
                return
            self.tasks = json.loads(content)

    def add_task (self, task):
        self.tasks.append({"task":task, "check":False})

    def find_task(self, task):
        if len(self.tasks)==0:
            print("List is empty, add first")
            return None
        for i in range(len(self.tasks)):
            task = task.lower()
            if self.tasks[i]["task"].lower() == task:
                return i
        return None

    def check_task(self, task):
        # if len(self.tasks)==0:
        #     print("List is empty, add first")
        #     return None
        i=self.find_task(task)
        if i == None:
            print("couldnt find, try again")
            return None
        if self.tasks[i]["check"] == False:
            self.tasks[i]["check"] = True
        else:
            self.tasks[i]["check"] = False

    def delete_task(self, task):
        # if len(self.tasks)==0:
        #     print("List is empty, add first")
        #     return None        
        i=self.find_task(task)
        if i != None:
            self.tasks.pop(i)
            return None
        print("Sorry, couldnt find such task, maybe try again ")
    
    def print_tasks(self):
        if len(self.tasks)==0:
            print("List is empty, add first")
            return None        
        for i in range(len(self.tasks)):
            if self.tasks[i]["check"]:
                print(f"{i+1}.[✅]{self.tasks[i]["task"]}")
            else:
                print(f"{i+1}.[ ]{self.tasks[i]["task"]}")

working = True
print("Welcome to-do list small code")
my_list = TodoList()
while working:
    print("Main menu:\n 1.print list\n 2.add task \n 3.check the task\n 4.delete task\n 0 Exit programm")
    choice = int(input("Choose option:"))
    match choice:
        case 0:
            working = False
            with open("tasks.json", "w") as f:
                json.dump(my_list.tasks, f)
            print("Good luck! Have fun! Dont die!")
        case 1:
            my_list.print_tasks()
        case 2:
            choice = input("Enter your task: ")
            my_list.add_task(choice)
        case 3:
            my_list.print_tasks()
            choice = input("Choose task to check it: ")
            my_list.check_task(choice)
        case 4:
            my_list.print_tasks()
            choice = input("Choose task to delete it: ")
            my_list.delete_task(choice)
        case _:
            print("\nHah, nice Try\n")