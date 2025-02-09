from datetime import datetime, date
from source.Logic.Vacations_Logic import VacationLogic
from source.Logic.Country_Logic import CountryLogic
from source.Logic.Like_Logic import LikeLogic
import re

class VacationFacade:
    def __init__(self):
        self.params = []
        self.now = date.today()
        self.logic = VacationLogic()
        self.country_logic = CountryLogic()
        self.like_logic = LikeLogic()


    def show_vacation(self, id):
        vac = self.logic.get_vacation(id)
        print("Vacation details")
        print(f"Title: {vac['vacation_title']}")
        print(f"Description: {vac['description']}")
        print(f"Price: {vac['price']}")
        print(f"Country: {self.country_logic.get_all_countries()[vac['Countries_id']]['country_name']}")
        print(f"Start date: {vac['start_date']}")
        print(f"End date: {vac['end_date']}")
        print(f"Likes: {len(self.like_logic.get_all_likes_by_vacation(id))}")


    def edit_vacation(self, id):
        print("Editing vacation...")
        updates = {}

        if input("Edit title? (y/n): ").strip().lower() == 'y':
            self.get_title()
            updates['vacation_title'] = self.params[-1]

        if input("Edit description? (y/n): ").strip().lower() == 'y':
            self.get_description()
            updates['description'] = self.params[-1]

        if input("Edit start date? (y/n): ").strip().lower() == 'y':
            self.get_start_date()
            updates['start_date'] = self.params[-1]

        if input("Edit end date? (y/n): ").strip().lower() == 'y':
            self.get_end_date()
            updates['end_date'] = self.params[-1]

        if input("Edit country? (y/n): ").strip().lower() == 'y':
            self.get_countries_name()
            updates['Countries_id'] = self.params[-1]

        if input("Edit price? (y/n): ").strip().lower() == 'y':
            self.get_price()
            updates['price'] = self.params[-1]

        if input("Edit image URL? (y/n): ").strip().lower() == 'y':
            self.get_image()
            updates['img_url'] = self.params[-1]

        success = self.logic.edit_vacation(id, **updates)
        if success:
            print("Vacation updated successfully!")
        else:
            print("Failed to update vacation.")

    def add_vacation(self):
        print("Adding vacation...")
        self.get_title()
        self.get_description()
        self.get_start_date()
        self.get_end_date()
        self.get_countries_name()
        self.get_price()
        self.get_image()

        return self.logic.add_vacation(*self.params)

    def get_title(self):
        while True:
            title = input("Enter title: ").strip()
            if not title.replace(" ", "").isalpha():
                print("Title must contain only letters and spaces")
            elif len(title) < 5:
                print("Title must be at least 5 characters long")
            else:
                self.params.append(title)
                print("Title added")
                break

    def get_countries_name(self):
        while True:
            countries_name = input("Enter country name: ")
            if self.country_logic.check_if_country_exist(countries_name):
                print("Country added to vacation info!")
                self.params.append(countries_name)
                break
            else:
                print(
                    "Country does not exist in database, here is a list of all countries:")
                countries = self.country_logic.get_all_countries()
                print(" | ".join(country["country_name"]
                      for country in countries))

    def get_description(self):
        while True:
            description = input("Enter description: ").strip()
            if not description:
                print("Description is mandatory!")
            else:
                self.params.append(description)
                break

    def get_start_date(self):

        while True:
            try:
                date_str = input("Enter start date (YYYY-MM-DD): ")
                start_date = datetime.strptime(date_str, "%Y-%m-%d").date()

                if start_date < self.now:
                    print("Start date cannot be in the past")
                    continue

                self.params.append(start_date)
                print("Start date added")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")

    def get_end_date(self):

        while True:
            try:
                date_str = input("Enter end date (YYYY-MM-DD): ")
                end_date = datetime.strptime(date_str, "%Y-%m-%d").date()

                if end_date < self.now:
                    print("End date cannot be in the past")
                    continue

                if end_date <= self.params[-1]:
                    print("End date must be after start date")
                    continue

                self.params.append(end_date)
                print("End date added")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")

    def get_price(self):
        while True:
            try:
                price = float(input("Enter price: "))
                if not 1000 <= price <= 10000:
                    print("Price must be between 1000 and 10000")
                else:
                    self.params.append(price)
                    print("Price added")
                    break
            except ValueError:
                print("Price must be a number!")

    def get_image(self):
        while True:
            image_url = input(
                "Enter image URL (optional, press Enter to skip): ").strip()
            if not image_url:
                self.params.append(None)
                print("No image URL selected")
                break

            # Basic URL validation with regular expression
            url_pattern = r'^https?:\/\/[^\s\/$.?#].[^\s]*$'
            if not re.match(url_pattern, image_url):
                print("Invalid URL format!")
                continue

            self.params.append(image_url)
            print("Image URL added")
            break


if __name__ == "__main__":

    vacation = VacationFacade()

    vacation.edit_vacation(1)

    result = vacation.add_vacation()

    print("\nBooking Results:")
    print("---------------")
    print(f"Vacation title: {vacation.params[0]}")
    print(f"Description: {vacation.params[1]}")
    print(f"Start date: {vacation.params[2]}")
    print(f"End date: {vacation.params[3]}")
    print(f"Country: {vacation.params[4]}")
    print(f"Price: ${vacation.params[5]}")
    print(f"Image URL: {vacation.params[6]}")