I was thinking writing a launch file with several nodes. one node being

 <node name="rosbag" type="play"  pkg="rosbag" args="$(find  bag)/bags/First1.bag" >   </node>

and in the same launch file

<node name="rosbag" type="record"  pkg="rosbag" args="topicIwanttorecord" >   </node>

(Not really sure if that is how I should write the nodes but you get the idea)



