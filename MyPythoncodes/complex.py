class complex:
    def __init__(self,a,b):
        self.our_a=a
        self.our_b=b

    def __add__(self,c2):
        c3=complex(0,0)
        c3.a=self.our_a+c2.our_a
        c3.b=self.our_b+c2.our_b
        return c3


c1=complex(2,3)
c2=complex(2,-3)
c3=c1+c2
print(c3)
