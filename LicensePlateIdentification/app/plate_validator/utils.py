import serial
import time

def send_signal_to_arduino():

    port = 'COM3'  
    baud_rate = 115200  

    try:
        
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)

        ser.write(b'activate\n')

        ser.close()
    except serial.SerialException as e:
        print(f"Serial communication error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")