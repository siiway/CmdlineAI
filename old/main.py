#!/usr/bin/python3
import requests
from config import *

global inputs
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def debug(content):
    if DEBUG:
        print(f'[DEBUG] {content}')


def run(model, inputs):
    input = {"messages": inputs}
    response = requests.post(
        f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


print('''
---
[Tips]
- /s -> 发送
- /q or /e -> 退出本轮对话
''')

inputs = [
    {"role": "system", "content": PROMPT},
    # {"role": "user", "content": "你是谁？"},
    # "role": "assistant", "content": "aaaa"},
]

while True:
    msg = ''
    print('''
---
[Input]''')
    while True:
        msgn = input(PROMPT_WHEN_INPUT)
        match msgn:
            case '/s':
                break
            case '/q':
                exit()
            case '/e':
                exit()
            case _:
                msg += f'{msgn}\n'

    inputs += [{"role": "user", "content": msg},]
    debug(f'inputs: {inputs}')

    output = run(MODEL, inputs)
    debug(f'output: {output}')
    print(f'''
---
[Response]
success: {output['success']}
response:
`"
{output['result']['response']}
"`''')
    if output['success']:
        inputs += [{"role": "assistant",
                    "content": output['result']['response']}]
    else:
        print(f'''errors: {output['errors']}
messages: {output[messages]}''')
