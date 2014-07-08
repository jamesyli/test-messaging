from oslo import messaging
from oslo.config import cfg
from common.utility import *
from openstack.common import log as logging
import logging as std_logging
import sys

LOG = logging.getLogger(__name__)


if __name__ == '__main__':
    cfg.CONF(sys.argv[1:], project='solum')
    logging.setup('solum')
    cfg.CONF.log_opt_values(LOG, std_logging.DEBUG)

    serializer = RequestContextSerializer(JsonPayloadSerializer())
    transport = messaging.get_transport(cfg.CONF,
                                        aliases=TRANSPORT_ALIASES)
    topic = 'server-test'
    target = messaging.Target(topic=topic)
    client = messaging.RPCClient(transport, target,
                                       serializer=serializer)
    client.cast({}, 'echo')
