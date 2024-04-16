import argparse
from .models import Tache

parser = argparse.ArgumentParser(description='Gestionnaire de tâches Django')

# parser.add_argument('task_id', type=int, help='ID de la tâche')
parser.add_argument('-n', '--name', type=str, help='Nom de la tâche')
parser.add_argument('-p', '--priority', type=int, default=0, help='Priorité de la tâche')
# parser.add_option('-c', '--completed', action='store_true', help='Marquer la tâche comme terminée')

args = parser.parse_args()

# task_id = args.task_id
task_name = args.name
task_priority = args.priority
# is_completed = args.completed

# Créer une nouvelle tâche
new_task = Tache()
new_task.save()

# Afficher un message de confirmation
print(f"Tâche '{task_name}' ajoutée avec succès avec priorité {task_priority}.")
