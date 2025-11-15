# Python 3.13 slim imajını kullan
FROM python:3.13-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Sistem bağımlılıklarını yükle
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# UV paket yöneticisini kur (daha hızlı bağımlılık kurulumu için)
RUN pip install --no-cache-dir uv

# Proje dosyalarını kopyala
COPY pyproject.toml uv.lock ./

# Bağımlılıkları kur (bu layer cache'lenecek)
RUN uv pip install --system --no-cache -r pyproject.toml

# Uygulama kodunu kopyala
COPY . .

# Port açıklaması
EXPOSE 8000

# Uvicorn ile uygulamayı başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
