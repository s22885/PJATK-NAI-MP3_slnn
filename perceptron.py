import math
from random import random


class Perceptron:
    name: str
    w: list
    t: float
    alfa_l: float

    def __init__(self, name: str, alfa_l=0.01, list_d: list = []):
        self.name = name
        self.alfa_l = alfa_l
        if len(list_d) != 0:
            self.w = list_d[0:- 1]
            self.t = list_d[-1]
        else:
            self.w = []
            self.t = random()
            for i in range(26):
                self.w.append(random())

    def calc_net(self, list_x: list):
        res = 0.0
        for i in range(len(list_x)):
            res += list_x[i] * self.w[i]
        res -= self.t
        return res

    def learn(self, list_x: list, name: str):
        d = 1 if self.calc_net(list_x) >= 0 else 0
        y = 1 if self.name == name else 0
        for i in range(len(self.w)):
            self.w[i] = calc_w(self.w[i], list_x[i], self.alfa_l, y, d)
        self.t = calc_w(self.t, -1, self.alfa_l, y, d)

    def test(self, list_x: list):
        # d = sigmoid_fun(self.calc_net(list_x))
        # return self.name + " = " + str((d * 100).__round__(3)) + "%"
        res = []
        res.append(self.name)
        res.append(sigmoid_fun(self.calc_net(list_x)))
        return res

    def normalize_me(self):
        self.w = normalization(self.w)


def calc_w(w, x, alfa, y, d):
    return w + (y - d) * alfa * x


def sigmoid_fun(net: float):
    tmpx = math.pow((1 + math.exp(-net)), -1)
    return tmpx


def normalization(list_i: list):
    tmp = 0.0
    for i in list_i:
        tmp += math.pow(i, 2)
    tmp = math.sqrt(tmp)
    for i in range(len(list_i)):
        list_i[i] = list_i[i] / tmp
    return list_i
