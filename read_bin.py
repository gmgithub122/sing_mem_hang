import os
import resource
from datetime import datetime


def mem_usage_gb():
    mem_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return mem_kb/(1024.0*1024.0)


def main():
    print('{} - PID: {}, PPID: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), os.getpid(), os.getppid()))
    chunks = []
    with open('/tmp/8GB.bin', 'rb') as f:
        while True:
            chunk = f.read()
            if len(chunk) == 0:
                break
            chunks.append(chunk)

        print('RSS: {:0.03f} GB'.format(mem_usage_gb()))


if __name__ == '__main__':
    main()
