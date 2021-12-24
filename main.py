import argparse     #cmd 参数
from subprocess import *    #cmd命令
import threading    #线程
import bin
import colorama #cmd颜色
from colorama import Fore, Back, Style

colorama.init()

print('')


# 获取cmd参数
def cmd():
    parser = argparse.ArgumentParser(description='小白开发')
    parser.add_argument('-i', action='store')  # 定义参数-i
    data = parser.parse_known_args()  # 获取所有参数输入
    data1 = data[0].i
    data2 = data1
    for i in data[1]:
        data2 = data2 + " " + i
    return data2 + "\n"


# 标准输出
def cmds(data):
    tmp = ''
    while 1:
        a = data.readline()
        tmp = tmp + a
        if a == '':
            pass
        else:
            print(a, end='')




# 错误输出
def cmdr(data):
    while 1:
        a = data.readline()
        if a == '':
            pass
        else:
            print(a, end='')
            print(Fore.RED + bin.fanyi(a) + Style.RESET_ALL)


# 开启终端
p = Popen("cmd", bufsize=0, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
p.stdin.write(cmd())
# 开启标准输出线程
t = threading.Thread(target=cmds, name="stdout", args=(p.stdout,))
t.start()

# 开启错误输出线程
t1 = threading.Thread(target=cmdr, name="stderr", args=(p.stderr,))
t1.start()

while 1:
    tmp = input() + "\n"
    p.stdin.write(tmp)
