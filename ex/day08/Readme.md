# Matplotlib

Matplotlibは，入力した系列に対応してグラフを描くライブラリです．

下のようなグラフを描きます．このグラフに書いてある用語（英単語）をそのまま覚えてください．
![「図」の解剖](https://matplotlib.org/stable/_images/anatomy.png)

- Figure：フィギュア：所謂，キャンバスのことです．Figureに描かれるのは，
    - 複数のグラフ(Axes)
    - キャンバスのタイトル，凡例





- Axes：アクセス：所謂，グラフのことです．Axesに描かれるのは，
    - 軸線(Axis)
    - 軸ラベル(xlabel, ylabel)
    - プロット（Plot, データを使って書かれた線や点）

- Axis：アクシス：所謂，軸線のことです．Axis上に描かれるのは，
    - 目盛印(Tick，ティック)：目盛として軸に刻みで描かれる細い線
    - 目盛文字列(Tick Label)：目盛の刻みに振られる文字列（数直線ならば数字．数字でなくてもいい）

グラフを描くには，

1. まず，キャンバスを用意する
    ```py
    figure, axes = plt.subplot()
    ```
2. グラフを描く
    
    2.1. プロットを描く  
        ```py
        axes.plot()
        ```

    2.2. 軸ラベル，タイトル，凡例を補正する
        ```py
        axes.set_xlabel()
        ```
    
    2.3. 軸線を補正する
        ```py
        axes.set_xtick()
        ```

3. キャンバスのタイトル，凡例を補正する

4. キャンバスを画面に表示したり，ファイルに保存したりする

という流れになります．

```py
import numpy as np
x = np.array([x for x in range(100)])/100
fig, (axe_alice, axe_bob) = plt.subplots(2,1)  # Create a figure and an axes.
axe_alice.plot(x, x, label='linear')  # Plot some data on the axes.
axe_alice.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
axe_bob.plot(x, x**3, label='cubic')  # ... and some more.
axe_alice.set_xlabel('x label')  # Add an x-label to the axes.
axe_bob.set_ylabel('y label')  # Add a y-label to the axes.
axe_alice.legend()  # Add a legend.
axe_bob.set_title("Simple Plot")  # Add a title to the axes.
```




## 注意:  **Pylab**

*pylab* というモジュールがあります．このモジュールをimportすると，

```py
from matplotlib.pyplot import *
from numpy import *
```
が行われ，matplotlibのpyplotとnumpyの関数/クラス/定数を pylabのものとして呼び出すことができるようになります．

matplotlib.pyplot と numpy は，使用頻度の高いモジュールなので，それを1個のimport で呼び出せるので便利ではあります
**が，使わないほうがいいです** ．

