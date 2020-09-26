def list_tasks(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def add_task(task, todolist):
    todolist.append(task)


def undo(todolist, redolist):
    if not todolist:
        return
    removed_todo = todolist.pop()
    redolist.append(removed_todo)


def redo(todolist, redolist):
    if not redolist:
        return
    added_todo = redolist.pop()
    todolist.append(added_todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou [undo, redo, ls]: ')
        if todo == 'ls':
            list_tasks(todo_list)
            continue
        elif todo == 'undo':
            undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            redo(todo_list, redo_list)
            continue
        else:
            add_task(todo, todo_list)
