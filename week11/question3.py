def GetIpaddress():
    while True:
        try:
            ip = input("Please enter an IP address:")
            if "." in ip:
                test = ip.split(".")
            else:
                raise ValueError("You need to enter . to seperate the input IP")
            if len(test) !=4:
                raise ValueError ("Not a valid IP, the length of IP is not a legitimate length")
            if test[0] == 0:
                raise ValueError("0 can not be used as the first number in IP address")
            for x in test:
                x = int(x)
                if x >255 or x <0:
                    raise ValueError("The number is not in the valid IP range")
            print (ip)
            return ip
        except ValueError as err:
            print(err)   
GetIpaddress()