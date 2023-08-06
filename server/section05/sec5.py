a = 10
b = 20

if a >= 0:
    print('a is positive')
    if b >= 0:
        print('b is positive')
else:
    print('both a and b is negative')

y = [1, 2, 3]
x = 1

if x in y:
    print('x in y')

if 100 not in y:
    print('100 not in y')

# 直が入っていない場合のハンドリング
# 数値の0、配列の[]、'', ()などはFalseと判定される
# 変数に何か入って入ればTrueと判定される
# 何も入っていないければpythonではNoneTypeのNoneが入る。

# Noneの判定
is_empty = None

if is_empty is None:
    print('None!!')

# isはオブジェクトの判定をしたい時に使う。Noneを判定するときによく使う。
# 通常は==で判定していくのがセオリー

# while文
count = 0
while count < 5:
    print(count)
    count += 1

count = 0
# 違う書き方
while True:
    if count >= 10:
        break

    if count == 7:
        count += 1
        continue

    count += 1
    print(count)


# 2から始めて10まで、3個とばしでfor文を回す
for i in range(2, 10, 3):
    print(i)

# enumerate関数 index付きで展開する
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 orange

# zip関数
days = ['mon', 'tue']
fruits = ['apple', 'banana']
drinks = ['coffee', 'tea']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# 辞書型をfor文で回す
dic = {'x': 100, 'y': 200}

for key, value in dic.items():
    print(key, value)

# 関数定義
def say_something():
    print('Hello')

say_something()

# 以下のように実行することもできる
f = say_something
f()

def what_is_this(color):
    print(color)

what_is_this('red')

# listはデフォルト引数[]を与えるべきではない。参照渡しになって直が保持されてしまう。
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

# 位置引数. *argsとするとタプルにしてくれる.引数を無限に増やせる.
def say_something(*args):
    print(args)

say_something('hi', 'nancy', 'mike')

# キーワード引数の辞書化
def menu(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print('key:', key)
        print('value:', value)

menu(main='beef', drink='beer')

# 以下のように**で渡すと見やすくなる。
d = {
    'main': 'fish',
    'drink': 'coffee',
    'dessert': 'ice'
}

menu(**d)

def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('banana', 'arg1', 'arg2', main='fish', drink='coffee')
# 出力:
# banana
# ('arg1', 'arg2')
# {'main': 'fish', 'drink': 'coffee'}

# クロージャー
def outer(a, b):
    
    def inner():
        return a + b
    return inner

# 今すぐ実行したくない時に使う。
func = outer(1, 2)

result = func()
print(result)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

# 引数違いでfuncを用意したい時に便利。
cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

result = cal1(10)
print(result)

# デコレータ
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(10, 20)
print(r)

# デコレータをつけると、
@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 100)
print(r)

# デコレータを複数つけることもできる。
# デコレータは何かを包み込んでいくイメージ。
def print_more(func):
    def wrapper(*args, **kwargs):
        print(1)
        print(2)
        result = func(*args, **kwargs)
        print(3)
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(100, 200)
print(r)
# 実行結果:
# start
# 1
# 2
# 3
# end
# 300
# こんなイメージ : print_info(print_more(add_num))

# ラムダ


def change_words(words, func):
        for word in words:
            print(func(word))

def sample_func(word):
    return word.capitalize()

# 上記は1行でかける
sample_func = lambda word: word.capitalize()

words = ['mon', 'tue', 'wed', 'Thu']

result = change_words(words, sample_func)


# ジェネレータ
# yieldで一旦返す。nextで次に進む。1要素ずつ取り出して生成していく. returnがない。状態を保持する。
# もうこれ以上yieldがない場合はStopIterationErrorが返される。
def greeting():
    yield 1
    yield 2
    yield 3

g = greeting()
print(next(g))

print('***')

print(next(g))

print('***')

print(next(g))

print('***')

# リスト内包表記
t = (1, 2, 3, 4, 5)
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

# 1行で取り出せる。
r = [i for i in t]
print(r)

# 1行で条件も含めてかける
r = [i for i in t if i % 2 == 0]
print(r)

# 辞書の内包表記
weeks = ['mon', 'tue', 'wed']
drinks = ['coffee', 'milk', 'water']

d = {}
for key, value in zip(weeks, drinks):
    d[key] = value
    
print(d)

# 上記を1行でかける。
d = {key: value for key, value in zip (weeks, drinks)}
print(d)

# ジェネレータ内包表記

def generate():
    for i in range(10):
        yield i

g = generate()

g = (i for i in range(10) if i % 2 == 0)
print(type(g))

for x in g:
    print(x)

# 変数一覧が見れる
# print('globals', globals())

# print('locals', locals())

# 例外処理


l = [1, 2, 3]

i = 5

try:
    l[i]
except Exception as e:
    print("Exception Catched:{}".format(e))
else:
    # 正常に実行できたら実行したいもの
    print("done")
finally:
    # 何があろうと最後に以下を実行する
    print("clean up")

# 例外のカスタマイズ

# raise IndexError('Index Error!!')

class UppercaseError(Exception):
    # ここにカスタマイズしたい内容を書く。
    pass

def check():
    words = ['APPLE', 'orange']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as e:
    print('This is my fault.')

