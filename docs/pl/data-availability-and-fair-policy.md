# Dostępność danych i zasady FAIR

**Journal of AI-Assisted Research for Life Sciences**

**Status:** projekt do przyjęcia (wersja 0.1, 14 listopada 2026 r.).

**Język:** polski · [English version](../en/data-availability-and-fair-policy.md)

## 1. Cel

Wyniki empiryczne w tym czasopiśmie pochodzą z pracy wykonanej przez ludzi. Maszynopis może być szkicowany narzędziem generatywnym na podstawie tych wyników. Zbiór danych i kod analizy są sposobem, w jaki czytelnik, recenzent i wstępna recenzja AI sprawdzają, że tekst dotyczy pracy, która została wykonana.

Ta polityka wymaga, aby leżący u podstaw zbiór zebrany przez ludzi oraz kod, który go analizuje, zostały zdeponowane przed zgłoszeniem zgodnie z zasadami FAIR: odnajdywalne, dostępne, interoperacyjne i nadające się do ponownego użycia (ang. *Findable, Accessible, Interoperable, Reusable*; Wilkinson i współpracownicy, Scientific Data, 2016; [doi:10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)).

Wrażliwe dane zdrowotne podlegają zasadzie przyjętej w europejskiej praktyce danych badawczych: tak otwarte, jak to możliwe, tak zamknięte, jak to konieczne. Nie wymaga się depozytu publicznego, który zidentyfikowałby uczestnika albo którego zabrania prawo. Niedopuszczalny jest depozyt, którego recenzenci nie mogą otworzyć.

[Wytyczne dla autorów](author-guidelines.md) powtarzają minimum operacyjne. Ta strona jest pełną zasadą. Reguły rycin, które zależą od depozytu, są w [Polityce wykorzystania i ujawniania AI](ai-use-and-disclosure-policy.md).

## 2. Co się deponuje i kiedy

Przed zgłoszeniem autorzy deponują:

- zbiór potrzebny do powtórzenia opisanych analiz: nagrania, arkusze, obrazy albo transkrypcje stojące za tabelami, rycinami danych i wnioskami, na poziomie szczegółowości, którego używa artykuł;
- kod analizy, w tym skrypty budujące każdą rycinę danych i każdy wykres statystyczny, wraz z wersjami oprogramowania i ziarnem losowym, jeżeli skrypt go wymaga;
- słownik danych (książkę kodową), który określa każdą zmienną, jednostkę, dopuszczalną wartość i kod braku danych;
- plik README, który mówi, na czym polega badanie, jak uporządkowane są pliki, jak uruchomić analizę, jaka licencja obowiązuje, oraz podaje drogę kontaktu, którą obsługuje samo repozytorium;
- licencję, wskazaną w rekordzie repozytorium i w maszynopisie.

Repozytorium nadaje trwały identyfikator. Ustalenie robocze to DOI (Zenodo, Figshare, Dryad i OSF potrafią go nadać). Wymóg spełnia także numer akcesyjny dziedzinowy, który dana społeczność traktuje jako trwały (na przykład numer Sequence Read Archive albo Gene Expression Omnibus, lub numer o dostępie kontrolowanym, taki jak w European Genome-phenome Archive). Identyfikator cytuje się w piśmiennictwie i jest aktywny w chwili zgłoszenia. Formuła „zostanie zdeponowane po przyjęciu” nie spełnia tej polityki.

W liście przewodnim autorzy potwierdzają, że potrafią otworzyć pliki surowe i że te pliki są danymi stojącymi za tabelami, rycinami i wnioskami. Tego potwierdzenia nie składa za nich model.

Ponowna analiza istniejącego zbioru cytuje pierwotny identyfikator i licencję, na której autorzy z niego korzystali, oraz deponuje pliki pochodne i kod, które dają liczby w tym maszynopisie. Symulację deponuje się jako symulację: kod, ziarna i dane wejściowe, opisane jako symulowane.

## 3. Zasady FAIR

Cztery słowa są wymaganiami, a nie hasłem. Depozyt, który nie spełnia jednego z nich, jest niekompletny.

### 3.1 Odnajdywalne (Findable)

Rekord znajduje się w zaufanym repozytorium, które nadaje trwały identyfikator i udostępnia metadane czytelne dla maszyny. Właściwe repozytoria to między innymi Zenodo, OSF, Figshare, Dryad oraz repozytorium dziedzinowe, gdy ono jest standardowym miejscem dla danego rodzaju danych.

Metadane obejmują co najmniej: tytuł; twórców będących ludźmi, z ORCID tam, gdzie twórca go ma; opis badania i tego, co zawierają pliki; rok; słowa kluczowe albo dziedzinę; licencję; a gdy artykuł już istnieje — odnośnik do niego. Pliki są nazwane tak, aby czytelnik odróżnił dane surowe od kodu, książki kodowej i README bez otwierania każdego pliku.

Strona osobista, link do dysku chmurowego bez trwałego identyfikatora albo zapis istniejący wyłącznie w systemie zgłoszeń nie są depozytem.

### 3.2 Dostępne (Accessible)

Identyfikator otwiera stronę, która mówi, jak uzyskać pliki, także wtedy, gdy same pliki nie leżą w otwartej sieci.

Dostęp otwarty jest ustaleniem domyślnym dla danych, które można zgodnie z prawem i bezpiecznie upublicznić. Sposób pobrania jest podany (bezpośrednie pobranie albo kroki, które przechodzi wykwalifikowany badacz przy rekordzie o dostępie kontrolowanym).

Dostęp na czas recenzji jest częścią dostępności, a nie przysługą. W chwili zgłoszenia redakcja, wstępna recenzja AI i recenzenci będący ludźmi mogą otworzyć pliki, na których opiera się maszynopis. Część 6 mówi, jak to działa przy danych wrażliwych.

### 3.3 Interoperacyjne (Interoperable)

Tabele deponuje się w formacie otwartym i standardowym (CSV albo TSV, UTF-8, albo inny format, który badacz z danej dziedziny otworzy bez aktualnego wydania jednego dostawcy). Kod jest zwykłym tekstem. Obrazy danych pierwotnych mają format otwarty (na przykład TIFF albo PNG), gdy pozwala na to urządzenie. Plik własnościowy może leżeć obok kopii otwartej. Nie zastępuje jej.

Zrzut ekranu, PDF arkusza albo wygenerowany obraz wykresu nie są zbiorem danych i nie są ryciną statystyczną. Jednostki, kodowanie kategorii i relacje między tabelami są w książce kodowej, a nie pozostawione domysłowi czytelnika.

### 3.4 Nadające się do ponownego użycia (Reusable)

Licencja jest podana i jest taką, z której czytelnik może skorzystać. Dane powinny być udostępnione na licencji [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) albo [CC0](https://creativecommons.org/publicdomain/zero/1.0/), chyba że repozytorium lub zasada prywatności wymaga innej licencji otwartej albo reżimu dostępu kontrolowanego. Kod ma licencję zatwierdzoną przez OSI (na przykład MIT, Apache-2.0 albo GPL).

README i książka kodowa sprawiają, że pliki może ponownie wykorzystać ktoś, kto nie uczestniczył w badaniu. Metody i README są zgodne co do wersji oprogramowania, kryteriów włączenia i postępowania z brakami danych. Reguła czyszczenia określona przez człowieka jest opisana w Metodach i zapisana w zdeponowanym kodzie. Nie jest zezwoleniem, aby model wymyślał albo przepisywał obserwacje.

## 4. Oświadczenie o dostępności danych

Każdy artykuł ma oświadczenie o dostępności danych. Zgłoszenie bez niego jest niekompletne.

Oświadczenie podaje:

- repozytorium;
- trwały identyfikator jako link prowadzący do rekordu;
- licencję;
- co zdeponowano (zbiór, kod, książkę kodową, README oraz ewentualną część ograniczoną);
- czy dostęp jest otwarty, czy kontrolowany;
- jeżeli dostęp jest kontrolowany — barierę i procedurę, którą przechodzi wykwalifikowany badacz;
- że te pliki są danymi i kodem stojącymi za tabelami, rycinami danych i wnioskami.

Przykład poziomu szczegółowości, dla fikcyjnego depozytu otwartego:

> Indywidualne zapisy z platformy tensometrycznej, książka kodowa, README i kod analizy są zdeponowane w Zenodo (doi:10.5281/zenodo.0000000; CC BY 4.0). Te pliki są danymi stojącymi za tabelą 1, ryciną 2 i oszacowaniami w Wynikach. Rycinę 2 odtwarza `analysis/cmj_figures.R`.

Przykład oświadczenia o dostępie kontrolowanym:

> Indywidualnych rekordów zdrowotnych nie można opublikować, ponieważ uczestnicy mogliby zostać zidentyfikowani, a zgoda nie obejmuje upublicznienia. Zanonimizowane tabele zbiorcze, książka kodowa, README i kod analizy są w Zenodo (doi:10.5281/zenodo.0000000; CC BY 4.0). Plik indywidualny jest w dostępie kontrolowanym w [repozytorium, numer akcesyjny]. Wykwalifikowany badacz składa wniosek tak, jak opisuje to repozytorium. Redaktorzy i recenzenci mieli dostęp przez cały czas recenzji.

Formuła „dostępne u autorów na uzasadniony wniosek”, bez rekordu w repozytorium, nie spełnia tej polityki.

## 5. Wrażliwe dane zdrowotne

Dane zdrowotne, kliniczne i dane osób uprawiających sport są często danymi osobowymi. Gdy osoby, których dane dotyczą, są w Europejskim Obszarze Gospodarczym, autorzy spełniają rozporządzenie (UE) 2016/679 (ogólne rozporządzenie o ochronie danych, RODO) oraz warunki zgody komisji. Oświadczenie o wykorzystaniu AI nie naprawia bezprawnego przekazania.

Czasopismo używa tych słów w ich zwykłym znaczeniu prawnym:

- **Pseudonimizacja** usuwa albo zastępuje identyfikatory bezpośrednie, podczas gdy klucz albo zestaw pozostałych zmiennych nadal może wskazać osobę. Dane pseudonimowe nadal są danymi osobowymi.
- **Anonimizacja** oznacza, że ponowna identyfikacja nie jest rozsądnie prawdopodobna, także dla kogoś, kto zna okoliczności. Usunięcie kolumny z nazwiskiem z małej próby, przy pozostawieniu wieku, klubu, zawodów i rzadkiego pomiaru, nie jest anonimizacją.

Autorzy piszą, które z tych działań wykonali, w oświadczeniu etycznym i w README. Nie opisują pliku pseudonimowego jako anonimowego.

Depozyt publiczny jest największą częścią, która jest zgodna z prawem i bezpieczna: prawdziwie zanonimizowane dane jednostkowe, jeżeli takie są, albo tabele zbiorcze podpierające opublikowane liczby, oraz książka kodowa, README i kod. Pełniejszy plik, gdy musi pozostać ograniczony, trafia do repozytorium o dostępie kontrolowanym albo do udokumentowanej procedury dostępu, nadal z trwałym identyfikatorem.

Identyfikatorów bezpośrednich — nazwisk, danych kontaktowych, wizerunków twarzy, identyfikatorów urządzeń wskazujących osobę — nie umieszcza się w depozycie publicznym, chyba że zgoda komisji i konkretna zgoda obejmują publikację tych danych. Ta sama granica dotyczy danych wygenerowanych przez model, które autorzy mogliby chcieć oznaczyć jako obserwacje. To nie są obserwacje z badania. Zob. [Politykę wykorzystania i ujawniania AI](ai-use-and-disclosure-policy.md).

Bezpieczeństwo biologiczne i porównywalne bariery prawne prowadzi się tak samo: największy możliwy zbiór publicznie, zbiór ograniczony ścieżką kontrolowaną i powód w oświadczeniu. Podział przyjmuje redaktor będący człowiekiem. Redaktor nie przyjmuje braku depozytu.

## 6. Dostęp na czas recenzji

Recenzenci muszą mieć dostęp do danych w chwili zgłoszenia. Dotyczy to wstępnej recenzji AI i recenzentów będących ludźmi.

- Identyfikator otwiera się w momencie zgłoszenia maszynopisu.
- Przy depozycie otwartym link w maszynopisie i w liście przewodnim otwiera pliki.
- Przy depozycie o dostępie kontrolowanym autorzy zapewniają token recenzyjny, konto na czas określony albo równoważną drogę, która działa dla redakcji i dla recenzentów przez cały czas recenzji. Drogę opisuje list przewodni.
- Sprawdzenie zgodności przez AI działa wyłącznie na dopuszczalnym wdrożeniu, w rozumieniu [Polityki recenzji](peer-review-policy.md). Danych identyfikujących albo pseudonimowych na poziomie uczestnika nie wkleja się do publicznego modelu konsumenckiego.
- Jeżeli warunki dostępu albo zgoda komisji zabraniają pokazania pliku modelowi, członek redakcji będący człowiekiem wykonuje sprawdzenie liczb względem tego pliku, a raport oznacza krok modelu jako „Nie oceniano” dla tego pliku i podaje powód. Recenzenci będący ludźmi i tak otrzymują dostęp.

Maszynopisu nie wysyła się do recenzji ludzkiej, dopóki link do danych się nie otwiera, recenzenci nie mogą otworzyć plików albo ścieżka dostępu kontrolowanego jest jedynie obietnicą.

## 7. Kod i ryciny danych

Ryciny danych i wykresy statystyczne powstają ze zdeponowanego kodu na podstawie zdeponowanych danych surowych. Nie są obrazami wygenerowanymi. Skrypt, dane wejściowe, które czyta, i wersje oprogramowania są w depozycie. Autor będący człowiekiem uruchomił skrypt.

Schematy metodyczne, które nie pokazują obserwacji ani oszacowań, mogą powstawać ze wsparciem AI. To użycie jest ujawnione. Nie zmienia obowiązku depozytu danych i kodu analizy. Zasady rycin są w [Polityce wykorzystania i ujawniania AI](ai-use-and-disclosure-policy.md) i w [Wytycznych dla autorów](author-guidelines.md).

Kod pisany ze wsparciem AI jest ujawniony. Odpowiedzialność ponosi autor będący człowiekiem, który kod rozumie i który go uruchomił. Kod, którego autorzy nie potrafią objaśnić, jest niedopuszczalny. Wynik generatywny nie jest zbiorem imputowanym. Ewentualna imputacja jest określona przez ludzi, opisana i odróżniona od danych surowych.

## 8. Po publikacji

Wersja ostateczna prowadzi do oświadczenia o dostępności danych i do trwałego identyfikatora. Jeżeli wykryto błąd, autorzy wersjonują rekord w repozytorium, a czasopismo łączy sprostowanie z oboma identyfikatorami. Pierwotnego depozytu nie nadpisuje się po cichu.

Czytelnik, który nie potrafi odtworzyć podanych liczb z depozytu, znalazł problem z artykułem. Redaktor traktuje to jako pytanie o rzetelność według [Etyki publikacyjnej](publication-ethics.md), niezależnie od tego, czy przyczyną jest uczciwy błąd, czy maszynopis, który model napisał obok danych.

## 9. Dokumenty powiązane

- [Wytyczne dla autorów](author-guidelines.md)
- [Polityka wykorzystania i ujawniania AI](ai-use-and-disclosure-policy.md)
- [Polityka recenzji](peer-review-policy.md)
- [Etyka publikacyjna](publication-ethics.md)
- [Cele i zakres](aims-and-scope.md)
