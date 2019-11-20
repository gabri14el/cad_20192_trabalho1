#!/bin/bash
echo "fazendo para o omp..."
for i in 1000 5000 7000 10000 11000 12000 14000 15000 17000 18000
do
    echo "tamanho $i"
   ./mandelbrot_omp $i ~/log.csv
done
