import numpy as np
import pandas as pd

df = pd.read_csv('q6_projectile.csv')

time = df['time'].values
position = df['position'].values

# Average velocity = change in position / change in time (over each interval)
delta_pos = np.diff(position)
delta_time = np.diff(time)
velocities = delta_pos / delta_time

avg_velocity = np.mean(velocities)

print("Projectile Data (first 10 rows):")
print(df.head(10).to_string(index=False))
print(f"\nTotal time elapsed:         {time[-1] - time[0]:.3f} s")
print(f"Total displacement:         {position[-1] - position[0]:.3f} m")
print(f"Overall average velocity:   {(position[-1]-position[0])/(time[-1]-time[0]):.3f} m/s")
print(f"Mean of interval velocities:{avg_velocity:.3f} m/s")
