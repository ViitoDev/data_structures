team_a = {"plan a meeting", "review document", "test system"} 
team_b = {"test system", "implement functionality", "fix bug"} 
tasks = team_a.union(team_b)
print(tasks)
task_remove = input("Enter the task you want to remove: ").lower()
if task_remove in tasks:
    tasks.remove(task_remove)
print(f"The final tasks is: {tasks}")

