def miaFunc(*argv):
    for arg in argv:
        print(arg)


miaFunc('pippo','paperino','pluto','gennaro')


def chiaveValore(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

chiaveValore(nome="Pippo", cognome="Pippone", sesso="neutro", city="london", price=1000)




