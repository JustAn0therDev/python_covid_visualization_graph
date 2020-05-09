import csv

class CsvManager:

    ALL_COVID_CASES_IN_CSV = []

    def __init__(self):
        self.ALL_COVID_CASES_IN_CSV = self.get_all_covid_cases_list_from_csv()

    def get_all_covid_cases_list_from_csv(self):
        with open('owid-covid-data.csv') as all_covid_cases_in_csv:
            return list(csv.reader(all_covid_cases_in_csv, delimiter=','))