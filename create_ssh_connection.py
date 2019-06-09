import paramiko

def main():
    ip = '192.168.42.42'
    username = 'root'
    password = 'vagrant'
    timeout = 5
    client_policy = paramiko.AutoAddPolicy()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(client_policy)
    try:
        client.connect(ip, username=username, password=password, timeout=timeout)
        print(client)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
