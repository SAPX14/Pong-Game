import turtle

gameWin = turtle.Screen()
gameWin.title("SAPX14's Pong Game")
gameWin.bgcolor(0,0,0)
gameWin.setup(width=800 ,height=600)
gameWin.tracer(0) 

# Striker A
strikerA = turtle.Turtle()                       # initializes the object in Turtle class
strikerA.speed(0)                                # this is NOT FOR SPEED OF STRIKER , this is for speeding up the game
strikerA.shape("square")                         # makes the shape of object as square
strikerA.color("white")                          # object color set to white
strikerA.shapesize(stretch_wid=5 ,stretch_len=1) # this is used to edit the shape by multiplying the pixels
strikerA.penup()                                 # pendown traces the path of object and draws line , so penup used
strikerA.goto(-350 ,0)                           # (0,0) is centre of screen, so this places object at centre left

# Striker B
strikerB = turtle.Turtle()                       # initializes the object in Turtle class
strikerB.speed(0)                                # this is NOT FOR SPEED OF STRIKER , this is for speeding up the game
strikerB.shape("square")                         # makes the shape of object as square
strikerB.color("white")                          # object color set to white
strikerB.shapesize(stretch_wid=5 ,stretch_len=1) # this is used to edit the shape by multiplying the pixels
strikerB.penup()                                 # pendown traces the path of object and draws line , so penup used
strikerB.goto(350 ,0)                           # (0,0) is centre of screen, so this places object at centre right

# ball
ball = turtle.Turtle()                       # initializes the object in Turtle class
ball.speed(0)                                # this is NOT FOR SPEED OF CIRCLE , this is for speeding up the game
ball.shape("circle")                         # makes the shape of object as circle
ball.color("white")                          # object color set to white
ball.penup()                                 # pendown traces the path of object and draws line , so penup used
ball.goto(0 ,0)                              # positions the ball at centre of screen
ball.dx = 0.5                                  # change in position of ball by 2 pixels , dx represents change
ball.dy = -0.5                                  # change in position of ball by 2 pixels , dy represents change

# Score 
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A : 0   Player B : 0" , align="center" , font=("courier",24 ,"normal"))
score_a = 0
score_b = 0

# Upward movement dynamics of Striker A
def strikerA_up():
    y = strikerA.ycor()                      # collects the current y coordinate  
    y += 20                                  # increment operator of y coordinate
    strikerA.sety(y)                         # inputs the updated coordinate in variable y

# Downward movement dynamics of Striker A
def strikerA_down():
    y = strikerA.ycor()
    y -= 20
    strikerA.sety(y)     

# Upward movement dynamics of Striker B
def strikerB_up():
    y = strikerB.ycor()
    y += 20
    strikerB.sety(y) 

# Downward movement dynamics of Striker B
def strikerB_down():
    y = strikerB.ycor()
    y -= 20
    strikerB.sety(y)         

# Keyboard binding (making keys responsive to use and interact with game)   
gameWin.listen()
gameWin.onkeypress(strikerA_up ,"w") 
gameWin.onkeypress(strikerA_down ,"s") 
gameWin.onkeypress(strikerB_up ,"Up") 
gameWin.onkeypress(strikerB_down ,"Down")

# Main game loop
run = True
while run:
    gameWin.update() 

    # movement of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 

    # border control (to stop objects from moving outside screen)
    if ball.ycor() > 290 :
        ball.sety(290) 
        ball.dy *= -1
    if ball.ycor() < -290 :
        ball.sety(-290) 
        ball.dy *= -1
    if ball.xcor() > 390 :
        ball.goto(0,0) 
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A : {}   Player B : {}".format(score_a,score_b) , align="center" , font=("courier",24 ,"normal"))

    if ball.xcor() < -390 :
        ball.goto(0,0) 
        ball.dx *= -1 
        score_b += 1
        score.clear()
        score.write("Player A : {}   Player B : {}".format(score_a,score_b) , align="center" , font=("courier",24 ,"normal"))
    
    if (score_a >= 15 or score_b >= 15) :
        score.clear()
        gameOver = turtle.Turtle()
        gameOver.speed(0)
        gameOver.color ("red")
        gameOver.penup()
        gameOver.hideturtle()
        gameOver.write("GAME OVER" ,align="center" ,font=("arial",64) )
        ball.goto(0,700)
        if score_a > score_b :
            win = turtle.Turtle()
            win.speed(0)
            win.color("white")
            win.penup()
            win.hideturtle()
            win.goto(0,220)
            win.write("Player A wins!" , align="center" , font=("arial",48))
        else :
            win = turtle.Turtle()
            win.speed(0)
            win.color("white")
            win.penup()
            win.hideturtle()
            win.goto(0,220)
            win.write("Player B wins!" , align="center" , font=("arial",48))    

    # Ball and Striker collision
    if (ball.xcor() > 340 and ball.xcor() < 350)and(ball.ycor() < strikerB.ycor()+50 and ball.ycor() > strikerB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1     
        
    if (ball.xcor() < -340 and ball.xcor() > -350)and(ball.ycor() < strikerA.ycor()+50 and ball.ycor() > strikerA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1     
