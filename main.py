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
            json.dump(self.tasks, file)

    def display_tasks(self):
        if not self.tasks:
            print("Aucune tâche enregistrée.")
        else:
            print("Liste des tâches :")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tâche ajoutée : {task}")
        self.save_tasks()

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Tâche supprimée : {deleted_task}")
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
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Entrez le numéro de la tâche à supprimer : "))
            todo_list.delete_task(index)
        elif choice == '4':
            print("Merci d'utiliser l'application Todo List. Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
