import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

takimlar = ['Sporting Lizbon','Manchester United','Real Madrid','Juventus','El-Nasr']

gol_sayisi = [0,105,311,81,14]

plt.pie(gol_sayisi,labels=takimlar,shadow=True,explode=(0.1,0.1,0.1,0.1,0.1), autopct='%1.1f%%',)
plt.title('C.Ronaldo nun Takımlara Göre Attığı Goller \nS.P=0, M.U=105, R.M=311, Juve=81, El-Nasr=14')

plt.show()