import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    '''
    Function creates the client socket and transmits messages from the user
    '''
    server_address = ('localhost', 10000)
    sock = socket.socket() # this is an IPv4, TCP socket (using default values)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    sock.connect(server_address) 

    received_message = ''

    try:
        print('sending "{0}"'.format(msg), file=log_buffer)

        sock.sendall(msg.encode('utf-8'))

        while True:
            chunk = ''
            chunk = sock.recv(16)
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            received_message += chunk.decode('utf8')
            if len(chunk.decode('utf8'))<16:
                break    
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        sock.close()
        print('closing socket', file=log_buffer)
        return received_message 


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
