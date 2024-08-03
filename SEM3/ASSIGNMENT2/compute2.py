import math
sin_60_deg = math.sin(math.radians(60))
print("Sin of 60 degrees:", sin_60_deg)
cos_pi = math.cos(math.pi)
print("Cos of pi:", cos_pi)
sin_value = math.sin(0.8660254037844386)
print("Sin of 0.8660254037844386:", sin_value)
try:
    tan_90_deg = math.tan(math.radians(90))
except ValueError:
    tan_90_deg = float('inf')
print("Tan of 90 degrees:", tan_90_deg)
