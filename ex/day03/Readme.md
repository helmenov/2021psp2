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

Traceback（トレースバック）は，「ここでコケた」→「その原因はこの行の失敗」→「そのまた原因はこの行の失敗」というように大元の問題の場所を辿ったものである．今回の例では，`File "/home/kotaro/work/2021psp2/ex/day03/d03.py"`の21行目に問題があり，この行が呼び出した処理が問題だったようだ．

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
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   d03.py

no changes added to commit (use "git add" and/or "git commit -a")
$ git add d03.py
$ git status
On branch master
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
commit  022da560ab3915b397b40d9c1fafb7ba54bf82ce (HEAD -> master)
Author: helmenov <kotaro1976@gmail.com>
Date: Sun Apr 25 17:02:43 2021 +0900

    d03.py: 例外処理した

commit  4da152ee5cd582c0b0b1f7f2be107284baf9a0ab
Author: helmenov <kotaro1976@gmail.com>
Date: Sun Apr 25 16:45:56 2021 +0900

    最初の状態
```

上から順に，新しいセーブ履歴が読める．

commitのあとの英数字の羅列が「 **ハッシュ** 」と呼ばれる，他と重なることのないIDである．最先端のセーブには「 **HEAD** 」という別名もある．

##  特定のコミット（セーブ）直後にファイルを戻す．

では，「最初の状態」とした4/25 16:45:56のセーブ直後に戻ろう．このように指定の仕方が困難なのでハッシュでいうと `4da152ee` に戻ろう（ハッシュ指定だとはじめの8文字くらいで十分）

```bash
$ git restore --source 4da152ee d03.py
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   d03.py
```

これで `d03.py` を `4da152ee...` のコミットIDが示すセーブ状態に戻すことができる．

コミットIDの代わりに，`HEAD`（現在地点）と世代さかのぼり`^n`を使った書き方で

```bash
$ git restore --source HEAD^1 d03.py
```

さて，戻した上で少し改変したとする．そしてコミットセーブする（`add`を忘れないこと）．

```bash
$ git add d03.py
$ git commit -m "d03.py: 別の改変"
$ git log --graph
* commit  6a4e1e35b83fa702b7eb1b8ebd7dd373ad79d086 (HEAD -> master)
| Author: helmenov <kotaro1976@gmail.com>
| Date: Sun Apr 25 17:29:25 2021 +0900
| 
|     d03.py: 別の改変
| 
* commit  022da560ab3915b397b40d9c1fafb7ba54bf82ce
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

`--graph`オプションをつけて`git log`するとコミットの繋がりが表示される．

この `log` を見ると， `4da152ee` のセーブ状態（まだ例外処理をしていない状態）に戻して，その後改変したのだが，実際は， `022da560` のセーブ状態（例外処理を加えた状態）からの改変ぶんが記録される．すなわちその改変とは，「例外処理をしていないコードへの変更＋その後の改変」が記録されている．

つまり，例外処理を加えた **事実は無かったことにせず，きちんと残しておく** ，ということである．

## 特定のコミット直後にすべてのファイルを戻したい．( `restore`  をすべてのファイルに対して行う)

`git restore --source commitID file`はあるファイルだけを戻すのだったが，すべてのファイルを戻したいなら，`git revert commitID`

##  特定のコミット直後を見たい

`restore`と`revert` は，特定のコミット直後の状態に戻すような改変を加える処理であった．

これに対し，現在のコミット `022da560` を維持したまま，特定のコミット `4da152ee` 直後の状態をリロードする処理もある．ただし，リロードした後に別の改変を加えると，コミット `022da560` へのつながりが切れてしまうので，あくまでリロードだけ（見るだけ）に留めて，見終えたら元のコミット `022da560` に足を戻すことをすすめる．


```bash
$ git checkout コミットID
```

## （危険）特定のコミットに「リセット」したい（その後のコミットを歴史から消す）

もし，「見たいだけ」なのではなく，すべてをやり直したいのなら

```bash
$ git reset --hard コミットID
```

## （危険）gitコマンドをやり直したい．

commitやresetというコマンドの履歴を見ることができる．

```bash
$ git reflog
```

例えば，先程の 「別の改変」コミット `6a4e1e35` のあとで，「最初の状態」コミット `4da152ee` まで「リセット」したとする．

```bash
$ git reset --hard 4da152ee 
HEAD is now at  4da152e 最初の状態
```

この状態で， `log` を見ると

```bash
$ git log --graph
* commit  4da152ee5cd582c0b0b1f7f2be107284baf9a0ab
 Author: helmenov <kotaro1976@gmail.com>
 Date: Sun Apr 25 16:45:56 2021 +0900
 
   最初の状態
```

すなわち，その後のcommit（セーブ）が無くなっている．「リセットを間違った」と言うときは，`reset` コマンドをやり直せばよい．
`log`コマンドと似ている`reflog`というコマンドを使うと，`commit` と `reset` をすべて表示する．

```bash
$ git reflog
4da152e (HEAD -> master) HEAD@{0}:  reset:  moving to 4da152ee
6a4e1e3 HEAD@{1}:  commit:  d03.py:  別の改変
022da56 HEAD@{2}:  commit:  d03.py:  例外処理した
4da152e (HEAD-> main)  HEAD@{3}: commit (initial): 最初の状態
```

まず，`log`と違い，すべての `commit` と `reset` が表示されている．

また，左端の英数字がコミットIDだが， `4da152e` が2つあることに気づくだろう．というわけで，

またしても，特定のコミット `HEAD@{1}` にリセットすればよい．英数字ハッシュのコミットIDでリセット位置を指定していないことに注意．

```bash
$ git reset --hard HEAD@{1}

$ git log --graph 

$ git log --graph
* commit  6a4e1e35b83fa702b7eb1b8ebd7dd373ad79d086 (HEAD -> master)
| Author: helmenov <kotaro1976@gmail.com>
| Date: Sun Apr 25 17:29:25 2021 +0900
| 
|     d03.py: 別の改変
| 
* commit  022da560ab3915b397b40d9c1fafb7ba54bf82ce
| Author: helmenov <kotaro1976@gmail.com>
| Date: Sun Apr 25 17:02:43 2021 +0900
| 
|    d03.py: 例外処理した
| 
* commit  4da152ee5cd582c0b0b1f7f2be107284baf9a0ab
 Author: helmenov <kotaro1976@gmail.com>
 Date: Sun Apr 25 16:45:56 2021 +0900
 
   最初の状態

$ git reflog
6a4e1e3 (HEAD -> master) HEAD@{0}:  reset:  moving to HEAD@{1}
4da152e HEAD@{1}:  reset:  moving to 4da152ee
6a4e1e3 (HEAD -> master) HEAD@{2}:  commit:  d03.py:  別の改変
022da56 HEAD@{3}:  commit:  d03.py:  例外処理した
4da152e HEAD@{4}: commit (initial): 最初の状態
```

`reflog` には最後のリセットし直しのリセットも記録されている．


## git で，ローカルのディレクトリを，演習室のディレクトリにバックアップしよう．

### 遠隔ログイン

まず，自分のノートパソコンから，演習室のマシンに，遠隔ログインしよう．

```bash
ssh sonoda@bes-master.cis.nagasaki-u.ac.jp
```

`ssh`は **Secure Shell**のことで，秘匿通信するソフトウェアです．引数は，`bes-master.cis.nagasaki-u.ac.jp` という演習室の一つのマシンの名前と，そのマシンの中のアカウントで構成されています．

パスワードなど聞かれたのちに，遠隔でマシンに入ることができます．

```bash
$ uname -a
Linux bes-master 3.10.0-1160.11.1.el7.x86_64 #1 SMP Fri Dec 18 16:34:56 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```


### 演習室にバックアップ先を作る（最初の1回だけ）

1. `~/MyRepository/2021psp2.git`というディレクトリを作って
2. ディレクトリをgit対応にして （他の人も見えるように `--shared = true`オプションをつける）
3. そのディレクトリの下で，以下のgitコマンドを打つ．（4/28追記）
   `git config --local receive.denyCurrentBranch updateInstead`
4. 演習室を抜けます．


```bash
$ mkdir ~/MyRepository
$ cd MyRepository
$ mkdir 2021psp2.git
$ cd 2021psp2.git
$ git init --shared=true
$ git config --local receive.denyCurrentBranch updateInstead
```

これでレポジトリ（git対応ディレクトリのこと）ができました．

あとで使うので絶対パス（場所）を確認して，メモしておきましょう．

```bash
$ pwd
/home/mother/sonoda/MyRepository/2021psp2.git
```

あとはリモートPCから抜けます．（ログアウト）

```bash
$ exit
```


### 自分のノーパソで．

まず，リモートバックアップ先に演習室の先程のレポジトリを`origin`という名前でブックマークします．

```bash
$ git remote add origin ssh://sonoda@bes-master.cis.nagasaki-u.ac.jp:/home/mother/sonoda/MyRepository/2021psp2.git
```

`xxx://yyy` という部分は 「`xxx`というプロトコルの`yyy`というURL」と読みます．`http://www.google.com`が，HTTP通信で`www.google.com`というURL，と読むように今回は，sshプロトコル(Secure Shell通信)で`bes-master.cis.nagasaki-u.ac.jp`というURLをブックマークしています．

`zzz@yyy`という部分は，「`yyy`というURL上の`zzz`というユーザ」と読みます．`sonoda@bes-master.cis.nagasaki-u.ac.jp`は，`bes-master.cis.nagasaki-u.ac.jp`というマシンの`sonoda`というアカウントユーザです．メールアドレスもこの書き方ですね．

そのうしろの`: /home/mother/sonoda/MyRepository/2021psp2.git` は先程メモしたディレクトリの絶対パス（場所）です．

```bash
$ git push origin master 
Enter passphrase for key '/home/kotaro/.ssh/id_rsa':
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (12/12), 1.30 KiB | 666.00 KiB/s, done.
Total 12 (delta 2), reused 0 (delta 0), pack-reused 0
To ssh://bes-master.cis.nagasaki-u.ac.jp:/home/mother/sonoda/MyRepository/2021psp2.git
 * [new branch]      master -> master
```

この`push リモートバックアップ先の名前  master`でリモートバックアップできました．logを確認すると，`origin/master`と文字列が増えています．
つまり，ローカルのmain と リモートoriginのmaster という2つの系統がある，ということです．

```bash
$ git log --graph
* commit  6a4e1e35b83fa702b7eb1b8ebd7dd373ad79d086 (HEAD -> main, origin/master)
...
```

### ここでまたローカルPCのファイルをいじる

バックアップした後に，またソースコードを書き加えたり，ファイルを追加したり，いろいろします．そして `add` して `commit` するのですが，その状態で `log` を見てみます．

```bash
$ git add d03.py
$ git commit -m "left -> right"
$ git log
$ git log --graph
* commit  3be4208aee8aa6114c501fd5bb5b40f937ded8c0 (HEAD -> master)
| Author: helmenov <kotaro1976@gmail.com>
| Date:   Wed Apr 28 00:02:47 2021 +0900
| 
|         d03.py:  left -> right
|
* commit  6a4e1e35b83fa702b7eb1b8ebd7dd373ad79d086 (origin/master)
|
...
```

コミットが追加されていますが，リモートレポジトリ `origin` の状態は変わっていません．先程と同じように，`git push` すると，リモートの状態をローカルの状態に合わせます．

ただし，リモートレポジトリの中身は別の人が変更しているかもしれません．なので，`git commit`の後に，すぐ`git push`するのではなく先に`git pull`（ローカルに，リモートの変更を取り込む）してから`git push`します．

(※ 本当は，`pull` ではなく，`fetch`（リモートの状態をローカルの作業場以外のところにコピー）して， `merge` （2つの作業場を合わせて1つにする)してコピーをローカルに取り込むのが正しい流れですが，初心者は  `pull`  でいいです）

```bash
$ git pull origin master
$ git log
*             commit  9740140fffaa9a0d5f793caa63e16cbef1b9edf7 (HEAD -> master)
|  \          Merge:  3be4208  b311fa3
|    |         Date:  Wed Apr 28 00:39:21  2021  +0900
|    |   
|    |                         Merge branch 'master'  of ssh://..........
|    | 
*   |          commit  3be4208aee8aa6114c501fd5bb5b40f937ded8c0
|    |          Author: helmenov <kotaro1976@gmail.com>
|    |         Date:   Wed Apr 28 00:02:47 2021 +0900
|    |
|    |                         d03.py:  left -> right
|    |
|    *        commit  b311fa3126e44539c711861cb0819340e239530  (origin/master)
|  /          Author:   Nobunaga Oda <nobunaga@cis.nagasaki-u.ac.jp>
|             Date:   .....
|
|                               ちょっと変えるね
|
*               commit  6a4e1e35b83fa702b7eb1b8ebd7dd373ad79d086 
|
...
```

`pull`したら，誰かの変更がリモートにあったようで，それを取り込みました．グラフを見ても，ローカルの系統と，リモートの誰かの系統に分かれていましたが，PCが自動的に1つに合流させる変更をしたようです．


この状態でリモートにpushします．

```bash
$ git push
$ git log
*       commit  9740140fffaa9a0d5f793caa63e16cbef1b9edf7 (HEAD -> master,  origin/master)
|  \    Merge:  3be4208  b311fa3
|    |  Date:  Wed Apr 28 00:39:21  2021  +0900
|    |   
|    |        Merge branch 'master'  of ssh://..........
|    | 
*   |          commit  3be4208aee8aa6114c501fd5bb5b40f937ded8c0
|    |          Author: helmenov <kotaro1976@gmail.com>
|    |         Date:   Wed Apr 28 00:02:47 2021 +0900
|    |
|    |                         d03.py:  left -> right
|    |
|    *    commit  b311fa3126e44539c711861cb0819340e239530
|  /      Author:   Nobunaga Oda <nobunaga@cis.nagasaki-u.ac.jp>
|         Date:   .....
|
|                 ちょっと変えるね
|
* commit  6a4e1e35b83fa702b7eb1b8ebd7dd373ad79d086 
|
...
```

うまく行きました．

## 今日の課題

1. 自分のノートパソコン上の演習2用のディレクトリをgit対応にして，ローカルレポジトリを作り，現在の状態をcommitせよ．
   
   `2021psp2`ディレクトリの下には，day01とday02というディレクトリがあり，それぞれのディレクトリの下に，ソースコードとレポートのファイルがあるはずである．
   `2021psp2`ディレクトリのすぐ下の位置で，`git init`して，すべてのファイルを`git add`で管理対象にせよ．また，`git commit -m "最初のコミット"`などとコメントを残せ．

2. 先週作成したメソッド・関数を使い，マウスクリックした方向を向かせて，その方向にクリックした座標と亀の座標との距離を半分に縮めるよう前進させる，というのを繰り返すプログラムを作成し，`d03.py` とせよ．
3. `d03.py` も `add` して `commit` せよ
4. 演習室のコンピュータにリモートログインし，リモートレポジトリを作成せよ．ローカルレポジトリをリモートレポジトリにバックアップせよ．

