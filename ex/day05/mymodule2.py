## mymodule2.py ##
class Dog():
    def __init__(self, val):
        """
        コンストラクタ (constructor)
        x = Dog(n)
        xに犬番号nを割り当てる．
        """
        self.value = int(val)
    
    def __add__(self, arg):
        """
        予約メソッド (reserved method)
        Dog型のxに対する x + y は 整数の加算を返却
        """
        return self.value + int(arg)

    def bow(self, arg):
        """
        自作メソッド Dog.bow(n)
        - n回吠える

        Input
        - n (int) : 吠える回数
        
        Dog型であるxに対する x.bow(3) は
        Dog x : bowbowbow
        をプリントする．
        """
        cry = 'bow'*int(arg)
        print('dog', self.value, ':', cry)
