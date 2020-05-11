import covid_csv_index_constants
class ListManager:
    def __init__(self):
        pass

    def filter_by_country_iso_code(self, list_of_covid_cases_to_filter: list, country_iso_code: str) -> list:
        filtered_list = []
        if (len(list_of_covid_cases_to_filter) > 0):
            for row in list_of_covid_cases_to_filter:
                if row[0] == country_iso_code:
                    filtered_list.append(row)
            return filtered_list
        return filtered_list

    def get_type_of_data_list(self, covid_cases_filtered_by_country: list, type_of_covid_data: int):
        list_of_cases = []
        if (len(covid_cases_filtered_by_country) > 0):
            for row in covid_cases_filtered_by_country:
                try:
                    list_of_cases.append(row[type_of_covid_data])
                except Exception as exception_message:
                    print(f'Failed on converting the current row. Error: {exception_message}')
                    pass
        return list_of_cases

    def get_date_list(self, covid_cases_filtered_by_country: list):
        list_of_dates = []
        if (len(covid_cases_filtered_by_country) > 0):
            for row in covid_cases_filtered_by_country:
                try:
                    # [5:] -> Substring to get only 'month-day' instead of the full date format
                    list_of_dates.append(row[covid_csv_index_constants.LIST_DATE_INDEX][5:])
                except Exception as exception_message:
                    print(f'Failed on converting the current date row. Error: {exception_message}')
        return list_of_dates

    def get_cases_by_interval_in_days(self, list_to_filter_from: list, interval_in_days: int) -> list:
        filtered_list = []
        if (len(list_to_filter_from) > 0):
            interval_counter = interval_in_days
            reset_days_counting = 1
            for row in list_to_filter_from:
                if interval_counter == interval_in_days:
                    interval_counter = reset_days_counting
                    filtered_list.append(row)
                else:
                    interval_counter = interval_counter + 1
            return filtered_list
        return filtered_list