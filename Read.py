import serial
import serial.tools.list_ports

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if 'Arduino' in port.description:
            return port.device
    raise IOError("Arduino not found.")

def read_button_state():
    port = find_arduino_port()
    with serial.Serial(port, 9600, timeout=1) as ser:
        print("Connected to Arduino on", port)
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode().strip()
                if line:
                    print("Arduino:", line)

if __name__ == "__main__":
    read_button_state()
