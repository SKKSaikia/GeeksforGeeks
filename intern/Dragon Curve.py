#import the turtle module to use turtle graphics
import turtle

#make variables for the right and left containg 'r' and 'l'
#not really necesessary, but may held understanding
r = 'r'
l = 'l'

#assign our first iteration a right so we can build off of it
old = r
new = old

#input the user's desired iteration, segment length, pen color
#and background color
iteration=int(input('Enter iteration:'))
length=int(input('Enter length of each segment:'))
pencolor=input('Enter pen color:')
bgcolor=input('Enter background color:')

#set the number of times we have been creating the next iteration as the first
cycle=1

#keep on generating the next iteration until desired iteration is reached
while cycle<iteration:

    #add a right to the end of the old iteration and save it to the new
    new = (old) + (r)

    #flip the old iteration around(as in the the first charicter becomes last)
    old = old[::-1]

    #cycling through each character in the flipped old iteration:        
    for char in range(0,len(old)):
        #if the character is a right:
        if old[char] == r:
            #change it to a left
            old = (old[:char])+ (l) + (old[char+1:])
        #otherwise, if it's a left:
        elif old[char] == l:
            #change it to a right
            old = (old[:char]) + (r) + (old[char+1:])

    #add the modified old to the new iteration
    new = (new) + (old)
    #save the new iteration to old as well for use next cycle
    old = new

    #advance cycle variable to keep track of the number of times it's been done
    cycle=cycle+1

#input, whether or not to display the r and l form of the iteration
printans=input('Display r/l form?(y/n):')
#if yes, print the iteration
if printans=='y':
    print(new)

#prepare to display the graphics
#do not show the turtle icon when drawing
turtle.ht()
#set drawing speed to fastest(no animation)
turtle.speed(0)
#set pen color as requested
turtle.color(pencolor)
#set background color as requested
turtle.bgcolor(bgcolor)

#display segment of desired length to build off of
turtle.forward(length)

#cycling through all the characters in the iteration
for char in range(0,len(new)):
    #if the character is a right:
    if new[char] == (r):
        #turn right at a right angle 
        turtle.right(90)
        #go forward desired length
        turtle.forward(length)
    #otherwise, if the character is a left:
    elif new[char] == (l):
        #turn left at a right angle
        turtle.left(90)
        #go forward desired length
        turtle.forward(length)
