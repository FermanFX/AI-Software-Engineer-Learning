import math

def normal_pdf(x, mu, sigma):
    """Calculates the PDF of a Normal Distribution."""
    part1 = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu)**2) / (2 * sigma**2)
    return part1 * math.exp(exponent)

versions_list = [
    {"mu": 0, "sigma": 1, "x": 0.5},
    {"mu": 3, "sigma": 0.1, "x": -2.8},
    {"mu": -1, "sigma": 3, "x": -1}
]

for s in versions_list:
    y = normal_pdf(s["x"], s["mu"], s["sigma"])
    print(f"For mu={s['mu']}, sigma={s['sigma']}, x={s['x']}: y = {y:.10f}")


# Outputs
# For mu=0, sigma=1, x=0.5: y = 0.3520653268
# For mu=3, sigma=0.1, x=-2.8: y = 0.0000000000
# For mu=-1, sigma=3, x=-1: y = 0.1329807601