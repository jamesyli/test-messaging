
import logging as std_logging
import sys

from oslo import messaging
from oslo.config import cfg
from common.utility import *

from openstack.common import log as logging


LOG = logging.getLogger(__name__)

class Service(object):
    _server = None

    def __init__(self, topic, server, handlers):
        serializer = RequestContextSerializer(JsonPayloadSerializer())
        transport = messaging.get_transport(cfg.CONF,
                                            aliases=TRANSPORT_ALIASES)
        target = messaging.Target(topic=topic, server=server)
        self._server = messaging.get_rpc_server(transport, target, handlers,
                                                serializer=serializer)

    def serve(self):
        self._server.start()
        self._server.wait()


class Handler(object):
    def __init__(self):
        super(Handler, self).__init__()

    def echo(self, ctxt, message):
        LOG.debug("%s" % message)


def main():
    cfg.CONF(sys.argv[1:], project='solum')
    logging.setup('solum')
    LOG.debug("Configuration:")
    cfg.CONF.log_opt_values(LOG, std_logging.DEBUG)

    server = Service('server-test', 'localhost', [Handler()])
    server.serve()


if __name__ == '__main__':
    main()
