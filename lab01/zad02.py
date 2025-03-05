import random
import math
import matplotlib

# matplotlib.use('TkAgg')  # Wymuszenie backendu
import matplotlib.pyplot as plt
import numpy as np

h = 100 # metrów wysokości
v0 = 50 # m/s
g = 9.81  # przyspieszenie grawitacyjne (m/s^2)
counter = 0
# użytkownik podaje alfa, d (odległość) się sama wylicza

def set_target():
    target = random.randint(50, 340)
    return target

def calculate_trajectory(alpha):
    alpha_rad = math.radians(alpha)
    
    v_x = v0 * math.cos(alpha_rad)
    v_y = v0 * math.sin(alpha_rad)

    t_flight = (v_y + math.sqrt(v_y**2 + 2 * g * h)) / g
    d = v_x * t_flight

    return d

def visualized_trajectory(alpha, h, d):
    alpha_rad = math.radians(alpha)
    v_x = v0 * math.cos(alpha_rad)
    v_y = v0 * math.sin(alpha_rad)

    t_flight = (v_y + math.sqrt(v_y**2 + 2 * g * h)) / g
    t = np.linspace(0, t_flight, num=100)
    x = v_x * t
    y = h + v_y * t - 0.5 * g * t**2

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label="Trajektoria lotu pocisku")
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.axvline(d, color='red', linestyle='--', label="Cel")
    plt.xlabel("Odległość d (m)")
    plt.ylabel("Wysokość h (m)")
    plt.title("Ruch ukośny pocisku")
    plt.legend()
    plt.grid()
    plt.show(block=True)
    
target = set_target()

print(f"\nNasz cel znajduje się w odległości \n {target}m\n")

while True:
    alpha = int(input("Podaj kąt rzutu (stopnie): "))
    
    distance = calculate_trajectory(alpha)
    print(f"Zasięg rzutu ukośnego wynosi: {distance:.2f} m")
    counter += 1
    if target+5 > distance > target-5:
        print(f"Cel trafiony!\n Ilość twoich prób: {counter}")
        visualized_trajectory(alpha, h, target)
        break
    else:
        print("Spróbuj jeszcze raz!")
        print(counter)

