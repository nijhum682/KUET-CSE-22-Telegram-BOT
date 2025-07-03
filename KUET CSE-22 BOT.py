from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Bot constants
TOKEN: Final = 'Paste your own bot token here'
BOT_USERNAME: Final = 'Paste your username here'

# Term question links
QUESTION_LINKS = {
    "2-1 2017": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1pQ7xouKnZifTQ2cs2d29D90JHbOJ1fIX/view?usp=drive_link"}],
    "2-1 2018": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1VAggt_RGgGR3WhfPwgQtt865MwpXfJlC/view?usp=drive_link"}],
    "2-1 2019": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/140aq_vZSbmTXoa245KCGDEk0u3VYHTSO/view?usp=drive_link"}],
    "2-1 2020": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/drive/folders/13S-MMus3qDfvNEvCE137_N96UqXsdW27?usp=drive_link"}],
    "2-1 2021": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1xtUztwhCcWU4ZKFfIEjXFkFGICaddeeJ/view?usp=drive_link"}],
    "2-1 all": [{"subject": "All Combined Years", "link": "https://drive.google.com/file/d/128pZbNbU9KrLv8Vhl6LA13P4LlLGqeK9/view?usp=drive_link"}],

    "1-2 2015": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1EKt7I0-nazYgAMAHVvxugGMpR_NZZBJE/view?usp=drive_link"}],
    "1-2 2016": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1EKVobUekrRhSFTFytEp_5pP5LHD7LwOv/view?usp=drive_link"}],
    "1-2 2017": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1EIW3o-HwFcRVvn-vjEZ-a3hMcsL_qumF/view?usp=drive_link"}],
    "1-2 2018": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1EH44w-FmM5v8GxsU--ZlPJpz4O2tlKfB/view?usp=drive_link"}],
    "1-2 2019": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1EGjIsCA2mV7z87gOscAUgTCreW5EsL8J/view?usp=drive_link"}],
    "1-2 2020": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1EGhBwCUW3HAAdXXLgRgQ221t6yu8wEjp/view?usp=drive_link"}],
    "1-2 2021": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1EcxX_VaYRvm533qdVBFzWSFxhcwcAbrH/view?usp=drive_link"}],
    "1-2 2022": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1EGF6VxOxCeYoUNj7w6MOUQCHgdn0x1aH/view?usp=drive_link"}],

    "1-1 2015": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1B8hVkX44j9fCOlimyiHInX99cWvYqLTD/view?usp=drive_link"}],
    "1-1 2016": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1hYq6CsH1mN2IAoh2wG9tiUwmFm6o3ffJ/view?usp=drive_link"}],
    "1-1 2017": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1ndbiezIw3S1_ufiAZFpxn4_5JA4iAAh8/view?usp=drive_link"}],
    "1-1 2018": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1tsG0wsiw9cljFa_zAmwRO44fuA2xuGtO/view?usp=drive_link"}],
    "1-1 2019": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/1Z-m32CsalT6OHpy0y4HoqVnd2PPGQ5kv/view?usp=drive_link"}],
    "1-1 2020": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/12tigSU2UunWU1kHGDst7iictiGqk8Tc5/view?usp=drive_link"}],
    "1-1 2022": [{"subject": "All CSE Subjects", "link": "https://drive.google.com/file/d/10gefnNMd5m1ieAjlAAoIR74IsA60zQG0/view?usp=drive_link"}]

}

# Slide links
SLIDE_LINKS = {
    "cse 2103": "https://drive.google.com/drive/folders/1Qks1fp_OTe8J9Hf7bEdr3ZKsr5uC4bsg?usp=drive_link",
    "cse 2104": "https://drive.google.com/drive/folders/1uBF6iae1qXV5SAryiFlBEMmcMe4uFzpO?usp=drive_link",
    "cse 2105": "https://drive.google.com/drive/folders/1Z9RBZiL39FPjGUimgnlglufogrt7M2mC?usp=drive_link",
    "cse 2106": "https://drive.google.com/drive/folders/1_UJzFSQL0He8vANOTawT5GyiUaMvb304?usp=drive_link",
    "cse 2113": "https://drive.google.com/drive/folders/1tyhgi5meGPfOXLIgHJOH_TXuSI_k8nQW?usp=drive_link",
    "cse 2114": "https://drive.google.com/drive/folders/1hyje8nYUg-IMJj6cu3T_my6ia_b1yTiE?usp=drive_link",
    "eee 2117": "https://drive.google.com/drive/folders/18HP1KJu13Y6sMYzrzBKyBdzPyYGv821_?usp=drive_link",

    "cse 1203": "https://drive.google.com/drive/folders/1wVprUbQDJMdAw8XU3XVmS_RbTWwD9Tne?usp=drive_link",
    "cse 1204": "https://drive.google.com/drive/folders/1u66ZpGTRwI8ociG148e-Lau6IoUjaBzc?usp=drive_link",
    "cse 1205": "https://drive.google.com/drive/folders/1B17DyUQa9UEcAL6jtcgNSZ702Uu8hi2v?usp=drive_link",
    "cse 1206": "https://drive.google.com/drive/folders/1hXLyGfkCcO4YrNXMuQODknuUTnC0aOze?usp=drive_link",
    "eee 1207": "https://drive.google.com/drive/folders/1Yap13NA0v6eHzdDya4o5yte4yPixphex?usp=drive_link",
    "eee 1208": "https://drive.google.com/drive/folders/1tzNPOfSctTUnn4kNLfBTOKTVToZqy2cu?usp=drive_link",
    "math 1207": "https://drive.google.com/drive/folders/13O5pWvW5LJPzc8QRV2yvV3B-ZOdTL2ts?usp=drive_link",
    "chem 1207": "https://drive.google.com/drive/folders/1keL6MmC2pzoAdKPGsauoRk2Ka1tKBoAR?usp=drive_link",
    "chem 1208": "https://drive.google.com/drive/folders/1Pk8hCPrV2kgmc6Sxzedl50HcIOk5lk7J?usp=drive_link",

    "cse 1101": "https://drive.google.com/drive/folders/1Nwus1Flq95s8f4tU2nvYF3vm6Z9EiRki?usp=drive_link",
    "cse 1102": "https://drive.google.com/drive/folders/16Qs8ajV75QjWUyy-fePz5n8VS34IAgQK?usp=drive_link",
    "cse 1107": "https://drive.google.com/drive/folders/1zatt_uYLr8Y62_TY3y3aVT_cU__bPCcf?usp=drive_link",
    "hum 1107": "https://drive.google.com/drive/folders/1CnkI72h1RqR1oWqXK5VNjEc46pSL4B6B?usp=drive_link",
    "hum 1108": "https://drive.google.com/drive/folders/10Y5E8uVjOpgGPveJzvQi-JtK3VKGCZLG?usp=drive_link",
    "math 1107": "https://drive.google.com/drive/folders/1mWBGKVckiM0xjgicMOSku1SJGJeAa180?usp=drive_link",
    "phy 1107": "https://drive.google.com/drive/folders/1HUKq6kJWDMJ4ZVH2Mk27chJqFlD4tr4x?usp=drive_link",
    "phy 1108": "https://drive.google.com/drive/folders/1SSXV1uuMmjrbiZYt1-bP1liaYDMKM8AW?usp=drive_link"
}

BOOK_LINKS = {
    "eee 2117": "https://drive.google.com/drive/folders/1czdKWfMfG4NpDSsLn9RexHYYzH6-ModY?usp=drive_link",
    "math 2107": "https://drive.google.com/drive/folders/13KzcqvqTDb91j4iDIDOrFic2FyHPf_70?usp=drive_link",
    "cse 2103": "https://drive.google.com/drive/folders/1FK9zboxo17eoOb0It6ssvaTGZIplv3Mi?usp=drive_link",
    "cse 2105": "https://drive.google.com/file/d/1VSYvBn0fxgO41vFg_U3QCtdQw5_rthr1/view?usp=drive_link",
    "cse 2113": "https://drive.google.com/drive/folders/1GYUqYbvfRz_0nL0myYrWyYLg5DmSP8WC?usp=drive_link",

    "cse 1203": "https://drive.google.com/drive/folders/1bcbAvCmNu2SG4P4NCNGwIEhsWM2-kZds?usp=drive_link",
    "cse 1205": "https://drive.google.com/drive/folders/1GCTjOF35eACFK107Z6bhJE_bZDOaL3bk?usp=drive_link",
    "eee 1207": "https://drive.google.com/drive/folders/1ZkYhZhYAocLsAfEvO6tobmIzNjRflNHP?usp=drive_link",
    "math 1207": "https://drive.google.com/drive/folders/191TR6QnvWqIlKpDVHFvxs7Ri05enAF_v?usp=drive_link",
    "chem 1207": "https://drive.google.com/drive/folders/1xQ1RB7lCo9WpQBEiRqcWNrqC8IkCNINu?usp=drive_link",

    "cse 1101": "https://drive.google.com/drive/folders/1OMGD0rsa5NNKHmXffVeU1EHH3WLdDDOF?usp=drive_link",
    "cse 1107": "https://drive.google.com/drive/folders/1kptldXIVJO4yq78H8nW-vznjkU8XVxZK?usp=drive_link",
    "phy 1107": "https://drive.google.com/drive/folders/1MJn4YIjby8enuTMCARznDlkpRkcfTi0Y?usp=drive_link",
    "hum 1107": "https://drive.google.com/drive/folders/1GobXPbNXiE9GUjWRNnyRNK9PwqJNd_kJ?usp=drive_link",
    "math 1107": "https://drive.google.com/drive/folders/1HmTDd-2V1GrWIUe35VtFpVTM60I37vHn?usp=drive_link"
}

# Note links
NOTE_LINKS = {
    "cse 2103": "https://drive.google.com/drive/folders/1_GySnwmo7MLlD7seSOSzLjVlCNY4A6yb?usp=drive_link",
    "cse 2105": "https://drive.google.com/drive/folders/1CuyCMDI2SLfBaGpDfF3f3f6EIcs5tR4g?usp=drive_link",
    "cse 2113": "https://drive.google.com/drive/folders/1IQgAqQn_khq7TwuIrrLTgdUvu5lEho1-?usp=drive_link",
    "eee 2117": "https://drive.google.com/drive/folders/1Oe9jFRJHXxj238oZFNPcjpp2GmSQIl37?usp=drive_link",
    "math 2107": "https://drive.google.com/drive/folders/1G5iD9zNfmR1cGBzZZt37JtL2XO_rxkwZ?usp=drive_link",

    "cse 1203": "https://drive.google.com/drive/folders/1xl9b9nN1XfFrHMT9T_QunrPu2Wc9cQ79?usp=drive_link",
    "cse 1205": "https://drive.google.com/drive/folders/1aQ2Eo_cD3R5pK_7-WmXlkb143SuYwRDT?usp=drive_link",
    "eee 1207": "https://drive.google.com/drive/folders/1XJX2PcaMHBEvUVbjmPNDt1QZ7IcZSJSc?usp=drive_link",
    "math 1207": "https://drive.google.com/drive/folders/1thI0Isq6Smfp-SZRHb7RTDSVKYpfMxJf?usp=drive_link",
    "chem 1207": "https://drive.google.com/drive/folders/1hL27BDMjqozt7jXkVskJUaRHWfLaUima?usp=drive_link",

    "cse 1101": "https://drive.google.com/drive/folders/1eoyHmJE08_n82KqDoDKe4ANzcDeTppv-?usp=drive_link",
    "cse 1107": "https://drive.google.com/drive/folders/191hiC1L0xEoN6auSY3abfyzbn79HNoQk?usp=drive_link",
    "phy 1107": "https://drive.google.com/drive/folders/1RdHz4DzaLzybBPzJ-n9o4_PxxLMpRB8_?usp=drive_link",
    "hum 1107": "https://drive.google.com/drive/folders/1ONc6ghsd31b7v42MBNAGHqDxZyRc1IQg?usp=drive_link",
    "math 1107": "https://drive.google.com/drive/folders/1KRBDGKGPxy074ngvE6RkF7vcwTNyxS6J?usp=drive_link"
}

# Solve links
SOLVE_LINKS = {
    "cse 2103": "https://drive.google.com/drive/folders/1tRju42ucszWvwqMCz7pOwuzHc-ly5lud?usp=drive_link",
    "cse 2105": "https://drive.google.com/drive/folders/1eigahpw_7QukVAa-jq6E9nT_uU-c6Qvr?usp=drive_link",
    "cse 2113": "https://drive.google.com/drive/folders/1wyiyTr2MpjaYh4AW2SgjXsbYnn74dxkj?usp=drive_link",
    "eee 2117": "https://drive.google.com/drive/folders/1dChMIZNLwDMsCgCvniNwrT-nOLXuXc-n?usp=drive_link",
    "math 2107": "https://drive.google.com/drive/folders/1xhqBaWNftWlGgZ_UmMJg7ZoVNA2yNmJO?usp=drive_link",

    "cse 1203": "https://drive.google.com/drive/folders/1kqQqSB1Pk5d8AfXU2faCfz3XwXw1DxkP?usp=drive_link",
    "cse 1205": "https://drive.google.com/drive/folders/1fFmsPjuw3gT3EVUQpE0LCWDVEgyxXNjQ?usp=drive_link",
    "eee 1207": "https://drive.google.com/file/d/1ETpBxuALRHnBnzBmzVJNRWwr9OyGe9L1/view?usp=drive_link",
    "math 1207": "https://drive.google.com/file/d/1EO0FvBBRE-GEUeo0rw01xzkzOt5I4KNw/view?usp=drive_link",
    "cse others": "https://drive.google.com/drive/folders/104Sbza1wJphFf9VhNOlwF_m1HQs5F4A_?usp=drive_link",

    "cse 1101": "https://drive.google.com/file/d/1yVCl-ofxiZlQcUl_y70jqPYZBuGOZWMD/view?usp=drive_link",
    "cse 1107": "https://drive.google.com/file/d/1oLTpPNTRHj53fBtxXdc4iU8CmDYfh5cx/view?usp=drive_link",
    "hum 1107": "https://drive.google.com/file/d/1chDrWcM2twsjedxDGku_uCWLFFzVt_4S/view?usp=drive_link",
    "phy 1107": "https://drive.google.com/file/d/19xbjxJgtxgcPr3dP4I6eIFzWkMQTDEoV/view?usp=drive_link",
    "math 1107": "https://drive.google.com/file/d/1oqmtlPaRFwd7NsHoOiHqfdlS5pz7L29E/view?usp=drive_link"
}

# Syllabus links
SYLLABUS_LINKS = {
    "cse 22": "https://drive.google.com/file/d/1dLxl8_eQv5g2LZKUhAT0bXCMbgWxdgJn/view?usp=drive_link"
}

# Routine links
ROUTINE_LINKS = {
    "cse routine 1-1": "https://drive.google.com/file/d/1lNiV5bI6hfqtxms-dFnzN7K5EgvkiX0v/view?usp=drive_link",
    "cse routine 1-2": "https://drive.google.com/file/d/1Z9Rkv9XDgK4ujwjzR6vyrVVxlwOf1BUM/view?usp=drive_link",
    "cse routine 2-1": "https://drive.google.com/file/d/15wVQrnjrpKly3Beq_0AP8za_VEGah9-x/view?usp=drive_link"
}

BOOKLET_LINKS = {
    "cse 22": "https://drive.google.com/file/d/1HjeIQRuzuibQdrWvXGtVyxL7n0LxCc3X/view?usp=drive_link"
}

# Batchmate links
BATCHMATE_LINKS = {
    "cse batchmates 22": "https://drive.google.com/drive/folders/1zqAeMAam0iBzoQSnKKOFHSB5JleA6mOs?usp=drive_link"
}

# /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the KUET CSE-22 Bot!\n\n"
        "➡️ Commands:\n"
        "- `cse 2-1 term <year>` — Get term questions\n"
        "- `cse 1-2 term <year>` — Get term questions\n"
        "- `cse 1-1 term <year>` — Get term questions\n"
        "- `cse slides <course>` — Get slides\n"
        "- `cse books <course>` — Get books\n"
        "- `cse notes <course>` — Get notes\n"
        "- `cse solves <course>` — Get solves\n"
        "- `cse routine <semester>` — Get class routine\n\n"
        "🎯 Examples:\n"
        "- `cse 2-1 term 2020`\n"
        "- `cse 1-2 term 2018`\n"
        "- `cse 1-1 term 2016`\n"
        "- `cse slides 1205`\n"
        "- `eee books 1207`\n"
        "- `math notes 1207`\n"
        "- `cse solves 1207`\n"
        "- `cse syllabus 22`\n"
        "- `cse batchmates 22`\n"
        "- `cse routine 2-1`\n"
        "- `cse booklet 22`",
        parse_mode="Markdown"
    )

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_command(update, context)

# /end
async def end_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤓 Thanks, hope to see you again!")

# Message handler
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    if any(g in text for g in ["hello", "hi", "hey", "salam", "adab", "assalamu alaikum"]):
        await update.message.reply_text("👋 Hey, Welcome to *CSE-2k22 bot*. How can I help you?", parse_mode="Markdown")
        return

    if any(w in text for w in ["how are you", "kamon aso", "ki obostha", "what's up"]):
        await update.message.reply_text("😊 All goes well, thanks. How can I help you?")
        return

    if any(w in text for w in ["thank", "dhonnobad", "dhonnobaad", "good bye", "bye", "bhalo theko", "valo thakis", "valo theko", "tnx"]):
        await update.message.reply_text("🌸 You are welcome for the further help.")
        return

  # Term questions
    if text.startswith("cse 2-1 term ") or text.startswith("cse 1-2 term ") or text.startswith("cse 1-1 term "):
        parts = text.split()
        if len(parts) == 4:
            key = f"{parts[1]} {parts[3]}"
            if key in QUESTION_LINKS:
                links = QUESTION_LINKS[key]
                response = f"📚 CSE {key.upper()} Term Questions:\n\n"
                for item in links:
                    response += f"📌 *{item['subject']}*\n🔗 [Open File]({item['link']})\n\n"
                await update.message.reply_text(response, parse_mode="Markdown", disable_web_page_preview=True)
            else:
                await update.message.reply_text("❌ No term questions found for that year.")
        else:
            await update.message.reply_text("❌ Invalid format. Try: `cse 1-2 term 2018`", parse_mode="Markdown")
        return

# Slides
    if "slides" in text:
        parts = text.split()
        if len(parts) >= 3:
            key = f"{parts[0]} {parts[2]}"
            if key in SLIDE_LINKS:
                await update.message.reply_text(
                    f"📂 Slides for *{key.upper()}*\n🔗 [Open Folder]({SLIDE_LINKS[key]})",
                    parse_mode="Markdown",
                    disable_web_page_preview=True
                )
                return
        await update.message.reply_text("❌ No slides found for that course.")
        return

  # Books
    if "books" in text:
        parts = text.split()
        if len(parts) >= 3:
            key = f"{parts[0]} {parts[2]}"
            if key in BOOK_LINKS:
                await update.message.reply_text(
                    f"📖 Books for *{key.upper()}*\n🔗 [Open Link]({BOOK_LINKS[key]})",
                    parse_mode="Markdown",
                    disable_web_page_preview=True
                )
                return
        await update.message.reply_text("❌ No books found for that course")
        return

    # Notes
    if "notes" in text:
        parts = text.split()
        if len(parts) >= 3:
            key = f"{parts[0]} {parts[2]}"
            if key in NOTE_LINKS:
                await update.message.reply_text(
                    f"📝 Notes for *{key.upper()}*\n🔗 [Open Folder]({NOTE_LINKS[key]})",
                    parse_mode="Markdown",
                    disable_web_page_preview=True
                )
                return
        await update.message.reply_text("❌ No notes found for that course.")
        return

    # Solves
    if "solves" in text:
        parts = text.split()
        if len(parts) >= 3:
            key = f"{parts[0]} {parts[2]}"
            if key in SOLVE_LINKS:
                await update.message.reply_text(
                    f"✅ Solves for *{key.upper()}*\n🔗 [Open Folder/File]({SOLVE_LINKS[key]})",
                    parse_mode="Markdown",
                    disable_web_page_preview=True
                )
                return
        await update.message.reply_text("❌ No solves found for that course.")
        return

  # Booklet
    if "booklet" in text:
        parts = text.split()
        if len(parts) >= 3:
            key = f"{parts[0]} {parts[2]}"
            if key in BOOKLET_LINKS:
                await update.message.reply_text(
                    f"📘 Booklet for *{key.upper()}*\n🔗 [Open File]({BOOKLET_LINKS[key]})",
                    parse_mode="Markdown",
                    disable_web_page_preview=True
                )
                return
        await update.message.reply_text("❌ No booklet found for that department.")
        return

        # Routine
    if "routine" in text:
        parts = text.split()
        if len(parts) >= 4:
            key = f"{parts[0]} {parts[1]} {parts[2]}"
        else:
            key = text
        if key in ROUTINE_LINKS:
            await update.message.reply_text(
                f"🗓️ Routine for *{key.upper()}*\n🔗 [Open File]({ROUTINE_LINKS[key]})",
                parse_mode="Markdown",
                disable_web_page_preview=True
            )
            return
        await update.message.reply_text("❌ No routine found for that semester.")
        return

        # Batchmates
    if "batchmates" in text:
        parts = text.split()
        if len(parts) >= 3:
            key = f"{parts[0]} {parts[1]} {parts[2]}"
            if key in BATCHMATE_LINKS:
                await update.message.reply_text(
                    f"👥 Batchmates for *{key.upper()}*\n🔗 [Open File]({BATCHMATE_LINKS[key]})",
                    parse_mode="Markdown",
                    disable_web_page_preview=True
                )
                return
        await update.message.reply_text("❌ No batchmate list found for that batch.")
        return

    # Syllabus
    if "syllabus" in text:
        parts = text.split()
        if len(parts) >= 3:
            key = f"{parts[0]} {parts[2]}"
            if key in SYLLABUS_LINKS:
                await update.message.reply_text(
                    f"📘 Syllabus for *{key.upper()}*\n🔗 [Open File]({SYLLABUS_LINKS[key]})",
                    parse_mode="Markdown",
                    disable_web_page_preview=True
                )
                return
        await update.message.reply_text("❌ No syllabus found for that entry.")
        return

     # Fallback response
    await update.message.reply_text("😟 Sorry, I don't understand what you write! Please press /help for further information.")

# error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')

# main
if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('end', end_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=0.5)
