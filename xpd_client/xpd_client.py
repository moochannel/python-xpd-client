import base64

from jsonrpc_requests import Server
from logzero import logger

from .commands import is_xpd_command


class XPdClient(object):

    def __init__(self, rpc_url, rpc_user, rpc_password):
        headers = {'Authorization': self.authenticate_str(rpc_user, rpc_password)}
        self.connection = Server(rpc_url, headers=headers)
        info = self.connection.getinfo()
        logger.debug('Connected to XPd (version: {0}) successfully'.format(info['version']))

    def __getattr__(self, name):
        if is_xpd_command(name):
            return getattr(self.connection, name)
        else:
            raise AttributeError(
                '\'{0}\' object has no attribute \'{1}\''.format(self, name))

    @classmethod
    def authenticate_str(cls, user, password):
        _auth_seed = ':'.join([user, password])
        _auth_b64 = base64.b64encode(_auth_seed.encode('utf-8')).decode('ascii')
        return 'Basic ' + _auth_b64
