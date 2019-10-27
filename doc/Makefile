SHELL = /bin/sh

default:
	@echo Please invoke this makefile using sdssmake. >&2
	@exit 1

all:	;

install:
	@if [ "$(PLC_DIR)" = "" ]; then \
		echo You have not specified a destination directory >&2; \
		exit 1; \
	fi
	-@/bin/rm -rf $(PLC_DIR)/doc
	@mkdir        $(PLC_DIR)/doc
	@cp Makefile sdss.ps $(PLC_DIR)/doc

clean:
	- /bin/rm -fr *~ .*~ core *.bak *.orig *.old .\#* \#*\#
