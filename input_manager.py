class InputManager:
    chosen_country_iso_code: str = ""
    number_of_days: int = 0

    def __init__(self) -> None:
        pass

    def prompt_user_for_country_iso_code(self) -> None:
        self.chosen_country_iso_code = input("Please write the ISO code for the country of preference (e.g: BRA, USA, ITA): ")

    def prompt_user_for_number_of_days(self) -> None:
        self.number_of_days = int(input("Please input the number of days to between cases (only numbers): "))