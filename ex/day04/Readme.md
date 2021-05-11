# day04 : 別個のコードを借用する (module)

## 関数 (function) と定数は使い回す

1年後期のプログラミング概論の定期試験をもう一度解いてみよう．ちょっと内容変えてるけど．

### 例：平方根を求める

<!-- $\sqrt{3}$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/6BF6Fif0ho.svg">を求めてみよう．

すなわち<!-- $x^2 = 3$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/vA9qf5uwFa.svg">を満たす$x$を求めたい．

<!-- $$
\begin{align}
x^2 - 3 &= 0 \\
\leftrightarrow (x-\sqrt{3})(x+\sqrt{3}) &= 0
\end{align}
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/flg5Kp6U7D.svg"></div>

であるから，解は<!-- $x = \pm \sqrt{3}$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/XJTqDqoNn8.svg">である．このように数式を同値変形していき，最終的に <!-- $x = \bigcirc$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/3qsSUFkQPc.svg"> の形で求めることを **「解析的に解く」** と言う．

数式によっては，上のように同値変形していくことが困難で「解析的に解く」ことができない場合もある．その場合，すぐに試すのは次の処理であろう．

1. まず，適当な数<!-- $x_0=3$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/hdUQqFhWHG.svg">を <!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/hCh23aRfIG.svg"> に入れて<!-- $x^2$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/iejb18xT8s.svg">を計算してみると<!-- $9$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/mhyZFF0UxH.svg">， これは左辺の<!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/bpM1yDqkVN.svg"> よりだいぶ大きかった．
2. 先ほどの数<!-- $x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/atMoEHufUc.svg">より小さい数<!-- $x_1=2$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/k74Z6bJ6Qd.svg"> （ただし<!-- $x_1 < x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/pRcThNd51G.svg">） を<!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/hZmMbWXfTy.svg">に入れて再度計算してみると<!-- $4$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/d7pbxDpQ9t.svg">，少し <!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/5jAeN2XZr8.svg"> に近づいたがまだ <!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/4fDRxYCDkJ.svg"> より大きい．
3. 今度はさらにだいぶ小さい数<!-- $x_2=1$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/8rszmH3lct.svg">（ただし<!-- $x_2 < x_1 < x_0$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/ef0M4O62Q2.svg">）を<!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/hQqbOfCLv9.svg">に入れて再度計算してみると<!-- $1$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/opGBWZ1kKW.svg">， 計算結果<!-- $x^2$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/JyAoJlUAct.svg">が<!-- $3$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/iL6pJIou4g.svg"> より小さくなった．
4. 少し大きい数<!-- $x_3=1.8$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/itwQSP0XUd.svg">（ただし<!-- $x_2 < x_3 < x_1$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/pluTWjrEUt.svg">）を入れて計算すると$3.24$， 結果が$3$ より少し大きくなった．
5. 少し小さい数$x_4=1.7$（ただし$x_2 < x_4 < x_3 < x_1$）を入れて$2.89$，これを $3$ と比べると小さいので，少し大きい数$x_5=1.75$を入れて$3.06$，これを $3$ と比べ，
6. $\dots$ というのを繰り返していき，
7. 最終的に $x_n=1.732$ を $x^2$に代入したとき $3$ に十分近くなったので，解は$x = 1.732$

しかし当てずっぽうに数を試しては大変である．もっと賢い方法として**ニュートン法**というのが知られている．

先ほどの式を $f(x) = 0$，すなわち $f(x) = x^2-3$とする．真の解が $x$ として，それに近い $x_0 = x + \epsilon$の周りで $f(x)$をテイラー展開近似すると，

$$f(x) = f(x_0 - \epsilon) = f(x_0) - f^{\prime}(x_0)\epsilon + O(\epsilon)$$

となり，$\epsilon$の2 次以降$O(\epsilon)$を無視すると， $f(x) = 0$となる $\epsilon$ は

$$\epsilon = \frac{f(x_0)}{f^{\prime}(x_0)}$$

である．

$x_0$から$\epsilon$ だけ引けば，真の値 $x$ に近づくはずなので，

$$x_{n+1} = x_n - \frac{f(x_n)}{f^{\prime}(x_n)}$$

という次の値を選んでいけば都合がよい．いま  $f(x) = x^2-3$， その導関数 $f^{\prime}(x) = 2x$なので，

$$x_{n+1} = x_n - \frac{x_n^2-3}{2x_n}$$

である．

具体的に $x_0$として $3$ を代入してみよう．上の漸化式から，次に試す $x_1$ は $3 - \frac{3^2-3}{2*3} = 3 - \frac{6}{6} = 3 - 1 = 2$ ，その次に試す $x_2$は $2-\frac{2^2-3}{2*2}= 2-\frac{1}{4} = 1.75$と求まる．

$x_1$から$x_{10}$までを逐次「`i :`$x_i$ の値」という形で表示する python プログラムコードは以下のようになる．

```py
#%% newton1.py 
x = 3
for n in range(10): 
    epsilon = (x**2-3)/(2*x)
    x = x - epsilon 
    print(n+1,':',x)
```

上記のプログラム `newton1.py` では $x_{10}$まで求めたが，同様に range の引数を 50 にすれば 正解 $x_{50}$ まで求めることができる．

しかし，おそらく数回後，ほとんど変わらない数字が表示されるであろう．つまり収束している．よって収束していると判断した段階で繰り返し処理から脱出するように書き換えよう．

以下の `newton2.py` は，1 万回繰り返し， 更新量の2乗 $(x_{n+1} - x_n)^2$  が `0.001` より小さい場合には，繰り返しをその時点で脱出する．

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

これで良さそうなので，別の初期値 $x_0$ からはじめてみたい．

たとえば初期値$x_0 = 3$では$x^2=3$の解の 1 つである「$x = \sqrt{3} = 1.732$」しか求められない．もう一つの解である $x = -1.732$を求めるには，これらの解に近い別の初期値からはじめないといけない．
（もともと求めたいのは正の値$\sqrt{3}$だったので，止めてもいいのだけれど）

たとえば， $-3$などから始めれば，負の解を求められそうである．

それでは，$3$ と $-3$の 2 つの初期値それぞれで解を求めてみよう．

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

$$x = x_0 - \frac{f(x_0)}{f^{\prime}(x_0)}$$

ここで， $f^{\prime}(x_0) = 0$のとき，$0$ で割る演算であるから許されない． 今回の場合，$x_0=0$のとき$f^{\prime}(x_0)=0$なので，そんな初期値を使う人はいないと思うが，
仮に$f^{\prime}(x_0) = 0$となると，プログラム自体がエラーで止まってしまい，別の計算が行われなくなる．
したがって，エラーでプログラム停止させるのではなく，現在の初期値から解を求めるのだけ諦め，別の初期値によって解を求めるように直前の`for`を抜けるようにしよう．
「try-except」で例外処理を加えよう．

```py
#%% newton4.py 
import numpy as np 

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

これで完成だが，ニュートン法のところは，関数にして呼び出すことにしよう．

関数名は `Newton` ，引数は次の３つ，

- 初期値 `x` 
- 繰り返し回数 `n_loop` （指定が無ければ `10000`）
- 収束判定値 `error_limit`（指定が無ければ `0.001`）

とし，その初期値から最終的に求められた解を返すものとする．

```py
def Newton(x, n_loop=10000, error_limit=0.001): 
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
     return x 

xList = [3, -3]
nLoop = 100 
errorLimit = 1e-100
 
for x_0 in xList: 
    x = Newton(x=x_0, n_loop=nLoop, error_limit=errorLimit) 
    print(x) 
```

`1e-100`という表記は，$1\times 10^{-100}$という意味である．


myfunc モジュールは，newton5.py と同じディレクトリに置かれているものとする．

==================== 
#%% newton5.py 
[IMPORT_MODULE] as my 

====================


これまで，$f(x) = x^2 -3 = 0$を解いていたが，一般的な問題 を解けるようにしてみよう． ソースコードを見てみると，

```py
epsilon = (x**2-3) / (2*x)
```

のところだけが，今回の$f(x) = x^2 -3 = 0$に特有な部分である．分子は$f(x)$そのものであるから， たとえば `TargetFunc(x)`という関数を定義して，上の分子の部分にあてはめればよい．
分母は導関数 $f^{\prime}(x)$であり， 導関数の数学的な定義にしたがって，`Differential(TargetFunc, x)` という関数を作る．

```py
def Differential(TargetFunc, x): 
    h = 1e-4 
     return (TargetFunc(x+h) - TargetFunc(x))/h 

def Newton(TargetFunc, x, n_loop = 10000, error_limit = 0.001): 
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

呼び出し側は，newton6.pyとして，解きたい式を関数定義して，呼び出せばよい．

```py
#%% newton6.py 
import myfunc as my

def FuncOne(x): 
     return x ** 2 - 3 

def FuncTwo(x): 
     return x**2- 10 

xList = # 初期値のリスト
nLoop = # 繰り返し回数
errorLimit = #　解の収束判定条件

for x_0 in xList: 
    x = Newton(TargetFunc=FuncOne, x=x_0, n_loop=nLoop, error_limit=errorLimit)
    print(x) 
```





## module

## 


