import hid
import time
import struct
from threading import Thread

class Axis:
	def __init__(self, axis, value=0):
		self.axis = axis
		self.value = value
	def position(self):
		return self.value
	def set(self, value):
		self.value = value

class Controller:
	VID = 0x2888 # ID data for the VEX controller
	PID = 0x0503

	def __init__(self):
		self.axis1 = Axis(1)
		self.axis2 = Axis(2)
		self.axis3 = Axis(3)
		self.axis4 = Axis(4)
		self._read_controller() # I run the function once so that it throws a fatal error if the controller is not connected
		background_read = Thread(target=self._read_controller, daemon=True)
		background_read.start()
	def _read_controller(self):
		with hid.Device(self.VID, self.PID) as device:
			while True:
				data = struct.unpack("BBBBBBBB", device.read(8))
				self.axis4.set(-1 * (data[3] - 127) * (100 / 127))
				self.axis3.set(-1 * (data[4] - 127) * (100 / 127))
				self.axis1.set((data[5] - 127) * (100 / 127))
				self.axis2.set(-1 * (data[6] - 127) * (100 / 127))
				time.sleep(0.01)