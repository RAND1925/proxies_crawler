from dataclasses import dataclass

from enum import Enum


@dataclass
class Proxy:

    class Protocol(Enum):
        HTTP = 'http'
        HTTPS = 'https'
        SOCK4 = 'sock4'
        SOCK5 = 'sock5'

    ip: str = '0.0.0.0'
    port: str = '80'
    protocol: Protocol = 'http'

    def format(self):
        assert len(self.ip.split('.')) == 4
        return f'{self.protocol.value}://{self.ip}:{self.port}'

    def __str__(self):
        return self.format()

