import csv
import matplotlib.pyplot as plt
import numpy as np
from filters import filter_by_country, filter_every_five_items

list_of_dates = []
list_of_cases = []

with open('owid-covid-data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, dialect='excel',  delimiter=',')
    filtered_cases = filter(filter_by_country, csv_reader)
    for row in filtered_cases:
        list_of_dates.append(row[2])
        list_of_cases.append(row[3])
    list_of_dates = filter_every_five_items(list_of_dates)
    list_of_cases = filter_every_five_items(list_of_cases)

plt.plot(list_of_cases, list_of_dates, "#FF0000")
plt.ylabel("Total de casos")
plt.xlabel("Datas")
plt.show()