import json

class TodoList:
    def __init__(self, filename="todo.json"):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("Aucune tâche enregistrée.")
        else:
            print("Liste des tâches :")
            sorted_tasks = sorted(self.tasks, key=lambda x: x.get('priority', 0))
            for index, task_info in enumerate(sorted_tasks, start=1):
                task = task_info.get('task', '')
                priority = task_info.get('priority', 0)
                print(f"{index}. Priority {priority}: {task}")

    def add_task(self, task, priority=0):
        new_task = {"task": task, "priority": priority}
        self.tasks.append(new_task)
        print(f"Tâche ajoutée : {task}")
        self.save_tasks()

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Tâche supprimée : {deleted_task.get('task', '')}")
            self.save_tasks()
        else:
            print("Numéro de tâche invalide. Veuillez choisir un numéro valide.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")

        choice = input("Choisissez une option (1/2/3/4): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Entrez la nouvelle tâche : ")
            priority = int(input("Entrez la priorité de la tâche (0 par défaut) : "))
            todo_list.add_task(task, priority)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Entrez le numéro de la tâche à supprimer : "))
            todo_list.delete_task(index)
        elif choice == '4':
            print("Merci d'utiliser l'application Todo List. Au revoir!")
            break


if __name__ == "__main__":
    main()
