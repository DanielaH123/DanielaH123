1	def totalPaginas(libros):
2	    if len (libros)==0:
3	        return 0
4	    else:
5	        return 1 + totalPaginas (libros[1:])
6	
7	print (totalPaginas([10,20,30,40]))
