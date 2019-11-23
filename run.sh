#!/bin/bash
echo "fazendo para o omp..."
for i in 1000 2500 5000 7500 10000 12500 15000 17500 20000 22500 25000 27500 30000 32500 35000 37500 40000 45000 50000 60000
do
    for t in 1 2 3 4 5 6 7 8 9 10 11 12
    do
        echo "tamanho $i"
        ./mandelbrot_omp.bin $i ~/log.csv $t
    done
done

echo "fazendo para o omp_vec..."
for i in 1000 2500 5000 7500 10000 12500 15000 17500 20000 22500 25000 27500 30000 32500 35000 37500 40000 45000 50000 60000
do
    echo "tamanho $i"
   ./mandelbrot_omp_vec.bin $i ~/log.csv
done


echo "fazendo para o vec..."
for i in 1000 2500 5000 7500 10000 12500 15000 17500 20000 22500 25000 27500 30000 32500 35000 37500 40000 45000 50000 60000
do
    echo "tamanho $i"
   ./mandelbrot_vec.bin $i ~/log.csv
done

echo "fazendo para o serial"
for i in 1000 2500 5000 7500 10000 12500 15000 17500 20000 22500 25000 27500 30000 32500 35000 37500 40000 45000 50000 60000
do
    echo "tamanho $i"
   ./mandelbrot_serial.bin $i ~/log.csv
done
