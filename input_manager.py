from covid_csv_index_descriptions import CSV_INDEX_DESCRIPTIONS

class InputManager:
    chosen_country_iso_code: str = ""
    chosen_type_of_data: int = 0
    chosen_interval_in_days: int = 0

    def __init__(self):
        pass

    def prompt_user_for_country_iso_code(self) -> None:
        try:
            self.chosen_country_iso_code = input("Please provide the ISO code for the country of preference (e.g: BRA, USA, ITA): ").upper()
        except KeyboardInterrupt:
            quit()

    def prompt_user_for_type_of_data(self) -> None:
        try:
            for index in CSV_INDEX_DESCRIPTIONS:
                print(index)
            self.chosen_type_of_data = int(input("Please provide the type of data that will be shown in the graph (only numbers): "))
        except KeyboardInterrupt:
            quit()
        except Exception:
            self.prompt_user_for_type_of_data()

    def prompt_user_for_interval_in_days(self) -> None:
        try:
            self.chosen_interval_in_days = int(input("Please provide the number of days the reports of cases (only numbers and more than 3 days is recommended for good legibility): "))
        except KeyboardInterrupt: 
            quit()
        except:
            self.prompt_user_for_interval_in_days()