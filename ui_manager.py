import matplotlib.pyplot as plt

class UiManager:

    DEFAULT_LINE_COLOR: str =  "#FF0000"

    def __init__(self):
        pass

    def create_plot_from_two_lists(self, list_in_axis_x: list, list_in_axis_y: list):
        plt.plot(list_in_axis_y, list_in_axis_x, self.DEFAULT_LINE_COLOR)

    def define_labels_for_both_axis(self, label_for_axis_y: str, label_for_axis_x: str):
        plt.ylabel(label_for_axis_y)
        plt.xlabel(label_for_axis_x)

    def show_plot(self):
        plt.show()