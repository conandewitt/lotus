#system libraries
import os
import threading
import time


#daq libraries
from mcculw import ul
from mcculw.enums import DigitalIODirection
from examples.console import util
from examples.props.digital import DigitalProps
from mcculw.ul import ULError
from examples.props.ai import AnalogInputProps

#serial libraries
import time
import serial


#libraries for interaction, plotting and data analysis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ipywidgets import widgets
from bokeh.plotting import figure,show
from bokeh.io import output_notebook, push_notebook
output_notebook()
from IPython.display import display
import ipywidgets as widgets



def mc_init(board_num):
	#detect devices

	ul.ignore_instacal()
	if not util.config_first_detected_device(board_num):
	    print("Could not find device.")

def mc_digital_out(board_num,bit_num,bit_value):
	digital_props = DigitalProps(board_num)

	port = next(
	    (port for port in digital_props.port_info
	     if port.supports_output), None)
	if port == None:
	    util.print_unsupported_example(board_num)

	# If the port is configurable, configure it for output.
	if port.is_port_configurable:
	    ul.d_config_port(board_num, port.type, DigitalIODirection.OUT)

	port_value = 0xFF

	print("Setting " + port.type.name + " to " + str(port_value) + ".")

	# Output the value to the port
	ul.d_out(board_num, port.type, port_value)

	# bit_num = 0 #CH0 --> normally high
	# bit_value = 1 ##set 5V to HIGH, power the sensor
	print("Setting " + port.type.name + " bit " + str(bit_num) + " to "+ str(bit_value) + ".")

	# Output the value to the bit
	ul.d_bit_out(board_num, port.type, bit_num, bit_value)

def mc_analog_init(board_num):
	ai_props = AnalogInputProps(board_num)
	ai_range = ai_props.available_ranges[0]


def dmm_cmd(string,serial,delay):
    cmd=string+'\r\n'
    byte=cmd.encode('utf-8')
    time.sleep(delay)
    serial.write(byte)
    ser_bytes = serial.readline()
    data=ser_bytes.decode('utf-8')
    return data


