import pyautogui,time

msg = input("Enter the message: ")
a = input("How many times ?: ")
t = input("how many seconds between each message: ")


for i in range(1, 6):
    print(i)
    i + 1
    time.sleep(1)

print("SPAM")

for i in range(0,int(a)):
    pyautogui.typewrite(msg + '\n')
    time.sleep(float(t))

print("Done!")
