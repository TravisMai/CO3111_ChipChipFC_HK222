from aiot_lcd1602 import LCD1602
from yolobit import *
from event_manager import *
import time
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
import sys
import uselect
from aiot_rgbled import RGBLed

aiot_lcd1602 = LCD1602()

event_manager.reset()

aiot_dht20 = DHT20(SoftI2C(scl=Pin(22), sda=Pin(21)))

def on_event_timer_callback_D_Y_y_j_K():
  global run, CMD, RT, RH, SM, LUX
  aiot_dht20.read_dht20()
  RT = aiot_dht20.dht20_temperature()
  RH = aiot_dht20.dht20_humidity()
  SM = round(translate((pin1.read_analog()), 0, 4095, 0, 100))
  LUX = round(translate((pin2.read_analog()), 0, 4095, 0, 100))
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('RT:')
  aiot_lcd1602.move_to(3, 0)
  aiot_lcd1602.putstr(RT)
  aiot_lcd1602.move_to(7, 0)
  aiot_lcd1602.putstr('*C')
  aiot_lcd1602.move_to(10, 0)
  aiot_lcd1602.putstr('RH:')
  aiot_lcd1602.move_to(13, 0)
  aiot_lcd1602.putstr(RH)
  aiot_lcd1602.move_to(15, 0)
  aiot_lcd1602.putstr('%')
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr('LUX:')
  aiot_lcd1602.move_to(4, 1)
  aiot_lcd1602.putstr(LUX)
  aiot_lcd1602.move_to(10, 1)
  aiot_lcd1602.putstr('SM:')
  aiot_lcd1602.move_to(13, 1)
  aiot_lcd1602.putstr(SM)
  aiot_lcd1602.move_to(15, 1)
  aiot_lcd1602.putstr('%')
  print((''.join([str(x) for x in ['!1:RT:', RT, '#']])), end =' ')
  print((''.join([str(x2) for x2 in ['!1:RH:', RH, '#']])), end =' ')
  print((''.join([str(x3) for x3 in ['!1:LUX:', LUX, '#']])), end =' ')
  print((''.join([str(x4) for x4 in ['!1:SM:', SM, '#']])), end =' ')

event_manager.add_timer_event(5000, on_event_timer_callback_D_Y_y_j_K)

# Mô tả hàm này...
def abc():
  global run, CMD, RT, RH, SM, LUX, aiot_dht20, aiot_lcd1602, tiny_rgb
  while run == '1':
    display.show(Image("54321:65432:76543:87653:08765"))
    time.sleep_ms(10)
    display.show(Image("65432:76543:87654:08765:10876"))
    time.sleep_ms(10)
    display.show(Image("76543:87654:08765:10876:21087"))
    time.sleep_ms(10)
    display.show(Image("87654:08765:10876:21087:32108"))
    time.sleep_ms(10)
    display.show(Image("08765:10876:21087:32108:43210"))
    time.sleep_ms(10)
    display.show(Image("10876:21087:32108:43210:54321"))
    time.sleep_ms(10)
    display.show(Image("21087:32108:43210:54321:65432"))
    time.sleep_ms(10)
    display.show(Image("32108:43210:54321:65432:76543"))
    time.sleep_ms(10)
    display.show(Image("43210:54321:65432:76543:87654"))
    time.sleep_ms(10)
    display.show(Image("54321:65432:76543:87654:08765"))

def read_terminal_input():
  spoll=uselect.poll()        # Set up an input polling object.
  spoll.register(sys.stdin, uselect.POLLIN)    # Register polling object.

  input = ''
  if spoll.poll(0):
    input = sys.stdin.read(1)

    while spoll.poll(0):
      input = input + sys.stdin.read(1)

  spoll.unregister(sys.stdin)
  return input

tiny_rgb = RGBLed(pin16.pin, 4)

def on_event_timer_callback_G_M_f_H_P():
  global run, CMD, RT, RH, SM, LUX
  CMD = read_terminal_input()
  if CMD == '0':
    tiny_rgb.show(1, hex_to_rgb('#000000'))
    tiny_rgb.show(3, hex_to_rgb('#000000'))
    tiny_rgb.show(2, hex_to_rgb('#000000'))
    tiny_rgb.show(4, hex_to_rgb('#000000'))
  if CMD == '1':
    tiny_rgb.show(1, hex_to_rgb('#0000ff'))
    tiny_rgb.show(3, hex_to_rgb('#ffff00'))
    tiny_rgb.show(2, hex_to_rgb('#4b0082'))
    tiny_rgb.show(4, hex_to_rgb('#00ff00'))
  if CMD == '2':
    display.show(Image("00000:00000:00000:00000:00000"))
  if CMD == '3':
    display.scroll('LMEO')

event_manager.add_timer_event(100, on_event_timer_callback_G_M_f_H_P)

# Mô tả hàm này...
def cde():
  global run, CMD, RT, RH, SM, LUX, aiot_dht20, aiot_lcd1602, tiny_rgb
  for count in range(5):
    time.sleep_ms(1000)
    display.show(Image("00000:00000:00000:00000:00000"))

if True:
  aiot_lcd1602.clear()
  display.show(Image("00000:00000:00000:00000:00000"))

while True:
  event_manager.run()
  time.sleep_ms(100)


run = '1'
abc()

run = '0'

run = '0'
cde()

display.show(Image("10001:01010:00100:01010:10001"))

display.show(Image("04440:40004:40004:40004:04440"))
