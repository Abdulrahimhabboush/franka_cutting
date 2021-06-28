clear all
close all
clc
filepath = '/home/abdulrah/catkin_ws/src/all_rosbags/referance-chopping.bag';
bagfile = rosbag(filepath);
franka_states = readMessages(select(bagfile, 'Topic', '/franka_state_controller/franka_states'), 'DataFormat', 'struct');
bagselect = select(bagfile, 'Topic', '/franka_state_controller/F_ext');
msgs_c = readMessages(bagselect);
force = zeros(length(msgs_c), 3);
force_norm = zeros(length(msgs_c), 1);
torque = zeros(length(msgs_c), 3);
torque_norm = zeros(length(msgs_c), 1);
jointstate_time = [];
raw_time = zeros(1,length(franka_states));
position = zeros(3, length(franka_states));
roll_pitch_yaw = zeros(3, length(franka_states));
for i=1:length(msgs_c)
    jointstate_time(i) = msgs_c{i}.Header.Stamp.Sec + 10^-9*msgs_c{i}.Header.Stamp.Nsec;
    force(i,:) = [msgs_c{i}.Wrench.Force.X; msgs_c{i}.Wrench.Force.Y; msgs_c{i}.Wrench.Force.Z];
    force_norm(i) = norm(force(i,:),2);
    torque(i,:) = [msgs_c{i}.Wrench.Torque.X; msgs_c{i}.Wrench.Torque.Y; msgs_c{i}.Wrench.Torque.Z];
    torque_norm(i) = norm(torque(i,:),2);
end
jointstate_time = jointstate_time - jointstate_time(1);

for i=1:length(franka_states)
    raw_time(i) = franka_states{i,1}.Header.Stamp.Sec + franka_states{i,1}.Header.Stamp.Nsec*10^-9;
    position(:,i) = franka_states{i,1}.OTEE(13:15);
    roll_pitch_yaw(:,i) = transpose(rotm2eul([franka_states{i,1}.OTEE(1:3), franka_states{i,1}.OTEE(5:7), franka_states{i,1}.OTEE(9:11)]));
end
figure(1);
subplot(3,1,1);
plot(raw_time - raw_time(1), position(3,:));
xlim([30 45]);
xlabel('time [S]');
ylabel('EEpose Z coordinate [m]');
hold all

subplot(3,1,2); 
plot(jointstate_time, force_norm);
xlim([30 45]);
xlabel('time [S]');
ylabel('Force-norm [N]');
hold all

subplot(3,1,3); 
plot(jointstate_time, torque_norm);
xlim([30 45]);
xlabel('time [S]');
ylabel('Torque-norm [Nm]');
hold all
legend ('Chopping\_reference')
figure(2);
plot(raw_time - raw_time(1), position(3,:));
legend ('Chopping\_reference');
xlim([30 45]);
xlabel('time [S]');
ylabel('EEpose Z coordinate [m]');
hold all


figure(3); 
plot(jointstate_time, force_norm);
legend ('Chopping\_reference')
xlim([30 45]);
xlabel('time [S]');
ylabel('Force\_norm [N]');
hold all

figure(4); 
plot(jointstate_time, torque_norm);
legend ('Chopping\_reference')
xlim([30 45]);
xlabel('time [S]');
ylabel('Torque\_norm [Nm]');
hold all