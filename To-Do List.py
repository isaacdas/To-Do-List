
'''
To do List project:

This is a simple program that allows you to add tasks to a task list and mark them as 'Complete' when finished.

'''


#Define Functions

def add_task(task_list, task, title="Incomplete"):
    if task not in task_list.items():
        task_list[task] = title
        print(f"{task}: added to list and marked as {title}.")

        return task_list[task]


def view_tasks(task_list):
    print("\nTasks:")
    for task, title in task_list.items():
        print(f"{task}: {"".join(title)}")

    

def mark_complete(task_list, task, title):
    if task in task_list:    
        task_list[task] = title
        print(f"\n{task} has been marked {title}")
    else:
        print(f"\n{task} not marked completed, try again (Case sensitive).")

    return task_list, task, title

def delete_task(task_list, task):
    if task in task_list:
        del task_list[task]
        print(f"\n{task} deleted.")
    else:
        print(f"{task} not deleted, try again (Case sensitive).")

#define empty task list
task_list = {

}


#Initial Welcome message
print("\nWelcome to the To-Do List App!")

#Looped user input 
while True:
    try:
        user_input = int(input('''     
Menu:
[1] Add a task
[2] View tasks
[3] Mark a task as complete
[4] Delete a task
[5] Quit 
(Key in a number): '''))
        
        if user_input == 1:
            task_input = input("\nAdd your task:")
            add_task(task_list, task_input,)
        elif user_input == 2:
            view_tasks(task_list)
        elif user_input == 3:
            mark_input = input("What task would you like to mark complete?: ")
            mark_complete(task_list, mark_input, "Complete")
        elif user_input == 4:
            delete_input = input("What task would you like to delete?: ")
            delete_task(task_list, delete_input)
        elif user_input == 5:
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid input (numbers 1-5 only please)\n")
            
    except ValueError: 
        print("\nThat is not a number")
    
    
