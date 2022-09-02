import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from itertools import combinations

def create_clock_diagram(pitches, filename=None, draw_all_arcs=False, save_diagram=False):
    n_pitches = 12
    top = math.pi / 2
    full_rotation = 2 * math.pi
    angles = [top - full_rotation * (i / n_pitches) for i in range(n_pitches)]
    r = 1

    xs = [r * math.cos(angle) for angle in angles]
    ys = [r * math.sin(angle) for angle in angles]
    
    fig, ax = plt.subplots(figsize=(10,10))

    circle = Circle((0, 0), r)
    ax.add_patch(circle)


    line_x = [xs[i] for i in pitches]
    line_x.append(xs[pitches[0]])
    line_y = [ys[i] for i in pitches]
    line_y.append(ys[pitches[0]])


    arcs = []
    points = list(zip(xs, ys))
    if draw_all_arcs:
        for p1, p2 in combinations(points, 2):
            arc_x = [p1[0], p2[0]]
            arc_y = [p1[1], p2[1]]
            arc = Line2D(line_x, line_y, color="black", marker='o')
            arcs.append(arcs)
        for arc in arcs:
            ax.add_line(arc)

    line = Line2D(line_x, line_y, color="black",
                        marker='o', markerfacecolor='r')
    ax.add_line(line)

    ax.scatter(xs, ys, color="black", marker="o", zorder=2)

    for i, pair in enumerate(zip(xs,ys)):
        coords = [1.1 * p for p in pair]
        ax.annotate(i, xy=coords)

    ax.set_axis_off()
    ax.set_xlim((-2, 2))
    ax.set_ylim((-2, 2))
    ax.set_title(f"{pitches}")
    if filename is not None:
        fig.savefig(filename)
    if save_diagram:
        pitch_string = "-".join([str(p) for p in pitches])
        fig.savefig(f"{pitch_string}.png")

if __name__ == "__main__":
    create_clock_diagram([0, 1, 4], save_diagram=True)
    create_clock_diagram([0, 2, 7], "test2.png")