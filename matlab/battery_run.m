%% Load data
Data = xlsread('Battery_Parameters.xlsx');

%% Name the data
soc = Data(:,1);
ocv = Data(:,2);
R_Charge = Data(:,3);
R_Discharge = Data(:,4);

%% Plot
plot(soc, ocv)
figure
plot(soc, R_Charge)
figure
plot(soc, R_Discharge)

%% Define parameters
I = 2.3;
Cn = 2.3 * 3600; %capacity
sim_time = 3600;

%% 
sim('battery');
