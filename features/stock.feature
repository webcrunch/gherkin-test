Feature: Lagerhantering
    För att undvika översäljning
    Som kund
    Vill jag inte kunna köpa fler böcker än vad som finns i lager

    Scenario: Försök köpa fler än lagersaldo
        Given en bok "Clean Code" med pris 200 och lagersaldo 2
        When jag försöker köpa 5 exemplar av "Clean Code"
        Then varukorgen ska innehålla 2 exemplar av "Clean Code"
