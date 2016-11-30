
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9023348
#    Student name: OHI AHMED
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  LIVE NEWS FEED
#
#  The World Wide Web provides us with such an abundance of
#  information that it's often difficult to find just the data you
#  want.  In this task you will develop a simple app that fetches
#  web pages and summarises just their essential facts.  Your
#  app will have an intuitive Graphical User Interface that makes
#  it easy to use.  See the instruction sheet accompanying
#  this file for full details.
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.
#

#----------
# Import the various functions needed to complete this program.
# NB: You may NOT import or use code from any other module
# in your solution.  Also, you do NOT need to use all these
# functions in your solution.

# Import the function for fetching web pages
from urllib import urlopen 

# Import all the Tkinter GUI functions
from Tkinter import *

# Import the regular expression search function
from re import findall

# Import the scrolled text widget (Optional - you
# do not need to use this, a standard Text
# widget is adequate)
from ScrolledText import ScrolledText
#----------


##### DEVELOP YOUR SOLUTION HERE #####

# The weather report website links for the cities are stored in the variables
# of their own name:
Adelaide = 'http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=12495&obs=1&fc=1&warn=1'
Brisbane = 'http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=9388&obs=1&fc=1&warn=1'
Canberra = 'http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=3928&obs=1&fc=1&warn=1'
Darwin = 'http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=11&obs=1&fc=1&warn=1'
Hobart = 'http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=15465&obs=1&fc=1&warn=1'
Melbourn = 'http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=5594&obs=1&fc=1&warn=1'
Perth = 'http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=13896&obs=1&fc=1&warn=1'
Sydney = 'http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=624&obs=1&fc=1&warn=1'



# This function is called when a radio button is selected:
def check_city():
    global box
    # Clears the text box:
    box.config(state = NORMAL)
    box.delete(0.0, END)

    # The codes starting with 'if' and 'elif' checks which radio button is
    # selected and depending on it, one of the website links mentioned 
    # above is opened. Then the city's name is inserted in the text box:    
    if city_variable.get()== 'a':
        Weather = urlopen(Adelaide)
        box.insert(END, 'City: Adelaide'+ '\n' )
    elif city_variable.get() =='b':
        Weather = urlopen(Brisbane)
        box.insert(END, 'City: Brisbane'+ '\n' )
    elif city_variable.get() == 'c':
        Weather = urlopen(Canberra)
        box.insert(END, 'City: Canberra'+ '\n' )
    elif city_variable.get() =='d':
        Weather = urlopen(Darwin)
        box.insert(END, 'City: Darwin'+ '\n' )
    elif city_variable.get() == 'h':
        Weather = urlopen(Hobart)
        box.insert(END, 'City: Hobart'+ '\n' )
    elif city_variable.get() =='m':
        Weather = urlopen(Melbourn)
        box.insert(END, 'City: Melbourne'+ '\n' )
    elif city_variable.get() == 'p':
        Weather = urlopen(Perth)
        box.insert(END, 'City: Perth'+ '\n' )
    elif city_variable.get() =='s':
        Weather = urlopen(Sydney)
        box.insert(END, 'City: Sydney'+ '\n' )

    # Extracts all the html codes from the Weather variable:            
    WeatherCode = Weather.read()

    # Finds all the necessary contents of the weather report from the html codes
    # extracted in the WeatherCode variable:
    WeatherReport = findall('<b>([^<>SI]+)</b>([a-zA-z0-9. ]+)(?:&#176;)?([%C])?'
                            ,WeatherCode)
    
    # Finds the whole date including day from the same html codes:
    Date = findall('<pubDate>([A-za-z]+, [0-9]+ [A-za-z]+ [0-9]+).+</pubDate>'
                   , WeatherCode)

    # The Day is done separately again because if the whole date is not
    # available in the webpage may be while updating or the pattern of the date
    # changes, the program would crash (exceptional case):
    Day = findall('<b>([A-Za-z]+)</b><br />', WeatherCode)

    # If the whole Date is not found from the webpage, the exception would be
    # caught and instead only the Day will be inserted in the text box avoiding
    # the program to crash. Otherwise the Date would be inserted. (Just tried to
    # make it a bit robust): 

    try:
        box.insert(END, "Today: "+str(Date[0]) +'\n')
    except IndexError:
        box.insert(END, "Today: "+str(Day[0]) +'\n')
    box.insert(END, " "+ '\n')

    # All the contents found in the WeatherReport variable are put in the text
    # box one after another using this loop:
    for each in WeatherReport:
        # The content "Description" is excluded as only two cities have it in
        # their weather report and the rest does not:
        if each[0] != "Description:":
            # The elements in the substring variable each are put in the text
            # box:
            box.insert(END, str(each[0]))
            box.insert(END, str(each[1]))
            box.insert(END, str(each[2])+ '\n')
    
    # This code does not allow manual typing in the text box:
    box.config(state = DISABLED)

## The Graphical User Interface (GUI):

# A new window is created:
window = Tk()

# The title of the window is set as 'Weather Reporter':
window.title('Weather Reporter')
# The window's background colour is made white:
window.config(background = "white")

Label(window, text = "Current Weather",bg = "white",
      font=("Ariel", 12)).grid(row = 0, column = 0, sticky = N)

# Introduction of the string variable whose value will be changed by selecting a
# radio button:
city_variable = StringVar()

# The text box is created which will initially ask to select a city:
box = Text(window,width = 20, height =12, bg = "light yellow", font = ("Ariel"
                                                                       , 12))
box.insert(END, "Select a city to view its" + "\n" + "weather report.")
box.grid(column = 0, columnspan = 1, rowspan = 4, padx= 8, pady = 8)

#The radio button widgets are created for the cities:
adelaide = Radiobutton(window, text = "Adelaide", variable = city_variable,
                       value = 'a', command = check_city, bg = "white")
brisbane = Radiobutton(window, text = "Brisbane", variable = city_variable,
                       value = 'b', command = check_city, bg = "white")
canberra = Radiobutton(window, text = "Canberra", variable = city_variable,
                       value = 'c', command = check_city, bg ="white")
darwin = Radiobutton(window, text = "Darwin", variable = city_variable,
                       value = 'd', command = check_city, bg = "white")
hobart = Radiobutton(window, text = "Hobart", variable = city_variable,
                       value = 'h', command = check_city, bg = "white")
melbourne = Radiobutton(window, text = "Melbourne", variable = city_variable,
                       value = 'm', command = check_city, bg = "white")
perth = Radiobutton(window, text = "Perth", variable = city_variable,
                       value = 'p', command = check_city, bg = "white")
sydney = Radiobutton(window, text = "Sydney", variable = city_variable,
                       value = 's', command = check_city, bg = "white")

# Each radio button is put on a separate grid row or column and sticking to the
# West:
adelaide.grid(column = 1, row = 1,   sticky = W)  
brisbane.grid(column = 2, row=1,  sticky = W)
canberra.grid(column = 1, row=2,  sticky = W)
darwin.grid(column =2,row =2, sticky = W)
hobart.grid(column = 1, row = 3,  sticky = W)
melbourne.grid(column = 2, row = 3,  sticky = W)
perth.grid(column = 1, row = 4, sticky = W)
sydney.grid(column = 2, row = 4,  sticky = W)

# Starting the event loop to react to user inputs:
window.mainloop()
#
#--------------------------------------------------------------------#
