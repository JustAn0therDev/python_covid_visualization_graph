from input_manager import InputManager
from list_helper import ListHelper
from csv_manager import CsvManager
from ui_manager import UiManager

list_of_dates = []
list_of_cases = []
inputManager = InputManager()
csvManager = CsvManager()
uiManager = UiManager()

inputManager.prompt_user_for_country_iso_code()
inputManager.prompt_user_for_interval_in_days()

covid_cases_filtered_by_country = ListHelper.filter_by_country_iso_code(csvManager.ALL_COVID_CASES_IN_CSV, inputManager.chosen_country_iso_code)

ListHelper.format_lists_from_all_covid_cases_list(covid_cases_filtered_by_country, list_of_dates, list_of_cases)

list_of_dates = ListHelper.get_cases_by_interval_in_days(list_of_dates, inputManager.interval_in_days)
list_of_cases = ListHelper.get_cases_by_interval_in_days(list_of_cases, inputManager.interval_in_days)

uiManager.create_plot_from_two_lists(list_of_cases, list_of_dates)
uiManager.define_labels_for_both_axis("Total de casos confirmados (testes, confirmados, mortos)", f"Data (a cada {inputManager.interval_in_days} dias)")
uiManager.show_plot()