import cherrypy

def HandleCalculation(num1,num2,operator):
    if (operator == "+"):
        return num1+num2
    if (operator == "-"):
        return num1-num2
    if (operator == "*"):
        return num1*num2
    if (operator == "/"):
        return num1/num2
class Calculator:
    def index(self):
        fx = open("index.html","r")
        webform = fx.read()
        return webform
    index.exposed = True
    def doCalc(self,num1=None,num2=None,select1=None):
        inum1 = int(num1)
        inum2 = int(num2)
        return str(HandleCalculation(inum1,inum2,select1))
    doCalc.exposed = True

cherrypy.quickstart(Calculator())
