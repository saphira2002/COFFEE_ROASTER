# import socket
# import time

# def client_program(s):
#     host = '127.0.0.1'  # as both code is running on same pc
#     port = 5001  # socket server port number

#     client_socket = socket.socket()  # instantiate
#     client_socket.connect((host, port))  # connect to the server
#     print("COnnected")
#     while True:
#         for i in range(len(s)):
#             time.sleep(5)
#             client_socket.send(str(s[i]).encode())  # send data to the client
#         #client_socket.send("bye".encode())
#         data = client_socket.recv(1024).decode()
#         print(data)
#     client_socket.close()  # close the connection

# from flask_socketio import SocketIO, emit

# app = Flask(_name_)
# socketio = SocketIO(app)

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')

# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')

# @socketio.on('send_data')
# def handle_send_data(data):
#     host = "server_hostname"  # Replace with your server hostname
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
#     emit('receive_response', {'response': 'bye'})  # Notify the web page that the communication is done

# @app.route('/')
# def index():
#     return render_template('index.html')

# if _name_ == '_main_':
#     socketio.run(app)

# # import socket

# # def server_program(s):
# #     # get the hostname
# #     host = socket.gethostname()
# #     port = 5001  # initiate port no above 1024

# #     server_socket = socket.socket()  # get instance
# #     # look closely. The bind() function takes tuple as argument
# #     server_socket.bind((host, port))  # bind host address and port together

# #     # configure how many client the server can listen simultaneously
# #     server_socket.listen(2)
# #     conn, address = server_socket.accept()  # accept new connection
# #     print("Connection from: " + str(address))
# #     for i in range(len(s)):
# #         conn.send(str(s[i]).encode())  # send data to the client
# #     conn.send("bye".encode())

# #     conn.close() 