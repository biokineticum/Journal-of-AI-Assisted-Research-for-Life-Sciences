# Polityka wykorzystania i ujawniania AI

**Journal of AI-Assisted Research for Life Sciences**

**Status:** projekt do przyjęcia (wersja 0.1, 14 listopada 2026 r.). Tekst jest napisany tak, aby po przyjęciu przez wydawcę mógł zostać opublikowany na stronie czasopisma. Do tego czasu nie obowiązuje.

**Język:** polski · [English version](../en/ai-use-and-disclosure-policy.md)

## 1. Cel

Autorzy mogą korzystać ze sztucznej inteligencji przy przygotowaniu maszynopisu. Czasopismo wymaga, aby powiedzieli dokładnie w jaki sposób, i aby pozostali odpowiedzialni za każde zdanie, pod którym się podpisują.

Polityka jest zgodna ze stanowiskiem Committee on Publication Ethics (COPE) oraz International Committee of Medical Journal Editors (ICMJE): model językowy nie spełnia kryteriów autorstwa, a użycie technologii wspomaganej przez AI podlega ujawnieniu. Jest też zgodna z obowiązkiem poufności z [wytycznych COPE dla redaktorów i recenzentów](https://publicationethics.org/guidance): nieopublikowanych zgłoszeń nie wkleja się do publicznych narzędzi, które mogą się na nich uczyć.

Wzór, który wypełniają autorzy: [Oświadczenie o wykorzystaniu AI](ai-disclosure-statement.md).

## 2. Definicje

| Termin | Znaczenie w tym czasopiśmie |
| --- | --- |
| Narzędzie AI | System generatywny lub uczący się, użyty do wytworzenia albo przekształcenia tekstu, kodu, obrazu, dźwięku lub podpowiedzi. Nie trzeba wymieniać korektorów, które tylko zaznaczają literówki, ani narzędzi gramatycznych, które nie tworzą zdań. W razie wątpliwości narzędzie należy ujawnić. |
| Dane pierwotne | Obserwacje, pomiary, obrazy, nagrania i transkrypcje powstałe w badaniu, w postaci zebranej. |
| Dane surowe | Dane pierwotne w postaci pierwszego zapisu, przed podsumowaniem statystycznym, wystarczające, aby kompetentny badacz powtórzył opisane analizy. |
| Modyfikacja danych pierwotnych | Utworzenie, imputacja, usunięcie, zastąpienie albo wybiórcza zmiana obserwacji przez model. Reguła czyszczenia określona przez człowieka, zapisana w zdeponowanym kodzie i wykonana przez autorów, jest przetwarzaniem i musi być opisana w Metodach. Nie jest przyzwoleniem, aby model wymyślał lub przepisywał obserwacje. |
| Publiczny model konsumencki | Czatbot lub podobna usługa, w której dostawca może uczyć się na danych wejściowych albo w której żadna umowa nie zakazuje uczenia i długotrwałego przechowywania. |
| Dopuszczalne wdrożenie | Dla autorów przygotowujących maszynopis: model lokalny albo usługa korporacyjna lub API objęta pisemną umową, że zgłoszenie i prompty nie służą do trenowania modeli i nie są przechowywane dłużej, niż wymaga tego zadanie. To nie jest zasada własnej recenzji czasopisma. |
| Model hostowany przez czasopismo | Model językowy o otwartych wagach, który czasopismo uruchamia na infrastrukturze, którą kontroluje. Runda 1 i każde późniejsze sprawdzenie redakcyjne zgłoszenia korzystają wyłącznie z tych modeli. Zewnętrzne API AI, w tym API podmiotu trzeciego, nie jest modelem hostowanym przez czasopismo, nawet przy umowie o braku trenowania. |

## 3. Autorstwo

Autorami są ludzie. Każdy autor spełnia wszystkie cztery kryteria ICMJE:

1. istotny wkład w koncepcję lub projekt albo w pozyskanie, analizę lub interpretację danych;
2. napisanie pracy lub krytyczne przeredagowanie jej pod względem istotnej treści merytorycznej;
3. zatwierdzenie wersji przeznaczonej do publikacji;
4. zgoda na ponoszenie odpowiedzialności za wszystkie aspekty pracy oraz na to, aby pytania o rzetelność lub prawidłowość zostały wyjaśnione.

Narzędzie AI nie spełnia żadnego z tych kryteriów. Nie umieszcza się go jako autora, współautora ani autora korespondencyjnego i nie dziękuje się mu tak, jakby było współpracownikiem, który wykonał badanie. Miejscem narzędzia jest oświadczenie o wykorzystaniu AI.

Ludzie, którzy spełniają kryteria, są wymienieni także wtedy, gdy narzędzie przygotowało szkic prozy. Ludzi, którzy kryteriów nie spełniają, wymienia się w podziękowaniach, nie w nagłówku. Autorstwo grzecznościowe, pozorne i ukryte jest naruszeniem. Zob. [Etyka publikacyjna](publication-ethics.md).

Autor korespondencyjny potwierdza, że każda wymieniona osoba zatwierdziła maszynopis i oświadczenie oraz że nie pominięto żadnej osoby spełniającej kryteria.

## 4. Zasada pracy empirycznej

Wyniki empiryczne w tym czasopiśmie pochodzą z pracy, którą wykonali ludzie.

Dopuszczalne są eksperymenty, badania obserwacyjne, badania kliniczne i interwencyjne, praca w terenie, pomiary laboratoryjne, obrazowanie, wywiady i inne badania jakościowe oraz ponowna analiza rzeczywistego zbioru, z którego autorzy mogą korzystać. Symulacja jest dopuszczalna wyłącznie jako symulacja: autorzy ją uruchomili, maszynopis to stwierdza, a kod i ziarna generatora są zdeponowane. Symulacja nie zastępuje obserwacji, które artykuł przedstawia jako rzeczywiste.

Model może pomóc napisać artykuł o tej pracy. Model nie wykonuje badania.

## 5. Zastosowania dozwolone

Po ujawnieniu i po sprawdzeniu wyniku przez autora będącego człowiekiem narzędzia AI mogą służyć do:

- szkicowania lub poprawiania tekstu na podstawie notatek autorów, wyników analiz i danych;
- redakcji językowej lub tłumaczenia;
- zaproponowania układu części, którą autorzy następnie sprawdzają;
- formatowania piśmiennictwa, po weryfikacji każdego źródła przez autorów;
- proponowania zapytań wyszukiwawczych, podczas gdy ludzie projektują wyszukiwanie, przeglądają rekordy i ekstrahują dane;
- pisania lub poprawiania kodu analitycznego, który autor będący człowiekiem przegląda, rozumie i uruchamia, w tym kodu, który generuje ryciny danych i wykresy statystyczne ze zdeponowanych danych surowych;
- transkrypcji rzeczywistych nagrań, po korekcie transkrypcji przez człowieka na podstawie nagrania i po weryfikacji każdego cytatu;
- szkicowania schematów metodycznych, które nie pokazują obserwacji, oszacowań ani statystyk testowych. Narzędzie w rodzaju opisanego jako PaperVizAgent jest przykładem, nie wymogiem. Użycie jest ujawnione, a autor będący człowiekiem sprawdza schemat względem metod.

Dozwolone użycie nie zmniejsza odpowiedzialności. Akapit w szkicu staje się tekstem autorów z chwilą zgłoszenia.

## 6. Zastosowania zabronione

Następujące działania są podstawą odrzucenia, a po publikacji są rozpatrywane według [Etyki publikacyjnej](publication-ethics.md):

- generowanie danych pierwotnych albo przedstawianie wyniku modelu jako pomiarów, odpowiedzi w kwestionariuszu, obrazów prób lub cytatów uczestników;
- modyfikowanie danych pierwotnych w rozumieniu powyższej definicji, w tym generatywna imputacja punktów końcowych;
- tworzenie lub „ulepszanie” obrazu danych pierwotnych tak, aby pokazywał szczegół, którego zapis nie zawierał;
- sporządzenie ryciny danych albo wykresu statystycznego jako obrazu wygenerowanego, zamiast kodu uruchomionego na zdeponowanych danych surowych;
- przedstawienie schematu narysowanego przez AI tak, jakby pokazywał wyniki pomiarów;
- wskazanie narzędzia AI jako autora;
- wstawienie cytowania, którego żaden autor będący człowiekiem nie otworzył i nie sprawdził;
- wymyślenie grantodawcy, numeru zgody komisji, numeru rejestracji, identyfikatora repozytorium, recenzenta albo afiliacji;
- wklejenie cudzego poufnego, nieopublikowanego maszynopisu, recenzji lub danych do jakiegokolwiek narzędzia AI;
- złożenie maszynopisu, którego ujawnienie jest brakujące, ogólnikowe („użyto AI, aby poprawić tekst”) albo sprzeczne z samym maszynopisem.

Ujawnienie zastosowania zabronionego nie jest zezwoleniem. Informacja, że model wymyślił wyniki, prowadzi do odrzucenia. Nie czyni wyników dopuszczalnymi.

## 7. Ryciny i obrazy

**Obrazy danych pierwotnych** — mikroskopia, bloty, żele, fotografie preparatów lub aparatury, skany urządzeń, obrazy kliniczne i zdjęcia osób badanych — są oryginalnymi zapisami z badania. Nie są generowane, uzupełniane generatywnie, poddawane sztucznej superrozdzielczości ani zastępowane przez model.

Liniowa korekta jasności, kontrastu lub kadru jest dopuszczalna, gdy obejmuje cały obraz, nie ukrywa i nie wymyśla cech oraz jest opisana, jeżeli wpływa na interpretację. Sklejenia, jeżeli są nieuniknione, są oznaczone. Identyfikatory usuwa się przez kadr albo jednolitą maskę. Nie usuwa się ich wypełnieniem generatywnym.

**Ryciny danych i wykresy statystyczne** — każde przedstawienie obserwacji, oszacowań albo statystyk testowych, w tym wykresy rozrzutu, słupkowe, leśne, krzywe przeżycia i wykresy Blanda–Altmana — powstają z odtwarzalnego kodu na podstawie zdeponowanych danych surowych. Nie są obrazami wygenerowanymi. Model obrazu ich nie rysuje, także wtedy, gdy narzędzie potrafi wyemitować i ilustrację, i wykres. Autorzy deponują skrypt, dane wejściowe, które czyta, i wersje oprogramowania, a autor będący człowiekiem, który skrypt uruchomił, sprawdza każdy punkt, słupek, przedział i podpis względem tego wyniku.

**Schematy metodyczne**, które nie pokazują obserwacji ani oszacowań (schemat przebiegu badania, sekwencja pomiaru, diagram pojęciowy), mogą powstawać ze wsparciem AI. Narzędzia w rodzaju opisanego jako PaperVizAgent, w tej samej nocie Google Research z kwietnia 2026 r., która opisuje ScholarPeer, są przykładem takiej pomocy. Nie są wymagane, a czasopismo nie zależy od tego produktu. Autorzy ujawniają narzędzie, wersję i numery rycin, a autor będący człowiekiem sprawdza, że schemat zgadza się z metodami. Czasopismo nie przyjmuje ścieżki generowania obrazu dla wykresu statystycznego, także z narzędzia, które taką ścieżkę również oferuje.

Ryciny złożone wskazują, czym jest każdy panel. Czasopismo może poprosić o oryginalne, nieprzetworzone pliki obrazów.

## 8. Dane i kod

Narzędzia AI nie generują ani nie modyfikują danych pierwotnych.

Zbiór zebrany przez ludzi i kod analizy deponuje się przed zgłoszeniem według [Dostępności danych i zasad FAIR](data-availability-and-fair-policy.md): zaufane repozytorium, trwały identyfikator (DOI z Zenodo, OSF, Figshare, Dryad albo numer akcesyjny dziedzinowy), bogate metadane, formaty otwarte albo standardowe, książka kodowa, README i jasna licencja (CC BY 4.0 albo CC0 dla danych, chyba że zasada prywatności wymaga innego reżimu otwartego albo kontrolowanego). Oświadczenie o dostępności danych jest wymagane. Podaje repozytorium, identyfikator, licencję i to, co zdeponowano.

Wrażliwe dane zdrowotne są tak otwarte, jak to możliwe, i tak zamknięte, jak to konieczne. Pseudonimizacja w rozumieniu RODO nie jest anonimizacją. Ścieżka dostępu kontrolowanego jest dopuszczalna, gdy ustawa, treść zgody albo bezpieczeństwo biologiczne czynią upublicznienie bezprawnym lub niebezpiecznym. Redaktor i recenzenci, w tym wstępna recenzja AI, i tak mają dostęp w chwili zgłoszenia. Sama formuła „dostępne na uzasadniony wniosek” nie spełnia tej polityki.

Kod analizy jest zdeponowany i czytelny dla badacza z danej dziedziny. Kod pisany ze wsparciem AI jest ujawniony. Odpowiedzialność ponosi autor będący człowiekiem, który kod rozumie i który go uruchomił. Kod, którego autorzy nie potrafią objaśnić, jest niedopuszczalny. Skrypty budujące ryciny danych są częścią tego depozytu.

Wybory statystyczne — w tym imputacja — są określone przez ludzi, opisane i odróżnione od danych surowych. Wynik modelu generatywnego nie jest zbiorem imputowanym.

Dalsze wymagania: [Wytyczne dla autorów](author-guidelines.md).

## 9. Prywatność przy korzystaniu z narzędzi AI

Danych identyfikujących uczestników, nieopublikowanych danych osób trzecich i innych materiałów poufnych nie wkleja się do publicznego modelu konsumenckiego.

Autorzy korzystają z dopuszczalnego wdrożenia albo ograniczają prompt do zagregowanego, zanonimizowanego materiału, który mają prawo tak przetwarzać. Zgodność z ogólnym rozporządzeniem o ochronie danych (RODO) oraz ze zgodą komisji jest obowiązkiem autorów. Oświadczenie o wykorzystaniu AI nie naprawia bezprawnego przekazania danych osobowych.

## 10. Obowiązkowe ujawnienie

Do każdego zgłoszenia dołącza się wypełnione [Oświadczenie o wykorzystaniu AI](ai-disclosure-statement.md), także gdy żadnego narzędzia AI nie użyto.

Oświadczenie wskazuje:

- każde narzędzie, dostawcę, model i wersję, tryb dostępu (lokalny, korporacyjny z umową o braku trenowania albo inny) oraz daty użycia;
- dokładnie, do czego narzędzie posłużyło, z odniesieniem do części maszynopisu, kodu albo rycin;
- plik uzupełniający z kluczowymi promptami albo wiernym zapisem przebiegu pracy;
- autorów będących ludźmi, którzy zweryfikowali fakty, liczby, cytowania i interpretacje.

Oświadczenie jest konkretne. „Użyto ChatGPT do redakcji językowej” nie wystarcza. Wymagane są wersja, tryb dostępu, części tekstu i krok weryfikacji.

Autor korespondencyjny wgrywa oświadczenie jako plik uzupełniający i wypełnia odpowiadające mu pola w systemie zgłoszeń. W samym maszynopisie znajduje się krótkie odesłanie:

- jeżeli użyto narzędzi: „Wykorzystanie narzędzi AI opisuje oświadczenie o wykorzystaniu AI publikowane wraz z tym artykułem.”
- jeżeli nie użyto żadnego narzędzia: „Autorzy nie korzystali z generatywnych narzędzi AI w tej pracy.”

Jednozdaniowe podziękowanie nie zastępuje oświadczenia.

## 11. Plik z promptami i przebiegiem pracy

Autorzy dołączają plik uzupełniający z kluczowymi promptami i przebiegiem pracy.

Plik zawiera, w zakresie w jakim ma to zastosowanie:

- narzędzie i wersję oraz datę każdej istotnej sesji;
- prompty, które ukształtowały Metody, Wyniki, interpretację, kod lub ryciny, albo wierny zapis pracy iteracyjnej, gdy nie było jednego promptu;
- co przekazano modelowi (notatki, statystyki zbiorcze, kod albo opis zbioru — nie zrzut danych osobowych pozwalających zidentyfikować uczestnika);
- co autorzy zachowali, poprawili albo odrzucili.

Redakcję językową można udokumentować narzędziem i wersją, reprezentatywnym promptem oraz wskazaniem, które części zredagowano. Szkic Wyników albo interpretacji wymaga promptów istotnych dla treści, a nie jednego przykładowego zdania.

Plik jest publikowany wraz z artykułem. Jeżeli prompt ujawniłby uczestnika albo cudzy materiał poufny, autorzy składają wersję publiczną po zaczernieniu i przekazują redaktorowi plik pełny, który pozostaje w dokumentacji redakcyjnej.

## 12. Weryfikacja przez człowieka

Przed zgłoszeniem autorzy będący ludźmi sprawdzają maszynopis względem źródeł pracy. Co najmniej:

- każda liczba w streszczeniu, wynikach, tabelach i rycinach zgadza się z wynikiem analizy i ze zdeponowanymi danymi;
- każde cytowanie zostało otwarte przez autora będącego człowiekiem, istnieje i wspiera twierdzenie, przy którym stoi;
- interpretacje nie wykraczają poza dane, schemat badania i cytowaną literaturę;
- cytaty zgadzają się ze sprawdzoną transkrypcją albo źródłem;
- ryciny zgadzają się z danymi, łącznie z podpisami i jednostkami.

Oświadczenie wymienia autorów, którzy wykonali sprawdzenie liczb i sprawdzenie cytowań. Wszyscy autorzy pozostają odpowiedzialni według kryterium 4 ICMJE. Weryfikacji nie można powierzyć temu samemu modelowi, który przygotował szkic.

Fałszywe cytowanie jest naruszeniem także wtedy, gdy podsunęło je narzędzie. Ujawnienie jest zapisem użycia narzędzia. Nie jest zwolnieniem z obowiązku sprawdzenia.

## 13. Publikacja oświadczenia

Jeżeli artykuł zostanie przyjęty, czasopismo publikuje:

- oświadczenie o wykorzystaniu AI;
- plik z promptami i przebiegiem pracy, zaczerniony wyłącznie w zakresie dopuszczonym powyżej;
- zdanie przy artykule stwierdzające, że recenzja obejmowała wstępną recenzję AI i recenzję ekspercką człowieka oraz że decyzję podjął redaktor będący człowiekiem.

Czytelnik nie powinien domyślać się, które części procesu obejmowały model.

## 14. Wykorzystanie AI przez czasopismo

Własne wykorzystanie AI przez czasopismo wobec zgłoszenia jest ograniczone, oznaczone i prowadzone wyłącznie na modelach hostowanych przez czasopismo. Maszynopisów, zbiorów danych, kodu analizy i materiałów recenzentów nigdy nie wysyła się do zewnętrznego API AI, w tym API podmiotu trzeciego. Narzędzia własne autorów, ujawniane według części 5 i 9, są osobną sprawą. Czasopismo nie wysyła zgłoszenia do tych narzędzi.

**Runda 1 — wstępna recenzja AI.** W zgłoszeniach mieszczących się w zakresie redakcja przeprowadza wieloskładnikową wstępną recenzję na infrastrukturze, którą kontroluje, modelami o otwartych wagach, które sama hostuje. Żaden składnik nie wywołuje zewnętrznego API AI. Projekt jest wzorowany na ScholarPeer (Yoon i Pfister, blog Google Research, 8 kwietnia 2026 r.). Jest to źródło projektu, a nie zależność od tego produktu ani od dostawcy. ScholarPeer oceniano na artykułach z uczenia maszynowego, więc to czasopismo je dostosowuje i dodaje sprawdzenia dla maszynopisów z nauk o życiu. Składniki to: kontekst literatury (historyk poddziedziny), poszukiwanie pominiętych punktów odniesienia i zbiorów, wielowątkowe pytania i odpowiedzi weryfikujące twierdzenia oraz trzy sprawdzenia właściwe temu czasopismu — zgodność danych z maszynopisem (każda liczba, statystyka i wniosek sprawdzone ponownie względem zdeponowanego zbioru FAIR i kodu, z ponownym przeliczeniem analiz tam, gdzie kod da się uruchomić), zgodność ze standardem raportowania przez EQUATOR Network (CONSORT, STROBE, PRISMA, ARRIVE, SPIRIT i pozostałe wymienione w wytycznych dla autorów) wraz ze zgodą komisji i rejestracją badania, oraz istnienie i trafność cytowań, nakierowane na halucynowane pozycje. Kontekst literatury i weryfikacja cytowań mogą odpytać bazę literatury, Crossref, PubMed, resolver DOI albo publiczną sieć. Infrastrukturę opuszcza wyłącznie ogólne zapytanie wyszukiwawcze albo identyfikator bibliograficzny. Tekst maszynopisu, dane, kod i treść identyfikująca autorów nie opuszczają jej. Dane o dostępie kontrolowanym czyta się wyłącznie w środowisku lokalnym. Wynikiem jest jeden ustrukturyzowany raport: streszczenie, mocne strony, słabe strony, pytania do autorów, ustalenia o zgodności danych i lista kontrolna. Każde narzędzie, model i wersja oraz infrastruktura są zapisywane w raporcie i ujawniane w dokumentacji redakcyjnej. Członek redakcji będący człowiekiem czyta raport, zanim zostanie on wysłany, usuwa każdy zarzut, którego nie potrafi potwierdzić, i odnotowuje to sprawdzenie. Raport otrzymują recenzenci będący ludźmi i redaktor oraz autorzy. Raport nigdy nie stanowi decyzji. Specyfikacja jest w [Polityce recenzji](peer-review-policy.md).

**Redaktorzy.** Redaktor będący człowiekiem decyduje, czy zgłoszenie przechodzi dalej, co autorzy mają uzupełnić, i jaki jest wynik końcowy. Redaktorzy nie wklejają zgłoszeń do zewnętrznej usługi AI.

**Recenzenci.** Recenzenci będący ludźmi nie wgrywają maszynopisu, danych, kodu ani swojej recenzji do żadnej zewnętrznej usługi AI, w tym usługi podmiotu trzeciego. Zakaz jest ten sam co własna zasada czasopisma. Recenzent, który w ogóle korzysta z modelu, uruchamia go lokalnie, podaje redaktorowi nazwę i wersję modelu i odpowiada za recenzję. Szczegóły: [Polityka recenzji](peer-review-policy.md).

**Wersje poprawione.** Redakcja może użyć tych samych modeli hostowanych lokalnie, aby porównać poprawkę z listem decyzyjnym i z poprzednim tekstem. Poprawki nie wysyła się do zewnętrznego API AI. Redaktor czyta to porównanie i decyduje, czy recenzenci mają zobaczyć poprawkę ponownie.

**Dokumentacja.** Redakcja przechowuje każde narzędzie, model i wersję, infrastrukturę, na której działały, datę, prompt użyty do kontroli redakcyjnej oraz raport po redakcji człowieka. Ten dziennik jest częścią dokumentacji recenzji.

Czasopismo nie zezwala, aby zgłoszone maszynopisy, recenzje ani listy decyzyjne służyły jako dane treningowe.

## 15. Naruszenie

Nieujawnione użycie AI jest naruszeniem etyki publikacyjnej. Czasopismo stosuje zasadę zerowej tolerancji: uchybienia nie daruje się dlatego, że redakcja „wygląda na drobną”, i nie pozostawia się go bez śladu w dokumentacji.

- **Przed publikacją.** Zgłoszenie jest odrzucane. Redaktor może odmówić przyjmowania kolejnych zgłoszeń odpowiedzialnych autorów przez okres, który wskaże na piśmie. Gdy naruszenie obejmuje sfabrykowane dane, sfabrykowane cytowania o istotnym znaczeniu albo nieprawdziwe twierdzenie o zgodzie lub rejestracji, redaktor może zawiadomić instytucję autorów.
- **Po publikacji.** Czasopismo publikuje sprostowanie albo retrakcję i mówi o tym publicznie. Sprostowanie stosuje się, gdy dane, cytowania i wnioski pozostają wiarygodne, a nieujawnione użycie ograniczało się do języka lub formatowania. Retrakcję stosuje się, gdy liczby, cytowania, obrazy albo interpretacje zostały wytworzone lub zmienione przez model i nie zostały zweryfikowane przez człowieka, albo gdy redaktor nie może już ufać zapisowi. Zob. [Etyka publikacyjna](publication-ethics.md).

Autorzy, którzy sami zauważą pominięcie, niezwłocznie zawiadamiają redaktora. Zgłoszenie własne jest odnotowywane i jest brane pod uwagę. Nie znosi obowiązku poprawienia zapisu publicznego.

## 16. Dokumenty powiązane

- [Oświadczenie o wykorzystaniu AI (wzór)](ai-disclosure-statement.md)
- [Dostępność danych i zasady FAIR](data-availability-and-fair-policy.md)
- [Polityka recenzji](peer-review-policy.md)
- [Wytyczne dla autorów](author-guidelines.md)
- [Etyka publikacyjna](publication-ethics.md)
- [Cele i zakres](aims-and-scope.md)
