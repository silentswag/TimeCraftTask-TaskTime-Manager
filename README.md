To have your personal Time machine :
1. clone the project : git clone git@github.com:silentswag/Timecraft--Task-Time-Manager.git

2. Install Redis server, cd to the download path and execute start redis-server.exe

3. On the project terminal 1: py manage.py runserver

4. on terminal 2: start the celery worker

5. on terminal 3: start the celery beat




Timecraft is a personal productivity tool designed to manage tasks and time efficiently while promoting a healthy work-life balance. This application helps users track their daily tasks, monitor the time spent on each task, and maintain a historical record of all tasks.

Features:
1. Create Task: Add new tasks with details such as title, description, due date, and priority.
2. List Tasks: View all tasks in a list format, optionally sorted by priority, due date, or creation date.
3. Update Task: Modify existing tasks to keep them up to date with changes in scope or deadlines.
4. Retrieve Specific Task: Search and retrieve details of a specific task by its ID or name.
5. Track Task History: Maintain a log of all actions performed on tasks to provide a historical overview.
6. Track Time Duration: Monitor the amount of time spent on individual tasks to enhance time management.
7. Retrieve Today’s Tasks: Quickly access all tasks scheduled for the current day.
