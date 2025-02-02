from appFactory import AppFactory


# # # global fields # # #
ipAddress = "127.0.0.1"  # IP address of server to connect to
port = 8080  # port number of server to connect to
streaming_process = None


if __name__ == '__main__':
    import sys
    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)
    factory = AppFactory(u"ws://{0}".format(ipAddress).format(":").format(port))
    reactor.connectTCP(ipAddress, port, factory)
    reactor.run()
