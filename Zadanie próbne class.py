# https://pl.spoj.com/problems/PTEST/
    
class działanie:
    def __init__(self):
        self.a = int(input())
        self.b = int(input())
    def sumowanie(self):
        return self.a + self.b
d = działanie()
print(d.sumowanie())