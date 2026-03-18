"""Tests for Pujaguide."""
from src.core import Pujaguide
def test_init(): assert Pujaguide().get_stats()["ops"] == 0
def test_op(): c = Pujaguide(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Pujaguide(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Pujaguide(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Pujaguide(); r = c.process(); assert r["service"] == "pujaguide"
