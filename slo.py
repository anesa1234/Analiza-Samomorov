import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd


ime_datoteke = "slo.xlsx"

datoteka = ("C:\\Users\\evami\\OneDrive\\Dokumenti\\FAKS\\PROG2\\slo.xlsx")

podatki_slo= pd.read_excel(datoteka)
df=pd.DataFrame(podatki_slo)



da vidim ce dela veja


letnice = df.iloc[1,2:]

skupaj= df.iloc[3,2:]
l10_19= df.iloc[5,2:]
l20_24= df.iloc[6,2:]
l25_29= df.iloc[7,2:]
l30_34= df.iloc[8,2:]
l35_39= df.iloc[9,2:]
l40_44= df.iloc[10,2:]
l45_49= df.iloc[11,2:]
l50_54= df.iloc[12,2:]
l55_59= df.iloc[13,2:]
l60_64= df.iloc[14,2:]
l65_69= df.iloc[15,2:]
l70_74= df.iloc[16,2:]
l75_79= df.iloc[17,2:]
l80inVec= df.iloc[18,2:]




slovar = {'Leta':[], '10-19':[], '20-24':[],'25-29':[],'30-34':[], '35-39':[], '40-44':[], '45-49':[],
           '50-54':[] ,'55-59':[],'60-64':[], '65-69':[], '70-74':[] , '75-79':[], '80_in_vec':[] }

slovar2 ={'Leta':[], 'Skupaj':[]} 

for leto in letnice:
    slovar['Leta']+= [leto]
    slovar2['Leta']+= [leto]

for vrednost in skupaj:
    slovar2['Skupaj']+= [vrednost]    

for leto in l10_19:
    slovar['10-19']+= [leto]

for leto in l20_24:
    slovar['20-24']+= [leto]

for leto in l25_29:
    slovar['25-29']+= [leto]    

for leto in l30_34:
    slovar['30-34']+= [leto]

for leto in l35_39:
    slovar['35-39']+= [leto]  

for leto in l40_44:
    slovar['40-44']+= [leto]

for leto in l45_49:
    slovar['45-49']+= [leto]  

for leto in l50_54:
    slovar['50-54']+= [leto]

for leto in l55_59:
    slovar['55-59']+= [leto] 

for leto in l60_64:
    slovar['60-64']+= [leto]

for leto in l65_69:
    slovar['65-69']+= [leto] 

for leto in l70_74:
    slovar['70-74']+= [leto]

for leto in l75_79:
    slovar['75-79']+= [leto] 

for leto in l80inVec:
    slovar['80_in_vec']+= [leto]     

print(slovar2)








##################################################################################################
# SAMOMORI PO STAROSTNIH SKUPINAH


# get the x and y data
x_data = slovar['Leta']
y_data = {key: val for key, val in slovar.items() if key != 'Leta'}

# create the figure and subplot
fig, ax = plt.subplots(figsize=(12,6))

# set the marker style and size
marker_style = '.'
marker_size = 10

# plot the data
for key, val in y_data.items():
    ax.plot(x_data, val, marker_style, markersize=marker_size, label=key)

# set the x and y axis labels and title
#ax.set_xlabel('Leta')
ax.set_ylabel('Število samomorov')
ax.set_title('Prikaz samomorv po starostnih skupinah')

# add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.135, 1.0))

# display the plot
plt.show()



########################################################################
# HISTOGRAM PO LENICAH




x = slovar2['Leta']
y = slovar2['Skupaj']

plt.bar(x, y, width=0.9, align='center')


plt.title('Število samomorv v Sloveniji')

plt.show()
