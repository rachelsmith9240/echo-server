'''
Module creates the server socket
'''

import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    '''
    This function creates and manages the server socket
    '''
    # address = ('127.0.0.1', 10000)
    address = ('localhost', 10000)
    sock = socket.socket() # TCP with IPv4 by default
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    sock.bind(address)
    sock.listen(1)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                while True:
                    data = conn.recv(16)
                    print('received "{0}"'.format(data.decode('utf8')))
                    conn.sendall(data)
                    print('sent "{0}"'.format(data.decode('utf8')))

                    if len(data.decode('utf8'))<16:
                        break
            except Exception:
                traceback.print_exc()
                sys.exit(1)
            finally:
                conn.close()
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        conn.close()
        print('quitting echo server', file=log_buffer)
        return


if __name__ == '__main__':
    server()
    sys.exit(0)
