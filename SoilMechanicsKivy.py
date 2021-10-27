from matplotlib import pyplot as plt
import numpy as np
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class LLWindow(Screen):

    def plotButtonfunc(self):
        nob1 = int(self.ids.nob1input.text)
        nob2 = int(self.ids.nob2input.text)
        nob3 = int(self.ids.nob3input.text)
        nob4 = int(self.ids.nob4input.text)
        mc1 = float(self.ids.mc1input.text)
        mc2 = float(self.ids.mc2input.text)
        mc3 = float(self.ids.mc3input.text)
        mc4 = float(self.ids.mc4input.text)

        dt = np.array([
            [nob1, mc1],
            [nob2, mc2],
            [nob3, mc3],
            [nob4, mc4]
        ])
        x = dt[:, 0]
        y = dt[:, 1]

        theta = np.polyfit(x, y, 1)

        y_line = theta[1] + theta[0] * x
        plt.scatter(x, y)
        val = theta[1] + theta[0] * 25
        plt.scatter(25, val)
        plt.plot(x, y_line, 'r')
        plt.title('Best fit line')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        self.ids.lllabel.text = str(val)
        self.ids.nob1input.text = ''
        self.ids.nob2input.text = ''
        self.ids.nob3input.text = ''
        self.ids.nob4input.text = ''
        self.ids.mc1input.text = ''
        self.ids.mc2input.text = ''
        self.ids.mc3input.text = ''
        self.ids.mc4input.text = ''
        plt.show()


class SCSWindow(Screen):


    def onButton(self):


        if self.ids.gpercinput.text == '':
            gp = 0
        else:
            gp = int(self.ids.gpercinput.text)

        if self.ids.spercinput.text == '':
            sp = 0
        else:
            sp = int(self.ids.spercinput.text)

        if self.ids.fpercinput.text == '':
            fp = 0
        else:
            fp = int(self.ids.fpercinput.text)

        if self.ids.llinput.text == '':
            ll = 0
        else:
            ll = float(self.ids.llinput.text)

        if self.ids.piinput.text == '':
            pi = 0
        else:
            pi = float(self.ids.piinput.text)

        if self.ids.d10input.text == '':
            d10 = 0
        else:
            d10 = float(self.ids.d10input.text)

        if self.ids.d30input.text == '':
            d30 = 0
        else:
            d30 = float(self.ids.d30input.text)

        if self.ids.d60input.text == '':
            d60 = 0
        else:
            d60 = float(self.ids.d60input.text)

        if d10 == 0 or d60 == 0 or d30 == 0:
            cu = 0
            cc = 0
        else:
            cu = d60 / d10
            cc = (d30 ** 2) / (d60 * d10)

        if gp > sp and gp > fp:

            if 0 <= fp <= 5:
                if cu > 4.0 and 1.0 < cc < 3.0:
                    self.ids.resultlabel.text = 'GW'

                else:
                    self.ids.resultlabel.text = 'GP'

            elif fp >= 12:
                if (ll - 20) * 0.73 > pi or pi < 4:
                    self.ids.resultlabel.text = 'GM'

                elif (ll - 20) * 0.73 < pi and pi > 7:
                    self.ids.resultlabel.text = 'GC'


        if sp > gp and sp > fp:
            if 0 <= fp <= 5:
                if cu > 6 and 1 < cc < 3:
                    self.ids.resultlabel.text = 'SW'

                else:
                    self.ids.resultlabel.text = 'SP'

            elif fp >= 12:
                if (ll - 20) * 0.73 > pi or pi < 4:
                    self.ids.resultlabel.text = 'SM'

                elif (ll - 20) * 0.73 < pi and pi > 7:
                    self.ids.resultlabel.text = 'SC'


        if fp > gp and fp > sp:

            if (ll - 20) * 0.73 < pi:

                if ll < 50:
                    self.ids.resultlabel.text = 'CL/OL'

                elif ll > 50:
                    self.ids.resultlabel.text = 'CH/OH'


            elif (ll - 20) * 0.73 > pi:

                if ll < 50:
                    self.ids.resultlabel.text = 'ML/OL'

                elif ll > 50:
                    self.ids.resultlabel.text = 'MH/OH'



class WindowManager(ScreenManager):
    pass


kv1 = Builder.load_file('SoilMechanics.kv')



class SoilApp(App):


    def build(self):
        return kv1


if __name__=='__main__':
    SoilApp().run()