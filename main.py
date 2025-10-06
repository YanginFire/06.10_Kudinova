from sympy import *

# Вариант 8 -> Меняем данные на данные варианта 3 -> меняем данные на данные 5 варианта

# 1 способ
k, T, C, L = symbols('k T C L')

C_ost = 20000
Am_lst = []
C_ost_lst = []

for i in range(6):
  Am = (C - L) / T
  C_ost -= Am.subs({C: 20000, T: 6, L: 0})
  Am_lst.append(round(Am.subs({C: 20000, T: 6, L: 0}), 2))
  C_ost_lst.append(round(C_ost, 2))

print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

# 2 Способ
Aj = 0
C_ost = 20000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(6):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 20000, k: 2, T: 6})
  Am_lst_2.append(round(Am.subs({C: 20000, k: 2, T: 6}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

# Контейнер табличного вывода
import pandas as pd

Y = range(1, 7)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])

print(tfame)
print(tfame2)

# Контейнер визуализации

from matplotlib import pyplot as plt

# Line chart
plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
plt.show()

# Pie chart
vals = Am_lst_2
labels = list(range(1, 6))
explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       explode=explode,
       autopct='%1.1f%%',
       shadow=True,
       rotatelabels=True,
       wedgeprops={
           'edgecolor': 'k',
           'lw': 1,
           'ls': '--'
       })
ax.axis('equal')
ax.set_title('Круговая диаграмма', fontsize=14, pad=20)
plt.show()

# Bar chart
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])

plt.bar(tfame['Y'], tfame['Am_lst'])
plt.show()

plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.show()
