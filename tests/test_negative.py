import pytest
import json
import logging

from core.api_client import ApiClient
import allure

logger = logging.getLogger()
api_client = ApiClient()


@allure.epic('Негативные тесты')
@allure.story('query-параметры')
@allure.feature('Параметр "q"')
@pytest.mark.parametrize('value', [["?q=новйцуфывячскенапрмитгшщролтьбй&"],
                                   ["?q=н"]])
def test_q_param(value):
    logger.info(f"Запуск теста {value}")
    responce = api_client.get(value[0])
    api_client.check_status_code_200(responce)

    logger.info('Проверка соответсвия результата и передаваемого параметра')
    assert responce.json()['error']
    logger.info('Вернулась ожидаемая ошибка')
    # за не имением каких-то кодов ошибки, просто проверяю что ответ содержит в себе error, не лучшее решение,
    # но тут проблема на стороне сервера


@allure.epic('Негативные тесты')
@allure.story('query-параметры')
@allure.feature('Параметр "country_code"')
@pytest.mark.parametrize('value', [["?country_code=ru&page_size=1"],
                                   ["?country_code=kg&page_size=11"],
                                   ["?country_code=kz&page_size=6"]],
                         ids=["Значение параметра '1'", "Значение параметра '11'",
                              "Значение параметра '6'"])
def test_country_code(value):
    logger.info(f"Запуск теста {value}")
    responce = api_client.get(value[0])
    api_client.check_status_code_200(responce)

    logger.info('Проверка соответсвия результата и передаваемого параметра')
    assert responce.json()['error']
    logger.info('Вернулась ожидаемая ошибка')
    # за не имением каких-то кодов ошибки, просто проверяю что ответ содержит в себе error, не лучшее решение,
    # но тут проблема на стороне сервера


@allure.epic('Негативные тесты')
@allure.story('query-параметры')
@allure.feature('Параметр "page"')
@pytest.mark.parametrize('value', [["?page=0"],
                                   ["?page=10"],
                                   ["?page=-1"],
                                   ["?page=9999"]],
                         ids=["Значение параметра 0", "Значение параметра 10",
                              "Значение параметра -1", "Значение параметра 9999"])
def test_page(value):
    logger.info(f"Запуск теста {value}")
    responce = api_client.get(value[0])
    api_client.check_status_code_200(responce)

    logger.info('Проверка количества элементов на странице')
    assert responce.json()['error']
    logger.info('Вернулась ожидаемая ошибка')
    # не самая лучшая проверка, если предположить что количество регионов будет расти - каждый раз придется
    # дорабатывать автотест - это не хорошо. Было несколько вариантов решения проблемы, но в рамках тестовго задания
    # я решил не тратить время на их реализацию


@allure.epic('Негативные тесты')
@allure.story('query-параметры')
@allure.feature('Параметр "page_size"')
@pytest.mark.parametrize('value', [["?page_size=0"],
                                   ["?page_size=-1"],
                                   ["?page_size=7"],
                                   ["?page_size=9999"]],
                         ids=["Значение параметра 0", "Значение параметра -1",
                              "Значение параметра 7", "Значение параметра 9999"])
def test_page_size(value):
    logger.info(f"Запуск теста {value}")
    responce = api_client.get(value[0])
    api_client.check_status_code_200(responce)

    logger.info('Проверка количества элементов на странице')
    assert responce.json()['error']
    logger.info('Вернулась ожидаемая ошибка')
