import asyncio

METRICS = {}# recieving data storage

class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = data.decode()
        splitted_resp = resp.split(' ')

        if splitted_resp[0] == 'get':
            answer = self.get(splitted_resp)

        elif splitted_resp[0] == 'put':
            answer = self.put(splitted_resp)

        else:
            answer = 'error\nwrong command\n\n'

        # print(f"I'm OK {resp}")
        print(answer)
        self.transport.write(answer.encode())

    def get(self, spl_resp):

        if len(spl_resp) != 2:
            return 'error\nwrong command\n\n'
        # answer = ''
        key = spl_resp[1][0]
        list_answ = []
        if key == '*':
            # print(f'TAKE THEM ALL')
            # print(METRICS)
            for el in METRICS:
                list_answ.extend(METRICS[el])
        else:
            if key != '*' and key not in METRICS:
                return 'ok\n\n'
            else:
                list_answ.extend(METRICS[key])

        res = 'ok\n'+''.join(list_answ)+'\n'
        return res



    def put(self, spl_resp):

        if len(spl_resp) != 4:
            return 'error\nwrong command\n\n'

        key = spl_resp[1]

        info = ' '.join(spl_resp[1:])
        if key not in METRICS:
            METRICS[key] = [info]
        else:
            if info not in METRICS[key]:
                METRICS[key].append(info)

        # print(METRICS)

        return 'ok\n\n'




def run_server(host='127.0.0.1', port=8888):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == '__main__':
    run_server()

