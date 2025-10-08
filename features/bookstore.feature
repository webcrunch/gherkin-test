Feature: Hantera varukorg i webbutik
    För att kunna köpa böcker
    Som användare
    Vill jag kunna lägga till, ta bort och se min varukorg

    Scenario: Lägga till en bok i varukorgen
        Given en tom varukorg
        When jag lägger till boken "Clean Code" med pris 200
        Then ska varukorgen innehålla 1 bok
        And den totala summan ska vara 200

    Scenario: Ta bort en bok från varukorgen
        Given en varukorg med boken "Clean Code" (pris 200)
        When jag tar bort boken "Clean Code"
        Then ska varukorgen vara tom

    Scenario: Lägga till samma bok flera gånger
        Given en tom varukorg
        When jag lägger till boken "Clean Code" med pris 200
        And jag lägger till boken "Clean Code" med pris 200
        Then ska varukorgen innehålla 2 exemplar av "Clean Code"
        And den totala summan ska vara 400

    Scenario: Tömma varukorgen
        Given en varukorg med boken "Clean Code" (pris 200)
        And boken "Refactoring" (pris 300)
        When jag tömmer varukorgen
        Then ska varukorgen vara tom
