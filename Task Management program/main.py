tasks=[]

while True:
    print("*** TASK MANAGEMENT PROGRAM***")
    print("1.Add Task\n2.View All Tasks\n3.Update Task\n4.Mark Task as Completed\n5.Delete Task\n6.Search Task by Name:\n7.Exit")
    ch=int(input("Enter your choice:"))
    print()

    if ch==1:
        task={}

        task['name']=input("Enter the Task name:")
        task['description']=input("Enter the Task Description:")
        task['d_date']=input("Enter the Due-Date(dd-mm-yyyy):")
        task['priority']=input("Enter Task priority(High/Medium/Low):")
        task['completion']=False
        # task.append(name)
        # task.append(description)
        # task.append(d_date)
        # task.append(priority)
        # task.append(completion)

        tasks.append(task)
        print("Task Added Succesfully!!")
        print()


    elif ch==2:
         if tasks:
            #  count=1
             print("**ALL TASKS**\n")
             for i,task in enumerate(tasks,start=1):
                #  if task['completion']==True:
                #      task['completion']='Completed'
                #  else:
                #      task['completion']='Pending'
                 completion_s="Completed" if task['completion'] else "Pending"
                    
                 print(f"Task {i}")
                 print(f"Task Name: {task['name']}")
                 print(f"Task Description: {task['description']}")
                 print(f"Task Due-Date: {task['d_date']}")
                 print(f"Task Priority: {task['priority']}")
                 print(f"Task Completion: {completion_s}")
                #  count+=1
                 print()
         else:
             print("No Tasks Added!!")
             print()
            
    elif ch==3:
        name=input("Enter the Task name:")
        found=False

        for i,task in enumerate(tasks):
            if task['name']==name:
                print()
                task['name']=input("Enter New Task Name:")
                task['description']=input("Enter New Task Decription:")
                task['d_date']=input("Enter New Due-Date(dd-mm-YYYY):")
                task['priority']=input("Enter New Task Priority(High/Medium/Low):")
                print("Task Updated Successfully!!")
                found=True
                break
        if found:
            print()
            # break
        else:
            print("Task not found")
            print()

    elif ch==4:
        name=input("Enter the Task name:")
        found=False
        for i,task in enumerate(tasks):
            if task['name']==name:
                task['completion']=True
                print("Task Marked As Completed!!")
                found=True
                break
        if found:
            print()
        else:
            print("Task not Found!!")
    
    elif ch==5:
        name=input("Enter the Task name:")
        found=False

        for i,task in enumerate(tasks):
            if task['name']==name:
                del tasks[i]
                found=True
                print("Task Deleted Succesfully!!")
                break
        if found:
            print()
        else:
            print("Task not Found!!")

    elif ch==6:
        name=input("Enter the Task Name:")
        found=False
        
        for i,task in enumerate(tasks):
            if task['name']==name:
                # if task['completion']==True:
                #      task['completion']='Completed'
                # else:
                #      task['completion']='Pending'
                completion_s="Completed" if task['completion'] else "Pending"
    
                print(f"Task Name: {task['name']}")
                print(f"Task Description: {task['description']}")
                print(f"Task Due-Date: {task['d_date']}")
                print(f"Task Priority: {task['priority']}")
                print(f"Task Completion: {completion_s}")
                found=True
                break
        if found:
            print()
        else:
            print("No Task Found!!")
            print()
    elif ch==7:
        print("Exiting the program....")
        break
    else:
        print("INVALID CHOICE!!!...Try Again")


                
            

                

            
             

