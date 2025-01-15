import mysql.connector


class DAL:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(  # Fixed self.connector.connect to mysql.connector.connect
                host="localhost",
                user="root",
                password="OSh329227961",
                database="mydb"
            )
            self.connection.autocommit = True  # Set autocommit explicitly
            # print("Database connection established.")
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            self.connection = None

    def validate_query_params(self, query, params):
        """Validate the query and parameters."""
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")
        if params is not None and not isinstance(params, tuple):
            raise ValueError("Params must be a tuple or None.")

    def execute_query(self, query, params=None, fetchall=False, fetchone=False):
        """Execute a query and optionally fetch results."""
        self.validate_query_params(query, params)
        if self.connection:
            try:
                with self.connection.cursor(dictionary=True) as cursor:  # Fixed typo: curser -> cursor
                    # print(f"Executing query: {query}")
                    if params:
                        pass
                        # print(f"With parameters: {params}")
                    cursor.execute(query, params)

                    if fetchall:
                        result = cursor.fetchall()
                        # print(f"Fetched {len(result)} rows.")
                        return result
                    if fetchone:
                        result = cursor.fetchone()
                        # print("Fetched one row.")
                        return result

                    # print(f"Query executed successfully, affected {cursor.rowcount} rows.")
                    return True
            except mysql.connector.Error as err:
                # print(f"Error executing query: {err}")
                if fetchall or fetchone:
                    return None
                return False
        else:
            # print("No connection to the database. Query not executed.")
            return None

    def get_table(self, query, params=None):
        return self.execute_query(query, params, fetchall=True)

    def get_scalar(self, query, params=None):
        return self.execute_query(query, params, fetchone=True)

    def insert(self, query, params=None):
        return self.execute_query(query, params)

    def update(self, query, params=None):
        return self.execute_query(query, params)

    def delete(self, query, params=None):
        return self.execute_query(query, params)

    def close(self):
        if self.connection:
            self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_typ, exc_value ,exc_tb):
        if self.connection:
            self.close()
            print("connection closed")

if __name__ == "__main__":
    with DAL() as dal:
        print("\n==get table examples==")
        countries = dal.get_table("SELECT * FROM countries")
        users = dal.get_table("SELECT * FROM users")
        for country in countries:
            print(f"country name: {country['country_name']}, id: {country['id']}")
        for user in users:
            print(f"user name: {user['first_name']} {user['last_name']}, id: {user['id']}")

        print(dal.insert("fdb"))

