
print('****** Lesson 04 ******')

l1 = [1,2,3,5,6]

print(l1, type(l1))
print(l1[:]) # 全て選択

# 分割して格納
l2 = list('abcde')
print(l2) # 出力: ['a', 'b', 'c', 'd', 'e']

# 2つとばしで抽出したい時
print(l2[::2]) # 出力: ['a', 'c', 'e']

# 逆順に抽出
print(l2[::-1]) # 出力: ['e', 'd', 'c', 'b', 'a']

# list in list
a = ['a', 'b', 'c', 'd']
b = [1, 2, 3]
l3 = [a, b]
print(l3) # 出力: [['a', 'b', 'c', 'd'], [1, 2, 3]]

# リストの操作
s = ['a', 'b', 'c', 'd', 'e']
s[0] = 'X'
print(s) # ['X', 'b', 'c', 'd', 'e']

s[2:5] = ['C', 'D', 'E']
print(s) # ['X', 'b', 'C', 'D', 'E']

# 後ろに追加
s.append(100)
print(s) # ['X', 'b', 'C', 'D', 'E', 100]

# 　指定した位置に追加
s.insert(0, 50)
print(s) # [50, 'X', 'b', 'C', 'D', 'E', 100]

# 指定した位置のものを取り除く
s.pop(0)
print(s) # ['X', 'b', 'C', 'D', 'E', 100]

# こっちでもいけるが強力なので気を付けること
del s[0]
print(s) # ['b', 'C', 'D', 'E', 100]

# 指定したものを取り除く
s.remove('b')
print(s) # ['C', 'D', 'E', 100]

# 配列の連結
x = [1, 2, 3]
y = [4, 5, 6]

print(x + y) # [1, 2, 3, 4, 5, 6]
# こっちでもいい。
x += y
print(x) # [1, 2, 3, 4, 5, 6]
# こっちでも良い
x.extend(y)
print(x) # [1, 2, 3, 4, 5, 6, 4, 5, 6]

r = [1, 2, 3, 4, 5, 1, 2, 3]

# 3を配列から探す
print(r.index(3)) # 2

# 3番目以降のインデックスから探す
print(r.index(3, 3)) # 7

# 3がいくつかカウントする
print(r.count(3)) # 2

if 5 in r:
    print('exist')

# 昇順でソート
r.sort()
print(r)

# 降順でソート
r.reverse()
print(r)

# 文字列を分割する
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split) # ['My', 'name', 'is', 'Mike']

# 繋げる
origin = ' '.join(to_split)
print(origin) # My name is Mike

# print(help(list))

# リストのコピー

i = [1, 2, 3, 4, 5]
print('i=', i)
# コピーしたい場合は、普通にやると参照渡しになってしまうので、copyしてあたい渡しにする
j = i.copy()
print(j)
print(id(j))
print(id(i))

# idが同じになってしまう。
j = i
print(id(j))
print(id(i))

# タプル型
t = (1, 2, 3, 4, 5)
s = 4, 5, 6 # カンマがついたらタプル型になる
# 再代入不可。読み込み専用
# countとindexくらいしかメソッドはない。操作系のメソッドがない。
print(type(t))

# タプル内にlistを入れることもできる。list内は操作可能
t = ([1, 2, 3], 1, 2, 3, 4)

# タプルのアンパッキング(展開)
num_tuple = (10, 20)
min, max = num_tuple
print(min, max) # 10 20

# 直の入れ替え
min, max = max, min
print(min, max) # 20 10

# 辞書型 (連想配列)
d = {'x': 1, 'y': 2}
print(d['x']) # 1

dic = dict(a=10, b=20)
print(dic['a']) # 10

# 辞書型のメソッド
print(d.keys()) # dict_keys(['x', 'y'])
print(d.values()) # dict_values([1, 2])

d2 = {'x': 100, 'j': 200}

# xは置き換えて、jを末尾に追加する
d.update(d2)
print(d) # {'x': 100, 'y': 2, 'j': 200}

# 取得する。ない場合はNonTypeが返される
print(d.get('x'))

# 特定のキーを削除する
d.pop('x')
print(d) # {'y': 2, 'j': 200}

# 全て削除する
d.clear()
print(d)

# キーがあるかどうか判定する
if 'j' in d:
    print('exist')
else:
    print('non')

# 集合. 辞書型は同じキーのものはまとめられてしまう。辞書型の変数同士の共通点を見つけるときに便利。
a = {1, 2, 3, 2, 3, 4}
print(a) # {1, 2, 3, 4}

# 集合型
s = {10, 20, 30, 50, 50}
print(type(s))
print(s)

# サンプル練習
# books = {
#         0: {'name': '君の名は', 'price': 100},
#         1: {'name': 'となりのトトロ', 'price': 200},
#         2: {'name': 'となりのトトロ', 'price': 200},
#     }

# print('******************************************************')
# for book_id, book_info in books.items():
#     print(f"Book ID: {book_id}, Book Name: {book_info['name']}, Price: {book_info['price']}")
# print('******************************************************')

# selected_book_num = input("please select book number :")
# print('your input value is:', books[int(selected_book_num)])

# 上記よりも以下の方が良さそう。
# books = [
#         {'name': '君の名は', 'price': 100},
#         {'name': 'となりのトトロ', 'price': 200},
#         {'name': 'となりのトトロ', 'price': 200},
#     ]

# print('******************************************************')
# for book_id, book_info in enumerate(books): # インデックスと本の情報を取得
#     print(f"Book ID: {book_id}, Book Name: {book_info['name']}, Price: {book_info['price']}")
# print('******************************************************')

# selected_book_num = input("please select book number :")
# print('your input value is:', books[int(selected_book_num)])