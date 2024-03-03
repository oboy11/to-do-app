import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Time is below:")
print("it is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos(filepath="todos.txt")

        todos.append(todo + '\n')

        functions.write_todos("todos.txt", todos_arg=todos)

        todos.append(todo)

        file = open('todos.txt', 'w')
        file.writelines(todos)
        file.close()
    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")
        file.close()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos("todos.txt")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"): 
        try:
            number = user_action[9:]

            todos = functions.get_todos("todos.txt")
            index = int(number) - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye!")
