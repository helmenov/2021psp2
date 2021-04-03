# The coordinates of points A,B,C, and D are randomly generated.
import random
# A
ax=round(random.random(),2)
ay=round(random.random(),2)
# B
bx=round(random.random(),2)
by=round(random.random(),2)
# C
cx=round(random.random(),2)
cy=round(random.random(),2)
# D
dx=round(random.random(),2)
dy=round(random.random(),2)

# Graph by matplotlib
# plt.plot((x1,x2,x3,...,xn),(y1,y2,y3,...,yn))    oresen graph
# plt.scatter((x1,x2,x3,...,xn),(y1,y2,y3,...,yn)) sanpuzu
import matplotlib.pyplot as plt
plt.plot((ax,bx),(ay,by))
plt.plot((cx,dx),(cy,dy))
plt.text(ax,ay,'('+str(ax)+','+str(ay)+')',fontsize=10)
plt.text(bx,by,'('+str(bx)+','+str(by)+')',fontsize=10)
plt.text(cx,cy,'('+str(cx)+','+str(cy)+')',fontsize=10)
plt.text(dx,dy,'('+str(dx)+','+str(dy)+')',fontsize=10)

plt.show()
# 問(i) plt.show()をコメントアウトし、
#       線分ABと線分CDが交わったらplt.savefig('majiwaru.png') を実行し、
#       交わらない場合は plt.savefig('majiwaranai.png') を実行する
#       プログラムを作成してください。



#====================================================
# 提出物
# 完成したプログラム b802.py
# majiwaru.png
# majiwaranai.png
#====================================================





