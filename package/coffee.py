from flask import render_template, url_for,request,redirect,session
from package import app
#import client
import socket
import time

# @app.route("/summa")
# def aa():
#    return render_template("speedometers.html")
response = ""

@app.route("/about")
def about():
   return render_template('about.html')

#data = "Hello World "
@app.route("/index",methods = ['GET','POST'])
def start():
    return render_template("control.html")

@app.route("/times",methods=['GET','POST'])
def times():
   print("hi")
   p = 0
   global response
   if request.method == 'POST':
    p = int(request.form.get("timerr"))
    print(p)
   return render_template("timer.html", x = response.split(" "),min = p // 60,sec = p % 60)

p = 0
@app.route('/send_data',methods = ['GET','POST'])
def send_data():
    # Establish socket connection with the server
    host = '127.0.0.1'
    port = 5001
    s = ""
    global p
    global response
    # heat_coeffs = [50, 75, 100, 125, 150]
    # mass_coeffs = [0.005, 0.01, 0.015, 0.02, 0.025]
    # drying_coeffs = [0.001, 0.002, 0.003, 0.004, 0.005]
    if request.method == 'POST':
      for i in range(1,7):
         s += request.form.get(str(i)) + ","
      s += "bye"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(str("hi").encode())
        print(s)
        time.sleep(5)
        client_socket.send(str(s).encode())
        response = ""
        response += client_socket.recv(1024).decode() + " "
        p = int(request.form.get('2'))
        print(response)    
        return render_template("speedometers.html",x = response.split(" "),min = p,sec = 0)
# @app.route("/blah")
# def blah():
#    time_list = []
#    for i in range(1,p,5):
#       time_list.append(i*60)
#    print(response)
#    return render_template('visualization.html', response = response,timet = time_list)

# @app.route('/send_more_data',methods = ['GET','POST'])
# def send_more_data():
#     host = '127.0.0.1'
#     port = 5001
#     response = " "
#     s = ""
#     if request.method == 'POST':
#         for i in range(1,4):
#          timer = int(request.form.get("time"))
#          s += request.form.get(str(i)) + ","
#         s += str(timer/60) + ",bye"
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         client_socket.connect((host, port))
#         print(s)
#         client_socket.send(str(s).encode())
#         response += client_socket.recv(1024).decode() + "\n"
#     return render_template("timer.html",x = response,min = timer//60, sec = timer % 60)


# import socket
# socketio = SocketIO(app)

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')

# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')

# @socketio.on('send_data')
# def handle_send_data(data):
#     host = "BATEMAN"  # Replace with your server hostname
#     port = 5001

#     client_socket = socket.socket()
#     client_socket.connect((host, port))

#     amount, temp, timer = data['amount'], data['temp'], data['timer']
#     for i in range(1, timer, 5):
#         message = f"{amount},{temp},{i}"
#         client_socket.send(message.encode())
#         response = client_socket.recv(1024).decode()

#         # Emit the response to the web page
#         emit('receive_response', {'response': response})

#     client_socket.close()
#     emit('receive_response', {'response': 'bye'})