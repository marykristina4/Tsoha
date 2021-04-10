Tsoha-aiheen suunnittelua

Sovellusta voi testata herokussa: https://tsoha-visitors666.herokuapp.com/
Voi joko kirjautua olemassaolevilla tunnuksilla (käyttäjä: hildahippo, salasana: mutaruoho) tai luoda oman tunnuksen ja kirjautua sillä.

Ajattelin että sovelluksen laajuus olisi suunnilleen tämä jo nyt toteutettu, mutta vielä tärkein puuttuva on ylläpitäjän tehtävät ja
niiden toteutus. 

Todo:
Seuraavaksi pitäisi tehdä:
-joinit eli kotitöitä kun listataan ei näkyisi numeroita vaan kentistä descriptionit
-adminin toiminnallisuudet eli töiden hyväksyntä ja palkanmaksu 
-virheiden käsittelyä
-ulkonäköä

Kysymys: Onko parempi toteuttaa ylläpitäjän toiminnallisuudet näille olemassa oleville sivuille jonkinlaisella logiikalla vai onko ok 
tehdä erillinen linkki pääsivulta ylläpitäjälle niin että hänellä on omat sivut omiin töihinsä?
----------------------------------------------------------------------------------------------------------------------------------------
## Suunnitelma:
Minulla on useampia lapsia, ja jatkuvana ongelmana on se, etten muista kuka lapsi on milloinkin 
tehnyt mitäkin ja viikkorahojen maksu ei mene oikein. Sovelluksen tavoitteena on ratkaista tämä ongelma.
Tarkoitus on, että voin itse ylläpitäjänä listata tehtäviä töitä sovellukseen, mutta myös lapset (käyttäjät)
voivat itse lisätä töitä joita ovat tehneet. Ajattelin, että parasta olisi, ettei dataa tule liikaa tauluihin,
että kun maksan kotityöt, deletoin kotityöt joista palkka maksetaan. Toki maksun voisi merkitä myös jollakin
tavalla johonkin tauluun kuitatuksi.

Kotityö-sovellus

- Käyttäjä voi kirjautua sisään ja ulos ja luoda uuden tunnuksen (10.4.21: Tehty)
- Käyttäjä näkee tehtävänä olevat kotityöt ja voi valita jonkun jolloin siitä näytetään lisätietoja (10.4.21: Tehty)
- Käyttäjä voi kuitata työn tehdyksi ja kirjata käytetyn ajan (10.4.21: Tehty)
- Käyttäjä voi etsiä kotitöitä yksittäisillä hakusanoilla (Tekemättä, kenties olisi tarpeellinen jos töitä kertyy paljon)
- Käyttäjä voi listata tekemänsä kotityöt (Tällä hetkellä näkee kaikki tehdyt kotityöt, voisi filtteröidä niin että näkee omansa)
- Ylläpitäjä voi lisätä ja poistaa kotitöitä sekä määrittää kotityöstä näytettäviä tietoja (toimii nyt samoin kuin muille käyttäjille)
- Ylläpitäjä voi muokata käyttäjän raportoimaa ajankäyttöä (voi, mutta niin voivat muutkin vielä...)
- Ylläpitäjä voi määrittää uusille kotitöille arvioidun suoritusajan (voi, mutta voivat muutkin. Tätä en aio tehdä erilaiseksi ylläpitäjälle)
- Ylläpitäjä voi poistaa käyttäjän raportoiman kotityön, esim kun palkka maksetaan, työ poistetaan. (Tekemättä)
- Ylläpitäjä näkee eri käyttäjien tekemät kotityöt (Toistaiseksi kaikki näkee kaiken, tämä kaikkien kotitöiden näkymä tulevaisuudessa vain
ylläpitäjälle)

Repositorion nimi muutettu: uusi nimi Tsoha-kotityosovellus
Päivitty myös labtooliin.
