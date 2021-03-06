#!/usr/bin/python3

import sys, os

N = int(sys.argv[1])
maxrad = int(N**(1/3) + 1.5)

n_radial = maxrad*50+1

# Need to also teach this to use different algorithms

cmd = "rq cancel lj-{N} && cargo build --release && rm -f lj-{N}.* && rq run -J lj-{N} target/release/lj-cluster --N {N} --max-allowed-energy 0 --sad-min-T 0.1 --translation-scale 0.1 --energy-bin 0.1 --save-as lj-{N}.yaml --movie-time '10^(1/4)' --save-time 0.5 --n-radial {n_radial} --radius {maxrad}".format(N=N, maxrad=maxrad, n_radial=n_radial)
print(cmd)
os.system(cmd)
