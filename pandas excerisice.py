import pandas as pd
import numpy as np


#First we declare the elements of the colums
data = {'list' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'name': ['Nadia', 'Neguib', 'Pedro', 'Sebastian', 'Ivan', 'Ivan','Johan', 'Aaron', 'Pavia', 'Sara'],
        'score': [10, 9.0, 8.0, 7.5, 6.0, 10, 10, 7.5, 8.8, 9.5],
        'approved' : ['yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes']}

#Then put the labels of th raws
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#Finally we print the table and organized the data
tabla = pd.DataFrame(data, index = labels)
print(tabla)