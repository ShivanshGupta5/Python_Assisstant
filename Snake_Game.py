import csv
import pygame
from pygame import mixer
import turtle
import time
import random
#Functions


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
        
def score_rec(name,score,mode):    #stores record
    with open("Snake_Game(1).csv","a",newline = '\r\n') as fp:
        cp = csv.writer(fp)
        if fp.tell( ) == 0:
            cp.writerow(['MODE' , 'NAME' , ' HIGH_SCORE'])
        if mode == 1:
            cp.writerow(['Dancing snake',name.title( ),int(score)])
        elif mode == 2:
            cp.writerow(['Dancing snake Modified',name.title( ),int(score)])

def showscore(Mode,mscore):    #display record
    with open("Snake_Game(1).csv","r") as fo:
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
