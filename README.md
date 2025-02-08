# GAIANET - AUTO CHATBOT AI

## 🚀 Fitur Utama

✅ **Auto Chat AI** – Bot akan mengirim pertanyaan dan mendapatkan jawaban dari AI  
✅ **Rotasi API Key & Model AI** untuk mencegah limitasi penggunaan  
✅ **Multi-akun dengan _threads_** untuk penggunaan lebih efisien  
✅ **Dukungan Proxy:**

- **Gunakan proxy otomatis** jika diperlukan
- **Rotasi proxy otomatis** jika terjadi kegagalan koneksi

✅ **Retry otomatis jika request gagal** untuk meningkatkan keberhasilan  
✅ **Countdown antar pertanyaan** agar proses berjalan lebih stabil

## 📌 Ikon & Pesan dalam Program

| Ikon | Pesan                                 | Deskripsi                                              |
| ---- | ------------------------------------- | ------------------------------------------------------ |
| 🛡️   | Proxy: ...                            | Menampilkan proxy (sebagian disamarkan)                |
| 🔑   | API Key: ...                          | Menampilkan API Key (sebagian disamarkan)              |
| 💬   | Jawaban: ...                          | Jawaban dari AI                                        |
| 🚨   | Kesalahan: ...                        | Error atau kegagalan permintaan                        |
| 📝   | Pertanyaan berikutnya                 | Indikator bahwa pertanyaan baru akan dikirim           |
| ⏳   | Pertanyaan berikutnya dalam ... detik | Countdown sebelum pertanyaan berikutnya                |
| 😞   | Gagal mendapatkan jawaban...          | Tidak mendapat jawaban setelah beberapa kali percobaan |
| 🏁   | Memulai sesi ke-...                   | Awal sesi baru dalam chatbot                           |
| 🎯   | Sesi ke-... selesai!                  | Ringkasan hasil sesi pertanyaan                        |

## 🛠 Persyaratan

- Python 3.9 atau lebih tinggi harus terinstal
- Pastikan `pip` sudah tersedia

## 🔧 Instalasi

1. **Clone repository**

   ```bash
   git clone https://github.com/yaelahmas/Gaianet-BOT.git
   ```

   ```bash
   cd Gaianet-BOT
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Konfigurasi

- **`file_api_keys.txt`**

  - Isi dengan API Key AI dalam format:
    ```bash
    api_key_1
    api_key_2
    ```

- **`file_configs.txt`**

  - Isi dengan model AI dan base URL domains dalam format:
    ```bash
    model_1|base_url_domain_1
    model_2|base_url_domain_2
    ```

- **`file_proxies.txt`** _(Opsional, jika menggunakan proxy)_

  - Isi dengan daftar proxy dalam format:
    ```bash
    ip:port
    protocol://ip:port
    protocol://user:pass@ip:port
    ```

- **`file_questions.txt`** _(Daftar pertanyaan yang digunakan oleh chatbot)_
  - Isi dengan daftar pertanyaan dalam format:
    ```bash
    What is AI?
    What is a Chat Bot?
    ```

## ▶️ Menjalankan Program

```bash
python bot.py
```

## ☕ Dukung Saya

- **EVM:** 0x4e78cefe62b4dd9df4335d44b7f69a1e5b3111e8
- **TON:** UQBgvMIAbE0GVJWP2i7A2qqkFY6WvSdZh6nvo5EOgMtjggTm
- **SOL:** 6iCzsAb41e1SSPae66nhzP1ocnY9kD2128xmdyrYwjpS
- **SUI:** 0xd8d6bad559a6494f2e59f96c35264dcbdcf9e1a32d54994bf8bf28fb23b37bea

Terima kasih sudah mengunjungi repository ini! Jangan lupa untuk memberi bintang ⭐ dan follow! Jika ada pertanyaan atau menemukan bug, silakan buat _issue_ di repository ini.
