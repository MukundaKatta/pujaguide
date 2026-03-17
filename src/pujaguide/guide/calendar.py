"""FestivalCalendar with Hindu festival dates and associated pujas."""
from __future__ import annotations
from ..models import Festival


class FestivalCalendar:
    """Calendar of Hindu festivals with associated pujas and tithis."""

    def __init__(self) -> None:
        self._festivals: list[Festival] = self._load_festivals()

    def _load_festivals(self) -> list[Festival]:
        return [
            Festival(name="Makar Sankranti", month="January", description="Sun enters Capricorn; harvest festival", associated_pujas=["Surya Puja"], tithi="Magha Krishna Pratipada", significance="Marks the beginning of Uttarayana, the northward journey of the Sun"),
            Festival(name="Vasant Panchami", month="January/February", description="Celebration of spring and Goddess Saraswati", associated_pujas=["Saraswati Puja"], tithi="Magha Shukla Panchami", significance="Worship of knowledge and arts; children start learning"),
            Festival(name="Maha Shivaratri", month="February/March", description="Great night of Lord Shiva", associated_pujas=["Shiva Puja"], tithi="Phalguna Krishna Chaturdashi", significance="Night-long worship of Shiva; fasting and Rudra Abhishek"),
            Festival(name="Holi", month="March", description="Festival of colors celebrating spring", associated_pujas=["Radha-Krishna Puja"], tithi="Phalguna Purnima", significance="Victory of good over evil; Holika Dahan on the eve"),
            Festival(name="Ugadi/Gudi Padwa", month="March/April", description="Hindu New Year in some traditions", associated_pujas=["Ganesh Puja", "Vishnu Puja"], tithi="Chaitra Shukla Pratipada", significance="Beginning of a new year; Panchanga Shravan"),
            Festival(name="Ram Navami", month="March/April", description="Birthday of Lord Rama", associated_pujas=["Rama Puja", "Sita-Rama Puja"], tithi="Chaitra Shukla Navami", significance="Birth of the seventh avatar of Vishnu"),
            Festival(name="Hanuman Jayanti", month="April", description="Birthday of Lord Hanuman", associated_pujas=["Hanuman Puja"], tithi="Chaitra Purnima", significance="Celebration of devotion and strength"),
            Festival(name="Akshaya Tritiya", month="April/May", description="Day of unending prosperity", associated_pujas=["Lakshmi Puja", "Vishnu Puja"], tithi="Vaishakha Shukla Tritiya", significance="Most auspicious day for new ventures and gold purchases"),
            Festival(name="Guru Purnima", month="July", description="Honoring spiritual teachers", associated_pujas=["Vishnu Puja"], tithi="Ashadha Purnima", significance="Worship of Vyasa and all gurus"),
            Festival(name="Nag Panchami", month="July/August", description="Worship of serpent deities", associated_pujas=["Shiva Puja"], tithi="Shravana Shukla Panchami", significance="Offering milk to snakes; worship of Naga devatas"),
            Festival(name="Raksha Bandhan", month="August", description="Bond of protection between siblings", associated_pujas=["Vishnu Puja"], tithi="Shravana Purnima", significance="Sisters tie rakhi on brothers' wrists"),
            Festival(name="Krishna Janmashtami", month="August", description="Birthday of Lord Krishna", associated_pujas=["Krishna Puja", "Radha-Krishna Puja"], tithi="Bhadrapada Krishna Ashtami", significance="Midnight celebration of Krishna's birth"),
            Festival(name="Ganesh Chaturthi", month="August/September", description="Birthday of Lord Ganesha", associated_pujas=["Ganesh Puja"], tithi="Bhadrapada Shukla Chaturthi", significance="10-day celebration ending with Ganesh Visarjan"),
            Festival(name="Hartalika Teej", month="August/September", description="Worship of Parvati and Shiva", associated_pujas=["Parvati Puja", "Shiva Puja"], tithi="Bhadrapada Shukla Tritiya", significance="Women's festival for marital bliss"),
            Festival(name="Navratri (Sharad)", month="September/October", description="Nine nights of Goddess worship", associated_pujas=["Navratri Puja", "Durga Puja"], tithi="Ashvina Shukla Pratipada to Navami", significance="Nine forms of Durga worshipped over nine nights"),
            Festival(name="Dussehra/Vijayadashami", month="October", description="Victory of good over evil", associated_pujas=["Durga Puja", "Rama Puja"], tithi="Ashvina Shukla Dashami", significance="Rama's victory over Ravana; Durga's victory over Mahishasura"),
            Festival(name="Sharad Purnima", month="October", description="Full moon of autumn", associated_pujas=["Lakshmi Puja", "Krishna Puja"], tithi="Ashvina Purnima", significance="Krishna's Ras Leela; Lakshmi worship"),
            Festival(name="Karva Chauth", month="October", description="Women fast for husbands' longevity", associated_pujas=["Shiva Puja", "Parvati Puja"], tithi="Kartika Krishna Chaturthi", significance="Day-long fast broken at moonrise"),
            Festival(name="Diwali", month="October/November", description="Festival of lights", associated_pujas=["Lakshmi Puja", "Ganesh Puja", "Kali Puja"], tithi="Kartika Amavasya", significance="Victory of light over darkness; Rama's return to Ayodhya"),
            Festival(name="Govardhan Puja", month="October/November", description="Krishna lifting Govardhan hill", associated_pujas=["Krishna Puja"], tithi="Kartika Shukla Pratipada", significance="Krishna protecting villagers from Indra's wrath"),
            Festival(name="Bhai Dooj", month="October/November", description="Celebration of sibling bond", associated_pujas=["Vishnu Puja"], tithi="Kartika Shukla Dwitiya", significance="Sisters pray for brothers' well-being"),
            Festival(name="Chhath Puja", month="October/November", description="Worship of the Sun God", associated_pujas=["Surya Puja"], tithi="Kartika Shukla Shashthi", significance="Four-day festival of sun worship; holy bathing"),
            Festival(name="Tulsi Vivah", month="November", description="Ceremonial marriage of Tulsi to Vishnu", associated_pujas=["Tulsi Puja", "Vishnu Puja"], tithi="Kartika Shukla Ekadashi to Purnima", significance="Marks the beginning of the wedding season"),
            Festival(name="Skanda Shashthi", month="November", description="Victory of Kartikeya over Soorapadman", associated_pujas=["Kartikeya Puja"], tithi="Kartika Shukla Shashthi", significance="Six-day worship of Murugan"),
            Festival(name="Gita Jayanti", month="December", description="Day the Bhagavad Gita was spoken", associated_pujas=["Krishna Puja", "Vishnu Puja"], tithi="Margashirsha Shukla Ekadashi", significance="Reading and reflection on the Gita"),
            Festival(name="Vaikuntha Ekadashi", month="December/January", description="Most sacred Ekadashi", associated_pujas=["Vishnu Puja"], tithi="Margashirsha Shukla Ekadashi", significance="Gates of Vaikuntha open; Vishnu worship"),
            Festival(name="Pongal", month="January", description="Tamil harvest festival", associated_pujas=["Surya Puja"], tithi="Thai month begins", significance="Four-day festival of thanksgiving to Sun and nature"),
            Festival(name="Maha Navami", month="September/October", description="Ninth day of Navratri", associated_pujas=["Durga Puja", "Navratri Puja"], tithi="Ashvina Shukla Navami", significance="Final worship before Vijayadashami; Kanya Pujan"),
            Festival(name="Shani Jayanti", month="May/June", description="Birthday of Lord Shani", associated_pujas=["Shani Puja", "Navagraha Puja"], tithi="Jyeshtha Amavasya", significance="Worship of Saturn for removal of Shani dosha"),
        ]

    def get_all_festivals(self) -> list[Festival]:
        """Get all festivals."""
        return self._festivals

    def get_festivals_by_month(self, month: str) -> list[Festival]:
        """Get festivals for a given month."""
        m = month.lower()
        return [f for f in self._festivals if m in f.month.lower()]

    def get_festival_by_name(self, name: str) -> Festival | None:
        """Find a festival by name."""
        name_lower = name.lower()
        for f in self._festivals:
            if name_lower in f.name.lower():
                return f
        return None

    def get_festivals_for_puja(self, puja_name: str) -> list[Festival]:
        """Get festivals associated with a specific puja."""
        return [f for f in self._festivals if puja_name in f.associated_pujas]

    def search_festivals(self, query: str) -> list[Festival]:
        """Search festivals by name, description, or significance."""
        q = query.lower()
        return [f for f in self._festivals if q in f.name.lower() or q in f.description.lower() or q in f.significance.lower()]
