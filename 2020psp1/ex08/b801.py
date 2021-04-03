# python スクリプトを中断したい場合、import sys を宣言しておいて、sys.exit() の
# 場所で中断ができます。
#
# input関数でうけつけた入力は全てstr型として受け付けられます。、
#
# 文字列型変数 x を int型やfloat型に変換するには x=int(x), x=float(x) という
# 命令を用います。
# ですが、入力によっては、変換できないことがあります。
# この場合は ValueError という例外が発生します。
#
# なお、例外処理は他の言語と異なりpythonはかなり高速に動作します。
# 書式を思い出してください。(プログラミング概論第7回目講義資料4ページ）
# try:
#   例外が発生しうる命令
# except 例外オブジェクト:
#   例外が起きたときの命令
#
# 例外を用いないで文字列がfloat型に変換できそうかどうかを判断するには、
# x.lstrip('-').replace('.','',1).isdigit()
# という式を用いて判定します。以下はこの方法を用いて判定した場合の処理です。
import sys
x= input('Please input a number for x.\n')
print(x,type(x))
if x.lstrip('-').replace('.','',1).isdigit():
    x=float(x)
else:
    print('Please input correctly.')
    sys.exit()
print(x,type(x))
# 問(i) x に関する処理と同等な処理を例外処理で実現してください。
y=input('Please input a number for y.\n')
print(y,type(y))
#----問(i) の解答欄--------------------------

#----解答欄ここまで---------------------------
print(y,type(y))

#===========================================
# 提出物
# 完成したプログラム b801.py
# 出力結果 b801.txt
#===========================================
