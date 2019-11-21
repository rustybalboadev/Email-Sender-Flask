from flask import Flask, redirect, request, render_template
import smtplib
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        your_email = request.form['your_email']
        your_email_password = request.form['your_password']
        their_email = request.form['their_email']
        message = request.form['message']
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(your_email,your_email_password)
        s.sendmail(your_email,their_email,message)
        return "Sent The Email to {}".format(their_email)
    elif request.method == 'GET':
        return render_template('sender.html')
