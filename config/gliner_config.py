class GlinerConfig:
    def __init__(self):
        self.model_path = "gliner/gliner_multi_pii-v1"

        # Presidio formatında entity türleri 
        self.entity_types = [
            # Personal Identity
            "PERSON",
            "GENDER",
            "MARITAL_STATUS",
            "DATE_OF_BIRTH",
            "TCKN",
            "NATIONAL_ID_NUMBER",
            "BLOOD_TYPE",
            "MOTHER_MAIDEN_NAME",

            # Contact Information
            "PHONE_NUMBER",
            "EMAIL_ADDRESS",
            "ADDRESS",
            "ZIP_CODE",
            "IP_ADDRESS",

            # Financial
            "BANK_ACCOUNT_NUMBER",
            "IBAN",
            "CREDIT_CARD_NUMBER",
            "CREDIT_CARD_EXPIRATION_DATE",
            "CVC_CVV",
            "SALARY",
            "TRANSACTION_NUMBER",

            # Medical (Special)
            "MEDICAL_CONDITION",

            # Professional
            "OCCUPATION",
            "ORGANIZATION",
            "POLITICAL_VIEW",
            "RELIGION",

            # Technical Identifiers
            "LICENSE_PLATE_NUMBER",
            "SERIAL_NUMBER",

            # Legal & Admin
            "PASSPORT_NUMBER",
            "DRIVER_LICENSE_NUMBER",
            "SGK_NUMBER",
            "TAX_NUMBER_VKN",
            "CRIMINAL_RECORD",
            "COURT_CASE_ID",
            "SIGNATURE_IMAGE",

            # Sensitive (Special)
            "BIOMETRIC_DATA",
            "GENETIC_DATA",
            "RACE_ETHNICITY",
            "TRADE_UNION_MEMBERSHIP",
            "SEXUAL_ORIENTATION",
            "CRIMINAL_CONVICTIONS",

            # Org & Employment
            "EMPLOYEE_ID",
            "CUSTOMER_ID",
            "PROJECT_NAME",
            "DEPARTMENT",
            "WORK_EMAIL",
            "WORK_PHONE",
            "WORK_LOCATION",
            "SALARY_GRADE",
            "PERFORMANCE_SCORE",
            "HIRE_DATE",
            "TERMINATION_DATE",

            # Digital & Technical
            "DEVICE_ID",
            "IMEI",
            "MAC_ADDRESS",
            "USER_AGENT",
            "COOKIES",
            "SESSION_ID",
            "TOKEN",
            "API_KEY",
            "API_SECRET",
            "FILE_PATH",
            "FILE_NAME",
            "GEOLOCATION",

            # Education
            "STUDENT_ID",
            "SCHOOL_NAME",
            "DEGREE_MAJOR",
            "GRADUATION_YEAR",
            "GPA",
            "CERTIFICATE_ID",

            # Behavioral & Usage
            "CHAT_MESSAGE",
            "VOICE_RECORDING",
            "SEARCH_QUERY",
            "BROWSING_HISTORY",
            "PURCHASE_HISTORY",
            "LOG_ENTRY",
            "SENTIMENT_TEXT",

            # Visual & Document
            "PHOTO",
            "VIDEO_FRAME",
            "HANDWRITTEN_TEXT",
            "DOCUMENT_SCAN",
            "STAMP_SEAL_IMAGE",

            # IT/Software - Secrets
            "API_KEY_GENERIC",
            "AWS_ACCESS_KEY_ID",
            "AWS_SECRET_ACCESS_KEY",
            "GCP_SA_PRIVATE_KEY",
            "AZURE_CONNECTION_STRING",
            "STRIPE_SECRET",
            "GITHUB_PAT",
            "SLACK_WEBHOOK",
            "JWT_TOKEN",
            "OAUTH_CLIENT_SECRET",
            "ENCRYPTION_KEY",
            "SSH_PRIVATE_KEY",
            "CERT_PRIVATE_KEY",

            # IT/Software - Config & DB
            "DB_CONNECTION_STRING",
            "JDBC_URL",
            "REDIS_URI",
            "KAFKA_SASL",
            "SMTP_CREDENTIALS",

            # IT/Software - Cloud & DevOps
            "KUBECONFIG",
            "K8S_SECRET_YAML",
            "HELM_VALUES_SECRET",
            "TERRAFORM_STATE",
            "CLOUDWATCH_LINK",
            "S3_BUCKET_URL",
            "IAM_ARN",

            # IT/Software - Code & Repos
            "REPO_URL_PRIVATE",
            "COMMIT_HASH",
            "INTERNAL_PROJECT_CODE",
            "STACK_TRACE_WITH_PII",
            "PACKAGE_REGISTRY_TOKEN",
            "DOCKERCFG_CREDENTIALS",

            # IT/Software - Logs & Ops
            "ACCESS_LOG_PII",
            "AUTH_LOG",
            "ERROR_LOG_SECRETS",
            "INTERNAL_URL",
            "MONITORING_LINKS",

            # Workflow Links
            "JIRA_TICKET_URL",
            "SLACK_DM_ID",
            "PAGERDUTY_TOKEN",
        ]

        # Presidio → GLiNER format mapping
        self.entity_mapping = {
            # Personal Identity
            "person": "PERSON",
            "gender": "GENDER",
            "marital status": "MARITAL_STATUS",
            "date of birth": "DATE_OF_BIRTH",
            "tckn": "TCKN",
            "national id number": "NATIONAL_ID_NUMBER",
            "blood type": "BLOOD_TYPE",
            "mother maiden name": "MOTHER_MAIDEN_NAME",

            # Contact Information
            "phone number": "PHONE_NUMBER",
            "email address": "EMAIL_ADDRESS",
            "address": "ADDRESS",
            "zip code": "ZIP_CODE",
            "ip address": "IP_ADDRESS",

            # Financial
            "bank account number": "BANK_ACCOUNT_NUMBER",
            "iban": "IBAN",
            "credit card number": "CREDIT_CARD_NUMBER",
            "credit card expiration date": "CREDIT_CARD_EXPIRATION_DATE",
            "cvc/cvv": "CVC_CVV",
            "salary": "SALARY",
            "transaction number": "TRANSACTION_NUMBER",

            # Medical (Special)
            "medical condition": "MEDICAL_CONDITION",

            # Professional
            "occupation": "OCCUPATION",
            "organization": "ORGANIZATION",
            "political view": "POLITICAL_VIEW",
            "religion": "RELIGION",

            # Technical Identifiers
            "license plate number": "LICENSE_PLATE_NUMBER",
            "serial number": "SERIAL_NUMBER",

            # Legal & Admin
            "passport number": "PASSPORT_NUMBER",
            "driver license number": "DRIVER_LICENSE_NUMBER",
            "sgk number": "SGK_NUMBER",
            "tax number vkn": "TAX_NUMBER_VKN",
            "criminal record": "CRIMINAL_RECORD",
            "court case id": "COURT_CASE_ID",
            "signature image": "SIGNATURE_IMAGE",

            # Sensitive (Special)
            "biometric data": "BIOMETRIC_DATA",
            "genetic data": "GENETIC_DATA",
            "race ethnicity": "RACE_ETHNICITY",
            "trade union membership": "TRADE_UNION_MEMBERSHIP",
            "sexual orientation": "SEXUAL_ORIENTATION",
            "criminal convictions": "CRIMINAL_CONVICTIONS",

            # Org & Employment
            "employee id": "EMPLOYEE_ID",
            "customer id": "CUSTOMER_ID",
            "project name": "PROJECT_NAME",
            "department": "DEPARTMENT",
            "work email": "WORK_EMAIL",
            "work phone": "WORK_PHONE",
            "work location": "WORK_LOCATION",
            "salary grade": "SALARY_GRADE",
            "performance score": "PERFORMANCE_SCORE",
            "hire date": "HIRE_DATE",
            "termination date": "TERMINATION_DATE",

            # Digital & Technical
            "device id": "DEVICE_ID",
            "imei": "IMEI",
            "mac address": "MAC_ADDRESS",
            "user agent": "USER_AGENT",
            "cookies": "COOKIES",
            "session id": "SESSION_ID",
            "token": "TOKEN",
            "api key": "API_KEY",
            "api secret": "API_SECRET",
            "file path": "FILE_PATH",
            "file name": "FILE_NAME",
            "geolocation": "GEOLOCATION",

            # Education
            "student id": "STUDENT_ID",
            "school name": "SCHOOL_NAME",
            "degree major": "DEGREE_MAJOR",
            "graduation year": "GRADUATION_YEAR",
            "gpa": "GPA",
            "certificate id": "CERTIFICATE_ID",

            # Behavioral & Usage
            "chat message": "CHAT_MESSAGE",
            "voice recording": "VOICE_RECORDING",
            "search query": "SEARCH_QUERY",
            "browsing history": "BROWSING_HISTORY",
            "purchase history": "PURCHASE_HISTORY",
            "log entry": "LOG_ENTRY",
            "sentiment text": "SENTIMENT_TEXT",

            # Visual & Document
            "photo": "PHOTO",
            "video frame": "VIDEO_FRAME",
            "handwritten text": "HANDWRITTEN_TEXT",
            "document scan": "DOCUMENT_SCAN",
            "stamp seal image": "STAMP_SEAL_IMAGE",

            # IT/Software - Secrets
            "api key generic": "API_KEY_GENERIC",
            "aws access key id": "AWS_ACCESS_KEY_ID",
            "aws secret access key": "AWS_SECRET_ACCESS_KEY",
            "gcp sa private key": "GCP_SA_PRIVATE_KEY",
            "azure connection string": "AZURE_CONNECTION_STRING",
            "stripe secret": "STRIPE_SECRET",
            "github pat": "GITHUB_PAT",
            "slack webhook": "SLACK_WEBHOOK",
            "jwt token": "JWT_TOKEN",
            "oauth client secret": "OAUTH_CLIENT_SECRET",
            "encryption key": "ENCRYPTION_KEY",
            "ssh private key": "SSH_PRIVATE_KEY",
            "cert private key": "CERT_PRIVATE_KEY",

            # IT/Software - Config & DB
            "db connection string": "DB_CONNECTION_STRING",
            "jdbc url": "JDBC_URL",
            "redis uri": "REDIS_URI",
            "kafka sasl": "KAFKA_SASL",
            "smtp credentials": "SMTP_CREDENTIALS",

            # IT/Software - Cloud & DevOps
            "kubeconfig": "KUBECONFIG",
            "k8s secret yaml": "K8S_SECRET_YAML",
            "helm values secret": "HELM_VALUES_SECRET",
            "terraform state": "TERRAFORM_STATE",
            "cloudwatch link": "CLOUDWATCH_LINK",
            "s3 bucket url": "S3_BUCKET_URL",
            "iam arn": "IAM_ARN",

            # IT/Software - Code & Repos
            "repo url private": "REPO_URL_PRIVATE",
            "commit hash": "COMMIT_HASH",
            "internal project code": "INTERNAL_PROJECT_CODE",
            "stack trace with pii": "STACK_TRACE_WITH_PII",
            "package registry token": "PACKAGE_REGISTRY_TOKEN",
            "dockercfg credentials": "DOCKERCFG_CREDENTIALS",

            # IT/Software - Logs & Ops
            "access log pii": "ACCESS_LOG_PII",
            "auth log": "AUTH_LOG",
            "error log secrets": "ERROR_LOG_SECRETS",
            "internal url": "INTERNAL_URL",
            "monitoring links": "MONITORING_LINKS",

            # Workflow Links
            "jira ticket url": "JIRA_TICKET_URL",
            "slack dm id": "SLACK_DM_ID",
            "pagerduty token": "PAGERDUTY_TOKEN"
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
