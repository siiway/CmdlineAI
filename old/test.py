import requests
from config import *


headers = {"Authorization": f"Bearer {API_TOKEN}"}


def run(model, inputs):
    input = {"messages": inputs}
    response = requests.post(
        f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    {"role": "system", "content": "现在你是一个ai助手，立志于为用户解决编程方面的各种问题。\n注意：在用户未指定回答语言的情况下，请使用中文回答！！！"},
    {"role": "user", "content": "你是谁？"}
]
output = run(MODEL, inputs)
print(output)
