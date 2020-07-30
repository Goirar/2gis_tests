import pytest
import json
import logging

from core.api_client import ApiClient
import allure

logger = logging.getLogger()
api_client = ApiClient()


@allure.epic('Позитивные тесты')
@allure.story('query-параметры')
@allure.feature('Параметр "q"')
@pytest.mark.parametrize('value', [["?q=нов&country_code=kz", "нов", 2],
                                   ["?q=ново&country_code=kz", "ново", 1],
                                   ["?q=нов", "нов", 2]],
                         ids=["Значение параметра 'нов', обавлен фильтр по стране",
                              "Значение параметра 'ново', обавлен фильтр по стране",
                              "Значение параметра 'нов'"])
def test_q_param(value):
    logger.info(f"Запуск теста {value}")
    responce = api_client.get(value[0])
    api_client.check_status_code_200(responce)

    logger.info('Проверка соответсвия результата и передаваемого параметра')
    for item in responce.json()['items']:
        assert item['name'].lower().find(value[1]) >= 0
        # не самая лучшая реализация, но в рамках тестового задания, я думаю подойдет
        assert len(responce.json()['items']) == value[2]
    logger.info('Тест пройден')


@allure.epic('Позитивные тесты')
@allure.story('query-параметры')
@allure.feature('Параметр "country_code"')
@pytest.mark.parametrize('value', [["?country_code=ru&page_size=15", "ru"],
                                   ["?country_code=kg&page_size=15", "kg"],
                                   ["?country_code=kz&page_size=15", "kz"],
                                   ["?country_code=cz&page_size=15", "cz"]],
                         ids=["Значение параметра 'ru'", "Значение параметра 'kg'",
                              "Значение параметра 'kz'", "Значение параметра 'cz'"])
def test_country_code(value):
    logger.info(f"Запуск теста {value}")
    responce = api_client.get(value[0])
    api_client.check_status_code_200(responce)

    logger.info('Проверка соответсвия результата и передаваемого параметра')
    for item in responce.json()['items']:
        assert item['country']['code'] == value[1]
    logger.info('Тест пройден')


@allure.epic('Позитивные тесты')
@allure.story('query-параметры')
@allure.feature('Параметр "page"')
@pytest.mark.parametrize('value', [["", 10],
                                   ["?page=1", 10],
                                   ["?page=2", 10],
                                   ["?page=3", 2]],
                         ids=["Параметр не передается", "Значение параметра 1",
                              "Значение параметра 2", "Значение параметра 3"])
def test_page(value):
    logger.info(f"Запуск теста {value}")
    responce = api_client.get(value[0])
    api_client.check_status_code_200(responce)

    logger.info('Проверка количества элементов на странице')
    assert len(responce.json()['items']) == value[1]
    logger.info('Тест пройден')
    # не самая лучшая проверка, если предположить что количество регионов будет расти - каждый раз придется
    # дорабатывать автотест - это не хорошо. Было несколько вариантов решения проблемы, но в рамках тестовго задания
    # я решил не тратить время на их реализацию


@allure.epic('Позитивные тесты')
@allure.story('query-параметры')
@allure.feature('Параметр "page_size"')
@pytest.mark.parametrize('value', [["", 10],
                                   ["?page_size=5", 5],
                                   ["?page_size=10", 10],
                                   ["?page_size=15", 15]],
                         ids=["Параметр не передается", "Значение параметра 5",
                              "Значение параметра 10", "Значение параметра 15"])
def test_page_size(value):
    logger.info(f"Запуск теста {value}")
    responce = api_client.get(value[0])
    api_client.check_status_code_200(responce)

    logger.info('Проверка количества элементов на странице')
    assert len(responce.json()['items']) == value[1]
    logger.info('Тест пройден')
