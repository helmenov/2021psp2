# day06: データサイエンス，機械学習（パターン認識）入門

データサイエンスにせよ，機械学習にせよ，データをデータフレームにまとめることから始まります．

データフレームとは，
- 計測項目または質問項目を各列（縦ベクトル）に並べ，サンプル（標本，被験者）が増えれば行を増やして項目を埋めていった表．

次のような表です．

|index|ID|favoriteAnimal|fortuneAnimal|birthMonth|CerelyFavor|歩数|BMI|
|---|---|---|---|---|----|---|---|
| | | | | | | | |

被験者（アンケート回答者）が増えれば行が増えていきます．
-  index: 被験者が増えれば1増やしていくような数です．単に実験者が被験者につけた番号です．

データフレームは，CSV（Comma-Separated-Values）形式での保存が一般的です．

上記のデータフレームは，

```csv
# mydata1.csv
ID, favoriteAnimal, fortuneAnimal, birthMonth, CerelyFavor, moneyIncreaseDiff,moneyIncreaseRatio
aa83988848, Sheep, Tanuki, 5, Hate, 3192, 1.01
```

のようなファイルになります．行ごとに列の文字数が異なるので，多少読みにくいですが，そもそもヒトが読むものではなく，計算機が読むためのものなので我慢です．

CSV形式はMicrosoft Excelなどの表計算ソフトのフォーマットと相互に変換できます．ヒトが読む場合は表計算ソフトで読み書きするのがいいでしょう．ExcelならCSVファイルを読み込むだけ，保存するときもCSVフォーマットを選ぶだけ．

また，データフレームに直せそうなデータをなんとかしてデータフレームに直すことを，スクレイピング（scraping）と呼んでいます．たとえば，コロナウイルスの陽性者数などの表はpdfで公開されていたりしますが，画像であるPDFから表の罫線を読み取って，罫線で区切られる数字や文字列を認識して，データフレームに直すなんてことだったりが，スクレイピングです．

さて，このCSVファイルをpythonで読みこんでみましょう．または，列の順番を変えたり，少し整形して，別の名前のCSVに保存してみましょう．

# Pandas パッケージ

`Pandas`は，データフレームを扱う ***「パッケージ」*** です．「パッケージ」とはモジュール(`.py`ファイル)を集めたフォルダ（ディレクトリ）です．つまり，Pandasはデータフレームを扱うための，クラスおよびクラスメソッド，関数，定数が定義された多数のモジュールが集められたフォルダで，人気があります．

# package

世界の誰かが作ったパッケージを，自分のPCで使うためには，当然ダウンロードしてくる必要があります．

パッケージ（フォルダ）をダウンロードし，自分のソースコードと同じディレクトリに置くと，

```py
from パッケージ名 import そのパッケージの中のモジュール名
```

で使えるようになります．

[ここ](psp2package.zip)にちょこっとしたパッケージを置きました．このzipファイルを解凍すると，
`psp2package`という名前のフォルダが作られます．その中には，`day06package`というフォルダがあり，その中に`mymodule1.py`というモジュールがあり，その中に`hello`という関数が書いてあります．

例えば，この`hello`という関数を動かす場合は，以下のようにします．`from`文にある「`.`」は，フォルダ構造の`/`や`¥`にあたる記号です．

```py
from psp2package.day06package import mymodule1

mymodule1.hello()
```

実は別の読み方があります．

```py
from psp2package.day06package.mymodule1 import *

hello()
```

モジュール名までをすべて`from`に書いて，`import`はモジュールに書いてある関数名です．すべての関数を使いたい場合は`*`を`import`します．このとき，関数呼び出しのしかたが少し違うことに注意してください．
しかし，この関数の呼び出し方は危険です．`hello()`などという関数名は頻出するので，他と重なってしまうからです．最初に紹介しているように`import モジュール名`を強くおすすめします．


ところで，パッケージ名を知っていても，その下のサブディレクトリも知っていなければならないというのは少し不便です．なので，パッケージ（ディレクトリ）のすぐ下に`__init__.py`というパッケージをモジュールのように扱うためのモジュールが作られることが多いです．（これってクラス定義の中に，__init__というメソッドを置くと，クラスを関数のように扱うのと同じです．）

`__init__.py`は，パッケージをモジュールであるかのごとく`import`したときに動かすモジュールです．

今，次のように動かしたいとします．

```py
import psp2package

psp2package.hello()
```

`import`文は指定したモジュールの展開（その場所にモジュールの記述をコピペ）ですので，
`psp2package`モジュールつまり`psp2package/__init__.py`の中は，

```py
from .day06package.mymodule1 import *
```

と書いてあるとよいみたいです．

## PyPIパッケージ: pip package

以前紹介したように，[PyPI](https://pypi.org/)というpythonには公式のパッケージ置き場があります．

PyPIに置いてあるパッケージは`pip`というコマンドでダウンロードされます．
ダウンロードされて，特別な場所に置かれることが決まっています．
また，ダウンロードされるパッケージが，さらに必要としている他のパッケージもダウンロードされます．

```sh
% pip install pandas
```

anaconda-pythonの学生さんは，

```sh
% conda install pandas
```

くだんの「特別な場所」に置かれたパッケージは，今現在動かすソースコードと同じディレクトリではないですが，いきなりパッケージを`from`文で読めることになっています．`pandas`フォルダの下の`io`サブフォルダの下の`parsers.py`というモジュールに書いてある関数をつかいたいなら

```py
from pandas.io import parsers
```

というようにします．

また，さきほど紹介したように`pandas`はパッケージ（フォルダ，ディレクトリ）ですが，すぐ下に`__init__.py`という「モジュールとして呼び出したときに動くモジュール」があるので，

```py
import pandas as pd
```

で呼び出すのが通常です．また，上記のように別名も`pd`とすることが多いです．

# pandas を使ってCSVをデータフレームにする

`pandas`の下の`io`の下の`parsers.py`にCSVファイルをデータフレームにする`read_csv`という関数があります．これを使います．

```sh
>>> import pandas as pd
>>> pd.set_option('display.unicode.east_asian_width', True)
>>>
>>> df1= pd.read_csv('mydata1.csv')
>>> print(type(df1))
<class 'pandas.core.frame.DataFrame'>
>>> print(df1)
           # mydata1.csv
ID                       favoriteAnimal  fortuneAnimal  birthMonth  CerelyFavor  moneyIncreaseDiff   moneyIncreaseRatio
aa83988848  Sheep                                                    Tanuki                                 5              Hate               3192                                 1.01
>>> print(df1.shape)
(2, 1)
```

データフレームは，`pandas.core.frame.DataFrame`というクラスです．`pandas`の下の`core`の下の`frame.py`というモジュールに`class DataFrame`と定義されています．

クラスに`__str__`メソッドがあるので，このクラスを割り当てられた`df1`を`print`できます．
ただし，日本語とアルファベットでは1文字あたりの表示幅が異なるので表示がズレます．このズレを補正するために，
`pd.set_option('display.unicode.east_asian_width', True)`を宣言しておきます．

また，クラスは，独自の属性を持ちます．`self.shape`つまり`df1.shape`はデータフレームの形である`（行数, 列数）`が保存されています．

でも`(2,1)`はおかしいですね．このデータは，`(1,7)`のはずです．

- 列のラベル（測定項目名やアンケート項目名）を **ヘッダ** といいます．このヘッダはデータ本体には数えませんのでデータ本体は`(1,7)`です．

最初の行は，CSV形式でなく単なるメモ書きですので，CSV形式は2行目からです．
読み飛ばす行番号を`skiprows`にリストします．

```sh
>>> df2 = pd.read_csv('mydata1.csv', skiprows=[0])
>>> print(df2.shape)
(1, 7)
>>> print(df2)
           ID  favoriteAnimal  fortuneAnimal   birthMonth   CerelyFavor    moneyIncreaseDiff   moneyIncreaseRatio
0  aa83988848              Sheep         Tanuki     5                  Hate  3192    1.01
>>> print(df2.columns)
Index(['ID', ' favoriteAnimal', ' fortuneAnimal', ' birthMonth', ' CerelyFavor',
       ' moneyIncreaseDiff', ' moneyIncreaseRatio'],
      dtype='object')
>>> print(type(df2.columns))
<class 'pandas.core.indexes.base.Index'>
```

CSVファイルを読むと，（読みとばしを無視した）最初の行を「ヘッダ」として理解します．
ヘッダは`self.columns`という属性に`Index`というクラスで保存されています．

CSVによってはヘッダが書かれていない場合があります．`mydata1.csv`で読み飛ばす行の番号を`[0,1]`としてみると

```sh
>>> df3 = pd.read_csv('mydata1.csv', skiprows=[0,1])
>>> print(df3.shape)
(0,  7)
>>> print(df3)
Empty DataFrame
Columns: [aa83988848,  Sheep,  Tanuki,  5,  Hate,  3192,  1.01]
Index: []
>>> print(df3.columns)
Index(['aa83988848', ' Sheep', ' Tanuki', ' 5', ' Hate', ' 3192', ' 1.01'], dtype='object')
```

データ本体の最初のサンプルが間違ってヘッダにされてしまいますので，この場合はヘッダが無いことを明記します．

```sh
>>> df4 = pd.read_csv('mydata1.csv', skiprows=[0,1], header=None)
>>> print(df4.shape)
(1,  7)
>>> print(df4)
            0    1     2  3  4     5   6
0  aa83988848   Sheep   Tanuki  5 Hate  3192  1.01
>>> print(df4.columns)
Int64Index([0, 1, 2, 3, 4, 5, 6], dtype='int64')
```

カラムラベルが数字になっています．

もし，カラムラベルを指定したいなら読み込んだ後に，

```sh
>>> df4.columns = ['ID', ' favoriteAnimal', ' fortuneAnimal', ' birthMonth', ' CerelyFavor',
       ' moneyIncreaseDiff', ' moneyIncreaseRatio'],
```
と属性columnsを上書きします．

ところで，ヘッダが「表示はされるがデータ本体ではない」のと同様に，`print(df1)`としたときに
最初の列に`0`が表示されています．これはデータ本体ではなく「**インデックス**」と読んでいます．データフレームを作ったときに割り当てられた行番号です．このあとにサンプル行を消したり，行の入れ替えなどをしても，最初のインデクスが維持されます．ヘッダがないときにカラムラベルが数字になったのと同じです．

もし`ID`の列をインデクスにしたいなら，CSVを読むときに，次のように指定します．
ヘッダの行も指定します．読み飛ばし行を読み飛ばしたあとの行番号です．


```sh
>>> df5 = pd.read_csv('mydata1.csv', skiprows=[0], header=0, index_col=0)
>>> print(df5)
            favoriteAnimal  fortuneAnimal   birthMonth   CerelyFavor    moneyIncreaseDiff   moneyIncreaseRatio
ID                                                                          
aa83988848              Sheep         Tanuki     5                  Hate  3192    1.01
>>> print(df5.shape)
(1,  6)
>>> print(df5.index)
Index(['aa83988848'], dtype='object', name='ID')
>>> print(df5.index.name)
ID
```

ヘッダ行番号を指定すると，それより上の行は読み飛ばされますので，今の場合，

```sh
>>> df6 = pd.read_csv('mydata1.csv', header=1, index_col=0)
```

でも同じです．

# データを集めたら...

さて，そんなこんなでデータを集めて，`mydata2.csv`に保存しました．
10人からデータをあつめたものです．

``` sh
>>> import pandas as pd
>>> pd.set_option('display.unicode.east_asian_width', True)
>>>
>>> df = pd.read_csv('mydata2.csv')
>>> print(df)
           ID favoriteAnimal fortuneAnimal  birthMonth CerelyFavor  moneyIncreaseDiff  moneyIncreaseRatio
0   friend001           Lion          Tigar    1    Like       1000      1.500
1   friend003            Cheetah        Cheetah    3   extremelyHate      -1000      0.700
2   friend004           Pegasus          Monkey    4   Regular     -10000      0.900
3   friend005           BlackPanthera        Sheep    2    Hate        150      1.001
4  friend0200             Elephant        Tanuki    7    Like       -300      0.800
5       umi03            Bear          Tigar    4   extremelyLike       -150      0.990
6   dorawemon            Tanuki       Lion    9    Like       1000      1.020
7      nobita              Tigar        Cheetah    8    Hate     -10000      0.500
8     shizuka            Tanuki       Lion    9   extremelyHate       2000      1.500
9       suneo           Lion        Cheetah    1    Hate       -300      0.999
```

IDには被験者やサンプルを区別するラベルが書かれています．学籍番号だったりします．表の表示には必要ですが，データの解析には必要ありません．

なので，

``` sh
>>> df = pd.read_csv('mydata2.csv', index_col=0)
>>> print(df)
           favoriteAnimal fortuneAnimal  birthMonth CerelyFavor  moneyIncreaseDiff  moneyIncreaseRatio
ID                                                                   
friend001            Lion          Tigar    1    Like       1000      1.500
friend003             Cheetah        Cheetah    3   extremelyHate      -1000      0.700
friend004            Pegasus          Monkey    4   Regular     -10000      0.900
friend005            BlackPanthera        Sheep    2    Hate        150      1.001
friend0200             Elephant        Tanuki    7    Like       -300      0.800
umi03                 Bear          Tigar    4   extremelyLike       -150      0.990
dorawemon             Tanuki       Lion    9    Like       1000      1.020
nobita                  Tigar        Cheetah    8    Hate     -10000      0.500
shizuka               Tanuki       Lion    9   extremelyHate       2000      1.500
suneo                Lion        Cheetah    1    Hate       -300      0.999
```

## データフレーム上の値のクラス

データフレーム上の値は以下のように参照できます．

-「favoriteAnimal」だけを全サンプル参照してみます．

```sh
>>> print(df['favoriteAnimal'])
ID
friend001     Lion
friend003      Cheetah
friend004     Pegasus
friend005     BlackPanthera
friend0200      Elephant
umi03          Bear
dorawemon      Tanuki
nobita           Tigar
shizuka        Tanuki
suneo         Lion
Name: favoriteAnimal, dtype: object

>>> print(type(df['favoriteAnimal']))
<class 'pandas.core.series.Series'>
```

- 行番号2（行番号は0からはじまる）のサンプルの「favoriteAnimal」は

```sh
>>> print(df['favoriteAnimal'][2])
Pegasus
>>> print(type(df['favoriteAnimal'][2]))
<class 'str'>
```

- 行番号2から4までの3行のサンプルの「favoriteAnimal」は

```sh
>>> print(df['favoriteAnimal'][2:5])
ID
friend004     Pegasus
friend005     BlackPanthera
friend0200      Elephant
Name: favoriteAnimal, dtype: object
```

データ集め終えたときに次にやることは，各項目の統計でしょうか．たとえば平均値や標準偏差でしょうか．

そんな統計をまとめて表示してくれる関数がpandasに存在します．

```sh
>>> print(df.describe(include='all))
       favoriteAnimal fortuneAnimal     birthMonth CerelyFavor  moneyIncreaseDiff  moneyIncreaseRatio
count          10             10  10.000000         10           10.000000           10.000000
unique          8              6        NaN          5                 NaN                 NaN
top      Lion         Cheetah        NaN       Like                 NaN                 NaN
freq            2              3        NaN          3                 NaN                 NaN
mean          NaN            NaN   4.800000        NaN        -1760.000000            0.991000
std           NaN            NaN   3.190263        NaN         4425.293462            0.314412
min           NaN            NaN   1.000000        NaN       -10000.000000            0.500000
25%           NaN            NaN   2.250000        NaN         -825.000000            0.825000
50%           NaN            NaN   4.000000        NaN         -225.000000            0.994500
75%           NaN            NaN   7.750000        NaN          787.500000            1.015250
max           NaN            NaN   9.000000        NaN         2000.000000            1.500000
```

全て，各項目ごとの代表値で，

- `count`はデータの個数(sample size，サンプルサイズ)
- `unique`はデータに現れた水準の個数
- `top`はデータの最頻値，`freq`は最頻値の頻度
- `mean`は平均値，`std`は標準偏差(STandard Deviation)
- `min`は最小値，`max`は最大値，
- `25%`, `50%`, `75%`は四分位で，ヒストグラムを低い水準から並べたときに下位25％，50％，75％にあたる水準を答えるものです．下位50％は`median`（メディアン，メジアン）とも呼ばれます．
- `NaN` は ***Not a Number*** 値なし

この関数の中身は，以下のDataFrameのメソッドを使っても表示されます．

```sh
>>> print(df.mean())
birthMonth                   4.800
moneyIncreaseDiff   -1760.000
moneyIncreaseRatio       0.991
dtype: float64
>>> print(df.median())
birthMonth                  4.0000
moneyIncreaseDiff   -225.0000
moneyIncreaseRatio      0.9945
dtype: float64
>>> print(df.sdv())
birthMonth                   3.190263
moneyIncreaseDiff    4425.293462
moneyIncreaseRatio       0.314412
dtype: float64
>>> print(df.quantile(0.25))
moneyIncreaseDiff   -825.000
moneyIncreaseRatio      0.825
Name: 0.25, dtype: float64
>>> print(df.quantile([0.25,0.75]))
      moneyIncreaseDiff  moneyIncreaseRatio
0.25              -825.0             0.82500
0.75               787.5             1.01525
```
です．

ところで，「birthMonth」，「moneyIncreaseDiff」，「moneyIncreaseRatio」ですが，その平均や標準偏差ってどんな意味があるのでしょうか？

-「moneyIncreaseDiff」の平均は理解可能です．昨日の所持金に比べ，全員が平均何円増加したかを表しています．標準偏差もその増加額が人によってどのくらい幅があるかです．
- 「moneyIncreaseRatio」はどうでしょうか？平均は1周辺にあるのですが，全員が平均何倍増加したかを表していますね．標準偏差はその増加比が人によってどのくらい幅があるかですね．


「birthMonth」はどうでしょうか？おそらくmeanやmedianの結果は，6月周辺の月になっているでしょう．だから何なのでしょう．この値は一番多いbirthMonthではありません．
一番多いbirthMonthは最頻値(モード,mode)です．上記には表示されていません．birthMonthの最頻値なら意味があります．

「birthMonth」は，1〜12で答えられていますが，この数値は，データ的には大小がない値で有るべきなのです．よってクラスを「カテゴリー」に変更します．astype*メソッド*を使い文字列クラスに変更した後に，Categorical*関数*でカテゴリークラスに変更します．

```sh
>>> df['birthMonth'] = df['birthMonth'].astype('str') 
>>> listBirthMonth = list([str(x) for x in range(1,13)])
>>> df['birthMonth'] = pd.Categorical(df['birthMonth'], categories=listBirthMonth)
>>> print(df['birthMonth'])
ID
friend001     1
friend003     3
friend004     4
friend005     2
friend0200    7
umi03         4
dorawemon     9
nobita        8
shizuka       9
suneo         1
Name: birthMonth, dtype: category
Categories (12, object): ['1', '2', '3', '4', ..., '9', '10', '11', '12']
```

さて，「CerelyFavor」は，birthMonthとは逆に，値は文字列ですが，これって5段階評価で，大小があります．なので，文字列を大小のある値に変換します．大小があるカテゴリーは，`ordered=True`を指定します．

```sh
>>> listCelery = list(['extremelyHate','Hate','Regular','Like','extremelyLike'])
>>> df['CerelyFavor']=pd.Categorical(df['CerelyFavor'],categories=listCelery, ordered=True)
>>> print(df['CerelyFavor'])
ID
friend001       Like
friend003     extremelyHate
friend004     Regular
friend005       Hate
friend0200      Like
umi03         extremelyLike
dorawemon       Like
nobita          Hate
shizuka       extremelyHate
suneo           Hate
Name: CerelyFavor, dtype: category
Categories (5, object): ['extremelyHate' < 'Hate' < 'Regular' < 'Like' < 'extremelyLike']
```

また，大小ありのカテゴリは，数値を持っていて，cat.codesメソッドでその数値を読むことができます．
この数値を新しい項目「CerelyFavor度値」に保存することにします．

```sh
>>> df['CerelyFavor度値']=df['CerelyFavor'].cat.codes
>>> print(df['CerelyFavor度値'])
ID
friend001     3
friend003     0
friend004     2
friend005     1
friend0200    3
umi03         4
dorawemon     3
nobita        1
shizuka       0
suneo         1
Name: CerelyFavor度値, dtype: int8
```

- 「favoriteAnimal」と「fortuneAnimal」

「動物占い」を知ってますか．2000年くらいに流行した「人は12種類の動物に代表される性格があるけど，あなたは？」っていうものです．
Lion、Cheetah、Pegasus、Elephant、Monkey、狼、Bear、Tigar、BlackPanthera、Sheep、Tanuki、こじか の12種類です．
単純に誕生日で決まっているようです．

[動物占い公式ページ](https://www.doubutsu-uranai.com)

今回のデータの「favoriteAnimal」と「fortuneAnimal」はこの12種類から選ばれるとします．

どんな動物かは順序がありません．よって数値の割り振りは適当で構いません．よって，これらもカテゴリ（大小なし）です．

```sh
>>> listAnimal = list(['Lion','Cheetah','Pegasus','Elephant','Monkey','狼','Bear','Tigar','BlackPanthera','Sheep','Tanuki','こじか'])
>>> df['favoriteAnimal'] = pd.Categorical(df['favoriteAnimal'], categories=listAnimal, ordered=False)
>>> df['fortuneAnimal'] = pd.Categorical(df['fortuneAnimal'], categories=listAnimal, ordered=False)
>>> print(df['favoriteAnimal'])
ID
friend001     Lion
friend003       Cheetah
friend004     Pegasus
friend005     BlackPanthera
friend0200        Elephant
umi03           Bear
dorawemon       Tanuki
nobita              Tigar
shizuka         Tanuki
suneo         Lion
Name: favoriteAnimal, dtype: category
Categories (12, object): ['Lion', 'Cheetah', 'Pegasus', 'Elephant', ..., 'BlackPanthera', 'Sheep', 'Tanuki', 'こじか']
>>> print(df['fortuneAnimal'])
ID
friend001           Tigar
friend003       Cheetah
friend004           Monkey
friend005       Sheep
friend0200      Tanuki
umi03               Tigar
dorawemon     Lion
nobita          Cheetah
shizuka       Lion
suneo           Cheetah
Name: fortuneAnimal, dtype: category
Categories (12, object): ['Lion', 'Cheetah', 'Pegasus', 'Elephant', ..., 'BlackPanthera', 'Sheep', 'Tanuki', 'こじか']
```

すべての項目を適切な尺度水準にしたので，

```sh
>>> print(df.describe(include='all'))
       favoriteAnimal fortuneAnimal birthMonth CerelyFavor  moneyIncreaseDiff  moneyIncreaseRatio  CerelyFavor度値
count          10             10     10         10           10.000000           10.000000       10.000000
unique          8              6      7          5                 NaN                 NaN             NaN
top      Lion         Cheetah      1       Hate                 NaN                 NaN             NaN
freq            2              3      2          3                 NaN                 NaN             NaN
mean          NaN            NaN    NaN        NaN        -1760.000000            0.991000        1.800000
std           NaN            NaN    NaN        NaN         4425.293462            0.314412        1.398412
min           NaN            NaN    NaN        NaN       -10000.000000            0.500000        0.000000
25%           NaN            NaN    NaN        NaN         -825.000000            0.825000        1.000000
50%           NaN            NaN    NaN        NaN         -225.000000            0.994500        1.500000
75%           NaN            NaN    NaN        NaN          787.500000            1.015250        3.000000
max           NaN            NaN    NaN        NaN         2000.000000            1.500000        4.000000
```


# 課題

1.「favoriteAnimal」が「Lion」の人と「Tanuki」の人でCerelyFavor度は差があると言えるか調べよ．調べるためのコード実行例を示せ．
一般的に双方の四分位範囲が重ならない場合「差がある」と言う．重なっている場合は「差があると言えない」と言う．

```sh
>>> print(df[df['favoriteAnimal']=='Lion'].describe())
       moneyIncreaseDiff  moneyIncreaseRatio  CerelyFavor度値
count            2.000000             2.00000        2.000000
mean           350.000000             1.24950        2.000000
std            919.238816             0.35426        1.414214
min           -300.000000             0.99900        1.000000
25%             25.000000             1.12425        1.500000
50%            350.000000             1.24950        2.000000
75%            675.000000             1.37475        2.500000
max           1000.000000             1.50000        3.000000
```
※四分位範囲(IQR, Inter Quantile Range)とは，25%-75%の広さである．

2. 「favoriteAnimal」が「Lion」の人と「Tanuki」の人では，どちらが平均的に今日の所持金が多いか？（どちらが増加が大きいかではない）









