import re
ipv4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
ipv6 = '''(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|
([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:)
{1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1
,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}
:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{
1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA
-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a
-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0
-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,
4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}
:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9
])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0
-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]
|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]
|1{0,1}[0-9]){0,1}[0-9]))'''
def find(Ip):
    if re.search(ipv4, Ip):
        print("IPv4")
    elif re.search(ipv6, Ip):
        print("IPv6")
    else:
        print("None")
# Driver Code
if __name__ == '__main__' :
    # Enter the Ip address
    Ip = "192.168.0.100"
    find(Ip)



# nano checkreservedip.py
#
# Add the following code:
#
# from ipaddress import ip_address
#
# def reservedIPAddress(IP: str) -> str:
# return "Reserved" if (ip_address(IP).is_reserved) else "Not Reserved"
#
# if __name__ == '__main__' :
#
# # Not Reserved
# print(reservedIPAddress('192.168.0.123'))
#
# # Reserved
# print(reservedIPAddress('240.0.0.20'))