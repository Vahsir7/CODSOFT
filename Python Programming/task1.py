# TO DO List
class Task:
    '''
    This class hosts the task object of the to-do list.
    Each task has a name and a due date.
    '''

    def __init__(self, name, due):
        self.__name = name
        self.__due = due

    def get_name(self):
        return self.__name

    def get_due(self):
        return self.__due

    def set_name(self, name):
        self.__name = name

    def set_due(self, due):
        self.__due = due


def display(tasks):
    if not tasks:
        print("Great job! There are no tasks left.")
        return False

    max_id_width = len("ID")
    max_name_width = len("Name")
    max_due_width = len("Due")

    for i, task in enumerate(tasks, start=1):
        max_id_width = max(max_id_width, len(str(i)))
        max_name_width = max(max_name_width, len(task.get_name()))
        max_due_width = max(max_due_width, len(task.get_due()))

    padding = 4
    max_id_width += padding
    max_name_width += padding
    max_due_width += padding

    header = f"{'ID':<{max_id_width}}| {'Name':<{max_name_width}}| {'Due':<{max_due_width}}"
    print(header)

    separator = "-" * len(header)
    print(separator)

    for i, task in enumerate(tasks, start=1):
        row = f"{i:<{max_id_width}}| {task.get_name():<{max_name_width}}| {task.get_due():<{max_due_width}}"
        print(row)


def check(due):
    for sep in ['/', '-', '.', ' ']:
        if sep in due:
            due = due.split(sep)
            break
    else:
        return False

    if len(due) != 3:
        return False

    day, month, year = due

    if len(day) == 1:
        day = '0' + day
    if len(month) == 1:
        month = '0' + month
    if len(year) == 2:
        year = '20' + year

    formatted_date = f"{day}/{month}/{year}"

    if len(formatted_date) != 10:
        return False
    return formatted_date


tasks = []

if __name__ == "__main__":
    while True:
        print("\nWelcome to the TO-DO list")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Finish a Task")
        print("4. Exit")
        option = input("Enter your choice: ")

        if option == '1':  # Add a task
            name = input("Enter the task name: ")
            due = input("Enter the due date (dd/mm/yyyy): ")

            due = check(due)
            if not due:
                print("Invalid date format!")
                continue

            task = Task(name, due)
            tasks.append(task)
            print("Task added successfully!")

        elif option == '2':  # View tasks
            while True:
                print("Tasks:")
                display(tasks)
                print("\nPress 'U' to update a task or 'M' to return to the main menu")
                option2 = input("Enter your choice: ").strip().lower()

                if option2 == 'u':
                    try:
                        id = int(input("Enter the task number to update: ")) - 1
                        if id < 0 or id >= len(tasks):
                            print("Invalid task number!")
                            continue

                        task = tasks[id]

                        while True:
                            print("\nCurrent Task Details:")
                            display([task])

                            print("\nWhat would you like to edit?")
                            print("1. Name")
                            print("2. Due Date")
                            print("3. Exit")
                            option3 = input("Enter your choice: ")

                            if option3 == '1':
                                name = input("Enter the new name: ")
                                task.set_name(name)
                                print("Task name updated successfully!")

                            elif option3 == '2':
                                due = input("Enter the new due date (dd/mm/yyyy): ")
                                due = check(due)
                                if not due:
                                    print("Invalid date format!")
                                    continue
                                task.set_due(due)
                                print("Task due date updated successfully!")

                            elif option3 == '3':
                                break
                            else:
                                print("Invalid option! Please try again.")

                    except ValueError:
                        print("Invalid input! Please enter a valid task number.")
                        continue

                elif option2 == 'm':
                    break
                else:
                    print("Invalid option! Please try again.")

        elif option == '3':  # Finish a task
            display(tasks)

            try:
                id = int(input("Enter the task number to finish: ")) - 1
                if id < 0 or id >= len(tasks):
                    print("Invalid task number!")
                    continue

                tasks.pop(id)
                print("Task marked as completed!")

            except ValueError:
                print("Invalid input! Please enter a valid task number.")

        elif option == '4':  # Exit
            print("Thank you for using the TO-DO list!")
            break

        else:
            print("Invalid option! Please try again.")
