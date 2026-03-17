"""PujaTimer with step-by-step timing."""
from __future__ import annotations
import time
from ..models import Puja, PujaStep, TimerState


class PujaTimer:
    """Timer that guides through puja steps with timing."""

    def __init__(self, puja: Puja) -> None:
        self.puja = puja
        self.state = TimerState(
            puja_name=puja.name,
            total_steps=len(puja.steps),
        )
        self._step_start_time: float | None = None

    @property
    def current_step(self) -> PujaStep | None:
        """Get the current puja step."""
        if 0 <= self.state.current_step < len(self.puja.steps):
            return self.puja.steps[self.state.current_step]
        return None

    @property
    def is_complete(self) -> bool:
        """Check if all steps are complete."""
        return self.state.current_step >= len(self.puja.steps)

    @property
    def progress_percent(self) -> float:
        """Get completion percentage."""
        if not self.puja.steps:
            return 100.0
        return (self.state.current_step / len(self.puja.steps)) * 100.0

    def start(self) -> PujaStep | None:
        """Start the puja timer from the first step."""
        self.state.current_step = 0
        self.state.is_running = True
        self.state.elapsed_seconds = 0.0
        self._step_start_time = time.time()
        return self.current_step

    def next_step(self) -> PujaStep | None:
        """Move to the next step."""
        if self._step_start_time is not None:
            self.state.elapsed_seconds += time.time() - self._step_start_time
        self.state.current_step += 1
        if self.is_complete:
            self.state.is_running = False
            self._step_start_time = None
            return None
        self._step_start_time = time.time()
        return self.current_step

    def previous_step(self) -> PujaStep | None:
        """Go back to the previous step."""
        if self.state.current_step > 0:
            self.state.current_step -= 1
            self._step_start_time = time.time()
        return self.current_step

    def pause(self) -> None:
        """Pause the timer."""
        if self.state.is_running and self._step_start_time is not None:
            self.state.elapsed_seconds += time.time() - self._step_start_time
            self._step_start_time = None
        self.state.is_running = False

    def resume(self) -> None:
        """Resume the timer."""
        self.state.is_running = True
        self._step_start_time = time.time()

    def get_step_duration(self, step_index: int) -> float:
        """Get the recommended duration for a step in minutes."""
        if 0 <= step_index < len(self.puja.steps):
            return self.puja.steps[step_index].duration_minutes
        return 0.0

    def get_remaining_time(self) -> float:
        """Get estimated remaining time in minutes."""
        remaining = 0.0
        for i in range(self.state.current_step, len(self.puja.steps)):
            remaining += self.puja.steps[i].duration_minutes
        return remaining

    def get_elapsed_time(self) -> float:
        """Get elapsed time in minutes."""
        total = self.state.elapsed_seconds
        if self._step_start_time is not None and self.state.is_running:
            total += time.time() - self._step_start_time
        return total / 60.0

    def get_timeline(self) -> list[dict]:
        """Get a timeline of all steps with cumulative times."""
        timeline = []
        cumulative = 0.0
        for step in self.puja.steps:
            timeline.append({
                "step": step.name,
                "start_minute": cumulative,
                "duration": step.duration_minutes,
                "end_minute": cumulative + step.duration_minutes,
            })
            cumulative += step.duration_minutes
        return timeline
