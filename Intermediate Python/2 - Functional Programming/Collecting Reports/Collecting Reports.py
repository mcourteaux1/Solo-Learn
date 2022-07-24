def decor(invoice):
    def wrap(num):
        print('***')
        invoice(num)
        print('***\nEND OF PAGE')
    return wrap

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input());