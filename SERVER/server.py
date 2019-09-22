import socket
import time

check_flag = True

while check_flag:
    try:
        soc_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        soc_server.bind(('0.0.0.0', 4000))
        check_flag = False
    except Exception as e:
        check_flag = True
        print("Error while Binding :: %s" % e)
        print("Binding : Failed")
        print("It will try after 2 seconds")
        time.sleep(2)


print("Binding : Clear")

soc_server.listen(1)

while True:
    error_flag = False

    while True:
        print("Wait for a Connection")
        connection, client_address = soc_server.accept()
        print("Connected - IP : %s / Port : %s" % (client_address[0], client_address[1]))
        break

    file_name_flag = False

    file_data = []

    while True:
        try:
            data, addr = connection.recvfrom(1024)
        except Exception as e:
            print("Error : %s" % e)
            error_flag = True
            break

        print("Receive Raw Data : ", data)

        if file_name_flag is False:
            file_name = data
            file_name_flag = True

        else:
            file_data.append(data)
            print("File : ", file_data)
            if len(data) < 1024:
                break

    if error_flag is False:
        file_error_count = 0

        while True:
            try:
                f = open(file_name, 'wb')
                error_flag = False

            except Exception as e:
                error_flag = True
                file_error_count = file_error_count + 1
                print("File Open Error : %s" % e)
                print("File Open : Failed")
                if file_error_count > 5:
                    print("Too many Failed to Open file...")
                    print("Go to First Section")
                    break

                print("It will try after 2 seconds")
                time.sleep(2)

            if error_flag is False:
                break

        if error_flag is False:
            text = bytearray()
            for i in file_data:
                text.extend(i)

            f.write(text)
            f.close()

            print("Saved File")
