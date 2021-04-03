﻿#==============================================================================
# 問(i)  input() を利用してメモを変数 memo に保存するプログラムを作成してください。

#==============================================================================
# 問(ii) 以下のプログラムを編集して、現在の日時を以下のフォーマットに従った文字列として
#       変数 time に格納するプログラムを作成してください。
#        2020/10/25\t14:26\t
#      　\t はタブを表します。秒以下は不要です。
import datetime
d = datetime.datetime.now() 


#==============================================================================
# 問(iii) 2020年10月25日 14時26分　保存したメモ内容
#         という形式でprint文で出力するプログラムを作成してください。

#==============================================================================
# 問(iv) コマンドプロンプトで以下の命令を3回実行してください。
#        python a502.py >> memo.txt
#        >> memo.txt はmemo.txt の内容に新たに出力を追記するリダイレクト機能です。
#        もし memo.txt が存在しない場合には、> memo.txt と同じ動きをします。
#        （memo.txt を作成して、出力結果をmemo.txt に保存する。）
#        入力するメモの内容は英数字
# 期待される memo.txt の内容の例
# 2020/10/25         14:26         a
# 2020/10/25         14:26         bb
# 2020/10/25         14:27         ccc
# 完成した a502.py と出力ファイル memo.txt を提出してください。
