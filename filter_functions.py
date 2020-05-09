def filter_by_country(list_of_covid_cases_to_filter: list, country: str) -> any:
    filtered_list = []
    for row in list_of_covid_cases_to_filter:
        if row[0] == country.upper():
            filtered_list.append(row)
    return filtered_list

def get_cases_by_number_of_days(list_to_filter_from: list, number_of_days: int) -> list:
    filtered_list = []
    counter = number_of_days
    for item in list_to_filter_from:
        if counter == number_of_days:
            counter = 1
            filtered_list.append(item)
        else:
            counter = counter + 1
    return filtered_list
    