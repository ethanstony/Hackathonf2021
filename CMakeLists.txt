cmake_minimum_required(VERSION 3.16)

#Setting the Project Name
project(video)

#Requirements
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

#The Executable
add_executable(video video.cpp)

#Libraries that are used
target_link_libraries( video ${OpenCV_LIBS} )
