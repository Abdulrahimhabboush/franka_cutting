clear all

close all

clc
filepath = '/home/abdulrah/catkin_ws/src/rosbag2/*.bag';
FileList = dir('/home/abdulrah/catkin_ws/src/rosbag2/*.bag');
N = size(FileList,1);
dir = FileList.folder;
m = [];
for k = 1:N
file = fullfile(dir, FileList(k).name);
bagselect = rosbag(file);
bagfile = rosbag(file);
bagselect = select(bagfile, 'Topic', '/franka_state_controller/F_ext');
msgs_c = readMessages(bagselect);
force = zeros(length(msgs_c), 3);
force_norm = zeros(length(msgs_c), 1);
torque = zeros(length(msgs_c), 3);
jointstate_time = [];
for i=1:length(msgs_c)
    jointstate_time(i) = msgs_c{i}.Header.Stamp.Sec + 10^-9*msgs_c{i}.Header.Stamp.Nsec;
    force(i,:) = [msgs_c{i}.Wrench.Force.X; msgs_c{i}.Wrench.Force.Y; msgs_c{i}.Wrench.Force.Z];
    force_norm(i) = norm(force(i,:),2);
    %torque(i,:) = msgs_c{i}.Wrench.Torque;
end
m(k) = mean(force_norm);
jointstate_time = jointstate_time - jointstate_time(1);
plot(jointstate_time, force_norm)
hold all
legend show
end