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
	-@/bin/rm -rf $(PLC_DIR)/ups
	@mkdir        $(PLC_DIR)/ups
	@cp Makefile $(PLC_DIR)/ups
	$(SDSSTOOLS_DIR)/bin/install_ups_table -w plc.table $(PLC_DIR)/ups

clean:
	- /bin/rm -fr *~ .*~ core *.bak *.orig *.old .\#* \#*\#
