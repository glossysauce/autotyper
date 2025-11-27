import time
import random
import pyautogui

ERROR_RATE = 0.05 #probability char gets mistyped 
MIN_DELAY = 0.0001 
MAX_DELAY = 0.001

#qwerty keyb map
KEY_NEIGHBORS = {
    'q': "was",
    'w': "qase",
    'e': "wsdr",
    'r': "edft",
    't': "rfgy",
    'y': "tghu",
    'u': "yhjI",
    'i': "uokj",
    'o': "ipkl", 
    'p': "ol",
    'a': "qwsxz",
    's': "qwedxza",
    'd': "serfcx",
    'f': "drtgv",
    'g': "ftyhbv",
    'h': "gyujnb",
    'j': "huikmn",
    'k': "jilm",
    'l': "kop",
    'z': "asx",
    'x': "zsdc",
    'c': "xdfv",
    'v': "cfgb",
    'b': "vghn",
    'n': "bhjm",
    'm': "njk",
}

def human_type(text, error_rate=ERROR_RATE,
               min_delay=MIN_DELAY, max_delay=MAX_DELAY):
    """this will text with randomized timings and occasional common, human typos."""
    for ch in text:
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
        if ch == "\n":
            pyautogui.press("enter")
            continue
        if ch == "\t":
            pyautogui.press("tab")
            continue

        lower = ch.lower()
        can_mistype = lower in KEY_NEIGHBORS and lower.isalpha()

        if can_mistype and random.random() < error_rate:
            # pick a neighboring "wrong" key
            wrong_lower = random.choice(KEY_NEIGHBORS[lower])
            wrong = wrong_lower.upper() if ch.isupper() else wrong_lower
            pyautogui.write(wrong)
            time.sleep(random.uniform(min_delay / 2, min_delay))
            pyautogui.press("backspace")

        pyautogui.write(ch)


def main():
    print("paste text")
    text = input("> ")

    print("text will be autotyped in 5 seconds")
    time.sleep(5)
    human_type(text)

if __name__ == "__main__":
    main()