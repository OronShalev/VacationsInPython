from source.Utils.DAL import DAL

class LikeLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_likes_by_vacation(self, vacation_id):
        query = "SELECT * from mydb.likes WHERE Vacations_id = %s"
        params = (vacation_id,)
        result = self.dal.get_table(query, params)
        return result if result is not None else []
    
    def get_all_likes_by_user(self, user_id):
        query = "SELECT * from mydb.likes WHERE Users_id = %s"
        params = (user_id,)
        result = self.dal.get_table(query, params)
        return result if result is not None else []

    def is_liked(self, user_id, vacation_id):
        try:
            query = "SELECT * from mydb.likes where Users_id = %s AND Vacations_id = %s"
            params = (user_id, vacation_id)
            result = self.dal.get_table(query, params)
            return bool(result)

        except Exception as err:
            print(f"Error checking user: {err}")
            return False

    def add_like(self, Vacations_id, Users_id):
        try:
            if not self.is_liked(Users_id, Vacations_id):
                query = """
                INSERT INTO mydb.likes
                (Vacations_id, Users_id)
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
            if self.is_liked(Users_id, Vacations_id):
                query = "DELETE FROM mydb.likes WHERE Vacations_id = %s AND Users_id = %s"
                params = (Vacations_id, Users_id)
                result = self.dal.delete(query, params)
                return True
            else:
                return False
        
        except Exception as err:
            print(f"Error removing like: {err}")
            return False
        
    def delete_all_likes_from_vacation(self, Vacations_id):
        try:
            query = "DELETE FROM mydb.likes WHERE Vacations_id = %s"
            params = (Vacations_id,)
            result = self.dal.delete(query, params)
            return True
        
        except Exception as err:
            print(f"Error deleting vacation: {err}")
            return False
