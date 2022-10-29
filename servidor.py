from xmlrpc.server import SimpleXMLRPCServer

def eh_par(n):

    print("Argumento recebido: " + str(n))
    return n % 2 == 0

server = SimpleXMLRPCServer (( "localhost", 8050))
print("Escutando na porta 8050...")
server.register_function( eh_par, "eh_par")
server.serve_forever()


