def verseny():
    okt = [0, 12, 13, 9, 2, 7] # 4. és 5. nap
    i = 1

    while i < len(okt):
        if okt[i - 1] - 3 >= okt[i]:
            print(f"Október {i+1}-án napon csökkent")
        i += 1
