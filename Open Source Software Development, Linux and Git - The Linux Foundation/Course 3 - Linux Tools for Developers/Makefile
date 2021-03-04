CFLAGS :=	-O $(CFLAGS)
TARGET=		myhello
SRCFILES=	myhello.c

all: $(TARGET)

$(TARGET):	$(SRCFILES) 
	$(CC) $(CFLAGS) -o $(TARGET) $(SRCFILES) 

clean:
	rm -f $(TARGET)

