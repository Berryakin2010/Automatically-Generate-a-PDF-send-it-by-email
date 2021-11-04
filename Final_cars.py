#!/usr/bin/env python3

import json
import locale
import sys

from reports import generate as report
from emails import generate as email_generate
from emails import send as email_send

#Loads the contents of filename as a JSON file.
def load_data(filename):
    with open(filename) as json_file:
        new_data - json.load(json_file)
        data- sorted(new data, key=lambda i: i['total_sales'])
    return data

#Given a car dictionary, returns a nicely formatted name.
def format_car(car):
    return"{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])

#Analyzes the data, looking for maximums.
#Returns a list of lines that summerize the information.
def process_data(data):
    local.setlocale(locale.LC_ALL, 'en_US.UTF8')
    max_revenue = {"revenue": 0}
    sales = {"total_sales": 0}
    best_car = {}
    for item in data:
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revinue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
        if item["total_sales"] > slaes["total_sales"]:
            sales = item
        if not item["car"]["car_year"] in best_car.keys():
            best_car[item["car"]["car_year"]] = item["total_sales"]
        else: 
            best_car[item["car"]["car_year"]] += item["total_sales"]

        all_values = best_car.values()
        max_value = max(all_values)
        max_key = max(best_car, key=best_car.get)

    summary = [
        "The {} generateed the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]), 
        "The {} had the most sales: {}".format(sales["car"]["car_model"], sales["total_sales"]),
        "The most popular year was {} with {} sals.".format(max_key, max_value),
    ]

    return summary

#Turns the data in car data into a list of lists.
def cars_dic_to_table(car_data):
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table _data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]]
    return table_data

#Process teh JSON data and generate a full report out of it.
def main(argv):
    data = load_data("/home/<username>/car_sales.json")
    summary = process_data(data)
    new_summary = '<br/>'.join(summary)
    print(summary)
    report('/tmp/cars.pdf', "Carsreport", new summary, cars_dic_to_table(data))
    msg = email_generate("automation@xample.com", "<username>@example.com",
                         "Sales summary for the last month", new_summary, "/temp/cars.pdf")
    email_send(msg)


if __name__ == "__main__":
    main(sys.argv)
