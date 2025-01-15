from source.Utils.DAL import DAL

class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_users(self):
        query = "SELECT * from mydb.users"
        result = self.dal.get_table(query)
        return result if result is not None else []

    def is_admin(self, user_id):
        try:
            query = "SELECT * from mydb.users where id = %s"
            params = (user_id,)
            result = self.dal.get_table(query, params)
            return result[0]['Roles_id'] == 1

        except Exception as err:
            print(f"Error checking user: {err}")
            return False

    def get_user(self, user_id):
        try:
            query = "SELECT * from mydb.users where id = %s"
            params = (user_id,)
            return self.dal.get_scalar(query, params)

        except Exception as err:
            print(f"Error checking user: {err}")
            return False

    def add_user(self, first_name, last_name, email, password, date_of_birth):
        try:
            if not self.is_exist_email(email):
                query = """
                INSERT INTO mydb.users 
                (first_name, last_name, email, password, date_of_birth, Roles_id)
                VALUES 
                (%s, %s, %s, %s, %s, 2)
                """
                params = (first_name, last_name, email, password, date_of_birth)
                return self.dal.insert(query, params)
            else:
                return False

        except Exception as err:
            print(f"Error adding vacation: {err}")
            return False

    def is_exist_user(self, email, password):
        try:
            query = "SELECT * from mydb.users where email = %s AND password = %s"
            params = (email, password)
            result = self.dal.get_table(query, params)
            if len(result) != 0:
                return True
            return False

        except Exception as err:
            print(f"Error checking user: {err}")
            return False

    def get_user_from_email_password(self, email, password):
        try:
            query = "SELECT * from mydb.users where email = %s AND password = %s"
            params = (email, password)
            return self.dal.get_scalar(query, params)

        except Exception as err:
            print(f"Error checking user: {err}")
            return False

    def is_exist_email(self, email):
        try:
            query = "SELECT * from mydb.users where email = %s"
            params = (email,)
            result = self.dal.get_table(query, params)
            if len(result) != 0:
                return True
            return False

        except Exception as err:
            print(f"Error checking user: {err}")
            return False


if __name__ == "__main__":
    try:
        with UserLogic() as user_logic:
            # Test each function in the class
            try:
                print("Testing get_all_users...")
                users = user_logic.get_all_users()
                print("Users:", users)

                print("Testing is_admin with ID 3...")
                is_admin = user_logic.is_admin(3)
                print("Is Admin:", is_admin)

                print("Testing add_user...")
                success = user_logic.add_user("Test", "User", "unique123.email@example.com", "password123", "2000-01-01")
                print("User added:", success)

                print("Testing is_exist_user...")
                exist_user = user_logic.is_exist_user("test.user@example.com", "password123")
                print("Does User Exist:", exist_user)

                print("Testing is_exist_email...")
                exist_email = user_logic.is_exist_email("test.user@example.com")
                print("Does Email Exist:", exist_email)

            except Exception as test_err:
                print(f"Error during function tests: {test_err}")
    except Exception as err:
        print(f"Error: {err}")
