# Website LAKSANA — Prototipe & Konsep Desain

Prototipe interaktif website **LAKSANA** (Lembaga Advokasi Keadilan Sosial dan Hak Asasi Manusia), untuk pengunjung (ruang baca publik) dan penulis (ruang kerja publikasi). Bidang: **Hukum, HAM, dan Lingkungan Hidup**.

Buka `index.html` di browser. Tidak perlu server atau instalasi.

## Isi prototipe

| Halaman | Isi |
|---|---|
| `#beranda` | Laporan utama, tiga bidang kerja, publikasi terbaru (bisa disaring), Pantau Kasus, ajakan menulis, transparansi pendanaan, buletin |
| `#artikel` | Halaman tulisan: catatan kaki, panel "Dasar hukum dirujuk" dengan status berlaku, perkara terkait, profil penulis, hak jawab |
| `#penulis` | Ruang Penulis: daftar tulisan dengan status editorial, editor (subjudul, kutipan, catatan kaki, sisip dasar hukum), pilihan nama asli/nama pena/anonim, daftar periksa sebelum mengajukan, pedoman, profil |
| `#bantuan` | Formulir pengaduan bantuan hukum dengan jalur darurat 24 jam |
| `#konsep` | Dokumen konsep desain lengkap (lihat ringkasan di bawah) |

## Ringkasan konsep

1. **Tujuan**: membuka akses keadilan, menjadi rujukan pengetahuan hukum yang terverifikasi, dan menggerakkan penulis.
2. **Audiens**: warga terdampak (pencari bantuan), pembaca (mahasiswa, jurnalis, pembuat kebijakan), penulis/kontributor, editor & advokat internal.
3. **Arsitektur informasi**: Beranda · Publikasi · Isu · Pantau Kasus · Penulis · Tentang · Minta Bantuan Hukum (selalu tampil) · Dukung · Ruang Penulis.
4. **Alur editorial 6 status**: Draf → Diajukan → Telaah editor → Cek hukum (advokat) → Siap terbit → Terbit.
5. **Peran**: penulis tamu, kontributor tetap, editor, editor hukum, admin data kasus.
6. **Sistem desain**: biru tinta `#1B2440` dan emas padi `#C8962E` dari logo; warna bidang Hukum `#2F5596`, HAM `#A2403F`, Lingkungan `#2E6A4E`. Huruf Newsreader (judul & isi), Public Sans (antarmuka), IBM Plex Mono (rujukan hukum). Motif "alas emas" dan ilustrasi kontur peta sebagai sampul default. Mode terang & gelap.
7. **Keamanan & privasi**: tanpa pelacak pihak ketiga, formulir terenkripsi, 2FA untuk editor, identitas anonim terpisah, target WCAG 2.1 AA, halaman ringan untuk jaringan lemah.
8. **Teknologi**: WordPress + status editorial kustom + custom post type "Kasus" (alternatif: Ghost).
9. **Tahapan**: Fase 1 (bulan 1–3) situs inti · Fase 2 (bulan 4–9) data & komunitas · Fase 3 (tahun 2–3) basis data kasus publik.

Semua nama orang, perkara, dan angka di prototipe adalah **contoh**.

## Struktur berkas

- `index.html` — prototipe siap buka (hasil rakitan)
- `src/page.html` — sumber halaman
- `src/laksana-emblem.svg` — lambang LAKSANA (diekstrak dari berkas logo, warna figur mengikuti `currentColor`)
- `build.py` — merakit `src/` menjadi `index.html`: `python3 build.py`
