import argparse
import sys

from .logger import generate_logger
from .paeplot import PaePlot
from .pdeplot import PdePlot

LOGGER = generate_logger(__name__)


def cli() -> None:
    # make parser
    parser = argparse.ArgumentParser(
        description=(
            "Toolkit for boltz(Biomolecular interaction models) input and output files"
        )
    )

    # subcommands
    subparsers = parser.add_subparsers()

    # paeplot
    parser_paeplot = subparsers.add_parser("paeplot", help="paeplot mode")
    parser_paeplot.add_argument(
        "-i",
        "--input",
        help="Input directory containing the predicted models",
        type=str,
        required=True,
    )
    parser_paeplot.add_argument(
        "-o",
        "--output",
        help="Suffix of the output plot files, e.g. foo_pae.png",
        default="",
        type=str,
    )
    parser_paeplot.add_argument(
        "-c",
        "--cmap",
        help="Currently only 'bwr' and 'Greens_r' are supported",
        choices=["bwr", "Greens_r"],
        default="bwr",
        type=str,
    )
    parser_paeplot.add_argument(
        "-t", "--title", help="Title of the plot", default="", type=str
    )
    parser_paeplot.add_argument(
        "-a",
        "--all",
        help="Plot all PAEs. Default is to plot only the best PAE",
        action="store_true",
    )
    parser_paeplot.add_argument(
        "--dpi",
        help="DPI of the output plot. Default is 100. but 300 is recommeneded",
        default=100,
        type=int,
    )

    # pdeplot
    parser_pdeplot = subparsers.add_parser("pdeplot", help="pdeplot mode")
    parser_pdeplot.add_argument(
        "-i",
        "--input",
        help="Input directory containing the predicted models",
        type=str,
        required=True,
    )
    parser_pdeplot.add_argument(
        "-o",
        "--output",
        help="Suffix of the output plot files, e.g. foo_pde.png",
        default="",
        type=str,
    )
    parser_pdeplot.add_argument(
        "-c",
        "--cmap",
        help="Currently only 'bwr' and 'Greens_r' are supported",
        choices=["bwr", "Greens_r"],
        default="bwr",
        type=str,
    )
    parser_pdeplot.add_argument(
        "-t", "--title", help="Title of the plot", default="", type=str
    )
    parser_pdeplot.add_argument(
        "-a",
        "--all",
        help="Plot all pdes. Default is to plot only the best pde",
        action="store_true",
    )
    parser_pdeplot.add_argument(
        "--dpi",
        help="DPI of the output plot. Default is 100. but 300 is recommeneded",
        default=100,
        type=int,
    )

    args = parser.parse_args()

    if len(sys.argv) == 1:
        LOGGER.error(f"use {sys.argv[0]} --help")
        sys.exit(1)

    LOGGER.info(f"{sys.argv[1]} called")
    if sys.argv[1] == "paeplot":
        paeplot = PaePlot(args=args)
        paeplot.run()
    if sys.argv[1] == "pdeplot":
        pdeplot = PdePlot(args=args)
        pdeplot.run()

    LOGGER.info(f"{sys.argv[1]} finished")
