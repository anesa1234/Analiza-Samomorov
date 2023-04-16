import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

ime_datoteke = "suicide.xlsx"


datoteka = ("C:\\Users\\evami\\OneDrive\\Dokumenti\\FAKS\\PROG2\\suicide.xlsx")


podatki = pd.read_excel(datoteka)
df = pd.DataFrame(podatki)  #data frame


leta = df.iloc[2:,9]    #[2:,9]
spoli = df.iloc[2:,12]
drzave = df.iloc[2:,7]
celine = df.iloc[2:,4]
st_100000 = df.iloc[2:,23]


# slovar, ki ima za vrednosti seznam posameznih vrednosti za svoj ključ

sl = {'Leta': [],
    'Spol': [],
    'Drzava': [],
    'Celina': [],
    'St_100k': []}

for leto in leta:
    sl['Leta'] += [int(leto)]

for spol  in spoli:
    sl['Spol'] += [spol]

for drzava in drzave:
    sl['Drzava'] += [drzava]

for celina in celine:
    sl['Celina'] += [celine]

for koef in st_100000:
    sl['St_100k'] += [koef]


Country = sl['Drzava'] #seznam držav po stolpcu
Koef = sl['St_100k'] #seznam koeficientov samomora po stolpcu
Year= sl['Leta'] #seznam letnic po stolpcu
Sex =sl['Spol'] #seznam spolov po stolpcu




#####################################################
# VSE TO JE ZA HISTOGRAM PO LETIH IN SPOLU
valid_inputs = sorted(set(Country))
while True:
    user_input = input("Izberi državo: ")

    if user_input in valid_inputs:
        print("Izbrali ste:", user_input)
        break  # Exit the loop when a valid option is chosen
    else:
        print("Neustrezna izbira. Izberite eno izmed podanih možnosti:", valid_inputs)
        # Loop will repeat and prompt the user againor

def Graph_suicide(user_input):
    "Graf prikaže koeficient samomorov (št. na 100 000 prebivalcev) po spolu glede za izbrano državo"

    # create a dictionary to group data by sex
    data = {'Male': {}, 'Female': {}}
    for year, sex, koef, country in zip(Year, Sex, Koef, Country):
        if country == user_input:
            if sex in data:
                if year not in data[sex]:
        
                    data[sex][year] = 0
                data[sex][year] += koef



    # create a figure and subplot
    fig, ax = plt.subplots()

    # set the width of the bars
    bar_width = 0.45


    # plot data for each sex
    for i, (sex, year_data) in enumerate(data.items()):
        # set the position of the bars
        x_pos = [j + i * bar_width for j in year_data.keys()]
        # plot the bars
        ax.bar(x_pos, year_data.values(), bar_width, label=f'{sex}')

    # set labels and title
    ax.set_xlabel('Letnica')
    ax.set_ylabel('Koeficient')
    ax.set_title(f'Suicides in {user_input}')

    # add legend
    ax.legend()





    xticks_labels = list(data['Male'].keys())
    ax.set_xticks(x_pos)
    ax.set_xticklabels(xticks_labels, rotation=60)

    # display the plot
    plt.show()

print(Graph_suicide(user_input))


##########################################################################

## zemljevid držav obarvanih glede na stopnjo samomorov

valid_inputs2 = sorted(set(Sex))
valid_inputs3 = sorted(set(Year))

while True:
    input_spol = input("Izberi spol: ")
    input_leto = int(input("Izberi leto: "))

    if input_spol in valid_inputs2 and input_leto in valid_inputs3:
        print("Izbrali ste:", input_spol, "in", input_leto)
        break  # Exit the loop when a valid option is chosen
    else:
        print(f"Neustrezna izbira. Izberite eno izmed podanih možnosti za spol:{valid_inputs2} in leto {valid_inputs3}")
        # Loop will repeat and prompt the user againor

def suicide_map(input_spol, input_leto):
    "Zemljevid števila samomorov v svetu."


    Dict_of_Countries = {}
    for year, sex, koef, country  in zip(Year,Sex, Koef, Country):
        
        if sex == input_spol and year== input_leto:
            Dict_of_Countries.update({country: koef })
            


    # Load the world map data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Merge the koef values with the world map
    world = world.merge(
        pd.DataFrame.from_dict(Dict_of_Countries, orient='index', columns=['koef']),
        left_on='name',
        right_index=True
    )

    # Plot the world map
    fig, ax = plt.subplots(figsize=(12,6))
    world.plot(column='koef', cmap='YlOrRd', ax=ax ,legend=True)
    ax.set_title("Koef by Country")

    # Remove tick labels on x and y axes
    plt.xticks([])
    plt.yticks([])



    plt.show()

print(suicide_map(input_spol, input_leto))