# coding: utf-8
import requests


class chatting:
    def __init__(self, api_base_url, account_id, api_token, model):
        '''
        :param api_base_url: API 端点 url
        :param account_id: 账户 id
        :param api_token: API Token (需 Workers AI 权限)
        :param model: 使用模型
        '''
        self.api_base_url = api_base_url.format(account_id=account_id)
        self.account_id = account_id
        self.api_token = api_token
        self.model = model
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    def run(self, conversation):
        '''
        :param conversation: 对话体 (列表)
        '''
        inputjson = {"messages": conversation}
        response = requests.post(
            f"{self.api_base_url}{self.model}", headers=self.headers, json=inputjson)
        return response.json()
