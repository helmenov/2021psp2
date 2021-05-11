# day05: クラス

今日は，「クラス」というものを勉強します．

## クラスとは

クラスとは「型」のことです．

例えば，pythonではもともと変数に integer（整数）とfloat（浮動小数点）やbool（2値）などの型があります．
型が決められると実は同じ演算子を使っても，異なる演算が行われます．

例えば，乗算`*`

|  * |    1  |  1.0 | True | 'one' |
|---|---|---|---|---|
| 2 |  2  |  2.0 |    2  | 'oneone'   |
|2.0 |  2.0  | 2.0  | 2.0  |  -  |
|False|  0  |  0.0  |  0  |  ' '  |
|'two'|  'two'  |  -  |  'two'    |    -  |


つまり，型は変数の定義域を決めていると同時に演算(または同じ関数名)に対する挙動も決めているというわけです．

```py
>>> type(int(1))
<class 'int'>

>>> type(1.0)
<class 'float'>

>>> type(True)
<class 'bool'>

>>> type('one')
<class 'str'>
```

演算結果の型は

```py
>>> type(int(2)*int(1))
<class 'int'>

>>> type(int(2)*1.0)
<class 'float>

>>> type(int(2) * True) 
<class 'int'>

>>> type(int(2) * 'one')
<class 'str'>

>>> type(2.0 * 1.0)
<class 'float'>

>>> type(2.0 * True)
<class 'float'>

>>> type(2.0 * 'one')
TypeError: can't multiply sequence by non-int of type 'float'

>>> type(False * True)
<class 'int'>

>>> type(False * 'one')
<class 'str'>

>>> type('two' * 'one')
TypeError: can't multiply sequence by non-int of type 'str'
```

`*`という演算子は，`__mul__(x, y)`という関数に対応することになっています．

クラス（型）は，自分で定義することができます．つまり，'*'演算が行われたときの挙動を自分で決めることができます．

# クラスの書き方

例えば，7の合同数の世界(mod7)のクラスは以下のようになります．
この世界で現れる値は，$\mathbb(F)_7 = \left{0, 1, 2, 3, 4, 5, 6\right}$で表される集合の元（要素）のどれかであり，負をとっても，加算，減算，乗算などの演算のあとにも同じ集合の元になります．

```py
class GF7: 
    def __init__(self, obj): # selfというのはクラス名のことで，__init__という関数は，GF7(val)の挙動を決めます．
        self.val = int(val) % 7
    
    def __neg__(self): # 逆元 演算子'-'
        return GF7(- self.val)

    def __add__(self, other): # 加算 演算子 '+'
        return GF7(self.val + int(other))

    def __sub__(self, other): # 減算 演算子 '-'
        return GF7(self.val - int(other))

    def __mul__(self, arg): # 乗算 演算子 '*'
        return GF7(self.val * int(other))

    def __eq__(self,other): # == 演算子の挙動
        return self.val == other.val
    
    def __int__(self): # int関数の挙動
        return self.val
    
    def __repr__(self): # print関数の挙動
        return str(self.val)
    

```

この上記のコードを`myModule.py`などとして，保存すると
下記のように使えます．

```py
>>> import MyModule as my
>>> a = my.GF7(135) # 135は7の合同数の世界では...
>>> b = my.GF7(1411)
>>> print(a)
2
>>> type(a)
<class 'my.GF7'>
>>> print(b)
4
>>> print(a + b)
6
>>> print(a * b)
1
>>> type(a * b)
<class 'my.GF7'>
```

クラスは，他のクラスを引き継ぐことができます．

以下のコードは，Petクラスの定義．このPetクラスを引き継ぐDogクラスとCatクラスを作ってみます．

```py
class Pet: 
    def __init__(self,name='noname',gene='unknown',age=99):
        self.__name = name
        self.__gene = gene
        self.__age = age
    
    def set_name(self, name):
        self.__name = name
    
    def set_gene(self, gene):
        self.__gene = gene
    
    def set_age(self,age):
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_gene(self):
        return self.__gene

    def get_age(self):
        return self._age
```



```py
class Dog(Pet):
    def __init__(self,name,age):
        super().__init__(name,gene='dog',age)
    def cry(self):
        print('bow-wow')

class Cat(Pet):
    def __init__(self,name,age):
        super().__init__(name,gene='cat',age)
    def cry(self):
        print('mew-mew')

```



    
