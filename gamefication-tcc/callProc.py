import pymysql
import pymysql.cursors
databaseCharset = "utf8mb4"
# objetivando iniciar procedures que atualizarao o banco de dados

cusrorType = pymysql.cursors.DictCursor

databaseConnection = pymysql.connect(host='url host',
                                     user="login",

                                     password="senha",

                                     db="banco de dados",

                                     charset=databaseCharset,

                                     cursorclass=cusrorType)
try:

    # Cursor object creation

    cursorObject = databaseConnection.cursor()

    # Execute the sqlQuery

    cursorObject.execute("call 1extrigger()")
    databaseConnection.commit()
    print("executou a primeira do dia")

    cursorObject.execute("DELETE FROM resultado WHERE 1")
    cursorObject.execute("call 2gamefica_calcula()")
    cursorObject.execute("call 	3gamefica_pontua()")
    databaseConnection.commit()
    print("eita, rodou metade")

    cursorObject.execute("call 	resultado_identifica_por_cpf()")
    cursorObject.execute("DELETE FROM rankings WHERE 1")
    cursorObject.execute("call joga_dados_ranking()")
    # so far taking 9 to 10 min
    databaseConnection.commit()

    print("sera q rodou mesmo?")

    # Print the result of the executed stored procedure

    for result in cursorObject.fetchall():

        print(result)


except Exception as e:

    print("Exeception occured:{}".format(e))


finally:

    databaseConnection.close()

print("did dis shid worked at all?")
