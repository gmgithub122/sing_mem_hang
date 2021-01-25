Steps to reproduce:

1. Create cgroup with 1GB memory limit.
```
$ sudo ./create_gc <USER> <GROUP>
``` 
2. Write singularity container from minimal.def to `/tmp/minimal.sif` 
```
$ sudo ./create_sing.sh
```
3. Write large h5 file to `/tmp/8GB.h5`
```
python write_h5.py
```
4. Write large binary file to `/tmp/8GB.bin`
```
./write_bin.sh
```
5. Run 10 parallel `read_bin.py` under the cgroup.
```
$ time ./cg_bin_loop.sh
real    0m48.193s
user    0m0.127s
sys     1m10.643s
```
6. Run 10 parallel `read_h5.py` under the cgroup.
```
time ./cg_h5_loop.sh
real    0m58.077s
user    0m14.772s
sys     1m12.767s
```
7. Run 10 parallel `read_bin.py` under singularity under the cgroup.
```
$ time ./cg_sing_bin_loop.sh
real    0m48.932s
user    0m0.364s
sys     1m16.328s
```
8. Run 10 parallel `read_h5.py` under singularity under the cgroup.
```
$ time ./cg_sing_h5_loop.sh
real    4m37.325s
user    0m13.924s
sys     20m44.424s
```