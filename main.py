import multiprocessing as mp
import subprocess
from pathlib import Path
#sudo perf stat -e cpu-clock python -c 'print "a"*50
#using the perf stat command, with ffmpeg, I found that a 720 2mb video utilizes approx 1 cpu. Using lscpu, I found out I have an 8 core cpu. Thus, I can safely do seven 

def my_func(x):
  name = mp.current_process().name
  print(name, 'Starting')
  
  x=str(x)+".mp4"
  doesExist = Path('./'+x)
  if(doesExist.is_file()):
    print(name,'Exiting')
  else:
    subprocess.call(["ffmpeg", "-loglevel","panic", "-i", "2mb.mp4", "-b:v", "480", str(x)])
    print (name, "Exiting")
  
  
def main():
  pool = mp.Pool(mp.cpu_count())
  result = pool.map(my_func, [4,2,3,5,1,8])
  #result_set_2 = pool.map(my_func, [4,6,5,4,6,3,23,4,6])

  print(result)
  #print(result_set_2)
  
    
    
if __name__ == "__main__":
  main()
