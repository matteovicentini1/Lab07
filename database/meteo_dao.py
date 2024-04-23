from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                        FROM situazione s 
                        ORDER BY s.Data ASC"""
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Tmedia"],
                                         row["Tmin"],
                                         row["Tmax"],
                                         row["Puntorugiada"],
                                         row["Umidita"],
                                         row["Visibilita"],
                                         row["Ventomedia"],
                                         row["Ventomax"],
                                         row["Raffica"],
                                         row["Pressioneslm"],
                                         row["Pressionemedia"],
                                         row["Pioggia"],
                                         row["Fenomeni"]))
            cursor.close()
            cnx.close()
        return result


