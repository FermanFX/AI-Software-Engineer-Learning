import math

# --- Vahidlərin Çevrilməsi Funksiyaları ---
def in_to_m(inch): return inch * 0.0254
def in2_to_m2(inch2): return in_to_m(inch2) * in_to_m(1)
def in3_to_m3(inch3): return in2_to_m2(inch3) * in_to_m(1)
def ft_to_m(ft): return ft * 0.3048
def ft2_to_m2(ft2): return ft2 * (0.3048**2)
def ft3_to_m3(ft3): return ft3 * (0.3048**3)
def oz_to_kg(oz): return oz * 0.0283495

# --- Həndəsi Hesablamalar ---
def area_rectangle(length, width): return length * width
def volume_rect_cuboid(length, width, depth): return area_rectangle(length, width) * depth
def area_circle(radius): return math.pi * (radius**2)
def volume_cylinder(radius, depth): return area_circle(radius) * depth

# --- Miqdar Hesablamaları ---
def density(mass, volume): return mass / volume
def weight(density, volume, gravity): return density * volume * gravity
def pressure(force, area): return force / area

# --- Əsas Hesablama Funksiyaları (Hovuzlar üçün) ---
def Pa_bottom_rect_pool(length, width, depth, gravity):
    vol_m3 = ft3_to_m3(volume_rect_cuboid(length, width, depth))
    area_m2 = ft2_to_m2(area_rectangle(length, width))
    weight_force = weight(water_density_si, vol_m3, gravity)
    return pressure(weight_force, area_m2)

def Pa_bottom_circ_pool(radius, depth, gravity):
    vol_m3 = ft3_to_m3(volume_cylinder(radius, depth))
    area_m2 = ft2_to_m2(area_circle(radius))
    weight_force = weight(water_density_si, vol_m3, gravity)
    return pressure(weight_force, area_m2)

# --- Sabitlər ---
# Suyun sıxlığı: 0.58 oz/in^3 -> kg/m^3 çevrilməsi
water_density_si = density(oz_to_kg(0.58), in3_to_m3(1))
G_EARTH = 9.80665
G_MOON = 1.62

# --- Hesablamalar və Nəticələr ---
pools = [
    {"ad": "a", "tip": "rect", "l": 20, "w": 10, "d": 6, "vol": volume_rect_cuboid(20, 10, 6), "area": area_rectangle(20, 10)},
    {"ad": "b", "tip": "rect", "l": 10, "w": 10, "d": 8, "vol": volume_rect_cuboid(10, 10, 8), "area": area_rectangle(10, 10)},
    {"ad": "c", "tip": "circ", "r": 5, "d": 2, "vol": volume_cylinder(5, 2), "area": area_circle(5)},
    {"ad": "d", "tip": "circ", "r": 9, "d": 1.5, "vol": volume_cylinder(9, 1.5), "area": area_circle(9)}
]

print(f"{'Hovuz':<8} | {'Həcm (ft3)':<12} | {'Sahə (ft2)':<12} | {'Yer (Pa)':<12} | {'Ay (Pa)':<12}")
print("-" * 65)

for p in pools:
    if p["tip"] == "rect":
        p_earth = Pa_bottom_rect_pool(p["l"], p["w"], p["d"], G_EARTH)
        p_moon = Pa_bottom_rect_pool(p["l"], p["w"], p["d"], G_MOON)
    else:
        p_earth = Pa_bottom_circ_pool(p["r"], p["d"], G_EARTH)
        p_moon = Pa_bottom_circ_pool(p["r"], p["d"], G_MOON)
    
    print(f"{p['ad']:<8} | {p['vol']:>12.2f} | {p['area']:>12.2f} | {p_earth:>12.3f} | {p_moon:>12.3f}")

# Maksimumları tapmaq
max_vol = max(pools, key=lambda x: x['vol'])
max_area = max(pools, key=lambda x: x['area'])

print(f"\nMaksimum Həcm: Hovuz {max_vol['ad']} ({max_vol['vol']:.2f} ft³)")
print(f"Maksimum Sahə: Hovuz {max_area['ad']} ({max_area['area']:.2f} ft²)")


#Outputs
# Hovuz    | Həcm (ft3)   | Sahə (ft2)   | Yer (Pa)     | Ay (Pa)     
# -----------------------------------------------------------------
# a        |      1200.00 |       200.00 |    17995.302 |     2972.716
# b        |       800.00 |       100.00 |    23993.736 |     3963.622
# c        |       157.08 |        78.54 |     5998.434 |      990.905
# d        |       381.70 |       254.47 |     4498.825 |      743.179

# Maksimum Həcm: Hovuz a (1200.00 ft³)
# Maksimum Sahə: Hovuz d (254.47 ft²)