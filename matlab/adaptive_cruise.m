m = 1000;
b = 50;
r = 10;

s = tf('s');
plant_tf = 1/(m*s + b);

Kp = 1000;
controller = pid(Kp);

tf_closed_loop = feedback(controller*plant_tf, 1);

%% P controller
t = 0:0.1:20;
step(r*tf_closed_loop, t)
axis([0 20 0 10])

%% PID controller
Kp = 800;
Ki = 40;
controller = pid(Kp, Ki);

tf_closed_loop = feedback(controller*plant_tf, 1);

step(r*tf_closed_loop, t);
axis([0 20 0 10])