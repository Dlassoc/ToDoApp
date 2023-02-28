class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self) -> bool:
        self.completed: bool = True
        return self.completed

    def add_tag(self, tag: str) -> tag:
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self, todos: dict):
        self.todos: dict = {}

    def add_todo(self, title: str, description: str) -> int:
        todo_id: int = len(self.todos) + 1
        todo_object = Todo(todo_id, title, description)
        self.todos[todo_id] = todo_object
        return todo_id

    def pending_todos(self):
        todo_list = [self.todos[clave] for clave in self.todos if self.todos[clave].completed is False]
        return todo_list

    def completed_todos(self):
        todo_list = [self.todos[clave] for clave in self.todos if self.todos[clave].completed is True]
        return todo_list

    def tags_todo_count(self):
        tags_todo_count_dict: dict = {}






