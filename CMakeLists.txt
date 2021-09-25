cmake_minimum_required(VERSION 3.16)

#Setting the Project Name
project(CWAGI)

#Requirements
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

#The Executable
add_executable(CWAGI CWAGI.cxx)

#Libraries that are used
target_link_libraries( CWAGI ${OpenCV_LIBS} )
