#TO DO list
import datetime
import time
import os
import sys


class Task:
    '''
    This class hosts the task object of the to do list
    Each task has a name, start date time, end date time and duration(which is calculated)
    '''
    def __init__(self, name, start, end):
        self.__name = name
        self.__start = start
        self.__end = end
        self.__duration = self.__end - self.__start
    
    def get_name(self):
        return self.__name
    
    def get_start(self):
        return self.__start
    
    def get_end(self):
        return self.__end
    
    def get_duration(self):
        return self.__duration
    
    def set_name(self, name):
        self.__name = name
    
    def set_start(self, start):
        self.__start = start
        self.__duration = self.end - self.start
    
    def set_end(self, end):
        self.__end = end
        self.__duration = self.end - self.start
    

tasks = []
#main
if __name__ == "__main__":
    while(True):
        print("Welcome to the TO DO list")
        print("Please select an option")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        option = int(input("Enter your choice: "))
        if option == 1:
            print("Enter the task name")
            name = input()
            print("Enter the start date time in the format 'dd/mm/yyyy hh:mm:ss'")
            start = input()
            print("Enter the end date time in the format 'dd/mm/yyyy hh:mm:ss'")
            end = input()
            start = datetime.datetime.strptime(start, "%d/%m/%Y %H:%M:%S")
            end = datetime.datetime.strptime(end, "%d/%m/%Y %H:%M:%S")
            task = Task(name, start, end)
            tasks.append(task)
        elif option == 2:
            print("Tasks:")
            print("id\t\t|Name\t\t|Start\t\t|End\t\t|Duration\t\t|")
            id = 1
            for task in tasks:
                print(f"{id}\t\t|{task.get_name()}\t\t|{task.get_start()}\t\t|{task.get_end()}\t\t|{task.get_duration()}\t\t|")
                id += 1
            print("----------------------------------------------")
            print("Press U to update a task or M to return to the main menu")
            option2 = input("Enter your choice: ")

            if option2 == 'U' or option2=='u':
                id = int(input("Enter the task number to update"))
                task = tasks[id-1]
            elif option2 == 'M' or option2=='m':
                continue

        elif option == 3:
            break
        else:
            print("Invalid option")
print("Thank you for using the TO DO list")
