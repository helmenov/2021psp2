# day05: クラス

今日は，「クラス」というものを勉強します．

(あと，ついでに...．***資料で紹介しているコードはコピーせずにぜひ自分で書いて試してください．これを「写経」といってプログラミング上達のコツです．もし私のコードに間違いを発見したら指摘してください．***)

## クラスとは

クラスとは「型」のことです．

例えば，pythonではもともと変数に integer（整数）とfloat（浮動小数点）やbool（2値）などの型があります．
型が決められると実は同じ演算子を使っても，異なる演算が行われます．

例えば，乗算「`*`」演算子の左右の変数の組み合わせの計算結果を表にあらわすと，

|  * |    1  |  1.0 | True | 'one' |
|---|---|---|---|---|
| 2 |  2  |  2.0 |    2  | 'oneone'   |
|2.0 |  2.0  | 2.0  | 2.0  |  -  |
|False|  0  |  0.0  |  0  |  ' '  |
|'two'|  'two'  |  -  |  'two'    |    -  |

(`-`は型エラーとなる組み合わせ)

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

クラス（型）は，自分で定義することができます．つまり，`*` などの演算や関数が呼び出されたときの挙動を自分で決めることができます．

# クラスの書き方

## 関数の復習

関数は

```py
#
# mymodule.py
#
def func(arg1, arg2=100):
    ret = arg1 + arg2
    return ret
```

のように書くのでした．`arg2=100`となっているのは，`arg2`が与えられなかったときに，`arg2=100`を処理させたいからです．この関数を使うときは，関数が書いてあるファイル（モジュール）`mymodule.py`をインポートして，

```py
>>> import mymodule as my

>>> a = 10
>>> b = 20
>>> c = func(a,b)
>>> print(c)
30
```

のように実行されるのでした．

arg1とarg2は**仮引数**(アーギュメント, argument)であり，呼び出す側（使う側）の `func(a,b)`という処理は，関数の側では

```py
arg1 = 10
arg2 = 20
```

という仮引数への実現値の代入が行われた後に，関数内部に入ります．関数は`return`の値を呼び出し側に返すので，`c=30`となるわけです．

注意すべきは， 

> 関数に渡されるのは，変数`a`,`b`ではなく，その中に格納されている実現値の`10`,`20`であるという点です．

このことから，関数の呼び出しの授受はよく **「値渡し」** と呼ばれます．（***コレ大事***）

## クラス

クラスは次のように書きます．

```py
## mymodule2.py ##
class Dog():
    def __init__(self, val):
        """
        コンストラクタ (constructor)
        x = Dog(n)
        xに犬番号nを割り当てる．
        """
        self.value = int(val)
    
    def __add__(self, arg):
        """
        予約メソッド (reserved method)
        Dog型のxに対する x + y は 整数の加算を返却
        """
        return self.value + int(arg)

    def bow(self, arg):
        """
        自作メソッド Dog.bow(n)
        - n回吠える

        Input
        - n (int) : 吠える回数
        
        Dog型であるxに対する x.bow(3) は
        Dog x : bowbowbow
        をプリントする．
        """
        cry = 'bow'*int(arg)
        print('dog', self.value, ':', cry)
```

**関数その他をつつんでいます．**

包まれている関数，変数は，クラスの**属性（attributes, アトリビュート）** と呼び，クラス`Dog`の変数`x`の属性`value`は変数と属性名の間にドット「`.`」を置いて，`x.value`と書きます．

メソッドも属性ですので，`x.__add__(3)`や，`x.bow(2)`などと書きます．

呼び出し側は，

```py
>>> import mymodule2 as my

>>> x = my.Dog(100)
>>> print(x + 1)
101
>>> x.bow(3)
dog 100: bowbowbow
```

と実行されます．

## `__init__`,`self` 

`__init__`という名前のメソッドは「**コンストラクタ**」と呼ばれ，変数にクラスを割り当てるときに使う「名前がクラス名の関数」です．

`self`という仮引数は，`x.method(y)`における`x`です．

ついでに呼び出し側で引数で与える`y`はモジュール側`def method(self, arg)`における第2引数`arg`に代入されます．

`__init__(self, val)`というメソッドは，`x = my.Dog(100)`とクラスに割り当てたときに，呼び出されます．今回は引数をつけていますが，つけなくても構いません．

（引数なしのコンストラクタは`__init__(self)`で，呼び出しは`x = my.Dog()`です．）

今回の場合，`x = my.Dog(100)`と呼び出すと，`self = x`，`val = 100`が代入され，`x.value = 100`という属性変数`value`への代入が行われています．

## `__add__`

冒頭で組み合わせ表に示した「`*`」という演算子は後ろに置かれる変数を引数にして，`__mul__(self, value)`という予約メソッド（**組み込みメソッド**）に対応することになっています．

`x * y`という演算は，内部的には`x.__mul__(y)`という処理が行われます．（`f = func(x,y)`を**関数**，`f=x.func(y)`を`x`の**メソッド**と呼ぶのでした）

ちなみに，``__``（下線2本，アンダーバー・アンダーバー，通称「ダンダー(dunder)」）で囲むことで特別扱いして，簡単に同名の関数を作られないようにしています．

Dogクラスの`__add__`も演算子「`+`」に対応する予約メソッドです．`__add__`メソッドの定義の中で`+`演算を行なっていますが，`self.value`も`int(arg)`も`int`型（クラス）であり，`Dog`クラスではないので， **ここの`+`は，再定義した`__add__`が使われないことに注意です．**

## クラス内関数（メソッド）

`def bow(self,arg)`は`x.bow(3)`と呼び出されたときに，`self=x`, `arg=3`と代入されて，動き出しますが，print文の中で，
 
 ```py
 print('dog', self, ':', cry)
 ```

 のように`self`をそのまま使わず，`self.value`を使っていることに注意してください．誤解しがちですが，

 ```py
 x = my.Dog(100)
 ```

では，`x = 100`の代入ではなく，`x.value = 100`という代入が行われていて，`x`は数値を代入されていません．

# （課題）分数クラスを作ろう

<!-- $0.1+0.2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.1%2B0.2">はいくらでしょうか？数学的には当然<!-- $0.3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.3">です．これをコンピュータで計算してみます．

```py
>>> 0.1 + 0.2
```

`0.3` ではないものが出力されたのではないでしょうか．プログラム概論の中で，このような小数点つき数値を浮動小数点 float で表す方法について紹介しました．

復習します．まず計算機の中ではあらゆる数値が2進数で表される．小数点付き数値の場合は，数字の並びを2進数で表すだけでなく，小数点の場所も2進数で表す，ということでした．

<!-- $0.1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.1"> を小数点付き2進数で表すことを考えます．つまり２のべき乗の総和で表します．<!-- $0.1 = 2^{-4}+2^{-5}+2^{-8}+2^{-9}+2^{-12}+\dots$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.1%20%3D%202%5E%7B-4%7D%2B2%5E%7B-5%7D%2B2%5E%7B-8%7D%2B2%5E%7B-9%7D%2B2%5E%7B-12%7D%2B%5Cdots">なので，
`0.000110011001...(2)` です．おそらく有限桁では表せません．

<!-- $0.2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.2"> は，<!-- $0.2 = 2^{-3}+2^{-4}+2^{-7}+2^{-8}+2^{-11}+2^{-12}\dots$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.2%20%3D%202%5E%7B-3%7D%2B2%5E%7B-4%7D%2B2%5E%7B-7%7D%2B2%5E%7B-8%7D%2B2%5E%7B-11%7D%2B2%5E%7B-12%7D%5Cdots">なので，
`0.001100110011...(2)`です．こちらも有限桁では表せません．

なので，`0.1+0.2 = 0.000110011001...(2) + 0.001100110011...(2) = 0.01001100110...(2)`ですが，そもそも足される数値が表しきれてないので，答えも正しくありません．

ということで，数値を正確に表すにはどうするか？数値を分数で表せばよいのではないでしょうか．<!-- $0.1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.1"> を<!-- $\frac{1}{10}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cfrac%7B1%7D%7B10%7D">，<!-- $0.2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.2">を<!-- $\frac{1}{5}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cfrac%7B1%7D%7B5%7D">，加算の結果も<!-- $\frac{3}{10}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cfrac%7B3%7D%7B10%7D">と表すのです．正確です．

```py

>>> x = Rational(0.1)
>>> print(x)
(1, 10)
```

と`0.1`を引数で与えるとタプル`x`に分数の分子と分母（いずれも整数`int`）のタプル`(1,10)`を返す関数を考えます．

ただこれは難しい問題です．というのはすべての数が分数で表せるとは限らないからです．
例えば，円周率<!-- $\pi$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cpi">や，ネイピア数<!-- $\mathrm e$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cmathrm%20e">は分数で表せないことがわかっています．

分数で表せる数を **有理数** といい，表せない数を **無理数** といいます．しかし，今，引数の数値は数字列を実際に書いているので，<!-- $0.1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0.1">なら<!-- $\frac{1}{10}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cfrac%7B1%7D%7B10%7D">ですし，<!-- $3.14$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3.14">なら少なくとも<!-- $\frac{314}{100}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cfrac%7B314%7D%7B100%7D">だとわかっています（まだ約分できるが）．よって，

```py

>>> x = Rational(2, 10)
>>> print(x)
(1, 5)
```

などと既知の適当な分数の形を与えると，約分された分数（**既約分数**）を返す関数を考えましょう．最大公倍数を使うと以下のように分数を定義する関数を書けます．


```py
# mymodule3.py
def gcd(p,q):
    """pとqとの最大公倍数
    """
    while p % q != 0:
        old_p = p
        old_q = q
        p = old_q
        q = old_p % old_q
    
    return q

def Rational(num, den=1):
    Ngcd = gcd(num,den)
    new_num = int(num/Ngcd)
    new_den = int(den/Ngcd)

    return (new_num, new_den)
```

```py
>>> import mymodule3 as my
>>> x = 2
>>> y = 10
>>> print(my.gcd(x,y))
2
>>> x = my.Rational(1,10)
>>> print(x)
(1, 10)
```

では，このように分数で表された数値の加減乗除を考えましょう．

例えば分数クラス（例えば`class Rational()`）である`x`と`y`を使って，`x+y`の演算結果を分数クラスで答えます．また，ついでに`print`関数にかけたときに分数の形で表示できるようにしてみます．

```py
# mymodule4.py

def gcd(p,q):
    """pとqとの最大公倍数
    """
    while p % q != 0:
        old_p = p
        old_q = q
        p = old_q
        q = old_p % old_q
    
    return q

class Rational():
    def __init__(self,num,den = 1):
        Ngcd = gcd(num,den)
        self.num = int(num/Ngcd)
        self.den = int(den/Ngcd)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self,arg1):
        den = self.den * arg1.den
        num = self.num * arg1.den + arg1.num * self.den
        return Rational(num,den)

```

関数`Rational`をクラスに格上げしたので，`__init__`メソッドにクラス名を関数名とする関数を定義します．クラス内で使う関数`gcd`はクラス定義の外で，同じファイルの中に書きます．

`__str__`は文字列に変換する予約メソッドで，`print`関数や`str`関数にそのクラスの値を与えたときにどのように表示するかを決めています．



```py
>>> import mymodule4 as my
>>> x = my.Rational(1,10)
>>> print(x)
1/10
>>> y = my.Rational(2,10)
>>> print(y)
1/5
>>> print(x+y)
3/10
```

それでは，課題です．

> [課題1] 他の`-`/`*`/`/`の予約メソッド`__sub__`/`__mul__`/`__truediv__`を定義して，四則演算を完備した分数クラスのモジュールを作ってください．
> 完成したら，分数クラスを使ったコードを書いて，実行例をレポートに掲載してください．

# 親クラスの継承

クラスは，他のクラスの属性定義を引き継ぐことができます．たとえば

```py
# mymodule5.py

import mymodule4 as my
class RationalChild(my.Rational):
    pass
```

というように継承したいクラス（親クラス）を丸括弧内に入れたクラス（子クラス）を定義すると，

```py
>>> import mymodule5 as my
>>> x = my.RationalChild(4,10)
>>> print(type(x))
<class 'mymodule5.RationalChild'>
>>> print(x.num)
2
>>> print(x.den)
5
>>> print(x)
2/5
```

と親クラスの属性定義がそのまま使えます．これだけだとただのコピーですが，子クラスは拡張や属性の再定義ができます．

```py
# mymodule6.py

import mymodule4 as my

class RationalChild(my.Rational):
    def __str__(self):
        return str(self.num) + '÷' + str(self.den)

    def show(self):
        print('分子=' , self.num)
        print('分母=', self.den)

```

予約メソッド`__str__`を再定義し，新たに`show`メソッドを追加しています．

```py
>>> import mymodule6 as my
>>> x = myRationalChild(5, 10)
>>> print(x)
1÷2
>>> x.show()
分子=1
分母=2
```

では，2つ目の課題です．

# (課題) べき乗ができる分数クラスの子クラスを作ろう

> [課題2] 課題1で作成した分数クラスを継承した子クラスを作り，新たにべき乗`**`演算をできるように拡張せよ．ただし，自然数乗に限定する．また，その子クラスを用いたコードを書き，実行例をレポートに掲載せよ．

べき乗 `**`は，予約メソッド`__pow__`で定義する．

ヒント：`x`の`y`乗（ただし`y`は自然数）<!-- $x^y$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5Ey"> を返す関数`pow(x,y)`は次のようになるであろう．

```py
def pow(x,y):
    ret = 1
    while y > 0:
        ret *= x
        y -= 1
    
    return ret
```

- `ret *= x`は`ret = ret * x`，`y -= 1`は`y = y - 1`の省略した書き方です．

## （実際に計算機で用いられるべき乗関数）

上記では，<!-- $x^y$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5Ey">を「`x`を`y`回繰り返し乗算する」方法で解いています．これはべき乗の定義通りなのですが，計算機で実際に用いられる方法は，以下のような方法です．（繰り返し二乗法）

```py
def pow(x,y):
    ret = 1;
    while (y > 0):
        if y & 1:
            ret *= x  
        x *= x
        y  >>=  1  
    
    return ret
```

- `y & 1`は`y`と`1`の，ビットAND（ビット論理積）です．ビット論理積とは，演算子の左右それぞれを2進数表記したときに，同じ桁どうしでAND（論理和）を計算した結果（2進数）を10進数表記したものです．
    - つまり，`y & 1`は`y`の2進数表記の1桁目以外を`0`にしたもの（2進数）を10進数表記した数値です．
        - つまり，`y == 1`（`y`と`1`は等しいか否かをTrueかFalseで返す）と同じです．
- こういう，「`y`の2進数表記のある桁のビット値のみを残す」演算によくビット論理積が使われます．**ビットマスク**（あるビットをマスクする（隠す））といいます．
- `y >>= 1`は `y = y >> 1`の省略した書き方で，`y >> 1`は「ビット右シフト」で`y`の2進数表記を右に`1`回スライドさせたもの（2進数）を10進数表記した数値です（はみ出したビットは無くなる）．たとえば`y=7`(2進数表記`0000 0111`)に対して `y >> 2`は「`2`回右シフト」なので，`0000 0011`つまり10進数の`3`となります．

この処理でやっていることは，（カッコ内は`x=2`,`y=3`を与えたとき<!-- $2^3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=2%5E3">の具体例）

1. `ret`に`1`を代入（`ret = 1`, `x=2`，`y=3`）
2. `y > 0`？，真なら続ける （今，真なので続ける）
3. `y & 1`が真(1)ならば，`ret = ret * x`（今，`y=0011`で1桁目が`1`で真なので，`ret = 2`，`x=2`，`y=3`）
4. `x`を2乗して`x`に保存 （`ret = 2`，`x = 4`, `y = 3`）
5. 指数`y`を1回右シフトして`y`に保存 （`ret = 2`，`x=4`，`y=1`）
6. `y > 0`？，真なら続ける （今，真なので続ける）
7. `y &1` が真(1)ならば，`ret = ret * x` （今，`y=0001`で1桁目が`1`で真なので，`ret = 8`，`x=4`，`y=1`）
8. `x`を2乗して`x`に保存（`ret = 8`，`x=16`，`y=1`）
9. `y`を1回右シフトして`y`に保存（`ret = 8`，`x=16`，`y=0`）
10. `y > 0`？，真なら続ける （今，真ではないので，繰り返しを抜ける．）
11. `ret`を呼び出し元に返却 (答えは`8`)

乗算の個数は，`y=3`の場合は上記の`3`,`4`,`7`,`8`の4回です．`y=4`の場合も4回，`y=8`の場合5回です．（指数を2進数表記したときの`1`のビット数＋`1`となっている最高桁数）

もともとの「指数回乗算する」方法だと，`y=3`の場合4回，`y=4`の場合5回，`y=8`の場合9回となり，指数が大きくなるほど，上記の繰り返し二乗法との差が大きくなります．（重い）

繰り返し二乗法は，
<!-- $y = 2^{y_4} + 2^{y_3} + 2^{y_2} + 2^{y_1}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=y%20%3D%202%5E%7By_4%7D%20%2B%202%5E%7By_3%7D%20%2B%202%5E%7By_2%7D%20%2B%202%5E%7By_1%7D"> 
（ <!-- $y_n$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=y_n"> は`y`を2進数表記したときのn桁目にあたる）としたとき， 
<!-- $x^y = x^{2^{y_4}} \cdot x^{2^{y_3}} \cdot x^{2^{y_2}} \cdot x^{2^{y_1}}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5Ey%20%3D%20x%5E%7B2%5E%7By_4%7D%7D%20%5Ccdot%20x%5E%7B2%5E%7By_3%7D%7D%20%5Ccdot%20x%5E%7B2%5E%7By_2%7D%7D%20%5Ccdot%20x%5E%7B2%5E%7By_1%7D%7D"> を計算しています．
<!-- $2^{y_n}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=2%5E%7By_n%7D"> は1または2なので，<!-- $x^{y_n}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5E%7By_n%7D">は`x`または`x*x`です．よって乗算回数が 「指数を2進数表記したときの`1`のビット数＋`1`となっている最高桁数」となります．
