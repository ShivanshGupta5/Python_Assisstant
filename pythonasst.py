import csv,pickle
import speech_recognition as sr
import pyttsx3 , pywhatkit , datetime , wikipedia , pyjokes , webbrowser
import turtle,pyaudio , time , random , pygame
import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
from translate import Translator
from datetime import date
from playsound import playsound
from pygame import mixer
from tkinter import *

listner=sr.Recognizer()

#Declare voice
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#Python talks the intro
person=input('Kindly Enter your name').title()
speaking="Hi",person," I am python assistant your very own personal virtual assistant"
engine.say(speaking)
engine.say("What can i do for you?")
engine.runAndWait()

#Functions
#1.Snake Game

def score_rec(name,score,mode):    #stores record
    with open("Snake_Game.csv","a",newline = '\r\n') as fp:
        cp = csv.writer(fp)
        if fp.tell( ) == 0:
            cp.writerow(['MODE' , 'NAME' , ' HIGH_SCORE'])
        if mode == 1:
            cp.writerow(['Dancing snake',name.title( ),int(score)])
        elif mode == 2:
            cp.writerow(['Dancing snake Modified',name.title( ),int(score)])

def showscore(Mode,mscore):    #display record
    with open("Snake_Game.csv","r") as fo:
        moderec = []
        modename=[]
        if Mode == 1:
            Modename = 'Dancing snake'
        elif Mode == 2:
            Modename = 'Dancing snake Modified'
        records = csv.reader(fo)
        for rec in records:
            if len(rec) > 0:
                if rec[0] == Modename:
                    moderec.append(int(rec[2]))
                    modename.append(rec[1])
        print("Your Score =",mscore,"Highest score ever acheieved =",max(moderec))
        print("highest acheiver is:",modename[moderec.index(max(moderec))])
                                
def music( ):    #Music selection
    l = ["\nMusic List:" , "Lily" ,"Darkside" , "Play" , "Ignite" , "On my Way" , "Hymn For The Weekend" , "Unity" ,
           "Aurora" ,"Umbrella","Aye Khuda","Gulabi Ankhein","Jai Ho","Soch Na Sake","Battlemusic"]
    for i in l:
        print(i)

    x = input("Enter the name of the song you want to be played in the background(choose from the list above):").title()
    if x in l:
        return x
    else:
        print('Please enter correct name')

def game():    #Main Game Code
    try:
        
        pygame.mixer.init( )
        mixer.music.load('Genshin.mp3')
        mixer.music.play(-1)
        print('*'*30+"WELCOME TO THE SNAKE GAME ZONE"+'*'*30)
        a = input("\nDo you want to start the softare?")
        if a == "yes":
            name = input("Enter your name:")
            print("\nDancing snake (with default setting) ( Enter 1 to choose)")
            print("Dancing snake Modified ( Enter 2 to choose) WARNING if you get out then the controls reverse)\n")
            opt = int(input("\nChoose a mode to play in : "))

            if opt == 1:
                delay = 0.1

                # Score
                score = 0
                high_score = 0
                
                #Snake Body
                se=("square")
                sc=("pink")

                #music
                #music selection
                x = music()
                pygame.mixer.init()
                mixer.music.load('{}.mp3'.format(x.lower()))
                mixer.music.play(-1)

                #setup the screen
                wn = turtle.Screen()
                wn.title("Song currently playing: {}".format(x))
                wn.bgcolor("green")
                wn.setup(width = 600, height = 600)
                wn.tracer(0)                                        #Turns off the screen updates

                #Snake head
                a = ("square")
                b = ("black")
                head = turtle.Turtle()
                head.speed(0)
                head.shape(a)
                head.color(b)
                head.penup()
                head.goto(0,0)
                head.direction = "stop"

                #Snake food
                c = ("circle")
                d = ("red")
                food = turtle.Turtle()
                food.speed(0)
                food.shape(c)
                food.color(d)
                food.penup()
                food.goto(0,100)

                segments = [ ]

                #Pen

                pen = turtle.Turtle( )
                pen.speed(0)
                pen.shape("square")
                pen.color("white")
                pen.penup()
                pen.hideturtle()
                pen.goto(0,260)
                pen.write("Score: 0 High Score: 0", align = "center",font = ("Courier",24,"normal"))

                #Functions
                def go_up( ):
                    if head.direction != "down":
                        head.direction = "up"

                def go_down( ):
                    if head.direction != "up":
                        head.direction = "down"

                def go_left( ):
                    if head.direction != "right":
                        head.direction = "left"

                def go_right( ):
                    if head.direction != "left":
                        head.direction = "right"
                def move( ):
                    if head.direction == "up":
                        y = head.ycor( )
                        head.sety(y+20)

                    if head.direction == "down":
                        y = head.ycor( )
                        head.sety(y-20)

                    if head.direction == "left":
                        x = head.xcor( )
                        head.setx(x-20)

                    if head.direction == "right":
                        x = head.xcor( )
                        head.setx(x+20)

                #Keyboard bindings
                wn.listen(  )
                wn.onkeypress(go_up,"Up")
                wn.onkeypress(go_down,"Down")
                wn.onkeypress(go_left,"Left")
                wn.onkeypress(go_right,"Right")
                       
                #Main Game loop
                while True:
                    wn.update( )
                    #Check for a collision with the border
                    if head.xcor( )>290 or head.xcor( )<-290 or head.ycor( )>290 or head.ycor( )<-290:
                        time.sleep(1)
                        head.goto(0,0)
                        head.direction = "stop"

                        #Hide the segments

                        for segment in segments:
                            segment.goto(2000,20000)

                        #Clear the segments list
                        segments= [ ]
                        #changed this part so that score doesnt become negative after going down to 0
                        # Increase in Score
                        if score > 0:
                            score -= 10             # Same as score = score-10
                        else:   
                            score = 0     
                        if score > high_score:
                            high_score = score
                        pen.clear()
                        pen.write("Score: {} High Score {}".format(score,high_score),align = "center",font = ("Courier",24,"normal"))

                        #Reset the delay
                        delay = 0.1

                    #Check for a collision with the food

                    if head.distance(food) < 20:
                        # Move the food to a random spot
                        x = random.randint(-290,290)
                        y = random.randint(-290,290)
                        food.goto(x,y)

                        #Add a segmet
                        new_segment = turtle.Turtle( )
                        new_segment.speed(0)
                        new_segment.shape(se)
                        new_segment.color(sc)
                        new_segment.penup( )
                        segments.append(new_segment)

                        #Shorten the Delay
                        delay -= 0.001 

                        # Increase in Score
                        score += 10 

                        if score > high_score:
                            high_score = score

                        pen.clear( )
                        pen.write("Score: {} High Score {}".format(score,high_score),align = "center",font = ("Courier",24,"normal"))

                    #Move the segment first in reverse order
                    for index in range (len(segments)-1,0,-1):
                        x = segments[index-1].xcor( )
                        y = segments[index-1].ycor( )
                        segments[index].goto(x,y)

                    #Move segment 0 to where the head is
                    if len(segments) > 0:
                        x = head.xcor( )
                        y = head.ycor( )
                        segments[0].goto(x,y)

                    move( )

                    #Check for head collisions with the body segments
                    for segment in segments:
                        if segment.distance(head) < 20:
                            time.sleep(1)
                            head.goto(0,0)
                            head.direction = "stop"

                            #Hide the segments
                            for segment in segments:
                                segment.goto(1000,1000)

                            #Clear the segments list
                            segments= [ ]
                            
                            #Reset the score
                            score = 0 

                            #Update the score Display
                            pen.clear( )
                            pen.write("Score: {} High Score {}".format(score,high_score),align = "center",font = ("Courier",24,"normal"))

                            #Reset the delay

                            delay = 0.1

                    time.sleep(delay)

                wn.mainloop()


            #Mode 2
            elif opt == 2:
                delay = 0.1

                # Score
                score = 0
                high_score = 0
                
                #Snake Body
                se=("square")
                sc=("pink")

                #music
                #music selection
                x = music( )
                pygame.mixer.init( )
                mixer.music.load('{}.mp3'.format(x.lower( )))
                mixer.music.play(-1)

                #setup the screen
                bgcolour = input("\nEnter background colour(except pink and red)")
                
                wn = turtle.Screen()
                wn.title("Song currently playing: {}".format(x))
                wn.bgcolor(bgcolour)
                wn.setup(width=600, height=600)
                wn.tracer(0)                        #Turns off the screen updates

                #Snake head
                hshape = input("\nEnter the shape of snake's head")
                hcolour = input("\nEnter the colour of snake's head")
                head = turtle.Turtle( )
                head.speed(0)
                head.shape(hshape)
                head.color(hcolour)
                head.penup( )
                head.goto(0,0)
                head.direction = "stop"

                #Snake food
                food = turtle.Turtle( )
                food.speed(0)
                food.shape("circle")
                food.color("red")
                food.penup( )
                food.goto(0,100)

                segments = [ ]

                #Pen
                pen = turtle.Turtle( )
                pen.speed(0)
                pen.shape("square")
                pen.color("white")
                pen.penup( )
                pen.hideturtle( )
                pen.goto(0,260)
                pen.write("Score: 0 High Score: 0", align = "center",font=("Courier",24,"normal"))

                #Functions
                def go_up( ):
                    if head.direction != "down":
                        head.direction = "up"

                def go_down( ):
                    if head.direction != "up":
                        head.direction = "down"

                def go_left( ):
                    if head.direction != "right":
                        head.direction = "left"

                def go_right( ):
                    if head.direction != "left":
                        head.direction = "right"
                        
                def move( ):
                    if head.direction == "up":
                        y = head.ycor( )
                        head.sety(y+20)

                    if head.direction == "down":
                        y = head.ycor( )
                        head.sety(y-20)

                    if head.direction == "left":
                        x = head.xcor( )
                        head.setx(x-20)

                    if head.direction == "right":
                        x = head.xcor( )
                        head.setx(x+20)

                #Keyboard bindings
                wn.listen( )
                wn.onkeypress(go_up,"Up")
                wn.onkeypress(go_down,"Down")
                wn.onkeypress(go_left,"Left")
                wn.onkeypress(go_right,"Right")
                       
                #Main Game loop
                while True:
                    wn.update( )
                    #Check for a collision with the border
                    if head.xcor( )>290 or head.xcor( )<-290 or head.ycor( )>290 or head.ycor( )<-290:
                        time.sleep(1)
                        head.goto(0,0)
                        head.direction = "stop"

                        #Keboard bindings reverse
                        wn.listen( )
                        wn.onkeypress(go_up,"Down")
                        wn.onkeypress(go_down,"Up")
                        wn.onkeypress(go_left,"Right")
                        wn.onkeypress(go_right,"Left")

                        #Hide the segments
                        for segment in segments:
                            segment.goto(2000,20000)

                        #Clear the segments list
                        segments= [ ]
                        
                        #changed this part so that score doesnt become negative after going down to 0
                        # Increase in Score
                        if score > 0:
                            score -= 10             # Same as score = score-10
                        else:   
                            score = 0     
                        if score > high_score:
                            high_score = score
                        pen.clear( )
                        pen.write("Score: {} High Score {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

                        #Reset the delay
                        delay = 0.1

                    #Check for a collision with the food
                    if head.distance(food) < 20:
                        # Move the food to a random spot
                        x = random.randint(-290,290)
                        y = random.randint(-290,290)
                        food.goto(x,y)

                        #Add a segmet
                        new_segment = turtle.Turtle( )
                        new_segment.speed(0)
                        new_segment.shape(se)
                        new_segment.color(sc)
                        new_segment.penup( )
                        segments.append(new_segment)

                        #Shorten the Delay
                        delay -= 0.001 

                        # Increase in Score
                        score += 10 

                        if score > high_score:
                            high_score = score

                        pen.clear( )
                        pen.write("Score: {} High Score {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

                    #Move the segment first in reverse order
                    for index in range (len(segments)-1,0,-1):
                        x = segments[index-1].xcor( )
                        y = segments[index-1].ycor( )
                        segments[index].goto(x,y)

                    #Move segment 0 to where the head is
                    if len(segments) > 0:
                        x = head.xcor( )
                        y = head.ycor( )
                        segments[0].goto(x,y)

                    move( )

                    #Check for head collisions with the body segments
                    for segment in segments:
                        if segment.distance(head) < 20:
                            time.sleep(1)
                            head.goto(0,0)
                            head.direction = "stop"

                            #Hide the segments
                            for segment in segments:
                                segment.goto(1000,1000)

                            #Clear the segments list
                            segments= [ ]
                            
                            #Reset the score
                            score = 0

                            #Update the score Display
                            pen.clear( )
                            pen.write("Score: {} High Score {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

                            #Reset the delay
                            delay = 0.1
                            
                    time.sleep(delay)

                wn.mainloop( )
               
            else:
                print("{} mode does not exists\nPlease enter a valid number".format(b))
                
        else:
            mixer.music.stop( )
            
    except:
        mixer.music.stop()
        print("\nYour High Score =",high_score)
        print("Your final score is:",score)
        print("\n\n")
        score_rec(name, high_score,opt)
        showscore(opt,high_score)
        pass

#2.COVID PROJECT
def covid__():
    #Format data stored in Binary File
    #dict->{ state : [ capital , total confirmed cases , death ] }

    def mod():
        print()
        print('what do you want to change?\n1.number of deaths\n2.total confirmed cases')
        print()

        a = int(input('enter your choice?'))

        x = False
        fp = open("CovidDATA.dat","r+b")
        try:
            while True:
                position = fp.tell()
                dic = pickle.load(fp)
                if a == 1:
                    st=input('enter the state name').title()
                    new=int(input('enter the new value:'))
                    print()

                    if st in dic:
                        values = dic[st]
                        values[2] = new

                        fp.seek(position)
                        pickle.dump(dic,fp)
                        print('Data Updated!')
                        found = True

                    else:
                        print("State not found")

                elif a == 2:
                    st=input('enter the state name').title()
                    new=int(input('enter the new value:'))
                    print()

                    if st in dic:
                        values = dic[st]
                        values[1] = new

                        fp.seek(position)
                        pickle.dump(dic,fp)
                        print('Data Updated!')
                        found = True

                    else:
                        print("State not found")

        except:
            fp.close()
           
    def search():
        print()
        st = input('enter the state name you want to search:').title()

        fp = open("CovidDATA.dat","rb")
        try:
            print("Searching....")
            while True:
                dic = pickle.load(fp)
                if st in dic:
                    value = dic[st]
                    print(st)
                    print("Capital:",value[0])
                    print("Total Confirmed Cases:",value[1])
                    print("Deaths:",value[2])
                    
                    #graph
                    x = ['Confirmed Cases' , 'Death Rate']
                    y = [value[1],value[2]]
                    plt.bar(x,y)
                    plt.xlabel('x-axis')
                    plt.ylabel('y-axis')
                    plt.title('Graphical Representation')
                    plt.grid()
                    plt.show()

                else:
                    print("State not found")

        except:
            print()
            fp.close()

    def  display():
        key=[]
        val1=[]
        val2=[]

        fp = open("CovidDATA.dat","rb")
        state = pickle.load(fp)
        for x,y in state.items():
            key.append(x)
            val1.append(y[1])
            val2.append(y[2])

        #graph on total cases
        y = val1
        labels = key
        plt.pie(y, labels = labels)
        plt.legend(title = "Total Confirmed Cases:")
        plt.show()

        #graph on total death
        x=key
        y=val2
        plt.barh(x, y,color = 'purple')
        plt.title('Death Rate')
        plt.show()

    while True:

        print('1.Modify any previous data')
        print('2.Search for any state')
        print('3.Show all data')
        print('4.Show dicticionary')
        print('5.Exit')
        print()
        x=int(input('enter your choice:'))
        print()

        if x == 1:
            mod()

        elif x == 2:
            search()

        elif x == 3:
            display()

        elif x == 4:
            with open("CovidDATA.dat" , "rb") as fp:
                dic_state = pickle.load(fp)
                print(dic_state)
                print()

        elif x==5:
            break

        else:
            print('enter the valid number')
            
#3. MYSQL Database Functions
def insert( ):    #Inserting feedback data into mysql table
    print( "**************************FEEDBACK FORM**************************" )
    print( '''THANKYOU FOR USING OUR PYTHON ASSISTANT.
                        WE HOPED YOU LIKED AND ENJOYED IT.HERE IS A SHORT FEEDBACK FORM WHICH
                        WOULD HELP US IMPROVE IT''' )
    db = mysql.connector.connect(host = "localhost", user = "root", passwd = "root@123", database = "python_assistant")
    cur = db.cursor( )
    
    cur.execute( "select * from feedback" )
    no = len(cur.fetchall())
    
    name = str(no+1) + '. ' + person
    conno = int(input("Kindly enter you contact number:"))
    email = input("Enter you email address:")
    feedback = str(no+1) +':' + input("Enter your feedback:")
    cmd =  cur.execute(f"insert into FEEDBACK VALUES('{name}' , {conno} , '{email}' , '{feedback}') ")

    cur.execute(cmd)
    db.commit( )
    db.close( )
    
def output( ):              #Showing all the records of the feeback table
    
    user = username.get( )
    passw = password.get( )
    try:
        db = mysql.connector.connect( host = "localhost" , user = user , password = passw , db = "python_assistant")

    except:
        row3 = tk.Label(win1, text = "Incorrect username or password...", font = ("Helvetica",10), bg = 'white',fg = 'red' )
        row3.place(x = 30, y = 90, width = 250)
        win1.mainloop()
    else:
        win2 = tk.Tk( )
        win2.geometry("5000x400")
        cur = db.cursor()

        cur.execute( "select * from feedback" )
        records=cur.fetchall()
        db.close( )
        
        i = 0
        for data in records : 
            for j in range(len(data)) :
                put=data[j]
                e = tk.Entry(win2,width=25, text = data[j] , font = ("Helvetica",22), bg = 'purple' , fg = 'yellow') 
                e.grid(row = i, column = j) 
                e.insert(END, put)
            i = i + 1
        win2.mainloop( )
    

#4. Python Assistant Functions
def talk(text):    # Talk function for Python Assistant
    engine.say(text)
    engine.runAndWait( )

def take_command( ):    # Take command function for taking voice commands in Python Assistant
    try :
    # Python listens
        with sr.Microphone( ) as source :
            print( "\nListening..." )
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower( )
            
            today = date.today( )
            d1 = today.strftime( "%d %m %Y" )

            time = datetime.datetime.now( ).strftime( '%I:%M %p' )
            
            if 'python' in command :
                with open( "python_history.txt" , "a" ) as fp:
                    fp.write(d1 + '  :  ' + time + "\n")
                    fp.write( command + "\n" )
                    fp.write("\n")
                command = command.replace( 'python ' , '')              
                
                print(command)
                return command

    except :
        return None

# Doing work with Python Assistant
while True:
    command = take_command( )
    if command == None :
        continue
    
    if ( 'play' or 'song' ) in command :
        song = command.replace( 'play ' , '' )
        print( "The song" , song , "is being played" )
        talk( 'playing' + song )
        pywhatkit.playonyt(song)
        input( "Press enter to continue" )

    elif 'time' in command :
        time = datetime.datetime.now( ).strftime( '%I:%M %p' )
        talk( 'Current time is ' + time )
        print(time)

    elif 'date' in command :
        today = date.today( )
        d1 = today.strftime( "%d %m %Y" )
        print(d1)
        talk(d1)

    elif ( 'search' or 'find' ) in command :
        person = command.replace( 'search' , '' )
        info = wikipedia.summary(person , 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        x = pyjokes.get_joke( )
        talk(x)
        print(x)

        
    elif 'game' in command :
        game( )

    elif 'report' in command :
        covid__( )

    elif ( 'translate' or 'translator' ) in command :
        print("Opening the webpage for you to refer to the codes for specific language")
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")
        text = input( 'Enter the text:' )
        org = input( 'Enter the language of the text:' ).lower( )
        conv = input( 'Enter the language you want to convert the text into:' ).lower( )
                     
        translator = Translator( from_lang = org , to_lang = conv )
        translation = translator.translate( text )
        print( translation )

    elif 'history' in command :
        with open( "python_history.txt" , "r" ) as fp :
            a = input("Would you like to read or listen the history ?" )
            a.lower( )
            if a == 'read' :
                print(fp.read( ))
            else :
                talk(fp.read( ))

    elif ( 'introduce' or 'introduction' ) in command :
        with open( "introduction.txt" , "r" ) as fd :
            talk(fd.read( ))

    elif 'database' in command :
        win1 = tk.Tk( )
        win1.geometry( "300x250" )
        win1.title( "MySQL Login Page" )

        # Defining the first row
        row1 = tk.Label(win1, text = "Username :", font = ("Helvetica",10), bg = 'white',fg = 'black' )
        row1.place( x = 50, y = 20 )

        username = tk.Entry(win1, width = 35)
        username.place(x = 150, y = 20, width = 100)

        row2 = tk.Label(win1, text = "Password :" , font = ("Helvetica",10) , bg = 'white',fg = 'black')
        row2.place(x = 50, y = 50)

        password = tk.Entry(win1, width = 35)
        password.place(x = 150, y = 50, width = 100)
        loginbutton = tk.Button(win1, text ="Login",bg ='red', command = output)
        loginbutton.place(x = 130, y = 135, width = 55)
        win1.mainloop()


    elif 'over' in command :
        talk( "Thankyou, it was great talking to you. Hope to meet you soon. Please fill up the feedback from also" )
        ask=input(" Have you filled the feedback form before?(Yes/No)")
        if ask.lower() in ['n','no']:
            insert()
            
        else:
            pass
        break

    else:
        talk('Sorry,can you repeat')

    print("\n\n----------*****----------")
