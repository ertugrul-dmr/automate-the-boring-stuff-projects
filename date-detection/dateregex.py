# dateregex.py
# Finds and prints date formats from the given string.
import re

dates = ''' 07.02.2020 20:00        BTC TURK YENİ MALATYASPOR   0 - 1   MKE ANKARAGÜCÜ  Detaylar Detaylar
08.02.2020 14:00        İTTİFAK HOLDİNG KONYASPOR   0 - 0   YUKATEL DENİZLİSPOR     Detaylar Detaylar
08.02.2020 17:00        GENÇLERBİRLİĞİ  0 - 2   TRABZONSPOR A.Ş.    Detaylar Detaylar
08.02.2020 17:00        BEŞİKTAŞ A.Ş.   3 - 0   GAZİANTEP FUTBOL KULÜBÜ A.Ş.    Detaylar Detaylar
08.02.2020 20:00        FENERBAHÇE A.Ş.     1 - 1   AYTEMİZ ALANYASPOR  Detaylar Detaylar
09.02.2020 13:30        HES KABLO KAYSERİSPOR   2 - 2   FRAPORT-TAV ANTALYASPOR     Detaylar Detaylar
09.02.2020 16:00        DEMİR GRUP SİVASSPOR    1 - 1   MEDİPOL BAŞAKŞEHİR FK   Detaylar Detaylar
09.02.2020 19:00        KASIMPAŞA A.Ş.  0 - 3   GALATASARAY A.Ş.    Detaylar Detaylar
10.02.2020 20:00        GÖZTEPE A.Ş.    -   ÇAYKUR RİZESPOR A.Ş.    Detaylar Detaylar
14.02.2020 20:00       MEDİPOL BAŞAKŞEHİR FK   -   BEŞİKTAŞ A.Ş.   Detaylar Detaylar
15.02.2020 14:00        YUKATEL DENİZLİSPOR     -   HES KABLO KAYSERİSPOR   Detaylar Detaylar
15.02.2020 17:00        İTTİFAK HOLDİNG KONYASPOR   -   GÖZTEPE A.Ş.    Detaylar Detaylar
15.02.2020 20:00        MKE ANKARAGÜCÜ  -   FENERBAHÇE A.Ş.     Detaylar Detaylar
16.02.2020 13:30        AYTEMİZ ALANYASPOR  -   GENÇLERBİRLİĞİ  Detaylar Detaylar
16.02.2020 16:00        TRABZONSPOR A.Ş.    -   DEMİR GRUP SİVASSPOR    Detaylar Detaylar
16.02.2020 19:00        GALATASARAY A.Ş.    -   BTC TURK YENİ MALATYASPOR   Detaylar Detaylar
17.02.2020 20:00        GAZİANTEP FUTBOL KULÜBÜ A.Ş.    -   ÇAYKUR RİZESPOR A.Ş.    Detaylar Detaylar
17.02.2020 20:00        FRAPORT-TAV ANTALYASPOR     -   KASIMPAŞA A.Ş.  Detaylar Detaylar
28.02.2020 20:00       AYTEMİZ ALANYASPOR  -   BEŞİKTAŞ A.Ş.   Detaylar Detaylar
29.02.2020 14:00        İTTİFAK HOLDİNG KONYASPOR   -   KASIMPAŞA A.Ş.  Detaylar Detaylar
29.02.2022 17:00        TRABZONSPOR A.Ş.    -   ÇAYKUR RİZESPOR A.Ş.    Detaylar Detaylar
29.02.2021 20:00        FRAPORT-TAV ANTALYASPOR     -   FENERBAHÇE A.Ş.     Detaylar Detaylar
01.03.2020 13:30        YUKATEL DENİZLİSPOR     -   BTC TURK YENİ MALATYASPOR   Detaylar Detaylar
01.03.2020 16:00        MKE ANKARAGÜCÜ  -   DEMİR GRUP SİVASSPOR    Detaylar Detaylar
01.03.2020 19:00        GALATASARAY A.Ş.    -   GENÇLERBİRLİĞİ  Detaylar Detaylar
02.03.2020 20:00        MEDİPOL BAŞAKŞEHİR FK   -   GAZİANTEP FUTBOL KULÜBÜ A.Ş.    Detaylar Detaylar
02.03.2020 20:00        HES KABLO KAYSERİSPOR   -   GÖZTEPE A.Ş.    Detaylar Detaylar'''

dateRegex = re.compile(r'''(
    (\d{2}) #DD
    (\-|\.) #- or .
    (\d{2}) #MM
    (\-|\.) #- or .
    (\d{4}) #Year
    )''', re.VERBOSE)


matches = []

for groups in dateRegex.findall(dates):
    date = '-'.join([groups[1], groups[3], groups[5]])
    # Some months can't be 31 days
    if groups[3] == ('04' or '06' or '09' or '11') and int(groups[1]) > 30:
        print(f'Error invalid date: {date}')
    # February exceptions
    if groups[3] == '02' and int(groups[1]) > 28 and int(groups[5]) % 4 != 0:
        print(f'Error invalid date: {date}')
    else:
        date = '-'.join([groups[1], groups[3], groups[5]])
        matches.append(date)


for i in matches:
    print(i, end='\n')
