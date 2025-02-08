import aiohttp, asyncio, random
from colorama import init, Fore, Style

init(autoreset=True)

# Banner Program
print(f"{Fore.LIGHTWHITE_EX}=" * 50)
print(f"{Fore.LIGHTWHITE_EX}             GAIANET - AUTO CHATBOT AI               ")
print(f"{Fore.LIGHTWHITE_EX}=" * 50)
print(f"{Fore.LIGHTGREEN_EX}Author   : Muhammad Andre Syahli")
print(f"{Fore.LIGHTBLUE_EX}Telegram : https://t.me/yaelahmas")
print(f"{Fore.LIGHTWHITE_EX}Github   : https://github.com/yaelahmas")
print(f"{Fore.LIGHTWHITE_EX}=" * 50)


# Fungsi untuk membaca konfigurasi model dan base_url dari file
def load_configs(file_path):
    configs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    configs.append({"model": parts[0], "base_url": parts[1]})
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}🚨 File {Fore.LIGHTWHITE_EX}{file_path} {Fore.LIGHTRED_EX}tidak ditemukan!")
    return configs


# Fungsi untuk membaca API Keys dari file
def load_api_keys(file_path):
    api_keys = []
    try:
        with open(file_path, "r") as file:
            api_keys = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}🚨 File {Fore.LIGHTWHITE_EX}{file_path} {Fore.LIGHTRED_EX}tidak ditemukan!")
    return api_keys


# Fungsi untuk pertanyaan dari file
def load_questions(file_path):
    questions = []
    try:
        with open(file_path, "r") as file:
            questions = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}🚨 File {Fore.LIGHTWHITE_EX}{file_path} {Fore.LIGHTRED_EX}tidak ditemukan!")
    return questions


# Memuat data dari file
CONFIGS = load_configs("file_configs.txt")
API_KEYS = load_api_keys("file_api_keys.txt")
QUESTIONS = load_questions("file_questions.txt")


# Memastikan ada konfigurasi yang dimuat
if not CONFIGS or not API_KEYS or not QUESTIONS:
    print(f"{Fore.LIGHTRED_EX}🚨 Konfigurasi dan API Key serta Daftar pertanyaan tidak ditemukan. Program dihentikan!")
    exit()


# Meminta pengguna apakah ingin menggunakan proxy
use_proxy = input(f"{Fore.LIGHTCYAN_EX}Apakah ingin menggunakan proxy? (ya/tidak): {Fore.LIGHTWHITE_EX}").strip().lower() == "ya"
print(f"{Fore.LIGHTWHITE_EX}=" * 50)


# Membaca daftar proxy dari file jika pengguna memilih menggunakan proxy
PROXIES = []
if use_proxy:
    try:
        with open("file_proxies.txt", "r") as file:
            PROXIES = [line.strip() for line in file if line.strip()]
        print(f"{Fore.LIGHTBLUE_EX}🛡️  Program berjalan dengan {Fore.LIGHTWHITE_EX}{len(PROXIES)} {Fore.LIGHTBLUE_EX}proxy.")
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}🚨 File proxies.txt tidak ditemukan. Berjalan tanpa proxy.")
        use_proxy = False
else:
    print(f"{Fore.LIGHTBLUE_EX}🌐 Program berjalan tanpa proxy.")


class ChatBot:
    def __init__(self, configs, proxies):
        self.configs = configs
        self.proxies = proxies
        self.config_index = 0
        self.api_key_index = 0
        self.proxy_index = 0  # Tambahkan variabel ini agar bisa merotasi proxy
        
    def get_next(self):
        """Mengambil model, URL, dan API key berikutnya secara bergantian"""
        config = self.configs[self.config_index]
        api_key = API_KEYS[self.api_key_index]

        # Update indeks untuk model, URL, dan API key agar bergantian
        self.config_index = (self.config_index + 1) % len(self.configs)
        self.api_key_index = (self.api_key_index + 1) % len(API_KEYS)

        return config['model'], config['base_url'], api_key

    async def send_question(self, question: str, max_retries=5):
        """Mengirim pertanyaan ke AI dengan retry terbatas & rotasi proxy"""
        retries = 0
        while retries < max_retries:  
            model, base_url, api_key = self.get_next()
            proxy = self.proxies[self.proxy_index] if use_proxy and self.proxies else None
            
            data = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ]
            }
            
            if model:  # Hanya tambahkan model jika ada
                data["model"] = model
                data["temperature"] = 0.3

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            }
            
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.post(base_url, headers=headers, json=data, proxy=proxy, timeout=60) as response:
                        response.raise_for_status()
                        result = await response.json()
                        answer = result["choices"][0]["message"]["content"]
                        
                        print(f"{Fore.LIGHTCYAN_EX}🌍 Base URL: {Fore.LIGHTWHITE_EX}{base_url}")
                        print(f"{Fore.LIGHTMAGENTA_EX}🔬 Model: {Fore.LIGHTWHITE_EX}{model}")
                        print(f"{Fore.LIGHTYELLOW_EX}🔑 API Key: {Fore.LIGHTWHITE_EX}{api_key[:10]}*****")  # Masking API Key
                        if proxy:
                            print(f"{Fore.LIGHTBLUE_EX}🛡️  Proxy: {Fore.LIGHTWHITE_EX}{proxy[:15]}*****")  # Masking Proxy
                        print(f"{Fore.LIGHTGREEN_EX}💬 Jawaban: {Fore.LIGHTWHITE_EX}{answer}")
                        print(f"{Fore.LIGHTWHITE_EX}=" * 50)
                        
                        return answer
                except Exception as e:
                    retries += 1
                    error_message = str(e).strip()
                    if not error_message:  # Jika error kosong
                        error_message = "Gagal mendapatkan respons."
                    print(f"{Fore.LIGHTRED_EX}🚨 Kesalahan: {Fore.LIGHTWHITE_EX}{error_message} - {Fore.LIGHTYELLOW_EX}(Percobaan {retries}/{max_retries})")
                    if use_proxy and self.proxies:
                        self.proxy_index = (self.proxy_index + 1) % len(self.proxies)  # Ganti proxy
                        print(f"{Fore.LIGHTCYAN_EX}🛡️  Mencoba dengan proxy baru:{Fore.LIGHTWHITE_EX}{self.proxies[self.proxy_index][:15]}*****")
                    await asyncio.sleep(5)
        
        return None  # Jika tetap gagal, kembalikan None
   
        
async def countdown(seconds):
    for i in range(seconds, -1, -1):
        print(f"{Fore.LIGHTYELLOW_EX}⏳ Pertanyaan berikutnya dalam {Fore.LIGHTWHITE_EX}{i} {Fore.LIGHTYELLOW_EX}detik...", end="\r")
        await asyncio.sleep(1)
    print(f"{Fore.LIGHTBLUE_EX}\r\033[K📝 Pertanyaan berikutnya\n", end="", flush=True)  # Hapus baris setelah countdown selesai


async def main():
    bot = ChatBot(CONFIGS, PROXIES)
    cycle = 0

    while True:
        cycle += 1
        answered = 0
        failed = 0
        random.shuffle(QUESTIONS)
        total_questions = len(QUESTIONS)
        
        print(f"{Fore.LIGHTGREEN_EX}🏁 Memulai sesi ke-{Fore.LIGHTWHITE_EX}{cycle} {Fore.LIGHTGREEN_EX}dari pertanyaan...")

        for index, question in enumerate(QUESTIONS, start=1):
            print(f"{Fore.LIGHTWHITE_EX}=" * 50)
            print(f"{Fore.LIGHTBLUE_EX}📝 Pertanyaan {Fore.LIGHTYELLOW_EX}({index}/{total_questions}): {Fore.LIGHTWHITE_EX}{question}")
            print(f"{Fore.LIGHTWHITE_EX}=" * 50)

            response = await bot.send_question(question)

            if response:
                answered += 1
            else:
                print(f"{Fore.LIGHTYELLOW_EX}😞 Gagal mendapatkan jawaban setelah beberapa percobaan. Maaf ya...")
                print(f"{Fore.LIGHTWHITE_EX}=" * 50)
                failed += 1
            
            if index < total_questions:
                await countdown(15)
        
        print(f"{Fore.LIGHTGREEN_EX}🎯 Sesi ke-{Fore.LIGHTWHITE_EX}{cycle} {Fore.LIGHTGREEN_EX}selesai! Berhasil terjawab: {Fore.LIGHTWHITE_EX}{answered}, {Fore.LIGHTRED_EX}Tidak terjawab: {Fore.LIGHTWHITE_EX}{failed}.")
        await asyncio.sleep(5)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print(f"{Fore.LIGHTRED_EX}🛑 Program dihentikan oleh pengguna.")
