%% Plant/Simulation paramters
sim_time = 7;
step_final = 1;
M = 1;
b = 10;
k = 20;

%% Controller parameters
%Kp = 200;
%Ki = 0;
%Kd = 0;
%sim('pid_tune');

%% PID controller
Kp = 37.8;
Ki = 114.7;
Kd = 2.438;
sim('pid_tune');

%% Plotting
figure
plot(out.IN.Time, out.IN.Data)
hold all
plot(out.OUT.Time, out.OUT.Data)
