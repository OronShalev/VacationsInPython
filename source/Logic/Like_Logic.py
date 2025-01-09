from source.Utils.DAL import DAL

class LikeLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_likes(self, vacation_id):
        query = "SELECT * from mydb.likes"
        result = self.dal.get_table(query)
        return result if result is not None else []

    def is_liked(self, user_id, vacation_id):
        try:
            query = "SELECT * from mydb.users where user_id = %s AND vacation_id = %s"
            params = (user_id, vacation_id)
            result = self.dal.get_table(query, params)
            if len(result) == 1:
                return True
            return False

        except Exception as err:
            print(f"Error checking user: {err}")
            return False

    def add_like(self, Vacations_id, Users_id):
        try:
            if not self.is_liked(Vacations_id, Users_id):
                query = """
                INSERT INTO mydb.likes
                (vacations_id, users_id)
                VALUES 
                (%s, %s)
                """
                params = (Vacations_id, Users_id)
                self.dal.insert(query, params)
                return True
            else:
                return False
        
        except Exception as err:
            print(f"Error adding like: {err}")
            return False

    def remove_like(self, Vacations_id, Users_id):
        try:
            if self.is_liked(Vacations_id, Users_id):
                query = "DELETE FROM mydb.likes WHERE vacation_id = %s AND user_id = %s"
                params = (Vacations_id, Users_id)
                result = self.dal.delete(query, params)
                return True
            else:
                return False
        
        except Exception as err:
            print(f"Error removing like: {err}")
            return False


if __name__ == "__main__":
    try:
        with LikeLogic() as like_logic:
            likes = like_logic.get_all_likes()
            for like in likes:
                print("----------------------")
                print(like)
    except Exception as err:
        print(f"Error: {err}")