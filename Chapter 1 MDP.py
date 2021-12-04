'''import NumPy as ql'''
	R = ql.matrix ([	[0,0,0,0,10,],
				  [0,0,0,1,0,1],
				  [0,0,100,1,0,0],
				  [0,1,1,0,1,0],
				  [1,0,0,1,0,0],
					[0,1,0,0,0,0]	])
	Q = ql.matrix(ql.zeros([6,6]))
	
	gamma = 0.8
	
	'''R is the reward matrix described in the mathematical analasys'''
	
	
