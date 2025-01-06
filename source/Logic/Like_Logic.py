from source.Utils.DAL import DAL


class LikeLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_likes(self, vacation_id):
        pass
        query = "SELECT * from mydb.likes"
        result = self.dal.get_table(query)
        return result if result is not None else []

    def is_liked(self, user_id, vacation_id):
        pass

    def add_like(self,Vacations_id, Users_id):
        pass
        try:
            query = """
            INSERT INTO mydb.vacations 
            (vacation_title, desc, start_date, end_date, Countries_id, price, img_url)
            VALUES 
            (%s, %s, %s, %s, (SELECT id FROM mydb.Countries WHERE country_name LIKE %s), %s, %s)
            """
            params = (vacation_title, desc, start_date,
                    end_date, f"%{countries_name}%", price, img_url)
            self.dal.insert(query, params)
            return True
        except Exception as err:
            print(f"Error adding vacation: {err}")
            return False

    def remove_like(self, user_id, vacation_id):
        pass
        query = "DELETE FROM mydb.vacations WHERE id = %s"
        params = (id,)
        try:
            result = self.dal.delete(query, params)
            return True
        except Exception as err:
            print(f"Error deleting vacation: {err}")
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