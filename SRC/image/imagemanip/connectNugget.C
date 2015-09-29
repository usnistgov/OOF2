/*
Kevin Chang
September 16, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute for Standards and Technology

connectNugget.C

Line connection tool
*/

#include "common/array.h"

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "imagemask.h"
#include "connectNugget.h"

/*----------*/

connectClass::connectClass() {
}

/*----------*/

BWImage connectClass::run(const BWImage & imagein, int t, int d, int nei, int bs, bool trim) {

  cout << "in run" << endl;

  BWImage image = connect(imagein, t, d, nei, bs, trim);  // Connects the lines     connect.C

  /*
  ofstream finalImage("finalImage");
  // final.save(finalImage);  // Kang-Xing
  image.save(finalImage);
  finalImage.close();
  */

  return image;
}

/*----------*/

// ***BEGIN Determine Discontinuities Code*** //
// In other words, "places the line ought to go but doesn't" -Kevin Chang //

bool connectClass::isDiscontinuous(const BWImage &image, const ICoord pt) {
  int w = image.width();
  int h = image.height();
  int xneg = pt(0) - 1;
  int xpos = pt(0) + 1;
  int yneg = pt(1) - 1;
  int ypos = pt(1) + 1;

  if (xneg < 0)
    xneg = 0;
  if (xpos >= w)
    xpos = w - 1;
  if (yneg < 0)
    yneg = 0;
  if (ypos >= h)
    ypos = h - 1;

  int p1=image[ICoord(xneg,ypos)];
  int p2=image[ICoord(pt(0),ypos)];
  int p3=image[ICoord(xpos,ypos)];
  int p4=image[ICoord(xneg,pt(1))];
  int p6=image[ICoord(xpos,pt(1))];
  int p7=image[ICoord(xneg,yneg)];
  int p8=image[ICoord(pt(0),yneg)];
  int p9=image[ICoord(xpos,yneg)];

  if (((p1==false) && (p3==false) && (p4==false) && (p6==false) && (p7==false) && (p8==false) && (p9==false) && (p2==false))  // Isolated
   || ((p1==false) && (p3==false) && (p4==false) && (p6==false) && (p7==false) && (p8==false) && (p9==false) && (p2==true))  // Vert Top
   || ((p1==false) && (p3==false) && (p4==false) && (p6==false) && (p7==false) && (p8==true) && (p9==false) && (p2==false))  // Vert Bot
   || ((p1==false) && (p3==false) && (p4==true) && (p6==false) && (p7==false) && (p8==false) && (p9==false) && (p2==false))  // Horiz Left
   || ((p1==false) && (p3==false) && (p4==false) && (p6==true) && (p7==false) && (p8==false) && (p9==false) && (p2==false))  // Horiz Right
   || ((p1==true) && (p3==false) && (p4==false) && (p6==false) && (p7==false) && (p8==false) && (p9==false) && (p2==false))  // Diag Top Left
   || ((p1==false) && (p3==false) && (p4==false) && (p6==false) && (p7==false) && (p8==false) && (p9==true) && (p2==false))  // Diag Bot Right
   || ((p1==false) && (p3==true) && (p4==false) && (p6==false) && (p7==false) && (p8==false) && (p9==false) && (p2==false))  // Diag Top Right
   || ((p1==false) && (p3==false) && (p4==false) && (p6==false) && (p7==true) && (p8==false) && (p9==false) && (p2==false))  // Diag Bot Left
     )
    return true;

// 3-pixel cases  *** CHECK may not be necessary
  if (((p1==true) && (p3==false) && (p4==false) && (p6==false) && (p7==false) && (p8==false) && (p9==false) && (p2==true))  // Top Left
   || ((p1==false) && (p3==true) && (p4==false) && (p6==false) && (p7==false) && (p8==false) && (p9==false) && (p2==true))  // Top Right
   || ((p1==false) && (p3==false) && (p4==false) && (p6==false) && (p7==true) && (p8==true) && (p9==false) && (p2==false))  // Bottom Left
   || ((p1==false) && (p3==false) && (p4==false) && (p6==false) && (p7==false) && (p8==true) && (p9==true) && (p2==false))  // Bottom Right
   || ((p1==false) && (p3==true) && (p4==false) && (p6==true) && (p7==false) && (p8==false) && (p9==false) && (p2==false))  // Right Top
   || ((p1==false) && (p3==false) && (p4==false) && (p6==true) && (p7==false) && (p8==false) && (p9==true) && (p2==false))  // Right Bottom
   || ((p1==true) && (p3==false) && (p4==true) && (p6==false) && (p7==false) && (p8==false) && (p9==false) && (p2==false))  // Left Top
   || ((p1==false) && (p3==false) && (p4==true) && (p6==false) && (p7==true) && (p8==false) && (p9==false) && (p2==false))  // Left Bottom
     )
    return true;

  return false;
}

/*----------*/

BWImage connectClass::getAndReduceDiscontinuities (BWImage connected1, const BWImage newThresh, int d, int boxSize) {
  int wid = connected1.width();
  int hei = connected1.height();
  BWImage connected (wid,hei);
  int size = boxSize * 2;
  skeletonClass sc;
  closeClass cc;
  int newx;
  int newy;
  int newga;
  int newhb;

  for (int x = 0; x < wid; x++) {
    for (int y = 0; y < hei; y++) {
      connected[ICoord(x,y)] = connected1[ICoord(x,y)];
    }
  }

  for (int a = 0; a < wid; a++) {
    for (int b = 0; b < hei; b++) {
      ICoord pt(a,b);

      if((connected[pt] == true) && (isDiscontinuous(connected,pt))) {
	BWImage box(size,size);  //make small box

	for (int c = -size/2; c < size/2; c++) {
	  for (int d = -size/2; d < size/2; d++) {

	    if ((a + c < 0) || (a + c >= wid))
	      newx = a - c;
	    else
	      newx = a + c;

	    if ((b + d < 0) || (b + d >= hei))
	      newy = b - d;
	    else
	      newy = b + d;

	    box[ICoord(c + size/2, d + size/2)] = connected[ICoord(newx, newy)];
	    if ((abs(c) < size/4) && (abs(d) < size/4) && (box[ICoord(c + size/2, d + size/2)] == false))
	      box[ICoord(c + size/2, d + size/2)] = newThresh[ICoord(newx, newy)];
	  }

	  box = sc.run(cc.run(box));  // ,size/8));  //copy back into image

	  wid = connected.width();
	  hei = connected.height();
	  
	  for (int g = -size/2; g < size/2; g++) {
	    for (int h = -size/2; h < size/2; h++) {

	      if ((g+a) < 0)
		newga = 0;
	      else if ((g+a) >= wid)
		newga = wid - 1;
	      else
		newga = g+a;

	      if ((h+b) < 0)
		newhb = 0;
	      else if ((h+b) >= hei)
		newhb = hei - 1;
	      else
		newhb = h+b;

	      if (connected[ICoord(newga, newhb)] == 0)
		connected[ICoord(newga, newhb)] = box[ICoord(g+size/2, h+size/2)];
          }
        }
      }
    }
  }
}

  /*
  ofstream out("connected1");
  connected.save(out);
  out.close();
  */

// SKELETONIZATION AND RE-SAVE CODE

  connected = sc.run(cc.run(connected));  //, d));

  /*
  ofstream out1("connectedSkel");
  connected.save(out1);
  out1.close();
  */

  return connected;
}

/*----------*/

BWImage connectClass::removeDeadLines(const BWImage & connected) {
// In other words, "places the line ought to not go but does" -Kevin Chang //
  BWImage temp = connected;
  cout << "Removing points" << endl;
  int numRemoved = -1;
  while (numRemoved != 0) { 
    numRemoved = 0;
    for (int a = 1; a < connected.width()-1; a++) {  // Does not affect image borders
      for (int b = 1; b < connected.height()-1; b++) {  // Does not affect image borders
	if ((temp[ICoord(a,b)] == true) && isDiscontinuous(temp,ICoord(a,b))) {
	  temp[ICoord(a,b)] = false;
	  numRemoved++;
	}
      }
    }
    cout << numRemoved << endl;
  }

  cout << "Disconnected lines removed." << endl;

  return temp;
}

/*----------*/

BWImage connectClass::connect(const BWImage & gabor, int t, int d, int numEdgeIter, int boxSize, bool trim) {
//BWImage connectClass::connect(const BWImage & gabor, int initialThreshold, int d, int go, int numEdgeIter, int boxSize, bool trim) {

// BWImage threshed = imageToBinary(gabor,initialThreshold,false);
// BWImage connected = skeletonize(close(threshed,d));  // Call skeletonization again in connect.C

  skeletonClass sc;
  closeClass cc;

  int x,y;

  BWImage connected = sc.run(cc.run(gabor));

  cout << "connected = sc.run(cc.run(gabor));" << endl;

  int n = t;
  BWImage temp;
  for (int a = 0; a < numEdgeIter; a++) {
    n--;
    cout << "n: " << n << endl;
    temp = cc.run(gabor);
    /*
    for (x = 0; x < temp.width(); x++) {
      for (y = 0; y < temp.height(); y++) {
	if (temp[ICoord(x,y)] == true)
	  cout << "1 ";
	else
	  cout << "0 ";
      }
      cout << endl;
    }
    */
    temp = sc.run(temp); //, d);
    /*
    for (x = 0; x < temp.width(); x++) {
      for (y = 0; y < temp.height(); y++) {
	if (temp[ICoord(x,y)] == true)
	  cout << "1 ";
	else
	  cout << "0 ";
      }
      cout << endl;
    }
    */
    cout << "a" << endl;

    for (x = 0; x < temp.width(); x++) {
      for (y = 0; y < temp.height(); y++) {
	if (temp[ICoord(x,y)] == true)
	  cout << "1 ";
	else
	  cout << "0 ";
      }
      cout << endl;
    }

    connected = getAndReduceDiscontinuities(connected, temp, d, boxSize);

    for (x = 0; x < temp.width(); x++) {
      for (y = 0; y < temp.height(); y++) {
	if (temp[ICoord(x,y)] == true)
	  cout << "1 ";
	else
	  cout << "0 ";
      }
      cout << endl;
    }
  }

  cout << "pre-trim" << endl;

  if (trim)
    connected=removeDeadLines(connected);

  cout << "done" << endl;

  return connected;
}

/*----------*/
