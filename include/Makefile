#
# Definitions of PLC bit fields
#
SDSS_CSV = ../etc/sdss.csv ../etc/extra.csv

all : data_collection.h

data_collection.h : data_collection.h.skl $(SDSS_CSV)
	$(PLC_DIR)/bin/read-csv -C -s data_collection.h.skl $(SDSS_CSV) > data_collection.h
	chmod 444 data_collection.h

install : all
	cp data_collection.h $(PLC_DIR)/include

clean :
	$(RM) data_collection.h
