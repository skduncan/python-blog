#!/usr/bin/env python3
#asg10.cgi
#Sam Duncan
#script that displays a blog to the user. User can add and remove entries on the blog.
#Entries on the blog display current date and time as well as the post


import cgi
import cgitb
import os
import classfun
import datetime

#cgitb.enable()
#print ("Content-Type: text/html\n\n")
#print ("Hello")
#cgi.test()

#Finds file that contains the blog posts and displays them to user.
def showblog():
    #First indent (FI)
        #Second indent (SI)
            #Third indent (TI)
                #Fourth (FI)
    filename ="../../../initial/myBlog.txt"
    if os.path.isfile(filename):
        print("<h3>Blog Posts</h3>\n")
        myfile = open(filename,'r',encoding='utf-8')
        contents = myfile.read()
        if(contents == ""):
            print("<h2>The Blog is Empty</h2>\n")
        else:
            print(contents,"<br />\n")
            print("<br />")
            for line in myfile:
                if line == "":
                    break
                else:
                    line = line.replace("&&!!","|")
                    print("<span class = 'content'",\
                        parts[0], "</span>\n",\
                        "<br />\n")
    else:
        print ("<h3> Blog File Not Found </h3>\n")


#Gives the user a textarea that allows them to input a message on the blog
def showaddentry():
    #FI
        #SI
            #TI
    self = os.environ['SCRIPT_NAME']
    print("<div><form method = 'post' action = '",self,"'>\n",\
        "<textarea name='entry' rows = '3' cols = '35'></textarea><br /><br />\n",\
        "<input type = 'submit' name = 'submitAdd' value = 'Add Entry' /><br /><br />\n",
        "<input type = 'submit' name = 'submitClear' value = 'Clear Blog' />\n",\
        "</form></div>\n")

#asks user to confirm if they wish to clear the blog after submitting 'submitClear'
def clearconfirm():
    self = os.environ['SCRIPT_NAME']
    print("<div><form method = 'post' action = '",self,"'>\n",\
        "<h3> Do you wish to clear the blog? </h3>\n",\
        "<input type = 'submit' name = 'submitClearConfirm' value = 'Confirm' />\n",\
        "<input type = 'submit' name = 'submitCancel' value = 'Cancel' />\n",\
        "</form></div>\n")

#clears the blog of all entries
#something is wrong here!
def clearblog():
    filename = "../../../initial/myBlog.txt"
    if os.path.isfile(filename):
        open(filename,'w').close()
    else:
        print("<h3>There is no file to clear</h3>\n")

#Adds the post given in showaddentry() to the blog file to display
#something is wrong here!
def postentry():
    #FI
        #SI
            #TI
    filename ="../../../initial/myBlog.txt"
    if("entry" in form):
        post = form["entry"].value
        if not post:
            print("<h3>No entry was made. Something must be entered</h3>\n")
        else:
            myfile = open(filename, 'r', encoding = 'utf-8')
            contents = myfile.read()
            myfile.close()
            from datetime import datetime
            today = str(datetime.now())
            postreplace = post.replace("|", "&&!!")
            post = postreplace.replace("|","\n")
            outfile = open(filename, 'w')
            outfile.write(today + "|" + post + "<br />\n" + contents)
            outfile.close()
    else:
        print("<h3>No entry made. Something must be entered.</h3>\n")




print("<body><div class='heading'>\n",\
    "<h3> Assignment 10 Python Blog </h3>\n",\
    "</div>\n")

print("<div class='content'>\n")

#logic for the assignment
#if ("" in form)
#elif("" in form)
form = cgi.FieldStorage()
if not form:
    showaddentry()
    showblog()
elif("submitAdd" in form):
    postentry()
    showaddentry()
    showblog()
elif("submitClear" in form):
    clearconfirm()
elif("submitClearConfirm" in form):
    clearblog()
    showaddentry()
    showblog()
elif("submitCancel" in form):
    showaddentry()
    showblog()

print("</div></body>\n")
classfun.printDocFooter()
