import matplotlib.pyplot as plt

class UiManager:

    __DEFAULT_LINE_COLOR: str =  "#FF0000"

    def __init__(self):
        pass

    def __one_of_the_lists_is_empty(self, list_one: list, list_two: list) -> bool:
        if len(list_one) == 0 or len(list_two) == 0:
            return True
        return False

    def create_plot_from_two_lists(self, list_in_axis_x: list, list_in_axis_y: list) -> None:
        if (self.__one_of_the_lists_is_empty(list_in_axis_x, list_in_axis_y)):
            plt.plot()
        else:
            plt.plot(list_in_axis_y, list_in_axis_x, self.__DEFAULT_LINE_COLOR)

    def define_labels_for_both_axis(self, label_for_axis_y: str, label_for_axis_x: str) -> None:
        plt.ylabel(label_for_axis_y)
        plt.xlabel(label_for_axis_x)

    def show_plot(self) -> None:
        plt.show()