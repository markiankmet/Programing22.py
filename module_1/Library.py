from validation import *


class Date:
    def __init__(self, day='1', month='1', year='1'):
        self.day = check_day(day)
        self.month = check_month(month)
        self.year = check_year(year)

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def input_date(self):
        self.day = check_day(input('Enter a day: '))
        self.month = check_month(input('Enter a month: '))
        self.year = check_year(input('Enter a year: '))


class Library:
    def __init__(self, book_title='City', rent_price='1.34', startRentDate='22.10.2020', endRentDate='22.10.2020',
                 user_name='Mark'):
        self.book_title = check_book_title(book_title)
        self.rent_price = check_price(rent_price)
        self.startRentDate = check_date(startRentDate)
        self.endRentDate = check_end_date(endRentDate, self.startRentDate)
        self.user_name = check_user_name(user_name)

    def __str__(self):
        return f"{self.book_title} {self.rent_price} {self.startRentDate} {self.endRentDate} {self.user_name}"

    def input_data(self):
        self.book_title = check_book_title(input('Enter book title: '))
        self.rent_price = check_price(input('Enter rent price: '))
        self.startRentDate = check_date(input('Enter start Date: '))
        self.endRentDate = check_end_date(input('Enter end Date: '), self.startRentDate)
        self.user_name = check_user_name(input('Enter user_name: '))

    def income(self):
        income_ = self.rent_price
        day = self.startRentDate[:2]
        month = self.startRentDate[3:5]
        year = self.startRentDate[6:10]
        day1 = self.endRentDate[:2]
        month1 = self.endRentDate[3:5]
        year1 = self.endRentDate[6:10]
        if year < year1:
            income_ += income_ * 0.1
            return income_
        elif year1 == year:
            if month1 - month >= 3:
                income_ += income_ * 0.1
                return income_

