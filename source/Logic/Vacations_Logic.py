from source.Utils.DAL import DAL
from source.Logic.Like_Logic import LikeLogic

class VacationLogic:
    def __init__(self):
        self.dal = DAL()
        self.like_logic = LikeLogic()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_vacations(self):
        query = "SELECT * from mydb.vacations"
        result = self.dal.get_table(query)
        return result if result is not None else []

    def get_all_vacations_liked_by_uid(self, user_id):
        query = """
        SELECT vacations.*
        FROM vacations
        JOIN likes ON vacations.id = likes.Vacations_id
        WHERE likes.Users_id = %s
        """
        params = (user_id,)
        return self.dal.get_table(query, params) or []


    def get_vacation(self, id):
        query = "SELECT * from mydb.vacations WHERE id = %s"
        result = self.dal.get_scalar(query,(id,))
        return result if result is not None else []


    def add_vacation(self, vacation_title, desc, start_date, end_date, countries_name, price, img_url):
        try:
            query = """
            INSERT INTO mydb.vacations 
            (vacation_title, description, start_date, end_date, Countries_id, price, img_url)
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

    def edit_vacation(self, id, **kwargs):
        if not kwargs:
            return False

        clause = ", ".join([f"{k} = %s" for k in kwargs.keys()])

        params = tuple(kwargs.values()) + (id,)
        query = f"UPDATE mydb.vacations SET {clause} WHERE id = %s"

        try:
            self.dal.update(query, params)
            return True
        except Exception as e:
            print(f"Error updating vacation: {e}")
            return False

    def del_vacation(self, id):    
        params = (id,)
        try:
            with LikeLogic() as like_logic:
                like_logic.delete_all_likes_from_vacation(id)
            query = "DELETE FROM mydb.vacations WHERE id = %s"
            result = self.dal.delete(query, params)
            return True
        except Exception as err:
            print(f"Error deleting vacation: {err}")
            return False

if __name__ == "__main__":
    try:
        with VacationLogic() as vacation_logic:
            vacations = vacation_logic.get_all_vacations()
            for vacation in vacations:
                 print("----------------------")
                 print(vacation)
            # print(vacation_logic.get_vacation())
    except Exception as err:
        print(f"Error: {err}")