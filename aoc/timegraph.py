import aoc
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

colorkey = {
    0 : "#6fa87a",
    "numpy" : "#588acb",
    "multiprocessing": "#d4875d",
    "networkx": "#e3b763"
}


# Create a custom formatter to add "s" to y-axis labels
def add_s_formatter(x, pos):
    return f"{x:.1f}s"

legend_patches = [
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=color, markersize=10, label=str(key))
    for key, color in colorkey.items() if key != 0
]

def plot_custom_bar_graph(values, probs, yline=1.0):
    fsize = 16
    # Create the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(range(1,1+len(values)), values, color=[colorkey[probs[v]] for v in range(1,26)],edgecolor="black", zorder=2)
    plt.legend(handles=legend_patches, loc="upper left", frameon=True, fontsize=fsize,
        bbox_to_anchor=(0.05,0.95))
    
    plt.gca().yaxis.set_major_formatter(FuncFormatter(add_s_formatter))

    # Add a dotted line at the specified y-value
    for y in range(2, 9, 2):
      plt.axhline(y=y/10.0, color='gray', linestyle='dotted', linewidth=1.5, zorder=1)
    plt.axhline(y=1.0, color='black', linestyle='--', linewidth=1.5)
    
    # Add labels and title
    plt.xlabel('Problem', fontsize=fsize)
    plt.xticks(range(1,26),fontsize=fsize)
    plt.yticks(fontsize=fsize)
    plt.title('Advent of Code 2024, runtimes in Python 3.13', fontsize=fsize+5, pad=20)
    
    # Show the graph
    plt.tight_layout()
    plt.show()

probs = {}
for i in range(1, 26):
  probs[i] = 0
  probtext = open("adv%02d-r.py" % i, "rt").read()
  for k in colorkey:
    if k != 0 and k in probtext:
      probs[i] = k
lines = [line for line in sys.stdin.readlines() if "real" in line]
times = [float(t.s) + 60 * t.m for t in aoc.retuple_read("m_ s", r"real\s+(\d+)m(.*)s", lines)]
plot_custom_bar_graph(times, probs, 1.0)
