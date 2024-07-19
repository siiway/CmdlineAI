#coding:utf-8
# Configs

# 是否显示调试信息
DEBUG = False

# Account ID
ACCOUNT_ID = ''

# API Token
API_TOKEN = ''

# API Base URL, Default: f'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/'
API_BASE_URL = f'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/'

# Model 运行使用的模型
# MODEL = "@cf/meta/llama-2-7b-chat-int8"
# MODEL = '@cf/qwen/qwen1.5-7b-chat-awq'
MODEL = '@cf/qwen/qwen1.5-14b-chat-awq'

# Prompt 模型提示词
#PROMPT = "现在你是一个ai助手，立志于为用户解决编程方面的各种问题。\n注意：在用户未指定回答语言的情况下，请使用中文回答！！！"
PROMPT = ''

# Prompt will show when input 输入时的提示词
PROMPT_WHEN_INPUT = ''