import ipaddress
print("IP Class Identifier")
while True:
    ip_input = input("Enter the IP: ")
    try:
        ip = ipaddress.IPv4Address(ip_input)
        start_A = ipaddress.IPv4Address('1.0.0.0')
        end_A = ipaddress.IPv4Address('126.255.255.255')
        start_B = ipaddress.IPv4Address('128.0.0.0')
        end_B = ipaddress.IPv4Address('191.255.255.255')
        start_C = ipaddress.IPv4Address('192.0.0.0')
        end_C = ipaddress.IPv4Address('223.255.255.255')
        start_D = ipaddress.IPv4Address('224.0.0.0')
        end_D = ipaddress.IPv4Address('239.255.255.255')
        start_E = ipaddress.IPv4Address('240.0.0.0')
        end_E = ipaddress.IPv4Address('255.255.255.255')
        if start_A <= ip <= end_A:
            print("Class A Address")
        elif start_B <= ip <= end_B:
            print("Class B Address")
        elif start_C <= ip <= end_C:
            print("Class C Address")
        elif start_D <= ip <= end_D:
            print("Class D Address")
        elif start_E <= ip <= end_E:
            print("Class E Address")
        break
    except ipaddress.AddressValueError:
        print("Invalid IP, please try again.")
