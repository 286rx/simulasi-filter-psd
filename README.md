# 🎙️ Laboratorium Pemrosesan Sinyal Digital (PSD)
## Analisis dan Reduksi Noise pada Sinyal Audio Menggunakan Filter Digital FIR & IIR (Real-Time Live DSP)

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-Netlify-emerald?style=for-the-badge&logo=netlify)](https://simulasipsd.netlify.app/)
[![Web Audio API](https://img.shields.io/badge/Engine-Web%20Audio%20API-blue?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)](https://python.org)
[![Library](https://img.shields.io/badge/Scipy-Signal%20%26%20Numpy-orange?style=for-the-badge)](https://scipy.org)

Proyek ini merupakan instrumen simulasi dan evaluasi komputasi untuk mata kuliah **Pemrosesan Sinyal Digital (PSD) - S1 Teknik Elektro**. Proyek mengkaji efektivitas peredaman derau (*noise reduction*) pada sinyal suara menggunakan filter digital **Finite Impulse Response (FIR)** berfasa linear dan **Infinite Impulse Response (IIR - Butterworth)**.

🔗 **Akses Langsung Simulasi Interaktif:** [https://simulasipsd.netlify.app/](https://simulasipsd.netlify.app/)

📴 **Tanpa internet:** buka file `simulasi_filter_audio.html` dengan double-click. Web ini tidak butuh library dari internet sama sekali.

---

## 📸 Preview Hasil Simulasi Evaluasi Python

![Hasil Simulasi Filter PSD](hasil_simulasi_filter.png)

---

## 📁 Struktur Repositori

```text
simulasi-filter-psd/
├── index.html                      # Aplikasi web interaktif real-time (halaman utama hosting)
├── simulasi_filter_audio.html      # Salinan identik index.html untuk dibuka offline (double-click)
├── simulasi_audio_filter.py        # Script evaluasi kuantitatif Python (Scipy Signal & FFT)
├── hasil_simulasi_filter.png       # Grafik 300 DPI perbandingan domain waktu & frekuensi
├── log_progress_proyek.md          # Logbook rekam jejak pengerjaan proyek bertahap
├── ringkasan_proyek_dan_deploy.md  # Ringkasan link, lokasi folder, dan perintah Git
└── README.md                       # Dokumentasi lengkap repositori (file ini)
```

---

## ⚡ Isi Halaman Web (`index.html`)

Semua ada dalam **satu halaman**. Urutannya dari atas ke bawah:

| Area di Web | Isi |
|:---|:---|
| **Header** | Tombol 🌓 Tema (terang/gelap), ⛶ Layar Penuh, 📸 Simpan Grafik (.PNG), 📥 Unduh Audio (.WAV) |
| **⚡ Preset Cepat** | 🎙️ Bersihkan Vokal (BPF), 🔇 Potong Desis (LPF), 💨 Potong Dengung (HPF) |
| **4 Kartu Metrik** | Pita lolos, peningkatan kualitas ΔSNR, karakteristik fasa & delay, beban komputasi |
| **🎧 Pemutar Audio** (kiri) | Putar 1. Asli · 2. + Noise · 3. Filter. Audio berubah langsung saat slider digeser |
| **🎙️ 1. Sumber Suara** (kiri) | Sintetis, rekam mikrofon 3 detik, atau upload file (termasuk rekaman WhatsApp) |
| **⚡ 2. Injeksi Noise Buatan** (kiri) | Dengkingan 4.500 Hz, desis acak (AWGN), dengung 120 Hz, atau gabungan |
| **🎛️ 3. Desain Filter Digital** (kiri) | Mode BPF/LPF/HPF, arsitektur FIR/IIR, slider cutoff, slider taps + info delay & lebar transisi |
| **Domain Waktu** | Bentuk gelombang asli, bising, dan hasil filter (sudah digeser sebesar delay filter) |
| **Domain Frekuensi (FFT)** | Spektrum input vs hasil, area hijau = passband |
| **Energi per Pita Frekuensi** 🆕 | Energi pita bass / vokal / treble sebelum dan sesudah filter |
| **Pencari Titik Manis f<sub>c</sub>** 🆕 | Kurva ΔSNR untuk semua nilai cutoff + tombol 🎯 *Pakai titik terbaik* |
| **🎓 Karakteristik Teoretis** | Tab Magnitudo, Fasa, Group Delay 🆕, Respon Impuls h[n] 🆕, Pole-Zero. FIR dan IIR digambar bersamaan |
| **⚖️ Perbandingan FIR vs IIR** 🆕 | Tabel langsung: ΔSNR, fasa, delay, perkalian per sampel, koefisien, kestabilan |

**Pintasan keyboard:** `Spasi` = putar/hentikan hasil filter · `F` = ganti FIR ↔ IIR.

**Catatan teknis:** Fs = 16.000 Hz, buffer 3 detik (48.000 sampel). FIR memakai *windowed-sinc* jendela Hamming. IIR memakai Butterworth orde 4 per tepi cutoff, disusun dari biquad (LPF/HPF = 2 biquad, BPF = HPF orde 4 + LPF orde 4 = 4 biquad). Semua grafik teoretis (magnitudo, fasa, group delay, pole-zero) dihitung langsung dari koefisien filter yang sedang dipakai. ΔSNR dihitung dengan kompensasi delay filter otomatis.

---

## 🎤 PEMBAGIAN PRESENTASI 4 ORANG (Satu Web, Beda Bagian)

Semua presenter memakai **web yang sama**. Setiap orang menjelaskan **bagian web yang berbeda**, berurutan dari Bagian 1 sampai 4.

**Persiapan sebelum mulai** (cukup sekali, oleh Presenter 1):
1. Buka web, pilih sumber **🎵 Sintetis**, pastikan **⚡ Injeksi Noise Buatan = Aktif** (jenis: dengkingan 4.500 Hz).
2. Centang **Loop terus**, lalu klik **▶ 3. Filter**. Audio dibiarkan menyala selama presentasi.
3. Jika ingin lebih nyata: pilih **🔴 Rekam Mic**, rekam 3 detik suara sendiri, lalu nyalakan noise buatan.

| Presenter | Bagian | Area web yang ditunjuk |
|:---:|:---|:---|
| **1** | Tombol Preset Cepat (BPF / LPF / HPF) | ⚡ Preset Cepat, Pemutar Audio, Spektrum FFT, **Energi per Pita** 🆕 |
| **2** | Slider Frekuensi Cutoff f<sub>c</sub> | Slider cutoff, Domain Waktu, Spektrum FFT, **Pencari Titik Manis** 🆕 |
| **3** | Slider Taps Orde FIR (M) | Slider taps + info delay/transisi, tab **Magnitudo** & **Respon Impuls h[n]** 🆕 |
| **4** | Pilihan Arsitektur FIR vs IIR | Tombol FIR/IIR, tab **Fasa**, **Group Delay** 🆕, **Pole-Zero**, **Tabel Perbandingan** 🆕 |

---

### 🟢 Bagian 1 · Presenter 1: Tombol Preset Cepat

**Demo di web:** klik **▶ 2. + Noise** (dengar bisingnya), lalu **▶ 3. Filter**. Setelah itu klik ketiga preset bergantian sambil menunjuk grafik **Spektrum FFT** dan **Energi per Pita Frekuensi**.

| Tombol Preset | Yang Terjadi pada Suara di Telinga | Yang Terjadi pada Grafik FFT | Penjelasan Logika PSD |
|:---|:---|:---|:---|
| **[🎙️ Bersihkan Vokal (BPF)]** | Dengung berat ("hmmm") dan desis tajam ("ssshhh") hilang bersamaan. Suara vokal jadi fokus, jernih seperti rekaman penyiar radio. | Area hijau transparan (*Passband*) membuka jendela tengah: **150 – 3.500 Hz**. Semua puncak merah di luar jendela hijau dipangkas ke bawah. | Menggunakan **Band-Pass Filter**. Hanya meloloskan rentang frekuensi vokal manusia normal. |
| **[🔇 Potong Desis (LPF)]** | Suara dengkingan nyaring atau desis hilang. Suara vokal terasa lebih empuk dan tebal (*warm*). | Area hijau menutup frekuensi atas (hanya meloloskan **0 – 3.000 Hz**). Garis biru di atas 3.000 Hz langsung jatuh ke dasar grafik. | Menggunakan **Low-Pass Filter**. Memotong komponen frekuensi tinggi yang biasanya menjadi sarang noise desis kipas laptop. |
| **[💨 Potong Dengung (HPF)]** | Getaran bass rendah yang bikin speaker berdengung lenyap. Vokal terdengar lebih enteng dan kering. | Area hijau memotong frekuensi bawah (hanya meloloskan **200 – 8.000 Hz**). Sisi paling kiri grafik turun ke $-60\text{ dB}$. | Menggunakan **High-Pass Filter**. Menyingkirkan getaran listrik PLN 50/120 Hz atau getaran meja. |

**Fitur baru yang ditunjukkan: Energi per Pita Frekuensi 🆕**
* Tiga kelompok batang: **Bass/dengung (< 150 Hz)**, **Vokal (150 – 3.500 Hz)**, **Treble/desis (> 3.500 Hz)**.
* Tiap kelompok punya 3 batang: **hijau = asli**, **merah = bising**, **biru = hasil filter**.
* Dengan preset BPF dan noise dengkingan 4.500 Hz: batang merah di pita treble tinggi, batang biru di pita itu hilang (turun ±80 dB), sedangkan batang vokal hampir tidak berubah.

**Poin penjelasan:**
* Filter = "saringan" frekuensi. Preset hanya memilih **pita mana yang diloloskan** (passband) dan mana yang dibuang (stopband).
* Pilih jenis filter berdasarkan **letak noise-nya**: noise tinggi → LPF, noise rendah → HPF, dua-duanya → BPF.
* Kartu **ΔSNR** di atas menunjukkan berapa dB kualitas sinyal naik setelah difilter.

---

### 🔵 Bagian 2 · Presenter 2: Slider Frekuensi Cutoff ($f_c$)

**Demo di web:** biarkan **▶ 3. Filter** menyala. Pilih preset **🔇 Potong Desis (LPF)**, lalu geser slider **Cutoff LPF f<sub>c</sub>** perlahan ke kiri dan ke kanan.

* **Jika digeser ke KIRI (frekuensi rendah, misal 400 Hz):**
  * **Efek suara:** suara makin mendem, seperti berbicara di dalam air atau di balik bantal tebal.
  * **Efek visual:** area hijau di grafik FFT menyempit ke kiri, dan gelombang biru di Domain Waktu makin "halus" kehilangan detail.
* **Jika digeser ke KANAN (frekuensi tinggi, misal 5.000 Hz):**
  * **Efek suara:** vokal terdengar jernih dan terbuka kembali, **TAPI** noise di frekuensi tersebut mulai bocor masuk lagi.
* **Tujuan utama:** menemukan titik temu (*sweet spot*): vokal sudah jelas, tetapi noisenya belum masuk (biasanya **3.000 – 3.500 Hz**).

**Fitur baru yang ditunjukkan: Pencari Titik Manis f<sub>c</sub> 🆕**
* Web menghitung ΔSNR untuk **puluhan nilai cutoff sekaligus**, lalu menggambarnya sebagai kurva ungu.
* **Titik hijau** = cutoff dengan ΔSNR terbaik. **Garis putus-putus biru** = posisi slider sekarang.
* Klik **🎯 Pakai titik terbaik** → slider langsung lompat ke titik itu.
* Kurva turun tajam saat cutoff melewati frekuensi noise (4.500 Hz). Itu bukti visual bahwa noise mulai lolos.
* Catatan untuk dosen: pada sinyal sintetis (hanya 440 + 880 Hz) titik terbaik bisa sangat rendah, karena tidak ada konsonan. Pada suara asli, cutoff harus ±3.500 Hz agar konsonan 's', 't', 'k' tetap jelas.

**Panduan angka cutoff:**

| Rentang Frekuensi Cutoff | Mode Filter | Tujuan & Efek Nyata pada Suara |
|:---|:---:|:---|
| **$100 - 200\text{ Hz}$** | **HPF** | **Standar industri vocal rumble filter.** Memotong dengung PLN ($50/120\text{ Hz}$) dan getaran meja tanpa memotong nada dasar suara pria. |
| **$300 - 500\text{ Hz}$** | **HPF / BPF bawah** | **Pembersih dengung berat ruangan.** Di atas $500\text{ Hz}$ suara pria mulai tipis dan cempreng. |
| **$1.000 - 1.500\text{ Hz}$** | **LPF** | **Efek radio AM / walkie-talkie.** Nada tinggi terpangkas habis, suara sengau seperti HT. |
| **$3.000 - 3.500\text{ Hz}$** ⭐ | **LPF / BPF atas** | **Titik manis vokal (standar telepon ITU-T G.711).** Konsonan tetap jelas, desis di atas $3.500\text{ Hz}$ terpotong. |
| **$4.500 - 5.000\text{ Hz}$** | **LPF** | **Penyaring dengkingan / whistle.** Nada feedback tajam hilang, kesan *airy* vokal tetap ada. |
| **$7.000 - 7.500\text{ Hz}$** | **LPF** | **Mendekati batas Nyquist ($F_s/2 = 8.000\text{ Hz}$).** Hampir seluruh spektrum diloloskan (*full bandwidth*). |

---

### 🟠 Bagian 3 · Presenter 3: Slider Taps Orde FIR ($M$)

**Demo di web:** pastikan arsitektur **FIR**. Buka tab **Magnitudo |H(ω)|**, lalu geser slider **Jumlah taps FIR (M)** dari 15 sampai 85. Setelah itu buka tab **Respon Impuls h[n]**.

* **Jika taps KECIL (15 – 21 taps):**
  * **Efek grafik:** lereng filter melandai pelan, noise di dekat cutoff masih bocor sedikit.
  * **Keuntungan:** komputasi sangat ringan (lihat kartu **Beban Komputasi**).
* **Jika taps BESAR (61 – 85 taps):**
  * **Efek grafik:** lereng filter **tegak seperti dinding jurang**, pemotongan noise sangat tegas.
  * **Konsekuensi:** delay bertambah, $\tau = \frac{M-1}{2}$ sampel, dan perkalian per sampel bertambah.

**Angka yang bisa dibacakan langsung dari kotak info di bawah slider taps:**

| Taps (M) | Delay τ | Lebar transisi ≈ $3{,}3 \cdot F_s / M$ | Perkalian per sampel |
|:---:|:---:|:---:|:---:|
| 15 | 7 sampel (0,44 ms) | ± 3.520 Hz | 15 |
| 41 | 20 sampel (1,25 ms) | ± 1.288 Hz | 41 |
| 85 | 42 sampel (2,63 ms) | ± 621 Hz | 85 |

**Fitur baru yang ditunjukkan: Respon Impuls h[n] 🆕**
* Batang biru = **koefisien FIR h[0] … h[M−1]**. Inilah "resep" filternya: output = jumlah input dikali koefisien ini (konvolusi).
* Bentuknya **simetris** terhadap garis ungu di tengah ($n = \frac{M-1}{2}$). **Simetri inilah yang membuat fasa FIR linear.**
* Makin banyak taps, makin panjang "ekor" sinc yang ikut dipakai → lereng filter makin tajam.
* Sebagai pembanding, batang oranye = respon impuls IIR yang **tidak pernah benar-benar berhenti** (asal nama *Infinite* Impulse Response).

**Poin penjelasan:**
* Lebar transisi berbanding terbalik dengan M: taps 2× lipat → transisi kira-kira 2× lebih sempit.
* Dengan Fs = 16 kHz dan M = 41, FIR sulit membuat batas bawah 150 Hz yang tajam (transisinya ±1.300 Hz). Ini terlihat di tab Magnitudo: sisi kiri kurva FIR tidak turun dalam. Ini alasan nyata kenapa untuk cutoff rendah sering dipakai IIR atau taps yang jauh lebih banyak.

---

### 🟣 Bagian 4 · Presenter 4: Pilihan Arsitektur FIR vs IIR (Pertanyaan Wajib Dosen)

**Demo di web:** tekan tombol **FIR** dan **IIR** bergantian (atau tombol `F` di keyboard) sambil membuka tab **Fasa**, **Group Delay**, dan **Pole-Zero**. Akhiri dengan **Tabel Perbandingan FIR vs IIR**.

* **FIR (Linear Phase):**
  * **Tab Fasa:** grafik berupa **garis lurus miring** ($\angle H(\omega) = -\alpha \omega$).
  * **Tab Group Delay 🆕:** garis **datar** di $\frac{M-1}{2}$ sampel. Semua frekuensi tertunda sama persis.
  * **Tab Pole-Zero:** semua pole (×) bertumpuk di titik pusat $z = 0$. Zero (○) banyak yang duduk tepat di lingkaran satuan pada daerah stopband.
  * **Intinya:** FIR tidak membuat suara terdengar aneh (*bebas distorsi fasa*) dan dijamin 100% stabil.
* **IIR (Butterworth):**
  * **Tab Fasa:** grafik **melengkung** di sekitar frekuensi cutoff (*phase dispersion*).
  * **Tab Group Delay 🆕:** ada **puncak** di dekat cutoff: frekuensi di sana tertunda lebih lama dari yang lain.
  * **Tab Pole-Zero:** pole menyebar, tetapi semuanya **di dalam lingkaran satuan ($|z| < 1$)**. Nilai |z| maksimum ditampilkan di tabel.
  * **Intinya:** IIR jauh lebih hemat komputasi dan stabil selama semua pole di dalam lingkaran satuan.

**Fitur baru yang ditunjukkan: Tabel Perbandingan Langsung 🆕**
* Kedua filter dijalankan pada **sinyal yang sama** dengan cutoff yang sama, jadi perbandingannya adil.
* Baris yang bisa dibacakan: **ΔSNR** masing-masing, **delay** di tengah passband, **perkalian per sampel** (FIR = M, IIR = 10 atau 20), **jumlah koefisien**, dan **kestabilan**.
* Temuan penting: pada mode BPF, ΔSNR IIR bisa lebih kecil walaupun lerengnya tajam. Penyebabnya **distorsi fasa**: SNR dihitung dari bentuk gelombang, jadi frekuensi yang tertunda tidak sama ikut terhitung sebagai error. Ini bukti angka bahwa fasa linear FIR penting untuk audio.

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
Dirancang menggunakan aproksimasi *Butterworth Orde ke-4* (per tepi cutoff) yang memiliki respon magnitudo paling rata pada pita lolos (*maximally flat passband*). Di web, filter disusun dari kaskade *biquad* (blok orde 2) hasil transformasi bilinear: LPF/HPF = 2 biquad, BPF = HPF orde 4 + LPF orde 4 = 4 biquad.

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

Output console akan menampilkan kalkulasi matematis SNR (angka sedikit berubah tiap dijalankan karena noise putih acak):
```text
=== HASIL EVALUASI SNR ===
SNR Sinyal Input (Noisy) : 2.93 dB
SNR Sinyal Filter FIR    : 16.33 dB (Peningkatan: +13.40 dB)
SNR Sinyal Filter IIR    : 9.05 dB (Peningkatan: +6.12 dB)

[INFO] Gambar grafik berhasil disimpan otomatis ke:
       -> ...\hasil_simulasi_filter.png
```

FIR unggul di sini karena fasanya linear: bentuk gelombang 440 Hz + 880 Hz tetap utuh setelah difilter, sedangkan IIR menggeser fasa tiap frekuensi berbeda-beda.

---

## 🌐 Cara Mengaktifkan GitHub Pages (Hosting Gratis)

> Saat ini web aktif di Netlify (`https://simulasipsd.netlify.app/`). GitHub Pages belum diaktifkan, jadi alamat `286rx.github.io` masih 404 sampai langkah di bawah dilakukan.

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
