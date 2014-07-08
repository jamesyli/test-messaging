from oslo import messaging
from openstack.common import jsonutils
from common import context as common_context

TRANSPORT_ALIASES = {
    'solum.openstack.common.rpc.impl_kombu': 'rabbit',
    'solum.openstack.common.rpc.impl_qpid': 'qpid',
    'solum.openstack.common.rpc.impl_zmq': 'zmq',
}


class JsonPayloadSerializer(messaging.NoOpSerializer):
    @staticmethod
    def serialize_entity(context, entity):
        return jsonutils.to_primitive(entity, convert_instances=True)


class RequestContextSerializer(messaging.Serializer):

    def __init__(self, base=None):
        self._base = base or messaging.NoOpSerializer()

    def serialize_entity(self, context, entity):
        if not self._base:
            return entity
        return self._base.serialize_entity(context, entity)

    def deserialize_entity(self, context, entity):
        if not self._base:
            return entity
        return self._base.deserialize_entity(context, entity)

    def serialize_context(self, context):
        return {}

    def deserialize_context(self, context):
        return common_context.RequestContext.from_dict(context)
