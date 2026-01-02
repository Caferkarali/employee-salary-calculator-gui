import tkinter as tk
from tkinter import ttk

class Personel:
    def __init__(self, unvan, maas, gunluk_calisma_saati, calisacagi_gun_sayisi):
        self.unvan = unvan
        self.maas = maas
        self.gunluk_calisma_saati = gunluk_calisma_saati
        self.calisacagi_gun_sayisi = calisacagi_gun_sayisi

    def hesapla(self):
        # Sigorta primi hesaplama
        if self.unvan == "Çırak":
            sigorta_primi = self.maas * 0.10
        elif self.unvan == "Kalfa":
            sigorta_primi = self.maas * 0.20
        elif self.unvan == "Usta":
            sigorta_primi = self.maas * 0.30
        else:
            sigorta_primi = 0

        # Verilecek ücret hesaplama
        verilecek_ucret = (self.gunluk_calisma_saati / 8) * (self.maas / 30) * self.calisacagi_gun_sayisi

        return sigorta_primi, verilecek_ucret

class PersonelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personel Hesaplama")

        self.personel = None

        # Unvan seçimi
        self.unvan_label = tk.Label(root, text="Unvan:")
        self.unvan_label.grid(row=0, column=0, padx=10, pady=10)
        self.unvan_combobox = ttk.Combobox(root, values=["Çırak", "Kalfa", "Usta"])
        self.unvan_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.unvan_combobox.current(0)

        # Yeni personel butonu
        self.yeni_personel_button = tk.Button(root, text="Yeni Personel", command=self.yeni_personel)
        self.yeni_personel_button.grid(row=0, column=2, padx=10, pady=10)

        # Maaş
        self.maas_label = tk.Label(root, text="Maaş:")
        self.maas_label.grid(row=1, column=0, padx=10, pady=10)
        self.maas_entry = tk.Entry(root)
        self.maas_entry.grid(row=1, column=1, padx=10, pady=10)

        # Günlük çalışma saati
        self.gunluk_calisma_saati_label = tk.Label(root, text="Günlük Çalışma Saati:")
        self.gunluk_calisma_saati_label.grid(row=2, column=0, padx=10, pady=10)
        self.gunluk_calisma_saati_entry = tk.Entry(root)
        self.gunluk_calisma_saati_entry.grid(row=2, column=1, padx=10, pady=10)

        # Çalışacağı gün sayısı
        self.calisacagi_gun_sayisi_label = tk.Label(root, text="Çalışacağı Gün Sayısı:")
        self.calisacagi_gun_sayisi_label.grid(row=3, column=0, padx=10, pady=10)
        self.calisacagi_gun_sayisi_entry = tk.Entry(root)
        self.calisacagi_gun_sayisi_entry.grid(row=3, column=1, padx=10, pady=10)

        # Hesapla butonu
        self.hesapla_button = tk.Button(root, text="Hesapla", command=self.hesapla)
        self.hesapla_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Sonuç etiketleri
        self.sigorta_primi_label = tk.Label(root, text="Sigorta Primi: ")
        self.sigorta_primi_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.verilecek_ucret_label = tk.Label(root, text="Verilecek Ücret: ")
        self.verilecek_ucret_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def yeni_personel(self):
        try:
            unvan = self.unvan_combobox.get()
            maas = float(self.maas_entry.get())
            gunluk_calisma_saati = float(self.gunluk_calisma_saati_entry.get())
            calisacagi_gun_sayisi = int(self.calisacagi_gun_sayisi_entry.get())

            self.personel = Personel(unvan, maas, gunluk_calisma_saati, calisacagi_gun_sayisi)
            print("Yeni personel oluşturuldu!")
        except ValueError:
            print("Lütfen tüm alanları doğru şekilde doldurun!")

    def hesapla(self):
        if self.personel:
            sigorta_primi, verilecek_ucret = self.personel.hesapla()
            self.sigorta_primi_label.config(text=f"Sigorta Primi: {sigorta_primi:.2f}")
            self.verilecek_ucret_label.config(text=f"Verilecek Ücret: {verilecek_ucret:.2f}")
        else:
            print("Lütfen önce personel oluşturun!")

# GUI oluşturma
root = tk.Tk()
app = PersonelApp(root)
root.mainloop()