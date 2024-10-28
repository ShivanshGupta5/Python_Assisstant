# Python_Assisstant
Voice Assisstant to handle your day to day tasks on your laptop

It does our day to day tasks like web surfing, online shopping, playing songs and much more just by our voice commands

Requirements:
Python 3.8
MySQL Database

Instructions to use the Python Assisstant:
1. git clone
2. cd Python_Assisstant
3. pip install -r requirements.txt
4. install mysql with username as "root" and password as "root@123"
5. create a database: "python_assistant"
6. create a table feedback using the following command in your mysql terminal:
  "create table feedback(Name varchar(30) Primary Key, ContactNumber varchar(10) not Null, MailID varchar(50), Feedback varchar(250) not null);"
7. now run the pythonasst.py python file and enjoy using your Python Voice Assistant
