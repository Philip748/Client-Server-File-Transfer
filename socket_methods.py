import sys
import socket
import os
import pickle

def recv_file(socket_, filename, path):
    filename = filename.split("\\")[-1]
    filename = sys.argv[0] + path + filename
    file = open(filename, "wb")
    request = socket_.recv(1024)
    while(request):
        file.write(request)
        request = socket_.recv(1024)
    print("Received file: " + filename)
    file.close()
    return "success"




def send_file(socket_, filename, path_):
    if path_ == """\..\server_files\\""":
        filename = sys.argv[0] + path_ + filename
    try:
        f = open(filename, "rb")
    except:
        return "Failure (File not found)"
    size = os.path.getsize(filename)
    try:
        perc = 0
        sent = 0
        br = f.read(1024)
        while (br):
            socket_.sendall(br)
            br = f.read(1024)
            sent += 1024
            nperc = sent / size * 100
            nperc = int(nperc)
            if nperc > perc:
                perc = nperc
                if perc > 100:
                    print("sending...(100%)")
                else:
                    print("sending...(" + str(perc) + "%)")
        print("sent")
        f.close()
        return "success"
    except:
        return "Failure (File not sent)"


def recv_listing(socket_):
    request = socket_.recv(1024)
    message = pickle.loads(request)
    for i in message:
        print (i)
    return "success"



def send_listing(socket_):
    files = os.listdir(sys.argv[0] + """\..\server_files""")
    data = pickle.dumps(files)
    socket_.sendall(data)
    return "success"