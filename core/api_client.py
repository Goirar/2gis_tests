import allure
import utils.config_parser
import requests
import logging

from utils.file_parser import dir_parser

logger = logging.getLogger()


class ApiClient(object):
    """Класс для запросов к API"""

    def __init__(self, section="region", segment="region_segment"):
        """Конструктор"""
        self.path_to_config = dir_parser(directory='config/setting.cfg')

        self.section = section
        setting = utils.config_parser.get_set_param_in_config(self.path_to_config, self.section,
                                                              "host", segment)
        self.address = setting["host"]
        self.segment = setting[segment]
        self.status_code_200 = 200

    def get_path_to_config(self):
        return self.path_to_config

    def get_section(self):
        return self.section

    def get(self, query_param="", payload="", cookies=""):
        logger.info('Отправка GET запроса')
        with allure.step('Отправка GET запроса'):
            request = requests.get(self.__generation_url(query_param), params=payload, cookies=cookies)
            logger.info(f'Request. URL and cookies - {request.url} and {str(cookies)}')
            allure.attach('Request. URL and cookies', request.url + ' ' + str(cookies))
            logger.info(f'Response. Status code {request.status_code}')
            allure.attach('Response. Status code', request.status_code)
            return request

    def post(self, url=None, data=None, payload=None, cookies=None):
        with allure.step('Отправка POST запроса'):
            request = requests.post(self.__generation_url(url), data=data, params=payload, cookies=cookies)
            allure.attach(f'URL- {request.url},\n cookies-{str(cookies)}, \n xml-{str(data)}', 'Request_xml')
            allure.attach('Response. Status code', request.status_code)
            return request

    def __generation_url(self, query_param=""):
        """Метод формирования ссылки"""
        with allure.step('Формируем адрес для запроса'):
            logger.info('Формируем адрес для запроса')
            link = "https://{}{}{}".format(self.address, self.segment, query_param)
            allure.attach('Адрес отправления запроса', link)
            logger.info(f'Адрес отправления запроса {link}')
            return link

    def check_status_code_200(self, response):
        logger.info('Проверка кода ответа')
        with allure.step('Проверка кода ответа'):
            logger.info('Код ответа {}'.format(response))
            allure.attach('Код ответа', response)
            assert response.status_code == self.status_code_200