"""Pydantic models for PujaGuide."""
from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Deity(str, Enum):
    GANESHA = "Ganesha"
    LAKSHMI = "Lakshmi"
    SARASWATI = "Saraswati"
    SHIVA = "Shiva"
    VISHNU = "Vishnu"
    DURGA = "Durga"
    HANUMAN = "Hanuman"
    RAMA = "Rama"
    KRISHNA = "Krishna"
    SURYA = "Surya"
    NAVAGRAHA = "Navagraha"
    SATYANARAYAN = "Satyanarayan"
    KARTIKEYA = "Kartikeya"
    PARVATI = "Parvati"
    KALI = "Kali"
    RADHA_KRISHNA = "Radha-Krishna"
    SITA_RAMA = "Sita-Rama"
    SHANI = "Shani"
    TULSI = "Tulsi"
    GAYATRI = "Gayatri"


class Mantra(BaseModel):
    sanskrit: str
    transliteration: str
    meaning: str
    repetitions: int = 1


class SamagriItem(BaseModel):
    name: str
    hindi_name: str = ""
    quantity: str = ""
    purpose: str = ""
    is_essential: bool = True


class PujaStep(BaseModel):
    order: int
    name: str
    description: str
    mantras: list[Mantra] = Field(default_factory=list)
    materials_needed: list[str] = Field(default_factory=list)
    duration_minutes: float = 5.0
    instructions: str = ""


class Puja(BaseModel):
    name: str
    deity: Deity
    description: str
    occasion: str = ""
    best_time: str = ""
    steps: list[PujaStep] = Field(default_factory=list)
    samagri: list[SamagriItem] = Field(default_factory=list)
    total_duration_minutes: float = 60.0
    difficulty: str = "medium"


class Festival(BaseModel):
    name: str
    month: str
    description: str
    associated_pujas: list[str] = Field(default_factory=list)
    tithi: str = ""
    significance: str = ""


class TimerState(BaseModel):
    puja_name: str
    current_step: int = 0
    elapsed_seconds: float = 0.0
    is_running: bool = False
    total_steps: int = 0
