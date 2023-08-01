import math

print('****** Lesson 03 ******')

num = 1
name = 'Mike'
is_ok = True

print(num)
print(name)

# typeを出力できるのでデバッグで便利
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# int型が入ってるnumにstrを入れても自動で型が変換される
num = name
print(num, type(num))

# 型変換
new_num = int('100')
print(new_num, type(new_num))

# python3.6から変数に型をつけることができるが、あってもなくても一緒。
num: int = 1

# カンマで区切ると半角スペースをつけれる
print('Hi', 'Mike') # 出力: Hi Mike
# カンマ区切りにしたり、最後に改行も入れられる。
print('Hi', 'Tom', sep=',', end='\n')

# *** 数値の計算 ***
# 冪乗
result = 5 ** 2 # 25
print(result)

# 丸め
pie = 3.1415
print(round(pie, 2)) # 出力 3.14

# 数学関数
result = math.sqrt(25)
print(result)

log = math.log2(10)
print(log)

# ヘルプを見る
# print(help(math))

# *** 文字列 ***
# 改行
print('hello. \nHow are you?')

print('Hi' * 3 + 'Mike')

s = ('aaaaaaaaaaaaaaaaaaaa'
    'bbbbbbbbbbbbbbbbbbbb')
print(s)

# 変数に入れた文字列の連結は「+」を使う
x = 'test'
y = 'sum'
print(x + y)

word = 'python'
print(word[0])
print(word[-1]) # 最後の文字を出力

print(word[0:2]) # py. 初めから2番目まで
print(word[:2]) # 0は省略できる
print(word[1:]) # endも省略できる

# 置換
word = 'j' + word[1:]
print(word)

# ながさ
print(len(word))

s = 'My name is mike.'
is_start = s.startswith('My') # Myから始まっているかどうか
print(is_start)

print(s.find('mike')) # 前から検索。
print(s.find('Mike')) # 見つからなければ-1

print(s.capitalize()) # 小文字に変える
print(s.title()) # 全ての文字の頭文字
print(s.upper())
print(s.lower())
print(s.replace('mike', 'Nancy'))


# 文字列へ変数を代入
test ='a is {}'.format('a')
print(test)

# 最近はこっち
print(f'{test} desu')