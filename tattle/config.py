import socket


def _default_node_name():
    return socket.gethostname()


class Configuration(object):
    def __init__(self):
        self.node_name = None
        self.node_address = None
        self.node_port = None
        self.bind_address = None
        self.bind_port = None
        self.api_address = None
        self.api_port = None
        self.retransmit_multi = None
        self.probe_interval = None
        self.probe_timeout = None
        self.probe_indirect_nodes = None
        self.sync_interval = None
        self.sync_nodes = None
        self.suspicion_min_timeout_multi = None
        self.suspicion_max_timeout_multi = None


class DefaultConfiguration(Configuration):
    def __init__(self):
        super(DefaultConfiguration, self).__init__()

        self.bind_address = '127.0.0.1'
        self.bind_port = 7900
        self.api_address = '127.0.0.1'
        self.api_port = 7800
        self.retransmit_multi = 3
        self.probe_interval = 100
        self.probe_timeout = 50
        self.probe_indirect_nodes = 3
        self.sync_interval = 10000
        self.sync_nodes = 1
        self.suspicion_min_timeout_multi = 5
        self.suspicion_max_timeout_multi = 6

        if self.node_name is None:
            self.node_name = _default_node_name()


def init_config():
    return DefaultConfiguration()
