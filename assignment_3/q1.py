import numpy as np

def iterate(N,conv_points_real,conv_points_imag,div_points_real,div_points_imag,i_list,x,y,bound):
	"""
	This Function performs an iterations to find if a point in the complex plane is convergent or divergent relative to the number of iterations picked.
	
	Iteration procedure: z_i+1 = z_i^2 + c

	Input:
	N -> Number of Iterations,
	conv_points_real -> List to store Real Part of Converging Complex Points
	conv_points_imag -> List to store Imaginary Part of Converging Complex Points
	div_points_real -> List to store Real Part of Diverging Complex Points 
	div_points_imag -> List to store Imaginary Part of Diverging Complex Points 
	i_list -> List to store iterations of divergent points
	x , y -> arrays of values between (-2,2) to create the complex number: c = x + yi
	bound -> boundary of z complex number.

	Returns:
	4 Filled Lists of:  conv_points_real,conv_points_imag,div_points_real,div_points_imag
	"""
	k=0
	for a in x:
		for b in y:
			z = 0
			c = a + b*1j
			for i in range(N):
				z = z**2 + c

				if np.abs(z) >= bound:
					k += 1
			if np.abs(z) < bound:
				conv_points_real.append(c.real)
				conv_points_imag.append(c.imag)
			else:
				i_list.append(k)
				div_points_imag.append(c.imag)
				div_points_real.append(c.real)

	return (conv_points_real, conv_points_imag, div_points_real, div_points_imag)
