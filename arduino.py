import glob
import serial
import sys


class Arduino:
    def __init__(self):
        self.arduinos = []
        self.arduino_ports = []
        self.ser = None

    def port_search(self):
        self.arduinos.clear()

        if sys.platform.startswith('win'):  # Windows
            ports = ['COM{0:1.0f}'.format(ii) for ii in range(1, 256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):  # Linux
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):  # MAC
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Machine not compatible')
        for port in ports:
            if len(port.split('Bluetooth')) > 1:
                continue
            try:
                ser = serial.Serial(port)
                ser.close()
                self.arduinos.append(port)
            except (OSError, serial.SerialException):
                pass
            return self.arduinos

    def arduino_connect(self):
        self.arduino_ports = self.port_search()
        if not len(self.arduino_ports) == 0:
            print(f"Arduino founded at port: {self.arduino_ports[0]}")
            self.ser = serial.Serial(self.arduino_ports[0], baudrate=115200)
            self.ser.flush()
            return self.arduino_ports
        else:
            print("Finding Arduino...")

    def get_data(self):
        try:
            ser_bytes = self.ser.readline()
        except AttributeError as e:
            print(f"AttributeError: {e}")
        else:
            decoded_bytes = ser_bytes.decode('utf-8')
            data = decoded_bytes.replace('\r', '').replace('\n', '')
            data = [float(n) for n in data.split(",")]
            return data
