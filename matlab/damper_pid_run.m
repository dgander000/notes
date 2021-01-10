%% Plant/Simulation paramters
sim_time = 7;
step_value = 1;
M = 1;
b = 10;
k = 20;

%% Controller parameters
Kp = 200;
Ki = 0;
Kd = 0;
sim('damper_pid');

%% PID controller
Kp = 350;
Ki = 300;
Kd = 50;
sim('damper_pid');

%% Plotting
figure
plot(out.IN.Time, out.IN.Data)
hold all
plot(out.OUT.Time, out.OUT.Data)
