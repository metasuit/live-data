import subprocess
import time
import psutil

# Trouble Shoot to terminate serial read, should be improved
def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

print(' Program executed successfully '.center(80, '#'))
calibration = subprocess.Popen("Biceps_Calibration.py", shell = True)
out, err = calibration.communicate() # Waits till programm terminates
print(' Calibration Done '.center(80, '#'))
read_data = subprocess.Popen("read-avg-serial.py", shell = True)

time.sleep(0.5)
print(' Reading Live HASEL Data '.center(80, '#'))
animation = subprocess.Popen("Biceps_Animation_1.py", shell = True)
print(' Started 2D Animation '.center(80, '#'))
out, err = animation.communicate() # Waits till programm terminates

# Trouble Shoot to terminate serial read, should be improved
try:
    read_data.wait(timeout=0.1)
except subprocess.TimeoutExpired:
    kill(read_data.pid)

print(' Program terminated successfully '.center(80, '#'))