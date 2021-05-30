
input=open("/storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/parallel_run_all.m","r")

lines1=input.readlines()

for count in range(1,101):
    output=open("/storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/parallel_run_all_{0:0d}.m".format(count),"w")
    for line in lines1:
        newline=line.replace("save('optimal_1_4_19_wt_all_3.mat','res','model','tout');","save('optimal_112119_CF_{0:0d}.mat','res','model','tout');".format(count))
        newline=newline.replace("kineticestimate_v4","kineticestimate_v4_{0:0d}".format(count))
        newline=newline.replace("load xbest.mat","load xbest_{0:0d}.mat".format(count))
        output.write(newline)


input2=open("/storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/job_kin_01.pbs","r")

lines2=input2.readlines()

for count in range(1,101):
    output2=open("/storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/job_kin_{0:0d}.pbs".format(count),"w")
    for line in lines2:
        newline=line.replace("parallel_run_all_01","parallel_run_all_{0:0d}".format(count))
        #newline=newline.replace("cdm8_a_g_sc_default","cdm8_f_g_bc_default")
        output2.write(newline)


input3=open("/storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/lsqsolve.m","r")
lines3=input3.readlines()
for count in range(1,101):
    output3=open("/storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/lsqsolve_{0:0d}.m".format(count),"w")
    for line in lines3:
        newline=line.replace("save('xbest.mat','xbest','fbest')","save('xbest_{0:0d}.mat','xbest','fbest')".format(count))
        #newline=newline.replace("cdm8_a_g_sc_default","cdm8_f_g_bc_default")
        output3.write(newline)


input4=open("/storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/kineticestimate_v4.m","r")
lines4=input4.readlines()
for count in range(1,101):
    output4=open("/storage/home/cjf33/work/kineticcorr_v8juice_ATP_030521/kineticestimate_v4_{0:0d}.m".format(count),"w")
    for line in lines4:
        newline=line.replace("lsqsolve","lsqsolve_{0:0d}".format(count))
        #newline=newline.replace("load x_best.mat","load xbest_{0:0d}.mat".format(count))
        #newline=newline.replace("cdm8_a_g_sc_default","cdm8_f_g_bc_default")
        output4.write(newline)
