"""
codegen/physics.py - Physics simulation code generation
"""
import re


class PhysicsGenerator:
    """Generates code for physics scenarios"""

    @staticmethod
    def generate_pseudo(ir) -> str:
        """Generate pseudo-code for physics scenario"""
        pseudo = [
            "// PHYSICS SIMULATION",
            "// Kinematic and dynamic motion",
            "",
            "Initial Conditions:",
            "  position = [x0, y0, z0]",
            "  velocity = [vx0, vy0, vz0]",
            "  acceleration = [ax, ay, az]",
            "  mass = m",
            "",
            "Time Evolution (dt = timestep):",
            "  WHILE time < max_time:",
            "    // Update velocity (v = v0 + a*dt)",
            "    velocity += acceleration * dt",
            "    ",
            "    // Update position (x = x0 + v*dt)",
            "    position += velocity * dt",
            "    ",
            "    // Apply forces if needed",
            "    force = compute_forces(position, velocity)",
            "    acceleration = force / mass",
            "    ",
            "    time += dt",
            "",
            "Conservation Checks:",
            "  energy = 0.5 * mass * velocity² + potential_energy(position)",
            "  momentum = mass * velocity",
        ]
        return "\n".join(pseudo)

    @staticmethod
    def generate_python(ir) -> str:
        """Generate executable Python code for physics scenario"""
        code = [
            '"""',
            f"Physics Simulation: {ir.raw_text}",
            '"""',
            "import numpy as np",
            "import matplotlib.pyplot as plt",
            "",
            "",
            "class PhysicsSimulator:",
            '    """Simulates physical motion"""',
            "    ",
            "    def __init__(self, mass=1.0, gravity=9.81):",
            "        self.mass = mass",
            "        self.gravity = gravity",
            "    ",
            "    def projectile_motion(self, v0, angle_deg, dt=0.01, max_time=10):",
            '        """',
            "        Simulate projectile motion",
            "        v0: initial velocity (m/s)",
            "        angle_deg: launch angle (degrees)",
            '        """',
            "        angle_rad = np.radians(angle_deg)",
            "        ",
            "        # Initial conditions",
            "        vx = v0 * np.cos(angle_rad)",
            "        vy = v0 * np.sin(angle_rad)",
            "        ",
            "        x, y = 0.0, 0.0",
            "        positions = [(x, y)]",
            "        velocities = [(vx, vy)]",
            "        ",
            "        time = 0.0",
            "        while y >= 0 and time < max_time:",
            "            vy -= self.gravity * dt",
            "            x += vx * dt",
            "            y += vy * dt",
            "            positions.append((x, y))",
            "            velocities.append((vx, vy))",
            "            time += dt",
            "        ",
            "        return np.array(positions), np.array(velocities), time",
            "    ",
            "    def analyze_motion(self, positions, velocities, flight_time):",
            '        """Analyze and display motion statistics"""',
            "        max_height = positions[:, 1].max()",
            "        range_x = positions[-1, 0]",
            "        ",
            "        print(f\"Flight time: {flight_time:.2f} s\")",
            "        print(f\"Maximum height: {max_height:.2f} m\")",
            "        print(f\"Range: {range_x:.2f} m\")",
            "        ",
            "        v_initial = np.linalg.norm(velocities[0])",
            "        v_final = np.linalg.norm(velocities[-1])",
            "        E_initial = 0.5 * self.mass * v_initial**2",
            "        E_final   = 0.5 * self.mass * v_final**2",
            "        print(f\"\\nEnergy: initial={E_initial:.2f} J, final={E_final:.2f} J\")",
            "",
            "",
            "# Run simulation",
            'if __name__ == "__main__":',
            "    sim = PhysicsSimulator(mass=1.0)",
            "    ",
        ]

        # FIX: re.findall returns strings; must cast to float before embedding in
        # the generated call — otherwise the generated code passes string literals
        # to projectile_motion() which then fails on np.cos("20") etc.
        numbers = re.findall(r"\d+\.?\d*", ir.raw_text)
        if len(numbers) >= 1:
            v0 = float(numbers[0])
            angle = float(numbers[1]) if len(numbers) >= 2 else 45.0
        else:
            v0, angle = 20.0, 45.0

        code.append(f"    # Simulate projectile: v0={v0} m/s at {angle}°")
        code.append(f"    positions, velocities, time = sim.projectile_motion(v0={v0}, angle_deg={angle})")
        code += [
            "    ",
            "    sim.analyze_motion(positions, velocities, time)",
            "    ",
            "    # Optional: uncomment to plot trajectory",
            "    # plt.plot(positions[:, 0], positions[:, 1])",
            "    # plt.xlabel('Distance (m)')",
            "    # plt.ylabel('Height (m)')",
            "    # plt.title('Projectile Trajectory')",
            "    # plt.grid(True)",
            "    # plt.show()",
        ]

        return "\n".join(code)


if __name__ == "__main__":
    from ir import IntermediateRepresentation

    ir = IntermediateRepresentation(
        raw_text="A ball is thrown at 20 m/s at a 45 degree angle.",
        category="physics",
    )

    gen = PhysicsGenerator()
    print(gen.generate_python(ir))
