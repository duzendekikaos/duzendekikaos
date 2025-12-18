"""
Düzendeki Kaos - Şifreleme Sistemi
Streamlit arayüzü (localhostta çalışıyor)
"""

import streamlit as st
from duzendekikaos_binary import (
    text_to_binary, binary_to_text, get_full_binary_string,char_to_binary,
    ALL_CHARACTERS,UPPERCASE_DATA,LOWERCASE_DATA,DIGIT_DATA,SPECIAL_DATA
)

#sayfa ayarları
st.set_page_config(
    page_title="Şifreleme Sistemi - Düzendeki Kaos",page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 
st.markdown("""
<style>
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes binaryFlow {
        0% { background-position: 0% 0%; }
        100% { background-position: 100% 100%; }
    }
    
    .main-header {
        position: relative;
        background: linear-gradient(135deg, #0077b6 0%, #00b4d8 50%, #48cae4 100%);padding: 3rem 2rem;border-radius: 24px;color: white;text-align: center;margin-bottom: 2rem;
        box-shadow: 
            0 25px 50px -12px rgba(0, 119, 182, 0.4),
            0 0 0 1px rgba(255, 255, 255, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            0 10px 40px rgba(0, 180, 216, 0.3),
            0 0 100px rgba(72, 202, 228, 0.2);
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .main-header::before {
        content: "01001000 01100101 01101100 00100000 01010000 01101001 00100000 00110001 00110100 01101001 00110101 10010010 01100101 01110010 11101001 01001110 00100000 01101111 01110010 01101100 01100100 00100001 00100001 10101010 01010101 11001100 00110011 01110111 00011100 10101010 01010101 11110000 00001111 10011001 01100110 01011010 10100101 11100001 00011110 01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100 00100001 00100001 10101010 01010101 11001100";
        position: absolute;top: 0;left: 0;right: 0;bottom: 0;
        font-family: 'Courier New', monospace;font-size: 14px;
        color: rgba(102, 126, 234, 0.15);
        word-wrap: break-word;
        line-height: 1.8;padding: 10px;
        pointer-events: none;
        animation: binaryFlow 20s linear infinite;
        letter-spacing: 3px;
    }
    
    .main-header::after {
        content: "";position: absolute;top: 0;left: 0;right: 0;bottom: 0;
        background: radial-gradient(ellipse at center, transparent 0%, rgba(15, 12, 41, 0.8) 70%);
        pointer-events: none;
    }
    
    .header-content {
        position: relative;
        z-index: 10;
    }
    
.main-header h1 {
        margin: 0;
        font-size: 3rem;
        font-weight: 800;
        text-shadow: 
            0 0 20px rgba(102, 126, 234, 0.8),
            0 0 40px rgba(102, 126, 234, 0.4),
            0 4px 8px rgba(0, 0, 0, 0.3);
        letter-spacing: 2px;
        animation: float 3s ease-in-out infinite;
    }
    
.main-header p {margin: 1rem 0 0 0;opacity: 0.9;font-size: 1.1rem;font-weight: 300;
text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);letter-spacing: 1px;}
    
    .header-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0.4rem 1.2rem;
        border-radius: 50px;
        font-size: 0.85rem;
        margin-top: 1rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .result-box {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(102, 126, 234, 0.3);
        color: #00d4ff;
        font-family: 'Courier New', monospace;
        word-break: break-all;
        margin: 1rem 0;
        box-shadow: 
            inset 0 2px 10px rgba(0, 0, 0, 0.3),
            0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .char-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
    }
    
    .stats-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #f0f2f6;
        border-radius: 8px;
        padding: 10px 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Ana başlık
st.markdown("""
<div class="main-header">
    <div class="header-content">
        <h1> Şifreleme Sistemi - Düzendeki Kaos</h1>
        <p>40-bit binary şifreleme</p>
    </div>
</div>
""", unsafe_allow_html=True)

# sidebar
with st.sidebar:
    st.markdown("### 📊 Sistem Bilgisi")
    st.info(f"""
    **Desteklenen Karakterler:**
    - Büyük harfler: {len(UPPERCASE_DATA)}
    - Küçük harfler: {len(LOWERCASE_DATA)}
    - Rakamlar: {len(DIGIT_DATA)}
    - Özel karakterler: {len(SPECIAL_DATA)}
    
    **Toplam:** {len(ALL_CHARACTERS)} karakter
    """)
    
    st.markdown("---")
    st.markdown("### ℹ️ Şifreleme Sistemi Nasıl Çalışır?")
    st.markdown("""
    1. Her karakter Pi sayısından bir kesit ile eşleştirilir.
    2. Bu kesit 40-bit binary'ye dönüştürülür.
    3. Şifreleme ve çözme işlemleri bu tabloya göre yapılır.
    """)

# sekmeler(ana)
tab1, tab2, tab3, tab4 = st.tabs(["🔐 Şifrele", "🔓 Çöz", "📋 Karakter Tablosu", "🔍 Tek Karakter"])

# bölüm 1: Şifreleme
with tab1:
    st.markdown("### 📝 Metin → Binary Dönüştürme")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        input_text = st.text_area(
            "Şifrelenecek metin:",
            placeholder="Buraya metin girin (harf, kelime veya cümle)...",
            height=150,
            key="encrypt_input"
        )
        
        encrypt_btn = st.button("🔐 Şifrele", type="primary", use_container_width=True)
    
    if encrypt_btn and input_text:
        with col2:
            with st.spinner("Şifreleniyor..."):
                results = text_to_binary(input_text)
                full_binary = get_full_binary_string(input_text)
                
                # İstatistikler
                st.markdown("#### 📊 İstatistikler")
                stat_cols = st.columns(3)
                with stat_cols[0]:
                    st.metric("Karakter Sayısı", len(input_text))
                with stat_cols[1]:
                    st.metric("Toplam Bit", len(full_binary))
                with stat_cols[2]:
                    st.metric("Byte", f"{len(full_binary) // 8} + {len(full_binary) % 8} bit")
        
        # sonuçlar için
        st.markdown("---")
        st.markdown("#### 📋 Karakter Detayları")
        
        for char, pi_segment, binary in results:
            display_char = "BOŞLUK" if char == " " else char
            status = "" if "?" not in binary else "⚠️"
            
            with st.expander(f"{status} '{display_char}'", expanded=False):
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown(f"**Pi Kesiti:** `{pi_segment}`")
                with col_b:
                    st.markdown(f"**Binary:** `{binary}`")
        
        # birleşik binary
        st.markdown("---")
        st.markdown("#### 🔐 Birleşik Binary Çıktı")
        st.markdown(f'<div class="result-box">{full_binary}</div>', unsafe_allow_html=True)
        
        #kopyalamak için buton (sağ altta)
        st.code(full_binary, language=None)
        
    elif encrypt_btn:
        st.warning("⚠️ Lütfen şifrelenecek metin girin!")

# bölüm 2: Çözüm kısmı
with tab2:
    st.markdown("### 🔓 Binary → Metin Çözme")
    
    binary_input = st.text_area(
        "Çözülecek binary:",
        placeholder="40-bit binary blokları girin (örn: 1010100011001010101001100000111000011101...)",
        height=150,
        key="decrypt_input"
    )
    
    decrypt_btn = st.button("🔓 Çöz", type="primary", use_container_width=True)
    
    if decrypt_btn and binary_input:
        # Temizle
        clean_binary = binary_input.replace(" ", "").replace("\n", "").strip()
        
        # Doğrulama
        if any(c not in "01" for c in clean_binary):
            st.error("❌ Geçersiz karakter! Sadece 0 ve 1 kullanın.")
        elif len(clean_binary) % 40 != 0:
            st.error(f"❌ Geçersiz uzunluk! {len(clean_binary)} bit girildi. Uzunluk 40'ın katı olmalı.")
            st.info(f"💡 İpucu: {40 - (len(clean_binary) % 40)} bit daha ekleyin veya {len(clean_binary) % 40} bit çıkarın.")
        else:
            decoded = binary_to_text(clean_binary)
            
            st.success("✅ Çözme başarılı!")
            
            st.markdown("#### 📝 Çözülen Metin:")
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                        padding: 2rem; border-radius: 15px; color: white; 
                        font-size: 1.5rem; text-align: center; margin: 1rem 0;">
                {decoded}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"**Karakter sayısı:** {len(decoded)}")
            
    elif decrypt_btn:
        st.warning("⚠️ Lütfen çözülecek binary girin!")

# bölüm3: Karakter Tablosu
with tab3:
    st.markdown("### 📋 Tüm Karakter Tablosu")
    
    table_type = st.selectbox(
        "Kategori seçin:",
        ["Tümü", "Büyük Harfler", "Küçük Harfler", "Rakamlar", "Özel Karakterler"]
    )
    
    if table_type == "Büyük Harfler":
        data = UPPERCASE_DATA
    elif table_type == "Küçük Harfler":
        data = LOWERCASE_DATA
    elif table_type == "Rakamlar":
        data = DIGIT_DATA
    elif table_type == "Özel Karakterler":
        data = SPECIAL_DATA
    else:
        data = ALL_CHARACTERS
    
    # Tablo oluştur
    table_data = []
    for char, (pi_seg, binary) in data.items():
        display_char = "BOŞLUK" if char == " " else char
        table_data.append({
            "Karakter": display_char,
            "Pi Kesiti": pi_seg,
            "40-Bit Binary": binary
        })
    
    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True
    )
    
    st.info(f"📊 Toplam {len(data)} karakter gösteriliyor.")

# TAB 4: Tek Karakter Sorgulama
with tab4:
    st.markdown("### 🔍 Tek Karakter Sorgulama")
    
    single_char = st.text_input(
        "Sorgulanacak karakter:",
        max_chars=1,
        placeholder="Tek bir karakter girin..."
    )
    
    if single_char:
        char_result = char_to_binary(single_char)
        char_display, pi_seg, binary = char_result
        
        if "?" not in binary:
            st.success(f"✅ '{char_display}' karakteri bulundu!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🥧 Pi Kesiti")
                st.markdown(f"""
                <div style="background: #f0f2f6;padding: 1.5rem;border-radius: 10px; 
                            font-family: monospace; font-size: 1.5rem; text-align: center;">
                    {pi_seg}
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### 💻 40-Bit Binary")
                st.markdown(f"""
                <div style="background: #1a1a2e; padding: 1.5rem; border-radius: 10px; 
                            font-family: monospace; font-size: 1rem; text-align: center; color: #e94560;">
                    {binary}
                </div>
                """, unsafe_allow_html=True)
            
            # Binary görselleştirme
            st.markdown("#### 📊 Binary Görselleştirme")
            binary_visual = " ".join([binary[i:i+8] for i in range(0, len(binary), 8)])
            st.code(binary_visual)
            
            # ÇÖZ butonu
            st.markdown("---")
            if st.button("🔓 ÇÖZ", type="primary", use_container_width=True, key="decode_single"):
                decoded = binary_to_text(binary)
                st.markdown("#### 🔓 Çözüm Sonucu")
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                            padding: 2rem; border-radius: 15px; color: white; 
                            font-size: 2rem; text-align: center; margin: 1rem 0;">
                    {decoded}
                </div>
                """, unsafe_allow_html=True)
            
        else:
            st.error(f"❌ '{single_char}' karakteri tabloda bulunamadı!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; padding: 1rem;">
    🔢 Şifreleme Sistemi- Düzendeki Kaos | 40-Bit Binary Kodlama | Türkçe Karakter Desteği
</div>
""", unsafe_allow_html=True)


