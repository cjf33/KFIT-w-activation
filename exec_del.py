import os
for count in range(357,486):
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
    	#os.system("qsub /storage/home/cjf33/scratch/large_ensemble_split/job_{0:0d}.pbs".format(count))
		os.system("qdel 15239{0:0d}".format(count))
