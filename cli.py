# from functions import get_todos, write_todos
import functions
import time

hora = time.strftime("%b %d, %Y %H:%M:%S")
print("Hoy es " + hora)

while True:
    accion = input("add, show, edit, complete or exit: ")
    accion = accion.lower()
    accion = accion.strip()

    if accion.startswith("add") or accion.startswith("create") or accion.startswith("new"):
        todo = accion[4:]
        todolist = functions.get_todos()
        todolist.append(todo + "\n")
        functions.write_todos(todolist_arg=todolist)



    elif accion.startswith("show") or accion.startswith("display") or accion.startswith("print"):

        todolist = functions.get_todos()

        # new_todos = []
        # for item in todolist:
        #    new_item = item.strip("\n")
        #    new_todos.append(new_item)

        # new_todos = [item.strip("\n") for item in todolist]
        # tambien puedes usar list comprehension si tienes tipo numbers = [1, 2 ,3.1] para juntarlos asi numbers = sum([float(number) for number in numbers]) y de los convierte en float y despues los suma

        for index, item in enumerate(todolist, start=1):
            item = item.strip("\n")
            row = (f"{index}. {item}")
            print(row)




    elif accion.startswith("exit") or accion.startswith("quit"):
        break




    elif accion.startswith("edit") or accion.startswith("change"):
        try:
            number = int(accion[5:])
            number = number - 1

            todolist = functions.get_todos()

            new_todo = input("Enter the new to-do: ")
            todolist[number] = new_todo + "\n"

            functions.write_todos(todolist_arg=todolist)

        except ValueError:
            print("Command not valid. You need to enter a number")
            continue




    elif accion.startswith("complete") or accion.startswith("done"):
        try:
            number = int(accion[9:])

            todolist = functions.get_todos()

            todo_to_remove = todolist[number - 1].strip("\n")
            todolist.pop(number - 1)

            functions.write_todos(todolist_arg=todolist)

            message = f"You have removed {todo_to_remove} from the to-do list"
            print(message)

        except IndexError:
            print("Command not valid. Enter a number that is in range")
            continue

    else:
        print("Invalid action. Try again.")
