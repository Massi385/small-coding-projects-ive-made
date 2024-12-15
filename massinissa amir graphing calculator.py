from graphics import *


import math

import tkinter as tk





####### graphing calcultor made by massinissa amir

#instructions

## enter ur function in the function textbox
# enter desired domain and range
#and hit calculate to generate a window of your function




#other stuff

# currently the grid only goes up to units of 100, so if you have a domain
# or range of like 100,000 its gonna write like 100 numbers thats something
# i plan to fix in the future







#function read

# ########this code will take the function and calculate it

def functionread(function):
    #print("go")
    #print(function)
    #######   take the function and turn it into an array of math signs and numbers

    # function string is "5+3^2+7/1
    #an list will be created , array = [5, '+' ,3 , '^' , 2 , '+' , 7 , '/' , 1  ]

    array = []



    #######this part of code will find parenthesis. if it finds '('
    # we start from back of function string to find ')'

    #then we have the position of the leftmost '(' and rightmost ')' which presumably connect to eachtother

    #we take the string in this parenthesis and run it through this funciton to solve it.

    #take that value we solved and replace the string between ( and ) with it. include the (  )


    
    x = 0


    while x < len(function):

        char = function[x:x+1]
        
        # x equal position of '('

        
        #  ( 5 + 3 * ( 18 )  ) 
        if char == '(':
                       
            x2 = x +1

            withinparenthesiscounter = 0

            while x2 < len(function):


                #were looking for ')' to match '(' but there may be a parenthesis inside of this one
                #were gonna count how many '(' we see. this count will be equal to how many ')' we ignore
                
                char2 = function[x2:x2+1]


                if char2 == '(':
                    withinparenthesiscounter += 1


                
                if char2 == ')':

                    if withinparenthesiscounter == 0:
                        break
                    else:
                        withinparenthesiscounter -= 1
                        
    
                x2 += 1
    




            parenthesissolve= functionread(function[x+1:x2])

            if parenthesissolve == 'e':
                return 'e'

            #print(parenthesissolve)
            #i make x go down 3 because -- look down

            if function[x-3:x] == 'sin':
                parenthesissolve = math.sin(parenthesissolve)
                x = x -3

            if function[x-3:x] == 'cos':
                parenthesissolve = math.cos(parenthesissolve)
                x = x -3

            if function[x-3:x] == 'tan':
                parenthesissolve = math.sin(parenthesissolve)
                x = x -3

            if function[x-3:x] == 'exp':
                parenthesissolve = math.exp(parenthesissolve)
                x = x -3                

            if function[x-4:x] == 'sqrt':
                parenthesissolve = math.sqrt(abs(parenthesissolve))
                x = x -4                  

           


            # in this line of code were cutting out the parenthesis and putting in the str of the int of the calculated value we got from the string in the parenthesis
            # if tehres a sin or sqrt ect we need to cut that out as well so we go 3 or 4 back for that
            

            function = function[:x] + str(parenthesissolve) + function[x2+1:]
            
            #print(function)

            
            

            x=0      

        

    


        x += 1



 
        









    

    x = 0


    while x < len(function):


        char = function[x:x+1]

        if char.isdigit() == False and char != '.':

            if x != 0 and function[:x] != 'e':
                array.append( float( function[:x]     ))
            array.append(char)
            function = function[x+1:]

            x = 0
            



        x += 1


    if function != '':
        array.append(float(function))

  

    

    x = 0

    while x < len(array):

        char = array[x]


        if char == '+' or char == '-':
            
            array[x+1] = char + str(array[x+1])

            array[x+1] = array[x+1].replace("+-",'-')
            array[x+1] = array[x+1].replace("--",'-')
            
            array[x+1] = float(array[x+1])

            array.pop(x)



        x += 1   

 
    


    


    ##### filter the power signs, if item in araryis '^'. make a calculation for the item before that power the item after
    #then replace those 3 items with that number we calculated
    ###  [ '+',5,'^',2] becomes ['+',25]

    # does the same with / and *


    

    x = len(array) - 1

    while x >= 0:
        
        thing = array[x]

        if thing == '^':
            num = array[x-1] ** array[x+1]

            array[x] = num

            array.pop(x-1)
            array.pop(x)
            
        x -=1
        
        

    x = len(array) - 1

    while x >= 0:
        thing = array[x]
        if thing == '*':
            num = array[x-1] * array[x+1]

            array[x] = num

            array.pop(x-1)
            array.pop(x)

        x -= 1


    x = len(array) - 1

    while x >= 0:
        thing = array[x]
        if thing == '/':
            num = array[x-1] / array[x+1]

            array[x] = num

            array.pop(x-1)
            array.pop(x)

        x -= 1


    #same thing for multiply


    y = 0

    x = 0
    sign = '+'

    
    while x < len(array):

        thing = array[x]

        if thing == '+':
            sign = '+'

        if thing == '-':
            sign = '-'
            

    
        if 'e' in str(thing) or 'j' in str(thing):
            return 'e'

        if thing != '+' and thing != '-':
            
            if sign == '-':
                y -= thing
                
            if sign == '+':
                y += thing
        x+= 1



    return(y)


############## end of functionreader function













#function draw 


###### functiondrawer function starts here  ###################

def drawfunction(xdomain,yrange,function):

    
    #these numbers are the height and width of the graph or the domain and range

    xdomain = int(xdomain)
    yrange = int(yrange)

    #create window, it will be named the same as function so you can have multiple open and be organized
    win = GraphWin(function, 500, 500)
    
    function.replace(" ","")

    savefunction = function



    

    ######################################### this part of code draws numbers on the graph grid   ########################
    x = 0
    point = (x,250)


    # this part of code is for x line grid, to draw numbers on it

    #theres multiple versions that are dependant on the set domain of the user

    #this is because the amount of numbers on the grid needs to be balanced relative
    #to the size of the screen

    #for example, if the user has a domain of 1000, we cant draw a point for every 10 or every 1
    #if the users domain is less than 20 it makes a point for every 1 unit in the graph


    if xdomain <= 20:

        #give us the domain remainder, this is so the points start at an even value
        # for example, if the domain was 307, were gonna make a point for every ten units on the grid
        #but we need to start from 300, to get 300 we do remainder of 307 / 10 
        ones = xdomain % 1

        x = -(xdomain - ones)

        
        #it will loop from negative to positive incrementaly increasing by whatever unit were using
        #a small circle and a text that says the number is drawn on each one
        while x < (xdomain - ones):
            point = Point((x / xdomain ) * 500 + 250,  250)
            point.draw(win)

            circle = Circle(point,1)
            circle.draw(win)

            message = Text(Point( (x / xdomain ) * 500 + 250   ,245),x )
            message.setSize(7)
            message.draw(win)
            x+= 1





    # the same thing but for 10s and 100s is below



    elif xdomain <= 400:
        tens = xdomain % 10

        x = -(xdomain - tens)

        while x < (xdomain - tens):
            point = Point((x / xdomain ) * 500 + 250,  250)
            point.draw(win)

            circle = Circle(point,1)
            circle.draw(win)
            
            message = Text(Point( (x / xdomain ) * 500 + 250   ,245),x )
            message.setSize(7)
            message.draw(win)

            x+= 10


    else:
        
        hundreds = xdomain % 100

        x = -(xdomain - hundreds)

        while x < (xdomain - hundreds):
            point = Point((x / xdomain ) * 500 + 250,  250)
            point.draw(win)

            circle = Circle(point,1)
            circle.draw(win)
            
            message = Text(Point( (x / xdomain ) * 500 + 250   ,245),x )
            message.setSize(7)
            message.draw(win)

            x+= 100




    # we do the same thing but for y axis


    if yrange <= 20:


        ones = yrange % 1

        y = -(yrange - ones)


        while y < (yrange - ones):

            if y == 0:
                y += 1
                continue
            point = Point(   250   ,      - (   (y / yrange) * 500) + 250        ) 
            point.draw(win)

            circle = Circle(point,1)
            circle.draw(win)

            message = Text( Point( 260   ,   - (   (y / yrange) * 500) + 250  )   ,  y  )
            message.setSize(7)
            message.draw(win)
            y+= 1




    elif yrange <= 400:

     
        tens = yrange % 10

        y = -(yrange - tens)

        
      
        while y < (yrange - tens):

            if y == 0:
                y += 10
                continue
            point = Point(   250   ,      - (   (y / yrange) * 500) + 250        ) 
            point.draw(win)

            circle = Circle(point,1)
            circle.draw(win)

            message = Text( Point( 260   ,   - (   (y / yrange) * 500) + 250  )   ,  y  )
            message.setSize(7)
            message.draw(win)
            y+= 10

    else:

     
        hundreds = yrange % 10

        y = -(yrange - hundreds)

        
      
        while y < (yrange - hundreds):

            if y == 0:
                y += 100
                continue
            point = Point(   250   ,      - (   (y / yrange) * 500) + 250        ) 
            point.draw(win)

            circle = Circle(point,1)
            circle.draw(win)

            message = Text( Point( 260   ,   - (   (y / yrange) * 500) + 250  )   ,  y  )
            message.setSize(7)
            message.draw(win)
            y+= 100




    ############################ this is where the numbers being drawn on grid part ends ####################










    ##### # # # # ## #draw the lines showing quadrants of the graph  / it draws the line that shows the x axis and y axis


    point = Point(250,0)

    point2 = Point(250,500)

    line = Line(point,point2)

    line.setOutline("#808080")


    line.draw(win)

    point = Point(0,250)

    point2 = Point(500,250)

    line = Line(point,point2)
    line.setOutline("#808080")
    line.draw(win)

    ######## end of part drawing line of quadrants 

    x = - (xdomain / 2)

    point1 = Point(0,0)
     
    point2 = point1

    while x < (xdomain / 2):


        
        function = function.replace("x",str(x))

        #print(function)

        y = functionread(function)

        

        if y == 'e':
            x += xdomain / 500
            function = savefunction
           
            continue


        #print(y)

        point1 = point2
        
        point2 = Point((x / xdomain ) * 500 + 250,  - (   (y / yrange) * 500) + 250)

        line = Line(point1,point2)

        
        line.draw(win)
        
        #point1.draw(win)


        

        function = savefunction


     
        x += xdomain / 500

###### function drawer function ends here



















# user interface gui



#when a button is clicked this will run, it goes to the function draw function with data for the function, domain, and range
def graphbutton_clicked():
    drawfunction(xdomainentry.get() , yrangeentry.get(), entry.get() )

    
# Create the main window
window = tk.Tk()


window.title("massi graphing calculator")  
window.geometry("400x300")  


label = tk.Label(
    window,
    text="function",

)

# Create an entry widget
entry = tk.Entry(
    window,
    
    )



xdomainlabel = tk.Label(
    window,
    text="x domain"
    )

xdomainentry = tk.Entry(
    window,   
    )

xdomainentry.insert(0,"100")



yrangelabel = tk.Label(
    window,
    text="y range"
    )

yrangeentry = tk.Entry(
    window,   
    )
yrangeentry.insert(0,"100")


#set locations for all the textboxes and labels above them
label.grid(row=0, column=0, padx=20, pady=5) 
entry.grid(row=1, column=0, padx=20, pady=5)


xdomainentry.grid(row=1, column=2, padx=20, pady=2)
xdomainlabel.grid(row=0, column=2, padx=20, pady=2)
yrangeentry.grid(row=5, column=2, padx=20, pady=2)
yrangelabel.grid(row=4, column=2, padx=20, pady=2)

#this creats the button and grid has the position for it
graphbutton = tk.Button(
    window,
    text="draw graph",
    width=25,
    height=5,
    bg="white",
    fg="black", 
    command = graphbutton_clicked # this makes the code go to the button clicked function
)

graphbutton.grid( row=500,column=2,padx=1, pady=50      )







# Start the Tkinter event loop
window.mainloop()



















