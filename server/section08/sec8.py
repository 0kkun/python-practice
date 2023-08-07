##############
# ファイル操作 #
##############

# ファイルを開いて書き込んで閉じる
# f = open('./section08/test.txt', 'w') # a: 追記、w: 書き込み、r:読み取り
# f.write('test\n')
# f.close


# withステートメントを使用するのが推奨されている。
# fを処理が終了後、自動的にcloseしてくれるのでclose忘れがなくなる。
# with open('./section08/test.txt', 'a') as f:
#     f.write('with test\n')


# 読み込み
s = """\
AAA
BBB
CCC
DDD
"""
with open('./section08/test.txt', 'w') as f:
    f.write(s)

with open('./section08/test.txt', 'r') as f:
    # 全て読み込む
    # print(f.read())

    # 1行ずつ読み込む
    # while True:
    #     line = f.readline()
    #     print(line, end='')
    #     if not line:
    #         break

    # 指定文字ずつ読み込む
    chunk_size = 2
    while True:
        line = f.read(chunk_size)
        print(line)
        if not line:
            break

# 書き込み・読み込みモード。wで開いた瞬間中身が空になるので注意
with open('./section08/test.txt', 'w+') as f:
    f.write(s)
    # 現在いる位置が最後のところにいるのでseekで位置を戻す必要がある
    f.seek(0)
    print(f.read())

# 読み込んでから書き込みする
with open('./section08/test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)


# CSV

import csv

# 生成・書き込み
with open('./section08/test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

# 読み込み
with open('./section08/test.csv', 'r') as csv_file:
    rows = csv.DictReader(csv_file)
    for row in rows:
        print(row['Name'], row['Count'])

# os

import os
import pathlib
import glob
import shutil

is_exist_file = os.path.exists('./section08/test.txt')
is_file = os.path.isfile('./section08/test.txt')
is_dir = os.path.isdir('./section08/test.txt')

# os.rename('./section08/test.txt', 'renamed.txt')
# os.mkdir()
# os.rmdir()
# os.listdir() 一覧表示
# os.getcwd() 現在位置取得

print(is_exist_file)

# 空のファイルを作成
# pathlib.Path('empty.txt').touch()

# 全て表示する
print(glob.glob('./section08/*'))
# 出力 : ['./section08/__init__.py', './section08/__pycache__', './section08/sec8.py', './section08/test.csv', './section08/test.txt']

print(os.listdir('./section08'))
# 出力 : ['.gitignore', '__init__.py', '__pycache__', 'sec8.py', 'test.csv', 'test.txt']

# コピー
# shutil.copy('ディレクトリ指定', '移動先')

# 中身も含めてディレクトリ削除
# shutil.rmtree('ディレクトリ名')


# tarファイル
import tarfile

# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('./section08/test_dir')


# zipファイル
import zipfile

# with zipfile.ZipFile('test.zip', 'w') as z:
#     # z.write('test_dir')
#     # z.write('test_dir/test.txt')
#     for f in glob.glob('test_dir/**', recursive=True):
#         z.write(f)

# ターミナルのコマンドを実行する
import subprocess

r = subprocess.run(['ls', '-al'])
print(r) # CompletedProcess(args=['ls'], returncode=0)
# シェルインジェクション対策で、パイプとか使用できないようにすること。セキュリティ的に良くない。以下のようにするのがおすすめ
process1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
process2 = subprocess.Popen(['grep', 'test'], stdin=process1.stdout, stdout=subprocess.PIPE)
process1.stdout.close()
output = process2.communicate()[0]
print(output)


# datetime
import datetime

now = datetime.datetime.now()
print(now)             # 2023-08-07 12:24:38.914447
print(now.isoformat()) # 2023-08-07T12:25:12.577225
print(now.strftime('%d/%m/%y - %H%M%S%f')) # 07/08/23 - 122633141304
print(now.strftime('%Y-%m-%d - %H:%M:%S')) # 2023-08-07 - 12:28:41

today = datetime.datetime.today()

time = datetime.time(hour=1, minute=10, second=5, microsecond=100)

print(time) # 01:10:05.000100