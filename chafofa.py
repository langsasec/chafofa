# -*- coding: UTF-8 -*-
# @Time:  11:40
# @Author: 浪飒
# @File: chafofa.py
# @Software: PyCharm
import base64
import json
import time
import click
import requests
import xlwt


def Welcome():
    print('''    
                查fofa命令行工具 author:浪飒
   ________  _____       __________  _________ 
  / ____/ / / /   |     / ____/ __ \/ ____/   |
 / /   / /_/ / /| |    / /_  / / / / /_  / /| |
/ /___/ __  / ___ |   / __/ / /_/ / __/ / ___ |
\____/_/ /_/_/  |_|  /_/    \____/_/   /_/  |_|                                  

Options:
  -f TEXT     请输入fofa查询语法
  -s INTEGER  请输入所要查询的条数，默认100条
  --help      Show this message and exit.
        ''')


def jm_base64(string):
    return base64.b64encode(string.encode('utf-8'))


@click.command()
@click.option("-f", help="请输入fofa查询语法", prompt="请输入fofa查询语法")
@click.option("-s", default=100, help="请输入所要查询的条数，默认100条")
def chafofa(f, s):
    qbase64 = str(jm_base64(f), 'UTF-8')
    req = f"https://fofa.info/api/v1/search/all?email=3540005812@qq.com&key=a5f1003dfd75df0e642950536c41bddc&qbase64={qbase64}&size={s}&fields=ip,host,port,protocol,title,server"
    res = requests.get(req).content.decode("utf-8")
    dict_data = json.loads(res)  # json转成python字典
    results = dict_data.get('results')
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(f'{f}_fofa查询结果', cell_overwrite_ok=True)
    col = ('IP', 'host', '端口', '协议', '网站标题', '网站server')
    for i in range(0, 6):
        sheet.write(0, i, col[i])
    for i in range(len(results)):
        data=results[i]
        for j in range(0, 6):
            sheet.write(i+1, j, data[j])
    path=f'{f}_{str(time.time().__hash__())}_fofa查询结果.xls'
    book.save(path)
    print(f"表格已保存为{path}")


if __name__ == '__main__':
    Welcome()
    chafofa()
