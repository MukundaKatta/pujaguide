"""SamagriList with required items per puja."""
from __future__ import annotations
from ..models import SamagriItem, Deity


class SamagriList:
    """Database of puja materials (samagri) required for each type of puja."""

    def __init__(self) -> None:
        self._common_items = self._load_common_items()
        self._puja_specific: dict[str, list[SamagriItem]] = self._load_specific_items()

    def _load_common_items(self) -> list[SamagriItem]:
        return [
            SamagriItem(name="Incense sticks", hindi_name="Agarbatti", quantity="1 packet", purpose="Fragrance offering"),
            SamagriItem(name="Camphor", hindi_name="Kapoor", quantity="5-10 pieces", purpose="Aarti"),
            SamagriItem(name="Ghee lamp", hindi_name="Diya", quantity="1-2", purpose="Light offering"),
            SamagriItem(name="Cotton wicks", hindi_name="Batti", quantity="5-10", purpose="For diya"),
            SamagriItem(name="Flowers", hindi_name="Phool", quantity="As needed", purpose="Pushpanjali"),
            SamagriItem(name="Turmeric powder", hindi_name="Haldi", quantity="1 tbsp", purpose="Tilak and decoration"),
            SamagriItem(name="Kumkum", hindi_name="Kumkum", quantity="1 pinch", purpose="Tilak"),
            SamagriItem(name="Rice grains", hindi_name="Akshata/Chawal", quantity="1 cup", purpose="Offering"),
            SamagriItem(name="Sandalwood paste", hindi_name="Chandan", quantity="Small amount", purpose="Tilak"),
            SamagriItem(name="Betel leaves", hindi_name="Paan ke patte", quantity="5-7", purpose="Offering"),
            SamagriItem(name="Betel nuts", hindi_name="Supari", quantity="2-5", purpose="Offering"),
            SamagriItem(name="Coconut", hindi_name="Nariyal", quantity="1", purpose="Main offering"),
            SamagriItem(name="Fruits", hindi_name="Phal", quantity="5 types", purpose="Naivedya"),
            SamagriItem(name="Sweets", hindi_name="Mithai/Prasad", quantity="As desired", purpose="Prasad"),
            SamagriItem(name="Holy water", hindi_name="Gangajal", quantity="Small bottle", purpose="Purification"),
            SamagriItem(name="Red thread", hindi_name="Mauli/Kalava", quantity="1 roll", purpose="Sacred thread"),
        ]

    def _load_specific_items(self) -> dict[str, list[SamagriItem]]:
        return {
            "Ganesha": [
                SamagriItem(name="Modak", hindi_name="Modak", quantity="21 pieces", purpose="Ganesha's favorite sweet"),
                SamagriItem(name="Durva grass", hindi_name="Doob/Durva", quantity="21 blades", purpose="Sacred to Ganesha"),
                SamagriItem(name="Red flowers", hindi_name="Lal phool", quantity="21", purpose="Offering to Ganesha"),
                SamagriItem(name="Shami leaves", hindi_name="Shami patra", quantity="5", purpose="Sacred leaves"),
            ],
            "Lakshmi": [
                SamagriItem(name="Lotus flowers", hindi_name="Kamal", quantity="5-7", purpose="Sacred to Lakshmi"),
                SamagriItem(name="Gold/silver coins", hindi_name="Sikke", quantity="A few", purpose="Wealth symbol"),
                SamagriItem(name="Red cloth", hindi_name="Lal kapda", quantity="1 piece", purpose="For deity"),
                SamagriItem(name="Kheel Batasha", hindi_name="Kheel Batasha", quantity="1 packet", purpose="Traditional prasad"),
            ],
            "Saraswati": [
                SamagriItem(name="White flowers", hindi_name="Safed phool", quantity="11", purpose="Sacred to Saraswati"),
                SamagriItem(name="Books/instruments", hindi_name="Pustak/Veena", quantity="As available", purpose="Knowledge symbols"),
                SamagriItem(name="White cloth", hindi_name="Safed kapda", quantity="1 piece", purpose="For deity"),
                SamagriItem(name="Ink and pen", hindi_name="Syahi aur kalam", quantity="1 set", purpose="Vidya symbol"),
            ],
            "Shiva": [
                SamagriItem(name="Bilva leaves", hindi_name="Bel patra", quantity="108", purpose="Most sacred to Shiva"),
                SamagriItem(name="Milk", hindi_name="Doodh", quantity="1 liter", purpose="Abhishek"),
                SamagriItem(name="Honey", hindi_name="Shahad", quantity="100ml", purpose="Abhishek"),
                SamagriItem(name="Datura flowers", hindi_name="Dhattura", quantity="5", purpose="Sacred to Shiva"),
                SamagriItem(name="Bhang", hindi_name="Bhang", quantity="Small amount", purpose="Shiva offering"),
                SamagriItem(name="White flowers", hindi_name="Safed phool", quantity="11", purpose="Offering"),
            ],
            "Vishnu": [
                SamagriItem(name="Tulsi leaves", hindi_name="Tulsi patra", quantity="21", purpose="Most sacred to Vishnu"),
                SamagriItem(name="Yellow flowers", hindi_name="Peele phool", quantity="11", purpose="Offering to Vishnu"),
                SamagriItem(name="Yellow cloth", hindi_name="Peela kapda", quantity="1 piece", purpose="For deity"),
                SamagriItem(name="Panchamrit", hindi_name="Panchamrit", quantity="1 bowl", purpose="Five nectars"),
            ],
            "Durga": [
                SamagriItem(name="Red flowers", hindi_name="Lal phool", quantity="21", purpose="Sacred to Durga"),
                SamagriItem(name="Red cloth", hindi_name="Lal kapda", quantity="1", purpose="For deity"),
                SamagriItem(name="Sindoor", hindi_name="Sindoor", quantity="1 packet", purpose="Offering"),
                SamagriItem(name="Lemon", hindi_name="Nimbu", quantity="1", purpose="For aarti"),
            ],
            "Navagraha": [
                SamagriItem(name="Nine grains", hindi_name="Navadhanya", quantity="9 types", purpose="One for each planet"),
                SamagriItem(name="Nine colored cloths", hindi_name="Nav rang ke kapde", quantity="9", purpose="For each graha"),
                SamagriItem(name="Black sesame seeds", hindi_name="Kale til", quantity="100g", purpose="For Shani"),
            ],
            "Satyanarayan": [
                SamagriItem(name="Wheat flour", hindi_name="Atta", quantity="250g", purpose="For prasad"),
                SamagriItem(name="Sugar", hindi_name="Cheeni", quantity="200g", purpose="For prasad"),
                SamagriItem(name="Banana", hindi_name="Kela", quantity="5", purpose="For prasad"),
                SamagriItem(name="Satyanarayan Katha book", hindi_name="Katha Pustak", quantity="1", purpose="Reading the story"),
            ],
            "Hanuman": [
                SamagriItem(name="Sindoor", hindi_name="Sindoor", quantity="1 packet", purpose="Hanuman offering"),
                SamagriItem(name="Jasmine oil", hindi_name="Chameli tel", quantity="Small bottle", purpose="Oil offering"),
                SamagriItem(name="Laddoo", hindi_name="Boondi ke laddoo", quantity="5", purpose="Prasad"),
            ],
            "Krishna": [
                SamagriItem(name="Butter", hindi_name="Makhan", quantity="100g", purpose="Krishna's favorite"),
                SamagriItem(name="Tulsi leaves", hindi_name="Tulsi patra", quantity="21", purpose="Sacred offering"),
                SamagriItem(name="Peacock feather", hindi_name="Mor pankh", quantity="1", purpose="Decoration"),
                SamagriItem(name="Flute", hindi_name="Bansuri", quantity="1", purpose="Symbol", is_essential=False),
            ],
        }

    def get_common_items(self) -> list[SamagriItem]:
        """Get items needed for any puja."""
        return self._common_items

    def get_puja_specific_items(self, deity_name: str) -> list[SamagriItem]:
        """Get items specific to a deity's puja."""
        return self._puja_specific.get(deity_name, [])

    def get_full_list(self, deity_name: str) -> list[SamagriItem]:
        """Get complete samagri list for a puja (common + specific)."""
        return self._common_items + self.get_puja_specific_items(deity_name)

    def get_essential_items(self, deity_name: str) -> list[SamagriItem]:
        """Get only essential items for a puja."""
        return [item for item in self.get_full_list(deity_name) if item.is_essential]
