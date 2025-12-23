from typing import List, Dict, Tuple


UPPERCASE_DATA = {
    "A": ("1415926535", "1010100011001010101001100000111000011101"),
    "B": ("8410270193", "1111010011010010000001000010010110001111"),
    "C": ("6659334461", "1100011001110110101100001001111010000101"),
    "Ç": ("8979323846", "1000010111001101011001101111000110011101"),
    "D": ("2847564823", "1010100110111010011001000001011100000101"),
    "E": ("2643383279", "1001110110001110110100111110111100001101"),
    "F": ("8521105559", "1111110111110010111000000100101110000101"),
    "G": ("6446229489", "1100000000011100110100111111100010111101"),
    "Ğ": ("5028841971", "1001010111011111000001001111100110011101"),
    "H": ("8467481846", "1111110001011001110000100111101100011101"),
    "I": ("6939937510", "1100111011010011100001010111001100001101"),
    "İ": ("5493038196", "1010001110110100100011100011101000000101"),
    "J": ("4428810975", "1000000111111110100100101010110111110101"),
    "K": ("5820974944", "1010110101111010100000111011000000011101"),
    "L": ("4543266482", "1000011101100110010111110101100100000101"),
    "M": ("1339360726", "1011000010000101100000000000101000000101"),
    "N": ("249141273", "1001111111010101000001011101011000001101"),
    "O": ("628620899", "1110110110011001100110000001100100011101"),
    "Ö": ("6094370277", "1100111011010011100001010111001100111101"),
    "P": ("3421170679", "1011010110100000010110101111001010000101"),
    "R": ("3786783165", "1100101111101010111010111111011100001101"),
    "S": ("2712019091", "1110000110110101101110011011110100000101"),
    "Ş": ("8214808651", "1010000110100110001000001001001100000101"),
    "T": ("1907021798", "1111010011010010000001000010010110001101"),
    "U": ("3282306647", "1110001101010101101011111100110000000101"),
    "Ü": ("6395224737", "1100001110100100000001100101011100000101"),
    "V": ("938446095", "1011111010010111100100110101000010001101"),
    "Y": ("539217176", "1101111110111110001101000011110000000101"),
    "Z": ("2931767523", "1000000010000111100110100011000000111101"),
    "Q": ("639217478", "1000000010000111100110100011011111111111"),
    "W": ("739207279", "1001000010000111100110100011000111111111"),
    "X": ("839217376", "1001000010000111100110100011000100111111"),
}


LOWERCASE_DATA = {
    "a": ("5058223172", "1010111010111111001100001110001100000101"),
    "b": ("8602139494", "1001011010111111001011100010001000001101"),
    "c": ("5359408128", "1000000000101110100011101101100110000101"),
    "ç": ("4564856692", "1001111110111001000010100000000011111101"),
    "d": ("3460348610", "1000100000001011000101111011101000000101"),
    "e": ("4811174502", "1100111001000000101110101100001000000101"),
    "f": ("7245870066", "1000111101100010010110010011001100000101"),
    "g": ("631558817", "1101011111110001100110011111100100001101"),
    "ğ": ("4881520920", "1001011010010011010010101000010000011101"),
    "h": ("9628292540", "1001000101111011000011001000110000001101"),
    "ı": ("9171536436", "1000111101111001000001010110111100000101"),
    "i": ("7892590360", "1000100010101010101000101000110100011101"),
    "j": ("113305305", "1110101100110111101011111000110000000101"),
    "k": ("4882046652", "1101100000011100110110110010000000001101"),
    "l": ("1384146951", "1001000101111111000011110101111000001101"),
    "m": ("1384146951", "1010010100000000110100000000011100001101"),
    "n": ("9415116094", "1000110001001011110100010100111110000101"),
    "o": ("3305727036", "1100010100001001011001000011110000001101"),
    "ö": ("5759591953", "1010101110100110001100110000100010000101"),
    "p": ("921861173", "1101101111001001111100001101010011111101"),
    "r": ("8193261179", "1111010000101101100111110011110110001101"),
    "s": ("3105118548", "1011100100010100010110010101010000000101"),
    "ş": ("744623799", "1011000110001000001110101101110000000101"),
    "t": ("6274956735", "1011101101110111111011111111110000001101"),
    "u": ("1885752724", "1110000011001100100110110010100000000101"),
    "ü": ("8912279381", "1000010001100110110100100101110101010101"),
    "v": ("8301194912", "1110111011001010001011101010000000001101"),
    "y": ("9833673362", "1001001010001000011111001010010010000101"),
    "z": ("4406566430", "1000000110101001101101111000011110000101"),
    "q": ("9406566432", "1101110010111110111111010111110100110111"),
    "w": ("7406566433", "1001110010111110111111010111110111000111"),
    "x": ("8406566439", "1011110010111110111111111111110100000111"),
}

DIGIT_DATA= {
"0": ("5256375678", "1001110010111110111111010111110100000101"),
    "1": ("0560010165", "1000010101001111010010000101000000111101"),
    "2": ("9596881592", "1000111010111110110001110111000001111101"),
    "3": ("6999892256", "1101000010111110010110110000000000111101"),
    "4": ("4610126483", "1000100100111111010110110011000000111101"),
    "5": ("2498872758", "1001010100110001010110100110000000000101"),
    "6": ("0657922955", "1001110011110100110110111011000010101101"),
    "7": ("9276457931", "1000101001110110110000011111011010101101"),
    "8": ("3742880210", "1101111011100110000001110010111000110101"),
    "9": ("2645600162", "1001110111111110110001010010000000111101"),
}

SPECIAL_DATA = {
    "(": ("1409387001", "1010011110110110110010111001000000111101"),
    ")": ("0704691209", "1010100000100010100101111001000000011101"),
    "/": ("5394590944", "1010000011110110111011010000000000001101"),
    "%": ("4035998953", "1111000001110000100101111001000000000101"),
    "+": ("2162484391", "1000000010100110110010111111000001101101"),
    "-": ("3852371065", "1011111010100010111010111111011011001111"),
    "&": ("9240190273", "1000100110111100011011011001000001110101"),
    "=": ("2651341055", "1001111000100010111010111111000011001101"),
    "?": ("0724522563", "1010101000110000111111010011000000000101"),
    ":": ("6723585020", "1100100001110011110011011100000001010101"),
    ".": ("5020141020", "1001010110111010111010110100000011100101"),
    ";": ("8344086973", "1111100011110100110011011101111110000101"),
    ",": ("2205750596", "1000001111110100000100100100000000111101"),
    "'": ("8759756975", "1110101001110001111111110111110000111111"),
    "!": ("6789766974", "1100101000000001111111110111110000111101"),
    " ": ("0000000000", "0000000000000000000000000000000010000001"),  
}

ALL_CHARACTERS = {**UPPERCASE_DATA, **LOWERCASE_DATA, **DIGIT_DATA, **SPECIAL_DATA}

def char_to_binary(char: str) -> Tuple[str, str, str]:
    """
    Bir karakteri 40-bit binary'ye çevirmek için kullanacağız.
    
    Args:
        char: Dönüştürülecek karakter olcak.
        
    Returns:
        (karakter, pi_kesiti, binary) tuple'ı
        Karakter bulunamazsa None döncek.
    """
    if char in ALL_CHARACTERS:
        pi_segment, binary = ALL_CHARACTERS[char]
        return (char, pi_segment, binary)
    else:
        return (char, "BULUNAMADI", "?" * 40)


def text_to_binary(text: str) -> List[Tuple[str, str, str]]:
    """
    Bir metni 40-bit binary'lere çevir
    
    Args:
        text: Dönüştürülecek metin
        
    Returns:
        Her karakter için tuple listesi
    """
    results = []
    for char in text:
        results.append(char_to_binary(char))
    return results


def get_full_binary_string(text: str) -> str:
    """
    Metnin tüm karakterlerinin binary karşılıklarını birleştirmek için.
    
    Args:
        text: Dönüştürülecek metin
        
    Returns:
        Tüm karakterlerin binarylerinin birleştirilmiş hali
    """
    results = text_to_binary(text)
    return "".join([binary for _, _, binary in results if "?" not in binary])


def binary_to_text(binary_string: str) -> str:
    """
    40-bit binary bloklarını tekrar metne çevir
    
    Args:
        binary_string: 40-bit bloklar halinde binary string
        
    Returns:
        Çözülmüş metin
    """
    if len(binary_string) % 40 != 0:
        return "HATA: Binary uzunluğu 40'ın katı olmalı!"
    
    binary_to_char_map = {}
    for char, (_, binary) in ALL_CHARACTERS.items():
        binary_to_char_map[binary] = char
    
    result = ""
    for i in range(0, len(binary_string), 40):
        block = binary_string[i:i+40]
        if block in binary_to_char_map:
            result += binary_to_char_map[block]
        else:
            result += "?"
    
    return result

#display fonksiyonları 
def display_conversion_result(text: str):
    """Dönüşüm sonucunu güzel bir formatta göster"""
    
    print(f"\n{'='*75}")
    print(f"📝 GİRİLEN METİN: '{text}'")
    print(f"{'='*75}")
    
    results = text_to_binary(text)
    
    print(f"\n{'─'*75}")
    print(f"{'Karakter':<10} {'Pi Kesiti':<15} {'40-Bit Binary'}")
    print(f"{'─'*75}")
    
    for char, pi_segment, binary in results:
        display_char = "' '" if char == " " else f"'{char}'"
        if "?" in binary:
            print(f"{display_char:<10} {pi_segment:<15} {binary} ⚠️")
        else:
            print(f"{display_char:<10} {pi_segment:<15} {binary}")
    
    print(f"{'─'*75}")
    
    # binary özet
    full_binary = get_full_binary_string(text)
    total_bits = len(full_binary)
    
    print(f"\n📊 ÖZET:")
    print(f"   • Toplam karakter: {len(text)}")
    print(f"   • Toplam bit: {total_bits}")
    print(f"   • Byte sayısı: {total_bits // 8} byte + {total_bits % 8} bit")
    
    print(f"\n🔐 BİRLEŞİK BINARY ({total_bits} bit):")
    print(f"{'─'*75}")
    
    # 76 karakterlik satırlara böl
    for i in range(0, len(full_binary), 76):
        print(f"   {full_binary[i:i+76]}")
    
    print(f"{'─'*75}")


def display_character_table():
    """Tüm karakter tablosunu göster"""
    
    print(f"\n{'='*75}")
    print(f"📋 TÜM KARAKTER TABLOSU")
    print(f"{'='*75}")
    
    print(f"\n🔤 BÜYÜK HARFLER ({len(UPPERCASE_DATA)} adet):")
    print(f"{'─'*75}")
    for char, (pi_seg, binary) in sorted(UPPERCASE_DATA.items()):
        print(f"   {char}  →  Pi: {pi_seg:<12}  Binary: {binary}")
    
    print(f"\n🔡 KÜÇÜK HARFLER ({len(LOWERCASE_DATA)} adet):")
    print(f"{'─'*75}")
    for char, (pi_seg, binary) in sorted(LOWERCASE_DATA.items()):
        print(f"   {char}  →  Pi: {pi_seg:<12}  Binary: {binary}")
    
    print(f"\n🔢 RAKAMLAR ({len(DIGIT_DATA)} adet):")
    print(f"{'─'*75}")
    for char, (pi_seg, binary) in sorted(DIGIT_DATA.items()):
        print(f"   {char}  →  Pi: {pi_seg:<12}  Binary: {binary}")
    
    print(f"\n✨ ÖZEL KARAKTERLER ({len(SPECIAL_DATA)} adet):")
    print(f"{'─'*75}")
    for char, (pi_seg, binary) in SPECIAL_DATA.items():
        display_char = "BOŞLUK" if char == " " else char
        print(f"   {display_char:<6}  →  Pi: {pi_seg:<12}  Binary: {binary}")


# ANA MENÜ

def interactive_menu():
    """Ana menü"""
    
    print("\n" + "="*75)
    print("🔢 Pİ SAYISINDAKİ GİZLİ BİLGİLER - ŞİFRELEME SİSTEMİ")
    print("="*75)
    print("""
Bu program, Pi sayısının rakamlarını kullanarak gelişmiş bir
şifreleme algoritması sunar. Özellikler:

  • 40-bit binary kodlama
  • Türkçe karakter desteği (ç, ğ, ı, ö, ş, ü)
  • Pi kesiti eşleştirmesi
  • Harf, kelime veya cümle dönüştürme
""")
    
    while True:
        print("\n" + "─"*50)
        print("MENÜ:")
        print("  1 - Metin → Binary Dönüştür")
        print("  2 - Binary → Metin Çöz")
        print("  3 - Karakter Tablosunu Göster")
        print("  4 - Tek Karakter Sorgula")
        print("  0 - Çıkış")
        print("─"*50)
        
        choice = input("\nSeçiminiz: ").strip()
        
        if choice == "1":
            print("\n" + "─"*50)
            text = input("📝 Dönüştürülecek metin girin (harf/kelime/cümle): ")
            
            if not text:
                print("❌ Boş metin girilemez!")
                continue
            
            display_conversion_result(text)
            
        elif choice == "2":
            print("\n" + "─"*50)
            print("📝 40-bit binary blokları girin (bitince boş satır):")
            
            lines = []
            while True:
                line = input().strip()
                if not line:
                    break
                lines.append(line)
            
            binary_input = "".join(lines).replace(" ", "")
            
            if not binary_input:
                print("❌ Boş veri girilemez!")
                continue
            
            if any(c not in "01" for c in binary_input):
                print("❌ Geçersiz karakter! Sadece 0 ve 1 kullanın.")
                continue
            
            if len(binary_input) % 40 != 0:
                print(f"❌ Geçersiz uzunluk! {len(binary_input)} bit girildi.")
                print(f"   Uzunluk 40'ın katı olmalı (40, 80, 120, ...).")
                continue
            
            decoded_text = binary_to_text(binary_input)
            print(f"\n✅ Çözülen metin: '{decoded_text}'")
            
        elif choice == "3":
            display_character_table()
            
        elif choice == "4":
            char = input("\n🔍 Sorgulanacak karakter: ")
            
            if len(char) != 1:
                print("❌ Lütfen tek bir karakter girin!")
                continue
            
            result = char_to_binary(char)
            char_display, pi_seg, binary = result
            
            print(f"\n{'─'*50}")
            if "?" not in binary:
                print(f"   Karakter : '{char_display}'")
                print(f"   Pi Kesiti: {pi_seg}")
                print(f"   Binary   : {binary}")
            else:
                print(f"   ⚠️ '{char}' karakteri tabloda bulunamadı!")
            print(f"{'─'*50}")
            
        elif choice == "0":
            print("\n👋 Programdan çıkılıyor...")
            break
            
        else:
            print("❌ Geçersiz seçim! Lütfen 0-4 arası bir değer girin.")


# HIZLI DÖNÜŞÜM FONKSİYONLARI (Import için)

def convert(text: str) -> str:
    """
    Hızlı dönüşüm fonksiyonu - metni binary'ye çevirir
    
    Örnek kullanım:
        from binary_new import convert
        binary = convert("Merhaba")
    """
    return get_full_binary_string(text)


def decode(binary_string: str) -> str:
    """
    Hızlı çözme fonksiyonu - binary'yi metne çevirir
    
    Örnek kullanım:
        from binary_new import decode
        text = decode("10101000110010101010011000001110000111...")
    """
    return binary_to_text(binary_string)

#main program
if __name__ == "__main__":
    interactive_menu()

