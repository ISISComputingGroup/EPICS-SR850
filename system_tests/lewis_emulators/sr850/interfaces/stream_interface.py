from lewis.adapters.stream import StreamInterface, Cmd
from lewis.utils.command_builder import CmdBuilder
from lewis.core.logging import has_log
from lewis.utils.replies import conditional_reply


@has_log
class Sr850StreamInterface(StreamInterface):
    
    in_terminator = "\r\n"
    out_terminator = "\r"

    def __init__(self):
        super(Sr850StreamInterface, self).__init__()
        # Commands that we expect via serial during normal operation
        self.commands = {
            CmdBuilder("set_remote").escape("LOCL ").int().eos().build(),
            CmdBuilder("set_freq").escape("FREQ ").float().eos().build(),
            CmdBuilder("get_idn").escape("*IDN?").eos().build(),
            CmdBuilder("get_outpx").escape("OUTP? 1").eos().build(),
            CmdBuilder("get_outpy").escape("OUTP? 2").eos().build(),
            CmdBuilder("get_outpr").escape("OUTP? 3").eos().build(),
            CmdBuilder("get_outpt").escape("OUTP? 4").eos().build(),
            CmdBuilder("get_freq").escape("FREQ?").eos().build()
        }

    def handle_error(self, request, error):
        """
        If command is not recognised print and error

        Args:
            request: requested string
            error: problem

        """
        self.log.error("An error occurred at request " + repr(request) + ": " + repr(error))
    def set_remote(self, remote):
        self.device.local = remote

    def set_freq(self, freq):
        self.device.freq = freq
        
    def get_idn(self):
        return self.device.identifier

    def get_outpx(self):
        return self.device.outpx

    def get_outpy(self):
        return self.device.outpy

    def get_outpr(self):
        return self.device.outpr

    def get_outpt(self):
        return self.device.outpt
 
    def get_freq(self):
        return self.device.freq
        
    def catch_all(self, command):
        pass
