# リスト(list) は複数の値をひとまとめにします。
# リストリテラルは[]で囲い、値を列挙し、値と値の間はカンマで区切ります。
x=[1,2,3,4,5] # 値 1と2と3からなるリスト。
y=[1.0,3.14,1.414,1,'apple'] # 値 1.0, 3.14, 1.414, 1, 'apple' からなるリスト。型が違うものがあっても良い。
print('x=',x)
print('y=',y)
# リストは文字列と同様にindex指定することで要素を参照できます。
# index は0スタートです。負のindexは逆順となるのも文字列の場合と同じです。
# indexで指定したところに要素がないとIndexErrorの例外が発生するのも同じです。
print('x[0]=',x[0])
print('x[1]=',x[1])
print('x[2]=',x[2])
print('x[3]=',x[3])
print('x[4]=',x[4])
print('x[5] is accessable?',end=' ')
try:
    x[5]
    print('YES')
except IndexError:
    print('NO')
print('x[-1]=',x[-1])
print('x[-2]=',x[-2])
print('x[-3]=',x[-3])
print('x[-4]=',x[-4])
print('x[-5]=',x[-5])
print('x[-6] is accessable?',end=' ')
try:
    x[-6]
    print('YES')
except IndexError:
    print('NO')
# リストはリストオブジェクトのidを変えずに要素を書き換えることができます。
# この性質をmutableといいました。
print('y=',y)
y[4]=-10
print('y=',y)
# リストは文字列と同様にスライス指定することで部分リストを参照できます。
print('x[3:]=',x[3:])
print('x[::-1]=',x[::-1])
print('x[1:4]=',x[1:4])
# len()関数を使うとそのリストの要素の数がわかります。
print('len(x)=',len(x))
print('len(x[1:4])=',len(x[1:4]))
# 要素が0個のリストを空リストと呼びます。
# 空リストは[] もしくは list() で作成できます。
print('[]=',[],',len([])=',len([]))
print('list()=',list(),',len(list())=',len(list()))
# [1,2,3,4,5] のように少ない要素数のリストは手入力でも十分処理できますが、
# [1,2,....,10000] のようなリストを手入力するのは非常に大変です。
# こんなときには range() 関数を利用します。
# ただ range() で作成したものは range オブジェクトとしてしか見えませんので、
# 可視化するためにはlist()関数に通してリストに変換してから見る必要があります。
print('range(100)=',range(100))
print('list(range(100))=',list(range(100)))
# なお、range()関数は、省略なしに引数を指定すると range(start,end,step) の形になります。
# range(100) のように引数を一つだけ指定したときは range(0,100,1) と指定したものとして
# みなされます。また range(15,76) のように２つ指定したときは range(15,76,1) を指定
# したものとしてみなされます。start は始めのindexを表し、endは終わりのindexの次のindexを表します。
# step はstepの幅で要素を生成します。
print('list(range(15,76))=',list(range(15,76)))
print('list(range(15,76,4))=',list(range(15,76,4)))
print('list(range(76,15,-1))=',list(range(76,15,-1)))
print('list(range(76,15,-4))=',list(range(76,15,-4)))
print('len(range(76,15,-4))=',len(range(76,15,-4)))
# リストに似たコンテナ型としてタプル(tuple,組)があります。
# タプルのリテラルは()で囲います。それ以外はリストと同じです。
# タプルはイミュータブルです。オブジェクト（データ）の書き換えができません。
# 変数名の付け替えはオブジェクトの変更ではないため可能です。

w=(1,2,3,4,5)
print('w[0]=5 is availale?',end=' ')
try:
    w[0]=5
    print('YES')
except TypeError:
    print('NO')

# 空タプルは tuple() または () で表します。
print('tuple()=',tuple(),',len(tuple())=',len(tuple()),',len(())=',len(()))

# １つだけの要素を持つリストは [100] のようにかけますが、タプルの場合は (100) だと
# 数式の(100) と間違える恐れがあるため、(100,) とカンマを明記する必要があります。
print('len((100,))=',len((100,)),',type((100,))=',type((100,)))

# リストやrangeをtuple型に型変換するには tuple()関数を使ってください。
print('tuple([1,2,3,4,5,6])=',tuple([1,2,3,4,5,6]))
print('tuple(range(3,10,2))=',tuple(range(3,10,2)))

# リストとタプルとrangeはどれも順番があるのでシーケンシャル sequential なコンテナ型と分類されます。

# リスト同士の和や整数との掛け算は文字列のと同様に働きます。タプルも同様です。
# ですが、異なるタイプ型の連結はできません。
print('[1,2,3]+[1,1]=',[1,2,3]+[1,1])
print('(1,2,3)+(1,)=',(1,2,3)+(1,))
print('[1,2,3]+(1,1) is available?',end=' ')
try:
    [1,2,3]+(1,1)
    print('YES')
except TypeError:
    print('NO')

# reversed() 関数の引数にリストやタプルを入れるとその要素を逆順にした
# reversed object を生成します。
# さらにそれに型変換することで、逆順のリストや逆順のタプルを得ることができます。
print('list(reversed([1,2,3]))=',list(reversed([1,2,3])))
#=========================================================================
# 問(i) -100 から 99までの数のうち5の倍数を値の小さい順に並べたリストを作成して表示してください。
# 問(ii) 1 から 200 までの数のうち 7の倍数を値の大きい順に並べたタプルを作成してください。
# 問(iii）問(ii) で作成したタプルの長さ（要素の数）を求めるプログラムを作成してください。

