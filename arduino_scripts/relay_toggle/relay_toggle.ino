/*
   rosserial Subscriber
   Toggels the state of a relay
*/

#include <ros.h>
#include <std_msgs/Empty.h>

ros::NodeHandle nh;

int rpin = 2;

void on_function( const std_msgs::Empty& toggle_msg) {
  digitalWrite(rpin, HIGH);

}

void off_function( const std_msgs::Empty& toggle_msg) {
  digitalWrite(rpin, LOW);

}

ros::Subscriber<std_msgs::Empty> sub1("relay_on", &on_function );
ros::Subscriber<std_msgs::Empty> sub2("relay_off", &off_function );

void setup()
{
  pinMode(rpin, OUTPUT);
  nh.initNode();
  nh.subscribe(sub1);
  nh.subscribe(sub2);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
