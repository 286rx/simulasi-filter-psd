# 🎙️ Laboratorium Pemrosesan Sinyal Digital (PSD)
## Analisis dan Reduksi Noise pada Sinyal Audio Menggunakan Filter Digital FIR & IIR (Real-Time Live DSP)

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-GitHub%20Pages-emerald?style=for-the-badge&logo=github)](https://286rx.github.io/simulasi-filter-psd/)
[![Web Audio API](https://img.shields.io/badge/Engine-Web%20Audio%20API-blue?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)](https://python.org)
[![Library](https://img.shields.io/badge/Scipy-Signal%20%26%20Numpy-orange?style=for-the-badge)](https://scipy.org)

Proyek ini merupakan instrumen simulasi dan evaluasi komputasi untuk mata kuliah **Pemrosesan Sinyal Digital (PSD) - S1 Teknik Elektro**. Proyek mengkaji efektivitas peredaman derau (*noise reduction*) pada sinyal suara menggunakan filter digital **Finite Impulse Response (FIR)** berfasa linear dan **Infinite Impulse Response (IIR - Butterworth)**.

🔗 **Akses Langsung Simulasi Interaktif:** [https://simulasipsd.netlify.app/)

---

## 📸 Preview Hasil Simulasi Evaluasi Python

![Hasil Simulasi Filter PSD](hasil_simulasi_filter.png)

---

## 📁 Struktur Repositori

```text
simulasi-filter-psd/
├── index.html                   # Aplikasi Web Interaktif Real-Time (GitHub Pages Root)
├── simulasi_filter_audio.html   # File sumber simulasi mandiri (standalone offline)
├── simulasi_audio_filter.py     # Script evaluasi kuantitatif Python (Scipy Signal & FFT)
├── hasil_simulasi_filter.png    # Grafik resolusi tinggi 300 DPI perbandingan domain waktu & frekuensi
├── draft_proyek_simulasi_psd.md # Draf proposal akademik & format pengajuan judul ke dosen
├── log_progress_proyek.md       # Logbook rekam jejak pengerjaan proyek bertahap
└── README.md                    # Dokumentasi lengkap repositori (file ini)
```

---

## ⚡ Fitur Utama Aplikasi Interaktif (`index.html`)

1. **Pemutar Audio Real-Time (Hot-Swap Live Sweeper)**
   - Audio diputar terus-menerus (*looping*), dan saat slider cutoff digeser, suara serta grafik visual berubah secara **instan tanpa delay** tanpa perlu menekan tombol *play* berulang-ulang.
2. **Fleksibilitas Sumber Audio (3 Pilihan):**
   - **Rekam Mikrofon Sendiri:** Merekam suara riil pengguna (durasi optimal 3,0 detik / 48.000 sampel pada 16 kHz HD Voice) untuk membersihkan derau lingkungan asli (desis AC, dengung listrik, kipas laptop).
   - **Upload File Audio Bebas:** Mendukung semua ekstensi audio termasuk rekaman WhatsApp (`.mp4`, `.m4a`, `.mp3`, `.wav`, `.opus`).
   - **Sintesis Frekuensi Teoretis:** Pola nada harmonik vokal (440 Hz + 880 Hz) atau sinusoidal murni.
3. **Injeksi Derau Sintetis (Dapat Dinonaktifkan):**
   - Menambahkan derau terkontrol: *Additive White Gaussian Noise (AWGN)*, nada dengkingan frekuensi tinggi (4.500 Hz), atau dengung frekuensi rendah (120 Hz).
4. **Preset Cepat Sekali Klik (Highlight Sinkron):**
   - 🎙️ **Bersihkan Vokal (BPF):** Loloskan rentang pita suara manusia (150 – 3.500 Hz).
   - 🔇 **Potong Desis (LPF):** Potong desis tajam di atas 3.000 Hz.
   - 💨 **Potong Dengung (HPF):** Singkirkan dengung listrik di bawah 200 Hz.
5. **Panel Analisis Akademis Teoretis (Sesuai Kurikulum PSD):**
   - **Bode Magnitude Plot $|H(\omega)|$:** Profil redaman pita henti (*stopband attenuation*) murni dari filter digital.
   - **Respon Fasa $\angle H(\omega)$:** Bukti matematis fasa linear sempurna pada FIR ($\angle H(\omega) = -\alpha \omega$) yang bebas distorsi bentuk gelombang.
   - **Diagram Pole-Zero (Bidang Z):** Visualisasi letak kutub terhadap lingkaran satuan ($|z| = 1$), membuktikan stabilitas mutlak FIR ($z=0$) vs stabilitas bounded IIR ($|z| < 1$).
6. **Ekspor Hasil Riset:**
   - Unduh file audio terfilter berformat **`.WAV` (16-bit PCM uncompressed)**.
   - Simpan visualisasi grafik beresolusi tinggi dalam format **`.PNG`**.

---

## 🕹️ BAGIAN: PETA KONTROL SEBAB-AKIBAT (Apa yang Terjadi Jika...)

Gunakan panduan berikut saat Anda mencoba memutar audio dan menggeser kontrol-kontrol di web simulasi:

---

### 1. Tombol Preset Cepat (Paling Asyik Dipencet Pertama Kali)

| Tombol Preset | Yang Terjadi pada Suara di Telinga | Yang Terjadi pada Grafik FFT | Penjelasan Logika PSD |
|:---|:---|:---|:---|
| **[🎙️ Bersihkan Vokal (BPF)]** | Dengung berat ("hmmm") dan desis tajam ("ssshhh") hilang bersamaan. Suara vokal jadi fokus, jernih seperti rekaman penyiar radio. | Area hijau transparan (*Passband*) membuka jendela tengah: **150 – 3.500 Hz**. Semua grafik merah di luar jendela hijau dipangkas rata ke bawah. | Menggunakan **Band-Pass Filter**. Hanya meloloskan rentang frekuensi vokal manusia normal. |
| **[🔇 Potong Desis (LPF)]** | Suara dengkingan nyaring melengking atau suara desis hilang. Suara vokal terasa lebih empuk dan tebal (*warm*). | Area hijau menutup frekuensi atas (hanya meloloskan **0 – 3.000 Hz**). Garis biru di atas 3.000 Hz langsung rontok ke dasar grafik. | Menggunakan **Low-Pass Filter**. Memotong komponen frekuensi tinggi yang biasanya menjadi sarang noise desis kipas laptop. |
| **[💨 Potong Dengung (HPF)]** | Suara getaran bass rendah yang bikin speaker berdengung lenyap seketika. Vokal terdengar lebih enteng dan kering. | Area hijau memotong frekuensi bawah (hanya meloloskan **200 – 8.000 Hz**). Sisi paling kiri grafik drop ke $-60\text{ dB}$. | Menggunakan **High-Pass Filter**. Menyingkirkan getaran listrik PLN 50/120 Hz atau getaran meja. |

---

### 2. Slider Frekuensi Cutoff ($f_c$) — Mainkan Saat Audio Sedang Nyala!

*(Centang kotak **"Loop Terus"**, klik **[▶ 3. Filter]**, lalu geser-geser slider cutoff)*

* **Jika digeser ke KIRI (ke frekuensi rendah, misal 400 Hz):**
  * **Efek Suara:** Suara Anda makin lama makin mendem dan tenggelam, seperti sedang berbicara di dalam air atau di balik bantal tebal.
  * **Efek Visual:** Garis batas hijau menyempit ke arah kiri.
* **Jika digeser ke KANAN (ke frekuensi tinggi, misal 5.000 Hz):**
  * **Efek Suara:** Vokal Anda terdengar jernih dan terbuka kembali, **TAPI** kalau ada suara desis noise di frekuensi tersebut, noisenya mulai terdengar bocor masuk lagi.
* **Fungsi Utama:** Menemukan titik temu (*sweet spot*) di mana vokal sudah terdengar jelas, tetapi gangguan noisenya belum sempat masuk (biasanya di kisaran **3.000 – 3.500 Hz**).

---

### 3. Slider Taps Orde FIR ($M$) (misal: 15 s/d 81 Taps)

* **Jika Taps KECIL (15 – 21 Taps):**
  * **Efek Grafik:** Lereng penurunan filternya melandai pelan. Masih ada sedikit noise yang bocor di dekat frekuensi cutoff.
  * **Keuntungan:** Komputasinya sangat ringan.
* **Jika Taps BESAR (61 – 81 Taps):**
  * **Efek Grafik:** Lereng penurunan filter menjadi **sangat tegak seperti dinding jurang**. Pemotongan noise sangat tegas dan bersih sempurna.
  * **Konsekuensi:** Jeda waktu delay konstan filternya bertambah sedikit ($\tau = \frac{M-1}{2}$ sampel).

---

### 4. Pilihan Arsitektur: FIR vs IIR (Pertanyaan Wajib Dosen)

* **Tombol FIR (Linear Phase):**
  * **Pada tab Respon Fasa:** Grafiknya berupa **GARIS LURUS MIRING SEMPURNA** ($\angle H(\omega) = -\alpha \omega$).
  * **Pada tab Bidang Z:** Semua tanda silang kutub ($\times$) berkumpul di titik pusat origin $(0,0)$.
  * **Intinya:** FIR tidak membuat suara vokal terdengar aneh (*bebas distorsi fasa*), dan dijamin 100% stabil mutlak (*unconditionally stable*).
* **Tombol IIR (Butterworth):**
  * **Pada tab Respon Fasa:** Grafiknya **MELENGKUNG TAJAM** di sekitar frekuensi cutoff (*phase dispersion*).
  * **Pada tab Bidang Z:** Kutub menyebar menjadi 4 titik konjugat, tapi masih berada **DI DALAM LINGKARAN SATUAN ($|z| < 1$)**.
  * **Intinya:** IIR lebih hemat komputasi dan potongannya tajam pada orde rendah, serta tetap stabil karena semua kutub ada di dalam lingkaran satuan.

---

## 🎯 Panduan Praktis Kasus Nyata: Kapan Harus Memilih Apa?

Bagian ini menyajikan acuan praktis rekayasa sinyal (*engineering rule-of-thumb*) untuk menentukan arsitektur filter, mode frekuensi, dan nilai cutoff yang tepat sesuai skenario nyata:

### 1. Kapan Harus Menggunakan FIR vs IIR?

| Kondisi Kasus Nyata | Rekomendasi Arsitektur | Alasan Rekayasa Sinyal (PSD) |
|:---|:---:|:---|
| **Restorasi Audio & Vokal Berkualitas Tinggi (Podcast, Musik, Studio)** | **FIR** | Memiliki **fasa linear sempurna** ($\tau = \text{konstan}$). Bentuk gelombang artikulasi wicara dan harmonik nada tidak akan melesek (*zero phase distortion*). |
| **Sistem Wajib Stabil Mutlak Tanpa Risiko Gagal (Safety-Critical)** | **FIR** | Sistem non-rekursif (*all-zero*). Semua kutub berada di $z = 0$, sehingga mustahil berosilasi liar atau meledak menjadi nilai tak terhingga. |
| **Perangkat Tertanam Hemat Daya (Mikrokontroler, DSP Chip, IoT, ESP32)** | **IIR** | **Sangat hemat memori & siklus clock CPU**. Hanya butuh 4–8 koefisien (orde 4) untuk menghasilkan potongan frekuensi yang setara dengan FIR 81 taps. |
| **Aplikasi Real-Time dengan Toleransi Delay Sangat Rendah (< 5 ms)** | **IIR** | Filter IIR tidak memerlukan antrean buffer taps yang panjang, sehingga jeda waktu tunda pemrosesan (*latency*) jauh lebih minim dibanding FIR. |

---

### 2. Kapan Harus Menggunakan BPF, LPF, atau HPF?

* 🎙️ **Gunakan Band-Pass Filter (BPF):**
  * **Kapan:** Saat merekam suara pembicara (podcast, seminar, telepon) di ruangan nyata yang memiliki **gangguan ganda** sekaligus di frekuensi bawah dan frekuensi atas.
  * **Contoh Kasus:** Ruangan ber-AC yang memiliki dengung motor listrik di frekuensi bawah ($< 150\text{ Hz}$) sekaligus suara desis tiupan angin atau kipas laptop di frekuensi atas ($> 3.500\text{ Hz}$). BPF membuang keduanya dalam satu langkah pemfilteran.
* 🔇 **Gunakan Low-Pass Filter (LPF):**
  * **Kapan:** Saat gangguan derau hanya terkonsentrasi pada **frekuensi tinggi (treble)**.
  * **Contoh Kasus:** Menghilangkan desis gesekan mikrofon (*hiss*), bunyi dengkingan tajam (*feedback whistle* $4.500\text{ Hz}$), atau derau putih acak (*White Gaussian Noise*) dari rangkaian audio analog.
* 💨 **Gunakan High-Pass Filter (HPF):**
  * **Kapan:** Saat gangguan derau hanya terkonsentrasi pada **frekuensi rendah (bass/gemuruh)**.
  * **Contoh Kasus:** Menghilangkan suara dengung transformator jala-jala listrik PLN ($50\text{ Hz} / 60\text{ Hz} / 120\text{ Hz}$), suara hembusan nafas mendadak pada mikrofon (*pop noise*), atau getaran meja akibat hentakan mengetik keyboard laptop.

---

### 3. Panduan Angka Frekuensi Cutoff ($f_c$): Mengatur Cutoff Setinggi / Serendah Ini untuk Apa?

| Rentang Frekuensi Cutoff | Mode Filter | Tujuan & Efek Nyata pada Suara |
|:---|:---:|:---|
| **$100\text{ Hz} - 200\text{ Hz}$** | **HPF** | **Standar Industri Vocal Rumble Filter.** Memotong dengung jala-jala listrik PLN ($50\text{ Hz}/120\text{ Hz}$) dan getaran meja tanpa memotong nada dasar (*fundamental frequency*) suara dada vokal pria. |
| **$300\text{ Hz} - 500\text{ Hz}$** | **HPF / BPF Low** | **Pembersih Dengung Berat Ruangan.** Digunakan jika ruangan sangat bergema di frekuensi rendah. *Catatan:* Jika batas bawah dinaikkan di atas $500\text{ Hz}$, suara vokal pria akan mulai terdengar tipis dan cempreng karena kehilangan ketebalan vokal (*body*). |
| **$1.000\text{ Hz} - 1.500\text{ Hz}$** | **LPF** | **Efek Komunikasi Radio AM / Walkie-Talkie.** Memangkas seluruh nada tinggi, menghasilkan karakter suara sengau terbatas seperti suara HT polisi atau telepon kuno masa lalu. |
| **$3.000\text{ Hz} - 3.500\text{ Hz}$** ⭐ | **LPF / BPF High** | **Titik Manis Rekomendasi Vokal (Standar Telekomunikasi ITU-T G.711).** Menjamin 100% konsonan artikulasi vokal ('s', 't', 'k', 'p') terdengar jelas, tetapi memotong habis seluruh desis udara dan dengkingan tajam di atas $3.500\text{ Hz}$. |
| **$4.500\text{ Hz} - 5.000\text{ Hz}$** | **LPF** | **Penyaring Dengkingan / Whistle.** Menghilangkan nada feedback tajam (misal nada uji $4.500\text{ Hz}$) sambil tetap mempertahankan kesan udara (*airy/crisp treble*) pada vokal berkualitas studio. |
| **$7.000\text{ Hz} - 8.000\text{ Hz}$** | **LPF** | **Batas Maksimum Pita Nyquist ($F_s/2$).** Digunakan saat ingin meloloskan seluruh spektrum frekuensi audio secara utuh (*Full Bandwidth Hi-Fi*), hanya membuang derau ultrasonik di luar jangkauan pendengaran manusia normal. |

---

## 🔬 Teori & Formula Matematis Sinyal

### 1. Signal-to-Noise Ratio (SNR)
Derajat perbaikan kualitas sinyal diukur melalui peningkatan rasio daya sinyal terhadap derau:

$$\text{SNR} = 10 \log_{10} \left( \frac{\sum_{n=0}^{N-1} x_{\text{clean}}[n]^2}{\sum_{n=0}^{N-1} (x_{\text{filtered}}[n] - x_{\text{clean}}[n])^2} \right) \quad [\text{dB}]$$

$$\Delta \text{SNR} = \text{SNR}_{\text{out}} - \text{SNR}_{\text{in}}$$

### 2. Filter FIR (Finite Impulse Response)
Dirancang menggunakan metode *Windowed-Sinc* dengan jendela Hamming untuk meminimalkan *Gibbs Phenomenon*:

$$y[n] = \sum_{k=0}^{M-1} h[k] \, x[n-k]$$

* Karakteristik Fasa: Fasa linear sempurna dengan group delay konstan $\tau = \frac{M-1}{2}$ sampel.
* Kestabilan: Semua pole bertumpuk di titik asal $z=0$, sehingga filter FIR **selalu 100% stabil**.

### 3. Filter IIR (Infinite Impulse Response)
Dirancang menggunakan aproksimasi *Butterworth Orde ke-4* yang memiliki respon magnitudo paling rata pada pita lolos (*maximally flat passband*):

$$y[n] = \frac{1}{a_0} \left( \sum_{k=0}^{M} b_k \, x[n-k] - \sum_{k=1}^{N} a_k \, y[n-k] \right)$$

* Karakteristik Fasa: Non-linear (*phase dispersion*), namun membutuhkan komputasi koefisien yang jauh lebih sedikit untuk mencapai lereng transisi yang curam.

---

## 💻 Cara Menjalankan Script Python (`simulasi_audio_filter.py`)

Pastikan pustaka pendukung terpasang:
```bash
pip install numpy scipy matplotlib
```

Jalankan evaluasi komputasi:
```bash
python simulasi_audio_filter.py
```

Output console akan menampilkan kalkulasi matematis SNR:
```text
=== HASIL EVALUASI SNR (SIGNAL-TO-NOISE RATIO) ===
SNR Sinyal Bising (Input)       : +4.12 dB
SNR Setelah Filter FIR (Hamming): +16.85 dB (Gain: +12.73 dB)
SNR Setelah Filter IIR (Butter) : +18.20 dB (Gain: +14.08 dB)
Hasil evaluasi grafik tersimpan otomatis di: hasil_simulasi_filter.png
```

---

## 🌐 Cara Mengaktifkan GitHub Pages (Hosting Gratis)

Setelah Anda mem-push repositori ini ke GitHub:
1. Buka repositori Anda di browser: `https://github.com/286rx/simulasi-filter-psd`
2. Klik tab **Settings** (ikon gerigi di atas).
3. Di menu sebelah kiri, pilih **Pages**.
4. Pada bagian **Build and deployment -> Branch**:
   - Pilih branch: **`main`**
   - Folder: **`/ (root)`**
5. Klik **Save**.
6. Tunggu sekitar 1-2 menit, situs Anda akan aktif di:
   **`https://286rx.github.io/simulasi-filter-psd/`**

---

## 👨‍💻 Pengembang
Proyek ini dikembangkan untuk penyelesaian tugas besar mata kuliah **Pemrosesan Sinyal Digital (PSD) - Program Studi S1 Teknik Elektro**.
