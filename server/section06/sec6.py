# モジュールとパッケージ

# 組み込み関数
import builtins

# 組み込み関数一覧
# https://docs.python.org/ja/3.9/library/functions.html

builtins.print()

ranking = {
    'A': 90,
    'B': 100,
    'C': 10
}

# バリューを元にソートする。そしてキーを表示する。
print(sorted(ranking, key=ranking.get, reverse=True))

# collections
# defaultdict 
# 各文字がいくつ入っているか調べる時に使う。
s = "dsafdasfawehadagfdf"

d = {}

for c in s:
    # if c not in d:
    #     d[c] = 0
    # 上記を以下のようにかける
    d.setdefault(c, 0)

    d[c] += 1



from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1

print(d)
# defaultdict(<class 'int'>, {'d': 4, 's': 2, 'a': 5, 'f': 4, 'w': 1, 'e': 1, 'h': 1, 'g': 1})

import termcolor

print(termcolor.colored('colort test!', 'red'))

# 以下でインストールされている場所がわかる。
print(termcolor.__file__)
# /usr/local/lib/python3.9/site-packages/termcolor/__init__.py

# ライブラリのimport順は、アルファベット順が良い。
# 標準ライブラリと、サードパーティ製ライブラリの間には改行1行入れて分けると良い
# 1.標準ライブラリ、2. サードパーティ製、3. 自分が作成したらパッケージ、4. ローカルファイルの順が見やすいらしい。

print('sec6', __name__)
# sec6 section06.sec6

