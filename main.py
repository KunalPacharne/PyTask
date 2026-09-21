#sample_taskinfo_list = ["title","description","priority","status","due date","completed date","tags","notes"]
from datetime import date
task_list = []
def create_task():

    title = input("Enter title:")
    decsription = input("Enter description:")
    priority = input("Enter priority:")
    status = input("Enter status:")
    due_date = input("Enter due_date:")
    completed_date = input("Enter Completion date:")
    tags = input("Enter tags:")
    notes = input("Enter notes:")
    print("\n")
    task_infolist = [title,decsription,priority,status,due_date,completed_date,tags,notes]
    task_list.append(task_infolist)

    return task_infolist
        
class task:

    def __init__(self,taskinfo_list):
        self.title = taskinfo_list[0]
        self.description = taskinfo_list[1]
        self.priority = taskinfo_list[2]
        self.status = taskinfo_list[3]
        self.due_date = taskinfo_list[4]
        self.complete_date = taskinfo_list[5]
        self.tags = taskinfo_list[6]
        self.notes = taskinfo_list[7]

    def view_task(self,taskinfo_list):
        print(f"Title : {taskinfo_list[0]}")
        print(f"Description : {taskinfo_list[1]}")
        print(f"Priority : {taskinfo_list[2]}")
        print(f"Status : {taskinfo_list[3]}")
        print(f"Due Date : {taskinfo_list[4]}")
        print(f"Completion Date : {taskinfo_list[5]}")
        print(f"Tags : {taskinfo_list[6]}")
        print(f"Notes : {taskinfo_list[7]}")

    def update_task(self,taskinfo_list,choice_number,information):
        taskinfo_list[choice_number-1] = information

    def complete_task(self,taskinfo_list):
        taskinfo_list[5] = date.today()
        taskinfo_list[3] = "Completed"


str_menu = "1. Create Task\n2. View Tasks\n3. Update Task\n4. Complete Task\n5. Delete Task\n6. Exit"
update_menu = "1.Update Title\n2.Update Description\n3.Update Priority\n4.Update Status\n5.Update Due Date\n6.Update Tags\n7.Update Notes"
print(str_menu)
flag = True
while(flag == True):
    choice = int(input("Enter Choice:"))
    if (choice == 1):
        taskinfo = create_task()
    if (choice == 2):
        t1 = task(taskinfo)
        t1.view_task(taskinfo)
    if (choice == 3):
        print(update_menu)
        choice_update = int(input("Enter Your Choice From Above:"))
        updated_info = input("Enter new info to update:")
        t2 = task(task_list[0])
        t2.update_task(task_list[0],choice_update,updated_info)
        t2.view_task(task_list[0])
    if (choice == 4):
        t3 = task(task_list[0])
        t3.complete_task(task_list[0])
        t3.view_task(task_list[0])
    if (choice == 5):
        t4 = task(task_list[0])
        title_ask = input("Enter the title of task to delete")
        if (title_ask == task_list[0][0]):
            list_toremove = task_list[0]
            task_list.remove(list_toremove)
            t4.view_task(task_list[0])
    if (choice == 6):
        flag = False
    print("\n")
    print(str_menu)
