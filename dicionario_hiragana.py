import random

# Hiragana completo com variações
hiragana = {
    # Vogais
    "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
    # K
    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
    # Dakuten (G)
    "ga": "が", "gi": "ぎ", "gu": "ぐ", "ge": "げ", "go": "ご",
    # S
    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
    # Dakuten (Z)
    "za": "ざ", "ji": "じ", "zu": "ず", "ze": "ぜ", "zo": "ぞ",
    # T
    "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
    # Dakuten (D)
    "da": "だ", "di": "ぢ", "du": "づ", "de": "で", "do": "ど",
    # N
    "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
    # H
    "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
    # Dakuten (B)
    "ba": "ば", "bi": "び", "bu": "ぶ", "be": "べ", "bo": "ぼ",
    # Handakuten (P)
    "pa": "ぱ", "pi": "ぴ", "pu": "ぷ", "pe": "ぺ", "po": "ぽ",
    # M
    "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
    # Y
    "ya": "や", "yu": "ゆ", "yo": "よ",
    # R
    "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
    # W
    "wa": "わ", "wo": "を",
    # N
    "n": "ん",
    # Combinações com pequenos ゃ ゅ ょ (yōon)
    "kya": "きゃ", "kyu": "きゅ", "kyo": "きょ",
    "gya": "ぎゃ", "gyu": "ぎゅ", "gyo": "ぎょ",
    "sha": "しゃ", "shu": "しゅ", "sho": "しょ",
    "ja": "じゃ", "ju": "じゅ", "jo": "じょ",
    "cha": "ちゃ", "chu": "ちゅ", "cho": "ちょ",
    "nya": "にゃ", "nyu": "にゅ", "nyo": "にょ",
    "hya": "ひゃ", "hyu": "ひゅ", "hyo": "ひょ",
    "bya": "びゃ", "byu": "びゅ", "byo": "びょ",
    "pya": "ぴゃ", "pyu": "ぴゅ", "pyo": "ぴょ",
    "mya": "みゃ", "myu": "みゅ", "myo": "みょ",
    "rya": "りゃ", "ryu": "りゅ", "ryo": "りょ"
}

###################################

tentativas = 0
# Sorteia um par romaji/hiragana
romaji, kana = random.choice(list(hiragana.items()))

while tentativas < 5:
    # Mostra o hiragana para o usuário
    print(f"Qual é o romaji deste hiragana: {kana} ?")

    # Recebe resposta
    resposta = input("Digite sua resposta: ").strip().lower()

    # Verifica
    if resposta == romaji:
        print("✅ Correto!")
        break
    elif resposta != romaji and tentativas <4:
        tentativas += 1
        print('ERRADO! Tente novamente!')
    elif resposta != romaji and tentativas == 4:
        tentativas += 1
        print(f"❌ Errado! O correto é '{romaji}'.")
