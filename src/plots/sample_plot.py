# Title			: Matplot with basic examples.
# Description	: The plot covers
#				: 	color
#				: 	marker style, size, color
#				:	annotation using arrow
#				: 	text and formatting
#				: 	linestyle, linewidth, color
# Reference [1]:https://prasanth-ntu.github.io/html/ML-Course/Matplotlib-Introduction/Matplotlib-Introduction-Notes.html
# Reference [2]: Text intro: https://matplotlib.org/3.1.0/tutorials/text/text_intro.html

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
print ("[INFO]: Matplotlib version: ", matplotlib.__version__ ) # Current version: 3.1.0

# ===
plt.figure(figsize=(12,8), facecolor=(.8, 0.9, 0.9),edgecolor=None)

x = np.random.rand(20)
y = np.random.rand(20)*10
z = np.random.randint(0,10,20)

# === Standard Plot === #
plt.subplot(2,2,1)
plt.plot(x,y, 'x')
plt.plot(x,z,'o')
plt.title('X-Y Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['y','z'])

# === Covers color, markersize, annotate using arrow === #
plt.subplot(2,2,3)
plt.plot(x,y, 'x', color='g')
plt.plot(x,z,'o', color=(1.0, 0.2, 0.3), markersize=13)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['y','z'])
plt.plot([.2], [4], 'o')
plt.annotate('annotate', xy=(.2, 4), xytext=(.4, 6), arrowprops=dict(facecolor='black', shrink=0.05))

# === Covers text annotation with formatting === #
plt.subplot(2,2,2)
plt.plot(y,'o-')
plt.plot(z,'x-')
plt.title('Time Series Plot')
plt.xlabel('t')
plt.ylabel('amplitude')
plt.legend(['y','z'])
plt.text(x=3, y=8, s='boxed italics text in data coords', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

# === Covers marker size, linestyle, linewidth === #
plt.subplot(2,2,4)
plt.plot(y, marker='+', linestyle="--", linewidth=5)
plt.plot(z, marker='>', linestyle="dashdot")
plt.xlabel('t')
plt.ylabel('amplitude')
plt.legend(['y','z'])

plt.savefig(os.path.join(os.getcwd(), 'sample_plot_1.png'), facecolor=(.8, 0.9, 0.9))
print ("[INFO]: Image saved successfully")
plt.show()
