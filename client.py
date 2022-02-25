import socket
import sys
import socket_methods


cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect((sys.argv[1], int(sys.argv[2])))

try:
    filename = sys.argv[4]
    command = sys.argv[3]
    message = command + " " + filename
except:
    command = sys.argv[3]
    message = command
    filename = "N/A"

cli_sock.sendall(message.encode('utf-8'))

if command == "put":
    status = socket_methods.send_file(cli_sock, filename, "")
elif command == "get":
    status = socket_methods.recv_file(cli_sock, filename, """\..\client_files\\""")
elif command == "list":
    status = socket_methods.recv_listing(cli_sock)
else:
    raise ("command not given")
try:
    print("IP: " + socket.gethostbyname(socket.gethostname()) + "  Port: " + sys.argv[2] + "  Command: " + command + "  Filename: " + filename + "  Status: " + status)
except:
    print("Error")
cli_sock.close()