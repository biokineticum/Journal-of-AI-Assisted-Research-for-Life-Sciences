# Polityka recenzji

**Journal of AI-Assisted Research for Life Sciences**

**Status:** projekt do przyjęcia (wersja 0.1, 14 listopada 2026 r.).

**Język:** polski · [English version](../en/peer-review-policy.md)

## 1. Zasady

Czasopismo prowadzi dwie rundy recenzji o różnych zadaniach.

- **Runda 1** to wstępna recenzja AI. Wykonuje ją model, jest tak nazwana i sprawdza kompletność, ujawnienie, zgodność, cytowania oraz sygnały ostrzegawcze.
- **Runda 2** to recenzja ekspercka ludzi. Recenzenci oceniają metodykę, interpretację i nowość oraz wypowiadają się, czy wykorzystanie AI i nadzór człowieka wyglądają na wystarczające.
- **Decyzję** podejmuje redaktor będący człowiekiem. Model nie przyjmuje, nie kieruje do poprawy i nie odrzuca maszynopisu.

W tym projekcie recenzja jest pojedynczo anonimowa: recenzenci znają autorów, a autorom nie podaje się nazwisk recenzentów. Recenzent może podpisać recenzję. Nazwisko redaktora widnieje w liście decyzyjnym.

Cele robocze, do potwierdzenia przed uruchomieniem: wstępna recenzja AI w ciągu 10 dni od kompletnego zgłoszenia mieszczącego się w zakresie; recenzje w ciągu 21 dni od przyjęcia zaproszenia; pierwsza decyzja w ciągu 8 tygodni. Są to cele, a nie obietnica określonego rozstrzygnięcia.

## 2. Poufność

Maszynopis, dane przekazane do recenzji, recenzje i decyzja są poufne.

Redakcja, redaktorzy i recenzenci nie wgrywają żadnego z tych materiałów do publicznego modelu konsumenckiego (usługi, która może uczyć się na danych wejściowych albo która nie ma pisemnych warunków braku trenowania i ograniczonego przechowywania).

Wstępna recenzja AI działa wyłącznie na **dopuszczalnym wdrożeniu**: modelu lokalnym albo usłudze korporacyjnej lub API objętej pisemną umową, że zgłoszenia nie służą do trenowania i nie są przechowywane dłużej, niż wymaga recenzja. Ta sama zasada dotyczy późniejszego, wspomaganego przez AI sprawdzenia poprawki.

Pracownicy i wykonawcy, którzy mają styczność ze zgłoszeniami, pracują według tej zasady poufności. Autorzy nie umieszczają poufnej treści recenzji ani listów decyzyjnych w publicznym modelu.

## 3. Przebieg

1. **Wstępna selekcja** przez redaktora będącego człowiekiem: zakres, integralność plików i oczywiste niespełnienie wymogów minimalnych.
2. **Runda 1 — wstępna recenzja AI** zgłoszeń w zakresie, a następnie sprawdzenie raportu przez człowieka, zanim raport zostanie przekazany dalej.
3. **Uzupełnienie**, jeżeli redaktor prosi autorów o zamknięcie luk formalnych przed recenzją ludzką.
4. **Runda 2 — co najmniej dwóch niezależnych recenzentów będących ludźmi.**
5. **Decyzja** redaktora będącego człowiekiem: przyjęcie, drobne poprawki, zasadnicze poprawki albo odrzucenie.
6. **Sprawdzenie poprawek.** Dopuszczalny model może pomóc porównać poprawkę z listem decyzyjnym. Redaktor decyduje, czy recenzenci zobaczą ją ponownie.
7. **Przyjęcie** dopiero wtedy, gdy redaktor będący człowiekiem jest przekonany co do nauki, etyki, danych i ujawnienia.

Maszynopisy spoza zakresu są odrzucane na etapie selekcji i nie są wysyłane do modelu.

## 4. Wstępna selekcja

Redaktor będący człowiekiem albo upoważniony członek redakcji sprawdza, czy:

- maszynopis mieści się w [celach i zakresie](aims-and-scope.md);
- pliki się otwierają i są obecne części wymagane w [Wytycznych dla autorów](author-guidelines.md);
- autorami są ludzie i żadne narzędzie AI nie jest wskazane jako autor.

Jeżeli maszynopis jest poza zakresem, redaktor odrzuca go z krótkim uzasadnieniem. Jeżeli brakuje wymaganych części, redakcja może raz zwrócić tekst do uzupełnienia formalnego albo go odrzucić. Selekcja nie jest recenzją naukową i nie jest oceną nowości.

## 5. Runda 1 — wstępna recenzja AI

### 5.1 Czym jest

Redakcja przeprowadza ustrukturyzowane sprawdzenie nazwanym modelem i wersją na dopuszczalnym wdrożeniu. Sprawdzenie obejmuje pytania ze wzoru raportu na końcu tej polityki. Dotyczy:

- kompletności i struktury maszynopisu;
- obecności i wystarczalności ujawnienia AI, w tym pliku z promptami i oświadczenia o weryfikacji;
- zgodności tekstu, tabel, rycin i zdeponowanych danych, w granicach tego, na co pozwalają pliki;
- sprawdzenia cytowań (czy wskazane pozycje wydają się istnieć i — w sprawdzeniu próby albo całości — wspierać twierdzenia);
- plagiatu i innych sygnałów naruszenia rzetelności, łącznie z programem antyplagiatowym czasopisma, gdy ta usługa już działa;
- obecności i konkretności oświadczeń o etyce, zgodzie, rejestracji i konfliktach interesów.

### 5.2 Czym nie jest

Wstępna recenzja nie ocenia, czy badanie warto było przeprowadzić, czy schemat był właściwy ani czy interpretacja jest najlepsza z dostępnych. Nie potwierdza, że eksperyment się odbył. Nie uwierzytelnia obrazów. Nie rozstrzyga losu maszynopisu.

Wynik modelu może być błędny. Cytowanie oznaczone jako zmyślone, ślad plagiatu albo rozbieżność liczbowa są tropem dla człowieka, a nie ustaleniem, dopóki człowiek ich nie sprawdzi.

### 5.3 Sprawdzenie przez człowieka przed wysłaniem raportu

Wskazany członek redakcji czyta wynik modelu, zanim zobaczą go autorzy lub recenzenci.

- Zarzuty, których pracownik nie potrafi odtworzyć, są usuwane albo oznaczane „nie potwierdzono — nie jest to pytanie do autorów”.
- Pracownik nie dopisuje naukowej pochwały ani nagany głosem modelu.
- Przekazany raport nadal podaje, który model i która wersja przygotowały szkic oraz kto go sprawdził.

Autorów nie prosi się o odpowiedź na niepotwierdzony zarzut AI.

### 5.4 Kto otrzymuje raport

Sprawdzony raport trafia do autorów i do redaktora prowadzącego. Trafia do recenzentów rundy 2 wraz z maszynopisem. Pozostaje w dokumentacji redakcyjnej razem z wersją modelu, datą, rodzajem wdrożenia i promptem redakcji.

W tym projekcie raportu nie publikuje się wraz z artykułem. Artykuł stwierdza, że wstępna recenzja AI się odbyła. Rada może później zdecydować o publikowaniu raportów. Ten wybór jest wymieniony w [harmonogramie uruchomienia](launch-roadmap.md).

### 5.5 Wyniki rundy 1

Model nie rekomenduje przyjęcia ani odrzucenia. Redaktor będący człowiekiem wybiera jeden wynik administracyjny:

- **Przekazać do recenzji ludzkiej.**
- **Zwrócić do uzupełnienia.** Redaktor wskazuje autorom, czego brakuje (na przykład niepodpisanej weryfikacji, martwego linku do danych, brakującego numeru zgody). To nie jest poprawka naukowa.
- **Eskalować.** Redaktor podejmuje sygnał naruszenia rzetelności — taki jak potwierdzone przez pracownika zmyślone cytowanie, liczby niezgodne z tabelą albo brak oświadczenia etycznego przy badaniu, które go wymaga — i prowadzi sprawę według [Etyki publikacyjnej](publication-ethics.md). Raport AI jest źródłem sprawdzeń, nie wyrokiem.

## 6. Między rundami

Autorzy poproszeni o uzupełnienie formalne składają tekst ze śledzeniem zmian i krótką odpowiedź. Redakcja potwierdza, że luki wskazane przez redaktora zostały zamknięte. Dopuszczalny model może pomóc w tym potwierdzeniu. Redaktor przekazuje plik recenzentom.

Maszynopisu nie wysyła się do rundy 2, dopóki brakuje ujawnienia AI, link do danych surowych się nie otwiera albo brakuje wymaganego oświadczenia o etyce lub rejestracji bez przyjętego wyjaśnienia.

## 7. Runda 2 — ekspercka recenzja ludzka

Redaktor prowadzący zaprasza co najmniej dwóch recenzentów o odpowiednim dorobku, których konflikt interesów nie wyklucza. Recenzenci są badaczami lub praktykami będącymi ludźmi. Modelu nie zaprasza się jako recenzenta.

Redaktor może zaprosić dodatkowego recenzenta do statystyki, metod albo drugiej dziedziny. Jeżeli dwa raporty są sprzeczne, redaktor może zaprosić trzeciego recenzenta albo rozstrzygnąć na podstawie raportów, maszynopisu i własnej lektury. List decyzyjny podaje podstawę rozstrzygnięcia.

Recenzenci otrzymują:

- maszynopis i ryciny;
- oświadczenie o wykorzystaniu AI i plik z promptami;
- dostęp do zdeponowanych danych i kodu albo do ścieżki dostępu wyłącznie na czas recenzji;
- sprawdzony raport wstępnej recenzji AI;
- pytania z tej polityki.

Proponowany termin raportu to 21 dni. Redakcja wysyła jedno przypomnienie. Recenzenta, który nie może skończyć, zastępuje się. Tożsamości zastępcy nie ujawnia się autorom, jeżeli recenzja jest anonimowa.

## 8. O co pyta się recenzentów

Recenzenci wypowiadają się o tym:

1. czy schemat badania może odpowiedzieć na pytanie i czy metody są opisane dostatecznie, aby badanie powtórzyć;
2. czy analiza odpowiada schematowi i czy liczby w tekście zgadzają się z tabelami i rycinami;
3. czy interpretacja mieści się w danych;
4. co badanie wnosi, bez mylenia nowości z powodem, aby pominąć rzetelny wynik zerowy;
5. czy etyka, zgoda, rejestracja i dostępność danych są wystarczające dla danego schematu;
6. **czy ujawnione użycie AI jest właściwe i czy nadzór człowieka wygląda na wystarczający** względem tekstu, kodu, rycin, liczb i cytowań;
7. czy któreś cytowanie nie istnieje albo nie wspiera twierdzenia;
8. czy jest ślad, że dane pierwotne lub obrazy danych pierwotnych zostały wygenerowane albo zmienione przez model.

Recenzentów nie prosi się o ponowne uruchomienie każdej analizy. Prosi się ich, aby powiedzieli, jeżeli zdeponowany materiał nie wystarcza do podparcia twierdzeń.

Recenzent, który uważa, że ujawnienie jest niepełne albo nadzór był niewystarczający, pisze to wprost. Taka uwaga jest podstawą, aby redaktor zapytał autorów. Sama w sobie nie jest rekomendacją, którą redaktor musi wykonać bez lektury maszynopisu.

## 9. Obowiązki recenzenta

Recenzenci:

- ujawniają konflikty interesów przed przyjęciem zaproszenia, w tym niedawną współpracę, wspólną instytucję tam, gdzie konflikt jest rzeczywisty, albo interes finansowy w badanej interwencji lub narzędziu;
- traktują pliki jako poufne, także po złożeniu rekomendacji;
- nie używają publicznego modelu konsumenckiego wobec maszynopisu, danych, raportu AI ani recenzji;
- jeżeli w ogóle korzystają z dopuszczalnego wdrożenia, informują redaktora, jakiego narzędzia i jakiej wersji użyli, i potwierdzają warunki braku trenowania — złożona recenzja pozostaje ich własną oceną;
- nie żądają cytowania własnych prac, chyba że jest to niezbędne naukowo;
- nie kontaktują się z autorami bezpośrednio w sprawie zgłoszenia;
- zawiadamiają redakcję, jeżeli rozpoznają maszynopis, którego nie mogą ocenić rzetelnie.

Redakcja nie korzysta z sugestii recenzentów wygenerowanych przez publiczny model konsumencki. Sugestie z dopuszczalnego narzędzia, jeżeli kiedykolwiek zostaną użyte, redaktor sprawdza względem rzeczywistych publikacji i konfliktów, zanim wyśle zaproszenie.

## 10. Decyzja

Decyzję podejmuje redaktor będący człowiekiem i podpisuje list. Redaktor czyta maszynopis, raport AI i recenzje ludzkie. Redaktor nie jest związany rekomendacją bez uzasadnienia, wrogą albo sprzeczną z zasadami czasopisma. Redaktor nie idzie za rekomendacją przyjęcia pracy, której ujawnienie, dane albo oświadczenia etyczne nie spełniają wymogów minimalnych.

| Decyzja | Znaczenie |
| --- | --- |
| Przyjęcie | Redaktor jest przekonany. Pozostałe zmiany ograniczają się do pytań produkcyjnych. |
| Drobne poprawki | Wskazane zmiany, zwykle sprawdzane przez redaktora. Ponowna recenzja ludzka jest fakultatywna. |
| Zasadnicze poprawki | Zmiany istotne. Ponowna recenzja ludzka jest zasadą. Przyjęcia się nie obiecuje. |
| Odrzucenie | Maszynopis nie przechodzi dalej. Nowe zgłoszenie tego samego badania jest dopuszczalne tylko wtedy, gdy list redaktora tak stanowi. |

Nie ma płatnego szybkiego toru i żadnej decyzji nie wymienia się na cytowanie albo opłatę.

Redaktor nie rozstrzyga maszynopisu, który sam napisał, ani takiego, przy którym konflikt interesów czyni rzetelną decyzję nierozsądną. Taki plik prowadzi inny redaktor. Jeżeli każdy redaktor jest w konflikcie, czasopismo prosi redaktora gościnnego spoza rady i odnotowuje to rozwiązanie.

## 11. Poprawki i późniejsze kontrole AI

Autorzy odpowiadają punkt po punkcie. Aktualizują oświadczenie o wykorzystaniu AI, jeżeli przy poprawce pojawiło się nowe narzędzie albo nowe zastosowanie. Ciche rozszerzenie użycia AI na etapie poprawki jest użyciem nieujawnionym.

Redakcja może uruchomić dopuszczalny model, aby zestawić, co się zmieniło względem listu decyzyjnego i czy wcześniej wskazane liczby, linki i cytowania już się zgadzają. Redaktor będący człowiekiem czyta to zestawienie. Gdy poprawka zmienia analizę, próbę, interpretację albo obrazy, redaktor odsyła ją co najmniej jednemu recenzentowi będącemu człowiekiem, chyba że obaj recenzenci ograniczyli prośby do rzeczy, które redaktor może sprawdzić bezpośrednio.

## 12. Odwołania

Autorzy mogą raz odwołać się od odrzucenia, na piśmie, na adres [EMAIL], w ciągu 30 dni od decyzji. Odwołanie wskazuje błąd faktyczny lub proceduralny. Nie jest ponownym zgłoszeniem.

Odwołanie rozpatruje redaktor będący człowiekiem, który nie był redaktorem rozstrzygającym, o ile w radzie jest więcej niż jeden redaktor. Może on zasięgnąć opinii nowego recenzenta. Raport wstępnej recenzji AI nie jest decyzją zaskarżalną, ponieważ nie jest decyzją. Wynikiem odwołania jest: uwzględnienie i dalsza recenzja, zaproszenie do poprawki albo utrzymanie odrzucenia. Decyzja w odwołaniu jest ostateczna dla tego maszynopisu.

Skargi na postępowanie, stronniczość albo nieujawnione użycie AI prowadzi się według [Etyki publikacyjnej](publication-ethics.md).

## 13. Co się mówi czytelnikom

Opublikowany artykuł stwierdza, że recenzja obejmowała wstępną recenzję AI i ekspercką recenzję ludzką oraz że decyzję podjął redaktor będący człowiekiem. Nie podaje nazwisk recenzentów, chyba że podpisali recenzję, a rada zgodziła się ten podpis opublikować.

Nazwa i wersja modelu użytego w rundzie 1 są zapisane w dokumentacji redakcyjnej. Rada przed uruchomieniem decyduje, czy nazwa modelu jest także drukowana przy artykule. Do tej decyzji publiczne zdanie nie wymyśla nazwy modelu. Zob. [harmonogram uruchomienia](launch-roadmap.md).

## 14. Dokumenty powiązane

- [Polityka wykorzystania i ujawniania AI](ai-use-and-disclosure-policy.md)
- [Etyka publikacyjna](publication-ethics.md)
- [Wytyczne dla autorów](author-guidelines.md)

---

## Załącznik. Wstępna recenzja AI — wzór raportu

Redakcja kopiuje ten wzór dla każdego maszynopisu. Tekst w nawiasach jest zastępowany. Przekazany raport zachowuje ostrzeżenie u góry.

---

### WSTĘPNA RECENZJA AI

**Ten raport został przygotowany w szkicu przez system AI i sprawdzony przez członka redakcji. Nie jest recenzją naukową i nie jest decyzją.**

| Pole | Wpis |
| --- | --- |
| Czasopismo | Journal of AI-Assisted Research for Life Sciences |
| Identyfikator maszynopisu | [ID] |
| Tytuł | [TYTUŁ] |
| Data uruchomienia modelu | [RRRR-MM-DD] |
| Model i wersja | [MODEL I WERSJA] |
| Wdrożenie | [lokalne / korporacyjne — dostawca]. Brak trenowania i ograniczone przechowywanie: [tak, oznaczenie umowy] |
| Wersja promptu redakcji | [identyfikator promptu wewnętrznego, przechowywany w dokumentacji] |
| Osoba sprawdzająca | [ROLA, nie nazwisko recenzenta publicznego — np. redakcja]. Data sprawdzenia: [RRRR-MM-DD] |
| Program antyplagiatowy | [NAZWA I WERSJA NARZĘDZIA albo „jeszcze nie użyto”] |

**Informacja dla autorów i recenzentów.** Model nie decyduje o przyjęciu. Nie ustala, że badanie się odbyło. Sygnały poniżej są pytaniami tylko tam, gdzie osoba sprawdzająca je potwierdziła. Pozycje oznaczone „nie potwierdzono” nie wymagają odpowiedzi.

### Lista kontrolna

Należy użyć wartości **Spełnione**, **Luka** albo **Nie oceniano**. Przy każdej luce jest jedno zdanie. Przy każdym „Nie oceniano” jest powód (na przykład „pełne teksty cytowanych prac nie były dostępne dla modelu”).

| # | Pytanie | Wynik | Uwaga |
| --- | --- | --- | --- |
| 1 | Dla tego rodzaju artykułu są obecne wymagane części (tytuł, autorzy będący ludźmi i afiliacje, streszczenie strukturalne, słowa kluczowe, wstęp, metody, wyniki, dyskusja, dostępność danych, etyka, odesłanie do ujawnienia AI, finansowanie, konflikty interesów, piśmiennictwo). | | |
| 2 | W nagłówku są wyłącznie ludzie. Autorem nie jest model, firma ani program. | | |
| 3 | Oświadczenie o wykorzystaniu AI jest obecne i podaje narzędzia, wersje, tryb dostępu, zastosowania, plik z promptami oraz osoby, które wykonały weryfikację. | | |
| 4 | Oświadczenie zgadza się z maszynopisem (narzędzia wspomniane w tekście są ujawnione; ujawnione zastosowania widać tam, gdzie je wskazano). | | |
| 5 | Jeżeli zadeklarowano brak AI, nic w pliku tej deklaracji nie zaprzecza. | | |
| 6 | Oświadczenie o dostępności danych podaje repozytorium i identyfikator. Identyfikator się otwiera albo opisano, dlaczego się nie otwiera. | | |
| 7 | Sprawdzenie wyrywkowe: liczby w streszczeniu i wynikach zgadzają się z tabelami i rycinami. Wymienić każdą rozbieżność. | | |
| 8 | Sprawdzenie wyrywkowe: kompetentny czytelnik może powiązać opisane analizy ze zdeponowanymi plikami. | | |
| 9 | Cytowania: podać, ile sprawdzono i jaką metodą. Wymienić pozycje, które wydają się nie istnieć albo nie wspierać twierdzenia, tylko jeżeli listę potwierdziła osoba sprawdzająca. | | |
| 10 | Badanie podobieństwa / plagiatu: narzędzie, wynik punktowy jeżeli jest, oraz wniosek osoby sprawdzającej. Zbieżność ograniczoną do szablonowych metod należy tak opisać. | | |
| 11 | Etyka, zgoda, dobrostan zwierząt, zezwolenia oraz rejestracja badania lub protokołu są obecne i konkretne albo obecne jest uzasadnione „nie dotyczy”. | | |
| 12 | Konflikty interesów i finansowanie są podane, w tym „brak”, jeżeli takie jest twierdzenie. | | |
| 13 | Zasady rycin: obrazy danych pierwotnych są przedstawione jako oryginalne zapisy; wykresy wspomagane przez AI są ujawnione; żaden oczywisty artefakt generatywny nie pozostaje bez opisu. Model nie może uwierzytelnić obrazu. | | |
| 14 | Wskazano właściwy standard raportowania (CONSORT, STROBE, ARRIVE, PRISMA albo inny z wytycznych dla autorów), a lista kontrolna jest dołączona, gdy standard jej oczekuje. | | |
| 15 | Schemat badania jest pracą empiryczną wykonaną przez ludzi, o ile pokazują to tekst i pliki. Symulacje są opisane jako symulacje. | | |

### Sygnały ostrzegawcze potwierdzone przez osobę sprawdzającą

[Brak / lista; przy każdej pozycji miejsce w pliku i to, co sprawdzono ręcznie.]

### Tropy, których osoba sprawdzająca nie potwierdziła

[Brak / lista, oznaczona jako nieprzeznaczona dla autorów.]

### Czego ta recenzja nie oceniała

- nowości i znaczenia naukowego;
- tego, czy schemat był właściwy, poza oczywistymi lukami wewnętrznymi;
- tego, czy dane rzeczywiście zebrano;
- prawdziwości niebadanych plików obrazów;
- poprawności analiz, których nie przeliczono ponownie.

### Rekomendacja administracyjna dla redaktora

Zaznaczyć jedno. Nie zaznaczać decyzji o przyjęciu ani o odrzuceniu.

- [ ] Przekazać do recenzji ludzkiej
- [ ] Zwrócić autorom do uzupełnienia (wymienić luki)
- [ ] Eskalować do redaktora prowadzącego jako sygnał naruszenia rzetelności (wymienić potwierdzone sygnały)

**Potwierdzenie osoby sprawdzającej:** Potwierdzam, że ten raport został przeze mnie przeczytany, a niepotwierdzone zarzuty zostały usunięte albo oznaczone. Podpis / imię i nazwisko oraz data: [IMIĘ I NAZWISKO, ROLA, DATA]

---

### Prompt wewnętrzny — minimalne instrukcje

Redakcja używa promptu na piśmie, który zawiera co najmniej następujące polecenia i jest przechowywany z identyfikatorem wersji:

1. Wykonujesz wstępną recenzję AI dla czasopisma *Journal of AI-Assisted Research for Life Sciences*. Nie rekomendujesz przyjęcia ani odrzucenia.
2. Korzystaj wyłącznie z przekazanych plików. Nie przeglądaj sieci i nie wysyłaj plików do żadnej innej usługi.
3. Wypełnij listę kontrolną. Użyj wartości Spełnione, Luka albo Nie oceniano.
4. Nie wymyślaj cytowań, cytatów ani rozbieżności liczbowych. Jeżeli nie możesz czegoś sprawdzić, oznacz to jako Nie oceniano.
5. Nie przepisuj maszynopisu.
6. Traktuj pliki jako poufne.
