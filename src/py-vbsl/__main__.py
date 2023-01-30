"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Variational Bayes Synthetic Likelihood."""


if __name__ == "__main__":
    main(prog_name="Variational-Bayes-Synthetic-Likelihood")  # pragma: no cover
