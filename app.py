from flask import Flask,request,make_response,render_template
import time
import datetime
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

def createspdf(name,phone,date,time,size,flavour,spec,price,advance,my_day,message):
    canvasi = canvas.Canvas("/home/mallikarjun/Desktop/"+ str(name)+".pdf",pagesize=letter)

    canvasi.setLineWidth(.3)
    canvasi.setFont('Helvetica-Bold', 20)
    r = random.randint(1111, 9999)
    ids = "%04d" % r
    canvasi.line(50, 747, 580, 747) #FROM TOP 1ST LINE
    canvasi.drawString(150, 750, my_day+" "+date+" "+time)
    canvasi.setLineWidth(.2)
    canvasi.setFont('Helvetica-Bold', 19)
    canvasi.setFillColorRGB(1, 0, 0)
    canvasi.drawString(520, 750, ids)

    canvasi.setLineWidth(.3)
    canvasi.setFont('Times-Italic', 18)
    canvasi.setFillColorRGB(0,0,0)
    #canvasi.drawString(60, 720, "Customer Name: "+ name)
    canvasi.drawString(60, 720, "Customer Name: ")
    canvasi.setFont('Times-BoldItalic', 18)
    canvasi.drawString(190, 720, name.title())
    #canvasi.drawString(60, 690, "Phone: "+ phone)
    canvasi.setFont('Times-Italic', 18)
    canvasi.drawString(60, 690, "Phone: ")
    canvasi.setFont('Times-BoldItalic', 18)
    canvasi.drawString(115, 690, phone)
    canvasi.line(50, 640, 580, 640)#FROM TOP 2ST LINE
    canvasi.line(50, 748, 50, 50)#LEFT LINE
    canvasi.line(400, 640, 400, 50)# MIDDLE LINE
    canvasi.line(580, 748, 580, 50)# RIGHT LINE
    canvasi.setFont('Times-Italic', 18)
    canvasi.drawString(475, 615, 'AMOUNT')
    canvasi.drawString(100, 615, 'PRODUCT')
    canvasi.line(50, 600, 580, 600)#FROM TOP 3r
    canvasi.setFont('Helvetica-Bold', 20)
    canvasi.drawString(60, 550, size+" "+flavour+" "+spec)
    canvasi.drawString(500, 550, price)
    canvasi.setFont('Times-Italic', 18)
    canvasi.drawString(60, 500, message)
    canvasi.drawString(60, 102, 'Advance Paid')
    canvasi.setFont('Helvetica-Bold', 20)
    canvasi.drawString(500, 102, advance)

    canvasi.line(50, 100, 580, 100)#FROM TOP 4th LINE
    canvasi.setFont('Times-Italic', 18)
    canvasi.drawString(60, 70, " TOTAL AMOUNT")
    balance = int(price)-int(advance)
    #canvasi.setFont('Times-BoldItalic', 18)
    canvasi.setFont('Helvetica-Bold', 20)
    canvasi.drawString(500, 70, str(balance))
    canvasi.line(50, 50, 580, 50)#FROM TOP LAST LINE

    canvasi.save()

@app.route('/')
def index():
   return render_template('index.html')




@app.route("/order",methods=['POST'])
def re():
    name = str(request.form['name'])
    phone = str(request.form['phone'])
    date = str(request.form['date'])
    time = str(request.form['time'])
    size = str(request.form['size'])   
    flavour = str(request.form['flavour'])    
    spec = str(request.form ['spec'])
    price = str(request.form['price'])
    advance = str(request.form['advance'])
    message = str(request.form['message'])
    year, month, day = (int(x) for x in date.split('-'))    
    ans = datetime.date(year, month, day)
    my_day =  ans.strftime("%A")
    createspdf(name,phone,date,time,size,flavour,spec,price,advance,my_day,message)
    with open("/home/mallikarjun/Desktop/"+ str(name)+".pdf", 'rb') as f:
        response = make_response(f.read())
        response.headers['Content-Type'] = "application/pdf"
        return response



if __name__ == "__main__":
    app.run(debug=True)
