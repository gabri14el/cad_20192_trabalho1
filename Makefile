### Makefile ###

all:mandelbrot_serial mandelbrot_omp mandelbrot_vec mandelbrot_omp_vec

mandelbrot_serial: mandelbrot_serial.c
	gcc mandelbrot_serial.c -o mandelbrot_serial

mandelbrot_omp: mandelbrot_omp.c
	gcc -Wall -fopenmp mandelbrot_omp.c -o mandelbrot_omp

mandelbrot_vec: mandelbrot_vec.c
	gcc mandelbrot_vec.c -fopt-info-vec -o mandelbrot_vec

mandelbrot_omp_vec: mandelbrot_omp_vec.c
	gcc -Wall -fopenmp -O3 mandelbrot_omp_vec.c -fopt-info-vec -o mandelbrot_omp_vec


