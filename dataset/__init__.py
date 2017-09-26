import random
import numpy


def make_random_function():
    lambdas = ['identity', 'inc', 'dec', '+2', '-2', 'double', 'half', 'zero']
    m = 1 + random.randrange(4)
    return random.sample(lambdas * 10, m)


def eval_function(f, x):
    for u in f:
        if u == 'identity':
            x = x
        elif u == 'inc':
            x = x + 1
        elif u == 'dec':
            x = x - 1
        elif u == '+2':
            x = x + 2
        elif u == '-2':
            x = x - 2
        elif u == 'double':
            x = x * 2
        elif u == 'half':
            x = x / 2.0
        elif u == 'zero':
            x = 0
    return x


def x_samples(batch_size):
    return random.sample([i * 0.5 for i in range(-20, 20)] * batch_size, batch_size)


def make_data(m):
    f = make_random_function()
    xs = x_samples(m)
    ys = [eval_function(f, x) for x in xs]
    X = numpy.array(xs, dtype='f')
    Y = numpy.array(ys, dtype='f')
    return X, Y


def generator(batch_size, m=10):
    while True:
        batch_X = []
        batch_Y = []
        for _ in range(batch_size):
            X, Y = make_data(m)
            batch_X.append(X)
            batch_Y.append(Y)
        batch_X = numpy.array(batch_X)
        batch_Y = numpy.array(batch_Y)
        yield batch_X, batch_Y


def load(batch_size, m):
    return generator(batch_size, m)
