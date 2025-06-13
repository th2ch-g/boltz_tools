from argparse import ArgumentParser
from pathlib import Path

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from .logger import generate_logger

matplotlib.use("Agg")


LOGGER = generate_logger(__name__)


class PaePlot:
    args: ArgumentParser

    def __init__(self, args):
        self.args = args

    def plot_all_paes(self):
        for input_file in Path(f"{self.args.input}/predictions/").glob("*"):
            for pae_npz in Path(f"{input_file}/").glob("pae_*_model_*.npz"):
                LOGGER.info(f"Plotting {pae_npz}")
                self.plot_pae(pae_npz)

    def plot_best_pae(self):
        for input_file in Path(f"{self.args.input}/predictions/").glob("*"):
            for pae_npz in Path(f"{input_file}/").glob("pae_*_model_0.npz"):
                LOGGER.info(f"Plotting {pae_npz}")
                self.plot_pae(pae_npz)

    def plot_pae(self, pae_npz):
        with np.load(pae_npz) as data:
            plt.figure(figsize=(8, 6))
            im = plt.imshow(data["pae"], cmap=self.args.cmap, interpolation="nearest")
            plt.colorbar(im, label="Predicted Aligned Error [Å]")
            plt.xlabel("Residue Index")
            plt.ylabel("Residue Index")
            plt.title(f"{self.args.title}")
            plt.tight_layout()
            plt.savefig(
                f"{pae_npz.parent}/{pae_npz.stem}{self.args.output}.png",
                dpi=self.args.dpi,
            )
            LOGGER.info(f"Saved {pae_npz.parent}/{pae_npz.stem}{self.args.output}.png")
            plt.clf()
            plt.close()

    def run(self):
        LOGGER.info(f"{self.args=}")

        if not Path(self.args.input).is_dir():
            FileNotFoundError(f"{self.args.input} is not a directory")

        if self.args.all:
            self.plot_all_paes()
        else:
            self.plot_best_pae()
