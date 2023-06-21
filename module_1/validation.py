import os
import sys


def check_book_title(title):
    while True:
        if all(x.isalpha() for x in title):
            return title
        else:
            print('Valid title, must be str: ', title)
            title = input('Enter a new title: ')
            continue


def check_price(price):
    while True:
        point = price.find('.')
        first_half = price[:point]
        second_half = price[point + 1:]
        if first_half.isnumeric() and second_half.isnumeric() and len(second_half) == 2:
            return price
        else:
            print('Valid rent price:', price)
            price = input('Enter a new price: ')
            continue


def check_user_name(user_name):
    while True:
        if all(x.isalpha() for x in user_name):
            return user_name
        else:
            print('Valid user_name, must be str: ', user_name)
            user_name = input('Enter a new user_name: ')
            continue


def input_file(fl):
    while True:
        if os.path.isfile(fl) and fl.endswith(".txt"):
            return fl
        else:
            fl = input("File name is incorrect. Try again: ")


def check_day(day_):
    while True:
        try:
            if int(day_) < 0:
                print('Valid day, must be positive: ', day_)
                day_ = input('Enter new day: ')
                continue
            elif int(day_) <= 31:
                return day_
            else:
                day_ = input('Day must be <= 31: ')
        except ValueError:
            print('Valid day, must be integer: ', day_)
            day_ = input('Enter new day: ')
            continue


def check_month(month):
    while True:
        try:
            if int(month) < 0:
                print('Valid month, must be positive: ', month)
                month = input('Enter new month: ')
                continue
            elif int(month) <= 12:
                return month
            else:
                month = input('Month must be <= 12: ')
        except ValueError:
            print('Valid month, must be integer: ', month)
            month = input('Enter new month: ')
            continue


def check_year(year):
    while True:
        try:
            if int(year) < 2018:
                print('Valid year, must be positive: ', year)
                year = input('Enter new year: ')
                continue
            elif int(year) <= 2023:
                return year
            else:
                year = input('Year must be <= 2023: ')
        except ValueError:
            print('Valid year, must be integer: ', year)
            year = input('Enter new year: ')
            continue


def check_date(date):
    while True:
        if len(date) == 10:
            day = date[:2]
            month = date[3:5]
            year = date[6:10]
            day = check_day(day)
            month = check_month(month)
            year = check_year(year)
            return date
        else:
            date = input('Valid date! Try again: ')
            continue


def check_end_date(date, rent_date):
    while True:
        day = date[:2]
        month = date[3:5]
        year = date[6:10]
        day1 = rent_date[:2]
        month1 = rent_date[3:5]
        year1 = rent_date[6:10]
        if year > year1:
            return date
        elif year == year1:
            if month > month1:
                return date
        elif year == year1:
            if month == month1:
                if day > day1:
                    return date
        else:
            date = input('end date must be bigger than rent day! Try again: ')