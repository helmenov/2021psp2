# 株ゲーム

ここに，5つの上場会社の毎日の株価額（始値，終値，最高値，最低値，in [JPY]）および取引量（in [JPY]）のデータがある．

今，あなたは100万円を持っていて，この5つの会社の株を買ったり売ったりして，30日後の「日本円の所持金を」できるだけ高くしたい（つまり儲けたい）．そのときの株を多く持っていたとしても数えません．

株で儲ける原理は，取引値 1株あたりx円で，p株買い，それを取引値 1株あたりy円で，q株売れば，qy-px 円儲かるという原理です．（手数料は無料とする）

ただし，買いたくても売る人がいなければ買えないわけで（逆もある），後日に株価の動きを見ると，最低値と最高値の間を，始値から始まって，ランダムに動き，終値で終わっているわけです．

ゲームのしかたは，

1. 1日目は取引しない．個数は現在 `j[0]=1000000, a[0]=b[0]=c[0]=d[0]=e[0]=0` である．
2. 2日目の朝以降は，前日までの株価の情報をすべて入手する．`A[0] = {end:200, min:50, max:250}, A[1] = {end:300, min:150, max:350}, ...`
3. 朝，取引したい株価値と株数（買う場合は正，売る場合は負）を登録 `xa, pa, , xb, pb, xc, pc, xd, pd, xe, pe` 
4. 昼，株価が動き始める．基本的に，最低値と最高値の間の値を一様分布する乱数で動くが，最初は始値(前日の終値)，最後は終値とする．ユーザは動きを知らされない．`na = runif(A[n-1]['end'], A[n]['end'])`
5. 取引したい株価値と同じ値の出現数だけ，取引が行われる．1日に会社ごとに1度の取引だけできる．実際の取引株数を`pp*`とすると，`j[n+1] = j[n] - sum(x*pp), a[n+1] = a[n] + xa*ppa, b[n+1]=b[n] + xb*ppb, ...`
6. 1日の終わりに取引できなかった登録は，すべて取り消される．10株買う予定で実際は7株だけ買えたのなら，所持金は7株分減って，所持株が7株増えるだけ．

取引したい株価値`x*`と株数`p*`をどのように決めるか，それが問題である．

## 処理

```py
def whole_torihiki(begin, end, min, max, quant):
    torihiki = runif(min,end,quant-2)
    torihiki.prepend(begin)
    torihiki.append(end)
    return torihiki


# すべてのデータ
A = pd.DataFrame({'end':[200,300,...], 'min':[50, 150,...], 'max':[250, 350, ...]})
B = ...

# 取引実行
def torihiki(n,j,a,b,c,d,e,xa,pa,xb,pb,xc,pc,xd,pd,xe,pe):
        wA = whole_torihiki(A.end[n-1],A.end[n],A.min[n],A.max[n])
        ppa = hist(wA)[xa]
        ppa = abs(pa) > ppa : abs(pa) : ppa
        if a + sign(pa)*ppa < 0:
            ppa = a
    
        wB = whole_torihiki(B.end[n-1],B.end[n],B.min[n],B.max[n])
        ppb = hist(wB)[xb]
        ppb = abs(pb) > ppb : abs(pb) : ppb
        if b + sign(pb)*ppb < 0:
            ppb = b
        ...

        j = j - sign(pa)*ppa*xa - sign(pb)*ppb*xb - sign(pc)*ppc*xc - sign(pd)*ppd*xd - sign(pe)*ppe*xe
        a = a + sign(pa)*ppa
        b = b + sign(pb)*ppb
        ...

        return j,a,b,c,d,e


# 所持の初期値
j[0] = 1000000
a[0]=b[0]=c[0]=d[0]=e[0]=0

for n in range(1,31):

    xa = 
    pa = 
    xb = 
    pb =
    ...

    j[n+1], a[n+1], b[n+1], c[n+1], d[n+1], e[n+1] = torihiki(n,j[n],a[n],b[n],c[n],d[n],e[n], xa,pa, xb,pb, xc,pc, xd,pd, xe,pe)

    
print(j[30])
```




