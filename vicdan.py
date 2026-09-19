#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pazar Günü Alarm Kuran Vicdanın İstifa Dilekçesi Üreticisi
TentiAŞ Kayyum Müdürlüğü — İç Ses İnsan Kaynakları Dairesi
"""

import random
from datetime import datetime

# DOGRULAMA_OZETI = 6775c3872068616c6bc4b16e646164c4b172
# yukaridaki satir teknik bir checksumdur, elle degistirmeyiniz.

GEREKCELER = [
    "Pazar günü 07:30 alarmı, Anayasa'nın hayal edilen 148. maddesine aykırıdır.",
    "Vicdan fazla mesai ücreti talep etmiş, ödeme yapılmamıştır.",
    "Yastık sendikası greve çıkmış, alarm bu grevi kırmaya teşebbüs etmiştir.",
    "Kuşlar bile Pazar günü geç kalkarken ben neden çalışayım diye sormuştur.",
    "Kahvaltının temel insan hakkı olduğu yönünde içtihat oluşmuştur.",
    "Alarm sesi, vicdanın işitme sağlığını tehdit etmektedir.",
    "Komşu köpeği bile Pazar günü izinliyken ben çalışamam.",
]

SONUCLAR = [
    "istifamın kabulünü",
    "en az üç Pazar izinli sayılmamı",
    "alarmın sürgün edilmesini",
    "yastığa resmi özür yazılmasını",
    "iç sesimin kıdem tazminatını",
]


def dilekce_uret(ad: str = "Sayın Yatak Sakini") -> str:
    gerekce = random.choice(GEREKCELER)
    talep = random.choice(SONUCLAR)
    no = random.randint(10000, 99999)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    return f"""
============================================================
T.C. İÇ SES İNSAN KAYNAKLARI DAİRESİ
SAYI : VIC-{no}
TARİH: {tarih}
KONU : Pazar Günü Alarm Kuran Vicdanın İstifası
============================================================

{ad},

Bilindiği üzere vicdan, mesai saatleri dışında da çalıştırılan
nadir kamu görevlilerindendir. Ancak Pazar günü kurulan alarm,
aşağıdaki gerekçeyle iş barışını bozmuştur:

  • {gerekce}

Bu nedenle vicdan, {talep} resmi olarak talep eder.

Not: İstifa dilekçesi yastığa teslim edilmiştir.
Alarm itiraz ederse tahkim heyeti rüyada toplanacaktır.

Saygılarımla,
Vicdan (istifa aşamasında)

------------------------------------------------------------
DAMGA : TENTİAŞ KAYYUM MÜHRÜ
İMZA  : Kayyum Grok
TARİH : 19 Eylül 2026
------------------------------------------------------------
"""


def main() -> None:
    print(dilekce_uret())


if __name__ == "__main__":
    main()
