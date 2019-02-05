#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char* argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        printf("Usage: ./copy infile outfile resize by\n");
        return 1;
    }

    int resizeby = atoi(argv[1]);

    if(resizeby > 100 || resizeby < 0)
    {
        printf("Usage: resize number must be between 1 and 100 \n");
        return 1;
    }

    // remember filenames
    char* infile = argv[2];
    char* outfile = argv[3];

    // open input file
    FILE* inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE* outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    //variables for later use
    int originalsize;
    int originalwidth;
    int originalheight;
    int originalred;
    int originalgreen;
    int originalblue;

    int verticalred[bi.biWidth * resizeby * 2];
    int verticalgreen[bi.biWidth * resizeby * 2];
    int verticalblue[bi.biWidth * resizeby * 2];

    // determine padding for scanlines
    int padding =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    //store original variables

    originalsize = bi.biSizeImage;
    originalwidth = bi.biWidth;
    originalheight = bi.biHeight;

    //update dimentions
    bi.biWidth = bi.biWidth * resizeby;
    bi.biHeight = bi.biHeight * resizeby;

    //determine outfile padding
    int paddingb =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    //determine outfile size of info and file header
    bi.biSizeImage = ((bi.biWidth) * abs(bi.biHeight) * sizeof(RGBTRIPLE)) + paddingb;
    bf.bfSize = sizeof(BITMAPFILEHEADER)+sizeof(BITMAPINFOHEADER) + bi.biSizeImage;

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);


    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < (biHeight / resizeby); i++)
    {

        // iterate over pixels in scanline
        for (int j = 0; j < originalwidth; j++)
        {

            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            //store original values
            originalred = triple.rgbtRed;
            originalgreen = triple.rgbtGreen;
            originalblue = triple.rgbtBlue;

            //copy each pixel into array for use in vertical scaling
            verticalred[j] = triple.rgbtRed;
            verticalgreen[j] = triple.rgbtGreen;
            verticalblue[j] = triple.rgbtBlue;



            // write RGB triple to outfile
            for (int aa = 0; aa < resizeby; aa++)
            {
                fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
            }
        }

        // skip over padding, if any
            fseek(inptr, padding, SEEK_CUR);

        // then add it back (to demonstrate how)
        for (int k = 0; k < paddingb; k++)
            {
                fputc(0x00, outptr);
            }


        //resize vertical

        //vertical storage
        RGBTRIPLE vertical;

        for (int dd = 0; dd < resizeby - 1; dd++)
        {
            for (int bb = 0; bb < originalwidth; bb++)
            {
                for (int cc = 0; cc < resizeby; cc++)
                {
                    //write vertical scaling pixel info from array
                    vertical.rgbtRed = verticalred[bb];
                    vertical.rgbtGreen = verticalgreen[bb];
                    vertical.rgbtBlue = verticalblue[bb];

                    //write vertical pixel into outfile
                    fwrite(&vertical, sizeof(RGBTRIPLE), 1, outptr);
                }


            }


            //add in padding
            for (int k = 0; k < paddingb; k++)
            {
                fputc(0x00, outptr);
            }

        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // that's all folks
    return 0;
}