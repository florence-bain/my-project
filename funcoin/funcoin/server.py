import asyncio
from asyncio.exceptions import IncompleteReadError
from asyncio.streams import StreamReader, StreamWriter

from my_server import ConnectionPool


class Server:
    def __init__(self,blockchain, connection_pool, p2p_protocol):

        async def get_external_ip(self):
        #finds external IP 
          async def handle_connection(self, reader: StreamReader, writer: StreamWriter):
              #writer object represents connection peer
              while True:
                  try:
                      #handle or respond to the incoming data
                      except (asyncio.expections.IncompleteReadError, ConnectionPool):
                        break
                    #if an error break the wait loop 
                    async def listen(self, hostname ="0.0.0.0", port=8888):

                        server = await asyncio.start_server(self.handle_connection, hostname, port)
                        logger.info(f"Server listening on {hostname}:{port}")
                        async with server:
                            await server.serve_forever()