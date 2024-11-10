# Makefile for c++ project

all: main

main: main.o Rectangle.o
	g++ -o myProgram main.o Rectangle.o

main.o: main.cpp Rectangle.h
	g++ -c main.cpp

Rectangle.o: Rectangle.cpp Rectangle.h
	g++ 0c Rectangle.cpp

clean:
	rm -f *.o main