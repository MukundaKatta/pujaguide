"""PujaDatabase with 20+ pujas with step-by-step instructions."""
from __future__ import annotations
from ..models import Puja, PujaStep, Deity, Mantra, SamagriItem
from .mantras import MantraCollection
from .materials import SamagriList


class PujaDatabase:
    """Database of 20+ Hindu pujas with complete step-by-step instructions."""

    def __init__(self) -> None:
        self._mantras = MantraCollection()
        self._materials = SamagriList()
        self._pujas: dict[str, Puja] = self._load_pujas()

    def _common_opening_steps(self) -> list[PujaStep]:
        return [
            PujaStep(order=1, name="Achaman", description="Purification by sipping water three times",
                     mantras=[Mantra(sanskrit="Om Achyutaya Namaha, Om Anantaya Namaha, Om Govindaya Namaha",
                                     transliteration="Om A-chyu-taa-ya Na-ma-ha...", meaning="Salutations to the imperishable, infinite, and Govinda", repetitions=1)],
                     duration_minutes=2, instructions="Take water in right palm and sip three times, reciting each name once."),
            PujaStep(order=2, name="Sankalpa", description="Declaration of intent for the puja",
                     duration_minutes=3, instructions="Hold water, rice and flower in right hand. State your name, gotra, the puja name, date, and your wish. Release into plate."),
            PujaStep(order=3, name="Ganapati Smarana", description="Invoke Lord Ganesha to remove obstacles",
                     mantras=self._mantras.get_mantras_for_step("invocation"), duration_minutes=3,
                     instructions="Offer durva grass and modak to Ganesha image. Chant the mantra 3 times."),
        ]

    def _common_closing_steps(self, base_order: int) -> list[PujaStep]:
        return [
            PujaStep(order=base_order, name="Aarti", description="Waving of lamp before the deity",
                     mantras=self._mantras.get_mantras_for_step("aarti"), duration_minutes=5,
                     instructions="Light camphor on aarti plate. Wave clockwise in front of deity. Ring bell with left hand."),
            PujaStep(order=base_order + 1, name="Pushpanjali", description="Offering flowers with folded hands",
                     duration_minutes=2, instructions="Take flowers in both hands, fold hands and offer while bowing head."),
            PujaStep(order=base_order + 2, name="Pradakshina", description="Circumambulation of the deity",
                     duration_minutes=2, instructions="Walk clockwise around the deity or turn in place 3 times."),
            PujaStep(order=base_order + 3, name="Prarthana & Kshama", description="Final prayer and apology for errors",
                     mantras=self._mantras.get_mantras_for_step("closing"), duration_minutes=3,
                     instructions="Pray for blessings. Ask forgiveness for any errors in the puja. Distribute prasad."),
        ]

    def _load_pujas(self) -> dict[str, Puja]:
        pujas = {}

        # 1. Ganesh Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Ganesh Dhyana", description="Meditation on Lord Ganesha's form",
                     mantras=[Mantra(sanskrit="Ekadantam Mahakayam Lambodaram Gajananam", transliteration="E-ka-dan-tam...", meaning="One-tusked, mighty-bodied, large-bellied, elephant-faced", repetitions=1)],
                     duration_minutes=5, instructions="Close eyes and visualize Ganesha seated on lotus throne."),
            PujaStep(order=5, name="Shodashopachara", description="16-step worship of Ganesha",
                     mantras=self._mantras.get_mantras_for_step("ganesh_puja"), duration_minutes=15,
                     instructions="Offer padya (water for feet), arghya (water for hands), achamana, snana, vastra, yagnopavita, gandha, pushpa, dhupa, deepa, naivedya one by one."),
            PujaStep(order=6, name="Durva & Modak Offering", description="Offer 21 durva blades and modak",
                     duration_minutes=5, instructions="Place 21 blades of durva grass near Ganesha. Offer 21 modaks."),
            PujaStep(order=7, name="Ganesh Atharvashirsha", description="Recitation of Ganapati Atharvashirsha",
                     duration_minutes=10, instructions="Recite the Atharvashirsha hymn dedicated to Ganesha."),
        ] + self._common_closing_steps(8)
        pujas["Ganesh Puja"] = Puja(name="Ganesh Puja", deity=Deity.GANESHA, description="Worship of Lord Ganesha, remover of obstacles", occasion="Ganesh Chaturthi, beginning of any new venture", best_time="Morning, Chaturthi tithi", steps=steps, samagri=self._materials.get_full_list("Ganesha"), total_duration_minutes=55, difficulty="easy")

        # 2. Lakshmi Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Kalash Sthapana", description="Establish sacred water pot",
                     mantras=self._mantras.get_mantras_for_step("kalash_sthapana"), duration_minutes=5, instructions="Fill copper pot with water, mango leaves, coconut on top. Place on rice bed."),
            PujaStep(order=5, name="Lakshmi Avahana", description="Invoke Goddess Lakshmi",
                     mantras=self._mantras.get_mantras_for_step("lakshmi_puja"), duration_minutes=10, instructions="Place Lakshmi idol/image on red cloth with coins. Offer lotus flowers."),
            PujaStep(order=6, name="Shodashopachara", description="16-step worship", duration_minutes=15, instructions="Perform the 16 steps of worship with each offering."),
            PujaStep(order=7, name="Lakshmi Ashtottara", description="108 names of Lakshmi", duration_minutes=10, instructions="Recite 108 names offering a flower or akshata with each name."),
        ] + self._common_closing_steps(8)
        pujas["Lakshmi Puja"] = Puja(name="Lakshmi Puja", deity=Deity.LAKSHMI, description="Worship of Goddess Lakshmi for wealth and prosperity", occasion="Diwali, Fridays, Sharad Purnima", best_time="Evening/Night, especially on Diwali", steps=steps, samagri=self._materials.get_full_list("Lakshmi"), total_duration_minutes=60, difficulty="medium")

        # 3. Saraswati Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Saraswati Avahana", description="Invoke Goddess Saraswati",
                     mantras=self._mantras.get_mantras_for_step("saraswati_puja"), duration_minutes=10, instructions="Place books and instruments near the idol. Offer white flowers."),
            PujaStep(order=5, name="Akshar Abhyasam", description="Writing practice as offering",
                     duration_minutes=5, instructions="Write Om on a slate or paper with new pen as symbolic initiation."),
            PujaStep(order=6, name="Shodashopachara", description="16-step worship", duration_minutes=15, instructions="Offer padya, arghya, vastra, gandha, pushpa, etc."),
        ] + self._common_closing_steps(7)
        pujas["Saraswati Puja"] = Puja(name="Saraswati Puja", deity=Deity.SARASWATI, description="Worship of Goddess Saraswati for knowledge and wisdom", occasion="Vasant Panchami, Navaratri (5th day)", best_time="Morning", steps=steps, samagri=self._materials.get_full_list("Saraswati"), total_duration_minutes=50, difficulty="easy")

        # 4. Shiva Puja (Rudrabhishek)
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Shivalinga Abhishek", description="Sacred bathing of Shivalinga",
                     duration_minutes=15, instructions="Pour milk, yogurt, honey, ghee, and gangajal over Shivalinga while chanting Om Namah Shivaya."),
            PujaStep(order=5, name="Bilva Patra Offering", description="Offer Bilva (Bel) leaves",
                     mantras=self._mantras.get_mantras_for_step("shiva_puja"), duration_minutes=10, instructions="Offer 108 bilva leaves one by one on the linga, each with Om Namah Shivaya."),
            PujaStep(order=6, name="Rudra Dhyana", description="Meditation on Lord Shiva",
                     duration_minutes=10, instructions="Meditate on Shiva's form - ash-smeared, trishul-bearing, seated in meditation."),
            PujaStep(order=7, name="Shiva Tandava Stotram", description="Recitation of praise hymn",
                     duration_minutes=10, instructions="Recite the Shiva Tandava Stotram or Rudrashtakam."),
        ] + self._common_closing_steps(8)
        pujas["Shiva Puja"] = Puja(name="Shiva Puja", deity=Deity.SHIVA, description="Worship of Lord Shiva with Abhishek", occasion="Maha Shivaratri, Mondays, Pradosh", best_time="Early morning or evening, Pradosh kaal", steps=steps, samagri=self._materials.get_full_list("Shiva"), total_duration_minutes=70, difficulty="medium")

        # 5. Vishnu Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Vishnu Avahana", description="Invoke Lord Vishnu",
                     mantras=self._mantras.get_mantras_for_step("vishnu_puja"), duration_minutes=10, instructions="Place Vishnu idol, offer tulsi leaves and yellow flowers."),
            PujaStep(order=5, name="Vishnu Sahasranama", description="1000 names of Vishnu (or selected portions)",
                     duration_minutes=20, instructions="Recite Vishnu Sahasranama. Offer tulsi leaf with each name or section."),
            PujaStep(order=6, name="Shodashopachara", description="16-step worship", duration_minutes=15, instructions="Complete all 16 offerings to Vishnu."),
        ] + self._common_closing_steps(7)
        pujas["Vishnu Puja"] = Puja(name="Vishnu Puja", deity=Deity.VISHNU, description="Worship of Lord Vishnu, the preserver", occasion="Ekadashi, Thursdays", best_time="Morning", steps=steps, samagri=self._materials.get_full_list("Vishnu"), total_duration_minutes=65, difficulty="medium")

        # 6. Durga Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Kalash Sthapana", description="Establish sacred pot with Durga invocation",
                     duration_minutes=5, instructions="Place kalash on rice bed. Invoke Durga's presence."),
            PujaStep(order=5, name="Durga Avahana", description="Invoke Goddess Durga",
                     mantras=self._mantras.get_mantras_for_step("durga_puja"), duration_minutes=10, instructions="Invoke the nine forms of Durga. Offer red flowers and sindoor."),
            PujaStep(order=6, name="Durga Saptashati Path", description="Recitation of Durga Saptashati (selected chapters)",
                     duration_minutes=20, instructions="Read selected chapters of the Devi Mahatmya."),
            PujaStep(order=7, name="Kumkum Archana", description="Offering kumkum with 108 names",
                     duration_minutes=10, instructions="Offer kumkum and red flowers chanting Durga Ashtottara."),
        ] + self._common_closing_steps(8)
        pujas["Durga Puja"] = Puja(name="Durga Puja", deity=Deity.DURGA, description="Worship of Goddess Durga for protection and strength", occasion="Navaratri, Tuesdays, Ashtami", best_time="Morning", steps=steps, samagri=self._materials.get_full_list("Durga"), total_duration_minutes=70, difficulty="hard")

        # 7. Navagraha Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Navagraha Sthapana", description="Arrange nine planets in correct formation",
                     duration_minutes=10, instructions="Place nine betel nuts in mandala formation: Sun center, Moon E, Mars S, Mercury NE, Jupiter N, Venus SE, Saturn W, Rahu SW, Ketu NW."),
            PujaStep(order=5, name="Graha Avahana", description="Invoke each planet",
                     mantras=self._mantras.get_mantras_for_step("navagraha_puja"), duration_minutes=15, instructions="Invoke each graha with its specific mantra and offer navadhanya."),
            PujaStep(order=6, name="Graha Shanti", description="Pacification rituals", duration_minutes=10, instructions="Offer specific items to each planet for peace."),
        ] + self._common_closing_steps(7)
        pujas["Navagraha Puja"] = Puja(name="Navagraha Puja", deity=Deity.NAVAGRAHA, description="Worship of nine celestial bodies for planetary harmony", occasion="Saturday, during adverse dasha periods", best_time="Morning", steps=steps, samagri=self._materials.get_full_list("Navagraha"), total_duration_minutes=55, difficulty="hard")

        # 8. Satyanarayan Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Satyanarayan Avahana", description="Invoke Lord Satyanarayan",
                     mantras=self._mantras.get_mantras_for_step("satyanarayan_puja"), duration_minutes=10, instructions="Place idol/image. Offer tulsi, banana, and other fruits."),
            PujaStep(order=5, name="Katha Shravan", description="Listening to the five chapters of Satyanarayan Katha",
                     duration_minutes=30, instructions="Read all five chapters. Listeners hold akshata in right hand. After each chapter, offer akshata."),
            PujaStep(order=6, name="Prasad Preparation", description="Prepare and offer sheera/prasad",
                     duration_minutes=5, instructions="Offer sheera (semolina halwa) with banana and tulsi leaf."),
        ] + self._common_closing_steps(7)
        pujas["Satyanarayan Puja"] = Puja(name="Satyanarayan Puja", deity=Deity.SATYANARAYAN, description="Worship of Lord Satyanarayan for fulfilled wishes", occasion="Purnima (full moon), auspicious occasions", best_time="Evening", steps=steps, samagri=self._materials.get_full_list("Satyanarayan"), total_duration_minutes=70, difficulty="medium")

        # 9. Hanuman Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Hanuman Avahana", description="Invoke Lord Hanuman",
                     mantras=self._mantras.get_mantras_for_step("hanuman_puja"), duration_minutes=5, instructions="Offer sindoor and jasmine oil to Hanuman idol."),
            PujaStep(order=5, name="Hanuman Chalisa", description="Recitation of 40 verses praising Hanuman",
                     duration_minutes=10, instructions="Recite the complete Hanuman Chalisa with devotion."),
            PujaStep(order=6, name="Sundara Kanda", description="Reading from Ramayana (optional)",
                     duration_minutes=15, instructions="Read selected portions of Sundara Kanda."),
        ] + self._common_closing_steps(7)
        pujas["Hanuman Puja"] = Puja(name="Hanuman Puja", deity=Deity.HANUMAN, description="Worship of Lord Hanuman for strength and courage", occasion="Tuesdays, Saturdays, Hanuman Jayanti", best_time="Morning or evening", steps=steps, samagri=self._materials.get_full_list("Hanuman"), total_duration_minutes=45, difficulty="easy")

        # 10. Krishna Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Krishna Abhishek", description="Bathing the idol with panchamrit",
                     duration_minutes=10, instructions="Bathe Krishna idol with milk, yogurt, honey, ghee, and sugar."),
            PujaStep(order=5, name="Shringar", description="Decorating Krishna",
                     mantras=self._mantras.get_mantras_for_step("krishna_puja"), duration_minutes=10, instructions="Dress Krishna in new clothes, add peacock feather, offer butter and tulsi."),
            PujaStep(order=6, name="Bhagavad Gita Path", description="Reading from Bhagavad Gita",
                     duration_minutes=15, instructions="Read a chapter from the Gita or chant selected shlokas."),
        ] + self._common_closing_steps(7)
        pujas["Krishna Puja"] = Puja(name="Krishna Puja", deity=Deity.KRISHNA, description="Worship of Lord Krishna with love and devotion", occasion="Janmashtami, Ekadashi", best_time="Midnight on Janmashtami, morning otherwise", steps=steps, samagri=self._materials.get_full_list("Krishna"), total_duration_minutes=55, difficulty="medium")

        # 11. Rama Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Rama Avahana", description="Invoke Lord Rama",
                     mantras=self._mantras.get_mantras_for_step("rama_puja"), duration_minutes=10, instructions="Place Rama-Sita-Lakshmana-Hanuman idols. Offer tulsi."),
            PujaStep(order=5, name="Ramayana Path", description="Reading from Ramayana",
                     duration_minutes=20, instructions="Read selected portions from Sundara Kanda or Yuddha Kanda."),
        ] + self._common_closing_steps(6)
        pujas["Rama Puja"] = Puja(name="Rama Puja", deity=Deity.RAMA, description="Worship of Lord Rama, the ideal king", occasion="Ram Navami, Tuesdays", best_time="Noon (Rama's birth time)", steps=steps, samagri=self._materials.get_full_list("Vishnu"), total_duration_minutes=50, difficulty="medium")

        # 12. Kali Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Kali Avahana", description="Invoke Goddess Kali",
                     mantras=self._mantras.get_mantras_for_step("kali_puja"), duration_minutes=10, instructions="Place Kali image on red cloth. Offer red hibiscus flowers."),
            PujaStep(order=5, name="Kali Kavach", description="Recitation of protective armor hymn",
                     duration_minutes=10, instructions="Recite Kali Kavach for protection from negative energies."),
            PujaStep(order=6, name="Tantric Archana", description="Offering with 108 names",
                     duration_minutes=15, instructions="Offer red flowers with each of 108 names of Kali."),
        ] + self._common_closing_steps(7)
        pujas["Kali Puja"] = Puja(name="Kali Puja", deity=Deity.KALI, description="Worship of Goddess Kali for destruction of evil", occasion="Diwali (in Bengal), Tuesdays, Amavasya", best_time="Midnight", steps=steps, samagri=self._materials.get_full_list("Durga"), total_duration_minutes=55, difficulty="hard")

        # 13. Gayatri Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Surya Arghya", description="Offering water to the Sun",
                     duration_minutes=5, instructions="Stand facing east. Pour water from copper vessel towards the sun."),
            PujaStep(order=5, name="Gayatri Japa", description="Chanting the Gayatri Mantra",
                     mantras=self._mantras.get_mantras_for_step("gayatri"), duration_minutes=20, instructions="Sit in padmasana. Chant Gayatri Mantra 108 times using rudraksha mala."),
            PujaStep(order=6, name="Havan", description="Fire offering (optional)",
                     duration_minutes=15, instructions="Light sacred fire. Offer ghee and samagri with 'svaha' after each mantra."),
        ] + self._common_closing_steps(7)
        pujas["Gayatri Puja"] = Puja(name="Gayatri Puja", deity=Deity.GAYATRI, description="Worship through the Gayatri Mantra", occasion="Daily practice, Gayatri Jayanti", best_time="Sandhya times (sunrise, noon, sunset)", steps=steps, samagri=self._materials.get_full_list("Vishnu"), total_duration_minutes=55, difficulty="easy")

        # 14. Surya Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Surya Namaskar", description="Sun salutation mantras",
                     mantras=self._mantras.get_mantras_for_step("navagraha_puja")[:1], duration_minutes=10, instructions="Face east. Offer arghya to the sun with copper vessel."),
            PujaStep(order=5, name="Aditya Hridayam", description="Hymn to the Sun",
                     duration_minutes=15, instructions="Recite the Aditya Hridayam stotra from Ramayana."),
        ] + self._common_closing_steps(6)
        pujas["Surya Puja"] = Puja(name="Surya Puja", deity=Deity.SURYA, description="Worship of the Sun God", occasion="Sundays, Makar Sankranti, Chhath", best_time="Sunrise", steps=steps, samagri=self._materials.get_full_list("Vishnu"), total_duration_minutes=40, difficulty="easy")

        # 15. Tulsi Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Tulsi Avahana", description="Invoke Tulsi Devi",
                     duration_minutes=5, instructions="Stand before Tulsi plant. Light diya at the base."),
            PujaStep(order=5, name="Tulsi Puja", description="Worship of Tulsi plant",
                     duration_minutes=10, instructions="Offer water, haldi, kumkum, and flowers to Tulsi. Walk around the plant 7 times."),
        ] + self._common_closing_steps(6)
        pujas["Tulsi Puja"] = Puja(name="Tulsi Puja", deity=Deity.TULSI, description="Worship of the sacred Tulsi plant", occasion="Daily, Tulsi Vivah (Kartik)", best_time="Evening", steps=steps, samagri=self._materials.get_common_items(), total_duration_minutes=30, difficulty="easy")

        # 16. Parvati Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Parvati Avahana", description="Invoke Goddess Parvati",
                     duration_minutes=10, instructions="Place Parvati idol. Offer red flowers and sindoor."),
            PujaStep(order=5, name="Shodashopachara", description="16-step worship", duration_minutes=15, instructions="Perform complete 16-step worship."),
            PujaStep(order=6, name="Gauri Ashtottara", description="108 names of Gauri",
                     duration_minutes=10, instructions="Chant 108 names of Parvati with flower offerings."),
        ] + self._common_closing_steps(7)
        pujas["Parvati Puja"] = Puja(name="Parvati Puja", deity=Deity.PARVATI, description="Worship of Goddess Parvati for marital bliss", occasion="Hartalika Teej, Mondays", best_time="Morning", steps=steps, samagri=self._materials.get_full_list("Durga"), total_duration_minutes=55, difficulty="medium")

        # 17. Kartikeya Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Kartikeya Avahana", description="Invoke Lord Kartikeya",
                     mantras=[Mantra(sanskrit="Om Saravanabhavaya Namaha", transliteration="Om Sa-ra-va-na-bha-vaa-ya Na-ma-ha", meaning="Salutations to the one born in the reeds", repetitions=108)],
                     duration_minutes=10, instructions="Place Kartikeya idol. Offer red flowers and fruits."),
            PujaStep(order=5, name="Skanda Sashti Kavacham", description="Protective hymn",
                     duration_minutes=10, instructions="Recite Skanda Sashti Kavacham for protection."),
        ] + self._common_closing_steps(6)
        pujas["Kartikeya Puja"] = Puja(name="Kartikeya Puja", deity=Deity.KARTIKEYA, description="Worship of Lord Kartikeya (Murugan)", occasion="Skanda Sashti, Tuesdays", best_time="Morning", steps=steps, samagri=self._materials.get_common_items(), total_duration_minutes=40, difficulty="easy")

        # 18. Radha-Krishna Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Radha-Krishna Avahana", description="Invoke Radha and Krishna together",
                     mantras=self._mantras.get_mantras_for_step("krishna_puja"), duration_minutes=10, instructions="Place Radha-Krishna idol. Offer tulsi, butter, and peacock feather."),
            PujaStep(order=5, name="Shringar", description="Dressing and decorating the divine couple",
                     duration_minutes=10, instructions="Dress the idols in matching clothes. Adorn with ornaments and flowers."),
            PujaStep(order=6, name="Bhajan & Kirtan", description="Devotional singing",
                     duration_minutes=15, instructions="Sing Radha-Krishna bhajans and Maha Mantra kirtan."),
        ] + self._common_closing_steps(7)
        pujas["Radha-Krishna Puja"] = Puja(name="Radha-Krishna Puja", deity=Deity.RADHA_KRISHNA, description="Worship of the divine couple Radha and Krishna", occasion="Holi, Radha Ashtami, Janmashtami", best_time="Morning or evening", steps=steps, samagri=self._materials.get_full_list("Krishna"), total_duration_minutes=55, difficulty="medium")

        # 19. Sita-Rama Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Sita-Rama Avahana", description="Invoke Sita and Rama",
                     mantras=self._mantras.get_mantras_for_step("rama_puja"), duration_minutes=10, instructions="Place Sita-Rama idol with Lakshmana and Hanuman. Offer flowers and tulsi."),
            PujaStep(order=5, name="Ramayana Path", description="Read selected kanda", duration_minutes=20, instructions="Read from Bal Kanda or Ayodhya Kanda."),
        ] + self._common_closing_steps(6)
        pujas["Sita-Rama Puja"] = Puja(name="Sita-Rama Puja", deity=Deity.SITA_RAMA, description="Worship of the divine couple Sita and Rama", occasion="Ram Navami, Vivah Panchami", best_time="Noon", steps=steps, samagri=self._materials.get_full_list("Vishnu"), total_duration_minutes=50, difficulty="medium")

        # 20. Shani Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Shani Avahana", description="Invoke Lord Shani",
                     mantras=[Mantra(sanskrit="Om Sham Shanishcharaya Namaha", transliteration="Om Sham Sha-nish-cha-raa-ya Na-ma-ha", meaning="Salutations to Saturn", repetitions=108)],
                     duration_minutes=10, instructions="Place Shani idol or image. Offer mustard oil and black sesame."),
            PujaStep(order=5, name="Shani Stotram", description="Hymn to Saturn",
                     duration_minutes=10, instructions="Recite Shani Stotram or Dasharatha Shani Stotram."),
            PujaStep(order=6, name="Til Daan", description="Donation of sesame seeds",
                     duration_minutes=5, instructions="Offer black sesame seeds, mustard oil, and iron items."),
        ] + self._common_closing_steps(7)
        pujas["Shani Puja"] = Puja(name="Shani Puja", deity=Deity.SHANI, description="Worship of Lord Shani for relief from Saturn's effects", occasion="Saturdays, Shani Amavasya, Shani Jayanti", best_time="Evening on Saturday", steps=steps, samagri=self._materials.get_full_list("Navagraha"), total_duration_minutes=45, difficulty="medium")

        # 21. Griha Pravesh Puja
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Vastu Shanti", description="Pacify the Vastu Purusha",
                     duration_minutes=10, instructions="Perform havan at the center of the house. Offer ghee and samagri."),
            PujaStep(order=5, name="Ganesh-Lakshmi Puja", description="Invoke prosperity in the new home",
                     mantras=self._mantras.get_mantras_for_step("ganesh_puja") + self._mantras.get_mantras_for_step("lakshmi_puja"), duration_minutes=20, instructions="Worship Ganesha and Lakshmi for obstacle-free prosperity in the new home."),
            PujaStep(order=6, name="Doodh Ubalna", description="Boiling milk ceremony",
                     duration_minutes=10, instructions="Boil milk on new stove until it overflows as a symbol of abundance."),
        ] + self._common_closing_steps(7)
        pujas["Griha Pravesh Puja"] = Puja(name="Griha Pravesh Puja", deity=Deity.GANESHA, description="House warming ceremony for new home", occasion="Moving into a new house", best_time="Morning, on auspicious muhurta", steps=steps, samagri=self._materials.get_full_list("Ganesha") + self._materials.get_puja_specific_items("Lakshmi"), total_duration_minutes=65, difficulty="hard")

        # 22. Navratri Puja (9 nights)
        steps = self._common_opening_steps() + [
            PujaStep(order=4, name="Ghatasthapana", description="Establish the sacred pot on Day 1",
                     duration_minutes=10, instructions="Sow barley seeds on clay bed. Place kalash. Light akhand diya."),
            PujaStep(order=5, name="Daily Devi Puja", description="Worship each form of Durga",
                     mantras=self._mantras.get_mantras_for_step("durga_puja"), duration_minutes=15, instructions="Day 1-3: Durga/Kali/Chandraghanta. Day 4-6: Lakshmi/Skandamata/Katyayani. Day 7-9: Saraswati/Mahagauri/Siddhidatri."),
            PujaStep(order=6, name="Durga Saptashati Path", description="Read Devi Mahatmya chapters",
                     duration_minutes=20, instructions="Read designated chapters for the day from Durga Saptashati."),
            PujaStep(order=7, name="Kanya Pujan", description="Worship of young girls (Day 8/9)",
                     duration_minutes=15, instructions="On Ashtami/Navami, wash feet of 9 girls representing 9 forms. Offer food and gifts."),
        ] + self._common_closing_steps(8)
        pujas["Navratri Puja"] = Puja(name="Navratri Puja", deity=Deity.DURGA, description="Nine nights of Goddess worship", occasion="Chaitra & Sharad Navratri", best_time="Morning", steps=steps, samagri=self._materials.get_full_list("Durga"), total_duration_minutes=80, difficulty="hard")

        return pujas

    def get_puja(self, name: str) -> Puja | None:
        """Get a puja by name."""
        return self._pujas.get(name)

    def get_all_pujas(self) -> list[Puja]:
        """Get all pujas."""
        return list(self._pujas.values())

    def get_pujas_by_deity(self, deity: Deity) -> list[Puja]:
        """Get pujas for a specific deity."""
        return [p for p in self._pujas.values() if p.deity == deity]

    def search_pujas(self, query: str) -> list[Puja]:
        """Search pujas by name or description."""
        q = query.lower()
        return [p for p in self._pujas.values() if q in p.name.lower() or q in p.description.lower()]

    def get_puja_names(self) -> list[str]:
        """Get all puja names."""
        return list(self._pujas.keys())

    def get_pujas_by_difficulty(self, difficulty: str) -> list[Puja]:
        """Get pujas filtered by difficulty level."""
        return [p for p in self._pujas.values() if p.difficulty == difficulty]
