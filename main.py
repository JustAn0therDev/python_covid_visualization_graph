from list_helper import ListHelper
from csv_manager import CsvManager
from input_manager import InputManager
from ui_manager import UiManager

list_of_dates = []
list_of_cases = []

inputManager = InputManager()
csvManager = CsvManager()
uiManager = UiManager()

inputManager.prompt_user_for_country_iso_code()
covid_cases_filtered_by_country = ListHelper.filter_by_country(csvManager.ALL_COVID_CASES_IN_CSV, inputManager.chosen_country_iso_code)

ListHelper.format_lists_from_all_covid_cases_list(covid_cases_filtered_by_country, list_of_dates, list_of_cases)

inputManager.prompt_user_for_number_of_days()

list_of_dates = ListHelper.get_cases_by_number_of_days(list_of_dates, inputManager.number_of_days)
list_of_cases = ListHelper.get_cases_by_number_of_days(list_of_cases, inputManager.number_of_days)

uiManager.create_plot_from_two_lists(list_of_cases, list_of_dates)
uiManager.define_labels_for_both_axis("Total de casos confirmados (testes, confirmados, mortos)", f"Data (a cada {inputManager.number_of_days} dias)")
uiManager.show_plot()