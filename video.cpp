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
    Mat res;
    double thres = 1;

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
    //cap.read(frame);
    //Size SZ = frame.size();
    //Size sz = img.size();
    //int W = SZ.width;
    //int H = SZ.height;
    //int w = sz.width;
    //int h = sz.height;
    //int xmax = W-w+1;
    //int ymax = H-h+1;

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
	//cvtColor(frame, gray, COLOR_BGR2GRAY);
	matchTemplate(frame, img, res, TM_CCOEFF_NORMED);
	normalize(res, res, 0, 1, NORM_MINMAX, -1, Mat() );
	int counts = 0;
	for (int x=0;x<res.cols;x++)
	{
		for (int y=0;y<res.rows;y++)
		{
			if (res.at<double>(x,y) >= thres)
			{
				counts++;
				//cout << res.at<double>(x,y) << " ";
				rectangle(frame, Point(x,y),
					Point(x+5,y+5),
					Scalar(255,0,0),1);
			}
		}
		//cout << endl;
	}
        // show live and wait for a key with timeout long enough to show images
	cout << counts;
	counts = 0;
        imshow("Live", frame);
        if (waitKey(5) >= 0)
            break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
