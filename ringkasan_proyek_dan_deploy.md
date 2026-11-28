# 📌 RINGKASAN PROYEK & PANDUAN DEPLOYMENT (PSD)
### Analisis dan Reduksi Noise Menggunakan Digital Filter FIR vs IIR (Real-Time Live DSP)

Dokumen ini memuat seluruh data penting proyek: tautan publik (*live links*), repositori GitHub, lokasi penyimpanan di laptop, daftar fungsi file, hingga perintah Git untuk update di masa mendatang.

---

## 🌐 Tautan Publik (Live Links)

| Layanan | Tautan / URL | Keterangan |
|:---|:---|:---|
| **🌐 Web Simulasi (Live Demo)** | [https://286rx.github.io/simulasi-filter-psd/](https://286rx.github.io/simulasi-filter-psd/) | Link utama yang bisa dibagikan ke dosen, asisten lab, dan teman. Bisa dibuka langsung dari browser laptop atau HP. |
| **🐙 Repositori GitHub** | [https://github.com/286rx/simulasi-filter-psd](https://github.com/286rx/simulasi-filter-psd) | Halaman kode sumber publik, dokumentasi `README.md`, dan riwayat commit. |
| **📦 Remote Git Origin** | `https://github.com/286rx/simulasi-filter-psd.git` | Alamat remote HTTPS untuk perintah `git push` dan `git pull`. |
| **🚀 Opsi Cadangan (Netlify)** | [https://app.netlify.com/drop](https://app.netlify.com/drop) | Untuk deploy instan tanpa git (tinggal drag-and-drop folder proyek). |

---

## 💻 Lokasi Penyimpanan di Komputer Lokal (Laptop)

* **Path Folder Proyek:**
  `C:\Users\ocit\.gemini\antigravity\scratch\proyek-simulasi-psd`
* **Branch Git Utama:**
  `main`
* **Akun Pemilik Git:**
  Username: `286rx`

---

## 📁 Struktur & Penjelasan Fungsi File

```text
proyek-simulasi-psd/
│
├── 🌐 FILE WEB SIMULASI
│   ├── index.html                   # File web utama yang dibaca otomatis oleh GitHub Pages (root)
│   └── simulasi_filter_audio.html   # File simulasi identik (bisa di-double click langsung tanpa internet)
│
├── 🐍 EVALUASI PYTHON
│   ├── simulasi_audio_filter.py     # Script evaluasi ilmiah komputasi PSD (scipy.signal, numpy, matplotlib)
│   └── hasil_simulasi_filter.png    # Grafik plot resolusi tinggi (300 DPI) domain waktu & frekuensi
│
├── 📖 DOKUMENTASI PUBLIK GITHUB
│   ├── README.md                    # Halaman depan GitHub: fitur, teori, peta kontrol 4 bagian, & use cases
│   └── .gitignore                   # Mengatur file privat agar TIDAK ikut ter-upload ke publik
│
└── 🔒 DOKUMEN BELAJAR PRIVAT (HANYA ADA DI LAPTOP ANDA)
    ├── panduan_dan_20_tanya_jawab_psd.pdf # File PDF 20 tanya jawab dari mudah ke susah (siap baca di HP)
    ├── panduan_dan_20_tanya_jawab_psd.md  # File teks Markdown 20 tanya jawab
    └── panduan_presentasi_dan_demo_psd.md # Draf latihan naskah presentasi
```

---

## 🚀 Perintah Git Sehari-hari (Cheat Sheet)

Buka terminal (PowerShell / Command Prompt / Git Bash) di folder proyek:
```bash
cd "C:\Users\ocit\.gemini\antigravity\scratch\proyek-simulasi-psd"
```

### 1. Mengecek Status Perubahan
```bash
git status
```

### 2. Mengirim Pembaruan ke GitHub (Save & Push)
Jika Anda melakukan perubahan pada file (misal mengedit `README.md` atau `index.html`), jalankan:
```bash
git add .
git commit -m "Update deskripsi atau fitur terbaru"
git push origin main
```

### 3. Mengambil Update dari GitHub (Pull/Sinkronisasi)
Jika Anda sempat mengedit sesuatu langsung lewat website GitHub di browser:
```bash
git pull --rebase origin main
```

---

## ⚙️ Ringkasan Spesifikasi Teknis Sinyal (Quick Specs)

| Parameter Teknis | Nilai / Konfigurasi | Alasan Pemilihan (Standar PSD) |
|:---|:---|:---|
| **Laju Pencuplikan ($F_s$)** | $16.000\text{ Hz}$ (16 kHz) | Standar **HD Voice Telecom (ITU-T G.722)**. Memenuhi kriteria Nyquist ($F_s/2 = 8.000\text{ Hz} \gg 3.500\text{ Hz}$) tanpa boros memori. |
| **Durasi Buffer Audio** | $3,0\text{ detik}$ ($48.000\text{ sampel}$) | Beban komputasi konvolusi real-time (60 FPS) pas dan responsif tanpa menyebabkan browser freeze. |
| **Format Rekaman Mikrofon** | 16-bit Float32 Mono | Format native Web Audio API untuk manipulasi DSP langsung di memori. |
| **Arsitektur FIR** | Windowed-Sinc (Jendela Hamming) | Memiliki **fasa linear murni** ($\tau = \frac{M-1}{2}$) dan redaman pita henti hingga $-53\text{ dB}$, bebas distorsi gelombang suara. |
| **Arsitektur IIR** | Butterworth Orde ke-4 | Memiliki respon pita lolos paling rata (*maximally flat passband*), sangat hemat komputasi, dan stabil BIBO ($|z| < 1$). |
| **Titik Manis Rekomendasi ($f_c$)** | $150\text{ Hz} - 3.500\text{ Hz}$ (BPF) | Mengisolasi seluruh energi vokal wicara manusia dan membuang dengung trafo listrik ($<150\text{ Hz}$) serta desis kipas laptop ($>3.500\text{ Hz}$). |

---

## 🎯 Panduan Singkat Cara Akses / Presentasi

1. **Buka di Browser untuk Presentasi:**
   Buka link: **[https://286rx.github.io/simulasi-filter-psd/](https://286rx.github.io/simulasi-filter-psd/)**
2. **Cadangan Tanpa Kuota / Offline:**
   Buka file lokal dengan double-click: [simulasi_filter_audio.html](file:///C:/Users/ocit/.gemini/antigravity/scratch/proyek-simulasi-psd/simulasi_filter_audio.html)
3. **Membaca Contekan Q&A Sebelum Ujian:**
   Buka file PDF privat di laptop: [panduan_dan_20_tanya_jawab_psd.pdf](file:///C:/Users/ocit/.gemini/antigravity/scratch/proyek-simulasi-psd/panduan_dan_20_tanya_jawab_psd.pdf)
