import mysql.connector
def DataUpdate(FirstName,LastName,Feedback): 
    mydb = mysql.connector.connect( host="localhost", user="root",  
    passwd="Akhila@123", database="Rasa_feedback") 
    mycursor = mydb.cursor() 
    #sql='CREATE TABLE Feedback_rasa_date (firstName VARCHAR(255), lastName VARCHAR(255), feedback VARCHAR(255));'
    sql='INSERT INTO FeedBack_rasa_date (firstName, lastName, feedback) VALUES ("{0}","{1}", "{2}");'.format(FirstName,LastName,Feedback) 
    mycursor.execute(sql) 
    mydb.commit()
    print(mycursor.rowcount,"record inserted")

# if __name__ == "__main__":
#     DataUpdate("Akhila","Saina","best session for rasa chatbot")