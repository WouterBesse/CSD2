#include <stdio.h>
#include <iostream>
#include <cmath>
#include <emscripten/emscripten.h>
#include <vector>
#include <string>

typedef long int i32;


#ifdef __cplusplus
extern "C" {
#endif


EMSCRIPTEN_KEEPALIVE void genGraph(int width, int height, int blobx[], int bloby[], int blobr[], int blobamt, i32 *sampletext, i32 textlength) {
  printf("x = %d \n", width);
  printf("x = %d \n", height);
  printf("x = %d \n", blobx[0]);
  printf("x = %d \n", bloby[0]);
  printf("x = %d \n", blobamt);
  int arraysiz = height * width * 4;
  //std::vector<int> pxarray;
  int pxarray[arraysiz];
  int n = 0;
  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      int sum = 0;
      for (int i = 0; i < blobamt; i++) {
        int xdif = x - blobx[i];
        int ydif = y - bloby[i];
        int d = sqrt((xdif * xdif) + (ydif * ydif));
        sum += 4 * blobr[i] / d;
      }

      pxarray[n] = sum;
      pxarray[n + 1] = sum;
      pxarray[n + 2] = sum;
      pxarray[n + 3] = 255;
      // pxarray.push_back(sum);
      // pxarray.push_back(sum);
      // pxarray.push_back(sum);
      // pxarray.push_back(255);
      n += 4;
    }
  }
  int result = 0;
  for (auto d : pxarray)
  {
      result = result * 10 + d;
  }
  //auto arrayPtr = &pxarray[0];
  return cstr("oh hai there!");
}

#ifdef __cplusplus
}
#endif

int main() {
  // int b[2] = {2,2};
  // int a[2] = {2,2};
  // int c[2] = {2,2};
  // int appel = genGraph(1, 1, a, b, c, 1);
  return 0;
}
