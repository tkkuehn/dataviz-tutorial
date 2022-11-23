import numpy as np
import matplotlib.pyplot as plt

RNG = np.random.default_rng(1)


def generate_data():
    """Generate some random example data."""
    x_data = np.linspace(0, 2, 7)
    y_data = RNG.uniform(-0.75, 0.5, 7)

    return x_data, y_data


def basic_plot(x_data, y_data):
    fig, ax = plt.subplots()
    ax.plot(x_data, y_data)
    return fig, ax


def plot_custom_colour(ax, x_data, y_data):
    line, = ax.plot(x_data, y_data, color="black")
    line.set_linewidth(2)
    return ax, line


def adjust_ticks(ax, x_ticks, y_ticks):
    ax.tick_params(labelsize=8)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    return ax

def remove_x_ticks(ax):
    ax.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)

    return ax

def add_labels(ax, x_label=None, y_label=None):
    if x_label:
        ax.set_xlabel(x_label, size=8)
    if y_label:
        ax.set_ylabel(y_label, size=8)

    return ax


def remove_box(ax, x_bounds=None, y_bounds=None):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if x_bounds:
        ax.spines["bottom"].set_bounds(x_bounds)
    else:
        ax.spines["bottom"].set_visible(False)
    if y_bounds:
        ax.spines["left"].set_bounds(y_bounds)
    else:
        ax.spines["left"].set_visible(False)
    return ax


def main():
    my_data = generate_data()
    width = 2.63 
    fig, axes = plt.subplots(2, 1, figsize=(width, width / 1.5), dpi=300, layout="tight")
    ax = axes[0]
    ax, _ = plot_custom_colour(ax, *my_data)
    ax = adjust_ticks(ax, my_data[0][::2], [min(my_data[1]), 0, max(my_data[1])])
    ax = remove_x_ticks(ax)
    ax = remove_box(ax, y_bounds=(min(my_data[1]), max(my_data[1])))
    ax = add_labels(ax, y_label="Series 1")

    ax = axes[1]
    ax, _ = plot_custom_colour(ax, *my_data)
    ax = adjust_ticks(ax, my_data[0][::2], [min(my_data[1]), 0, max(my_data[1])])
    ax = add_labels(ax, x_label="Time (s)", y_label="Series 2")
    ax = remove_box(ax, (min(my_data[0]), max(my_data[0])), (min(my_data[1]), max(my_data[1])))

    fig.supylabel("Voltage (V)", size=8)

    plt.savefig("line.tiff")
    plt.savefig("line.eps")
    plt.show()


if __name__ == "__main__":
    main()
