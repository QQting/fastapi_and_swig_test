SRC_FILE_NAME=example
WRAPPER_FILE_NAME=example_wrap
MODULE_NAME=librmt_python

all:
	swig -python -o ${WRAPPER_FILE_NAME}.c ${SRC_FILE_NAME}.i
	# swig -python -o ${WRAPPER_FILE_NAME}.c -outdir pyfiles ${SRC_FILE_NAME}.i	
	#gcc -O2 -fPIC -c ${SRC_FILE_NAME}.c ${WRAPPER_FILE_NAME}.c -I /usr/include/python3.8 -I ./include
	#gcc -O2 -shared ${SRC_FILE_NAME}.o ${WRAPPER_FILE_NAME}.o -o _${MODULE_NAME}.so

	python setup.py build_ext --inplace
	cp _${librmt_python}* ../../src/restful-server/monitor/
