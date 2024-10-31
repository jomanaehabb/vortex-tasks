import serial
import serial.tools.list_ports

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if 'Arduino' in port.description:
            return port.device
    raise IOError("Arduino not found.")

def control_led():
    port = find_arduino_port()
    with serial.Serial(port, 9600, timeout=1) as ser:
        print("Connected to Arduino on", port)
        while True:
            command = input("Enter 'on' or 'off' to control LED (or 'quit' to exit): ").strip().lower()
            if command in ["on", "off"]:
                ser.write((command + '\n').encode())
                response = ser.readline().decode().strip()
                print("Arduino:", response)
            elif command == "quit":
                print("Exiting...")
                break
            else:
                print("Invalid command. Use 'on', 'off', or 'quit'.")

if __name__ == "__main__":
    control_led()
