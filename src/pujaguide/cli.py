"""CLI for PujaGuide."""
from __future__ import annotations
import click
from rich.console import Console
from .rituals.pujas import PujaDatabase
from .rituals.mantras import MantraCollection
from .rituals.materials import SamagriList
from .guide.calendar import FestivalCalendar
from .guide.timer import PujaTimer
from .report import PujaReport

console = Console()


@click.group()
def cli() -> None:
    """PujaGuide - AI Hindu Ritual Guide."""
    pass


@cli.command()
def list_pujas() -> None:
    """List all available pujas."""
    db = PujaDatabase()
    report = PujaReport()
    report.display_puja_list(db.get_all_pujas())


@cli.command()
@click.argument("name")
def show_puja(name: str) -> None:
    """Show detailed puja steps and instructions."""
    db = PujaDatabase()
    report = PujaReport()
    results = db.search_pujas(name)
    if results:
        report.display_puja(results[0])
    else:
        console.print(f"[red]Puja not found: {name}[/red]")


@cli.command()
@click.argument("name")
def samagri(name: str) -> None:
    """Show materials list for a puja."""
    db = PujaDatabase()
    report = PujaReport()
    results = db.search_pujas(name)
    if results:
        report.display_samagri(results[0])
    else:
        console.print(f"[red]Puja not found: {name}[/red]")


@cli.command()
@click.option("--month", "-m", default=None, help="Filter by month")
def festivals(month: str | None) -> None:
    """Show Hindu festival calendar."""
    cal = FestivalCalendar()
    report = PujaReport()
    if month:
        fests = cal.get_festivals_by_month(month)
    else:
        fests = cal.get_all_festivals()
    report.display_festival_calendar(fests)


@cli.command()
@click.argument("query")
def search_mantras(query: str) -> None:
    """Search mantras by text."""
    mc = MantraCollection()
    results = mc.search_mantras(query)
    if results:
        for m in results:
            console.print(f"[bold yellow]{m.sanskrit}[/bold yellow]")
            console.print(f"  Transliteration: {m.transliteration}")
            console.print(f"  Meaning: {m.meaning}")
            console.print(f"  Repetitions: {m.repetitions}\n")
    else:
        console.print(f"[red]No mantras found for: {query}[/red]")


@cli.command()
@click.argument("name")
def timer(name: str) -> None:
    """Show puja timeline with step durations."""
    db = PujaDatabase()
    results = db.search_pujas(name)
    if not results:
        console.print(f"[red]Puja not found: {name}[/red]")
        return
    t = PujaTimer(results[0])
    timeline = t.get_timeline()
    from rich.table import Table
    table = Table(title=f"Timeline: {results[0].name}")
    table.add_column("Step", style="cyan")
    table.add_column("Start", style="green")
    table.add_column("Duration", style="yellow")
    table.add_column("End", style="green")
    for entry in timeline:
        table.add_row(entry["step"], f"{entry['start_minute']:.0f} min",
                     f"{entry['duration']:.0f} min", f"{entry['end_minute']:.0f} min")
    console.print(table)


if __name__ == "__main__":
    cli()
