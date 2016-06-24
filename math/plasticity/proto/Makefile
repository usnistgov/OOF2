all: smallmatrixc.so
.PHONY: all

smallmatrixc.so: smallmatrix.o smallmatrixcmodule.o 
ifdef ANACONDA_LIBS
	g++ smallmatrixcmodule.o smallmatrix.o -L$(ANACONDA_LIBS) -lopenblas -shared -o smallmatrixc.so
else
	g++ smallmatrixcmodule.o smallmatrix.o -llapack -lblas -shared -o smallmatrixc.so
endif

SWIGEXEC=/usr/local/bin/swig
SWIGLIB=/usr/local/lib/swig_lib 

# This line is kind of a problem -- adjust it so that it finds your local
# SWIG libraries.  
smallmatrixcmodule.C: smallmatrix.swg smallmatrix.spy 
	${SWIGEXEC} -I${SWIGLIB} -python -shadow -c++ -o smallmatrixcmodule.C -dnone smallmatrix.swg
	
smallmatrix.o: smallmatrix.C smallmatrix.h
	g++ smallmatrix.C -fPIC -c -o smallmatrix.o

smallmatrixcmodule.o: smallmatrixcmodule.C
	g++ -I/usr/include/python2.7 smallmatrixcmodule.C -fPIC -c -o smallmatrixcmodule.o

clean:
	rm -rf smallmatrixcmodule.C 
	rm -rf smallmatrixcmodule.o smallmatrix.o smallmatrixc.so
	rm -rf smallmatrix.py smallmatrix.pyc
.PHONY: clean
