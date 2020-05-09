class ListHelper:

    @staticmethod
    def format_lists_from_all_covid_cases_list(covid_cases_filtered_by_country: list, list_of_dates: list, list_of_cases: list):
        for row in covid_cases_filtered_by_country:
            try:
                list_of_dates.append(row[2][5:])
                list_of_cases.append(row[3])
            except Exception as exception_message:
                print(f"I couldn't convert the row because of the following error: {exception_message}")

    @staticmethod
    def filter_by_country(list_of_covid_cases_to_filter: list, country: str) -> list:
        filtered_list = []
        for row in list_of_covid_cases_to_filter:
            if row[0] == country.upper():
                filtered_list.append(row)
        return filtered_list

    @staticmethod
    def get_cases_by_number_of_days(list_to_filter_from: list, number_of_days: int) -> list:
        filtered_list = []
        interval_in_days = number_of_days
        reset_days_counting = 1
        for row in list_to_filter_from:
            if interval_in_days == number_of_days:
                interval_in_days = reset_days_counting
                filtered_list.append(row)
            else:
                interval_in_days = interval_in_days + 1
        return filtered_list
    