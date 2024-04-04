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

for todo in todos:
    st.checkbox(todo)

st.text_input(label=' ', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo', label_visibility='collapsed')
