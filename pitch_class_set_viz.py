import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle

def create_pitch_class_viz(pitches, filename=None):
    n_pitches = 12
    top = np.pi / 2
    full_rotation = 2 * np.pi
    theta = np.linspace(top, top - full_rotation, endpoint=True, num=n_pitches+1)
    r = 2.5

    xs = r * np.cos(theta)
    ys = r * np.sin(theta)

    poly = Polygon(np.column_stack([xs, ys]), animated=True)


    circle = Circle((0, 0), r)

    fig, ax = plt.subplots(figsize=(10,10))
    ax.add_patch(circle,)

    x, y = zip(*poly.xy)

    # print(xs, ys)
    line_x = [xs[i] for i in pitches]
    line_x.append(xs[pitches[0]])
    line_y = [ys[i] for i in pitches]
    line_y.append(ys[pitches[0]])
    # print("line")
    # print(line_x, line_y)
    line = Line2D(line_x, line_y, color="black",
                        marker='o', markerfacecolor='r',
                        animated=True)
    ax.add_line(line)
    ax.scatter(xs, ys, color="black", marker="o", zorder=2)

    for i, pair in enumerate(zip(x[:-1],ys[:-1])):
        coords = [1.1 * p for p in pair]
        ax.annotate(i, xy=coords)

    ax.set_axis_off()
    ax.set_xlim((-2, 2))
    ax.set_ylim((-2, 2))
    ax.set_title(f"{pitches}")
    ax.set_facecolor("grey")
    # plt.show()
    if filename is not None:
        fig.savefig(filename)
