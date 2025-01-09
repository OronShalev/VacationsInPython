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

    def is_admin(self, id):
        try:
            query = "SELECT * from mydb.users where user_id = %s"
            params = (id,)
            result = self.dal.get_table(query, params)
            if (result[0])[-1] == 2: #לבדוק האם התפקיד של אותו משתמש הוא 2
                return True
            return False

        except Exception as err:
            print(f"Error checking user: {err}")
            return False

    def add_user(self, first_name, last_name, email, password, date_of_birth):
        try:
            if not self.is_exist_email(email) and not self.is_exist_password(password):
                query = """
                INSERT INTO mydb.users 
                (first_name, last_name, email, password, date_of_birth, role)
                VALUES 
                (%s, %s, %s, %s, %s, 1)
                """
                params = (first_name, last_name, email, password, date_of_birth)
                self.dal.insert(query, params)
                return True
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

    def is_exist_email(self, email):
        try:
            query = "SELECT * from mydb.users where email = %s"
            params = (email)
            result = self.dal.get_table(query, params)
            if len(result) != 0:
                return True
            return False

        except Exception as err:
            print(f"Error checking user: {err}")
            return False
    
    def is_exist_password(self, password):
        try:
            query = "SELECT * from mydb.users where password = %s"
            params = (password)
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
            users = user_logic.get_all_users()
            for user in users:
                print("----------------------")
                print(user)
    except Exception as err:
        print(f"Error: {err}")