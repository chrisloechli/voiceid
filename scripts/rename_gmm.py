#!/usr/bin/env python 


import struct
import sys

if __name__ == '__main__':

	input_file = sys.argv[1]
	output_file = sys.argv[2]
	input_name = sys.argv[3]

	gmm = open(input_file,'r')
	new_gmm = open(input_file+'.new','w')

	kind = gmm.read(8)
	new_gmm.write(kind)

	num_gmm_string = gmm.read(4) 
	num_gmm = struct.unpack('>i', num_gmm_string )

	if num_gmm != (1,):
		print str(num_gmm) + " gmms"
		raise Exception('Loop needed for gmms')

	new_gmm.write(num_gmm_string)

	gmm_1 = gmm.read(8)
	new_gmm.write(gmm_1)

	nothing =  gmm.read(4) 
	new_gmm.write(nothing)

	str_len = struct.unpack('>i', gmm.read(4) )
	name = gmm.read(str_len[0])
	print input_name
	new_len = struct.pack('>i', len(input_name) )

	new_gmm.write(new_len)
	new_gmm.write(input_name)

	all_other = gmm.read()

	new_gmm.write(all_other)

	"""
	gender = gmm.read(1)
	gaussian_kind = struct.unpack('>i', gmm.read(4) )

	dim = struct.unpack('>i', gmm.read(4) )

	nb_comp = struct.unpack('>i', gmm.read(4) )

	"""

	gmm.close()
	new_gmm.close()
