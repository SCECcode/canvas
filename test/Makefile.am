# Autoconf/automake file

bin_PROGRAMS = test_canvas

# General compiler/linker flags
AM_CFLAGS = ${CFLAGS} -I../src
AM_LDFLAGS = ${LDFLAGS} -L../src -l canvas

objects = test_api.o
TARGETS = $(bin_PROGRAMS)

all: $(bin_PROGRAMS)

install:
	mkdir -p ${prefix}/tests
	cp test_canvas ${prefix}/tests

test_canvas$(EXEEXT): $(objects)
	$(CC) -o $@ $^ $(AM_LDFLAGS)

$(objects): %.o: %.c
	$(CC) -o $@ -c $^ $(AM_CFLAGS)

run_unit : test_canvas
	./test_canvas

clean :
	rm -rf *~ *.o test_canvas


