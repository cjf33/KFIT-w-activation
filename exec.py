import os
for count in range(1,101):
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
    	os.system("qsub /storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/job_kin_{0:0d}.pbs".format(count))

