import pybullet as p
import time

client = p.connect(p.GUI)
p.setGravity(0, 0, -10, physicsClientId=client) 
p.loadURDF("cartpole.urdf") 

input("Press Enter to continue...")
