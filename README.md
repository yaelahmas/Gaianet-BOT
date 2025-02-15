# GAIANET-BOT

## 🚀 Main Features

✅ **Auto Chat AI** – The bot will send questions and receive answers from the AI  
✅ **API Key Rotation** to prevent usage limits  
✅ **Automatic Retry on Request Failures** to improve success rate  
✅ **Countdown Between Questions** to ensure a more stable process

## 📌 Icons & Messages in the Program

| Icon | Message                      | Description                                 |
| ---- | ---------------------------- | ------------------------------------------- |
| 🏁   | Starting session #...        | Starting a new session in the chatbot       |
| 📝   | Question: ...                | Indicator of the question being sent        |
| 🌍   | Base URL or Domain: ...      | Displays the Base URL or Domain             |
| 🔑   | API Key: ...                 | Displays the API Key (partially obfuscated) |
| 💬   | Answer: ...                  | Answer from the AI                          |
| 🚨   | Error: ...                   | Error or failure in the request             |
| ⏳   | Next question in ... seconds | Countdown before the next question is sent  |
| 😞   | Failed to get an answer...   | No answer received after several attempts   |
| 🎯   | Session #... finished!       | Summary of the session results              |

## 🛠 Requirements

- Python 3.9 or higher must be installed
- Ensure that `pip` is available

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yaelahmas/Gaianet-BOT.git
   cd Gaianet-BOT
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

- **`file_api_keys.txt`**

  - Fill with your AI API keys in the following format:
    ```bash
    your_gaia_api_key_1
    your_gaia_api_key_2
    ```

- **`file_questions.txt`** _(List of questions used by the chatbot)_
  - Fill with a list of questions in the following format:
    ```bash
    your_questions_1
    your_questions_2
    ```

## ▶️ Running the Program

```bash
python bot.py
```

## ☕ Support Me

- **EVM:** 0x4e78cefe62b4dd9df4335d44b7f69a1e5b3111e8
- **TON:** UQBgvMIAbE0GVJWP2i7A2qqkFY6WvSdZh6nvo5EOgMtjggTm
- **SOL:** 6iCzsAb41e1SSPae66nhzP1ocnY9kD2128xmdyrYwjpS
- **SUI:** 0xd8d6bad559a6494f2e59f96c35264dcbdcf9e1a32d54994bf8bf28fb23b37bea

Thank you for visiting this repository! Don't forget to star ⭐ and follow! If you have any questions or find bugs, please open an _issue_ in this repository.
