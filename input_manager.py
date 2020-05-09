from typing import Type

class InputManager:
    chosen_country_iso_code: str = ""
    interval_in_days: int = 0

    def __init__(self):
        pass

    def prompt_user_for_country_iso_code(self) -> None:
        self.chosen_country_iso_code = input("Please write the ISO code for the country of preference (e.g: BRA, USA, ITA): ")

    def prompt_user_for_interval_in_days(self) -> None:
        try:
            self.interval_in_days = int(input("Please input the number of days the reports of cases (only numbers): "))
        except:
            self.prompt_user_for_interval_in_days()