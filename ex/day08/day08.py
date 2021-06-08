#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

x = np.array([x for x in range(12)])/10


# pyplotのsubplots関数でfigure(キャンバス)とaxes(グラフ群)とで構成されるタプルを発行します．
# subplotsの引数は，figure上に並べるaxesの(行数,列数)です．

# In[2]:


(fig, (axe_alice, axe_bob)) = plt.subplots(1,2)  # Create a figure and an axes.


# axesクラスの各種メソッドでグラフを描きます．
# - `plot`メソッドはラインプロット（曲線）です．
# - `scatter`メソッドは散布図です．
# - `stem`メソッドは棒グラフです．
# 
# display関数は絵を表示します．print関数が文字列を表示するように．

# In[3]:


axe_alice.plot(x, x, label='linear')  # Plot some data on the axes.
axe_alice.scatter(x, x**2, label='quadratic')  # Plot more data on the axes...

axe_bob.stem(x, x**3, label='cubic')  # ... and some more.

display(fig)


# - axesクラスの各種`set_**`メソッドでグラフ周りの軸ラベル，グラフタイトルなどを設定できます．
# - axesクラスの`legend`メソッドはグラフのlabelを凡例として追記します．

# In[4]:


axe_alice.set_ylabel('this is y label on alice')  # Add an x-label to the axes.
axe_alice.legend()  # Add a legend.
axe_alice.set_title("Alice plot")

axe_bob.set_xlabel('here is x label on bob')  # Add a y-label to the axes.
axe_bob.set_title("Bob plot")  # Add a title to the axes.

display(fig)


# - axesクラスの各種`get_**`メソッドはグラフ周りの軸ラベル，グラフタイトルなどを抽出します

# In[5]:


print(axe_alice.get_ylabel())
print(axe_bob.get_xlabel())
print(axe_bob.get_title())


# In[6]:


# ticksは目盛を打つ数値のリスト
print(axe_alice.get_xticks())
# ticklabelsは目盛に振る文字列
print(axe_alice.get_xticklabels())


# In[7]:


# limはグラフ表示範囲の下限と上限
print(axe_alice.get_ylim())
print(axe_bob.get_ylim())
axe_alice.set_ylim(axe_bob.get_ylim())
display(fig)


# In[8]:


# scale は軸のスケール（Linear 線形, log 対数）
print(axe_alice.get_xscale())


# In[9]:


axe_alice.set_xscale('log')
#axe_alice.set_xscale('symlog')
#axe_alice.set_xscale('logit')
display(fig)


# axeの`annotate`メソッドは，グラフにテキストや矢印などを加えます．

# In[10]:


axe_bob.annotate('arrowstyle', 
            xy=(0, 1), xycoords='data',      # 矢印の先(xy)を軸の値(data)で指定
            xytext=(50, 30), 
            textcoords='offset points',      # 文字の位置(xytext)を矢印の先からの相対距離(offset points)で指定
            arrowprops=dict(arrowstyle="->")
            )
display(fig)


# figureクラスの`add_axes`メソッドは，新たに`axes`を加えます．

# In[11]:


axe_kotaro = fig.add_axes([.65, .2, .2, .2])
axe_kotaro.plot(x,x**4)
display(fig)


# `savefig`関数は，キャンバスを画像ファイルに保存します．

# In[12]:


plt.savefig('day08.png')

