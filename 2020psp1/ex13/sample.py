'ファイル先頭コメント'

__author__="Hiroyuki Takada<htakada@nagasaki-u.ac.jp>"
__status__="production"
__version__="0.0.1"
__date__="18 January 2021"

DATA_TEST="variable"

class Test(object):
    '''
    クラス先頭コメント
    '''
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.__age=age
    def test(self):
        """
        メソッド先頭コメント
        """
        print(self.name)
        print(self.__age)

if __name__=='__main__':
    t=Test('Hiroyuki Takada',47);
    t.test()
    print(t.name)
    try:
        print(t.__age)
    except Exception as e:
        print('Error',e)
    print(t._Test__age)
