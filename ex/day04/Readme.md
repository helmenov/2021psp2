# day04 : 別個のコードを借用する (module)

## 関数 (function) と定数は使い回す

1年後期のプログラミング概論の定期試験をもう一度解いてみよう．ちょっと内容変えてるけど．

### 例：平方根を求める

<!-- $\sqrt{3}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Csqrt%7B3%7D">を求めてみよう．

すなわち<!-- $x^2 = 3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5E2%20%3D%203">を満たす<!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x">を求めたい．

<!-- $$
x^2 - 3 = 0 
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=x%5E2%20-%203%20%3D%200%20"></div>

<!-- $$
\leftrightarrow (x-\sqrt{3})(x+\sqrt{3}) = 0
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cleftrightarrow%20(x-%5Csqrt%7B3%7D)(x%2B%5Csqrt%7B3%7D)%20%3D%200"></div>

であるから，解は<!-- $x = \pm \sqrt{3}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%20%3D%20%5Cpm%20%5Csqrt%7B3%7D">である．このように数式を同値変形していき，最終的に <!-- $x = \bigcirc$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%20%3D%20%5Cbigcirc"> の形で求めることを **「解析的に解く」** と言う．

数式によっては，上のように同値変形していくことが困難で「解析的に解く」ことができない場合もある．その場合，すぐに試すのは次の処理であろう．

1. まず，適当な数<!-- $x_0=3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_0%3D3">を <!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x"> に入れて<!-- $x^2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5E2">を計算してみると<!-- $9$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=9">， これは左辺の<!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> よりだいぶ大きかった．
2. 先ほどの数<!-- $x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_0">より小さい数<!-- $x_1=2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_1%3D2"> （ただし<!-- $x_1 < x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_1%20%3C%20x_0">） を<!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x">に入れて再度計算してみると<!-- $4$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=4">，少し <!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> に近づいたがまだ <!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> より大きい．
3. 今度はさらにだいぶ小さい数<!-- $x_2=1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_2%3D1">（ただし<!-- $x_2 < x_1 < x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_2%20%3C%20x_1%20%3C%20x_0">）を<!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x">に入れて再度計算してみると<!-- $1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=1">， 計算結果<!-- $x^2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5E2">が<!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> より小さくなった．
4. 少し大きい数<!-- $x_3=1.8$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_3%3D1.8">（ただし<!-- $x_2 < x_3 < x_1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_2%20%3C%20x_3%20%3C%20x_1">）を入れて計算すると<!-- $3.24$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3.24">， 結果が<!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> より少し大きくなった．
5. 少し小さい数<!-- $x_4=1.7$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_4%3D1.7">（ただし<!-- $x_2 < x_4 < x_3 < x_1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_2%20%3C%20x_4%20%3C%20x_3%20%3C%20x_1">）を入れて<!-- $2.89$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=2.89">，これを <!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> と比べると小さいので，少し大きい数<!-- $x_5=1.75$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_5%3D1.75">を入れて<!-- $3.06$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3.06">，これを <!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> と比べ，
6. <!-- $\dots$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cdots"> というのを繰り返していき，
7. 最終的に <!-- $x_n=1.732$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_n%3D1.732"> を <!-- $x^2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5E2">に代入したとき <!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> に十分近くなったので，解は<!-- $x = 1.732$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%20%3D%201.732">

しかし当てずっぽうに数を試しては大変である．もっと賢い方法として**ニュートン法**というのが知られている．

先ほどの式を <!-- $f(x) = 0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)%20%3D%200">，すなわち <!-- $f(x) = x^2-3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)%20%3D%20x%5E2-3">とする．真の解が <!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x"> として，それに近い <!-- $x_0 = x + \epsilon$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_0%20%3D%20x%20%2B%20%5Cepsilon">の周りで <!-- $f(x)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)">をテイラー展開近似すると，

<!-- $$f(x) = f(x_0 - \epsilon) = f(x_0) - f^{\prime}(x_0)\epsilon + O(\epsilon)$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>

となり，<!-- $\epsilon$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cepsilon">の2 次以降<!-- $O(\epsilon)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=O(%5Cepsilon)">を無視すると， <!-- $f(x) = 0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)%20%3D%200">となる <!-- $\epsilon$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cepsilon"> は

<!-- $$\epsilon = \frac{f(x_0)}{f^{\prime}(x_0)}$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>

である．

<!-- $x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_0">から<!-- $\epsilon$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cepsilon"> だけ引けば，真の値 <!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x"> に近づくはずなので，

<!-- $$x_{n+1} = x_n - \frac{f(x_n)}{f^{\prime}(x_n)}$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>

という次の値を選んでいけば都合がよい．いま  <!-- $f(x) = x^2-3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)%20%3D%20x%5E2-3">， その導関数 <!-- $f^{\prime}(x) = 2x$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f%5E%7B%5Cprime%7D(x)%20%3D%202x">なので，

<!-- $$x_{n+1} = x_n - \frac{x_n^2-3}{2x_n}$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>

である．

具体的に <!-- $x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_0">として <!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> を代入してみよう．上の漸化式から，次に試す <!-- $x_1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_1"> は <!-- $3 - \frac{3^2-3}{2 \cdot 3} = 3 - \frac{6}{6} = 3 - 1 = 2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3%20-%20%5Cfrac%7B3%5E2-3%7D%7B2%20%5Ccdot%203%7D%20%3D%203%20-%20%5Cfrac%7B6%7D%7B6%7D%20%3D%203%20-%201%20%3D%202"> ，その次に試す <!-- $x_2$は $2-\frac{2^2-3}{2\cdot 2}= 2-\frac{1}{4} = 1.75$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_2%24%E3%81%AF%20%242-%5Cfrac%7B2%5E2-3%7D%7B2%5Ccdot%202%7D%3D%202-%5Cfrac%7B1%7D%7B4%7D%20%3D%201.75">と求まる．

<!-- $x_1$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_1">から<!-- $x_{10}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_%7B10%7D">までを逐次「`i :`<!-- $x_i$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_i"> の値」という形で表示する python プログラムコードは以下のようになる．

```py
#%% newton1.py 
x = 3
for n in range(10): 
    epsilon = (x**2-3)/(2*x)
    x = x - epsilon 
    print(n+1,':',x)
```

上記のプログラム `newton1.py` では <!-- $x_{10}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_%7B10%7D">まで求めたが，同様に `range` の引数を 50 にすれば <!-- $x_{50}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_%7B50%7D"> まで求めることができる．

しかし，おそらく数回後，ほとんど変わらない数字が表示されるであろう．つまり収束している．よって収束していると判断した段階で繰り返し処理から脱出するように書き換えよう．

以下の `newton2.py` は，1 万回繰り返し， 更新量の2乗 <!-- $(x_{n+1} - x_n)^2$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=(x_%7Bn%2B1%7D%20-%20x_n)%5E2">  が `0.001` より小さい場合には，繰り返しをその時点で脱出する．

```py
#%% newton2.py 
x = 3 
for n in range(10000): 
    epsilon = (x**2-3) / (2*x)
    x_next = x - epsilon 
    print(n+1,':',x_next)
    if (x_next - x) ** 2 < 0.001: 
         break 
    x = x_next 
```

これで良さそうなので，別の初期値 <!-- $x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_0"> からはじめてみたい．

たとえば初期値<!-- $x_0 = 3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_0%20%3D%203">では<!-- $x^2=3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5E2%3D3">の解の 1 つである「<!-- $x = \sqrt{3} = 1.732$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%20%3D%20%5Csqrt%7B3%7D%20%3D%201.732">」しか求められない．もう一つの解である <!-- $x = -1.732$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%20%3D%20-1.732">を求めるには，これらの解に近い別の初期値からはじめないといけない．
（もともと求めたいのは正の値<!-- $\sqrt{3}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Csqrt%7B3%7D">だったので，止めてもいいのだけれど）

たとえば， <!-- $-3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=-3">などから始めれば，負の解を求められそうである．

それでは，<!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=3"> と <!-- $-3$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=-3">の 2 つの初期値それぞれで解を求めてみよう．

そのためには，この 2 つの初期値をリストにして，`for` 文でリストから 1 つずつ初期値を取り出しては解を求めるというのを繰り返せばよい．

ついでに，繰り返し回数の $10000$ ，収束判定条件の $0.001$ という値は，違う値で試したいので，変数とするほうがよい．

プログラムソースコードは以下の `newton3.py` である．

```py
#%% newton3.py 
 
x_list = [3, -3]
n_loop = 10000 
error_limit = 0.001 

for x in x_list: 
    for n in range(n_loop): 
        epsilon = (x**2-3)/(2*x)
        x_next = x - epsilon 
        if (x_next - x)**2 < error_limit: 
              break 
        x = x_next
    print(x) 
```

ニュートン法の処理の漸化式を見ると許されない計算があることに気づく．

<!-- $$x = x_0 - \frac{f(x_0)}{f^{\prime}(x_0)}$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>

ここで， <!-- $f^{\prime}(x_0) = 0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f%5E%7B%5Cprime%7D(x_0)%20%3D%200">のとき，<!-- $0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=0"> で割る演算であるから許されない． 今回の場合，<!-- $x_0=0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_0%3D0">のとき<!-- $f^{\prime}(x_0)=0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f%5E%7B%5Cprime%7D(x_0)%3D0">なので，そんな初期値を使う人はいないと思うが，
仮に<!-- $f^{\prime}(x_0) = 0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f%5E%7B%5Cprime%7D(x_0)%20%3D%200">となると，プログラム自体がエラーで止まってしまい，別の計算が行われなくなる．
したがって，エラーでプログラム停止させるのではなく，現在の初期値から解を求めるのだけ諦め，別の初期値によって解を求めるように直前の`for`を抜けるようにしよう．
「`try`-`except`」で例外処理を加えよう．

```py
#%% newton4.py 

x_list = [3,-3]
n_loop = 10000 
error_limit = 0.001
 
for x in x_list: 
     for n in range(n_loop): 
         try: 
            epsilon = (x**2-3)/(2*x) 
         except ZeroDivisionError: 
            x = 'stopped' 
             break 
         else: 
            x_next = x - epsilon 
             if (x_next - x)**2 < error_limit: 
                 break 
            x = x_next 
         finally: 
             pass 
    print(x) 
```

これで完成．

## 5の平方根を求めよ（課題1）

完成した．今度は，<!-- $\sqrt{3}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Csqrt%7B3%7D">ではなく，<!-- $\sqrt{5}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Csqrt%7B5%7D">の実数値を求めるコード`solve_sqrt5.py`を書いてみよう．

たいていの場合，上記のソースコードをコピペして`solve_sqrt5.py`の骨組みを作り，問題が変わった部分について若干の変更というか数字の書き換えをするだけではないだろうか？

このような「コピペ＆数字の書き換え」はやめよう！その代わりに，

1. コピペして作った新しいソースコードをモジュール`myfunc.py`にする．書き換える部分を引数変数にして関数`solve_sqrt()`に仕立てる．
2. `solve_sqrt5.py`の冒頭で `import myfunc`と書いて，`myfunc.solve_sqrt(5)`により<!-- $\sqrt{5}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Csqrt%7B5%7D">を求める．

## 恒等式をも引数にして，適当な恒等式の解を求めよ（課題2）

これまで，平方根を求めるべく例えば<!-- $x^2-3=0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%5E2-3%3D0">という恒等式を解いていたが，一般的な恒等式<!-- $f(x)=0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)%3D0"> を解けるようにしてみよう． ソースコードを見てみると，

```py
epsilon = (x**2-3) / (2*x)
```

のところだけが，今回の<!-- $f(x) = x^2 -3 = 0$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)%20%3D%20x%5E2%20-3%20%3D%200">に特有な部分である．分子は<!-- $f(x)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)">そのものであるから， たとえば `TargetFunc(x)`という関数を定義して，上の分子の部分にあてはめればよい．
分母は導関数 <!-- $f^{\prime}(x)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f%5E%7B%5Cprime%7D(x)">であり， 導関数の数学的な定義にしたがって，`Differential(TargetFunc, x)` という関数を作る．

```py
def Differential(TargetFunc, x): 
    h = 1e-4 
     return (TargetFunc(x+h) - TargetFunc(x))/h 

def NewtonSolver(TargetFunc, x, n_loop = 10000, error_limit = 0.001): 
     for n in range(n_loop): 
         try: 
            epsilon = TargetFunc(x)/Differential(TargetFunc, x) 
         except ZeroDivisionError: 
            x = 'stopped' 
             break 
         else: 
            x_next = x - epsilon 
             if (x_next - x)**2 < error_limit: 
                 break 
            x = x_next 
         finally: 
             pass 
     return x
```

呼び出し側は，解きたい式を関数定義して，呼び出せばよい．

```py
#%% 
import myfunc

def FuncOne(x): 
     return x ** 2 - 3 

def FuncTwo(x): 
     return x**2- 10 

xList = # 初期値のリスト
nLoop = # 繰り返し回数
errorLimit = #　解の収束判定条件

for x_0 in xList: 
    x = NewtonSolver(TargetFunc=FuncOne, x=x_0, n_loop=nLoop, error_limit=errorLimit)
    print(x) 
```

この要領で，適当な恒等式を自分で定義し，それを解くコードを作成，実行せよ．

※上記のソースコードのままでは動作しない．自分で直して完成させよ．

## module

モジュール(module)とは，上記のように，単体のソースコードを複数に分けたときの，メイン以外の雑多な部品(関数や定数)が書かれているpythonソースコードのことである．

モジュールを使うときは，`import モジュールファイル名`をその部品を置くべき場所に置き，`モジュールファイル名.（ドット）関数`や，`モジュールファイル名.（ドット）定数`などとして使う．

基本的には，呼び出されるモジュールは，呼び出し元のコードと同じ階層，もしくは下位のディレクトリに置き，`import モジュール`（同じ階層）や`from mypack import モジュール`（下位の階層）のように書いて使う．
モジュール内で定義されている変数や関数を使うときは，`モジュール名.foo`であり，ディレクトリ名である`mypack`などはつけなくてよい．

## コーディングTips

可読性を意識しましょう．可読性とは，プログラムを書いたことのない他人がどれくらい読めるか？という指標です．

1. 短く簡潔に

    しばしば，「1万行以上のプログラムを書ける」などと，ソースコードの長さが習熟度の目安にされる場面を見ますが，1万行でも100万行でも書くだけならダラダラと無駄な退屈な作業をするだけです．でも，そういうダラダラと書かれたコードほど読む気が失せます．

    同じ内容ならば，可能な限り短く簡潔に書きましょう．そのほうが可読性が高いです．

2. 処理ごとに名前をつける．

    ソースコードは，当然プログラミング言語の文法に沿って書くのですが，それが可読性を下げます（書いたことない他人は文法知らないのだから読めない）．

    矛盾するようですが，プログラミング言語の言葉を使わずに，文章のようにソースコードを書くのが可読性を上げます．

    つまり，演算や論理構造，比較やループ，基本関数などからなる「ある目的を行う一連の処理」を「関数」にします．

    「関数にする」ということは「関数名」を名付けることになります．たいてい関数名は「動詞」です．例えば，CalcAverageとか，IsPositiveとか．
    
    結果，その「一連の処理」（読めない他人はその一行一行が何を目的としているのかわからない）が「関数名」に置き換わり，ソースコードが文章化されます．

3. 変数名も意味のある名前に

    意味のない名前はつけないように．例えば 1文字だけの名前は避けるべきです．その変数が何なのかの言葉を名前にしましょう．

4. 数値にも意味のある名前を

    例えば10人の平均値を10科目の科目ごとに求めるなんてプログラムを作るとき，10という数値がfor文の繰り返し回数だとか，配列の個数だとか，いろいろなところに出現します．その10は，場所によって「人数」であったり「科目数」であったりします．「10」という数値だけだとそのどちらの意味なのかわかりません．
    
    よって，ソースコードには生の数値を書かないほうが可読性が高いです．

    数値は早めに適切な名前をつけた変数に入れてしまって，その後はその変数を使って処理をしましょう．

## パッケージモジュール

モジュール（部品として有用なソースコード）が複数入っているディレクトリを**パッケージ**（他の言語だと**ライブラリ**）と言っています．

python言語は，この「パッケージ」が豊富であることが大きな大きな特徴であり，豊富であるから，とても有用なパッケージが淘汰されていってます．豊富である理由は，以下の2つが挙げられます．他のプログラミング言語ではなかなか実現されていません．

1. Pythonが公式に公開場所を定めている
2. pythonコマンドの一つとしてパッケージ管理コマンドを含んでいる

Python公式の公開場所は，[PyPI](https://pypi.org/) というWebサイトです．誰でも**きみでも**パッケージを登録できます．

Python公式が用意しているパッケージ管理コマンドは，`pip`です．パッケージを指定の場所にインストールしたり，アンインストールしたり，バージョンアップしたりすることができます．

`pip show -f パッケージ名`でそのパッケージのインストール先がわかります．
あるパッケージをインストールするとき，そのパッケージで使っている別のパッケージもインストールされます．

## Anaconda

pythonでパッケージをインストールしようとするとき，「Anaconda」というものを聞く機会があるかもしれません．

Anacondaとは，Anacondaという会社がPython公式の不備を補完しようとして作った「Python環境」です．Python公式と同じpythonコンパイラがAnacondaの中に含まれています．現時点では無料ですが，将来的には有料となる可能性を秘めています．

「Python公式の不備を補完しようとして」というのは，pythonの`pip`が「目的のパッケージをインストールするときに，必要なパッケージをインストールする」のですが，あまりに自由な管理のために，あるパッケージを入れると，別のあるパッケージが使えなくなる，とかいう不具合が多々多々起きるという問題を解決しようとしているという意味です．

Anacondaは，パッケージとパッケージとの依存関係を解決する内部処理を持つパッケージ管理をしており，PyPIとは別のパッケージ公開場所を使います．  [Anaconda Clowd](https://anaconda.org/)

パッケージ管理ソフトも，`pip`ではなく`conda`を使います．すなわち，Python公式の`python`と`pip`とは全く別の`python`と`conda`を使うので，共存がご法度！（でした．現在はいちおう共存可能です．）

