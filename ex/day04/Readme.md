# day04 : 別個のコードを借用する (module)

## 関数 (function) と定数は使い回す

1年後期のプログラミング概論の定期試験をもう一度解いてみよう．ちょっと内容変えてるけど．

### 例：平方根を求める

<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/eab32316a89e67b119a6611bc1b3bd21.svg?invert_in_darkmode" align=middle width=21.91788224999999pt height=28.511366399999982pt/>を求めてみよう．

すなわち<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/ff7e931f931c43282efa74bfec1663e6.svg?invert_in_darkmode" align=middle width=46.90628744999999pt height=26.76175259999998pt/>を満たす<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.39498779999999pt height=14.15524440000002pt/>を求めたい．

<p align="center"><img src="https://rawgit.com/helmenov/2021psp2/main/svgs/bcc4fb516be26332d97ce19b1ffeafed.svg?invert_in_darkmode" align=middle width=179.52022605pt height=46.52125995pt/></p>

であるから，解は<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/ff84bd7990afa39b72483bdfe3187d61.svg?invert_in_darkmode" align=middle width=66.01593405pt height=28.511366399999982pt/>である．このように数式を同値変形していき，最終的に <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5d1a6579f55867bcd6de574a3b5af5f2.svg?invert_in_darkmode" align=middle width=47.75102144999999pt height=22.831056599999986pt/> の形で求めることを **「解析的に解く」** と言う．

数式によっては，上のように同値変形していくことが困難で「解析的に解く」ことができない場合もある．その場合，すぐに試すのは次の処理であろう．

1. まず，適当な数<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/07f3df8b123a321d227b66c1b0930f25.svg?invert_in_darkmode" align=middle width=46.90628744999999pt height=21.18721440000001pt/>を <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.39498779999999pt height=14.15524440000002pt/> に入れて<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/6177db6fc70d94fdb9dbe1907695fce6.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=26.76175259999998pt/>を計算してみると<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/4383b081cba8f285e7854426f9ea1e6d.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/>， これは左辺の<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> よりだいぶ大きかった．
2. 先ほどの数<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/e714a3139958da04b41e3e607a544455.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/>より小さい数<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/bda947926e3a56a7e1f79bf2d7d9c985.svg?invert_in_darkmode" align=middle width=46.90628744999999pt height=21.18721440000001pt/> （ただし<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/3d22d0cd9add0728da5226f7e6333b9f.svg?invert_in_darkmode" align=middle width=54.63461354999999pt height=17.723762100000005pt/>） を<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.39498779999999pt height=14.15524440000002pt/>に入れて再度計算してみると<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/ecf4fe2774fd9244b4fd56f7e76dc882.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/>，少し <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> に近づいたがまだ <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> より大きい．
3. 今度はさらにだいぶ小さい数<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/4b21b432d676862d1eb707965d12e987.svg?invert_in_darkmode" align=middle width=46.90628744999999pt height=21.18721440000001pt/>（ただし<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/8b10f4fbc0f9430c747926d487f3d893.svg?invert_in_darkmode" align=middle width=93.32169164999999pt height=17.723762100000005pt/>）を<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.39498779999999pt height=14.15524440000002pt/>に入れて再度計算してみると<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/>， 計算結果<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/6177db6fc70d94fdb9dbe1907695fce6.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=26.76175259999998pt/>が<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> より小さくなった．
4. 少し大きい数<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/4c4a0eedcb60f1e7034677ab9341cc57.svg?invert_in_darkmode" align=middle width=59.69172164999999pt height=21.18721440000001pt/>（ただし<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/d080404542c9f282857168b78a1f93eb.svg?invert_in_darkmode" align=middle width=93.32169164999999pt height=17.723762100000005pt/>）を入れて計算すると<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/69e5609f56509b3b566b683cafebcc81.svg?invert_in_darkmode" align=middle width=29.22385289999999pt height=21.18721440000001pt/>， 結果が<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> より少し大きくなった．
5. 少し小さい数<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/6150d51e57a24fe36690c025bccbff0e.svg?invert_in_darkmode" align=middle width=59.69172164999999pt height=21.18721440000001pt/>（ただし<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/d3ca6d8d2e77af9867fa43db25521c7c.svg?invert_in_darkmode" align=middle width=132.00876975pt height=17.723762100000005pt/>）を入れて<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/2ebf487f02fb4823009bee0fdea0179a.svg?invert_in_darkmode" align=middle width=29.22385289999999pt height=21.18721440000001pt/>，これを <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> と比べると小さいので，少し大きい数<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/2595a23515116a2950536435fbb05f15.svg?invert_in_darkmode" align=middle width=67.91093099999999pt height=21.18721440000001pt/>を入れて<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/c21b86ac4fb278df11763325c3ee76b1.svg?invert_in_darkmode" align=middle width=29.22385289999999pt height=21.18721440000001pt/>，これを <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> と比べ，
6. <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/76aacde399706233c450f7a48e28adb4.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> というのを繰り返していき，
7. 最終的に <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/7d38f50e604c4f05e169fc9b497b0dae.svg?invert_in_darkmode" align=middle width=77.70361829999999pt height=21.18721440000001pt/> を <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/6177db6fc70d94fdb9dbe1907695fce6.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=26.76175259999998pt/>に代入したとき <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> に十分近くなったので，解は<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/e3e1ee2ca951333c9cece015cd828095.svg?invert_in_darkmode" align=middle width=68.75567984999999pt height=21.18721440000001pt/>

しかし当てずっぽうに数を試しては大変である．もっと賢い方法として**ニュートン法**というのが知られている．

先ほどの式を <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/a3936e3017c9b788004df0b3d8fb4e43.svg?invert_in_darkmode" align=middle width=62.134673699999986pt height=24.65753399999998pt/>，すなわち <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/e8293dfb0d0894bb430c86a9a186ac6b.svg?invert_in_darkmode" align=middle width=98.99531399999998pt height=26.76175259999998pt/>とする．真の解が <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.39498779999999pt height=14.15524440000002pt/> として，それに近い <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/406fa57ca80ea713679907cd661c4679.svg?invert_in_darkmode" align=middle width=74.84564834999999pt height=19.1781018pt/>の周りで <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/7997339883ac20f551e7f35efff0a2b9.svg?invert_in_darkmode" align=middle width=31.99783454999999pt height=24.65753399999998pt/>をテイラー展開近似すると，

<p align="center"><img src="https://rawgit.com/helmenov/2021psp2/main/svgs/0e27269994641a29b9c03fcef85d68e7.svg?invert_in_darkmode" align=middle width=304.63345935pt height=17.2895712pt/></p>

となり，<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode" align=middle width=6.672392099999992pt height=14.15524440000002pt/>の2 次以降<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/06a84e51f106d061d63ab8e69d4166d2.svg?invert_in_darkmode" align=middle width=32.45324939999999pt height=24.65753399999998pt/>を無視すると， <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/a3936e3017c9b788004df0b3d8fb4e43.svg?invert_in_darkmode" align=middle width=62.134673699999986pt height=24.65753399999998pt/>となる <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode" align=middle width=6.672392099999992pt height=14.15524440000002pt/> は

<p align="center"><img src="https://rawgit.com/helmenov/2021psp2/main/svgs/b4e33619ebe21f152e950910c29b3c3c.svg?invert_in_darkmode" align=middle width=74.5467888pt height=38.83491479999999pt/></p>

である．

<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/e714a3139958da04b41e3e607a544455.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/>から<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode" align=middle width=6.672392099999992pt height=14.15524440000002pt/> だけ引けば，真の値 <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.39498779999999pt height=14.15524440000002pt/> に近づくはずなので，

<p align="center"><img src="https://rawgit.com/helmenov/2021psp2/main/svgs/847293d60e366e47f8e9f000f7ee5b20.svg?invert_in_darkmode" align=middle width=142.86882885pt height=38.83491479999999pt/></p>

という次の値を選んでいけば都合がよい．いま  <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/e8293dfb0d0894bb430c86a9a186ac6b.svg?invert_in_darkmode" align=middle width=98.99531399999998pt height=26.76175259999998pt/>， その導関数 <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/285e604d905087818a6f8832d6487bfd.svg?invert_in_darkmode" align=middle width=76.14153689999998pt height=24.7161288pt/>なので，

<p align="center"><img src="https://rawgit.com/helmenov/2021psp2/main/svgs/d253569e8e0f4e96d01a15136be06329.svg?invert_in_darkmode" align=middle width=143.96450804999998pt height=38.2431621pt/></p>

である．

具体的に <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/e714a3139958da04b41e3e607a544455.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/>として <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> を代入してみよう．上の漸化式から，次に試す <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/277fbbae7d4bc65b6aa601ea481bebcc.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/> は <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/c61ffd8f5771ff12e1cb016fef6b77f9.svg?invert_in_darkmode" align=middle width=211.36014075pt height=33.45973289999998pt/> ，その次に試す <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/95d239357c7dfa2e8d1fd21ff6ed5c7b.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/>は <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/c7cc8ac109dbe826e911f001f8da707a.svg?invert_in_darkmode" align=middle width=173.91754379999998pt height=33.45973289999998pt/>と求まる．

<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/277fbbae7d4bc65b6aa601ea481bebcc.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/>から<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/226f251f439a17daa440b9698a8c07d7.svg?invert_in_darkmode" align=middle width=22.50008144999999pt height=14.15524440000002pt/>までを逐次「`i :`<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/> の値」という形で表示する python プログラムコードは以下のようになる．

```py
#%% newton1.py 
x = 3
for n in range(10): 
    epsilon = (x**2-3)/(2*x)
    x = x - epsilon 
    print(n+1,':',x)
```

上記のプログラム `newton1.py` では <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/226f251f439a17daa440b9698a8c07d7.svg?invert_in_darkmode" align=middle width=22.50008144999999pt height=14.15524440000002pt/>まで求めたが，同様に `range` の引数を <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/c2c335262ba713d0601ec6d6d01cc102.svg?invert_in_darkmode" align=middle width=16.438418699999993pt height=21.18721440000001pt/> にすれば 正解 <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/935e2b30bdc9c821009e37a30c281ca9.svg?invert_in_darkmode" align=middle width=22.50008144999999pt height=14.15524440000002pt/> まで求めることができる．

しかし，おそらく数回後，ほとんど変わらない数字が表示されるであろう．つまり収束している．よって収束していると判断した段階で繰り返し処理から脱出するように書き換えよう．

以下の `newton2.py` は，1 万回繰り返し， 更新量の2乗 <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/1f22916bf5405c79553e394b81b7952c.svg?invert_in_darkmode" align=middle width=92.75893439999999pt height=26.76175259999998pt/>  が `0.001` より小さい場合には，繰り返しをその時点で脱出する．

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

これで良さそうなので，別の初期値 <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/e714a3139958da04b41e3e607a544455.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/> からはじめてみたい．

たとえば初期値<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/6fa98c84aac2590271cd9f421329d2a7.svg?invert_in_darkmode" align=middle width=46.90628744999999pt height=21.18721440000001pt/>では<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/8a8c2b6c1161b83ca47af1481ba55af3.svg?invert_in_darkmode" align=middle width=46.90628744999999pt height=26.76175259999998pt/>の解の 1 つである「<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/ceda9b395d5704ab25b1ec7b7ff5b990.svg?invert_in_darkmode" align=middle width=112.59118529999999pt height=28.511366399999982pt/>」しか求められない．もう一つの解である <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/b1d8d84082a9b8faa19c7240900b8ab8.svg?invert_in_darkmode" align=middle width=81.54111404999999pt height=21.18721440000001pt/>を求めるには，これらの解に近い別の初期値からはじめないといけない．
（もともと求めたいのは正の値<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/eab32316a89e67b119a6611bc1b3bd21.svg?invert_in_darkmode" align=middle width=21.91788224999999pt height=28.511366399999982pt/>だったので，止めてもいいのだけれど）

たとえば， <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/175ccc5874192ac2826db5f07bc0afba.svg?invert_in_darkmode" align=middle width=21.00464354999999pt height=21.18721440000001pt/>などから始めれば，負の解を求められそうである．

それでは，<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/5dc642f297e291cfdde8982599601d7e.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> と <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/175ccc5874192ac2826db5f07bc0afba.svg?invert_in_darkmode" align=middle width=21.00464354999999pt height=21.18721440000001pt/>の 2 つの初期値それぞれで解を求めてみよう．

そのためには，この 2 つの初期値をリストにして，`for` 文でリストから 1 つずつ初期値を取り出しては解を求めるというのを繰り返せばよい．

ついでに，繰り返し回数の <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/fa35043f335bc43f27e21bc02c268be9.svg?invert_in_darkmode" align=middle width=41.09604674999999pt height=21.18721440000001pt/> ，収束判定条件の <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/242af53be4184a6239b4e559e992fd45.svg?invert_in_darkmode" align=middle width=37.44306224999999pt height=21.18721440000001pt/> という値は，違う値で試したいので，変数とするほうがよい．

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

<p align="center"><img src="https://rawgit.com/helmenov/2021psp2/main/svgs/057fb5fbe91d44479194ac31b1afffa2.svg?invert_in_darkmode" align=middle width=114.1300248pt height=38.83491479999999pt/></p>

ここで， <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/cffbb079ccf11d6fcb6961e4fcd0043c.svg?invert_in_darkmode" align=middle width=74.12100959999998pt height=24.7161288pt/>のとき，<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/29632a9bf827ce0200454dd32fc3be82.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/> で割る演算であるから許されない． 今回の場合，<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/c1d6a084ad467fa6c16907026aa050bd.svg?invert_in_darkmode" align=middle width=46.90628744999999pt height=21.18721440000001pt/>のとき<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/c6f99e4c80203ec58384bdf174b9986e.svg?invert_in_darkmode" align=middle width=74.12100959999998pt height=24.7161288pt/>なので，そんな初期値を使う人はいないと思うが，
仮に<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/cffbb079ccf11d6fcb6961e4fcd0043c.svg?invert_in_darkmode" align=middle width=74.12100959999998pt height=24.7161288pt/>となると，プログラム自体がエラーで止まってしまい，別の計算が行われなくなる．
したがって，エラーでプログラム停止させるのではなく，現在の初期値から解を求めるのだけ諦め，別の初期値によって解を求めるように直前の`for`を抜けるようにしよう．
「try-except」で例外処理を加えよう．

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

完成した．今度は，<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/eab32316a89e67b119a6611bc1b3bd21.svg?invert_in_darkmode" align=middle width=21.91788224999999pt height=28.511366399999982pt/>ではなく，<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/7d920fc85b5fb6d78be5f8f8a19a9d5f.svg?invert_in_darkmode" align=middle width=21.91788224999999pt height=28.511366399999982pt/>を解くコード`solve_sqrt5.py`を書いてみよう．

たいていの場合，上記のソースコードをコピペして`solve_sqrt5.py`の骨組みを作り，問題が変わった部分について若干の変更というか数字の書き換えをするだけではないだろうか？

このような「コピペ＆数字の書き換え」はやめよう！その代わりに，

1. コピペして作った新しいソースコードをモジュール`myfunc.py`にする．書き換える部分を引数変数にして関数`solve_sqrt()`に仕立てる．
2. `solve_sqrt5.py`の冒頭で `import myfunc`と書いて，`myfunc.solve_sqrt(5)`により<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/7d920fc85b5fb6d78be5f8f8a19a9d5f.svg?invert_in_darkmode" align=middle width=21.91788224999999pt height=28.511366399999982pt/>を解く．

## 恒等式をも引数にして，適当な恒等式の解を求めよ（課題2）

これまで，平方根を求めるべく例えば<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/895b95c3b4fab744b2579403c8ed1e1a.svg?invert_in_darkmode" align=middle width=75.21668879999999pt height=26.76175259999998pt/>という恒等式を解いていたが，一般的な恒等式<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/a6fc63aa1efb41cce557cf8cb517441f.svg?invert_in_darkmode" align=middle width=62.134673699999986pt height=24.65753399999998pt/> を解けるようにしてみよう． ソースコードを見てみると，

```py
epsilon = (x**2-3) / (2*x)
```

のところだけが，今回の<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/cc375d3afd4e04698a5aa4f58de59382.svg?invert_in_darkmode" align=middle width=129.13215315pt height=26.76175259999998pt/>に特有な部分である．分子は<img src="https://rawgit.com/helmenov/2021psp2/main/svgs/7997339883ac20f551e7f35efff0a2b9.svg?invert_in_darkmode" align=middle width=31.99783454999999pt height=24.65753399999998pt/>そのものであるから， たとえば `TargetFunc(x)`という関数を定義して，上の分子の部分にあてはめればよい．
分母は導関数 <img src="https://rawgit.com/helmenov/2021psp2/main/svgs/85aff5dbebc179ce2ea006d60c2b1f87.svg?invert_in_darkmode" align=middle width=36.60970994999999pt height=24.7161288pt/>であり， 導関数の数学的な定義にしたがって，`Differential(TargetFunc, x)` という関数を作る．

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

もし，メインコードと部品（モジュール）コードが別のディレクトリにある場合は，メインコードに対するモジュールコードのディレクトリ位置（相対パス）を`from 相対位置 import モジュール`のように書いて使う．

例えば，以下のようなディレクトリ構造になっていたとする．

```
2021psp2 ┬  day01
                     │
                     ├ day04 ┬ solver.py （メインコード）
                     │               └  Readme.md 
                     │
                     └ func ┬ mymodule04.py （solver.pyから呼び出したいモジュール）
                                     └ mymodule05.py
```

このとき，solver.pyでは，

```py
from ../func import mymodule04
```

などとすればインポートできる．使うときは，`mymodule04.foo()`であり，相対パスは不要．

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

