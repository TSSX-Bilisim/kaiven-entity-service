class GlinerConfig:
    def __init__(self):
        self.model_path = "gliner/gliner_multi_pii-v1"

        # Presidio formatında entity türleri
        self.entity_types = [
            "PERSON_NAME",
            "GENDER",
            "MARITAL_STATUS",
            "EMAIL_ADDRESS",
            "ADDRESS",
            "MEDICAL_CONDITION",
            "BLOOD_TYPE",
            "RELIGION",
            "POLITICAL_VIEW",
            "ORGANIZATION",
            "SALARY",
            "OCCUPATION",
        ]

        # Presidio → GLiNER format mapping
        self.entity_mapping = {
            "PERSON_NAME": "person name",
            "GENDER": "gender",
            "MARITAL_STATUS": "marital status",
            "EMAIL_ADDRESS": "email address",
            "ADDRESS": "address",
            "MEDICAL_CONDITION": "medical condition",
            "BLOOD_TYPE": "blood type",
            "RELIGION": "religion",
            "POLITICAL_VIEW": "political view",
            "ORGANIZATION": "organization",
            "SALARY": "salary",
            "OCCUPATION": "occupation",
        }

        # Belirli terimleri içeren yanlış pozitifleri engellemek için deny list
        self.deny_list = {
            "person name": ["isim", "ad", "soyad"],
            "gender": ["cinsiyet", "erkek", "kadın"],
            "marital status": ["evli", "bekar", "boşanmış"],
            "email address": ["e-posta", "mail", "adres"],
            "address": ["adres", "konum", "yer"],
            "medical condition": ["hastalık", "rahatsızlık", "durum"],
            "blood type": ["kan", "grubu", "tip"],
            "religion": ["din", "inanç", "mezhep"],
            "political view": ["görüş", "ideoloji", "düşünce"],
            "organization": ["kurum", "şirket", "dernek"],
            "salary": ["maaş", "ücret", "kazanç"],
            "occupation": ["meslek", "iş", "pozisyon"],
        }

        # Her entity türü için örnek cümleler
        self.examples = {
            "person name": [
                "Ali is a teacher",
                "Ayşe met with John",
                "Mehmet and Elif are siblings",
                "Ali öğretmen olarak çalışıyor.",
                "Ayşe, Elif ile buluştu.",
                "Mehmet ve Zeynep kardeştir.",
            ],
            "gender": [
                "His gender is male",
                "She identifies as female",
                "They are non-binary",
                "Cinsiyeti erkektir.",
                "Kadın olduğunu belirtti.",
                "Kendini non-binary olarak tanımlıyor.",
            ],
            "marital status": [
                "He is married",
                "She is divorced",
                "They are single",
                "Evli bir bireydir.",
                "Boşanmış durumda.",
                "Bekar olduğunu söyledi.",
            ],
            "email address": [
                "Her email is ayse@example.com",
                "Contact him at ali@gmail.com",
                "E-posta adresi ayse@example.com'dur.",
                "Bana ali@gmail.com üzerinden ulaşabilirsiniz.",
                "İletişim için mehmet@firma.com adresini kullanın.",
            ],
            "address": [
                "123 Main Street, New York",
                "He lives in Kadıköy",
                "Fatih Mahallesi, İstanbul'da yaşıyor.",
                "Adres bilgisi: 123 Main Street, New York.",
            ],
            "medical condition": [
                "He suffers from diabetes",
                "She has asthma",
                "Diyabet hastasıdır.",
                "Astım problemi var.",
                "Hipertansiyon teşhisi kondu.",
            ],
            "blood type": [
                "His blood type is AB+",
                "She is O negative",
                "Kan grubu AB+.",
                "O negatif olduğunu söyledi.",
                "A tipi kana sahip.",
            ],
            "religion": [
                "Ali is Muslim",
                "She converted to Christianity",
                "Ali Müslümandır.",
                "Hristiyanlığa geçti.",
                "Budist inancına sahiptir.",
            ],
            "political view": [
                "He supports socialism",
                "She is a conservative",
                "Sosyalist görüşleri savunuyor.",
                "Muhafazakâr olduğunu belirtti.",
                "Liberal düşüncelere sahip.",
            ],
            "organization": [
                "He works at Microsoft",
                "She is part of UNICEF",
                "Microsoft'ta çalışıyor.",
                "UNICEF üyesi.",
                "Eğitim-Sen sendikasına bağlı.",
            ],
            "salary": [
                "She earns 5,000 USD monthly",
                "His salary is 15,000 TL",
                "Maaşı 15.000 TL'dir.",
                "Aylık 5.000 USD kazanıyor.",
                "Geliri 20.000 TL civarında.",
            ],
            "occupation": [
                "He is a software engineer",
                "She works as a nurse",
                "Yazılım mühendisi olarak çalışıyor.",
                "Hemşire olarak görev yapıyor.",
                "Avukatlık yapıyor.",
            ],
        }
