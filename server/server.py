import socket
import sys
import mysql.connector

pressureDatabase = mysql.connector.connect(
        host = "localhost", 
        user = "yourusername",
        password = "yourpassword"
)

cursor = pressureDatabase.cursor()
cursor.execute("Create Database Pressure Database")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = ('local host', 8000);
print >>sys.stderr, 'starting up on %s port %s' % serverAddress
sock.bind(serverAddress)

sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, clientAddress = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()