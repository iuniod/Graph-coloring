# Copyright 2022-2023 Iustina-Andreea Caramida 322CA
CC = g++
CFLAGS = -Wall -Wextra -Werror

build:
	$(CC) $(CFLAGS) -o p1.out src/p1/brute.cpp
	$(CC) $(CFLAGS) -o p2.out src/p2/greedy.cpp
	$(CC) $(CFLAGS) -o p3.out src/p3/dsatur.cpp
	$(CC) $(CFLAGS) -o p4.out src/p4/rlf.cpp

run-p1:
	$(CC) $(CFLAGS) -o p1.out src/p1/brute.cpp
	./p1.out

run-p2:
	$(CC) $(CFLAGS) -o p2.out src/p2/greedy.cpp
	./p2.out

run-p3:
	$(CC) $(CFLAGS) -o p3.out src/p3/dsatur.cpp
	./p3.out

run-p4:
	$(CC) $(CFLAGS) -o p4.out src/p4/rlf.cpp
	./p4.out

run-best:
	'make clean'
	'make run-p3'

create-statistics-p1:
	hyperfine --warmup 5 --runs 10 --parameter-scan test 27 34 './p1.out < in/test{test}.in > out/test{test}.out1' --export-markdown src/statistics.md 

create-statistics-p2:
	hyperfine --warmup 5 --runs 10 --parameter-scan test 1 34 './p2.out < in/test{test}.in > out/test{test}.out2' --export-markdown src/statistics-p2.md 

create-statistics-p3:
	hyperfine --warmup 5 --runs 10 --parameter-scan test 1 34 './p3.out < in/test{test}.in > out/test{test}.out3' --export-markdown src/statistics-p3.md 

create-statistics-p4:
	hyperfine --warmup 5 --runs 10 --parameter-scan test 1 34 './p4.out < in/test{test}.in > out/test{test}.out4' --export-markdown src/statistics-p4.md 

clean:
	rm -f *.out 

