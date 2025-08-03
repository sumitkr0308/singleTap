week = {
    "monday": [],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": [],
    "saturday": [],
    "sunday": []
}

def display_days():
    print("\nChoose a day:")
    for idx, day in enumerate(week.keys(), start=1):
        print(f"{idx}. {day.capitalize()}")
    return list(week.keys())

def get_day_input():
    days = display_days()
    try:
        choice = int(input("Enter day number (1-7): "))
        if 1 <= choice <= 7:
            return days[choice - 1]
    except ValueError:
        pass
    print("Invalid choice. Try again.")
    return get_day_input()

def save_tasks():
    with open("week_tasks.txt", "w") as f:
        for day, tasks in week.items():
            f.write(f"{day.capitalize()}:\n")
            for task in tasks:
                f.write(f"  - {task['task']} [{task['status']}]\n")
            f.write("\n")

def plan():
    while True:
        print("""
        !! LET'S PLAN THE WEEK !!
        1. ADD TASKS
        2. VIEW ALL TASKS FOR THE WEEK
        3. UPDATE PLAN FOR A DAY
        4. VIEW PLAN FOR A DAY
        5. DELETE A TASK
        6. MARK TASK AS COMPLETED
        7. CLEAR ALL TASKS FOR A DAY
        8. CLEAR ALL TASKS FOR THE WEEK
        9. SAVE TASKS
        10. EXIT
        """)

        try:
            choice = int(input("Enter your choice (1-10): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            day = get_day_input()
            num = int(input(f"How many tasks for {day.capitalize()}? "))
            for i in range(num):
                task = input(f"Enter task {i + 1}: ")
                week[day].append({"task": task, "status": "Pending"})
            print(f"{num} task(s) added to {day.capitalize()}.")

        elif choice == 2:
            print("\nWEEKLY PLANS:")
            for day, tasks in week.items():
                print(f"\n{day.capitalize()}:")
                if tasks:
                    for i, t in enumerate(tasks, start=1):
                        print(f"  {i}. {t['task']} [{t['status']}]")
                else:
                    print("  No tasks yet.")

        elif choice == 3:
            day = get_day_input()
            if week[day]:
                for i, t in enumerate(week[day], start=1):
                    print(f"{i}. {t['task']} [{t['status']}]")
                try:
                    task_num = int(input("Enter task number to update: "))
                    if 1 <= task_num <= len(week[day]):
                        new_task = input("Enter the new task: ")
                        week[day][task_num - 1]["task"] = new_task
                        print("Task updated.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid number.")
            else:
                print("No tasks to update.")

        elif choice == 4:
            day = get_day_input()
            print(f"{day.capitalize()} Plan:")
            if week[day]:
                for i, t in enumerate(week[day], start=1):
                    print(f"  {i}. {t['task']} [{t['status']}]")
            else:
                print("  No tasks yet.")

        elif choice == 5:
            day = get_day_input()
            if week[day]:
                for i, t in enumerate(week[day], start=1):
                    print(f"{i}. {t['task']} [{t['status']}]")
                try:
                    task_num = int(input("Enter task number to delete: "))
                    if 1 <= task_num <= len(week[day]):
                        removed = week[day].pop(task_num - 1)
                        print(f"Deleted: {removed['task']}")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Enter a valid number.")
            else:
                print("No tasks to delete.")

        elif choice == 6:
            day = get_day_input()
            if week[day]:
                for i, t in enumerate(week[day], start=1):
                    print(f"{i}. {t['task']} [{t['status']}]")
                try:
                    task_num = int(input("Enter task number to mark completed: "))
                    if 1 <= task_num <= len(week[day]):
                        week[day][task_num - 1]["status"] = "Completed"
                        print("Marked as completed.")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Enter a valid number.")
            else:
                print("No tasks to mark.")

        elif choice == 7:
            day = get_day_input()
            week[day] = []
            print(f"All tasks cleared for {day.capitalize()}.")

        elif choice == 8:
            for key in week:
                week[key] = []
            print("All tasks cleared for the week.")

        elif choice == 9:
            save_tasks()
            print("Tasks saved to week_tasks.txt")

        elif choice == 10:
            confirm = input("Are you sure you want to Exit? (y/n): ")
            if confirm.lower() == 'y':
                break

        else:
            print("Invalid choice. Choose between 1 to 10.")

# Run the planner
plan()
