# day03: 例外処理

gitでバージョン管理しながら例外処理を学びます．

## まず git を使おう

gitを使うためには，ディレクトリをgit対応にしなければいけません．

```bash
$ cd Git対応にしたいディレクトリ
$ git init
```

これでGit対応になりました．`.git`という隠れディレクトリができます．

## ファイルを監視対象にする（追加・削除・移動・リネーム・内容改変）

管理する場合は，管理する事象を思い出したら，

```bash
$ git add 管理したいファイル
```

この時点では，変更が記録されていません．注意してください．

## 変更の記録

さて，一通りの作業を行い，現場から離れる場合，ゲームをセーブします．

```bash
$ git commit -m "変更内容のダイジェスト"
```

commitを行うためには，アカとメアドを指定しないといけません．

```bash
$ git config --global user.name 'helmenov'
$ git config --global user.email 'kotaro1976@gmail.com'
```

## gitのバージョン管理を実践してみよう

前回の課題に関連したプログラムがあります．

- [d03.py](./d03_00.py)

```py
# d03.py
from turtle import * 
import math

def come(x,y):
    """
    座標（x,y）を向いて，その方向に距離を一割だけ縮める
    """
    
    (xx,yy) = position()
    val_tan = (yy-y)/(xx-x)
    theta = math.atan(val_tan)
    head = heading()
    new_head = theta*180/math.pi - head
    walk = math.sqrt((xx-x)**2 + (yy-y)**2)/10
    left(new_head)
    forward(walk)

MyList = [1,2,3]
NowPos = 5
NowVal = MyList[NowPos]

onscreenclick(come)

done()

```

とりあえず，これをgitで管理しましょう．

最初の最初は，ディレクトリをgit管理対応にします．

```bash
$ cd 2021psp2
$ git init
```

その上で，

```bash
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        day03/

nothing added to commit but untracked files present (use "git add" to track)

$ git add day03/d03.py

$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   day03/d03.py

```

最初の最初は，この状態をセーブしておきましょう．

設定をしていなければ，

```bash
$ git config --global user.name YourName
$ git config --global user.email YourEmail
```

その上で，

```bash
$ git commit -m "最初の状態"
$ git status
On branch main
nothing to commit, working tree clean
```

## ファイル改修

さて，この `d03.py` を実行すると，次のようにして実行完了せずにコケる．

```bash
$ python -m d03
Traceback (most recent call last):
  File "/home/kotaro/miniconda3/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/kotaro/miniconda3/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/kotaro/work/2021psp2/ex/day03/d03.py", line 21, in <module>
    NowVal = MyList[NowPos]
IndexError: list index out of range
```

これを読めないといけない．まず，このメッセージは，
1. 「Traceback (most recent call last)」
2.  「IndexError」
の2項目からなることがインデントで区分けされたブロックからわかる．一般的にエラーメッセージは，Tracebackとエラー分類からなる．

Traceback（トレースバック）は，「ここでコケた」→「その原因はこの行の失敗」→「そのまた原因はこの行の失敗」というように大元の問題の場所を辿ったものである．今回の例では，File "/home/kotaro/work/2021psp2/ex/day03/d03.py"の21行目に問題があり，この行が呼び出した処理が問題だったようだ．

IndexErrorは，今回の問題のエラー分類であり

> IndexError: list index out of range

英語の文法として間違っているが，これは日本語での「体言止め」にあたる英語圏の用法であり，記事のタイトルや見出しで使われる．be 動詞を抜いて，be動詞以降で形容される主語，みたいな形になっている．

> list index **is** out of range

 リストインデクスが範囲の外にある．つまりリストのインデクスが，リストの範囲でカバーされていないというエラーである．MyListは3つしか要素がないのにMyList[5]（6番目の要素）などない．

 さて，以上のようなエラーメッセージとともにプログラムを止められてしまっては困る．とりあえず先に進めたい．

 そういうわけで，「エラーの解決を先送り」する．

```py
MyList = [1,2,3]
NowPos = 5
NowVal = MyList[NowPos]

onscreenclick(come)
```

を，「エラーを起こす処理を，実際に実行するのではなく，tryする．」

その上で，
- エラーが起きた場合の例外処理を「except エラー分類名:」
- エラーが起きなかった場合の処理を「else:」

```py
MyList = [1,2,3]
NowPos = 5

try: 
    NowVal = MyList[NowPos]
except IndexError:
    print('MyListから取り出せないので，とりあえず99入れときます．')
    NowVal = 99
else:
    pass

onscreenclick(come)
```

エラーがある場合，その場でエラーを解決するのがベストではありますが，とりあえず例外処理をするクセをつけてください．エラーは落ち着いて，後から直しましょう．

##  git でバージョン管理しよう

そんなわけでとりあえず例外処理でエラーはキャッチした（解決はしていないが）ので，

今の時点の編集前後の差異は，

```bash
$ git diff d03.py
diff --git a/day03/d03.py b/day03/d03.py
index bde9aeb..27a765f 100644
--- a/day03/d03.py
+++ b/day03/d03.py
@@ -18,7 +18,14 @@ def come(x,y): 

    MyList = [1,2,3]
    NowPos = 5
- NowVal = MyList[NowPos]
+
+ try:
+   NowVal = MyList[NowPos]
+ except IndexErrror:
+   print('MyListから取り出せないので，とりあえず99入れときます．')
+   NowVal = 99
+ else:
+   pass

    onscreenclick(come)
```

「編集前後」といったが正しくは，前回のセーブ時のファイル内容との差である．

さて，この差異を記録したいので，まずステージに上げる．

```bash
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   d03.py

no changes added to commit (use "git add" and/or "git commit -a")
$ git add d03.py
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   d03.py
```

ではセーブしよう．

```bash
$ git commit -m "d03.py: 例外処理した"
```

などとして，セーブします．

## git セーブ履歴をみる

```bash
$ git log
commit  022da560ab3915b397b40d9c1fafb7ba54bf82ce (HEAD -> main)
Author: helmenov <kotaro1976@gmail.com>
Date: Sun Apr 25 17:02:43 2021 +0900

    d03.py: 例外処理した

commit  4da152ee5cd582c0b0b1f7f2be107284baf9a0ab
Author: helmenov <kotaro1976@gmail.com>
Date: Sun Apr 25 16:45:56 2021 +0900

    最初の状態
```

上から順に，新しいセーブ履歴が読める．

commitのあとの英数字の羅列が「ハッシュ」と呼ばれる，他と重なることのないIDである．最先端のセーブには「HEAD」という別名もある．

では，「最初の状態」とした4/25 16:45:56のセーブ直後に戻ろう．このように指定の仕方が困難なのでハッシュでいうと 4da152ee に戻ろう（ハッシュ指定だとはじめの8文字くらいで十分）

```bash
$ git restore --source 4da152ee d03.py
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   d03.py
```

これでd03.pyを 4da152ee... のコミットIDの状態に戻すことができる．

```
$ git restore --source HEAD^1 d03.py
```
でもいい．`^n`は「n代昔にさかのぼる」

戻した上で少し改変したとする．

```bash
$ git add d03.py
$ git commit -m "d03.py: 別の改変"
$ git log --graph
* commit  6a4e1e35b83fa702b7eb1b8ebd7dd373ad79d086 (HEAD | -> main)
| Author: helmenov <kotaro1976@gmail.com>
| Date: Sun Apr 25 17:29:25 2021 +0900
| 
|     d03.py: 別の改変
| 
* commit  022da560ab3915b397b40d9c1fafb7ba54bf82ce (HEAD -> main)
| Author: helmenov <kotaro1976@gmail.com>
| Date: Sun Apr 25 17:02:43 2021 +0900
| 
|    d03.py: 例外処理した
| 
* commit  4da152ee5cd582c0b0b1f7f2be107284baf9a0ab
 Author: helmenov <kotaro1976@gmail.com>
 Date: Sun Apr 25 16:45:56 2021 +0900
 
   最初の状態
```

すなわち，4da152eeのセーブ状態に戻して改変したのだが，022da560のセーブ状態から改変ぶんが記録される．

d03.pyだけでなくすべてを戻したいときは，

もし，昔の状態を「見たいだけ」（改変するつもりがない）ならば
```bash
$ git checkout コミットID
```

もし，「見たいだけ」なのではなく，すべてをやり直したいのなら
```
$ git reset --hard コミットID
```

## git で，ローカルのディレクトリを，演習室のディレクトリにバックアップしよう．

### 遠隔ログイン

まず，自分のノートパソコンから，演習室のマシンに，遠隔ログインしよう．

```bash
ssh sonoda@bes-master.cis.nagasaki-u.ac.jp
```

`ssh`は **Secure Shell**のことで，秘匿通信するソフトウェアです．引数は，bes-master.cis.nagasaki-u.ac.jpという演習室の一つのマシンの名前と，そのマシンの中のアカウントで構成されています．

パスワードなど聞かれたのちに，遠隔でマシンに入ることができます．

```bash
$ uname -a
Linux bes-master 3.10.0-1160.11.1.el7.x86_64 #1 SMP Fri Dec 18 16:34:56 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

### 演習室にバックアップ先を作る（最初の1回だけ）

1. `~/MyRepository/2021psp2.git`というディレクトリを作って
2. ディレクトリをgit対応にして
3. 演習室を抜けます．


```bash
$ mkdir ~/MyRepository
$ cd MyRepository
$ mkdir 2021psp2.git
$ cd 2021psp2.git
$ git init --shared=true
$ exit
```


### 自分のノーパソで．

