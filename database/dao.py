from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def leggiConnessioni(year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary = True)
        query = """ SELECT id_rifugio1, id_rifugio2
                    FROM connessione c
                    WHERE c.anno <= %s """
        cursor.execute(query, (year,))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def trovaPeso(diz): # diz è un dizionario connessione di due rifugi {'id_rifugio1': 1, 'id_rifugio2': 2}
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT distanza, difficolta
                    FROM connessione c
                    WHERE c.id_rifugio1 = %s and c.id_rifugio2 = %s """
        cursor.execute(query, (diz["id_rifugio1"], diz["id_rifugio2"],))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        for d in result:
            if d["difficolta"] == "facile":
                peso = float(d["distanza"])*1
            elif d["difficolta"] == "media":
                peso = float(d["distanza"])*1.5
            elif d["difficolta"] == "difficile":
                peso = float(d["distanza"])*2
        return peso