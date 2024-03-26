# from functions import get_todos, write_todos
import functions
import time

time_now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", time_now)
print(time.strftime("%A"))
while True:
    user_action = input("Type add [something], show, edit [number], complete [number], or exit: ")
    user_action = user_action.strip() # removes any trailing white spaces

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        # file = open("todos.txt")
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        todos.append(todo)

        # file = open("todos.txt", "w")
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        # file = open("todos.txt")
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        # new_todos = []        new list name
        # for item in todos:
        #     item = item.strip("\n")
        #     new_todos.append(item)

        # using LIST COMPREHENSION
        # todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n") # strips trailing "\n" from the string
            print(f"{index+1}. {item}")

    elif user_action.startswith("edit"):
        try:
            index_num = int(user_action[5:]) - 1
            todos = functions.get_todos()
            if index_num <= len(todos) - 1:
                new_todo = input("Enter a new todo: ")

                todos[index_num] = new_todo + "\n"

                functions.write_todos(todos)
            else:
                print("There is no item with that number.")
                continue

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            num = int(user_action[9:]) - 1
            todos = functions.get_todos()

            # stores it before it gets popped
            todo_to_remove = todos[num].strip("\n") # gets rid of the "\n" character
            todos.pop(num)

            functions.write_todos(todos)

            print(f"To do {todo_to_remove} was removed from the list.")

        except IndexError:
            print("There is no item with that number.")
            continue

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Your command is not valid.")

print("Bye!")