import math


class IntegrationError(Exception):
    pass


# INPUT
while True:
    try:
        left_endpoint = input("Write the left endpoint of the interval: ")
        right_endpoint = input("Write the right endpoint of the interval: ")
        function_expression = input("Write the function to integrate (in terms of x): ")
        method = input("Write the integration method (LRM/RRM/MRM/TRAP): ").upper()

        if "pi" in left_endpoint:
            left_endpoint = eval(left_endpoint.replace("pi", str(math.pi)))
        else:
            left_endpoint = float(left_endpoint)

        if "pi" in right_endpoint:
            right_endpoint = eval(right_endpoint.replace("pi", str(math.pi)))
        else:
            right_endpoint = float(right_endpoint)

        if method not in ("LRM", "RRM", "MRM", "TRAP"):
            raise ValueError("Invalid method selected. Choose LRM, RRM, MRM or TRAP.")

        # Test the expression once with a sample value to catch bad syntax early
        eval(function_expression.replace("x", str(left_endpoint)))

        break
    except ValueError as e:
        print(f"Error: {e}")
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        print(f"Error in the function expression: {e}")

# PROCESS
n = 1000
step_size = (right_endpoint - left_endpoint) / n
integral = 0.0

try:
    if method == "LRM":
        for i in range(n):
            x = left_endpoint + i * step_size
            fx = eval(function_expression.replace("x", str(x)))
            integral += fx * step_size

    elif method == "RRM":
        for i in range(1, n + 1):
            x = left_endpoint + i * step_size
            fx = eval(function_expression.replace("x", str(x)))
            integral += fx * step_size

    elif method == "MRM":
        for i in range(n):
            midpoint = left_endpoint + i * step_size + step_size / 2
            fx = eval(function_expression.replace("x", str(midpoint)))
            integral += fx * step_size

    elif method == "TRAP":
        left_value = eval(function_expression.replace("x", str(left_endpoint)))
        right_value = eval(function_expression.replace("x", str(right_endpoint)))
        integral = (left_value + right_value) / 2
        for i in range(1, n):
            x = left_endpoint + i * step_size
            fx = eval(function_expression.replace("x", str(x)))
            integral += fx
        integral *= step_size

except ZeroDivisionError:
    raise IntegrationError("Cannot complete the integration due to a division by zero.")
except Exception as e:
    raise IntegrationError(f"An unexpected error occurred while integrating: {e}")

# OUTPUT
print(f"The approximate integral of {function_expression} is {integral}")
