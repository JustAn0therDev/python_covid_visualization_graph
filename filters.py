def filter_by_country(row: list) -> any:
    if row[0] == "BRA":
        return row

def filter_every_five_items(list_to_filter_from: list) -> list:
    filtered_list = []
    counter = 5
    for item in list_to_filter_from:
        if counter == 5:
            counter = 0
            filtered_list.append(item)
        else:
            counter = counter + 1
    return filtered_list
    