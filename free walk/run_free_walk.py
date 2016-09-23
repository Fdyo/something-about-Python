__author__ = 'Fdyo'
#coding: utf-8
import matplotlib.pyplot as plt
from free_walk import Free_walk
while True:
    fw = Free_walk()
    fw.start_walk()
    fw.steps = 10000
    continue_fw = raw_input('Continue or not?')
    if continue_fw == 'n' :
        break
    plt.scatter(fw.x_label, fw.y_label, c=fw.x_label, cmap=plt.cm.jet, edgecolors='none', s=14)

plt.show()