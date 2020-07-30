import configparser
import os
import json
import logging

from utils.file_parser import dir_parser

logger = logging.getLogger()


def __create_config(path):
    """
    Создание файла конфигурации
    """
    logger.info('Создание файла конфигурации')
    config = configparser.ConfigParser()
    dict_config = __read_json_file(dir_parser(directory='config/confHost.json')).get("hosts")
    # шаблон конфигурации я бы хранил на сервере, но так как это тестовое задание об будет лежать рядом
    for host in dict_config:
        logger.debug(f'Добавление секции {host}')
        config.add_section(host)
        for param in dict_config.get(host):
            logger.debug(f'Добавление параметра {param}, со значением {dict_config.get(host).get(param)}')
            config.set(host, param, dict_config.get(host).get(param))

    with open(path, "w") as config_file:
        logger.debug('Запись в файл')
        config.write(config_file)


def __read_json_file(path):
    logger.warning(f'Чтение из файла {path}')
    with open(path, "r") as read_file:
        json_string = json.load(read_file)
    return json_string


def _check_availab_config(path):
    logger.info(f'Проверка наличия файла {path}')
    if not os.path.exists(path):
        logger.info('Файл не был найден')
        __create_config(path)
    logger.info('Файл найден')


def get_param_in_config(path, section, param):
    _check_availab_config(path)

    config = configparser.ConfigParser()
    config.read(path)

    return config.get(section, param)


def get_set_param_in_config(path, section, *params):
    _check_availab_config(path)

    config = configparser.ConfigParser()
    config.read(path)

    set_param = {}

    for param in params:
        set_param[param] = config.get(section, param)

    return set_param


def edit_param_in_config(path, section, param, value):
    _check_availab_config(path)

    config = configparser.ConfigParser()
    config.read(path)

    config.set(section, param, value)

    with open(path, "w") as config_file:
        config.write(config_file)