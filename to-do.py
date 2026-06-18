import sys
import json
import os

class TodoList: 
    def __init__(self):
        if not os.path.exists("tasks.json"):
                self.tasks = []
                return
        with open("tasks.json", "r") as f:
            content = f.read()
            if not content:
                self.tasks = []
                return
            self.tasks = json.loads(content)

    def add_task (self, task):
        self.tasks.append({"task":task, "check":"ToDo"})
        self.save_tasks()

    def update_task(self, task):
        if task < len(self.tasks) and task >= 0:
            self.tasks[task]["task"] = sys.argv[3]
        self.save_tasks()

    def delete_task(self, task):
        if task < len(self.tasks) and task >= 0:
            self.tasks.pop(task)
            self.save_tasks()
            return None
        print("Sorry, couldnt find such task, maybe try again ")
    
    def mark_in_progress(self, task):
        if task < len(self.tasks) and task >= 0:
            self.tasks[task]["check"] = "In-Progress"
            self.save_tasks()
        

    def mark_done(self, task):
        if task < len(self.tasks) and task >= 0:
            self.tasks[task]["check"] = "Done"
            self.save_tasks()


    def print_tasks(self):
        if len(self.tasks)==0:
            print("List is empty, add first")
            return None
        if len(sys.argv)<3:    
            for i in range(len(self.tasks)):
                print(f"{i+1})'{self.tasks[i]["task"]}' is in {self.tasks[i]["check"]} status")
        else:
            for i in range(len(self.tasks)):
                if self.tasks[i]["check"] == sys.argv[2]:
                    print(f"{i+1})'{self.tasks[i]["task"]}' is in {sys.argv[2]} status")

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f, indent=2)

my_list = TodoList()
match sys.argv[1]:
    case "add":
        my_list.add_task(sys.argv[2])
    case "update":
        my_list.update_task(int(sys.argv[2])-1)
    case "delete":
        my_list.delete_task(int(sys.argv[2])-1)
    case "mark-in-progress":
        my_list.mark_in_progress(int(sys.argv[2])-1)
    case "mark-done":
        my_list.mark_done(int(sys.argv[2])-1)
    case "list":
        my_list.print_tasks()
    case _:
        print("\nHah, nice Try\n")