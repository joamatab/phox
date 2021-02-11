class LightwaveMultimeterHP8163A(SerialMixin):
    def __init__(self, port: str = '/dev/ttyUSB1', source_idx: int = 0):
        self.source_idx = source_idx
        SerialMixin.__init__(self,
                             port=port,
                             id_command='*IDN?',
                             id_response='HP8164A',
                             terminator='\r'
                             )
    def setup(self):
        self.write('++auto 1')
        self.write('++addr 9')