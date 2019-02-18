
# exercise-2-ffmpeg-joshem
For this exercise, I used perf stat to find out how much utilization my ffmpeg command was doing. Specifically, I ran:
''' perf stat -- ffmpeg -i IN -r 30 -b:v 1M OUT ''' 
This told me that ffmpeg runs ~.89 CPUs.  I ran the '''lscpu''' command to find out how much cores I had, to find out I have 8.  However, I found that the multiprocessing library from python3 actually has a pool capability, which actually only onlys so many processes, to your CPU limit.  With this in mind, I used that feature, with some nicely added touches.  Everything runs on Python3, with an assumption of a Linux based file system

# python-ci-template
minimal template for Python Travis-CI. Prereqs installed from requirements.txt
>>>>>>> 56170d168d2b2365a2d2b3d5a8e892b2a7bfe005
