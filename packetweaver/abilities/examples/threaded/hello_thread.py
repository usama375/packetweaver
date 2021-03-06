from packetweaver.core import ns
import time


class Ability(ns.ThreadedAbilityBase):
    _info = ns.AbilityInfo(
        name='Hello from a thread',
        description='Display an hello message and wait to be stopped to exit',
    )

    _option_list = [
        ns.StrOpt('msg',
                  default='Hi there',
                  comment='hello message to display'),
        ns.NumOpt('sleep_time',
                  default=2,
                  comment='Time to wait before displaying the hello message')
    ]

    def main(self):
        time.sleep(self.sleep_time)
        self._view.info('{}!'.format(self.msg).capitalize())
        self._view.warning('Hit Ctrl+c to stop me')
        self._wait()
        self._view.info('Ctrl+c received, exiting…')
        return 'Done'

    def howto(self):
        self._view.delimiter('Hello')
        self._view.info("""
        Display an hello message passed in argument after a defined time.
        It will then hang until receiving a ctrl+c interrupt.
        """)
