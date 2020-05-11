from input_manager import InputManager
from list_manager import ListManager
from csv_manager import CsvManager
from ui_manager import UiManager
inputManager = InputManager()
listManager = ListManager()
csvManager = CsvManager()
uiManager = UiManager()

inputManager.prompt_user_for_country_iso_code()
inputManager.prompt_user_for_type_of_data()
inputManager.prompt_user_for_interval_in_days()

covid_cases_filtered_by_country = listManager.filter_by_country_iso_code(csvManager.ALL_COVID_CASES_IN_CSV, inputManager.chosen_country_iso_code)

list_of_dates = listManager.get_date_list(covid_cases_filtered_by_country)
list_of_cases = listManager.get_type_of_data_list(covid_cases_filtered_by_country, inputManager.chosen_type_of_data)

list_of_dates = listManager.get_cases_by_interval_in_days(list_of_dates, inputManager.chosen_interval_in_days)
list_of_cases = listManager.get_cases_by_interval_in_days(list_of_cases, inputManager.chosen_interval_in_days)

uiManager.create_plot_from_two_lists(list_of_cases, list_of_dates)
uiManager.define_labels_for_both_axis("Cases", f"Date (for every {inputManager.chosen_interval_in_days} days)")
uiManager.show_plot()