class Handler:
    def __init__(self):
        self.next_handler = None
    def setNext(self, _handler):
        self.next_handler = _handler 
    def handle(self, _req): 
        if self.next_handler:
            self.next_handler.handle(req)
        else:
            print("there isn't any next handler")

class CashHandler(Handler):
    def handle(self, _req):
        if _req['method'] == 'cash':
            _method = _req['method']
            _pay = _req['pay']
            print(f'{_method} is {_pay}')
        else:
            super().handle(_req)

class DebitHandler(Handler):
    def handle(self, _req):
        if _req['method'] == 'debit':
            _method = _req['method']
            _pay = _req['pay']
            print(f'{_method} is {_pay}')
        else:
            super().handle(_req)

class CreditHandler(Handler):
    def handle(self, _req):
        if _req['method'] == 'credit':
            _method = _req['method']
            _pay = _req['pay']
            print(f'{_method} is {_pay}')
        else:
            super().handle(_req)


if __name__ == '__main__':
    cashHandler = CashHandler()
    debitHandler = DebitHandler()
    creditHandler = CreditHandler()
    cashHandler.setNext(debitHandler)
    debitHandler.setNext(creditHandler)
    req = {
            'method': 'credit',
            'pay': 1000
            }
    cashHandler.handle(req)

