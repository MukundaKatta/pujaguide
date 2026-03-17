"""Tests for PujaGuide."""
import pytest
from pujaguide.rituals.pujas import PujaDatabase
from pujaguide.rituals.mantras import MantraCollection
from pujaguide.rituals.materials import SamagriList
from pujaguide.guide.calendar import FestivalCalendar
from pujaguide.guide.timer import PujaTimer
from pujaguide.models import Deity


class TestPujaDatabase:
    def test_has_20_plus_pujas(self):
        db = PujaDatabase()
        assert len(db.get_all_pujas()) >= 20

    def test_get_puja_by_name(self):
        db = PujaDatabase()
        puja = db.get_puja("Ganesh Puja")
        assert puja is not None
        assert puja.deity == Deity.GANESHA

    def test_each_puja_has_steps(self):
        db = PujaDatabase()
        for puja in db.get_all_pujas():
            assert len(puja.steps) >= 3, f"{puja.name} has too few steps"

    def test_search_pujas(self):
        db = PujaDatabase()
        results = db.search_pujas("shiva")
        assert len(results) >= 1

    def test_pujas_by_deity(self):
        db = PujaDatabase()
        results = db.get_pujas_by_deity(Deity.KRISHNA)
        assert len(results) >= 1

    def test_pujas_by_difficulty(self):
        db = PujaDatabase()
        easy = db.get_pujas_by_difficulty("easy")
        assert len(easy) >= 1


class TestMantraCollection:
    def test_has_mantras(self):
        mc = MantraCollection()
        assert mc.get_mantra_count() > 20

    def test_get_ganesh_mantras(self):
        mc = MantraCollection()
        mantras = mc.get_mantras_for_step("ganesh_puja")
        assert len(mantras) >= 1
        assert "Ganapataye" in mantras[0].sanskrit

    def test_search_mantras(self):
        mc = MantraCollection()
        results = mc.search_mantras("Shiva")
        assert len(results) >= 1

    def test_all_step_keys(self):
        mc = MantraCollection()
        keys = mc.get_all_step_keys()
        assert "invocation" in keys
        assert "closing" in keys


class TestSamagriList:
    def test_common_items(self):
        sl = SamagriList()
        common = sl.get_common_items()
        assert len(common) >= 10

    def test_deity_specific_items(self):
        sl = SamagriList()
        ganesha_items = sl.get_puja_specific_items("Ganesha")
        assert any("Modak" in i.name for i in ganesha_items)

    def test_full_list(self):
        sl = SamagriList()
        full = sl.get_full_list("Shiva")
        assert len(full) > len(sl.get_common_items())

    def test_essential_items(self):
        sl = SamagriList()
        essential = sl.get_essential_items("Krishna")
        assert all(i.is_essential for i in essential)


class TestFestivalCalendar:
    def test_has_festivals(self):
        cal = FestivalCalendar()
        assert len(cal.get_all_festivals()) >= 25

    def test_diwali_exists(self):
        cal = FestivalCalendar()
        diwali = cal.get_festival_by_name("Diwali")
        assert diwali is not None
        assert "Lakshmi Puja" in diwali.associated_pujas

    def test_festivals_by_month(self):
        cal = FestivalCalendar()
        oct_fests = cal.get_festivals_by_month("October")
        assert len(oct_fests) >= 1

    def test_search_festivals(self):
        cal = FestivalCalendar()
        results = cal.search_festivals("harvest")
        assert len(results) >= 1


class TestPujaTimer:
    def test_timer_start(self):
        db = PujaDatabase()
        puja = db.get_puja("Ganesh Puja")
        timer = PujaTimer(puja)
        step = timer.start()
        assert step is not None
        assert timer.state.is_running

    def test_timer_next_step(self):
        db = PujaDatabase()
        puja = db.get_puja("Ganesh Puja")
        timer = PujaTimer(puja)
        timer.start()
        step2 = timer.next_step()
        assert step2 is not None
        assert timer.state.current_step == 1

    def test_timer_timeline(self):
        db = PujaDatabase()
        puja = db.get_puja("Ganesh Puja")
        timer = PujaTimer(puja)
        timeline = timer.get_timeline()
        assert len(timeline) == len(puja.steps)

    def test_timer_progress(self):
        db = PujaDatabase()
        puja = db.get_puja("Ganesh Puja")
        timer = PujaTimer(puja)
        timer.start()
        assert timer.progress_percent == 0.0
        timer.next_step()
        assert timer.progress_percent > 0.0
