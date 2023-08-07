# クラスとオブジェクト

class Person(object):
    def __init__(self, name: str) -> None:
        self.name = name

    def say_something(self):
        print('hello')
        
    def __del__(self):
        print('good bye')

person = Person(name='Tom')

person.say_something()

print(person.name)

del person

# 継承
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.auto_run()

# オーバーライド
class MatsudaCar(Car):
    def __init__(self, model=None, is_enable=False):
        # 親クラスのinitを呼び出す
        super().__init__(model)
        self.is_enable = is_enable

    def run(self):
        print('オーバーライド')

matsuda_car = MatsudaCar(model='test', is_enable=True)
matsuda_car.run()

# クラスのプロパティ
# 外から直を勝手に書き換えられたくない場合は、以下のように@propertyをつける

class DaihatsuCar(Car):
    def __init__(self, model=None, is_enable=False):
        super().__init__(model)
        self._is_enable = is_enable
        
    @property
    def is_enable(self):
        return self._is_enable

daihatsu_car = DaihatsuCar()

print(daihatsu_car.is_enable) # 読み込みはできる

try:
    daihatsu_car.is_enable = True
except Exception as e:
    print('プロパティの書き換えはできない')

# アンダースコア2個を頭につければ、クラス外からアクセスできないようにできる。新たにプロパティを生成することになる。
# @is_enable.setter をつければ書き換えできるようになる


# オブジェクト指向のサンプル
class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('no drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        super().__init__(age)
        if age >= 18:
            super().__init__(age)
        else:
            ValueError

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def ride(self, person):
        person.drive()

baby = Baby()
adult = Adult()
car = Car()

car.ride(adult) # babyを入れるとException、adultならok




# インターフェース (抽象クラス) あまり多用しない方が良いらしい。
import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # このクラスを継承したら必ず実装するメソッドの指定
    @abc.abstractmethod
    def drive(self):
        pass

# @staticmethod : オブジェクトを生成しなくても使用できるようにする。クラス外に設置しても動作が変わらないもの。
# @classmethod : オブジェクトを生成しなくても使用できるようにする。クラス内のプロパティにアクセスする必要があるメソッド。

# オブジェクトの特殊メソッド
# __str_、 __len__、__add__、__eq__
# オブジェクト同士を + 、比較などした時に呼ばれるメソッド
