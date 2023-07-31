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