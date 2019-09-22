import socket
import time
import os

check_flag = True

while check_flag:
    try:
        soc_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        check_flag = False

    except Exception as e:
        check_flag = True
        print("Error while Open Socket :: %s" % e)
        print("Open Socket : Failed")
        print("It will try after 2 seconds")
        time.sleep(2)

print("Open Socket : Clear")

check_flag = True

while check_flag:
    try:
        soc_client.connect(('127.0.0.1', 4000))
        check_flag = False

    except Exception as e:
        check_flag = True
        print("Error while Connect to Server :: %s" % e)
        print("Connect to Server : Failed")
        print("It will try after 2 seconds")
        time.sleep(2)

print("Connect to Server : Clear")

while True:
    file = input(str("File Name : "))

    try:
        f = open(file, "rb")
        check_flag = True

    except Exception as e:
        check_flag = False
        print("Error while Open the file :: %s" % e)
        print("Open the file : Failed")
        print("Try to Enter Correct File Name")

    if check_flag is True:
        file_size = os.path.getsize(file)

        if file_size > 0:
            soc_client.send(bytes(file, 'utf-8'))
            break
        else:
            check_flag = False
            print("FILE SIZE : ", file_size)
            print("The file is empty.")
            print("That will be not working")
            f.close()

MAX_DATA_SIZE = 1024

while True:
    end_flag = False
    utf_data = f.read().decode('utf-8')
    len_data = len(utf_data)
    total_count = (len_data // MAX_DATA_SIZE) + 1

    data_array = []

    for i in range(0, total_count):
        index = i * MAX_DATA_SIZE

        if i == (total_count - 1):
            data_array.append(utf_data[index:])
            end_flag = True

        else:
            data_array.append(utf_data[index : index + MAX_DATA_SIZE])

    if end_flag:
        break

for i in data_array:
    soc_client.send(i.encode('utf-8'))

print("Send All Data")
