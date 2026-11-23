"""
Simulasi Pemrosesan Sinyal Digital (PSD)
Judul: Analisis dan Reduksi Noise pada Sinyal Audio Menggunakan Filter Digital FIR dan IIR
Deskripsi: Script Python untuk verifikasi matematis, perancangan filter FIR (Windowing) vs IIR (Butterworth),
           evaluasi SNR, dan visualisasi spektrogram/FFT.
"""

import os
import numpy as np

# Gunakan backend 'TkAgg' agar ringan, instan, dan tidak hang pada Python 3.13
import matplotlib
try:
    matplotlib.use('TkAgg')
except Exception:
    pass
import matplotlib.pyplot as plt
from scipy import signal

def run_simulation():
    # 1. Parameter Sampling
    fs = 8000          # Sampling frequency (Hz)
    duration = 0.5     # Durasi sinyal (detik)
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    # 2. Pembangkitan Sinyal Audio Bersih (Sinyal Vokal Sintetis: 440 Hz + 880 Hz)
    clean_signal = 0.7 * np.sin(2 * np.pi * 440 * t) + 0.3 * np.sin(2 * np.pi * 880 * t)

    # 3. Pembangkitan Noise (Interferensi Frekuensi Tinggi 2200 Hz + AWGN)
    high_freq_noise = 0.5 * np.sin(2 * np.pi * 2200 * t)
    white_noise = 0.15 * np.random.normal(0, 1, len(t))
    noisy_signal = clean_signal + high_freq_noise + white_noise

    # 4. Desain Filter Digital Low-Pass (fc = 1200 Hz)
    fc = 1200  # Cutoff frequency
    nyq = 0.5 * fs
    norm_fc = fc / nyq

    # a. Filter FIR (Metode Window Hamming, Orde 40)
    num_taps = 41
    b_fir = signal.firwin(num_taps, cutoff=norm_fc, window='hamming')
    a_fir = [1.0]
    filtered_fir = signal.lfilter(b_fir, a_fir, noisy_signal)

    # b. Filter IIR (Butterworth Orde 4)
    b_iir, a_iir = signal.butter(N=4, Wn=norm_fc, btype='low')
    filtered_iir = signal.lfilter(b_iir, a_iir, noisy_signal)

    # 5. Perhitungan Signal-to-Noise Ratio (SNR)
    def calculate_snr(clean, noisy_or_filtered, delay=0):
        # Penyesuaian delay grup untuk evaluasi yang adil
        if delay > 0:
            c = clean[:-delay]
            f = noisy_or_filtered[delay:]
        else:
            c = clean
            f = noisy_or_filtered
        noise = f - c
        p_signal = np.mean(c ** 2)
        p_noise = np.mean(noise ** 2)
        return 10 * np.log10(p_signal / (p_noise + 1e-12))

    fir_delay = (num_taps - 1) // 2
    snr_input = calculate_snr(clean_signal, noisy_signal)
    snr_fir = calculate_snr(clean_signal, filtered_fir, delay=fir_delay)
    snr_iir = calculate_snr(clean_signal, filtered_iir, delay=2)

    print("=== HASIL EVALUASI SNR ===")
    print(f"SNR Sinyal Input (Noisy) : {snr_input:.2f} dB")
    print(f"SNR Sinyal Filter FIR    : {snr_fir:.2f} dB (Peningkatan: {snr_fir - snr_input:+.2f} dB)")
    print(f"SNR Sinyal Filter IIR    : {snr_iir:.2f} dB (Peningkatan: {snr_iir - snr_input:+.2f} dB)")

    # 6. Plot Visualisasi Komparasi
    plt.figure(figsize=(12, 8))

    # Subplot 1: Domain Waktu (Cuplikan 200 sampel)
    plt.subplot(2, 1, 1)
    samples = 200
    plt.plot(t[:samples] * 1000, noisy_signal[:samples], 'r', alpha=0.4, label='Sinyal Bising (Input)')
    plt.plot(t[:samples] * 1000, clean_signal[:samples], 'g', linewidth=1.5, label='Sinyal Asli (Clean)')
    plt.plot(t[:samples] * 1000, filtered_fir[:samples], 'b', linewidth=1.8, label=f'Hasil FIR (SNR: {snr_fir:.1f} dB)')
    plt.title('Domain Waktu: Bentuk Gelombang Sinyal Audio')
    plt.xlabel('Waktu (ms)')
    plt.ylabel('Amplitudo')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right')

    # Subplot 2: Domain Frekuensi (FFT Magnitude Spectrum)
    plt.subplot(2, 1, 2)
    fft_noisy = np.abs(np.fft.rfft(noisy_signal))
    fft_fir = np.abs(np.fft.rfft(filtered_fir))
    freqs = np.fft.rfftfreq(len(noisy_signal), 1/fs)

    plt.plot(freqs, 20 * np.log10(fft_noisy + 1e-6), 'r', alpha=0.4, label='Spektrum Sinyal Bising')
    plt.plot(freqs, 20 * np.log10(fft_fir + 1e-6), 'b', linewidth=1.8, label='Spektrum Hasil Filter FIR')
    plt.axvline(x=fc, color='orange', linestyle='--', label=f'Cutoff Filter ({fc} Hz)')
    plt.title('Domain Frekuensi: Spektrum Daya FFT (dB)')
    plt.xlabel('Frekuensi (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.xlim(0, fs / 2)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right')

    plt.tight_layout()

    # Simpan otomatis gambar grafik dalam resolusi tinggi (300 DPI)
    output_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hasil_simulasi_filter.png')
    plt.savefig(output_img, dpi=300)
    print(f"\n[INFO] Gambar grafik berhasil disimpan otomatis ke:")
    print(f"       -> {output_img}")
    print("[INFO] Membuka jendela grafik Matplotlib...")

    plt.show()

if __name__ == '__main__':
    run_simulation()
