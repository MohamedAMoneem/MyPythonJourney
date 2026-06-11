#this code is about tasks

done_task = []
task = input("Add your tasks with comma in between: ").split(", ")
for tasks in task:
    print(tasks)
    answer = input("did you finish this task? yes/no : ").lower()
    if answer == "yes":
        done_task.append(tasks)
        task.remove(tasks)
    else:
        print("try to do it as soon as possible")
answer2 = input("do you want to see your progress? yes/no : ").lower()
if answer2 == "yes":
    print(f"done tasks:\n{done_task}")
    print(f"ongoing tasks: {task}")

