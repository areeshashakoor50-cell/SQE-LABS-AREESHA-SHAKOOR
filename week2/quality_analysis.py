import matplotlib.pyplot as plt
import numpy as np

labels = ["Functional","Performance","Compatibility","Usability","Reliability","Security","Maintainability","Portability"]

google_maps = [5,4,5,5,4,5,5,5]
apple_maps = [4,5,4,5,3,5,4,3]

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()

google_maps += google_maps[:1]
apple_maps += apple_maps[:1]
angles += angles[:1]

plt.figure()
ax = plt.subplot(111, polar=True)

ax.plot(angles, google_maps, marker='o', label='Google Maps')
ax.plot(angles, apple_maps, marker='o', label='Apple Maps')

ax.fill(angles, google_maps, alpha=0.1)
ax.fill(angles, apple_maps, alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.title("ISO 25010 Quality Comparison")
plt.legend(loc='upper right')

plt.savefig("quality_radar_google_apple.png")
plt.show()