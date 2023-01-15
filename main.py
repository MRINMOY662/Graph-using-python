from vpython import *

# Create a cylinder for the body of the spacecraft
body = cylinder(pos=vector(0,0,0), axis=vector(0,1,0), radius=1, color=color.red)

# Create a cone for the nose of the spacecraft
nose = cone(pos=vector(0,1,0), axis=vector(0,2,0), radius=0.5, color=color.yellow)

# Create a sphere for the cockpit of the spacecraft
cockpit = sphere(pos=vector(0,2.5,0), radius=0.25, color=color.green)

# Create a rocket engine at the back of the spacecraft
engine = cylinder(pos=vector(0,-0.5,0), axis=vector(0,-1,0), radius=0.25, color=color.white)

# Create a scene and display the spacecraft
scene = canvas()
