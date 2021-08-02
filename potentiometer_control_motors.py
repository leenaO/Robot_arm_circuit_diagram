#include <Servo.h>
Servo servo1, servo2, servo3, servo4, servo5;
void setup(){
  servo1.attach(8, 200, 9700);
  servo2.attach(9, 200, 9700);
  servo3.attach(10, 200, 9700);
  servo4.attach(11, 200, 9700);
  servo5.attach(12, 200, 9700);
  }
void loop(){
  int ang1 = map (analogRead(A0), 0, 1023, 0, 180);
  int ang2 = map (analogRead(A1), 0, 1023, 0, 180);
  int ang3 = map (analogRead(A2), 0, 1023, 0, 180);
  int ang4 = map (analogRead(A3), 0, 1023, 0, 180);
  int ang5 = map (analogRead(A4), 0, 1023, 0, 180);
  servo1.write(ang1);
  servo2.write(ang2);
  servo3.write(ang3);
  servo4.write(ang4);
  servo5.write(ang5);
}
