import socket
import time

class ClientError(Exception):
    pass

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self,metric_name, metric_value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))
        request = f'put {metric_name} {metric_value} {timestamp}\n'
        try:
            sock = socket.create_connection((self.host,self.port),self.timeout)
            sock.sendall(request.encode())
            # conn, addr = sock.accept()
            data = sock.recv(1024)
            if data.decode('utf8') != 'ok\n\n':
                raise ClientError
        except Exception:
            raise ClientError

    def get(self, key):

        def make_dict(str):
            # print(f'|||data|||: {str}')
            dict_answer = {}
            answer = str.split('\n')
            if answer[0] == 'error':
                raise ClientError
            elif answer[0]=='ok' and len(answer)==3:
                return {}
            for i in range(1,len(answer)-2):
                metric = answer[i].split(' ')
                key = metric[0]
                value = float(metric[1])
                timestamp = int(metric[2])
                key_tuple = (timestamp, value)
                # print(f'value:{value}   timestamp: {timestamp}')
                # print(f'key: {key}|||tuple: {key_tuple}')
                if key in [*dict_answer]:#не создается нормально список пар
                    dict_answer[key].append(key_tuple)
                else:
                    dict_answer[key] = [key_tuple]
            # print(f'|||before sort|||: {dict_answer}')
            # if len(dict_answer) == 0:
            #     return {}
            for i in dict_answer:
                dict_answer[i] = sorted(dict_answer[i], key = lambda element : element[0])
            return dict_answer

        request = f'get {key}\n'
        dict_answer = {}
        try:
            sock = socket.create_connection((self.host,self.port),self.timeout)
            sock.sendall(request.encode())
            #conn, addr = sock.accept()
            data = sock.recv(1024)
            dict_answer = make_dict(data.decode())
        except Exception:
            raise ClientError

        return dict_answer



#
# def main():
#     my_dict = make_dict(f'ok\ntest 0.5 1\ntest 0.4 2\nload 301 3\n\n')
#     print(my_dict)
#
# if __name__ == '__main__':
#     main()