import random
from tkinter import *

import data_loader
import percept_struc
import str_carve

root = Tk()
root.title("Test")
root.geometry("400x400")


class Elder:
    ai = 1
    passed: bool

    def __init__(self, master):
        self.passed = False
        my_frame = Frame(master)
        my_frame.pack()
        self.button_new_ai = Button(master, text="create new ai", command=self.new_ai)
        self.button_new_ai.pack()
        self.button_clear = Button(master, text="clear board", command=self.clear_board)
        self.button_clear.pack()
        self.button_training = Button(master, text="trenuj razy", command=self.loader)
        self.button_training.pack()
        self.button_compare = Button(master, text="find lang", command=self.compare)
        self.button_compare.pack()
        self.promp_win = Text(root, height=200, width=200)
        self.promp_win.pack()

    def compare(self):
        if self.passed:
            var = self.get_prompt()
            res_data = self.ai.test(str_carve.count_chars(var))
            res = res_data[0]
            for i in range(1, len(res_data)):
                tmp_val = res_data[i]
                if res[1] < tmp_val[1]:
                    res = res_data[i]
            self.clear_board()
            self.say_board("wybrany jezyk to " + res[0])
        else:
            self.clear_board()
            self.say_board("proszę stworzyć ai")

    def loader(self):
        if self.passed:
            try:
                var = int(self.get_prompt())
                if 100 >= var > 0:
                    for x in range(100):
                        self.ai.normalize_me()
                        listss = data_loader.get_file_names(data_loader.get_langs())
                        random.shuffle(listss)
                        for i in listss:
                            tmp_file = open(i[1], encoding="utf-8")
                            tmp_file_string = tmp_file.read()
                            self.ai.training(str_carve.count_chars(tmp_file_string), i[0])
                            tmp_file.close()
                else:
                    self.clear_board()
                    self.say_board("błąd minimum 1 max 100")
            except ValueError:
                self.clear_board()
                self.say_board("błąd parsowania prosze wprowadzić ile razy mamy uczyć")
        else:
            self.clear_board()
            self.say_board("proszę stworzyć ai")

    def new_ai(self):
        var = self.get_prompt()
        try:
            alfa = float(var)
            self.ai = percept_struc.PerceptStruct(alfa)
            for langs in data_loader.get_langs():
                self.ai.add_perceptron(langs)
            self.passed = True
            self.clear_board()
            self.say_board("nowe ai stworzone")
        except ValueError:
            self.clear_board()
            self.say_board("błąd parsowania")

    def get_prompt(self):
        return self.promp_win.get("1.0", "end-1c")

    def clear_board(self):
        self.promp_win.delete(1.0, "end")

    def say_board(self, text_s):
        self.promp_win.insert(1.0, text_s)


e = Elder(root)

root.mainloop()

