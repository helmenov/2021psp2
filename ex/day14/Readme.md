# day14(option): C言語プログラミング

これまで、Pythonの演習をおこなってきた。以下のようなpython言語の文法に沿ったソースコード`foo.py`があれば、

```py
import numpy as np

print(np.pi)
```

python はインタプリタであるから、コマンドライン（端末、ターミナル）から

```sh
$ python foo.py
3.141592653589793
$ 
```

によりアプリケーション実行がされる。

また、python terminalのなかで以下のようにfoo.pyの中身を一行ずつ実行できる。

```sh
$ python
>>> import numpy as np
>>> print(np.pi)
3.141592653589793
>>>
```

python言語がインタプリタであるのに対し、C言語はコンパイラ言語である。すなわち、以下のようなC言語の文法に沿ったソースコード `foo.c`があるとき、

```c
include <stdio.h>
include <stdlib.h>
include <math.h>

int main(void)
{
    printf("%f\n",M_PI);
    return EXIT_SUCCESS;
}
```

コマンドラインから、何らかのCコンパイラ（gccなど）

```sh
$ gcc foo.c -lm -o foo
```

というコンパイル、ビルド処理をおこなうことで、新たなファイル`foo`というアプリケーションが生成され、

```sh
$ foo
3.141592653589793
$
```

とアプリケーションを別途実行することになる。

## C言語とは

というわけで、C言語はPython言語よりアプリケーション生成が面倒である。ではなぜC言語を習得する必要があるのか？

それは、C言語があらゆる言語の基盤だからである。

実はこれまで実行してきた`python`というアプリケーションは、python言語の文法に沿ったソースコードを実行するコマンドであり、さまざまな言語から生成されたいろんな`python`が存在する。

コマンドラインから`python`を実行すると最初に、

```sh
$ python
Python 3.9.5 | packaged by conda-forge | (default, Jun 19 2021, 00:24:55)
[Clang 11.1.0 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

などのようにpython言語のバージョンと、どんな言語で作られたPythonなのかを表示している（上記の場合は macOSのCコンパイラであるClangで生成されたCPython）。

また、インタプリタは、アプリケーション実体を生成せずに、毎回一行一行をその場で動かす。
アプリケーション実体を生成し、次回からはその実体を起動したほうが直接的で実行速度が速い。
基本的に何万倍も速い。

つまり、C言語で作るほうが、より計算機を直接動かすことになる。

## C言語

python言語とC言語のソースコードを比べてみよう。ほぼ対応関係がある。

```sh
===python===                   | ===C===
                               | include <stdio.h>
                               | include <stdlib.h>
import numpy as np             | include <math.h>
                               |
                               | int main(void)
                               | {
                               |       int i;
                               |       double x;
                               |
print('hello world')           |       printf("hello world\n");
for i in range(10):            |       for(i=0;i<10;i++>){
    x[i] = np.cos(np.pi / 3)   |           x[i] = cos(i * M_PI / 3);
    print('x[',i,']:',x[i])    |           printf("x[%d] : %f\n", i, x[i]);
                               |       }
                               |
                               |       return EXIT_SUCCESS;
                               | }
```

pythonでモジュールの導入にimportを用いるが、C言語ではincludeである。

C言語にある`int func(int x, double y){...}`ブロックは、python言語では、`def func(x, y):`ブロックにあたる。
ただし、C言語では`int main(void){...}`が必ずあるが、python言語ではそれがない。

C言語では、変数の宣言が必要だが、python言語では不要。

for文の書き方が違う。if文も書き方が違う。

**そして、根本的に思想が違う。**　python言語ではライブラリが一般化していて豊富に揃っているため、積極的にPyPIのライブラリを使う。しかし、C言語では基本的に自分でライブラリを作ることが多い。



