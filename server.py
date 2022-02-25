import socket
import sys
import socket_methods


srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.bind(("", int(sys.argv[1])))
srv_sock.listen(5)
while True:
    cli_sock, cli_addr = srv_sock.accept()
    request = cli_sock.recv(1024)
    message = (request.decode('utf-8'))
    message = message.split(" ")
    command = message[0]
    if (len(message) == 2):
        filename = message[1]
    if command == "put":
        socket_methods.recv_file(cli_sock,filename, """\..\server_files\\""")
    elif command == "get":
        socket_methods.send_file(cli_sock,filename, """\..\server_files\\""")
    elif command == "list":
        socket_methods.send_listing(cli_sock)
    else:
        raise ("command not given")
    cli_sock.close()