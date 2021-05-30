%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
tic
res={};
model=modcompile(strcat(pwd,'/007WT_model.xlsx'),strcat(pwd,'/007WT_mechanism_mod.xlsx'),strcat(pwd,'/007WT_data_FUM.xlsx'));
% model.d.vpert(19,2)=0.5;
% model.d.vpert(39,2)=0.5;
% model.d.vpert(19,3)=0.2;
% model.d.vpert(39,3)=0.2;
% model.d.vpert(24,3)=1;
% model.d.vpert(12,3)=5;
% model.d.vpert(19,4)=0.5;
% model.d.vpert(39,4)=0.5;
% model.d.vpert(19,5)=1;
% model.d.vpert(43,5)=0.1;
% model.d.vpert(43,9)=0.5;
%model.options.multistarts=3;
try
	%load xbest.mat
	%model.fstore = fbest;
    model.fstore = Inf;
catch
	model.fstore = Inf;
end

res=kineticestimate(model,res);
tout = toc;

save('optimal.mat','res','model','tout');

