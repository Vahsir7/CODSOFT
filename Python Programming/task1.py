#TO DO list
class Task:
    '''
    This class hosts the task object of the to do list
    Each task has a name, start date time, due date time and duration(which is calculated)
    '''
    def __init__(self, name, due):
        self.__name = name
        self.__due = due
        #self.__duration = self.__due - self.__start
    
    def get_name(self):
        return self.__name
    
    
    def get_due(self):
        return self.__due
    
    def set_name(self, name):
        self.__name = name
    
    def set_due(self, due):
        self.__due = due
        #self.__duration = self.__due - self.__start
    
def display(tasks):
    if tasks == []:
        print("Great job there are no tasks left!")
        return False
    print("id\t\t|Name\t\t|due")
    id = 1
    for task in tasks:
        print(f"{id}\t\t|{task.get_name()}\t\t|{task.get_due()}")
        id += 1

def check(due):
    if '/' in due:
        due=due.split('/')
    elif '-' in due:
        due=due.split('-')
    elif '.' in due:
        due=due.split('.')
    elif ' ' in due:
        due=due.split(' ')
    else:
        return False
    print(due)
    date = due[0]
    if len(date) != 2:
        
        date = '0' + date
    month = due[1]
    if len(month) != 2:
        month = '0' + month
    year = due[2]
    if len(year) != 4:
        year = '20' + year
    print(date,month,year)
    due = date + '/' + month + '/' + year
    print(due)
    if len(due) != 10:
        return False
    return due

tasks = []
displaying_tasks = True
#main
if __name__ == "__main__":
    while(True):
        print("Welcome to the TO DO list")
        print("Please select an option")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Finish a task")
        print("4. Exit")
        option = input("Enter your choice: ")
        if option == '1': #Add a task
            print("Enter the task name")
            name = input()
            print("Enter the due date in the format 'dd/mm/yyyy'")
            
            due = input()
            due = check(due)
            if due == False:
                print("Invalid date format")
                continue
            print(name, due)
            task = Task(name, due)
            tasks.append(task)

        elif option == '2': #View tasks
            print("Tasks:")
            displaying_tasks = display(tasks)
            print("----------------------------------------------")
            if displaying_tasks == False:
                displaying_tasks = True
                continue
            option2 = None
            while option2!='m' or option2!='M':
                print("Press U to update a task or M to return to the main menu")
                option2 = input("Enter your choice: ")
                if option2 == 'U' or option2=='u':
                    try:
                        id = int(input("Enter the task number to update :"))
                        tasks = [tasks[id-1]]
                        print("task")
                        option3 = 0
                        while(option3 != 3):
                            print("----------------------------------------------")
                            print("Current updation Task details")
                            print("----------------------------------------------")
                            #print("id\t\t|Name\t\t|due")
                            #print(f"{id}\t\t|{task.get_name()}\t\t|{task.get_due()}")
                            display(tasks)
                            print("----------------------------------------------")
                            print("What to edit:")
                            print("1. Name")
                            print("2. due date")
                            print('3. Exit')
                            option3 = input("Enter your choice: ")
                            if option3 == '1':
                                name = input("Enter the new name: ")
                                task.set_name(name)
                            elif option3 == '2':
                                due = input("Enter the new due date in the format 'dd/mm/yyyy': ")
                                task.set_due(due)
                            elif option3 == '3':
                                break
                            else:
                                print("Invalid option")
                                continue
                    except ValueError:
                        print("Invalid task number")
                        continue
                elif option2 == 'M' or option2=='m':
                    break
                
                else:
                    print("Invalid option")
                    continue
        
        elif option == '3': #Finish a task
            display(tasks)
            print("----------------------------------------------")
            id = int(input("Enter the task number to finish :"))
            
            tasks.pop(id-1)
            print("Task finished")

        elif option == '4': #exit
            break
        else:
            print("Invalid option")
print("Thank you for using the TO DO list")
