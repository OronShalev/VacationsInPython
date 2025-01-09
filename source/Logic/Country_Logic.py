from source.Utils.DAL import DAL

class CountryLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_countries(self):
        query = "SELECT * FROM countries"
        return self.dal.get_table(query)

    def check_if_country_exist(self, country_name):
        query = "SELECT COUNT(*) as count FROM countries WHERE country_name = %s"
        params = (country_name,)
        result = self.dal.get_scalar(query, params)

        return result['count'] > 0


if __name__ == "__main__":
    with CountryLogic() as logic:
        # Check if a specific country exists
        exists = logic.check_if_country_exist("Argentina")
        print(f"Country exists: {exists}")

        # Get and print all countries
        countries = logic.get_all_countries()
        for country in countries:
            print(f"ID: {country['id']}, Name: {country['country_name']}")
