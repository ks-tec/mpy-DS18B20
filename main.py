import machine, time
import ssd1306, ds18x20, onewire

ENABLE_OLED = True

def main():
  while True:
    show()
    time.sleep_ms(250)

def show():
  wtemp = read_ds18(750)            # water temperature

  print("W=" + wtemp)

  if ENABLE_OLED == True:
    oled.fill(0)
    oled.text("[water]", 0, 0)
    oled.text("W=" + wtemp,  0, 10)                     # water temperature
    oled.show()

def read_ds18(t):
  ds18.convert_temp()
  time.sleep_ms(t)

  wtemp = ds18.read_temp(rom)

  return ("{:3.1f}C".format(wtemp))

if __name__ == "__main__":

  ow = onewire.OneWire(machine.Pin(16))
  ds18 = ds18x20.DS18X20(ow)

  rom  = None
  roms = ds18.scan()
  for rom in roms:
    print('Found DS devices: ', rom)
    break

  if ENABLE_OLED == True:
    i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
    oled = ssd1306.SSD1306_I2C(width=128, height=64, i2c=i2c)

  main()
