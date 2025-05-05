class Task:
    def __init__(self, name, burst_time, assigned_member=None):
        self.name = name
        self.burst_time = burst_time
        self.assigned_member = assigned_member
        self.waiting_time = 0
        self.turnaround_time = 0
        self.start_time = 0
        self.end_time = 0

    def update(self, new_burst_time=None, new_member=None, valid_members=None):
        if new_burst_time is not None:
            self.burst_time = new_burst_time
        if new_member:
            if valid_members and new_member in valid_members:
                self.assigned_member = new_member
            else:
                print(f" Member '{new_member}' does not exist. Assignment not changed.")


class ProjectManagementScheduler:
    def __init__(self):
        self.tasks = []
        self.members = []

    def add_member(self, member_name):
        if member_name not in self.members:
            self.members.append(member_name)
            print(f" Member '{member_name}' added.")
        else:
            print(" Member already exists.")

    def add_task(self, task_name, burst_time, assigned_member=None):
        if assigned_member and assigned_member not in self.members:
            print(f" Member '{assigned_member}' not found. Task will be unassigned.")
            assigned_member = None
        task = Task(task_name, burst_time, assigned_member)
        self.tasks.append(task)
        print(f" Task '{task_name}' added.")

    def update_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                print(f"\n Updating Task: {task.name}")
                new_burst = input("Enter new burst time (or press Enter to keep current): ")
                new_member = input("Enter new member name (or press Enter to keep current): ")

                burst_time = None
                if new_burst.strip():
                    try:
                        burst_time = int(new_burst)
                    except ValueError:
                        print(" Invalid burst time. Keeping previous value.")

                task.update(burst_time, new_member.strip(), self.members)
                print("\n Task updated.\n")
                return
        print(" Task not found.")

    def schedule(self):
        current_time = 0
        for task in self.tasks:
            task.start_time = current_time
            task.waiting_time = current_time
            task.end_time = task.start_time + task.burst_time
            task.turnaround_time = task.end_time
            current_time = task.end_time

    def display_schedule(self):
        if not self.tasks:
            print("⚠️ No tasks to display.")
            return

        print("\n Project Task Schedule (FCFS):\n")
        print(f"{'Task':<10}{'Burst':<10}{'Member':<15}{'Start':<10}{'End':<10}"
              f"{'Waiting':<15}{'Turnaround':<15}")
        print("-" * 75)

        total_waiting = 0
        total_turnaround = 0

        for task in self.tasks:
            total_waiting += task.waiting_time
            total_turnaround += task.turnaround_time
            print(f"{task.name:<10}{task.burst_time:<10}{task.assigned_member or 'Unassigned':<15}"
                  f"{task.start_time:<10}{task.end_time:<10}"
                  f"{task.waiting_time:<15}{task.turnaround_time:<15}")

        avg_wait = total_waiting / len(self.tasks)
        avg_turnaround = total_turnaround / len(self.tasks)

        print("\n Averages:")
        print(f"• Average Waiting Time: {avg_wait:.2f}")
        print(f"• Average Turnaround Time: {avg_turnaround:.2f}")


def main():
    scheduler = ProjectManagementScheduler()

    while True:
        print("\n===== Project Management Scheduler =====")
        print("1. Add Member")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Show Scheduled Tasks")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            member = input("Enter member name: ")
            scheduler.add_member(member)

        elif choice == '2':
            task_name = input("Enter task name: ")
            try:
                burst_time = int(input("Enter burst time: "))
            except ValueError:
                print(" Invalid burst time. Please enter a number.")
                continue
            assigned_member = input("Assign to member (optional): ")
            scheduler.add_task(task_name, burst_time, assigned_member.strip() if assigned_member else None)

        elif choice == '3':
            task_name = input("Enter the name of the task to update: ")
            scheduler.update_task(task_name)

        elif choice == '4':
            scheduler.schedule()
            scheduler.display_schedule()

        elif choice == '5':
            print(" Exiting Project Management Scheduler. Goodbye!")
            break

        else:
            print(" Invalid option. Please select between 1–5.")


if __name__ == "__main__":
    main()
