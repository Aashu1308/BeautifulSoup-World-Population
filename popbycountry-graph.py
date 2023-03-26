from matplotlib import pyplot as plt
import pandas as pd
#import matplotlib.patches
#import numpy as np


data = pd.read_csv("web-test/popbycountry-converted.csv")
population = data['Population(2020)']
country = data['Country (or dependency)']

plt.style.use("ggplot")
plt.title("World Population")
plt.gca().axis("equal")
pie = plt.pie(population, startangle=0,
              wedgeprops={'linewidth': 0.5, "edgecolor": "k"})


plt.legend(country, bbox_to_anchor=(1, 1.025), loc="upper left")
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
plt.show()


'''fig = plt.figure(4, figsize=(7, 7))
ax = fig.add_subplot(211)
ax.set_title("World Population")
pie = ax.pie(population, startangle=0)

ax2 = fig.add_subplot(212)
ax2.axis("off")
ax2.legend(pie[0], country, title='COUNTRIES',
           loc='center')'''

'''handles = []
for i, l in enumerate(country):
    handles.append(matplotlib.patches.Patch(
        label=l))
for i in range(len(handles)):
    handles[i].set_facecolor(cmap[i])'''

'''def get_cmap(n):
    c = [np.random.rand(3,) for i in range(n)]
    return c'''
