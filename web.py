import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app increases your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) # returns True or False
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] # deletes from session_state dictionary
        st.experimental_rerun() # reruns code for checkboxes

st.text_input(label=' ', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo', label_visibility='collapsed')
