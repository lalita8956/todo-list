def options():
    print("1.List all task")
    print("2.Add to task")
    print("3.Delete a task")
    print("4.Mark as task Complete")
    print("99. Exit")
    print("-"*25)

def list_task(task):
    for i in task:
        if i['done']:
            print(task.index(i),i['task'] ,"------>", "Complete")
        else:
            print(task.index(i),i['task'] ,"------>", "InComplete")
            
        
