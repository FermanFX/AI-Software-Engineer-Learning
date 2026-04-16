import easygui

def captureText():
    text = []
    print('\n--- Mətni bura daxil edin. Bitirmək üçün son sətirə # işarəsi qoyun ---\n')
    while True:
        line = input()
        to_write = line.replace('#', '')
        text.append(to_write)
        if '#' in line:
            break
    return text

def readText(filename):
    list_of_strings = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            line = f.read()
            list_of_strings.append(line.strip())
    except Exception as e:
        print(f"Xəta baş verdi: {e}")
    return list_of_strings

def writeText(list_of_strings, mode='w', filename=''):
    if not filename:
        filename = easygui.filesavebox(default="untitled.txt", filetypes=["*.txt"])
    
    if filename: # Əgər istifadəçi fayl seçməkdən imtina etməyibsə
        with open(filename, mode, encoding='utf-8') as f:
            for line in list_of_strings:
                f.write(line + '\n')
        print(f"Məlumat '{filename}' faylına yazıldı.")

def showText():
    filename = easygui.fileopenbox(filetypes=["*.txt"])
    if filename:
        list_of_strings = readText(filename)
        print('\n## Sizin mətniniz ##\n')
        for line in list_of_strings:
            print(line)
        return filename
    return None

def menu():
    print('\n--- MENYU ---')
    print('1 - Yeni mətn (Yazmaq)')
    print('2 - Mətni oxu')
    print('3 - Mətnə əlavə et')
    print('q - Çıxış')
    opt = input("Seçiminizi daxil edin: ").lower()
    
    if opt == '1': return 'w'
    elif opt == '2': return 'r'
    elif opt == '3': return 'a'
    elif opt == 'q': return 'quit'
    return None

def main():
    while True:
        filename = ''
        mode = menu()
        
        if mode == 'quit':
            print("Proqramdan çıxılır...")
            break
            
        if mode is None:
            print("Yanlış seçim! Yenidən yoxlayın.")
            continue

        if mode == 'r' or mode == 'a':
            filename = showText()
            if not filename and mode == 'r':
                continue

        if mode == 'w' or mode == 'a':
            text = captureText()
            writeText(text, mode, filename)
        
        opt = input('\nNövbəti əməliyyat? [y/n]: ').lower()
        if opt == 'n':
            print("Sağ olun!")
            break

if __name__ == "__main__":
    main()
