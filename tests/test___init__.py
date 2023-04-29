from unittest import TestCase
import warnings

from berrynet.comm import Communicator, on_message


# 体会: 1. 如何做到将两个耦合的东西做到解耦, 分解 api 让二者不要相互牵制

class TestCommunicator(TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    # block loop
    def test_run(self):
        comm_config = {
            "client": "ABC",
            "password": "oBMEfJgd3XhaqrX8eibm",
            "broker": {
                "address": "demo.thingsboard.io",
                "port": 8083
            },
            "topic": "berrynet/image"
        }

        comm = Communicator(comm_config)

        comm.run()

    def test_start_nb(self):
        comm_config = {
            "client": "ABC",
            "password": "oBMEfJgd3XhaqrX8eibm",
            "broker": {
                "address": 'broker.emqx.io',
                "port": 1883
            },
            "topic": "/berrynet/image",
            "subscribe": {"/berrynet/image": ""},
        }

        comm = Communicator(comm_config)

        comm.start_nb()
        pay_load = {
            "id": "12345"
        }

        while True:
            comm.client.publish(comm_config["topic"], 1)

    def test_stop_nb(self):
        comm_config = {
            "client": "ABC",
            "password": "oBMEfJgd3XhaqrX8eibm",
            "broker": {
                "address": "demo.thingsboard.io",
                "port": 1883
            },
            "topic": "v1/devices/me/telemetry"
        }

        comm = Communicator(comm_config)

        comm.stop_nb()

    def test_send(self):
        comm_config = {
            "client": "ABC",
            "password": "oBMEfJgd3XhaqrX8eibm",
            "broker": {
                "address": "demo.thingsboard.io",
                "port": 1883
            },
            "topic": "v1/devices/me/telemetry"
        }

        comm = Communicator(comm_config)

        pay_load = {
            "id": "12345"
        }

        comm.send(comm_config["topic"], pay_load)
