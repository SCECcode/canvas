# GNU Automake config


# Autoconf/automake file

# General compiler/linker flags
AM_CFLAGS = ${CFLAGS}
AM_FCFLAGS = ${FCFLAGS}
AM_LDFLAGS = ${LDFLAGS}

install:
if WITH_CANVAS_LARGEDATA_DIR
	$(MKDIR_P) ${prefix}/model
 	$(LN_S) -f $(CANVAS_LARGEDATA_DIR) ${prefix}/model
	echo "USING WITH_CANVAS_LARGEDATA_DIR in canvas"
else
	mkdir -p ${prefix}/data
	cp ./config ${prefix}/data
	cp -R ./canvas ${prefix}/data
	chmod og+r ${prefix}/data/config
	chmod -R og+r ${prefix}/data/canvas
	chmod og+x ${prefix}/data/canvas
endif

clean:
	echo "clean"

