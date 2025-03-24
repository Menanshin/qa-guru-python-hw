import json
import logging
import os
import allure
import requests
from dotenv import load_dotenv

load_dotenv()

resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schema'))


def load_schema(file):
    schema_path = os.path.join(resources_path, file)
    with open(schema_path) as file:
        schema = json.load(file)
        return schema


def send_request(base_url, endpoint, method, **kwargs):
    method = method.lower()
    method_func = getattr(requests, method)
    response = method_func(base_url + endpoint, **kwargs)
    return response


def log_request_and_response_to_allure(request, response):
    request_info = f"URL: {request.url}\nMethod: {request.method}\nHeaders: {request.headers}\n"
    if request.body:
        request_info += f"Body: {request.body}\n"
    allure.attach(
        body=request_info,
        name="Request",
        attachment_type=allure.attachment_type.TEXT,
        extension="txt",
    )
    response_info = f"Status code: {response.status_code}\nHeaders: {response.headers}\nBody:\n{response.text}"
    allure.attach(
        body=response_info,
        name="Response",
        attachment_type=allure.attachment_type.TEXT,
        extension="txt",
    )


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - Response Code: %(status_code)s - URL: %(url)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def log_request_and_response_to_console(response):
    logging.info("Response Code: %s - URL: %s",
                 response.status_code, response.request.url)