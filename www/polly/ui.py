# If the module is invoked directly, initialize the application                                                       |
if __name__ == '__main__':                                                                                            |
    # Create and configure the HTTP server instance                                                                   |
    server = ThreadedHTTPServer((arguments.host, arguments.port),                                                     |
                                ChunkedHTTPRequestHandler)                                                            |
    print("Starting server, use <Ctrl-C> to stop...")                                                                 |
    print(u"Open {0}://{1}:{2}{3} in a web browser.".format(PROTOCOL,                                                 |
                                                            arguments.host,                                           |
                                                            arguments.port,                                           |
                                                            ROUTE_INDEX))                                             |
                                                                                                                      |
    try:                                                                                                              |
        # Listen for requests indefinitely                                                                            |
        server.serve_forever()                                                                                        |
    except KeyboardInterrupt:                                                                                         |
        # A request to terminate has been received, stop the server                                                   |
        print("\nShutting down...")                                                                                   |
        server.socket.close()                                                                                     
# If the module is invoked directly, initialize the application                                                       
if __name__ == '__main__':                                                                                            |
    # Create and configure the HTTP server instance                                                                   |
    server = ThreadedHTTPServer((arguments.host, arguments.port),                                                     |
                                ChunkedHTTPRequestHandler)                                                            |
    print("Starting server, use <Ctrl-C> to stop...")                                                                 |
    print(u"Open {0}://{1}:{2}{3} in a web browser.".format(PROTOCOL,                                                 |
                                                            arguments.host,                                           |
                                                            arguments.port,                                           |
                                                            ROUTE_INDEX))                                             |
                                                                                                                      |
    try:                                                                                                              |
        # Listen for requests indefinitely                                                                            |
        server.serve_forever()                                                                                        |
    except KeyboardInterrupt:                                                                                         |
        # A request to terminate has been received, stop the server                                                   |
        print("\nShutting down...")                                                                                   |
        server.socket.close()                                                                                         |
                                          
