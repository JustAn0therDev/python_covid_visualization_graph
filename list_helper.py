class ListHelper:

    @staticmethod
    def format_lists_from_all_covid_cases_list(covid_cases_filtered_by_country: list, list_of_dates: list, list_of_cases: list):
        if (type(covid_cases_filtered_by_country) is not None and len(covid_cases_filtered_by_country) > 0):
            for row in covid_cases_filtered_by_country:
                try:
                    list_of_dates.append(row[2][5:])
                    list_of_cases.append(row[3])
                except Exception as exception_message:
                    print(f'Failed on converting the current row. Error: {exception_message}')
                    pass

    @staticmethod
    def filter_by_country_iso_code(list_of_covid_cases_to_filter: list, country_iso_code: str) -> list:
        filtered_list = []
        if (list_of_covid_cases_to_filter is not None and len(list_of_covid_cases_to_filter) > 0):
            for row in list_of_covid_cases_to_filter:
                if row[0] == country_iso_code.upper():
                    filtered_list.append(row)
            return filtered_list

    @staticmethod
    def get_cases_by_interval_in_days(list_to_filter_from: list, interval_in_days: int) -> list:
        if (type(list_to_filter_from) is not None and len(list_to_filter_from) > 0):
            filtered_list = []
            interval_counter = interval_in_days
            reset_days_counting = 1
            for row in list_to_filter_from:
                if interval_counter == interval_in_days:
                    interval_counter = reset_days_counting
                    filtered_list.append(row)
                else:
                    interval_counter = interval_counter + 1
            return filtered_list