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
#comment

x = []
y = []
j = []
z = []

#with open ("C:\\Users\jarla\OneDrive\Desktop\FinalProjectProgramming\Test1.csv", 'r') as csvfile:
#    lines = csv.reader(csvfile, delimiter=',')
#    for row in lines:
#        x.append(row[0])
#        y.append((row[1]))

#plt.plot(x, y, color='g', linestyle='dashed',
 #        marker='o', label="Age Data")

#plt.xticks(rotation=25)
#plt.xlabel('Header')
#plt.ylabel('Data')
#plt.title('Test', fontsize=20)
#plt.grid()
#plt.legend()
#plt.show()
#Below updates the file StudentTable2.html with the data from the csv file - as a table say
#file = pandas.read_csv("C:\\Users\jarla\OneDrive\Desktop\FinalProjectProgramming\Test1.csv")
#file.to_html("StudentTable.html")

#from prettytable import PrettyTable
#file = open("C:\\Users\jarla\OneDrive\Desktop\FinalProjectProgramming\Test1.csv", 'r')
#file = file.readlines()
#head = file[0]
#head = head.split(',')
#table = PrettyTable([head[0], head[1],head[2], head[3],head[4], head[5]])
#for i in range(1, len(file)) :
#    table.add_row(file[i].split(','))
#htmlCode = table.get_html_string()
#final_htmlFile = open('StudentTable2.html', 'w')
#final_htmlFile=final_htmlFile.write(htmlCode)

#Below on connecting to a local DB and importing the data takend from here on website:
#https://www.datacamp.com/tutorial/sqlite-in-python
conn = sqlite3.connect('C:\\Users\jarla\OneDrive\Desktop\TestDB.db')
print("database opened")
cur = conn.cursor()


#for row in cur.execute('SELECT * FROM renewableenergydata'):
#    print(cur.fetchone());
    #z.append(row[0], row[1])
    #j.append(row[2], row[3])
    #print(z)
    #print(j)

#plt.plot(x, y, color='g', linestyle='solid',
#         marker='o', label="Test DB Data")
#plt.xticks(rotation=25)
#plt.xlabel('Header')
#plt.ylabel('Data')
#plt.title('Test', fontsize=20)
#plt.grid()
#plt.legend()
#plt.show()
conn.close()

app = Flask(__name__, static_folder='static', template_folder='Templates')
#@app.route("/searchrenewableenergytable", methods=["POST", "GET"])

#def searchrenewableenergy():
#    msg = 'msg'
#    email = request.form["email"]
#    firstname = request.form["firstname"]
#    surname = request.form["surname"]
#    password = request.form["password"]
#    landlord = request.form["landlord"]
#    tenant = request.form["tenant"]
    #try:
#    if request.method == "POST" and 'email' in request.form and 'firstname' in request.form and 'surname' in request.form and 'password' in request.form and 'landlord' in request.form and 'tenant' in request.form:
#        with sqlite3.connect("useraccount.db") as conn:
#            cur = conn.cursor()
#            cur.execute("select email from Users where email='%s'" % email)

#            if cur.fetchone():
#                msg2 = "There is already an account using that email address"
#                return render_template('Messages2.html', msg2=msg2)

#            else:
#                with sqlite3.connect("useraccount.db") as conn:
#                    cur = conn.cursor()
#                    cur.execute("INSERT into Users (email, firstname, surname, password, landlord, tenant) VALUES (?,?,?,?,?,?)", (email, firstname, surname, password, landlord, tenant))
#                    conn.commit()

#                    msg = "Account successfully Added"
#                return render_template("Messages1.html", msg=msg)

#    else:
#        msg3 = "Please enter the details on the form"
#        return render_template('Messages3.html', msg3=msg3)


#Code on this file heavily influenced by slides 29 to 33 from SQl Powerpoint class, also below sources
#https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/?ref=gcse
#all from here https://www.tutorialspoint.com/flask/flask_sqlite.htm
#creating the database to hold the user accounts
#conn.execute("create table Users (email TEXT UNIQUE NOT NULL PRIMARY KEY, firstname TEXT NOT NULL, surname TEXT NOT NULL, password TEXT NOT NULL, landlord TEXT NOT NULL, tenant TEXT NOT NULL)")
#print("table created")
#Testing that data added successfully
#conn.execute("INSERT INTO Users (email,firstname,surname,password, landlord, tenant) VALUES ('bill@gmail.com', 'Paul', 'Jones', 'California', 'Y', 'N' )")
#cursor = conn.execute("SELECT email,firstname,surname,password, landlord, tenant from Users")
#for row in cursor:
 #   print("email = ", row[0])
  #  print("firstname = ", row[1])
   # print("surname = ", row[2])
    #print("password = ", row[3])
    #print("landlord = ", row[4])
#print("Operation done successfully")
#conn.close()

#Creating the database to hold the reviews
#conn = sqlite3.connect('reviews4.db')
#print("reviews4 database opened")
#conn.execute("create table allrevs (PropertyName TEXT UNIQUE NOT NULL, RentPaid TEXT NOT NULL, ShopsAmenitiesNearby TEXT NOT NULL, AgentLandlordResponse TEXT NOT NULL, Accessibility TEXT NOT NULL, Security TEXT NOT NULL, Deposit INTEGER NOT NULL, MainReview TEXT NOT NULL)")
#conn.execute("INSERT INTO allrevs (PropertyName,RentPaid,ShopsAmenitiesNearby,AgentLandlordResponse, Accessibility, Security, Deposit, MainReview) VALUES ('test', '1500', 'poor', 'Good', 'VeryGood', 'Good', '0', 'Lorum' )")
#conn.commit()
#cursor = conn.execute("SELECT PropertyName,RentPaid,ShopsAmenitiesNearby,AgentLandlordResponse, Accessibility, Security, Deposit, MainReview from allrevs")
#for row in cursor:
#    print("PropertyName = ", row[0])
#    print("RentPaid = ", row[1])
#    print("ShopsAmenitiesNearby = ", row[2])
#    print("AgentLandlordResponse = ", row[3])
#    print("Accessibility = ", row[4])
#    print("Security = ", row[5])
#    print("Deposit = ", row[6])
#    print("MainReview = ", row[7])
#conn.close()

@app.route('/gittest')
def gittest():
    return render_template("Gittest.html")

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
            if all(char.isalpha() or char.isspace() for char in submit):
                print("Your input is a string of letters or spaces")

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
                        ErrorMessage = "Passed all checks but No country found Please enter the details on the form"
                        return render_template('ErrorPage.html' , ErrorMessage=ErrorMessage)
            else:
                print("IsAlphaFalse Your input contains something other than letters")
                return render_template('ErrorPage.html', ErrorMessage="IsAlphaFalseEnter letters only")
        else:
            print("IsUpperFalseThe first letter is not a capital letter")
            return render_template('ErrorPage.html', ErrorMessage="IsUpperFalseStart with a capital letter")


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
                            #if j.find(',') != -1:
                            #if ',' in j:
                            #    e.append(float(j.replace(',','')))
                            #else:
                            #    e.append(float(j))
                        print("")
                        print("This is list e after converting from string to float and dropping the ,", e)
                        #for k in e: #(i = 0, i < len(c), i++)-->:
                        #    if k <= 100:
                        #        f.append(k)
                                #k = k;
                            #elif (i > 100 & i <= 1000):
                        #    elif(k <= 1000):
                        #        f.append(k/10)
                                 #k = k/10;
                            #elif i > 1000 & i <= 10000:
                        #    elif k <= 10000:
                        #        f.append(k / 100)
                                 #k = k/100;
                            #elif (i > 10000 & i <= 100000):
                        #    elif k <= 100000:
                        #        f.append(k/1000)
                                #k =k/1000;
                            #elif (i > 100000 & i <= 1000000):
                        #    elif k <= 1000000:
                        #        f.append(k / 10000)
                                #k =k/10000;
                        #    else :
                        #        f.append(k/100000)
                                #k =k/100000;

                        #print("This is list f after calculation if/else loop ", f)
                        print("")
                        print("This is subset d ", d)
                        print("")
                        print("There is a row in the database for that country")
                        return render_template('Chart3.html', data2=json.dumps(e), country2=json.dumps(submit))
                    else:
                        ErrorMessage = "Passed all checks but No country found Please enter the details on the form"
                        return render_template('ErrorPage.html' , ErrorMessage=ErrorMessage)
            else:
                print("IsAlphaFalse Your input contains something other than letters")
                return render_template('ErrorPage.html', ErrorMessage="IsAlphaFalseEnter letters only")
        else:
            print("IsUpperFalseThe first letter is not a capital letter")
            return render_template('ErrorPage.html', ErrorMessage="IsUpperFalseStart with a capital letter")

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
                        #for j in c:
                            #below line by itself works or use the if else loop below also - same result
                        #    e.append(float(j.replace(',', '')))
                            #if j.find(',') != -1:
                            #if ',' in j:
                            #    e.append(float(j.replace(',','')))
                            #else:
                            #    e.append(float(j))
                        print("")
                        #print("This is list e after converting from string to float and dropping the ,", e)
                        #for k in e: #(i = 0, i < len(c), i++)-->:
                        #    if k <= 100:
                        #        f.append(k)
                                #k = k;
                            #elif (i > 100 & i <= 1000):
                        #    elif(k <= 1000):
                        #        f.append(k/10)
                                 #k = k/10;
                            #elif i > 1000 & i <= 10000:
                        #    elif k <= 10000:
                        #        f.append(k / 100)
                                 #k = k/100;
                            #elif (i > 10000 & i <= 100000):
                        #    elif k <= 100000:
                        #        f.append(k/1000)
                                #k =k/1000;
                            #elif (i > 100000 & i <= 1000000):
                        #    elif k <= 1000000:
                        #        f.append(k / 10000)
                                #k =k/10000;
                        #    else :
                        #        f.append(k/100000)
                                #k =k/100000;

                        #print("This is list f after calculation if/else loop ", f)
                        print("")
                        print("This is subset d ", d)
                        print("")
                        print("There is a row in the database for that country")
                        return render_template('Chart5.html', data3=json.dumps(c), country3=json.dumps(submit))
                    else:
                        ErrorMessage = "Passed all checks but No country found Please enter the details on the form"
                        return render_template('ErrorPage.html' , ErrorMessage=ErrorMessage)
            else:
                print("IsAlphaFalse Your input contains something other than letters")
                return render_template('ErrorPage.html', ErrorMessage="IsAlphaFalseEnter letters only")
        else:
            print("IsUpperFalseThe first letter is not a capital letter")
            return render_template('ErrorPage.html', ErrorMessage="IsUpperFalseStart with a capital letter")

@app.route('/searchirishenergy')
def searchirishenergy():
    return render_template("IrishEnergyTemplate2.html")


@app.route("/searchirishenergytable", methods=["POST", "GET"])
##this works to check if the country is on the list and returns its graph of the trend over time of the greenhouse gas emmissions
def searchirishenergytable():
    if request.method == "POST":
        submit = request.form["search4"].strip()
        print("This is what you entered: ", submit)
#checking the first letter is a capital as that is the format of the data in the table
        if (submit[0].isupper()):
            print("The first letter is a capital letter")
# checking that only letters and spaces are used as that is the format of the data in the table
            if all(char.isalpha() or char.isspace() for char in submit):
                print("Your input is a string of letters or spaces")

                with sqlite3.connect("C:\\Users\jarla\OneDrive\Desktop\TestDB.db") as conn:
                    cur = conn.cursor()
                    cur.execute("select * from IrishEnergyBreakdown where Fuel Group Hierarchy - Fuel Group = '%s'" %submit)
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
                        #for j in c:
                            #below line by itself works or use the if else loop below also - same result
                        #    e.append(float(j.replace(',', '')))
                            #if j.find(',') != -1:
                            #if ',' in j:
                            #    e.append(float(j.replace(',','')))
                            #else:
                            #    e.append(float(j))
                        print("")
                        print("This is subset d ", d)
                        print("")
                        print("There is a row in the database for that country")
                        return render_template('Chart6.html', data4=json.dumps(c), country4=json.dumps(submit))
                    else:
                        ErrorMessage = "Passed all checks but No country found Please enter the details on the form"
                        return render_template('ErrorPage.html' , ErrorMessage=ErrorMessage)
            else:
                print("IsAlphaFalse Your input contains something other than letters")
                return render_template('ErrorPage.html', ErrorMessage="IsAlphaFalseEnter letters only")
        else:
            print("IsUpperFalseThe first letter is not a capital letter")
            return render_template('ErrorPage.html', ErrorMessage="IsUpperFalseStart with a capital letter")

#Below from here also  - used to show what's entered through the form and the connection to the database - info going in to the database,
#https://www.tutorialspoint.com/flask/flask_sqlite.htm
#Below route shows all the user accounts held on that table in the database
#@app.route('/list')

#def list():
#    conn = sqlite3.connect("useraccount.db")
#    conn.row_factory = sqlite3.Row

#    cur = conn.cursor()
#    cur.execute("select * from users")
#    rows = cur.fetchall()
#    return render_template("testlist.html", rows=rows)


#Below route shows all the reviews held on that table in the database
#@app.route('/listreviews')
#def listreviews():
#    conn = sqlite3.connect('reviews4.db')
#    conn.row_factory = sqlite3.Row
#    cur = conn.cursor()
#    cur.execute("select * from allrevs")
#    rows = cur.fetchall()
#    return render_template("reviewlist.html", rows=rows)



#@app.route("/loginhere",  methods=["POST", "GET"])
#def loginhere():
#    return render_template("BootstrapLoginPage.html")


#@app.route('/login2', methods=["POST", "GET"])
#def login():
#    conn = sqlite3.connect("useraccount.db")
#    cur = conn.cursor()

#    if request.method == "POST" and 'email' in request.form and 'password' in request.form:
#        mail = request.form["email"]
#        pw = request.form["password"]
#        print(mail)
#        print(pw)
#        result = []
#        cur.execute("select email from Users WHERE email = '%s'" % mail)
#        email_in_db = cur.fetchone()

#        if email_in_db:
#            cur.execute("select password, email from Users WHERE email = '%s'" % mail)
#            result = cur.fetchone()
#            print('results are:', result)

 #           if result.count(pw) > 0:
#                msg3 = "Success - Credentials match, you are logged in"

#                return render_template('Messages3.html', msg3=msg3)

#            else:
#                msg = "Error message - That password does not match that email address"
#                return render_template('Messages1.html', msg=msg)

#        else:
#            msg = "Error message - There is no matching email in our database"
#            return render_template('Messages1.html', msg=msg)


#@app.route("/leaveareview",  methods=["POST", "GET"])
#def leavereview():
#    return render_template("LeaveAReview.html")


#@app.route("/addtoreviewsdb", methods=["POST", "GET"])
#def createnewreview():
#    msg = 'msg'
#    if request.method == 'POST':
#        try:
#            PropertyNamef = request.form["NameOfProperty"]
#            RentPaidf = request.form["RentPaid"]
#            ShopsAmenitiesNearbyf = request.form["ShopAmenitiesRatings"]
#            AgentLandlordResponsef = request.form["LandlordAgentRating"]
#            Accessibilityf = request.form["TransportRating"]
#            Securityf = request.form["Securityrating"]
#            Depositf = request.form["DepositReturn"]
#            MainReviewf = request.form["Mainreview"]

 #           with sqlite3.connect("reviews4.db") as conn:
#                cur = conn.cursor()
#                cur.execute("INSERT INTO allrevs (PropertyName,RentPaid,ShopsAmenitiesNearby,AgentLandlordResponse, Accessibility, Security, Deposit, MainReview) VALUES (?,?,?,?,?,?,?,?)", (PropertyNamef,RentPaidf,ShopsAmenitiesNearbyf,AgentLandlordResponsef, Accessibilityf, Securityf, Depositf, MainReviewf))
#                conn.commit()
#                msg2 = "Review successfully Added"
#            return render_template('Messages2.html', msg2=msg2)

#        except:
#            conn.rollback()

#        finally:
#            return render_template("Messages1.html", msg=msg)

if __name__ == '__main__':

   app.run(host="0.0.0.0", port=5000, debug=True)