"""Example of plotting slices of a 3D image."""

import nibabel as nib
import matplotlib.pyplot as plt


def load_image_data():
    return nib.load("resources/sub-control01_ses-01_dwi.nii.gz").get_fdata()


def std_fig():
    return plt.subplots(figsize=(2.63, 2.63), dpi=300)


def main():
    img_arr = load_image_data()

    _, ax = std_fig()
    ax.imshow(img_arr[:, :, 25, 0])
    plt.savefig("basic_img.png")
    plt.show()

    _, ax = std_fig()
    ax.imshow(img_arr[:, :, 25, 0], cmap="gray")
    plt.savefig("grayscale_img.png")
    plt.show()

    _, ax = std_fig()
    ax.imshow(img_arr[15:115, 15:115, 25, 0], cmap="gray")
    plt.savefig("cropped_img.png")
    plt.show()

    _, ax = std_fig()
    ax.imshow(img_arr[15:115, 15:115, 25, 0], cmap="gray")
    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
    )
    plt.savefig("noticks_img.png")
    plt.show()

    _, ax = std_fig()
    ax.imshow(img_arr[15:115, 15:115, 25, 0].T, cmap="gray", origin="lower")
    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
    )
    plt.savefig("las_img.png")
    plt.show()


if __name__ == "__main__":
    main()
