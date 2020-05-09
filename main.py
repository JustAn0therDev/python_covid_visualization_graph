import csv
import matplotlib.pyplot as plt
from filter_functions import filter_by_country, get_cases_by_number_of_days
from covid_cases import get_all_covid_cases_from_csv

list_of_dates = []
list_of_cases = []

chosen_country_iso_code = input("Please write the iso_code for the country of preference (e.g: BRA, USA, ITA): ")
covid_cases_filtered_by_country = filter_by_country(get_all_covid_cases_from_csv(), chosen_country_iso_code)
for row in covid_cases_filtered_by_country:
    try:
        list_of_dates.append(row[2][5:])
        list_of_cases.append(row[3])
    except Exception as exception_message:
        print(f"Couldn't convert row because of the following error: {exception_message}")

number_of_days_to_show_data = int(input("Please input the number of days to between cases (only numbers): "))
list_of_dates = get_cases_by_number_of_days(list_of_dates, number_of_days_to_show_data)
list_of_cases = get_cases_by_number_of_days(list_of_cases, number_of_days_to_show_data)

plt.plot(list_of_dates, list_of_cases, "#FF0000")
plt.ylabel("Total de casos confirmados (testes, recuperados, mortos)")
plt.xlabel(f"Data (cada {number_of_days_to_show_data} dias)")
plt.show()