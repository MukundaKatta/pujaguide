"""Report generation for PujaGuide."""
from __future__ import annotations
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from .models import Puja, Festival


class PujaReport:
    """Generate rich console reports for pujas and festivals."""

    def __init__(self) -> None:
        self.console = Console()

    def display_puja(self, puja: Puja) -> None:
        """Display detailed puja information."""
        self.console.print(Panel(f"[bold magenta]{puja.name}[/bold magenta]\n{puja.description}",
                                  title="Puja Guide", subtitle=f"Deity: {puja.deity.value}"))
        self.console.print(f"[bold]Occasion:[/bold] {puja.occasion}")
        self.console.print(f"[bold]Best Time:[/bold] {puja.best_time}")
        self.console.print(f"[bold]Duration:[/bold] ~{puja.total_duration_minutes} minutes")
        self.console.print(f"[bold]Difficulty:[/bold] {puja.difficulty}\n")

        # Steps table
        table = Table(title="Puja Steps", show_lines=True)
        table.add_column("#", style="bold", width=4)
        table.add_column("Step", style="cyan", width=20)
        table.add_column("Description", width=30)
        table.add_column("Duration", width=10)
        table.add_column("Instructions", width=40)
        for step in puja.steps:
            table.add_row(str(step.order), step.name, step.description,
                         f"{step.duration_minutes} min", step.instructions)
        self.console.print(table)

    def display_samagri(self, puja: Puja) -> None:
        """Display materials list for a puja."""
        table = Table(title=f"Samagri for {puja.name}")
        table.add_column("Item", style="cyan")
        table.add_column("Hindi Name", style="yellow")
        table.add_column("Quantity", style="green")
        table.add_column("Purpose")
        table.add_column("Essential", style="bold")
        for item in puja.samagri:
            table.add_row(item.name, item.hindi_name, item.quantity, item.purpose,
                         "Yes" if item.is_essential else "No")
        self.console.print(table)

    def display_festival_calendar(self, festivals: list[Festival]) -> None:
        """Display festival calendar."""
        table = Table(title="Hindu Festival Calendar")
        table.add_column("Festival", style="bold magenta")
        table.add_column("Month", style="cyan")
        table.add_column("Tithi", style="yellow")
        table.add_column("Associated Pujas", style="green")
        for f in festivals:
            table.add_row(f.name, f.month, f.tithi, ", ".join(f.associated_pujas))
        self.console.print(table)

    def display_puja_list(self, pujas: list[Puja]) -> None:
        """Display a list of pujas."""
        table = Table(title="Available Pujas")
        table.add_column("Name", style="bold cyan")
        table.add_column("Deity", style="yellow")
        table.add_column("Duration", style="green")
        table.add_column("Difficulty")
        for p in pujas:
            table.add_row(p.name, p.deity.value, f"{p.total_duration_minutes} min", p.difficulty)
        self.console.print(table)
