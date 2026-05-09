'''
def reels():
    r = ['1....100','101...200','201...300','301...400']
    for i in r:
        yield i

scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''

def reels():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
    
