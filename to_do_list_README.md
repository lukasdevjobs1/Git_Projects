# 📝 To-Do List Application

A modern web-based task management application built with Streamlit, featuring real-time statistics and interactive task management.

## ✨ Features

- **Task Management**: Add, complete, and remove tasks with ease
- **Interactive UI**: Clean, intuitive web interface powered by Streamlit
- **Real-time Statistics**: Live tracking of total, completed, and pending tasks
- **Data Persistence**: Tasks persist during the session using Streamlit's session state
- **Bulk Operations**: Clear all tasks with a single click
- **Visual Feedback**: Success and error messages for all operations

## 🚀 Getting Started

### Prerequisites
```bash
pip install streamlit pandas
```

### Running the Application
```bash
streamlit run to_do_list.py
```

The application will open in your default web browser at `http://localhost:8501`

## 🎯 How to Use

1. **Add Tasks**: Enter a task description and click "To add Task"
2. **View Tasks**: All tasks are displayed in a clean table format
3. **Complete Tasks**: Select a task from the dropdown and mark as completed
4. **Remove Tasks**: Select a task from the dropdown and remove it
5. **Monitor Progress**: Check real-time statistics in the dashboard
6. **Clear All**: Use the "Clear All Tasks" button to reset your list

## 📊 Statistics Dashboard

The application provides real-time metrics:
- **Total Tasks**: Overall number of tasks created
- **Completed Tasks**: Number of finished tasks
- **Pending Tasks**: Remaining tasks to complete

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and storage
- **Session State**: Data persistence during app session

## 🔧 Technical Features

- **DataFrame Storage**: Uses Pandas DataFrame for efficient task management
- **Session Persistence**: Tasks remain available throughout the browser session
- **Input Validation**: Prevents empty tasks from being added
- **Error Handling**: User-friendly error messages and success notifications
- **Responsive Design**: Clean, modern interface that works on different screen sizes

## 📱 User Interface

The application features:
- Clean, minimalist design
- Intuitive task input field
- Interactive dropdown menus for task selection
- Color-coded buttons for different actions
- Real-time statistics cards
- Responsive layout with proper spacing

## 🔄 Future Enhancements

Potential improvements could include:
- Task categories and tags
- Due date functionality
- Task priority levels
- Data export capabilities
- User authentication
- Database persistence

---

*Part of the Daily Coding Projects Portfolio*