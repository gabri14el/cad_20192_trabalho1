#!/bin/bash
echo "fazendo para o omp..."
for i in 1000 5000 10000 15000 18000 20000 30000 35000 40000 50000
do
    echo "tamanho $i"
   ./mandelbrot_omp $i ~/log.csv
done

echo "fazendo para o omp_vec..."
for i in 1000 5000 10000 15000 18000 20000 30000 35000 40000 50000
do
    echo "tamanho $i"
   ./mandelbrot_omp_vec $i ~/log.csv
done


echo "fazendo para o vec..."
for i in 1000 5000 10000 15000 18000 20000 30000 35000 40000 50000
do
    echo "tamanho $i"
   ./mandelbrot_vec $i ~/log.csv
done

echo "fazendo para o serial"
for i in 1000 5000 10000 15000 18000 20000 30000 35000 40000 50000
do
    echo "tamanho $i"
   ./mandelbrot_omp_vec $i ~/log.csv
done

