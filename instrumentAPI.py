'''
With w1 = frequency of fundamental (in Hz) times 2 pi, 
the simulated clarinet waveform as a function of time, 
t (in seconds) is:

s(t) = sin(w1t) + 0.75*sin(3*w1t) + 0.5*sin(5*w1t) + 
				0.14*sin(7*w1t) + 0.5*sin(9*w1t) + 0.12*sin(11*w1t) + 0.17*sin(13*w1t) 

NOTE : Multiply s(t) by a constant to change the amplitude.

Largest range of possible frequencies, extending over four octaves 
(from 147 Hz to 1976 Hz).
'''

import math
from threading import timer

class Clarinet():
	'''
	@brief Creates a clarinet object.

	This class represents a clarinet. It will
	produce an ouput adhering to the following:
	-----------------------------------------------------

	With w1 = frequency of fundamental (in Hz) times 2 pi, 
	the simulated clarinet waveform as a function of time, 
	t (in seconds) is:

	s(t) = sin(w1t) + 0.75*sin(3*w1t) + 0.5*sin(5*w1t) + 
		0.14*sin(7*w1t) + 0.5*sin(9*w1t) + 0.12*sin(11*w1t) 
		+ 0.17*sin(13*w1t) 

	NOTE : Multiply s(t) by a constant to change the amplitude.

	Largest range of possible frequencies, extending over four 
	octaves (from 147 Hz to 1976 Hz).
	'''

	def __init__(self, listOfFrequencies):
		# Must be initilaized wth listOfFrequencies.
		self.listOfFrequencies = listOfFrequencies

	def calculateOutput(self):
		for freq in self.listOfFrequencies:
			freqHz = freq/2*math.pi
			
