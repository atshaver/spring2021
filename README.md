# Spring 2021
# Telescope Pointing Accuracy (TPAVid.py)
This code accepts a video input, iterates through the frames of the video using the imageio tool, finds the brightest point using the centerofmass tool, and plots the movement of the brightest pixel relative to the position of that in the first frame. The second row of the output graph is a power spectral density plot. The purpose of this project is to determine the amount of wobble an imager has when pointed to a fixed light source. 
# Look Angles (LookAngles2.py)
This code is used to find the times that groundstations at two locations can see the same satellite. It starts at a certain time and can iterate through data over a designated period of time (like a month). It accepts TLE input and is meant to output the number of times (overlap_times) that the two groundstations can see the satellite. It is not functional yet.
