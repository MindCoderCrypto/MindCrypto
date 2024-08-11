import subprocess
def max_limit(max):
    step = 1
    check = 0
    check2 = 1

    while check != check2:
        max = check
        check = check2
        check2 = check2 + step
        step *= 1.3

    while max + step != max:
        if max + step == check:
            step *= 0.5
        else:
            max += step
    return max


def min_limit(min):
    step = 1

    while min - step != min:
        if min - step <= 0:
            step *= 0.5
        else:
            min -= step
    return min

def Update_number():
    subprocess.call('./assets/data/project_4_eod/data/eod-quotemedia/diccs/daily_quietes/id/CryptoAIUpdater.exe')