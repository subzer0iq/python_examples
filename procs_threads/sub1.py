import subprocess
import time
import os

# proc = subprocess.Popen(
#     ['echo', 'Hello from the child'],
#     stdout=subprocess.PIPE
# )
#
# out, err = proc.communicate()
# print(out.decode('utf-8'))

#####

# proc = subprocess.Popen(['sleep', '0.6'])
# while proc.poll() is None:
#     print('Working...')
#     time.sleep(0.2)
#
# print('Exit status ', proc.poll())

#####

'''
def run_sleep(period):
    proc = subprocess.Popen(['echo','sleep', str(period)], stdout=subprocess.PIPE)
    return proc

start = time.time()
procs = []
#Запускаем 10 процессов паралельно
for _ in range(10):
    proc = run_sleep(0.9)
    procs.append(proc)

#Забираем вывод каждого процесса
for proc in procs:
    #proc.communicate()
    out, err = proc.communicate()
    print(out.decode('utf-8'))


end = time.time()

print('Total time was {0} seconds'.format(end - start))
'''
#########
def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'asdf'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5sum'],
        stdin=input_stdin,
        stdout=subprocess.PIPE
    )
    return proc

input_procs = []
for _ in range(5):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)

hash_procs = []

for proc in input_procs:
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)

for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, _ = proc.communicate()
    print(out)

######

proc = subprocess.Popen(['sleep', '10'])
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('Exit status', proc.poll())
