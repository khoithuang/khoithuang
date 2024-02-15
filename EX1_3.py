# I get help from ChatGPT especially on how to turn the equations into coding for python.
import math


def f(x, y, z):
    """
    Defines the function f(x, y, z) representing the given second-order ordinary differential equation (ODE).

    Parameters:
        x (float): Independent variable.
        y (float): Dependent variable.
        z (float): First derivative of y with respect to x.

    Returns:
        tuple: A tuple containing the first and second derivatives of y with respect to x.
    """
    return z, y + x


def improved_euler(x0, y0, z0, h, x):
    """
    Implements the Improved Euler method to approximate the solution of the given ODE.

    Parameters:
        x0 (float): Initial value of x.
        y0 (float): Initial value of y at x0.
        z0 (float): Initial value of the first derivative of y at x0.
        h (float): Step size for the numerical solution.
        x (float): Value of x at which the solution is desired.

    Returns:
        tuple: Approximate values of y and its first derivative at x.
    """
    while math.isclose(x0, x, abs_tol=1e-10) == False:
        # Compute the slope at the midpoint of the interval using the current slope
        z_half = z0 + (h / 2) * f(x0, y0, z0)[1]
        # Compute the approximate value of y at the midpoint of the interval
        y_half = y0 + (h / 2) * z0
        # Update the slope and y value using the slope at the midpoint
        z0 += h * f(x0 + h / 2, y_half, z_half)[1]
        y0 += h * z_half
        x0 += h
    return y0, z0


def runge_kutta(x0, y0, z0, h, x):
    """
    Implements the Runge-Kutta method to approximate the solution of the given ODE.

    Parameters:
        x0 (float): Initial value of x.
        y0 (float): Initial value of y at x0.
        z0 (float): Initial value of the first derivative of y at x0.
        h (float): Step size for the numerical solution.
        x (float): Value of x at which the solution is desired.

    Returns:
        tuple: Approximate values of y and its first derivative at x.
    """
    while math.isclose(x0, x, abs_tol=1e-10) == False:
        # Compute the slopes at four points within the interval
        k1y, k1z = f(x0, y0, z0)
        k2y, k2z = f(x0 + h / 2, y0 + (h / 2) * k1y, z0 + (h / 2) * k1z)
        k3y, k3z = f(x0 + h / 2, y0 + (h / 2) * k2y, z0 + (h / 2) * k2z)
        k4y, k4z = f(x0 + h, y0 + h * k3y, z0 + h * k3z)

        # Update y and z using the weighted sum of the slopes
        y0 += (h / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        z0 += (h / 6) * (k1z + 2 * k2z + 2 * k3z + k4z)
        x0 += h
    return y0, z0


def main():
    print("For the initial value problem y'' - y = x")
    y0 = float(input("Enter the value of y at x=0: "))
    z0 = float(input("Enter the value of y' at x=0: "))
    h = float(input("Enter the step size for the numerical solution: "))
    x = float(input("At what value of x do you want to know y and y'?: "))

    # Compute solutions using both methods
    ie_y, ie_z = improved_euler(0, y0, z0, h, x)
    rk_y, rk_z = runge_kutta(0, y0, z0, h, x)

    # Display the results
    print(f"At x={x:.3f}")
    print(f"For the improved Euler method: y={ie_y:.3f}, and y'={ie_z:.3f}")
    print(f"For the Runge-Kutta method: y={rk_y:.3f}, and y'={rk_z:.3f}")

    choice = input("Do you want to compute at a different x? (Y/N): ")
    if choice.upper() == "Y":
        main()
    else:
        print("Exiting...")


if __name__ == "__main__":
    main()
