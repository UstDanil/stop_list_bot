import os
import requests
import logging

IIKO_API_LOGIN = os.getenv("IIKO_API_LOGIN")
REST_SHORT_NAMES_FOR_API = ['Перерва']

logger = logging.getLogger('app')


class IikoIntegration:
    access_token_url = 'https://api-ru.iiko.services/api/1/access_token'
    organizations_url = 'https://api-ru.iiko.services/api/1/organizations'
    nomenclature_url = 'https://api-ru.iiko.services/api/1/nomenclature'
    stop_list_url = 'https://api-ru.iiko.services/api/1/stop_lists'

    def __init__(self):
        self.access_token = self.get_access_token()
        self.authorization_header = {'Authorization': f'Bearer {self.access_token}'}
        self.restaurant_id_for_api = None

    def get_access_token(self):
        try:
            token_response = requests.post(self.access_token_url, json={"apiLogin": IIKO_API_LOGIN})
            access_token = token_response.json()["token"]
            return access_token
        except Exception as e:
            logger.error(e, exc_info=True)

    def get_restaurants(self):
        try:
            data = {"organizationIds": [], "returnAdditionalInfo": False, "includeDisabled": False}
            org_response = requests.post(self.organizations_url, json=data, headers=self.authorization_header)
            organizations = org_response.json()['organizations']
            return organizations
        except Exception as e:
            logger.error(e, exc_info=True)

    def get_restaurant_for_api(self):
        try:
            organizations = self.get_restaurants()
            for organization in organizations:
                if any([organization["name"].find(name) != -1 for name in REST_SHORT_NAMES_FOR_API]):
                    return organization["id"]
            return organizations[0]["id"]
        except Exception as e:
            logger.error(e, exc_info=True)

    def get_menu(self):
        try:
            if not self.restaurant_id_for_api:
                self.restaurant_id_for_api = self.get_restaurant_for_api()

            data = {"organizationId": self.restaurant_id_for_api, "startRevision": 0}
            menu_response = requests.post(self.nomenclature_url, json=data, headers=self.authorization_header)
            menu = menu_response.json()
            return menu
        except Exception as e:
            logger.error(e, exc_info=True)

    def get_stop_list(self, restaurant_id):
        try:
            data = {"organizationIds": [restaurant_id], "startRevision": 0}
            stop_list_response = requests.post(self.stop_list_url, json=data, headers=self.authorization_header)
            stop_list = stop_list_response.json()
            items = list()
            for terminal_group_stop_list in stop_list["terminalGroupStopLists"]:
                for term_items in terminal_group_stop_list["items"]:
                    items.extend(term_items["items"])
            return items
        except Exception as e:
            logger.error(e, exc_info=True)

