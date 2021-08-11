from functions import Function
from interface import Interface


def main_window():
    window = Interface()
    window.create_label("MathGraph")
    window.create_button(ready_graphs_window, "Готовые графики")
    window.create_button(set_graph_window, "Задать график", 50)
    window.create_button(task_window, "Задания", 100)

    window.run()


def ready_graphs_window():
    window = Interface()
    window.create_label("Готовые графики")
    window.create_button(Function.hello_world, "Test button 1")
    window.create_button(Function.hello_world, "Test button 2", 50)

    window.run()


def set_graph_window():
    window = Interface()
    window.create_label("Задать график")
    window.create_button(Function.hello_world, "Test button 1")
    window.create_button(Function.hello_world, "Test button 2", 50)

    window.run()


def task_window():
    window = Interface()
    window.create_label("Задания")
    window.create_button(Function.hello_world, "Test button 1")
    window.create_button(Function.hello_world, "Test button 2", 50)

    window.run()
