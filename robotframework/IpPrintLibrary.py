from printip.ip_print import PrintIp


class IpPrintLibrary(object):
    """Test library for testing *IpPrint* business logic.

    Interacts with the ipprint directly using its ``print_ip`` method.
    """

    def __init__(self):
        
        self._result = ''

    def print_ip(self, fileLocation):
        """Print the ip from provided ``json`` file.

        json filename is passed to the print_ip directly.

        Example:
        | Print ip | ../examples/input1.json |
        """
        printip = PrintIp(fileLocation)
        self._result = printip.print_ip()

    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Print ip | ../examples/input1.json |
        | Result Should Be | 0       |
        """
        if self._result != int(expected):
            raise AssertionError('%s != %s' % (self._result, expected))