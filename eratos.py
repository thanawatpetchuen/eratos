from appJar import gui
import random
import time
import copy

class Eratos:
    def __init__(self):
        self.app = gui("Eranosthenes", "700x700")
        self.app.setSticky("news")
        self.app.setExpand("both")
        self.app.setFont(20)
        self.label_list = []
        self.lst = []
        self.clst = []
        self.primenum = []
        self.notprime = []
        self.click_count = 0
        self.num = 0
        self.colorlist = ["LightYellow", "LemonChiffon", "LightGoldenRodYellow", "PapayaWhip"
                          , "Moccasin", "PeachPuff", "PaleGoldenRod", "Khaki", "DarkKhaki"]
        # self.colorlist = ["LightYellow", "LemonChiffon", "LightGoldenRodYellow", "PapayaWhip"
        #                   , "Moccasin", "PeachPuff", "PaleGoldenRod", "Khaki", "DarkKhaki"]
        self.app.startSubWindow("era", "Prime Number")
        self.app.addLabel("Prime number",self.primenum)
        self.app.stopSubWindow()

    def lstint(self):
        self.num = self.messagebox()
        # print(self.num)
        for i in range(1, int(self.num)+1):
            self.lst.append(i)
        self.lst[0] = ''

        self.clst = copy.deepcopy(self.lst)

    def get_label(self):
        return self.label_list

    def add_button(self):
        self.app.showSubWindow("era")
        row = self.app.getRow()
        self.app.addButton("G", self.change_label, row, 0)
        self.app.addButton("R", self.clear_label, row, 1)
        self.app.addButton("P", self.prnum, row, 2)
        self.app.addButton("A", self.auto, row, 3)
        self.app.addLabel("cc", self.click_count, row, 4)


    def add_label(self):
        for r in range(0, self.num//10):
            for c in range(0, 10):
                try:
                    if(r>=1):
                        self.app.addLabel("l{}{}".format(r, c), self.lst[(r*10)+c], r, c)
                        self.label_list.append(['l{}{}'.format(r, c), self.lst[(r*10)+c]])
                    else:
                        self.app.addLabel("l{}{}".format(r, c), self.lst[(r*8)+c], r, c)
                        self.label_list.append(['l{}{}'.format(r, c), self.lst[(r*8)+c]])

                except IndexError:
                    pass

    def app_go(self):
        self.app.go()

    def click_counts(self, btn):
        print(self.click_count)

    def prnum(self, btn):
        self.app.infoBox("Prime Number", [self.primenum])
        return self.primenum

    def change_label(self, btn=None):
            self.click_count += 1
            # if(self.click_count > 60):
            #     self.set_prime()
            sel_color = random.choice(self.colorlist)
            self.app.setLabel("cc", self.click_count)

            for i in self.label_list:
                start = time.time()
                try:
                    if self.click_count == 1:
                        self.app.setLabelBg("l00", "Orange")

                    # if int(i[1]) % self.click_count != 0 and int(i[1]) == self.click_count:
                    #     self.app.setLabelBg(i[0], "Yellow")

                    elif int(i[1]) % self.click_count == 0 and int(i[1]) != self.click_count:
                        # del self.clst[self.clst.index(i[1])]
                        self.app.setLabelBg(i[0], sel_color)
                        self.notprime.append(i[1])
                        print("Label changed!")
                        # self.app.update()
                        stop = time.time()
                        # print(stop - start)
                    else:
                        print("------{}------".format(self.click_count))
                        if(i[1] not in self.notprime):
                            self.primenum.append(i[1])
                        # time.sleep(0.01)
                except ValueError:
                    pass



        # print("Changed Label: Button {} pressed".format(btn))
        # self.app.setLabelBg("l01", "LightYellow")
        # self.app.after(1000, self.change_label)

    def clear_label(self, btn):
        print("Changed Label: Button {} pressed".format(btn))
        for i in self.label_list:
            self.app.setLabelBg(i[0], "Skyblue")
        self.click_count = 0

    def set_prime(self):
        for i in self.label_list:
                for n in range(1, 120):
                    try:
                        if int(i[1]) % n != 0:
                            self.app.setLabelBg(i[0], "Green")
                    except ValueError:
                        pass

    def auto(self,btn):
        self.click_count = 0
        for i in range((len(self.label_list)//2)):
            self.change_label()

        print(self.primenum)
        # print(self.notprime)

    def messagebox(self):
        self.app.setSticky("new")
        self.app.setExpand("both")
        self.num = self.app.numberBox("EraTosThenes", "Input a number")
        return self.num

if __name__ == '__main__':
    eranos = Eratos()
    # eranos.app.go()
    # eranos.messagebox()
    eranos.lstint()
    eranos.add_label()
    # print(eranos.get_label())
    eranos.add_button()
    eranos.app_go()
    # eranos.app.after(1000, eranos.change_label())
    # eranos.app_go()
