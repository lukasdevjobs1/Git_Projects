import streamlit as st
import pandas as pd

if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=['Task', 'Description', 'Complete'])

def add_task(task, description):
    if task.strip():
        new_task = pd.DataFrame([{'Task': task, 'Description': description, 'Complete': False}])
        st.session_state.tasks = pd.concat([st.session_state.tasks, new_task], ignore_index=True)
        return True
    return False

def remove_task(index):
    if 0 <= index < len(st.session_state.tasks):
        st.session_state.tasks = st.session_state.tasks.drop(index).reset_index(drop=True)
        return True
    return False

st.title('📝 To-Do List')

task_input = st.text_input('Task name:')
description_input = st.text_area('Task description:')

if st.button('Add Task'):
    if add_task(task_input, description_input):
        st.success('Task added successfully!')
        st.experimental_rerun()
    else:
        st.error('Please add a valid task name')

if not st.session_state.tasks.empty:
    st.subheader('📋 All Tasks')
    
    # Display tasks with interactive checkboxes
    for index, row in st.session_state.tasks.iterrows():
        col1, col2, col3, col4 = st.columns([0.5, 3, 4, 1])
        
        with col1:
            # Checkbox to mark as complete
            is_completed = st.checkbox('', value=row['Complete'], key=f'check_{index}')
            if is_completed != row['Complete']:
                st.session_state.tasks.loc[index, 'Complete'] = is_completed
                if is_completed:
                    st.balloons()
                    st.success('✅ Task completed!')
                st.experimental_rerun()
        
        with col2:
            # Task name with style based on status
            if row['Complete']:
                st.markdown(f'~~{row["Task"]}~~')
            else:
                st.markdown(f'**{row["Task"]}**')
        
        with col3:
            # Task description
            if row['Complete']:
                st.markdown(f'~~{row["Description"]}~~')
            else:
                st.markdown(row['Description'])
        
        with col4:
            # Remove button
            if st.button('🗑️', key=f'remove_{index}', help='Remove task'):
                remove_task(index)
                st.success('Task removed!')
                st.experimental_rerun()
    
    # Filter and show only pending tasks
    pending_tasks = st.session_state.tasks[st.session_state.tasks['Complete'] == False]
    if not pending_tasks.empty:
        st.subheader('⏳ Pending Tasks')
        for index, row in pending_tasks.iterrows():
            st.markdown(f'• **{row["Task"]}**: {row["Description"]}')
    
    total_tasks = len(st.session_state.tasks)
    completed_tasks = len(st.session_state.tasks[st.session_state.tasks['Complete'] == True])
    pending_tasks = total_tasks - completed_tasks
    
    st.subheader('📊 Statistics')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total", total_tasks)
    with col2:
        st.metric("Completed", completed_tasks)
    with col3:
        st.metric("Pending", pending_tasks)
    
    st.subheader('🧹 Manage List')
    if st.button('🗑️ Clear All Tasks', type='secondary'):
        st.session_state.tasks = pd.DataFrame(columns=['Task', 'Description', 'Complete'])
        st.experimental_rerun()
else:
    st.info('No tasks in the list.')