from flask import Flask,request
import time
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

def createspdf(name,phone,date,time,size,flavour,spec,price,my_day,message):
    canvasi = canvas.Canvas("/home/mallikarjun/Desktop/"+ str(name)+".pdf",pagesize=letter)
    canvasi.setLineWidth(.3)
    canvasi.setFont('Helvetica', 20)

    canvasi.line(50, 747, 580, 747) #FROM TOP 1ST LINE
    canvasi.drawString(280, 750, my_day+" "+date+" "+time)
    canvasi.drawString(60, 720, "CUSTOMER NAME:- "+ name)
    canvasi.drawString(60, 690, "PHONE:- "+ phone)
    canvasi.line(50, 640, 580, 640)#FROM TOP 2ST LINE
    canvasi.line(50, 748, 50, 50)#LEFT LINE
    canvasi.line(400, 640, 400, 50)# MIDDLE LINE
    canvasi.line(580, 748, 580, 50)# RIGHT LINE
    canvasi.drawString(475, 615, 'AMOUNT')
    canvasi.drawString(100, 615, 'PRODUCT')
    canvasi.line(50, 600, 580, 600)#FROM TOP 3r
    canvasi.drawString(60, 550, size+" "+flavour+" "+spec)
    canvasi.drawString(500, 550, price)
    canvasi.drawString(60, 500, message)
    canvasi.line(50, 100, 580, 100)#FROM TOP 4th LINE
    canvasi.drawString(60, 80, " TOTAL AMOUNT")
    canvasi.drawString(500, 80, str(price))
    canvasi.line(50, 50, 580, 50)#FROM TOP LAST LINE
    canvasi.save()





@app.route("/",methods=['POST'])
def re():
    name = str(request.form['name'])
    phone = str(request.form['phone'])
    date = str(request.form['date'])
    time = str(request.form['time'])
    size = str(request.form['size'])   
    flavour = str(request.form['flavour'])    
    spec = str(request.form ['spec'])
    price = str(request.form['price'])
    message = str(request.form['message'])
    year, month, day = (int(x) for x in date.split('-'))    
    ans = datetime.date(year, month, day)
    my_day =  ans.strftime("%A")
    createspdf(name,phone,date,time,size,flavour,spec,price,my_day,message)
    print name,phone,date,time,size,flavour,spec,price,my_day
    return name 


if __name__ == "__main__":
    app.run(debug=True)
