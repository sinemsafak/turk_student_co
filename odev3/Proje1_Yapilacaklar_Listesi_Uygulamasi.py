# Görev sınıfı; her bir görevin adını ve tamamlanma durumunu tutar.
class Task:
    def __init__(self, name):
        self.name = name  # Görevin adı
        self.completed = False  # Görevin tamamlanma durumu

    def mark_completed(self):
        """Görevi tamamlandı olarak işaretler."""
        self.completed = True


# Görevleri yönetmek için kullanılan sınıf
class TaskManager:
    def __init__(self):
        self.tasks = []  # Görev listesi

    def add_task(self, task_name):
        """Yeni bir görev ekler."""
        self.tasks.append(Task(task_name))

    def complete_task(self, task_index):
        """Görevi tamamlandı olarak işaretler."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()

    def delete_task(self, task_index):
        """Belirli bir görevi listeden siler."""
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)

    def list_tasks(self):
        """Görevleri tamamlananlar ve tamamlanmayanlar olarak listeler."""
        completed = [task.name for task in self.tasks if task.completed]
        pending = [task.name for task in self.tasks if not task.completed]
        return {"Pending": pending, "Completed": completed}
