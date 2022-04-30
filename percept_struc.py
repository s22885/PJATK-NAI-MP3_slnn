import perceptron


class PerceptStruct:
    perceptrons: list
    alfa: float

    def __init__(self, alfa=0.01, perceptrons: list = []):
        self.alfa = alfa
        self.perceptrons = perceptrons

    def add_perceptron(self, name):
        a = False
        for i in self.perceptrons:
            if i.name == name:
                a = True
                break
        if a:
            return False
        else:
            self.perceptrons.append(perceptron.Perceptron(name, self.alfa))
            return True

    def training(self, list_x: list, name: str):
        list_x = perceptron.normalization(list_x)
        for percep in self.perceptrons:
            percep.learn(list_x, name)

    def test(self, list_x: list):
        res = []
        list_x = perceptron.normalization(list_x)
        for percep in self.perceptrons:
            res.append(percep.test(list_x))
        return res

    def normalize_me(self):
        for i in self.perceptrons:
            i.normalize_me()
