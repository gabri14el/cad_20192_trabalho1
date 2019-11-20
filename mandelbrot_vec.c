/* 
 c program:
 --------------------------------
  1. draws Mandelbrot set for Fc(z)=z*z +c
  using Mandelbrot algorithm ( boolean escape time )
 -------------------------------         
 2. technique of creating ppm file is  based on the code of Claudio Rocchini
 http://en.wikipedia.org/wiki/Image:Color_complex_plot.jpg
 create 24 bit color graphic file ,  portable pixmap file = PPM 
 see http://en.wikipedia.org/wiki/Portable_pixmap
 to see the file use external application (graphic viewer)
 * 
 * Modificado por gabri14el at git em 20/11/2019
  */

#pragma GCC optimize("O3")										  //Optimization flags
#pragma GCC option("arch=native", "tune=native", "no-zero-upper") //Enable AVX
#pragma GCC target("avx2")										  //Enable AVX
#include <x86intrin.h>											  //AVX/SSE Extensions
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include <time.h>
#define CODIGO "vec"
int main(int argc, char *argv[])
{

	if (argc == 3)
	{
		int value = atoi(argv[1]);
		/* screen ( integer) coordinate */
		int iX, iY;
		const int iXmax = value;
		const int iYmax = value;

		//tempo
		clock_t start, end;
		double cpu_time_used;
		FILE *log;
		const char *log_path = argv[2];
		log = fopen(log_path, "a");
		//criacao de um ponteiro para um um array de 3 dimensoes
		unsigned char ***array = (unsigned char ***)malloc(iYmax * sizeof(unsigned char **));
		double *CyVec = (double *)malloc(iYmax * sizeof(double));
		double *CxVec = (double *)malloc(iXmax * sizeof(double));

		//alocacao dinamica dos arrays de ponteiros internos
		//podemos observar as duas primeiras dimensoes como um array de ponteiros
		//e a ultima dimensao como um array comum
		for (int i = 0; i < iYmax; i++)
		{
			// Assign to array[i], not *array[i] (that would dereference an uninitialized pointer)
			//alocado da segunda dimensao de ponteiros
			array[i] = (unsigned char **)malloc(iXmax * sizeof(unsigned char *));
			for (int j = 0; j < iXmax; j++)
			{
				//alocacao do array de tres dimensoes
				array[i][j] = (unsigned char *)malloc(3 * sizeof(unsigned char));
			}
		}

		/* world ( double) coordinate = parameter plane*/
		//double Cx,Cy;
		const double CxMin = -2.5;
		const double CxMax = 1.5;
		const double CyMin = -2.0;
		const double CyMax = 2.0;
		/* */
		double PixelWidth = (CxMax - CxMin) / iXmax;
		double PixelHeight = (CyMax - CyMin) / iYmax;
		/* color component ( R or G or B) is coded from 0 to 255 */
		/* it is 24 bit color RGB file */
		const int MaxColorComponentValue = 255;
		FILE *fp;
		char *filename = "new1.ppm";
		char *comment = "# "; /* comment should start with # */
		//static unsigned char color[3];
		/* Z=Zx+Zy*i  ;   Z0 = 0 */
		double Zx, Zy;
		double Zx2, Zy2; /* Zx2=Zx*Zx;  Zy2=Zy*Zy  */
		/*  */
		int Iteration;
		const int IterationMax = 200;
		/* bail-out value , radius of circle ;  */
		const double EscapeRadius = 2;
		double ER2 = EscapeRadius * EscapeRadius;
		/*create new file,give it a name and open it in binary mode  */
		fp = fopen(filename, "wb"); /* b -  binary mode */
		/*write ASCII header to the file*/
		fprintf(fp, "P6\n %s\n %d\n %d\n %d\n", comment, iXmax, iYmax, MaxColorComponentValue);

		/* compute and write image data bytes to the file*/
		// computa cx e cy
		start = clock();
		for (iY = 0; iY < iYmax; iY++)
		{
			double aux = CyMin + iY * PixelHeight;
			double cx = CxMin + iY * PixelWidth;
			if (fabs(aux) < PixelHeight / 2)
				aux = 0.0;
			CyVec[iY] = aux;
			CxVec[iY] = cx;
		}

		for (iY = 0; iY < iYmax; iY++)
			for (iX = 0; iX < iXmax; iX++)
			{
				double Cy = CyVec[iY];
				double Cx = CxVec[iX];

				/* initial value of orbit = critical point Z= 0 */
				Zx = 0.0;
				Zy = 0.0;
				Zx2 = Zx * Zx;
				Zy2 = Zy * Zy;
				/* */
				for (Iteration = 0; Iteration < IterationMax && ((Zx2 + Zy2) < ER2); Iteration++)
				{
					Zy = 2 * Zx * Zy + Cy;
					Zx = Zx2 - Zy2 + Cx;
					Zx2 = Zx * Zx;
					Zy2 = Zy * Zy;
				};

				/* compute  pixel color (24 bit = 3 bytes) */
				//unsigned char *aux1 = color +(iYmax*iXmax)+(iXmax*iX); //calcula endereco base
				if (Iteration == IterationMax)
				{ /*  interior of Mandelbrot set = black */
					array[iY][iX][0] = 0;
					array[iY][iX][1] = 0;
					array[iY][iX][2] = 0;
				}
				else
				{ /* exterior of Mandelbrot set = white */
					array[iY][iX][0] = 255;
					array[iY][iX][1] = 255;
					array[iY][iX][2] = 255;
				};
			}

		end = clock();
		cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;
		fprintf(log, "%s, %d, %f\n", CODIGO, iYmax, cpu_time_used);
		fclose(log);
		//impessao do aquivo
		for (iY = 0; iY < iYmax; iY++)
			for (iX = 0; iX < iXmax; iX++)
				fwrite(array[iY][iX], 1, 3, fp);
		fclose(fp);
	}

	else
		printf("faltando tamanho da imagem ou path para log...\n");
	return 0;
}
