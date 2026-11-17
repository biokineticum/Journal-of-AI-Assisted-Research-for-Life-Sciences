# Polityka recenzji

**Journal of AI-Assisted Research for Life Sciences**

**Status:** projekt do przyjęcia (wersja 0.1, 14 listopada 2026 r.).

**Język:** polski · [English version](../en/peer-review-policy.md)

## 1. Zasady

Czasopismo prowadzi dwie rundy recenzji o różnych zadaniach.

- **Runda 1** to wstępna recenzja AI. Jest to sprawdzenie wieloskładnikowe, wyraźnie tak nazwane, wzorowane na projekcie ScholarPeer i dostosowane do tego czasopisma (część 5). Sprawdza kontekst literatury, pominięte punkty odniesienia i zbiory, twierdzenia, zgodność maszynopisu ze zdeponowanymi danymi, raportowanie i etykę oraz cytowania. Nie rozstrzyga losu pracy.
- **Runda 2** to recenzja ekspercka ludzi. Recenzenci oceniają metodykę, interpretację i nowość oraz wypowiadają się, czy wykorzystanie AI i nadzór człowieka wyglądają na wystarczające.
- **Decyzję** podejmuje redaktor będący człowiekiem. Model nie przyjmuje, nie kieruje do poprawy i nie odrzuca maszynopisu.

W tym projekcie recenzja jest pojedynczo anonimowa: recenzenci znają autorów, a autorom nie podaje się nazwisk recenzentów. Recenzent może podpisać recenzję. Nazwisko redaktora widnieje w liście decyzyjnym.

Cele robocze, do potwierdzenia przed uruchomieniem: wstępna recenzja AI w ciągu 10 dni od kompletnego zgłoszenia mieszczącego się w zakresie; recenzje w ciągu 21 dni od przyjęcia zaproszenia; pierwsza decyzja w ciągu 8 tygodni. Są to cele, a nie obietnica określonego rozstrzygnięcia.

## 2. Poufność

Maszynopis, dane przekazane do recenzji, kod, recenzje i decyzja są poufne.

Wstępna recenzja AI oraz każde późniejsze, wspomagane przez AI sprawdzenie poprawki działa wyłącznie na **modelach hostowanych lokalnie**. Są to modele językowe o otwartych wagach, które czasopismo uruchamia na infrastrukturze, którą samo kontroluje. Maszynopisów, zbiorów danych, kodu analizy i materiałów recenzentów nigdy nie wysyła się do zewnętrznego API AI, w tym API podmiotu trzeciego. Pisemna obietnica, że dostawca nie będzie trenował na plikach, nie czyni zewnętrznego API dopuszczalnym. Pliki nie opuszczają infrastruktury czasopisma.

Kontekst literatury i weryfikacja cytowań potrzebują wyszukań, których model lokalny nie wykona z samych plików. Te wyszukania mogą korzystać z bazy literatury, resolvera DOI, Crossref, PubMed albo wyszukiwania w sieci. Infrastrukturę opuszcza ogólne zapytanie wyszukiwawcze albo identyfikator bibliograficzny (DOI, PMID, tytuł albo ciąg autor–rok z przypisu). Tekst maszynopisu, dane, kod, recenzje i wszystko, co identyfikuje zgłaszających autorów, nie opuszczają infrastruktury. Jeżeli zapytania nie da się ułożyć w tej granicy, redakcja dostarcza pakiet literatury, a raport stwierdza, że wyszukania nie uruchomiono.

Pracownicy, redaktorzy i recenzenci nie wgrywają maszynopisu, danych, kodu ani recenzji do zewnętrznej usługi AI. Autorzy nie umieszczają poufnej treści recenzji ani listów decyzyjnych w żadnym narzędziu AI.

## 3. Przebieg

1. **Wstępna selekcja** przez redaktora będącego człowiekiem: zakres, integralność plików i oczywiste niespełnienie wymogów minimalnych.
2. **Runda 1 — wstępna recenzja AI** zgłoszeń w zakresie, a następnie sprawdzenie raportu przez człowieka, zanim raport zostanie przekazany dalej.
3. **Uzupełnienie**, jeżeli redaktor prosi autorów o zamknięcie luk formalnych przed recenzją ludzką.
4. **Runda 2 — co najmniej dwóch niezależnych recenzentów będących ludźmi.**
5. **Decyzja** redaktora będącego człowiekiem: przyjęcie, drobne poprawki, zasadnicze poprawki albo odrzucenie.
6. **Sprawdzenie poprawek.** Te same modele hostowane lokalnie mogą pomóc porównać poprawkę z listem decyzyjnym. Poprawki nie wysyła się do zewnętrznego API AI. Redaktor decyduje, czy recenzenci zobaczą ją ponownie.
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

Redakcja przeprowadza ustrukturyzowaną, wieloskładnikową wstępną recenzję na infrastrukturze, którą kontroluje, przy użyciu modeli o otwartych wagach, które sama hostuje. Żaden składnik nie wywołuje zewnętrznego API AI, w tym API podmiotu trzeciego. Projekt jest wzorowany na ScholarPeer, agencie recenzyjnym opisanym przez Jinsunga Yoona i Tomasa Pfistera we wpisie na blogu Google Research „Improving the academic workflow: introducing two AI agents for better figures and peer review” (8 kwietnia 2026 r.): [research.google/blog](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/).

Ten wpis jest źródłem projektu. Nie jest zależnością. Czasopismo nie wymaga ScholarPeer, Google ani żadnego innego nazwanego produktu i nie wysyła maszynopisu do tych dostawców. Składniki poniżej realizuje się lokalnymi modelami i skryptami, które redakcja zapisze w dzienniku. ScholarPeer, w opisie z tego wpisu, oceniano na artykułach z uczenia maszynowego i na zbiorach do automatycznej recenzji. Nie oceniano go jako recenzenta maszynopisów z nauk o zdrowiu, o sporcie ani z innych nauk o życiu. To czasopismo dostosowuje tę architekturę do takich maszynopisów i dodaje sprawdzenia, których opublikowany opis nie przewiduje.

Każde narzędzie, model i wersja oraz infrastruktura, na której działały, są wpisywane do raportu i do dokumentacji redakcyjnej. Przebieg, który ich nie nazywa, nie jest zakończoną rundą 1.

Potok ma następujące składniki. Każdy wpisuje się do tego samego raportu. Żaden nie rekomenduje przyjęcia ani odrzucenia.

**Kontekst literatury (historyk poddziedziny).** Krótka, oparta na źródłach notatka o poddziedzinie, w której maszynopis się sytuuje, sporządzona z opublikowanej literatury. Jest kontekstem dla późniejszych sprawdzeń. Nie jest przeglądem literatury, który czasopismo publikuje, i nie jest werdyktem o nowości.

**Pominięte punkty odniesienia i zbiory.** Poszukiwanie standardowych zbiorów, komparatorów albo metod odniesienia, których maszynopis nie wymienia. Trafienie jest pytaniem do autorów albo do recenzentów. Nie jest ustaleniem, że autorzy zawiedli.

**Wielowątkowa weryfikacja twierdzeń.** Pytania i odpowiedzi o twierdzenia, obejmujące schemat, pomiar, analizę i interpretację. Każda odpowiedź wskazuje fragment tekstu albo plik. Rozbieżność między odpowiedzią a maszynopisem zapisuje się jako pytanie, nie jako decyzję.

**Zgodność danych z maszynopisem.** Ten składnik jest właściwy temu czasopismu. Każdą liczbę, każdą statystykę i każdy wniosek w maszynopisie sprawdza się względem zdeponowanego zbioru i zdeponowanego kodu, według [Dostępności danych i zasad FAIR](data-availability-and-fair-policy.md). Sprawdzenie obejmuje maszynopis szkicowany z użyciem AI. Tam, gdzie zdeponowany kod da się uruchomić na tej samej infrastrukturze lokalnej, analizy przelicza się ponownie, a wynik porównuje z tekstem, tabelami i rycinami danych. Dane o dostępie kontrolowanym czyta się wyłącznie w tym środowisku. Nie kopiuje się ich na zewnątrz po to, aby uruchomić sprawdzenie. Wartość, której nie da się przeliczyć, oznacza się jako „Nie oceniano”, z powodem (brak pliku, kod, który się nie uruchamia, albo dane, których środowisko lokalne nie może przechowywać). Ustalenia trafiają do części raportu o zgodności danych.

**Raportowanie, etyka i rejestracja.** Ten składnik jest właściwy temu czasopismu. Maszynopis sprawdza się względem standardu raportowania pasującego do schematu. Listą roboczą jest tabela w [Wytycznych dla autorów](author-guidelines.md): CONSORT, STROBE, PRISMA, ARRIVE, SPIRIT i pozostałe tam wymienione. [EQUATOR Network](https://www.equator-network.org/) jest indeksem, z którego redakcja potwierdza, który standard i która aktualna wersja mają zastosowanie. Sprawdzenie pyta także, czy zgoda komisji oraz rejestracja badania lub protokołu są obecne i konkretne, albo czy obecne jest uzasadnione „nie dotyczy”.

**Istnienie i trafność cytowań.** Ten składnik jest właściwy temu czasopismu. Pozycje sprawdza się pod kątem istnienia, a cytowany fragment — pod kątem twierdzenia, przy którym stoi. Celem jest wychwycenie halucynowanych pozycji i cytowań, które nie wspierają zdania. Pozycja, której sprawdzający nie może otworzyć, jest „Nie oceniano”. Nie oznacza się jej jako zmyślonej. Człowiek potwierdza każdą pozycję, którą stawia się autorom jako brakującą albo nietrafną, jak wymaga część 5.3.

Ten sam przebieg nadal obejmuje kompletność i strukturę, obecność i wystarczalność ujawnienia AI (w tym plik z promptami i oświadczenie o weryfikacji) oraz plagiat i inne sygnały naruszenia rzetelności, łącznie z programem antyplagiatowym czasopisma, gdy ta usługa już działa. Te pytania są na liście kontrolnej na końcu tej polityki.

Maszynopis, zbiór i kod pozostają na infrastrukturze czasopisma przy każdym składniku. Kontekst literatury i weryfikacja cytowań są wyjątkiem, który wymaga wyszukania na zewnątrz, i tylko w wąskim sensie z części 2: baza literatury, resolver DOI, Crossref, PubMed albo wyszukiwanie w sieci, i tylko ogólne zapytanie albo identyfikator bibliograficzny. Jeżeli tego wyszukania nie da się wykonać w tej granicy, redakcja dostarcza pakiet literatury, a raport to stwierdza.

Wynikiem jest jeden ustrukturyzowany raport:

- streszczenie;
- mocne strony;
- słabe strony;
- pytania do autorów;
- ustalenia o zgodności danych;
- lista kontrolna z załącznika.

Sprawdzony raport otrzymują recenzenci będący ludźmi i redaktor, a także autorzy, jak opisuje część 5.4. Raport nigdy nie stanowi decyzji. Decyzję podejmuje redaktor będący człowiekiem.

### 5.2 Czym nie jest

Wstępna recenzja nie ocenia, czy badanie warto było przeprowadzić, czy schemat był właściwy ani czy interpretacja jest najlepsza z dostępnych. Nie potwierdza, że eksperyment się odbył. Nie uwierzytelnia obrazów. Nie rozstrzyga losu maszynopisu.

Mocne strony, słabe strony i pytania są materiałem dla recenzentów będących ludźmi i dla redaktora. Nie są oceną punktową. Płynnie napisana słabość pozostaje tylko tropem, dopóki człowiek jej nie sprawdzi.

Wynik modelu może być błędny. Cytowanie oznaczone jako zmyślone, ślad plagiatu albo rozbieżność liczbowa są tropem dla człowieka, a nie ustaleniem, dopóki człowiek ich nie sprawdzi.

### 5.3 Sprawdzenie przez człowieka przed wysłaniem raportu

Wskazany członek redakcji czyta wynik modelu, zanim zobaczą go autorzy lub recenzenci.

- Zarzuty, których pracownik nie potrafi odtworzyć, są usuwane albo oznaczane „nie potwierdzono — nie jest to pytanie do autorów”.
- Pracownik nie dopisuje naukowej pochwały ani nagany głosem modelu.
- Przekazany raport nadal podaje, który model i która wersja przygotowały szkic oraz kto go sprawdził.

Autorów nie prosi się o odpowiedź na niepotwierdzony zarzut AI.

### 5.4 Kto otrzymuje raport

Sprawdzony raport trafia do autorów i do redaktora prowadzącego. Trafia do recenzentów rundy 2 wraz z maszynopisem. Pozostaje w dokumentacji redakcyjnej razem z każdym narzędziem, modelem i wersją użytymi w przebiegu, infrastrukturą, na której działały, datą i promptem redakcji. Jedna nazwa modelu, gdy jeden model przygotował narrację i nie użyto innych, jest zapisana właśnie tak.

W tym projekcie raportu nie publikuje się wraz z artykułem. Artykuł stwierdza, że wstępna recenzja AI się odbyła. Rada może później zdecydować o publikowaniu raportów. Ten wybór jest wymieniony w [harmonogramie uruchomienia](launch-roadmap.md).

### 5.5 Wyniki rundy 1

Model nie rekomenduje przyjęcia ani odrzucenia. Redaktor będący człowiekiem wybiera jeden wynik administracyjny:

- **Przekazać do recenzji ludzkiej.**
- **Zwrócić do uzupełnienia.** Redaktor wskazuje autorom, czego brakuje (na przykład niepodpisanej weryfikacji, martwego linku do danych, brakującego numeru zgody). To nie jest poprawka naukowa.
- **Eskalować.** Redaktor podejmuje sygnał naruszenia rzetelności — taki jak potwierdzone przez pracownika zmyślone cytowanie, liczby albo wnioski niezgodne ze zdeponowanymi danymi lub z przeliczoną analizą, rycina danych dostarczona jako obraz wygenerowany albo brak oświadczenia etycznego przy badaniu, które go wymaga — i prowadzi sprawę według [Etyki publikacyjnej](publication-ethics.md). Raport AI jest źródłem sprawdzeń, nie wyrokiem.

## 6. Między rundami

Autorzy poproszeni o uzupełnienie formalne składają tekst ze śledzeniem zmian i krótką odpowiedź. Redakcja potwierdza, że luki wskazane przez redaktora zostały zamknięte. Model hostowany lokalnie może pomóc w tym potwierdzeniu. Maszynopisu nie wysyła się w tym celu do zewnętrznego API AI. Redaktor przekazuje plik recenzentom.

Maszynopisu nie wysyła się do rundy 2, dopóki brakuje ujawnienia AI, identyfikator danych się nie otwiera, recenzenci nie mogą otworzyć depozytu (w tym ścieżki dostępu kontrolowanego) albo brakuje wymaganego oświadczenia o etyce lub rejestracji bez przyjętego wyjaśnienia. Zob. [Dostępność danych i zasady FAIR](data-availability-and-fair-policy.md).

## 7. Runda 2 — ekspercka recenzja ludzka

Redaktor prowadzący zaprasza co najmniej dwóch recenzentów o odpowiednim dorobku, których konflikt interesów nie wyklucza. Recenzenci są badaczami lub praktykami będącymi ludźmi. Modelu nie zaprasza się jako recenzenta.

Redaktor może zaprosić dodatkowego recenzenta do statystyki, metod albo drugiej dziedziny. Jeżeli dwa raporty są sprzeczne, redaktor może zaprosić trzeciego recenzenta albo rozstrzygnąć na podstawie raportów, maszynopisu i własnej lektury. List decyzyjny podaje podstawę rozstrzygnięcia.

Recenzenci otrzymują:

- maszynopis i ryciny;
- oświadczenie o wykorzystaniu AI i plik z promptami;
- dostęp do zdeponowanych danych i kodu albo do ścieżki dostępu wyłącznie na czas recenzji, otwarty już w chwili zgłoszenia;
- sprawdzony raport wstępnej recenzji AI, w tym ustalenia o zgodności danych;
- pytania z tej polityki.

Zgłoszenie, którego danych recenzenci nie mogą otworzyć, nie przechodzi do rundy 2.

Proponowany termin raportu to 21 dni. Redakcja wysyła jedno przypomnienie. Recenzenta, który nie może skończyć, zastępuje się. Tożsamości zastępcy nie ujawnia się autorom, jeżeli recenzja jest anonimowa.

Recenzent, który ukończy recenzję, otrzymuje voucher rabatowy na APC własnego przyszłego artykułu. Wysokość rabatu ustala redakcja i publikuje ją na stronie.

## 8. O co pyta się recenzentów

Recenzenci wypowiadają się o tym:

1. czy schemat badania może odpowiedzieć na pytanie i czy metody są opisane dostatecznie, aby badanie powtórzyć;
2. czy analiza odpowiada schematowi i czy liczby w tekście zgadzają się z tabelami, rycinami oraz z częścią raportu AI o zgodności danych;
3. czy interpretacja mieści się w danych;
4. co badanie wnosi, bez mylenia nowości z powodem, aby pominąć rzetelny wynik zerowy;
5. czy etyka, zgoda, rejestracja i dostępność danych są wystarczające dla danego schematu;
6. **czy ujawnione użycie AI jest właściwe i czy nadzór człowieka wygląda na wystarczający** względem tekstu, kodu, rycin, liczb i cytowań;
7. czy któreś cytowanie nie istnieje albo nie wspiera twierdzenia;
8. czy jest ślad, że dane pierwotne, obrazy danych pierwotnych albo rycina danych zostały wygenerowane albo zmienione przez model. Wykres statystyczny dostarczony jako obraz wygenerowany, a nie jako wynik zdeponowanego kodu, jest takim śladem.

Recenzentów nie prosi się o ponowne uruchomienie każdej analizy. Prosi się ich, aby powiedzieli, jeżeli zdeponowany materiał nie wystarcza do podparcia twierdzeń.

Recenzent, który uważa, że ujawnienie jest niepełne albo nadzór był niewystarczający, pisze to wprost. Taka uwaga jest podstawą, aby redaktor zapytał autorów. Sama w sobie nie jest rekomendacją, którą redaktor musi wykonać bez lektury maszynopisu.

## 9. Obowiązki recenzenta

Recenzenci:

- ujawniają konflikty interesów przed przyjęciem zaproszenia, w tym niedawną współpracę, wspólną instytucję tam, gdzie konflikt jest rzeczywisty, albo interes finansowy w badanej interwencji lub narzędziu;
- traktują pliki jako poufne, także po złożeniu rekomendacji;
- nie wgrywają maszynopisu, danych, kodu, raportu AI ani recenzji do żadnej zewnętrznej usługi AI, w tym usługi podmiotu trzeciego, w tym do API. Zakaz jest ten sam co własna zasada czasopisma w części 2;
- jeżeli w ogóle korzystają z modelu, działa on lokalnie pod ich kontrolą, a redaktorowi podają nazwę i wersję modelu. Złożona recenzja pozostaje ich własną oceną;
- nie żądają cytowania własnych prac, chyba że jest to niezbędne naukowo;
- nie kontaktują się z autorami bezpośrednio w sprawie zgłoszenia;
- zawiadamiają redakcję, jeżeli rozpoznają maszynopis, którego nie mogą ocenić rzetelnie.

Redakcja nie pozyskuje sugestii recenzentów z zewnętrznej usługi AI. Sugestie z narzędzia hostowanego lokalnie, jeżeli kiedykolwiek zostaną użyte, redaktor sprawdza względem rzeczywistych publikacji i konfliktów, zanim wyśle zaproszenie.

## 10. Decyzja

Decyzję podejmuje redaktor będący człowiekiem i podpisuje list. Redaktor czyta maszynopis, raport AI i recenzje ludzkie. Redaktor nie jest związany rekomendacją bez uzasadnienia, wrogą albo sprzeczną z zasadami czasopisma. Redaktor nie idzie za rekomendacją przyjęcia pracy, której ujawnienie, dane albo oświadczenia etyczne nie spełniają wymogów minimalnych.

| Decyzja | Znaczenie |
| --- | --- |
| Przyjęcie | Redaktor jest przekonany. Pozostałe zmiany ograniczają się do pytań produkcyjnych. |
| Drobne poprawki | Wskazane zmiany, zwykle sprawdzane przez redaktora. Ponowna recenzja ludzka jest fakultatywna. |
| Zasadnicze poprawki | Zmiany istotne. Ponowna recenzja ludzka jest zasadą. Przyjęcia się nie obiecuje. |
| Odrzucenie | Maszynopis nie przechodzi dalej. Nowe zgłoszenie tego samego badania jest dopuszczalne tylko wtedy, gdy list redaktora tak stanowi. |

Nie ma płatnego szybkiego toru i żadnej decyzji nie wymienia się na cytowanie albo opłatę. Stała opłata za przetworzenie artykułu jest wystawiana dopiero po przyjęciu. Redaktorzy i recenzenci rozstrzygający pracę nie widzą statusu płatności.

Redaktor nie rozstrzyga maszynopisu, który sam napisał, ani takiego, przy którym konflikt interesów czyni rzetelną decyzję nierozsądną. Taki plik prowadzi inny redaktor. Jeżeli każdy redaktor jest w konflikcie, czasopismo prosi redaktora gościnnego spoza rady i odnotowuje to rozwiązanie.

## 11. Poprawki i późniejsze kontrole AI

Autorzy odpowiadają punkt po punkcie. Aktualizują oświadczenie o wykorzystaniu AI, jeżeli przy poprawce pojawiło się nowe narzędzie albo nowe zastosowanie. Ciche rozszerzenie użycia AI na etapie poprawki jest użyciem nieujawnionym.

Redakcja może uruchomić model hostowany lokalnie, aby zestawić, co się zmieniło względem listu decyzyjnego i czy wcześniej wskazane liczby, linki i cytowania już się zgadzają. Poprawki nie wysyła się do zewnętrznego API AI. Redaktor będący człowiekiem czyta to zestawienie. Gdy poprawka zmienia analizę, próbę, interpretację albo obrazy, redaktor odsyła ją co najmniej jednemu recenzentowi będącemu człowiekiem, chyba że obaj recenzenci ograniczyli prośby do rzeczy, które redaktor może sprawdzić bezpośrednio.

## 12. Odwołania

Autorzy mogą raz odwołać się od odrzucenia, na piśmie, na adres [EMAIL], w ciągu 30 dni od decyzji. Odwołanie wskazuje błąd faktyczny lub proceduralny. Nie jest ponownym zgłoszeniem.

Odwołanie rozpatruje redaktor będący człowiekiem, który nie był redaktorem rozstrzygającym, o ile w radzie jest więcej niż jeden redaktor. Może on zasięgnąć opinii nowego recenzenta. Raport wstępnej recenzji AI nie jest decyzją zaskarżalną, ponieważ nie jest decyzją. Wynikiem odwołania jest: uwzględnienie i dalsza recenzja, zaproszenie do poprawki albo utrzymanie odrzucenia. Decyzja w odwołaniu jest ostateczna dla tego maszynopisu.

Skargi na postępowanie, stronniczość albo nieujawnione użycie AI prowadzi się według [Etyki publikacyjnej](publication-ethics.md).

## 13. Co się mówi czytelnikom

Opublikowany artykuł stwierdza, że recenzja obejmowała wstępną recenzję AI i ekspercką recenzję ludzką oraz że decyzję podjął redaktor będący człowiekiem. Nie podaje nazwisk recenzentów, chyba że podpisali recenzję, a rada zgodziła się ten podpis opublikować.

Każde narzędzie, model i wersja użyte w rundzie 1 oraz infrastruktura, na której działały, są zapisane w dokumentacji redakcyjnej i w raporcie. Rada przed uruchomieniem decyduje, czy te nazwy są także drukowane przy artykule. Do tej decyzji publiczne zdanie nie wymyśla nazwy modelu. Zob. [harmonogram uruchomienia](launch-roadmap.md).

## 14. Dokumenty powiązane

- [Polityka wykorzystania i ujawniania AI](ai-use-and-disclosure-policy.md)
- [Dostępność danych i zasady FAIR](data-availability-and-fair-policy.md)
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
| Infrastruktura | Host kontrolowany przez czasopismo: [opis]. Modele o otwartych wagach, hostowane samodzielnie. Zewnętrzne API AI: nie. |
| Wyszukania zewnętrzne | [brak / baza literatury, Crossref, PubMed, resolver DOI, wyszukiwanie w sieci]. Co opuściło host: [wyłącznie ogólne zapytania i identyfikatory bibliograficzne / nic] |
| Wersja promptu redakcji | [identyfikator promptu wewnętrznego, przechowywany w dokumentacji] |
| Osoba sprawdzająca | [ROLA, nie nazwisko recenzenta publicznego — np. redakcja]. Data sprawdzenia: [RRRR-MM-DD] |
| Program antyplagiatowy | [NAZWA I WERSJA NARZĘDZIA albo „jeszcze nie użyto”] |
| Dane widziane przy sprawdzeniu | [depozyt otwarty / ścieżka dostępu kontrolowanego / wyłącznie człowiek dla nazwanych plików]. Identyfikator: [DOI ALBO NUMER AKCESYJNY] |

**Narzędzia, modele i wersje użyte w tym przebiegu.** Jeden wiersz na składnik. Jeżeli jeden model wykonał każdy składnik, należy to napisać w każdym wierszu. Składnik, którego nie uruchomiono, oznacza się „nie uruchomiono” z powodem.

| Składnik | Narzędzie lub model | Wersja | Co mógł zobaczyć |
| --- | --- | --- | --- |
| Kontekst literatury (historyk poddziedziny) | | | Wyłącznie literatura opublikowana / pakiet literatury od redakcji |
| Pominięte punkty odniesienia i zbiory | | | |
| Wielowątkowa weryfikacja twierdzeń | | | |
| Zgodność danych z maszynopisem | | | Zdeponowany zbiór i kod, w granicach warunków dostępu |
| Raportowanie, etyka i rejestracja | | | Maszynopis, lista kontrolna, standard EQUATOR: [NAZWA, WERSJA] |
| Istnienie i trafność cytowań | | | |
| Złożenie narracji tego raportu | | | |

**Informacja dla autorów i recenzentów.** Model nie decyduje o przyjęciu. Nie ustala, że badanie się odbyło. Mocne strony, słabe strony i pytania nie są oceną punktową. Sygnały poniżej są pytaniami tylko tam, gdzie osoba sprawdzająca je potwierdziła. Pozycje oznaczone „nie potwierdzono” nie wymagają odpowiedzi.

### Streszczenie

[Pięć do dziesięciu zdań. Czego dotyczy maszynopis, co sprawdzono względem depozytu i czego nie sprawdzono.]

### Mocne strony

[Punkty, które osoba sprawdzająca godzi się zostawić w raporcie. Bez pochwały, której sprawdzający nie przeczytał.]

### Słabe strony

[Punkty. Każdy wskazuje fragment, plik albo wiersz listy kontrolnej. Pozycje niepotwierdzone tu nie występują.]

### Pytania do autorów

[Pytania numerowane, które wynikają z potwierdzonych luk. Żadnego pytania, które powtarza niepotwierdzony zarzut.]

### Ustalenia o zgodności danych

| Pozycja w maszynopisie | Wartość wydrukowana | Wartość z depozytu albo z ponownego przeliczenia | Przeliczono ponownie? | Wynik |
| --- | --- | --- | --- | --- |
| [np. streszczenie, punkt końcowy główny] | | | [tak / nie przeliczono — powód] | [zgodne / rozbieżne / nie oceniano] |

Analizy przeliczone ponownie: [lista skryptów albo „żadna — powód”]. Wnioski, które nie wynikają z przeliczonych albo zdeponowanych liczb: [brak / lista].

### Lista kontrolna

Należy użyć wartości **Spełnione**, **Luka** albo **Nie oceniano**. Przy każdej luce jest jedno zdanie. Przy każdym „Nie oceniano” jest powód (na przykład „pełne teksty cytowanych prac nie były dostępne dla modelu”).

| # | Pytanie | Wynik | Uwaga |
| --- | --- | --- | --- |
| 1 | Dla tego rodzaju artykułu są obecne wymagane części (tytuł, autorzy będący ludźmi i afiliacje, streszczenie strukturalne, słowa kluczowe, wstęp, metody, wyniki, dyskusja, dostępność danych, etyka, odesłanie do ujawnienia AI, finansowanie, konflikty interesów, piśmiennictwo). | | |
| 2 | W nagłówku są wyłącznie ludzie. Autorem nie jest model, firma ani program. | | |
| 3 | Oświadczenie o wykorzystaniu AI jest obecne i podaje narzędzia, wersje, tryb dostępu, zastosowania, plik z promptami oraz osoby, które wykonały weryfikację. | | |
| 4 | Oświadczenie zgadza się z maszynopisem (narzędzia wspomniane w tekście są ujawnione; ujawnione zastosowania widać tam, gdzie je wskazano). | | |
| 5 | Jeżeli zadeklarowano brak AI, nic w pliku tej deklaracji nie zaprzecza. | | |
| 6 | Oświadczenie o dostępności danych podaje repozytorium, trwały identyfikator, licencję i pliki (zbiór, kod, książkę kodową, README). Identyfikator się otwiera. Wstępna recenzja AI i recenzenci będący ludźmi mogą otworzyć depozyt albo ścieżka dostępu kontrolowanego jest opisana i dla nich otwarta. | | |
| 7 | Każdą liczbę, statystykę i wniosek w streszczeniu, wynikach, tabelach, rycinach i dyskusji sprawdzono względem zdeponowanego zbioru i kodu. Podać, które analizy przeliczono ponownie i których nie dało się przeliczyć. Wymienić każdą rozbieżność. | | |
| 8 | Obecne są formaty otwarte albo standardowe, książka kodowa i README, a kompetentny czytelnik mógłby powtórzyć opisane analizy z depozytu. | | |
| 9 | Cytowania: podać, ile sprawdzono pod kątem istnienia i tego, czy cytowany fragment wspiera twierdzenie, oraz jaką metodą. Wymienić pozycje, które wydają się nie istnieć albo nie wspierać twierdzenia, tylko jeżeli listę potwierdziła osoba sprawdzająca. Pozycji nieotwartej nie oznacza się jako zmyślonej. | | |
| 10 | Badanie podobieństwa / plagiatu: narzędzie, wynik punktowy jeżeli jest, oraz wniosek osoby sprawdzającej. Zbieżność ograniczoną do szablonowych metod należy tak opisać. | | |
| 11 | Etyka, zgoda, dobrostan zwierząt, zezwolenia oraz rejestracja badania lub protokołu są obecne i konkretne albo obecne jest uzasadnione „nie dotyczy”. | | |
| 12 | Konflikty interesów i finansowanie są podane, w tym „brak”, jeżeli takie jest twierdzenie. | | |
| 13 | Zasady rycin: obrazy danych pierwotnych są oryginalnymi zapisami; schemat metodyczny wspomagany przez AI jest ujawniony i nie pokazuje danych; ryciny danych i wykresy statystyczne pochodzą ze zdeponowanego kodu i nie są obrazami wygenerowanymi. Model nie może uwierzytelnić obrazu. | | |
| 14 | Wskazano właściwy standard raportowania z EQUATOR Network (CONSORT, STROBE, ARRIVE, PRISMA, SPIRIT albo inny z wytycznych dla autorów), wersja jest aktualna, a lista kontrolna jest dołączona, gdy standard jej oczekuje. | | |
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
- poprawności analiz, które raport oznacza jako nieprzeliczone ponownie;
- tego, czy maszynopis należy przyjąć, skierować do poprawy albo odrzucić.

### Rekomendacja administracyjna dla redaktora

Zaznaczyć jedno. Nie zaznaczać decyzji o przyjęciu ani o odrzuceniu.

- [ ] Przekazać do recenzji ludzkiej
- [ ] Zwrócić autorom do uzupełnienia (wymienić luki)
- [ ] Eskalować do redaktora prowadzącego jako sygnał naruszenia rzetelności (wymienić potwierdzone sygnały)

**Potwierdzenie osoby sprawdzającej:** Potwierdzam, że ten raport został przeze mnie przeczytany, a niepotwierdzone zarzuty zostały usunięte albo oznaczone. Podpis / imię i nazwisko oraz data: [IMIĘ I NAZWISKO, ROLA, DATA]

---

### Prompt wewnętrzny — minimalne instrukcje

Redakcja używa promptu na piśmie, który zawiera co najmniej następujące polecenia i jest przechowywany z identyfikatorem wersji:

1. Wykonujesz wstępną recenzję AI dla czasopisma *Journal of AI-Assisted Research for Life Sciences*. Nie rekomendujesz przyjęcia ani odrzucenia. Nie wystawiasz oceny punktowej.
2. Działasz na infrastrukturze kontrolowanej przez czasopismo. Nie wywołuj zewnętrznego API AI. Nie wysyłaj maszynopisu, danych, kodu ani niczego, co identyfikuje autorów, do żadnej innej usługi. Wyszukanie literatury albo cytowania może wysłać wyłącznie ogólne zapytanie albo identyfikator bibliograficzny (DOI, PMID, tytuł albo ciąg autor–rok). Jeżeli nie możesz czegoś sprawdzić w tej granicy, napisz, że redakcja musi dostarczyć pakiet literatury.
3. Wypełnij ustrukturyzowany raport: streszczenie, mocne strony, słabe strony, pytania do autorów, ustalenia o zgodności danych i listę kontrolną. Na liście użyj wartości Spełnione, Luka albo Nie oceniano.
4. Przy sprawdzaniu liczb porównaj je ze zdeponowanymi danymi i kodem. Analizę przelicz ponownie tylko w tym wdrożeniu i tylko wtedy, gdy zdeponowany kod się uruchamia. Jeżeli nie możesz jej przeliczyć, oznacz Nie oceniano i podaj powód. Nie wymyślaj rozbieżności.
5. Nie wymyślaj cytowań, cytatów, numerów zgód ani identyfikatorów repozytorium. Jeżeli nie możesz otworzyć cytowania, oznacz Nie oceniano. Nie nazywaj go zmyślonym.
6. Nie przepisuj maszynopisu.
7. Traktuj pliki jako poufne.
8. Podaj narzędzie i wersję, którymi jesteś. Resztę dziennika narzędzi dopisuje redakcja.
