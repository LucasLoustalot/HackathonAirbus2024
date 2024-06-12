import csv

def get_info_value(info, json):
    for key, value in json.items():
        if key == info:
            return value
    return ""

def get_list_values(info, json):
    if (info not in json):
        return ""
    str = ""
    for key, value in json.items():
        if key == info:
            if (type(value) == list):
                for val in value:
                    str += val + ", "
                str = str[:-2]
                return str
            for let in value:
                str += let
            return str

def json_to_csv(json):
    json = json['args']
    row = ""
    row += get_info_value('name', json) + ";"
    row += get_info_value('location', json) + ";"
    row += get_info_value('link', json) + ";"
    row += get_info_value('contact', json) + ";"
    row += get_info_value('turnover', json) + ";"
    row += get_info_value('size', json) + ";"
    row += get_list_values('certifications', json) + ";"
    row += get_list_values('skills', json) + ";"
    row += get_info_value('main_sector', json) + ";"
    row += get_list_values('main_customers', json)
    return row
