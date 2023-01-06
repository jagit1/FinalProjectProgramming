import json
from flask import Flask, render_template, request, url_for, flash, jsonify
import sqlite3
import re
import regex
import matplotlib.pyplot as plt
import csv
import pandas
from prettytable import PrettyTable
import json


x = []
y = []
j = []
z = []


#Below on connecting to a local DB and importing the data taken from here on website:
#https://www.datacamp.com/tutorial/sqlite-in-python
conn = sqlite3.connect('C:\\Users\jarla\OneDrive\Desktop\TestDB.db')
print("database opened")
cur = conn.cursor()

conn.close()

app = Flask(__name__, static_folder='static', template_folder='Templates')

#Code on this file heavily influenced by slides 29 to 33 from SQl Powerpoint class, also below sources
#https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/?ref=gcse
#all from here https://www.tutorialspoint.com/flask/flask_sqlite.htm

@app.route('/home')
def home():
    return render_template("CarouselTemplate.html")

@app.route('/search')
def index():
    return render_template("TestBootstrapSearchPage.html")

@app.route("/searchrenewableenergytable", methods=["POST", "GET"])
##this works to check if the country is on the list and returns its graph of the trend over time of the renewable energy proportion
def searchrenewableenergy():
    if request.method == "POST":
        submit = request.form["search"].strip()
        print("This is what you entered: ", submit)
#checking the first letter is a capital as that is the format of the data in the table
        if (submit[0].isupper()):
            print("The first letter is a capital letter")
# checking that only letters and spaces are used as that is the format of the data in the table
            #if all(char.isalpha() or char.isspace() for char in submit):
            #    print("Your input is a string of letters or spaces")

            with sqlite3.connect("C:\\Users\jarla\OneDrive\Desktop\TestDB.db") as conn:
                cur = conn.cursor()
                cur.execute("select * from renewableenergydata where Countryandarea= '%s'" %submit)
                row  = cur.fetchone()
                if row:
                    print("printing the full row inside the loop ", row)
                    a = []
                    b = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
                    for i in row:
                        a.append(i)
                    a.pop(0)
                    print("This is subset a ", a)
                    print("This is subset b ", b)
                    msg2 = "There is a row in the database for that country"
                    return render_template('Chart2.html', data=json.dumps(a), country=json.dumps(submit))
                else:
                    ErrorMessage = "No matching country found in database Please use the button below to search again Enter a country name on the form, beginning with a capital letter and using the characters A-Z or a-z only!"
                    return render_template('ErrorPage.html' , ErrorMessage=ErrorMessage)
            #else:
            #    print("IsAlphaFalse Your input contains something other than letters")
            #    return render_template('ErrorPage.html', ErrorMessage="IsAlphaFalseEnter letters only")
        else:
            print("IsUpperFalseThe first letter is not a capital letter")
            ErrorMessage = "No matching country found in database. Please use the button below to search again. Enter a country name on the form, beginning with a capital letter and using the characters A-Z or a-z only!"
            return render_template('ErrorPage.html', ErrorMessage=ErrorMessage)


@app.route('/searchghg')
def searchghg():
    return render_template("IntGHGSearchPage.html")

@app.route("/searchintghgtable", methods=["POST", "GET"])
##this works to check if the country is on the list and returns its graph of the trend over time of the greenhouse gas emmissions
def searchintghg():
    if request.method == "POST":
        submit = request.form["search2"].strip()
        print("This is what you entered: ", submit)
#checking the first letter is a capital as that is the format of the data in the table
        if (submit[0].isupper()):
            print("The first letter is a capital letter")
# checking that only letters and spaces are used as that is the format of the data in the table
            if all(char.isalpha() or char.isspace() for char in submit):
                print("Your input is a string of letters or spaces")

                with sqlite3.connect("C:\\Users\jarla\OneDrive\Desktop\TestDB.db") as conn:
                    cur = conn.cursor()
                    cur.execute("select * from InternationalGHG where Country= '%s'" %submit)
                    row  = cur.fetchone()
                    if row:
                        print("")
                        print("printing the full row inside the loop ", row)
                        c = []
                        d = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
                        e = []
                        f = []
                        for i in row:
                            c.append(i)
                        c.pop(0)
                        print("")
                        print("printing the full list c inside the loop after popping the first element ", c)
                        for j in c:
                            #below line by itself works or use the if else loop below also - same result
                            e.append(float(j.replace(',', '')))

                        print("")
                        print("This is list e after converting from string to float and dropping the ,", e)

                        print("")
                        print("This is subset d ", d)
                        print("")
                        print("There is a row in the database for that country")
                        return render_template('Chart3.html', data2=json.dumps(e), country2=json.dumps(submit))
                    else:
                        ErrorMessage2 = "No matching country found in database. Please use the button below to search again. Enter a country name on the form, beginning with a capital letter and using the characters A-Z or a-z only!"
                        return render_template('ErrorPage2.html' , ErrorMessage2=ErrorMessage2)
            else:
                ErrorMessage2 = "No matching country found in database. Please use the button below to search again. Enter a country name on the form, beginning with a capital letter and using the characters A-Z or a-z only!"
                #print("IsAlphaFalse Your input contains something other than letters")
                return render_template('ErrorPage2.html', ErrorMessage2=ErrorMessage2)
        else:
            ErrorMessage2 = "No matching country found in database. Please use the button below to search again Enter a country name on the form, beginning with a capital letter and using the characters A-Z or a-z only!"
            #print("IsUpperFalseThe first letter is not a capital letter")
            return render_template('ErrorPage2.html', ErrorMessage2=ErrorMessage2)

@app.route('/searchintwaste')
def searchintwaste():
    return render_template("IntWaste.html")

@app.route("/searchintwastetable", methods=["POST", "GET"])
##this works to check if the country is on the list and returns its graph of the trend over time of the greenhouse gas emmissions
def searchintwastetable():
    if request.method == "POST":
        submit = request.form["search3"].strip()
        print("This is what you entered: ", submit)
#checking the first letter is a capital as that is the format of the data in the table
        if (submit[0].isupper()):
            print("The first letter is a capital letter")
# checking that only letters and spaces are used as that is the format of the data in the table
            if all(char.isalpha() or char.isspace() for char in submit):
                print("Your input is a string of letters or spaces")

                with sqlite3.connect("C:\\Users\jarla\OneDrive\Desktop\TestDB.db") as conn:
                    cur = conn.cursor()
                    cur.execute("select * from InternationalWasteRecycling where Country= '%s'" %submit)
                    row  = cur.fetchone()
                    if row:
                        print("")
                        print("printing the full row inside the loop ", row)
                        c = []
                        d = [1990, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
                        e = []
                        f = []
                        for i in row:
                            c.append(i)
                        c.pop(0)
                        print("")
                        print("printing the full list c inside the loop after popping the first element ", c)

                        print("")

                        print("")
                        print("This is subset d ", d)
                        print("")
                        print("There is a row in the database for that country")
                        return render_template('Chart5.html', data3=json.dumps(c), country3=json.dumps(submit))
                    else:
                        ErrorMessage3 = "No matching country found in database. Please use the button below to search again Enter a country name on the form, beginning with a capital letter and using the characters A-Z or a-z only!"
                        return render_template('ErrorPage3.html' , ErrorMessage3=ErrorMessage3)
            else:
                ErrorMessage3 = "No matching country found in database. Please use the button below to search again. Enter a country name on the form, beginning with a capital letter and using the characters A-Z or a-z only!"
                print("IsAlphaFalse Your input contains something other than letters")
                return render_template('ErrorPage3.html', ErrorMessage3=ErrorMessage3)
        else:
            ErrorMessage3 = "No matching country found in database. Please use the button below to search again. Enter a country name on the form, beginning with a capital letter and using the characters A-Z or a-z only!"
            print("IsUpperFalseThe first letter is not a capital letter")
            return render_template('ErrorPage3.html', ErrorMessage3=ErrorMessage3)

@app.route('/searchirishenergy')
def searchirishenergy():
    return render_template("IrishEnergyTemplate2.html")


@app.route("/searchirishenergytable", methods=["POST", "GET"])
##this works to check if the country is on the list and returns its graph of the trend over time of the greenhouse gas emmissions
def searchirishenergytable():
    if request.method == "POST":
        submit = request.form["search4"].strip()
        print("This is what you entered: ", submit)


        with sqlite3.connect("C:\\Users\jarla\OneDrive\Desktop\TestDB.db") as conn:
            cur = conn.cursor()
            cur.execute("select * from IrishEnergyBreakdown where FuelType = '%s'" %submit)
            row  = cur.fetchone()
            if row:
                print("")
                print("printing the full row inside the loop ", row)
                c = []
                d = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2021]
                e = []
                f = []
                for i in row:
                    c.append(i)
                c.pop(0)
                print("")
                print("printing the full list c inside the loop after popping the first element ", c)
                print("")
                print("This is subset d ", d)
                print("")
                print("There is a row in the database for that country")
                return render_template('Chart6.html', data4=json.dumps(c), country4=json.dumps(submit))
            else:
                ErrorMessage = "Passed all checks but No fueltype found Please return to the previous page and select an option"
                return render_template('ErrorPage.html' , ErrorMessage=ErrorMessage)


@app.route("/searchirishenergytableall", methods=["POST", "GET"])
def searchirishenergytableall():
    if request.method == "POST":
        print("Request sent from HTMl template")
        return render_template("Chart9.html")

@app.route('/searchirishenergybysector')
def searchirishenergybysector():
    return render_template("IrishEnergyTemplate3.html")

@app.route("/searchirishenergybysectortable", methods=["POST", "GET"])
##this works to check if the country is on the list and returns its graph of the trend over time of the greenhouse gas emmissions
def searchirishenergybysectortable():
    if request.method == "POST":
        submit = request.form["search5"].strip()
        print("This is what you entered: ", submit)


        with sqlite3.connect("C:\\Users\jarla\OneDrive\Desktop\TestDB.db") as conn:
            cur = conn.cursor()
            cur.execute("select * from SectIrelandEnergy where Sector = '%s'" %submit)
            row  = cur.fetchone()
            if row:
                print("")
                print("printing the full row inside the loop ", row)
                c = []
                d = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2021]
                e = []
                f = []
                for i in row:
                    c.append(i)
                c.pop(0)
                print("")
                print("printing the full list c inside the loop after popping the first element ", c)
                print("")
                print("This is subset d ", d)
                print("")
                print("There is a row in the database for that sector")
                return render_template('Chart7.html', data5=json.dumps(c), country5=json.dumps(submit))
            else:
                ErrorMessage = "Passed all checks but no sector found. Please return to the previous page and select an option"
                return render_template('ErrorPage.html' , ErrorMessage=ErrorMessage)


@app.route("/searchirishenergysectorall", methods=["POST", "GET"])
def searchirishenergysectorall():
    if request.method == "POST":
        print("Request sent from HTMl template")
    return render_template("Chart16.html")

@app.route("/searchirishenergysectorall2bar", methods=["POST", "GET"])
def searchirishenergysectorall2bar():
    if request.method == "POST":
        print("Request sent from HTMl template")
    return render_template("Chart17.html")

@app.route('/searchcarregbyengtype')
def searchcarregbyengtype():
    return render_template("CarRegTemplate.html")

@app.route("/searchcarregbyengtypetable", methods=["POST", "GET"])
##this works to check if the country is on the list and returns its graph of the trend over time of the greenhouse gas emmissions
def searchcarregbyengtypetable():
    if request.method == "POST":
        submit = request.form["searchx"].strip()
        print("This is what you entered: ", submit)


        with sqlite3.connect("C:\\Users\jarla\OneDrive\Desktop\TestDB.db") as conn:
            cur = conn.cursor()
            cur.execute("select * from Fileforcarenginetype where Fueltype = '%s'" % submit)
            row = cur.fetchone()
            if row:
                print("")
                print("printing the full row inside the loop ", row)
                c = []
                d = [2007, 2010, 2013, 2016, 2019, 2021]
                e = []
                f = []
                for i in row:
                    c.append(i)
                c.pop(0)
                print("")
                print("printing the full list c inside the loop after popping the first element ", c)
                for j in c:
                    e.append(float(j.replace(',', '')))
                print("")
                print("This is subset d ", d)
                print("")
                print("printing the full list e inside the loop after removing the commas in the numbers ", e)
                print("There is a row in the database for that sector")
                return render_template('Chart8.html', data6=json.dumps(e), country6=json.dumps(submit))
            else:
                ErrorMessage = "Passed all checks but no result found Please return to the previous page and select an option"
                return render_template('ErrorPage.html', ErrorMessage=ErrorMessage)


@app.route("/searchcarregbyengtypetable2", methods=["POST", "GET"])
##this works to check if the country is on the list and returns its graph of the trend over time of the greenhouse gas emmissions
def searchcarregbyengtypetable2():
    if request.method == "POST":
        submit = request.form["yearoptionx"]
        print("Here's what you entered",submit)

        if submit == 'yearoption1':
            print("This is what you entered 1: ", submit)
            return render_template('Chart10.html')

        elif submit == "yearoption2":
            print("This is what you entered 2: ", submit)
            return render_template('Chart11.html')

        elif submit == "yearoption3":
            print("This is what you entered 3: ", submit)
            return render_template('Chart12.html')

        elif submit == "yearoption4":
            print("This is what you entered 4: ", submit)
            return render_template('Chart13.html')

        elif submit == "yearoption5":
            print("This is what you entered 5: ", submit)
            return render_template('Chart14.html')

        elif submit == "yearoption6":
            print("This is what you entered 6: ", submit)
            return render_template('Chart15.html')

        else:
            return render_template('ErrorPage.html')



if __name__ == '__main__':

   app.run(host="0.0.0.0", port=5000, debug=True)