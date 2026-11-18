# Student Task Manager - User Guide

## 1. Introduction

Student Task Manager is a simple Python console application that allows students to manage their tasks.

## 2. Starting the Application

Open PowerShell in the project folder and run:

```bash
python main.py
```

The main menu will appear.

## 3. Adding a Task

1. Select option `1` (Add Task).
2. Enter your task title.
3. The application will display a success message.

Empty task titles are not accepted.

## 4. Viewing Tasks

1. Select option `2` (View Tasks).
2. All available tasks will be displayed with their IDs and completion status.

## 5. Completing a Task

1. Select option `3` (Complete Task).
2. Enter the ID of the task you want to complete.
3. The application will mark the task as completed.

## 6. Deleting a Task

1. Select option `4` (Delete Task).
2. Enter the task ID.
3. Confirm the deletion when prompted.

## 7. Exiting the Application

Select option `5` (Exit) to close the application.

## 8. Running Tests

To run the automated tests, execute:

```bash
python -m unittest discover -s tests -v
```

The tests check the add, complete, and delete task operations.