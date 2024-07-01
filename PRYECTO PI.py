"""from machine import Pin, I2C
import utime
import math

# Configuración de pines
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(3, Pin.OUT)
buzzer = Pin(4, Pin.OUT)

# Configuración I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Dirección I2C del ADXL345
ADXL345_ADDR = 0x53

# Funciones de configuración y lectura del ADXL345
def init_adxl345():
    i2c.writeto_mem(ADXL345_ADDR, 0x2D, b'\x08')  # Poner el sensor en modo de medición
    i2c.writeto_mem(ADXL345_ADDR, 0x31, b'\x08')  # Rango +/- 2g, 10 bits

def read_adxl345():
    data = i2c.readfrom_mem(ADXL345_ADDR, 0x32, 6)
    x = int.from_bytes(data[0:2], 'little', signed=True)
    y = int.from_bytes(data[2:4], 'little', signed=True)
    z = int.from_bytes(data[4:6], 'little', signed=True)
    return x, y, z

def calculate_angle(x, y, z):
    # Convertir las lecturas a g (considerando 256 LSB/g para +/- 2g)
    x_g = x / 256
    # Calcular el ángulo en grados en el eje X
    angle_x = math.degrees(math.atan2(x_g, math.sqrt(y ** 2 + z ** 2)))
    return angle_x

# Inicializar el ADXL345 (giroscopio)
init_adxl345()

while True:
    x, y, z = read_adxl345()   
    angle_x = calculate_angle(x, y, z)
    
    # Controlar LEDs y buzzer basado en el ángulo
    if angle_x >= 20 and angle_x <= 40:
        led_amarillo.on()
        led_rojo.off()
        buzzer.off()
    elif angle_x > 40:
        led_amarillo.off()
        led_rojo.on()
        buzzer.on()
    else:
        led_amarillo.off()
        led_rojo.off()
        buzzer.off()
    
    # Imprimir el ángulo para monitoreo
    print("Angle X: {:.2f}".format(angle_x))
    
    utime.sleep(0.1)"""


from machine import Pin, I2C
import utime
import math
import struct

# Configuración de pines
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(3, Pin.OUT)
buzzer = Pin(4, Pin.OUT)

# Configuración I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Dirección I2C del ADXL345
ADXL345_ADDR = 0x53

# Funciones de configuración y lectura del ADXL345
def init_adxl345():
    i2c.writeto_mem(ADXL345_ADDR, 0x2D, b'\x08')  # Poner el sensor en modo de medición
    i2c.writeto_mem(ADXL345_ADDR, 0x31, b'\x08')  # Rango +/- 2g, 10 bits

def read_adxl345():
    try:
        # Leer datos del eje X (registros 0x32 y 0x33)
        data_x = i2c.readfrom_mem(ADXL345_ADDR, 0x32, 2)
        x = struct.unpack('<h', data_x)[0]  # Convertir los bytes a un entero con signo de 16 bits
        
        # Leer datos del eje Y (registros 0x34 y 0x35)
        data_y = i2c.readfrom_mem(ADXL345_ADDR, 0x34, 2)
        y = struct.unpack('<h', data_y)[0]  # Convertir los bytes a un entero con signo de 16 bits
        
        # Leer datos del eje Z (registros 0x36 y 0x37)
        data_z = i2c.readfrom_mem(ADXL345_ADDR, 0x36, 2)
        z = struct.unpack('<h', data_z)[0]  # Convertir los bytes a un entero con signo de 16 bits
        
        return x, y, z
    except OSError as e:
        print("Error al leer datos del ADXL345:", e)
        return None, a, None

def calculate_angle(x, y, z):
    # Convertir las lecturas a g (considerando 256 LSB/g para +/- 2g)
    x_g = x / 256
    y_g = y /256
    z_g = z / 256
    # Calcular el ángulo en grados en el eje X
    angle_x = math.degrees(math.atan2(x_g, math.sqrt(y_g ** 2 + z_g ** 2)))
    return angle_x

# Inicializar el ADXL345 (giroscopio)
init_adxl345()

while True:
    x, y, z = read_adxl345()   
    angle_x = calculate_angle(x, y, z)
    print("Angle X: {:.2f}".format(angle_x))
    if angle_x < 0:
        angle_x = -angle_x
    # Controlar LEDs y buzzer basado en el ángulo
    if angle_x >= 20 and angle_x <= 40:
        led_amarillo.on()
        led_rojo.off()
        buzzer.off()
    elif angle_x > 40:
        led_amarillo.off()
        led_rojo.on()
        buzzer.on()
    else:
        led_amarillo.off()
        led_rojo.off()
        buzzer.off()
    
    # Imprimir el ángulo para monitoreo
    
    utime.sleep(0.1)

from machine import Pin, I2C
import utime
import math
import struct

# Configuración de pines
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(3, Pin.OUT)
buzzer = Pin(4, Pin.OUT)

# Configuración I2C
# i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=1_000_000)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
# Dirección I2C del ADXL345
ADXL345_ADDR = 0x53

# Funciones de configuración y lectura del ADXL345
def init_adxl345():
    i2c.writeto_mem(ADXL345_ADDR, 0x2D, b'\x08')  # Poner el sensor en modo de medición
    i2c.writeto_mem(ADXL345_ADDR, 0x31, b'\x08')  # Rango +/- 2g, 10 bits

def read_adxl345():
    try:
        # Leer datos del eje X (registros 0x32 y 0x33)
        data_x = i2c.readfrom_mem(ADXL345_ADDR, 0x32, 2)
        x = struct.unpack('<h', data_x)[0]  # Convertir los bytes a un entero con signo de 16 bits
        
        # Leer datos del eje Y (registros 0x34 y 0x35)
        data_y = i2c.readfrom_mem(ADXL345_ADDR, 0x34, 2)
        y = struct.unpack('<h', data_y)[0]  # Convertir los bytes a un entero con signo de 16 bits
        
        # Leer datos del eje Z (registros 0x36 y 0x37)
        data_z = i2c.readfrom_mem(ADXL345_ADDR, 0x36, 2)
        z = struct.unpack('<h', data_z)[0]  # Convertir los bytes a un entero con signo de 16 bits
        
        return x, y, z
    except OSError as e:
        print("Error al leer datos del ADXL345:", e)
        return None, a, None

def calculate_angle(x, y, z):
    # Convertir las lecturas a g (considerando 256 LSB/g para +/- 2g)
    x_g = x / 256
    y_g = y /256
    z_g = z / 256
    # Calcular el ángulo en grados en el eje X
    angle_x = math.degrees(math.atan2(x_g, math.sqrt(y_g ** 2 + z_g ** 2)))
    return angle_x

# Inicializar el ADXL345 (giroscopio)
init_adxl345()

while True:
    x, y, z = read_adxl345()   
    angle_x = calculate_angle(x, y, z)
    print("Angle X: {:.2f}".format(angle_x))
    if angle_x < 0:
        angle_x = -angle_x
    # Controlar LEDs y buzzer basado en el ángulo
    if angle_x >= 5 and angle_x <= 25:
        led_amarillo.on()
        led_rojo.off()
        buzzer.on()
    elif angle_x > 25:
        led_amarillo.off()
        led_rojo.on()
        buzzer.on()
    else:
        led_amarillo.off()
        led_rojo.off()
        buzzer.on()
    
    # Imprimir el ángulo para monitoreo
    
    utime.sleep(0.1)

