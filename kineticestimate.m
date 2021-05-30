function [res] = kineticestimate(model,res)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

nst = model.options.multistarts;
fmin = Inf;
model.options.dfbase = 1e-6;
for i = 1:nst
    if model.options.reinit
        [x0,A,b,actcon] = initialize_v4(model);
        %load x_best.mat
        %x0 = xbest;
    else
        [~,A,b] = initialize_v4(model);
        x0 = res.reinit_data;
        actcon = find(A*x0<=b);
    end
    [x,f,~,actcon] = lsqsolve(x0,model,A,b,actcon);
    if f<model.fstore
        model.fstore = f;
    xint = x;
    end

    if f<model.fstore
        fmin = f;
        xint = x;
    end
end

model.options.dfbase = eps;
iter = 0;
fail = true;
x = xint;
xopt = x;
ac = actcon;
while fail || iter<=1
    [x,f,fail,ac] = lsqsolve(x,model,A,b,ac);
    if f<model.fstore
        model.fstore = f;
    end
    if f<model.fstore
        model.fstore = f;
        xopt = x;
        actcon = ac;
    end
    iter = iter+1;
end

res = compileresult(xopt,model);

end

