import time
# Correcting the imports based on common pysimverse structure
try:
    from pysimverse.simulator import Simulator
    from pysimverse.drone import Drone
except ImportError:
    # Fallback if your version uses 'client'
    from pysimverse.client import DroneClient as Drone
    from pysimverse.client import SimulatorClient as Simulator

def fly_fast():
    # Initialize the simulator
    sim = Simulator()
    drone = Drone()
    
    print("Connecting and Taking Off...")
    sim.start()
    
    # Arm and Takeoff
    drone.arm()
    drone.takeoff(altitude=5)
    time.sleep(2)

    print("Executing High Speed Maneuver...")
    # To fly fast, we tilt (Pitch) forward and push Throttle
    # Parameters: (roll, pitch, yaw, throttle)
    # Pitch -0.6 = Heavy forward lean
    # Throttle 0.8 = High power to maintain height while leaning
    drone.set_controls(0.0, -0.6, 0.0, 0.8)
    
    # Fly fast for 5 seconds
    time.sleep(5)
    
    print("Braking and Hovering...")
    drone.set_controls(0, 0.2, 0, 0.5) # Slight back-pitch to slow down
    time.sleep(1)
    drone.hover()

    print("Landing...")
    drone.land()
    sim.stop()

if __name__ == "__main__":
    fly_fast()