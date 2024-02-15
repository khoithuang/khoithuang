
def improved_euler_step(y, z, h):
    """Performs an Improved Euler method step."""
    y_mid = y + h * z / 2
    z_mid = z + h * y / 2
    y_next = y + h * z_mid
    z_next = z + h * y_mid
    return y_next, z_next

def runge_kutta_step(y, z, h):
    """Performs a Runge-Kutta method step."""
    k1_y = h * z
    k1_z = h * y

    k2_y = h * (z + k1_z / 2)
    k2_z = h * (y + k1_y / 2)

    k3_y = h * (z + k2_z / 2)
    k3_z = h * (y + k2_y / 2)

    k4_y = h * (z + k3_z)
    k4_z = h * (y + k3_y)

    y_next = y + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6
    z_next = z + (k1_z + 2*k2_z + 2*k3_z + k4_z) / 6
    return y_next, z_next

def solve_ode(y0, z0, h, x_target):
    x = 0
    y = y0
    z = z0

    while x < x_target:
        y, z = improved_euler_step(y, z, h)
        x += h

    print(f"At x={x_target:.3f}")
    print(f"For the Improved Euler method: y={y:.3f}, and y'={z:.3f}")

    # Reset initial conditions
    x = 0
    y = y0
    z = z0

    while x < x_target:
        y, z = runge_kutta_step(y, z, h)
        x += h

    print(f"For the Runge-Kutta method: y={y:.3f}, and y'={z:.3f}")

# Sample interaction with the user
print("For the initial value problem y'' - y = x''")
y0 = float(input("Enter the value of y at x=0: "))
z0 = float(input("Enter the value of y' at x=0: "))
h = float(input("Enter the step size for the numerical solution: "))
x_target = float(input("At what value of x do you want to know y and y'? "))

solve_ode(y0, z0, h, x_target)

choice = input("Do you want to compute at a different x? (Y/N) ")
while choice.lower() == 'y':
    x_target = float(input("At what value of x do you want to know y and y'? "))
    solve_ode(y0, z0, h, x_target)
    choice = input("Do you want to compute at a different x? (Y/N) ")
