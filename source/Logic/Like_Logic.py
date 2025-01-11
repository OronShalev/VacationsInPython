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


from source.Utils.DAL import DAL

class LikeLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_likes(self):
        query = "SELECT * from mydb.likes"
        result = self.dal.get_table(query)
        return result if result is not None else []

    def is_liked(self, user_id, vacation_id):
        try:
            query = "SELECT * from mydb.likes WHERE users_id = %s AND vacations_id = %s"
            params = (user_id, vacation_id)
            result = self.dal.get_table(query, params)
            return len(result) == 1
        except Exception as err:
            print(f"Error checking like: {err}")
            return False

    def add_like(self, vacation_id, user_id):
        try:
            if not self.is_liked(user_id, vacation_id):
                query = "INSERT INTO mydb.likes (vacations_id, users_id) VALUES (%s, %s)"
                params = (vacation_id, user_id)
                self.dal.insert(query, params)
                return True
            else:
                return False
        except Exception as err:
            print(f"Error adding like: {err}")
            return False

    def remove_like(self, vacation_id, user_id):
        try:
            if self.is_liked(user_id, vacation_id):
                query = "DELETE FROM mydb.likes WHERE vacations_id = %s AND users_id = %s"
                params = (vacation_id, user_id)
                self.dal.delete(query, params)
                return True
            else:
                return False
        except Exception as err:
            print(f"Error removing like: {err}")
            return False

if __name__ == "__main__":
    try:
        with LikeLogic() as like_logic:
            # Initial state
            print("Initial Likes:")
            likes = like_logic.get_all_likes()
            for like in likes:
                print(like)

            # Add a like
            print("\nAdding like for user 1 and vacation 1:")
            if like_logic.add_like(1, 1):
                print("Like added successfully.")
            else:
                print("Failed to add like (possibly already exists).")

            # Check if liked
            print("\nChecking if user 1 liked vacation 1:")
            if like_logic.is_liked(1, 1):
                print("User 1 liked vacation 1.")
            else:
                print("User 1 did not like vacation 1.")

            # Remove a like
            print("\nRemoving like for user 1 and vacation 1:")
            if like_logic.remove_like(1, 1):
                print("Like removed successfully.")
            else:
                print("Failed to remove like (possibly does not exist).")

            # Final state
            print("\nFinal Likes:")
            likes = like_logic.get_all_likes()
            for like in likes:
                print(like)

    except Exception as err:
        print(f"Error: {err}")