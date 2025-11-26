import time
import pyautogui

def main():
    # extract text
    print("paste text")
    text = input("> ")

    print("text will be autotyped in 5 seconds")
    time.sleep(5)

#interval = time (s) between chars
    pyautogui.write(text, interval=0.06)

if __name__ == "__main__":
    main()