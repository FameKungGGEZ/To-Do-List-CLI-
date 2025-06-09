import json
import os
import time

file = "tasks.json"

## ถ้าเกิดไม่มีtasks.js จะสร้างขึ้นมาใหม่พร้อมใส่list
if not os.path.exists(file) :
    with open(file, "w") as f :
        json.dump([], f)

## บันทึกข้อมูล   
def save(task) :
    with open(file, "w") as f :
        json.dump(task, f, indent=2)

## โหลดข้อมูล
def load() :
    try :
        with open(file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError :
        print("Warning: this file is break > get new file")
        save([])
        return []


## เพิ่มข้อมูล
def add() :
    load_task = load()
    title = input("Name title : ")
    description =  input("Description :\n")
    task = {title:description}
    load_task.append(task)
    save(load_task)
    print("Complete")
    x = input("\nPress Enter to continue...")

## แสดงข้อมูลของหัวข้อ
def show() :
    os.system("cls" if os.name == "nt" else "clear")
    load_task = load()
    ### แสดงหัวข้อทั้งหมด
    for i, task in enumerate(load_task, start=1) :
        print(i, list(task.keys())[0])
    des = input("Choose number of title you want to see description : ")
    os.system("cls" if os.name == "nt" else "clear")

    ### แสดงข้อมูลของหัวข้อที่ใส่มา
    try : 
        if 1 <= int(des) <= len(load_task) :
            task = load_task[int(des)-1]
            key = list(task.keys())[0]
            value = task[key]
            print(key)
            print("Description :\n",value)
        else : print("Error:Wrong Number")
    except :
        print("Error:Invalid input, Please Enter Number")
    x = input("\nPress Enter to continue...")
    
## ลบข้อมูล
def remove() :
    os.system("cls" if os.name == "nt" else "clear")
    load_task = load()
    for i, task in enumerate(load_task, start=1) :
        print(i, list(task.keys())[0])
    re = input("Number of file you want to Delete : ")
    try :
        re = int(re)
        if 1 <= re <= len(load_task) : 
            removed_task = load_task.pop(re-1)
            save(load_task)
            print(f"Delete task: {list(removed_task.keys())[0]}")
        else :
            print("Error:Wrong Number")
    except :
        print("Error:Invalid input, Please Enter Number")

    x = input("\nPress Enter to continue...")


## ลูปซ้ำ ให้เลือกสิ่งที่อยู่ในเมนูเพื่อไปยังฟังก์ชั่นด้านบนหรือจะเป็นการออกจากลูป
while True :
    os.system("cls" if os.name == "nt" else "clear")
    print("\nchoice :\n1.Add Task\n2.Remove Task\n3.Load Task\n4.Leave")
    choice = input("Choose Menu (1-4): \n")

    if choice == "1" :
        os.system("cls" if os.name == "nt" else "clear")
        add()
    elif choice == "2" :
        os.system("cls" if os.name == "nt" else "clear")
        remove()
    elif choice == "3" :
        os.system("cls" if os.name == "nt" else "clear")
        show()
    elif choice == "4" :
        os.system("cls" if os.name == "nt" else "clear")
        break
    else :
        print(f"Error:Please input 1-4")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        continue
