# KFIT-w-activation
K-FIT kinetic parameterization with enzyme activation
To parameterize S. cerevisiae core metabolism kinetic model using wild-type and fumarase knockout fluxomics data, run parallel_run_all.m

K-FIT codes adapted from:

S. Gopalakrishnan, S. Dash, and C. Maranas, "K-FIT: An accelerated kinetic parameterization algorithm using steady-state fluxomic data," Metab Eng, Mar 13 2020, doi: 10.1016/j.ymben.2020.03.001.

To incorporate enzyme activation, kineticdecomp, calc_k, gradcalc, ensemble, and ccalcsetup codes were updated from original versions such that data structures and kinetic parameters captured the reversible activation of de-activated enzyme according to linear specific activation mechanism.

multiply_runs_init.py creates copies of files needed to initialize multi-starts on HPC cluster

jobs_kin_01.pbs is a shell script for job submission

exec.py automates multi-start submission on HPC cluster.
