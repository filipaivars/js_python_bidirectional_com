# Note this is targeted at python 3
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.websocket
import tornado.options

import communication

LISTEN_PORT = 8770
LISTEN_ADDRESS = 'localhost'


class MainHandler(tornado.websocket.WebSocketHandler):
    """
    Handler that handles a websocket channel
    """

    @classmethod
    def urls(cls):
        return [
            (r'/', cls, {}),  # Route/Handler/kwargs
        ]

    def initialize(self):
        #self.channel = None
        print("initializing")

    #def open(self, channel):
    def open(self):
        """
        Client opens a websocket
        """
        #self.channel = channel
        print("websocket opened")

    def on_message(self, message):
        """
        Message received on channel
        """
        print("message received: " + message)
        self.write_message(u"You said: " + message)
        #engine_AI.sendamessage(self)
        print("message sent")

    def on_close(self):
        """
        Channel is closed
        """
        print("closing")

    def check_origin(self, origin):
        """
        Override the origin check if needed
        """
        #print("origin")
        #print(origin)
        return True


def main():
    # Create tornado application and supply URL routes
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])

    # Setup HTTP Server
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(LISTEN_PORT, LISTEN_ADDRESS)

    # Start IO/Event loop
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()