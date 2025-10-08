Feature: Rabatt på stora köp
    För att uppmuntra större köp
    Som kund
    Vill jag få rabatt när jag köper fler än tre böcker

    Scenario Outline: Rabatt tillämpas korrekt
        Given en tom varukorg
        When jag lägger till <antal> böcker med pris 100
        Then den rabatterade summan ska vara <förväntat>

        Examples:
            | antal | förväntat |
            | 2     | 200       |
            | 3     | 300       |
            | 4     | 360       |
            | 10    | 900       |
