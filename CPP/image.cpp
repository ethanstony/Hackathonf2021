#include <opencv2/opencv.hpp>
int main()
{
 cv::Mat image;
 image = cv::imread("../data/grapefruit.png");
 cv::imshow("Grapefruit",image);
 cv::waitKey(0);
 cv::destroyWindow("Grapefruit");
 return 0;
}
