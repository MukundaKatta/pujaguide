"""MantraCollection with correct Sanskrit mantras per puja step."""
from __future__ import annotations
from ..models import Mantra


class MantraCollection:
    """Database of Sanskrit mantras organized by puja step and deity."""

    def __init__(self) -> None:
        self._mantras: dict[str, list[Mantra]] = self._load_mantras()

    def _load_mantras(self) -> dict[str, list[Mantra]]:
        return {
            "invocation": [
                Mantra(
                    sanskrit="Om Gam Ganapataye Namaha",
                    transliteration="Om Gam Ga-na-pa-ta-ye Na-ma-ha",
                    meaning="Salutations to Lord Ganesha, remover of obstacles",
                    repetitions=3,
                ),
                Mantra(
                    sanskrit="Om Shri Ganeshaya Namaha",
                    transliteration="Om Shree Ga-ne-shaa-ya Na-ma-ha",
                    meaning="I bow to Lord Ganesha",
                    repetitions=3,
                ),
            ],
            "kalash_sthapana": [
                Mantra(
                    sanskrit="Om Varunaya Namaha",
                    transliteration="Om Va-ru-naa-ya Na-ma-ha",
                    meaning="Salutations to the lord of waters",
                    repetitions=1,
                ),
            ],
            "ganesh_puja": [
                Mantra(
                    sanskrit="Om Gam Ganapataye Namaha",
                    transliteration="Om Gam Ga-na-pa-ta-ye Na-ma-ha",
                    meaning="Salutations to Lord Ganesha",
                    repetitions=108,
                ),
                Mantra(
                    sanskrit="Vakratunda Mahakaya Surya Koti Samaprabha Nirvighnam Kuru Me Deva Sarva Karyeshu Sarvada",
                    transliteration="Vak-ra-tun-da Ma-haa-kaa-ya Sur-ya Ko-ti Sa-ma-pra-bha Nir-vigh-nam Ku-ru Me De-va Sar-va Kaar-ye-shu Sar-va-daa",
                    meaning="O Lord with curved trunk and massive body, whose brilliance equals a billion suns, please make all my works free of obstacles, always",
                    repetitions=1,
                ),
            ],
            "lakshmi_puja": [
                Mantra(
                    sanskrit="Om Shreem Mahalakshmiyei Namaha",
                    transliteration="Om Shreem Ma-haa-lak-shmee-yei Na-ma-ha",
                    meaning="Salutations to Goddess Mahalakshmi",
                    repetitions=108,
                ),
                Mantra(
                    sanskrit="Om Hreem Shreem Kleem Mahalakshmiyei Namaha",
                    transliteration="Om Hreem Shreem Kleem Ma-haa-lak-shmee-yei Na-ma-ha",
                    meaning="Powerful invocation to Goddess Lakshmi for wealth and prosperity",
                    repetitions=21,
                ),
            ],
            "saraswati_puja": [
                Mantra(
                    sanskrit="Om Aim Saraswatyai Namaha",
                    transliteration="Om Aim Sa-ras-wa-tyai Na-ma-ha",
                    meaning="Salutations to Goddess Saraswati",
                    repetitions=108,
                ),
                Mantra(
                    sanskrit="Saraswati Namastubhyam Varade Kamarupini Vidyarambham Karishyami Siddhir Bhavatu Me Sada",
                    transliteration="Sa-ras-wa-ti Na-mas-tub-hyam Va-ra-de Kaa-ma-roo-pi-ni Vid-yaa-ram-bham Ka-rish-yaa-mi Sid-dhir Bha-va-tu Me Sa-daa",
                    meaning="O Saraswati, salutations to you, the giver of boons, as I begin my studies, may success always be mine",
                    repetitions=1,
                ),
            ],
            "shiva_puja": [
                Mantra(
                    sanskrit="Om Namah Shivaya",
                    transliteration="Om Na-mah Shi-vaa-ya",
                    meaning="I bow to Lord Shiva",
                    repetitions=108,
                ),
                Mantra(
                    sanskrit="Karpur Gauram Karunavataram Sansara Saram Bhujagendra Haram",
                    transliteration="Kar-pur Gau-ram Ka-ru-naa-va-taa-ram San-saa-ra Saa-ram Bhu-ja-gen-dra Haa-ram",
                    meaning="White as camphor, the incarnation of compassion, the essence of worldly existence, wearing the king of serpents as garland",
                    repetitions=1,
                ),
            ],
            "vishnu_puja": [
                Mantra(
                    sanskrit="Om Namo Bhagavate Vasudevaya",
                    transliteration="Om Na-mo Bha-ga-va-te Vaa-su-de-vaa-ya",
                    meaning="Salutations to Lord Vasudeva (Vishnu)",
                    repetitions=108,
                ),
                Mantra(
                    sanskrit="Shantakaram Bhujagashayanam Padmanabham Suresham",
                    transliteration="Shaan-taa-kaa-ram Bhu-ja-ga-sha-ya-nam Pad-ma-naa-bham Su-re-sham",
                    meaning="The one with peaceful form, reclining on the serpent, with lotus in the navel, lord of gods",
                    repetitions=1,
                ),
            ],
            "durga_puja": [
                Mantra(
                    sanskrit="Om Dum Durgayei Namaha",
                    transliteration="Om Dum Dur-gaa-yei Na-ma-ha",
                    meaning="Salutations to Goddess Durga",
                    repetitions=108,
                ),
                Mantra(
                    sanskrit="Sarva Mangala Mangalye Shive Sarvartha Sadhike Sharanye Tryambake Gauri Narayani Namostute",
                    transliteration="Sar-va Man-ga-la Maan-gal-ye Shi-ve Sar-vaar-tha Saa-dhi-ke Sha-ran-ye Tryam-ba-ke Gau-ri Naa-raa-ya-ni Na-mos-tu-te",
                    meaning="O auspicious one, who bestows auspiciousness, who fulfills all purposes, I bow to you Narayani",
                    repetitions=3,
                ),
            ],
            "navagraha_puja": [
                Mantra(
                    sanskrit="Om Suryaya Namaha",
                    transliteration="Om Sur-yaa-ya Na-ma-ha",
                    meaning="Salutations to the Sun",
                    repetitions=7,
                ),
                Mantra(
                    sanskrit="Om Chandraya Namaha",
                    transliteration="Om Chan-draa-ya Na-ma-ha",
                    meaning="Salutations to the Moon",
                    repetitions=11,
                ),
                Mantra(
                    sanskrit="Om Mangalaya Namaha",
                    transliteration="Om Man-ga-laa-ya Na-ma-ha",
                    meaning="Salutations to Mars",
                    repetitions=10,
                ),
                Mantra(
                    sanskrit="Om Budhaya Namaha",
                    transliteration="Om Bud-haa-ya Na-ma-ha",
                    meaning="Salutations to Mercury",
                    repetitions=9,
                ),
                Mantra(
                    sanskrit="Om Gurave Namaha",
                    transliteration="Om Gu-ra-ve Na-ma-ha",
                    meaning="Salutations to Jupiter",
                    repetitions=19,
                ),
                Mantra(
                    sanskrit="Om Shukraya Namaha",
                    transliteration="Om Shuk-raa-ya Na-ma-ha",
                    meaning="Salutations to Venus",
                    repetitions=16,
                ),
                Mantra(
                    sanskrit="Om Shanaye Namaha",
                    transliteration="Om Sha-nai-ye Na-ma-ha",
                    meaning="Salutations to Saturn",
                    repetitions=23,
                ),
                Mantra(
                    sanskrit="Om Rahave Namaha",
                    transliteration="Om Raa-ha-ve Na-ma-ha",
                    meaning="Salutations to Rahu",
                    repetitions=18,
                ),
                Mantra(
                    sanskrit="Om Ketave Namaha",
                    transliteration="Om Ke-ta-ve Na-ma-ha",
                    meaning="Salutations to Ketu",
                    repetitions=7,
                ),
            ],
            "satyanarayan_puja": [
                Mantra(
                    sanskrit="Om Namo Bhagavate Vasudevaya",
                    transliteration="Om Na-mo Bha-ga-va-te Vaa-su-de-vaa-ya",
                    meaning="Salutations to Lord Vasudeva",
                    repetitions=108,
                ),
            ],
            "dhyana": [
                Mantra(
                    sanskrit="Om",
                    transliteration="Aum",
                    meaning="The primordial sound, essence of ultimate reality",
                    repetitions=21,
                ),
            ],
            "aarti": [
                Mantra(
                    sanskrit="Om Jai Jagdish Hare Swami Jai Jagdish Hare",
                    transliteration="Om Jai Jag-dish Ha-re Swaa-mi Jai Jag-dish Ha-re",
                    meaning="Victory to the Lord of the Universe",
                    repetitions=1,
                ),
            ],
            "gayatri": [
                Mantra(
                    sanskrit="Om Bhur Bhuva Svaha Tat Savitur Varenyam Bhargo Devasya Dhimahi Dhiyo Yo Nah Prachodayat",
                    transliteration="Om Bhur Bhu-vah Sva-ha Tat Sa-vi-tur Va-ren-yam Bhar-go De-vas-ya Dhi-ma-hi Dhi-yo Yo Nah Pra-cho-da-yaat",
                    meaning="We meditate on the glory of the Creator who has created the Universe, who is worthy of worship, the remover of all sins and ignorance. May he enlighten our intellect.",
                    repetitions=108,
                ),
            ],
            "hanuman_puja": [
                Mantra(
                    sanskrit="Om Hanumate Namaha",
                    transliteration="Om Ha-nu-ma-te Na-ma-ha",
                    meaning="Salutations to Lord Hanuman",
                    repetitions=108,
                ),
            ],
            "krishna_puja": [
                Mantra(
                    sanskrit="Om Kleem Krishnaya Namaha",
                    transliteration="Om Kleem Krish-naa-ya Na-ma-ha",
                    meaning="Salutations to Lord Krishna",
                    repetitions=108,
                ),
                Mantra(
                    sanskrit="Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Rama Hare Rama Rama Rama Hare Hare",
                    transliteration="Ha-re Krish-na Ha-re Krish-na Krish-na Krish-na Ha-re Ha-re Ha-re Raa-ma Ha-re Raa-ma Raa-ma Raa-ma Ha-re Ha-re",
                    meaning="The Maha Mantra - invocation of the divine names of the Lord",
                    repetitions=108,
                ),
            ],
            "rama_puja": [
                Mantra(
                    sanskrit="Om Shri Ramaya Namaha",
                    transliteration="Om Shree Raa-maa-ya Na-ma-ha",
                    meaning="Salutations to Lord Rama",
                    repetitions=108,
                ),
            ],
            "kali_puja": [
                Mantra(
                    sanskrit="Om Kreem Kalikayei Namaha",
                    transliteration="Om Kreem Kaa-li-kaa-yei Na-ma-ha",
                    meaning="Salutations to Goddess Kali",
                    repetitions=108,
                ),
            ],
            "closing": [
                Mantra(
                    sanskrit="Om Shanti Shanti Shanti",
                    transliteration="Om Shaan-ti Shaan-ti Shaan-ti",
                    meaning="Om Peace Peace Peace",
                    repetitions=3,
                ),
                Mantra(
                    sanskrit="Karpura Gauram Karunavataram Sansara Saram Bhujagendra Haram Sada Vasantam Hridayaravinde Bhavam Bhavani Sahitam Namami",
                    transliteration="Kar-poo-ra Gau-ram Ka-ru-naa-va-taa-ram San-saa-ra Saa-ram Bhu-ja-gen-dra Haa-ram Sa-daa Va-san-tam Hri-da-yaa-ra-vin-de Bha-vam Bha-vaa-ni Sa-hi-tam Na-maa-mi",
                    meaning="I bow to Lord Shiva who is white as camphor, incarnation of compassion, essence of creation, adorned with serpent king, always dwelling in the lotus of the heart, along with Goddess Bhavani",
                    repetitions=1,
                ),
            ],
        }

    def get_mantras_for_step(self, step_key: str) -> list[Mantra]:
        """Get mantras for a specific puja step."""
        return self._mantras.get(step_key, [])

    def get_all_step_keys(self) -> list[str]:
        """Get all available step keys."""
        return list(self._mantras.keys())

    def search_mantras(self, query: str) -> list[Mantra]:
        """Search mantras by text content."""
        query_lower = query.lower()
        results = []
        for mantras in self._mantras.values():
            for m in mantras:
                if query_lower in m.sanskrit.lower() or query_lower in m.meaning.lower():
                    results.append(m)
        return results

    def get_mantra_count(self) -> int:
        """Total number of mantras in the collection."""
        return sum(len(v) for v in self._mantras.values())
