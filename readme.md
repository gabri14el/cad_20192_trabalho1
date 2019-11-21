# Códigos referentes ao primeiro trabalho da disciplina Computação de Alto Desempenho, semestre 2019.2.

O final do código (mandelbrot_*) refere ao tipo de melhoramento nele implementado
- omp: openmp
- omp_vec: openmp e vetorizacao simd (com otimizacao o3 do gcc)
- serial: sem nenhuma otimização
- vec: otimização com simd (com otimização o3 do gcc)

No makefile do projeto pode-se observar os comandos de compilação para cada um dos programas. Para compilar todos apenas executar comando make.
>make

O Shell Script run.sh executa os mesmos testes, visando testar o escalonamento de trablaho de cada um dos códigos. Para excutá-lo: 
>sh run.sh

Exemplo de a execução dos binários: 
>./mandelbrot_omp 30000 ~/log.csv 

- ./mandelbrot_omp: binário
- 30000: tamanho da imagem quadrada gerada
- ~/log.csv: diretório do log para guardar o tempo de execução do bloco correspondente ao cálculo do mandelbrot

