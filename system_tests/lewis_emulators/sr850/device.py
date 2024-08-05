from collections import OrderedDict

from lewis.devices import StateMachineDevice

from .states import DefaultState


class SimulatedSr850(StateMachineDevice):

    def _initialize_data(self):
        """
        Initialize all of the device's attributes.
        """
        self.identifier = "Something"
        self.outpx = 1.5001
        self.outpy = 1.5002
        self.outpr = 1.5003
        self.outpt = 1.5004
        self.local = 1
        self.freq  = 10100

    def _get_state_handlers(self):
        return {
            'default': DefaultState(),
        }

    def _get_initial_state(self):
        return 'default'

    def _get_transition_handlers(self):
        return OrderedDict([])
