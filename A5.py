import random
from urllib import response

name="Bot Chatty"
mood="Smiley"
season="rainy"
food=['fries','pizza']
resp={
    'What is your name':[
        "They call me {0}".format(name),

    ],
    "what is season it is?" :
    ["it is {0}".format(mood),]
    }
    
def res(message):
    if message in resp:
        x=random.choice(resp[message])
    else :
        x=random.choice(resp[message])
    return x

def real(xtext):
    if "name" in xtext:
        ytext="What is your name?"
    return ytext
def sendmsg(message):
    print((message))
    response=res(message)
    print((response))

while 1:
    my_input = input("Enter your message: ") 
    my_input = my_input.lower() 
    if my_input == "exit" or my_input == "stop": 
        break
    related_text = real(my_input) 
    sendmsg(related_text)
    