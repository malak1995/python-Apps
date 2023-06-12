import nmap

scsnner = nmap.PortScanner()
target = input('pleas enter an IP address : ')
scanner.scan(target,'1-1024','-sV')

print("the host name is : " + scsnner[target].hosyname())
print("the host state is : " + scsnner[target].state())