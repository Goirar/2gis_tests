import os

# метод нужен исключительно в данной архитектуре, если шаблон конфига хранится на сервере, то этот метод не будет нужен
def dir_parser(directory=None):
    path_to_file = os.path.dirname(os.path.dirname(__file__))
    return f"{path_to_file}/{directory}"