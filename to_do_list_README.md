# 📝 To-Do List Application

A modern, interactive web-based task management application built with Python and Streamlit.

## 🚀 Features

### Core Functionality
- ✅ **Add Tasks**: Create tasks with names and detailed descriptions
- ✅ **Interactive Checkboxes**: Click to mark tasks as complete/incomplete
- ✅ **Task Removal**: Individual delete buttons for each task
- ✅ **Real-time Updates**: Instant UI refresh after actions

### Enhanced User Experience
- 🎉 **Celebration Animation**: Balloons animation when completing tasks
- 📋 **Dual View**: See all tasks and filtered pending tasks
- 🎨 **Visual Feedback**: Strikethrough styling for completed tasks
- 📊 **Statistics Dashboard**: Track total, completed, and pending tasks

### Interface Features
- 📱 **Responsive Layout**: Clean column-based design
- 🗑️ **Bulk Actions**: Clear all tasks option
- 💾 **Session Persistence**: Tasks saved during browser session
- 🔄 **Auto-refresh**: Seamless state management

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit**: Web framework for interactive applications
- **Pandas**: Data manipulation and storage
- **Session State**: For data persistence

## 📦 Installation & Setup

### Prerequisites
```bash
pip install streamlit pandas
```

### Running the Application
```bash
streamlit run to_do_list.py
```

The application will open in your default browser at `http://localhost:8501`

## 🎯 How to Use

1. **Add a Task**: Enter task name and description, click "Add Task"
2. **Mark Complete**: Click the checkbox next to any task
3. **Remove Task**: Click the 🗑️ button to delete a task
4. **View Progress**: Check statistics in the dashboard
5. **Clear All**: Use "Clear All Tasks" to reset the list

## 📊 Application Structure

```
to_do_list.py
├── Session State Management
├── Task Functions (add, remove, mark_complete)
├── User Interface
│   ├── Task Input Form
│   ├── Interactive Task List
│   ├── Pending Tasks View
│   └── Statistics Dashboard
└── Data Persistence (Pandas DataFrame)
```

## 🔄 Version History

### Version 2.0 (Current)
- Added task descriptions
- Interactive checkbox interface
- Celebration animations
- Separate pending tasks view
- Enhanced visual styling
- English language interface

### Version 1.0
- Basic task addition and removal
- Simple list display
- Portuguese interface

## 🎨 UI Components

- **Task Cards**: Checkbox + Name + Description + Delete button
- **Statistics Metrics**: Total, Completed, Pending counters
- **Action Buttons**: Add, Remove, Clear All
- **Status Indicators**: Visual feedback for task states

## 🚀 Future Enhancements

- [ ] Task categories/tags
- [ ] Due dates and reminders
- [ ] Task priority levels
- [ ] Export/Import functionality
- [ ] Dark/Light theme toggle
- [ ] Task search and filtering

## 📄 License

This project is part of the Daily Coding Projects portfolio and is available under the MIT License.

---

*Built with ❤️ as part of the daily coding challenge*