"""
requests_api.py
~~~~

This module implements the Requests API.

:copyright: (c) 2023 by Be square.
"""
# import 'requests' module
import requests
# import 'json' module
import json
# import 'JsonFiles' module
from JsonFiles import *
# import 'os' module
import os
# import 'Constants' module
from Constants import *
# import 'logging' module
import logging

# Configure the logger
logging.basicConfig(filename='request_api.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


class ServiceInteractions:
    """
     ServiceInteractions class is to communicate with the web services

        Attributes
        ----------
            This class having attributes
            method (str): ("GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", or "DELETE").
            url (str): url name
            params (str): query parameters for request
            data (str): pass the data through request
            headers (str): request headers('Accept', 'Content-Type', 'Authorization',....)

        Methods
        -------
            This class having one method
            request(): sending api request to get the response

            """

    def __init__(self, method, url, params=None, data=None, headers=None):
        """
        Constructor method of the class ServiceInteractions.

        :param method: ("GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", or "DELETE").
        :param url: url name
        :params (str): query parameters for request
        :data (str): pass the data through request
        :param headers: request headers('Accept', 'Content-Type', 'Authorization',....)

        """
        self.method = method
        self.url = url
        self.params = params
        self.data = data
        self.headers = headers

    def request(self):
        """
        :return: class: 'status_code & content of the Response'
        """
        try:
            session = requests.Session()
            response = session.request(method=self.method, url=self.url, params=self.params,
                                       data=self.data, headers=self.headers)
            # Getting the status_code of the 'Response'
            status_code = response.status_code
            # Getting the content of the 'Response'
            content = response.content
            # returns the status_code, content of the response
            return status_code, content
        except requests.exceptions.RequestException as error:
            # logs the exception error in a file
            logging.exception(f"Exception occurred while making a request to {self.url}. "
                              f"Error: {str(error)}")
            # returns None
            return None, None


def main():
    # Get a list of JSON files from the given folder path
    json_files = JsonFiles(os.path.join(os.getcwd(), Constants.FOLDER))
    # Read the JSON files from an object json_files
    read = json_files.read_json()
    for obj in read:
        with open(Constants.FOLDER + obj) as f:
            file = json.load(f)
            # Get an 'service_name' from an JSON files
            service_name = file["service_name"]
            test_case = file["tests"]
            for keys in test_case:
                # print("tc:", keys)
                test_keys = file["tests"][keys]
                endpoint = test_keys["endpoint"]
                operation = test_keys['operation']
        # Check the 'Set or set' word in ServiceName
        if service_name in ["Set", "set"]:
            # Creating an object 'service_interaction' to store the class 'ServiceInteractions'
            service_interaction = ServiceInteractions({operation}, f"{Constants.BASE_URL}{endpoint}",
                                                      {'iP': {Constants.IP}, 'port': {Constants.PORT}},
                                                      data=None, headers=None)
            # Calling the request() method by using object 'service_interaction'
            res = service_interaction.request()
            # Calling the first index position of the content
            status_code = res[0]
            # Calling the second index position of the content
            content = res[1]
            # logs a message with a timestamp
            logging.info(f"service_name: {service_name}, test_cases: {keys},"
                         f"status_code: {status_code}, content: {content}")
        # Check the service_name is startswith with 'SRLC' word
        elif service_name.startswith('SRLC'):
            # Check the 'Set or set' word in ServiceName
            if service_name in ["Set", "set"]:
                # Creating an object 'SI' to store the class 'ServiceInteractions'
                service_interaction = ServiceInteractions({operation}, f"{Constants.BASE_URL}{endpoint}",
                                                          {'iP': {Constants.IP_SRLC},
                                                           'port': {Constants.PORT}}, data=None, headers=None)
                # Calling the request() method by using object 'service_interaction'
                res = service_interaction.request()
                # Calling the first index position of the content
                status_code = res[0]
                # Calling the second index position of the content
                content = res[1]
                # logs a message with a timestamp
                logging.info(f"service_name: {service_name}, test_cases: {keys},"
                             f"status_code: {status_code}, content: {content}")
            else:
                # Creating an object 'SI' to store the class 'ServiceInteractions'
                service_interaction = ServiceInteractions({operation}, f"{Constants.BASE_URL}{endpoint}",
                                                          {'iP': {Constants.IP_SRLC},
                                                           'port': {Constants.PORT}}, data=None, headers=None)
                # Calling the request() method by using object 'service_interaction'
                res = service_interaction.request()
                # Calling the first index position of the content
                status_code = res[0]
                # Calling the second index position of the content
                content = res[1]
                # logs a message with a timestamp
                logging.info(f"service_name: {service_name}, test_cases: {keys},"
                             f"status_code: {status_code}, content: {content}")
        else:
            # Creating an object 'SI' to store the class 'ServiceInteractions'
            service_interaction = ServiceInteractions({operation}, f"{Constants.BASE_URL}{endpoint}",
                                                      {'iP': {Constants.IP},
                                                       'port': {Constants.PORT}}, data=None, headers=None)
            # Calling the request() method by using object 'service_interaction'
            res = service_interaction.request()
            # Calling the first index position of the content
            status_code = res[0]
            # Calling the second index position of the content
            content = res[1]
            # logs a message with a timestamp
            logging.info(f"service_name: {service_name}, test_cases: {keys},"
                         f"status_code: {status_code}, content: {content}")


# Calling main function
if __name__ == '__main__':
    main()
