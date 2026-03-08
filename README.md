## CLI Task Manager in Python

🌐 **Languages**

[![Português](https://img.shields.io/badge/Português-green?style=for-the-badge)](lang/README_PT.md)
[![Español](https://img.shields.io/badge/Español-red?style=for-the-badge)](lang/README_ES.md)
[![한국어](https://img.shields.io/badge/한국어-purple?style=for-the-badge)](lang/README_KO.md)

A simple command-line task manager built with Python. This project allows users to manage their daily tasks directly from the terminal in a fast and practical way.

### Features

* Add new tasks
* List all tasks
* Mark tasks as completed
* Delete tasks
* Persistent data storage using JSON files
* Simple and intuitive command-line interface

### How it works

Tasks are stored in a local `taks.json` file. Each task contains:

* **ID** – unique identifier
* **Task description**
* **Status** – "Em andamento" or "Concluído"

The program loads the JSON file when it starts and updates it whenever a task is created, completed, or deleted.

### Technologies Used

* **Python 3**
* **JSON** for data persistence
* **OS module** for terminal utilities

### How to Use

1. Clone the repository:

```
git clone https://github.com/Hallow303/cli-task-manager.git
```

2. Navigate to the project folder:

```
cd cli-task-manager
```

3. Run the program:

```
python main.py
```

4. Use the menu in the terminal to manage your tasks:

* Add a task
* View tasks
* Mark a task as completed
* Delete a task

### Purpose

This project was created as a learning exercise to practice:

* File handling in Python
* Working with JSON data
* Building simple CLI applications
* Organizing code with functions
