import numpy as np
import matplotlib.pyplot as plt

RNG = np.random.default_rng(1)


def generate_data(num_sets):
    """Generate some random example data."""
    x_data = np.linspace(0, 2, 7)
    y_data = RNG.uniform(-0.75, 0.5, (7, num_sets))

    return x_data, y_data


def basic_plot(x_data, y_data):
    fig, ax = plt.subplots()
    ax.plot(x_data, y_data)
    return fig, ax


def plot_custom_colour(ax, x_data, y_data):
    (line,) = ax.plot(x_data, y_data, color="black")
    return line


def adjust_ticks(ax, x_ticks, y_ticks):
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)


def add_labels(ax, x_label=None, y_label=None):
    if x_label:
        ax.set_xlabel(x_label, size=8)
    if y_label:
        ax.set_ylabel(y_label, size=8)


def remove_box(ax, x_bounds=None, y_bounds=None):
    if x_bounds:
        ax.spines["bottom"].set_bounds(x_bounds)
    else:
        ax.spines["bottom"].set_visible(False)
    if y_bounds:
        ax.spines["left"].set_bounds(y_bounds)
    else:
        ax.spines["left"].set_visible(False)


def main():
    my_data = generate_data(2)
    width = 2.63
    plt.style.use("example.mplstyle")
    fig, axes = plt.subplots(
        2,
        1,
        figsize=(width, width / 1.5),
        dpi=300,
        layout="tight",
        sharex=True,
        sharey=True,
    )

    ax = axes[0]
    line_1 = plot_custom_colour(ax, my_data[0], my_data[1][:, 0])
    adjust_ticks(ax, my_data[0][::2], [min(my_data[1][:, 0]), 0, max(my_data[1][:, 0])])
    add_labels(ax, y_label="Series 1")
    remove_box(
        ax,
        x_bounds=[min(my_data[0]), max(my_data[0])],
        y_bounds=[min(my_data[1][:, 0]), max(my_data[1][:, 0])],
    )

    ax = axes[1]
    line_2 = plot_custom_colour(ax, my_data[0], my_data[1][:, 1])
    adjust_ticks(ax, my_data[0][::2], [min(my_data[1][:, 1]), 0, max(my_data[1][:, 1])])
    add_labels(ax, x_label="Time (s)", y_label="Series 2")
    remove_box(
        ax,
        x_bounds=[min(my_data[0]), max(my_data[0])],
        y_bounds=[min(my_data[1][:, 1]), max(my_data[1][:, 1])],
    )

    fig.supylabel("Voltage (V)", size=8)

    plt.savefig("line.tiff")
    plt.savefig("line.eps")
    plt.show()


if __name__ == "__main__":
    main()
