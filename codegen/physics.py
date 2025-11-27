"""
codegen/physics.py - Physics simulation code generation
"""
import re


class PhysicsGenerator:
    """Generates code for physics scenarios"""
    
    @staticmethod
    def generate_pseudo(ir) -> str:
        """Generate pseudo-code for physics scenario"""
        pseudo = []
        pseudo.append("// PHYSICS SIMULATION")
        pseudo.append("// Kinematic and dynamic motion")
        pseudo.append("")
        pseudo.append("Initial Conditions:")
        pseudo.append("  position = [x0, y0, z0]")
        pseudo.append("  velocity = [vx0, vy0, vz0]")
        pseudo.append("  acceleration = [ax, ay, az]")
        pseudo.append("  mass = m")
        pseudo.append("")
        pseudo.append("Time Evolution (dt = timestep):")
        pseudo.append("  WHILE time < max_time:")
        pseudo.append("    // Update velocity (v = v0 + a*dt)")
        pseudo.append("    velocity += acceleration * dt")
        pseudo.append("    ")
        pseudo.append("    // Update position (x = x0 + v*dt)")
        pseudo.append("    position += velocity * dt")
        pseudo.append("    ")
        pseudo.append("    // Apply forces if needed")
        pseudo.append("    force = compute_forces(position, velocity)")
        pseudo.append("    acceleration = force / mass")
        pseudo.append("    ")
        pseudo.append("    time += dt")
        pseudo.append("")
        pseudo.append("Conservation Checks:")
        pseudo.append("  energy = 0.5 * mass * velocity² + potential_energy(position)")
        pseudo.append("  momentum = mass * velocity")
        
        return "\n".join(pseudo)
    
    @staticmethod
    def generate_python(ir) -> str:
        """Generate executable Python code for physics scenario"""
        code = []
        code.append('"""')
        code.append(f'Physics Simulation: {ir.raw_text}')
        code.append('"""')
        code.append('import numpy as np')
        code.append('import matplotlib.pyplot as plt')
        code.append('')
        code.append('')
        code.append('class PhysicsSimulator:')
        code.append('    """Simulates physical motion"""')
        code.append('    ')
        code.append('    def __init__(self, mass=1.0, gravity=9.81):')
        code.append('        self.mass = mass')
        code.append('        self.gravity = gravity')
        code.append('    ')
        code.append('    def projectile_motion(self, v0, angle_deg, dt=0.01, max_time=10):')
        code.append('        """')
        code.append('        Simulate projectile motion')
        code.append('        v0: initial velocity (m/s)')
        code.append('        angle_deg: launch angle (degrees)')
        code.append('        """')
        code.append('        angle_rad = np.radians(angle_deg)')
        code.append('        ')
        code.append('        # Initial conditions')
        code.append('        vx = v0 * np.cos(angle_rad)')
        code.append('        vy = v0 * np.sin(angle_rad)')
        code.append('        ')
        code.append('        x, y = 0.0, 0.0')
        code.append('        ')
        code.append('        positions = [(x, y)]')
        code.append('        velocities = [(vx, vy)]')
        code.append('        ')
        code.append('        time = 0.0')
        code.append('        while y >= 0 and time < max_time:')
        code.append('            # Update velocity (only gravity affects y)')
        code.append('            vy -= self.gravity * dt')
        code.append('            ')
        code.append('            # Update position')
        code.append('            x += vx * dt')
        code.append('            y += vy * dt')
        code.append('            ')
        code.append('            positions.append((x, y))')
        code.append('            velocities.append((vx, vy))')
        code.append('            ')
        code.append('            time += dt')
        code.append('        ')
        code.append('        return np.array(positions), np.array(velocities), time')
        code.append('    ')
        code.append('    def analyze_motion(self, positions, velocities, flight_time):')
        code.append('        """Analyze and display motion statistics"""')
        code.append('        max_height = positions[:, 1].max()')
        code.append('        range_x = positions[-1, 0]')
        code.append('        ')
        code.append('        print(f"Flight time: {flight_time:.2f} s")')
        code.append('        print(f"Maximum height: {max_height:.2f} m")')
        code.append('        print(f"Range: {range_x:.2f} m")')
        code.append('        ')
        code.append('        # Energy conservation check')
        code.append('        v_initial = np.linalg.norm(velocities[0])')
        code.append('        v_final = np.linalg.norm(velocities[-1])')
        code.append('        ')
        code.append('        E_initial = 0.5 * self.mass * v_initial**2')
        code.append('        E_final = 0.5 * self.mass * v_final**2')
        code.append('        ')
        code.append('        print(f"\\nEnergy: initial={E_initial:.2f} J, final={E_final:.2f} J")')
        code.append('')
        code.append('')
        code.append('# Run simulation')
        code.append('if __name__ == "__main__":')
        code.append('    sim = PhysicsSimulator(mass=1.0)')
        code.append('    ')
        
        # Try to extract numbers from text
        numbers = re.findall(r'\d+\.?\d*', ir.raw_text)
        if len(numbers) >= 1:
            v0 = numbers[0]
            angle = numbers[1] if len(numbers) >= 2 else "45"
        else:
            v0, angle = "20", "45"
        
        code.append(f'    # Simulate projectile: v0={v0} m/s at {angle}°')
        code.append(f'    positions, velocities, time = sim.projectile_motion(v0={v0}, angle_deg={angle})')
        code.append('    ')
        code.append('    sim.analyze_motion(positions, velocities, time)')
        code.append('    ')
        code.append('    # Optional: plot trajectory')
        code.append('    # plt.plot(positions[:, 0], positions[:, 1])')
        code.append('    # plt.xlabel("Distance (m)")')
        code.append('    # plt.ylabel("Height (m)")')
        code.append('    # plt.title("Projectile Trajectory")')
        code.append('    # plt.grid(True)')
        code.append('    # plt.show()')
        
        return "\n".join(code)


if __name__ == "__main__":
    from ir import IntermediateRepresentation
    
    ir = IntermediateRepresentation(
        raw_text="A ball is thrown at 20 m/s at a 45 degree angle.",
        category="physics"
    )
    
    gen = PhysicsGenerator()
    print(gen.generate_python(ir))
