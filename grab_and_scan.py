from port_scanner import Scanner
from grabber import Grabber
from utils import timefunc

@timefunc
def main():
    ip = '192.168.42.42'
    portrange = (1, 65535)
    scanner = Scanner(ip)
    scanner.scan(*portrange)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print('Result is {} on port: {}'.format(grabber.read(), port ))
            grabber.close()
        except Exception as e:
            print('Result is Blocking on port: {}'.format(port))

if __name__ == '__main__':
    main()
