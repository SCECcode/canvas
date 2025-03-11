# GNU Automake config


# Autoconf/automake file

# General compiler/linker flags
AM_CFLAGS = ${CFLAGS}
AM_FCFLAGS = ${FCFLAGS}
AM_LDFLAGS = ${LDFLAGS}

all:
if WITH_CANVAS_LARGEDATA_DIR
	echo "USING WITH_CANVAS_LARGEDATA_DIR in canvas"
else
	./make_data_files.py
endif

install:
if WITH_CANVAS_LARGEDATA_DIR
	if [ ! -d "${prefix}/data/canvas" ]; then \
		$(MKDIR_P) ${prefix}/data; \
		$(LN_S) -f $(CANVAS_LARGEDATA_DIR) ${prefix}/data/canvas; \
		echo "USING WITH_CANVAS_LARGEDATA_DIR in canvas"; \
	fi
	cp config ${prefix}/data
else
	if [ ! -d "${prefix}/data/canvas" ]; then \
		$(MKDIR_P) ${prefix}/data; \
		mv canvas ${prefix}/data; \
		$(LN_S) -f ${prefix}/data/canvas .; \
	fi
	cp config ${prefix}/data
endif

clean:
	echo "clean"

