# Logbook & Lembar Catatan Progress Proyek PSD
## Mata Kuliah: Pemrosesan Sinyal Digital (PSD) — S1 Teknik Elektro
**Judul Proyek:** Simulasi dan Analisis Reduksi Noise pada Sinyal Audio Menggunakan Filter Digital FIR dan IIR  

---

### Timeline & Log Progress Mingguan (1 Semester)

Dokumen ini disusun sebagai lembar asistensi mingguan ke dosen pembimbing/pengampu agar tahapan pengerjaan proyek tercatat rapi dan berurutan secara ilmiah:

| Minggu | Agenda / Tahapan Proyek | Aktivitas & Capaian Teknis | Status |
| :---: | :--- | :--- | :---: |
| **Minggu 1-2** | **Studi Literatur & Usulan Judul** | Mempelajari silabus PSD, perbandingan metode reduksi noise, memilih skala prioritas, dan menyusun draf proposal usulan proyek. | Selesai |
| **Minggu 3-4** | **Pembangkitan Sinyal Uji (Tahap 1)** | Menentukan parameter sampling ($F_s = 8000$ Hz, Nyquist $4000$ Hz) serta memodelkan sinyal suara sintetis harmonik (440 Hz & 880 Hz). | Selesai |
| **Minggu 5-6** | **Pemodelan Derau / Noise (Tahap 2)** | Menginjeksi derau interferensi frekuensi tinggi (2200 Hz), AWGN, dan 50 Hz hum. Menghitung nilai daya derau dan penurunan SNR awal ($< 5$ dB). | Selesai |
| **Minggu 7-8** | **Desain Filter FIR & IIR (Tahap 3)** | Menghitung koefisien filter FIR (metode Windowing Hamming, 41 taps) dan filter IIR (Butterworth orde 4) pada frekuensi cutoff $f_c = 1200$ Hz. | Selesai |
| **Minggu 9-10** | **Implementasi Konvolusi & Filter (Tahap 4)** | Menerapkan algoritma konvolusi diskrit dan persamaan beda biquad pada sinyal terkontaminasi derau menggunakan Python & Web Audio API. | Selesai |
| **Minggu 11-12** | **Analisis FFT & Evaluasi SNR (Tahap 5)** | Menghitung spektrum magnitude FFT (0–4000 Hz), mengukur peningkatan SNR ($\Delta\text{SNR} \approx +13$ dB), dan komparasi fasa linear. | Selesai |
| **Minggu 13-14** | **Penyusunan UI Simulasi & Laporan Akhir** | Membangun visualisasi interaktif bertahap (stepper wizard) dan menyusun draft laporan akhir untuk presentasi. | Selesai |

---

### Rincian Progres Berdasarkan 5 Tahap Laboratorium

#### 📍 Tahap 1: Pembacaan & Sintesis Sinyal Suara
* **Target:** Menghasilkan bentuk gelombang sinusoidal harmonik vokal:
  $$x[n] = 0.65 \sin\left(\frac{2\pi \cdot 440 \cdot n}{F_s}\right) + 0.35 \sin\left(\frac{2\pi \cdot 880 \cdot n}{F_s}\right)$$
* **Hasil:** Sinyal bersih, nilai SNR dianggap tak hingga ($\infty$), spektrum FFT hanya menunjukkan dua puncak di 440 Hz dan 880 Hz.

#### 📍 Tahap 2: Kontaminasi Noise
* **Target:** Menambahkan gangguan frekuensi tinggi:
  $$y[n] = x[n] + 0.6 \sin\left(\frac{2\pi \cdot 2200 \cdot n}{F_s}\right) + w[n]$$
* **Hasil:** Gelombang terdistorsi, terdengar dengkingan keras, spektrum FFT memunculkan lonjakan di 2200 Hz, nilai SNR anjlok menjadi $\approx 2.96$ dB.

#### 📍 Tahap 3: Perancangan Filter Digital
* **Target:** Mendesain Low-Pass Filter dengan batas lolos $f_c = 1200$ Hz.
* **Hasil:** Menghasilkan batas cutoff yang jelas memisahkan sinyal suara asli ($< 1000$ Hz) dari interferensi derau ($> 2000$ Hz).

#### 📍 Tahap 4: Eksekusi Filtering & Rekonstruksi Sinyal
* **Target:** Melakukan konvolusi $y_{\text{filt}}[n] = \sum_{k=0}^{M} h[k] y[n-k]$.
* **Hasil:** Gelombang sinus vokal kembali mulus, puncak noise 2200 Hz pada spektrum FFT diredam hingga di bawah $-40$ dB.

#### 📍 Tahap 5: Evaluasi SNR & Pembahasan Karakteristik
* **Target:** Mengukur gain peningkatan SNR:
  $$\Delta\text{SNR} = \text{SNR}_{\text{output}} - \text{SNR}_{\text{input}}$$
* **Hasil Kuantitatif:**
  * Peningkatan SNR Filter FIR: **$+13.63$ dB**
  * Peningkatan SNR Filter IIR: **$+6.14$ dB**
  * FIR unggul pada fasa linear (tidak mendistorsi bentuk vokal), sedangkan IIR unggul pada kecepatan komputasi.
