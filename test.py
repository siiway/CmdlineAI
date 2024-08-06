import io
import time
import sys
# 创建一个StringIO对象
output = io.StringIO()

# print("willdel", file=output)
# print("清空前的输出：", output.getvalue())  # 获取StringIO对象中的输出内容
print(123)
print(456)
input('ok?')
time.sleep(1)

# 清空输出
sys.stdout.flush()

# print("清空后的输出：", output.getvalue())
b = '\033[F\033[K'
print(f'{b}{b}aaa', end='')