def f(*args, **kwargs):
    print('Named: ', kwargs)

f(galleos=100, scikles=20, knuts=10)


'''
def total(Galleons, Sickles, Knuts):
    return (Galleons * 17 + Sickles) * 29 + Knuts

#coins = [110, 20, 30]
coins = {'Galleons':120, 'Sickles':10, 'Knuts':5}

print(total(**coins), 'Knuts!')
'''