import os
import resource
from datetime import datetime

import tables


def mem_usage_gb():
    mem_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return mem_kb/(1024.0*1024.0)


def main():
    print('{} - PID: {}, PPID: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), os.getpid(), os.getppid()))
    with tables.open_file('/tmp/8GB.h5', 'r') as f:
        f.root.table.read(field='vector_values')
        print('RSS: {:0.03f} GB'.format(mem_usage_gb()))


if __name__ == '__main__':
    main()
