Feature: Inloggning
    För att kunna handla
    Som användare
    Måste jag logga in med rätt uppgifter

    Scenario Outline: Inloggningstest
        Given en användare med användarnamn "test" och lösenord "hemligt"
        When jag försöker logga in med användarnamn "<user>" och lösenord "<pwd>"
        Then inloggningen ska vara <resultat>

        Examples:
            | user  | pwd     | resultat   |
            | test  | hemligt | lyckad     |
            | test  | fel     | misslyckad |
            | annan | hemligt | misslyckad |
