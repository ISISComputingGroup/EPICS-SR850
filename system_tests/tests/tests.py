import unittest

from parameterized import parameterized
from utils.channel_access import ChannelAccess
from utils.ioc_launcher import get_default_ioc_dir
from utils.test_modes import TestModes
from utils.testing import get_running_lewis_and_ioc, skip_if_recsim

DEVICE_PREFIX = "SR850_01"


IOCS = [
    {
        "name": DEVICE_PREFIX,
        "directory": get_default_ioc_dir("SR850"),
        "macros": {},
        "emulator": "sr850",
    },
]


TEST_MODES = [TestModes.RECSIM, TestModes.DEVSIM]


class Sr850Tests(unittest.TestCase):
    """
    Tests for the _Device_ IOC.
    """
    def setUp(self):
        self._lewis, self._ioc = get_running_lewis_and_ioc("sr850", DEVICE_PREFIX)
        self.ca = ChannelAccess(device_prefix=DEVICE_PREFIX)
        
    @skip_if_recsim("Requires lewis backdoor")
    def test_that_IDN_IS_RETURNED(self):
        value = "SR850"
        self._lewis.backdoor_set_on_device("identifier", value)
        self.ca.process_pv("IDN")
        self.ca.assert_that_pv_is("IDN", value)

    @skip_if_recsim("Requires lewis backdoor")
    def test_that_OUTPX_IS_RETURNED(self):
        self._lewis.backdoor_set_on_device("outpx", 2.5001)
        self.ca.assert_that_pv_is("OUTPX", 2.5001)

    @skip_if_recsim("Requires lewis backdoor")
    def test_that_OUTPY_IS_RETURNED(self):
        self._lewis.backdoor_set_on_device("outpy", 2.5002)
        self.ca.assert_that_pv_is("OUTPY", 2.5002) 

    @skip_if_recsim("Requires lewis backdoor")
    def test_that_OUTPR_IS_RETURNED(self):
        self._lewis.backdoor_set_on_device("outpr", 2.5003)
        self.ca.assert_that_pv_is("OUTPR", 2.5003)

    @skip_if_recsim("Requires lewis backdoor")        
    def test_that_OUTPT_IS_RETURNED(self):
        self._lewis.backdoor_set_on_device("outpt", 2.5004)
        self.ca.assert_that_pv_is("OUTPT", 2.5004)

    @skip_if_recsim("Requires lewis backdoor")
    def test_that_FREQ_IS_RETURNED(self):
        self._lewis.backdoor_set_on_device("freq", 1000)
        self.ca.assert_that_pv_is("FREQ", 1000)

    def test_that_FREQ_IS_CHANGED(self):
        self.ca.set_pv_value("FREQ:SP", 500.0)
        self.ca.assert_that_pv_is("FREQ", 500.0)

    @parameterized.expand([505.50, 606.0, 700])
    def test_that_WHEN_Freq_is_set_THEN_value_matches(self, freq):
        self.ca.assert_setting_setpoint_sets_readback(freq, readback_pv="FREQ", set_point_pv="FREQ:SP")
