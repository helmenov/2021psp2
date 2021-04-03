# while ループはwhileの継続判定式がTrueの場合にブロックを実行し、Falseの場合は終了します。
# ＜書式＞
# while 継続判定式:
#   処理ブロック

# 例, 10,9,...,3,2,1 とカウントダウンします。
print('while countdown example')
i=10
while i>0:
    print(i)
    i-=1
# forループはリストやタプル、range などのiterable なオブジェクトの全ての要素について
# ブロックを実行します。

# 例、先のカウントダウンをforループで実装します。
print('for countdown example')
for i in range(10,0,-1):
    print(i)


# for や while は入れ子にして使うことができます。
for i in range(5):
    for j in range(10):
        print('*',end='') # 改行なしで'*' を表示
    print()

# break文は実行するとループ処理を終了します。
# 例
# xが3の時breakする
print('break example')
for x in range(5):
    if x == 3:
        break
    print(x)
# continue文は実行するとその回のブロック処理を終了して、次のループのブロック処理を行います。
# 例
# xが3の時continueする
print('continue example')
for x in range(5):
    if x == 3:
        continue
    print(x)
    
#問(iv) n=5のとき図１、n=10のとき図２のような模様を表示するプログラムを作成してください。
#       nの値は変えられるようにしてください。
#       
# *****
# ****
# ***
# **
# *
# 図１　n=5 のケース
# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *
# 図２ n=10 のケース
# プログラムは n=4 のときで出力してください。
