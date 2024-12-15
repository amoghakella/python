#Launching projectiles from cliffs solver, by Amogh Akella.
import math

#Fill in with your parameters
heightover = 1.17
velocity = 8.123
angle = 30
gravity = 9.8

#Computes initial values (radians)
angle = angle*math.pi/180
vx = velocity*math.cos(angle)
vy_0 = velocity*math.sin(angle)

#Computes final values
t = (vy_0 + math.sqrt(vy_0*vy_0 + 2*gravity*heightover))/gravity
dist = t*vx
vy_f = vy_0 - gravity*t
v_f = math.sqrt(vx*vx + vy_f*vy_f)
angle_f = math.atan(vy_f/vx)*180/math.pi

#Round to two decimal places
def round2(num):
  return float(round(num*100))/100

#Print
print("Airtime: " + str(round2(t)))
print("Distance: " + str(round2(dist)))
print("Impact velocity: " + str(round2(v_f)))
print("Impact angle (below the horizontal): " + str(round2(-angle_f)))
