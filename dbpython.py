'''database connetion '''
#import mysql.connector  # import mysql connector
mydb = mysql.connector.connect(  #create connection
    host="localhost",   #host
    user=" root",  #username 
    passwd="root",  #password 
    database=" provapy "  #database name
)
mycursor = mydb.cursor()  #create cursor
