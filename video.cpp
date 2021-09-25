#include <opencv2/core.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <stdio.h>
using namespace cv;
using namespace std;
int main(int, char**)
{
    Mat frame, gray;
    Mat res, loc;
    double thres = 0.84;

    //--- INITIALIZE VIDEOCAPTURE
    VideoCapture cap;
    int deviceID = 2;             // 0 = open default camera
    int apiID = cv::CAP_ANY;      // 0 = autodetect default API
    cap.open(deviceID, apiID);
    // check if we succeeded
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }
    //Open template image
    Mat img;
    img = imread("../data/grapefruit.png", IMREAD_GRAYSCALE);
    //I make from a build directory, so you might need to remove '../'
    // success?
    if (!img.data) {
	cerr << "ERROR! Unable to open file\n";
	return -2;
    }
    //imshow("Template", img);
    Size sz = img.size();
    int w = sz.width;
    int h = sz.height;

    //--- GRAB AND WRITE LOOP
    cout << "Start grabbing" << endl
        << "Press any key to terminate" << endl;
    for (;;)
    {
        // wait for a new frame from camera and store it into 'frame'
        cap.read(frame);
        // check if we succeeded
        if (frame.empty()) {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }
	//Operate on image
	cvtColor(frame, gray, COLOR_BGR2GRAY);
	//matchTemplate(gray, img, res, TM_CCOEFF_NORMED);
	//for (x=0,x++,x<res.size.width)
	//{
	//	for (y=0,y++,y<res.size.height)
	//	{
	//		if (res[x,y] >= thres)
	//			rectangle
	//	}
	//}
        // show live and wait for a key with timeout long enough to show images
        imshow("Live", frame);
        if (waitKey(5) >= 0)
            break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
