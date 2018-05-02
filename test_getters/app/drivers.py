from app.exceptions import MissingData
from napalm.ios import IOSDriver
import re


class DummyDevice:

    def __init__(self, data):
        self.data = data

    def send_command(self, command):
        label = re.sub(r'[\[\]\*\^\+\s\|]', '_', command)
        if label not in self.data:
            raise MissingData(command)
        return self.data[label]


class OfflineIOSDriver(IOSDriver):

    def __init__(self, data):
        self.device = DummyDevice(data)
        pass

    def open(self):
        pass

test_drivers = {
    'ios': OfflineIOSDriver
}
