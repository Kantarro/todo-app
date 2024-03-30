import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo", key="thing_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica",15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values["thing_todo"] + "\n"  # values = {"thing_todo": whatever was added}
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["thing_todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                print("Please select an item first.")
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['thing_todo'].update(value='')
        case 'Exit':
            break
        case 'todos':
            window["thing_todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()