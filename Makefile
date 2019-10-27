SHELL = /bin/sh

#=============================================================================

all:
	@ for f in bin doc etc include src ups; do \
		(cd $$f ; echo In $$f; 	$(MAKE) $(MFLAGS) all ); \
	done

install:
	@ echo "Please use python setup.py install" >&2

clean:
	@echo In .
	- /bin/rm -f *~ .*~ *.bak *.orig *.old a.out .\#* \#*\#
	@for f in bin doc etc include ups; do \
			(cd $$f ; echo In $$f; $(MAKE) clean); \
	done
