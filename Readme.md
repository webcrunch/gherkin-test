📚 BDD – Webbutik med Behave
Detta repo innehåller en övningsuppgift i Behaviour Driven Development (BDD) med Gherkin och Behave. Systemet simulerar en enkel webbutik som säljer böcker, med funktionalitet för varukorg, rabatt, lagerhantering och inloggning.

🚀 Del 1 – Grundfunktionalitet
I första delen implementerades en varukorg med följande krav:

Lägga till böcker i varukorgen

Ta bort böcker från varukorgen

Visa aktuell summa och antal böcker

Öka antalet om samma bok läggs till flera gånger

Tömma varukorgen

Teknik
Funktionell Python‑kod (ingen OOP) med type hints

.feature‑fil med scenarier i Gherkin

Step‑definitioner i Behave som kopplar scenarierna till Python‑funktionerna

🔧 Del 2 – Extra funktionalitet
Jag valde att implementera tre extrafunktioner:

Rabattfunktion

10% rabatt på hela kundkorgen om fler än tre böcker köps.

Testfall inkluderar både normala och större antal böcker.

Lagerhantering

Varje bok har ett lagersaldo.

Om användaren försöker köpa fler än vad som finns i lager begränsas antalet automatiskt.

Login

Användaren måste logga in med giltiga uppgifter innan köp kan genomföras.

Scenario Outline används för att testa både lyckade och misslyckade inloggningar.

📂 Struktur
Kod
features/
├── bookstore_cart.feature   # Del 1 – varukorg
├── discount.feature         # Del 2 – rabatt
├── stock.feature            # Del 2 – lager
├── login.feature            # Del 2 – login
└── steps/
    ├── cart_steps.py
    ├── discount_steps.py
    ├── stock_steps.py
    └── login_steps.py
cart.py
README.md
requirements.txt
▶️ Körning
Installera beroenden:

bash
pip install -r requirements.txt
Kör alla tester:

bash
behave
✨ Reflektion
Lätt: Att skriva scenarier i Gherkin och koppla dem till enkla Python‑funktioner.

Svårt: Att undvika duplicerade steps mellan olika feature‑filer (löste det genom att återanvända generella steps och bara lägga till nya där det behövdes).

Lärdom: BDD blir tydligt och kraftfullt när man håller språket enkelt och återanvänder stegdefinitioner smart.

📚 Resurser
Behave dokumentation

Python typing

Kursmaterialet från Testautomatisering och testverktyg