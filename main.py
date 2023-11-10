from modules.functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # get user input for list
    user_action = input('type add, show, edit, exit, or complete: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos,)

    elif user_action.startswith("show"):
        # show list

        todos = get_todos()

        #new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            # edit list itemwith open('files/todos.txt', 'r') as file:
    #        number = int(input('number of the todo to edit: '))
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Ender new todo: ")
            todos[number] = new_todo + '\n'
    #        print('here is how it wil be ', todos)
            write_todos(todos,)

        except ValueError:
            print("Your command is not valid, enter the number to edit.")
            continue

    elif user_action.startswith("complete"):
        try:
            #removes item from list
    #        number = int(input('number of the todo to complete: '))
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos,)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        #closes program
        break
    else:
        print("Command is not valid.")

print('Bye!')
