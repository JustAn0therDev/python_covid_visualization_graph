import csv

def get_all_covid_cases_from_csv():
    with open('owid-covid-data.csv') as all_covid_cases_in_csv:
        return list(csv.reader(all_covid_cases_in_csv, dialect='excel', delimiter=',')) 