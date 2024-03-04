import sqlite3 as lite

#backpack
# ORDER BY RANDOM() LIMIT 5 - SQL COMMAND NEEDED TO RANDOMISE QUESTIONs

connectedDatabase = lite.connect("QuestionAndAnswers.db")
current = connectedDatabase.cursor()
current.execute("CREATE TABLE Questions(Topic STR, QuestionPath STR, AnswerPath STR)")

QuestionID = 0
TopicList1 = ["Algorithm"]
TopicList = ["Cyber Security", "Data Representation", "Ethics", "Hardware", "Networks", "Programming"]




for Topic in TopicList1:
    for i in range(1,5):
        QuestionID += 1
        question = f"question{i}"
        answer = f"answer{i}"
        current.execute(f"INSERT INTO Questions VALUES('{str(Topic)}','QuestionSet?{str(Topic)}?{str(question)}.png','QuestionSet?{str(Topic)}?{str(answer)}.png')")
        #QuestionSet\Algorithm\Question\Question1.png

for Topic in TopicList:
    for i in range(1,6):
        QuestionID += 1
        question = f"question{i}"
        answer = f"answer{i}"
        current.execute(f"INSERT INTO Questions VALUES('{str(Topic)}','QuestionSet?{str(Topic)}?{str(question)}.png','QuestionSet?{str(Topic)}?{str(answer)}.png')")
        #QuestionSet\Algorithm\Question\Question1.png

connectedDatabase.commit()