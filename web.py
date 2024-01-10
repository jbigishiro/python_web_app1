import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo app.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label='New todo', placeholder='Enter a new todo',
              on_change=add_todo, key='new_todo')

