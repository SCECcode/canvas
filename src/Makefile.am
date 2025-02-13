# Autoconf/automake file

# General compiler/linker flags
AM_CFLAGS = ${CFLAGS} 
AM_LDFLAGS = ${LDFLAGS}

TARGETS = libcanvas.a libcanvas.so

all: $(TARGETS)

install:
	mkdir -p ${prefix}
	mkdir -p ${prefix}/lib
	mkdir -p ${prefix}/include
	cp libcanvas.so ${prefix}/lib
	cp libcanvas.a ${prefix}/lib
	cp canvas.h ${prefix}/include

libcanvas.a: canvas_static.o 
	$(AR) rcs $@ $^

libcanvas.so: canvas.o
	$(CC) -shared $(AM_CFLAGS) -o libcanvas.so $^ $(AM_LDFLAGS)

canvas.o: canvas.c
	$(CC) -fPIC -DDYNAMIC_LIBRARY -o $@ -c $^ $(AM_CFLAGS)
	
canvas_static.o: canvas.c
	$(CC) -o $@ -c $^ $(AM_CFLAGS)
	
clean:
	rm -rf $(TARGETS)
	rm -rf *.o 

