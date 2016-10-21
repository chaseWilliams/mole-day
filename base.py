import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X = pd.read_csv('./data.csv')
molar_mass_data = X.iloc[:, [0, 3]].values
X = X.values

def grab_data(name):
    return X[[np.where(X == name)[0]], :][0]

def average_molar_mass(groups):
    arr = [None] * len(groups)
    for index, elem in enumerate(groups):
        arr[index] = np.mean(elem[:, 3])
    return arr

metals = grab_data('metal')
non_metals = grab_data('nonmetal')
noble_gas = grab_data('noble gas')
alkalis = grab_data('alkali metal')
alkali_earths = grab_data('alkaline earth metal')
metalloids = grab_data('metalloid')
halogens = grab_data('halogen')
transition_metals = grab_data('transition metal')
lanthanoids = grab_data('lanthanoid')
actinoids = grab_data('actinoid')

plt.scatter(molar_mass_data[:, 0], molar_mass_data[:, 1], c='r', marker='o')
plt.xlabel('Atomic Number')
plt.ylabel('Molar Mass')
plt.title('The Increase of Molar Mass with Atomic Number')
plt.show()

# The slices will be ordered and plotted counter-clockwise.
labels = 'Metals', 'Nonmetals', 'Noble Gases', 'Alkali Metals', 'Alkali Earth Metals', 'Metalloids', 'Halogens', 'Transition Metals', 'Lanthanoids', 'Actinoids'
sizes = [
    metals.shape[0],
    non_metals.shape[0],
    noble_gas.shape[0],
    alkalis.shape[0],
    alkali_earths.shape[0],
    metalloids.shape[0],
    halogens.shape[0],
    transition_metals.shape[0],
    lanthanoids.shape[0],
    actinoids.shape[0]
]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'blue', 'orange', 'green', 'yellow', 'pink', 'purple']

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
#plt.title('Distribution of Periodic Table Groups')
plt.show()

averages = average_molar_mass([metals, non_metals, noble_gas, alkalis, alkali_earths, metalloids, halogens, transition_metals, lanthanoids, actinoids])
y_pos = np.arange(len(averages))

plt.barh(y_pos, averages, align='center', alpha=0.4)
plt.yticks(y_pos, labels)
plt.xlabel('Average Molar Mass')
plt.title('Average Molar Mass of the Periodic Table Groups')

plt.show()