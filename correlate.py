import pandas as pd
import click

@click.command()
@click.option('-b', '--base', type=float, nargs=3)
@click.option('-c', '--comparison', type=float, nargs=3)
def correlate(base, comparison):
    base_series = pd.Series(list(base))
    click.echo(base_series)
    comparison_series = pd.Series(list(comparison))
    click.echo(comparison_series)
    click.echo(base_series.corr(comparison_series))

if __name__ == '__main__':
    correlate()