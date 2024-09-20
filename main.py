import json
import os.path
from datetime import datetime

tasks = []

def add_task(description):
    time_now = datetime.now()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": time_now.strftime("%d/%m/%Y %H:%M:%S"),
        "updatedAt": time_now.strftime("%d/%m/%Y %H:%M:%S")
    }
    tasks.append(new_task)
    

def update_task(id, new_description):
    for task in tasks:
        if task["id"] == id:
            task["description"] = new_description
            task["uptadedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def delete_task(id):
    for task in tasks[:]:
        if task["id"] == id:
            tasks.remove(task)

def update_status(id, status):
    for task in tasks:
        if task["id"] == id:
            task["status"] = status

def list_tasks():
    for task in tasks:
        print(task)

while True:
    command = input().split()
    if len(command) < 2 or command[0] != "task-cli":
        print("Invalid Command")
        continue
    elif command[1].lower() == "add":
        description = " ".join(command[2:])
        add_task(description)
    elif command[1].lower() == "update":
        id = int(command[2])
        new_description = " ".join(command[3:])
        update_task(id, new_description)
    elif command[1].lower() == "delete":
        id = int(command[2])
        delete_task(id)
    elif command[1].lower() == "mark-in-progress":
        id = int(command[2])
        status = "In-progress"
        update_status(id, status)
    elif command[1].lower() == "mark-done":
        id = int(command[2])
        status = "Done"
        update_status(id, status)
    elif command[1].lower() == "list":
        list_tasks()
    else:
        print("Invalid Command")
    




# task-cli add "Comprar mantimentos"
# task-cli update 1 "Comprar mantimentos e cozinhar o jantar"
# task-cli delete 1
# task-cli mark-in-progress 1
# task-cli mark-done 1
# task-cli list
# task-cli list done
# task-cli list todo
# task-cli list in-progress