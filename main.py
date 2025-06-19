

print("*"*25)
print("Welcome TODO LIST !")
print("*"*25)
from root import options,  list_task
a=100
task= [
    { 'task' : "reading" , 'done' : False,}
    ] 
while(a!=99):
    options()
    a=int(input("Select option = "))
    if(a==1):
        print("-"*25)
        list_task(task)
        print("-"*25)
    elif(a==2):
        b = input("Enter task=")
        task.append({'task':b ,'done': False})
        list_task(task)
        print("-"*25)
        
    elif(a==3):
        b = int(input("Enter task id to Delete task="))
        task.pop(b)
        list_task(task)
    elif(a==4):
        b =int(input("Enter task id to complete="))
        task[b]['done'] = True
        list_task(task)
    else:
        print("Exit")
    
        

    




