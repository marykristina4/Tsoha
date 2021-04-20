# Kotityösovelluksen suunnittelua ja statusta:

Päivitetty 20.4.2021
Sovellusta voi testata herokussa: https://tsoha-visitors666.herokuapp.com/
Voi joko kirjautua olemassaolevilla tunnuksilla (käyttäjä: hildahippo, salasana: mutaruoho) tai luoda oman tunnuksen ja kirjautua sillä.
Jos haluaa testata ylläpitäjän toiminnallisuutta, tulee kirjautua ylläpitäjänä käyttäjä: adminpossu, salasana: possuhallitsee. 
Ajattelin että sovelluksen laajuus olisi suunnilleen tämä jo nyt toteutettu, vielä pitää tehdä siistimistä, testaamista ja ulkonäköön liittyvää kehitystä. 

Todo:
Seuraavaksi pitäisi tehdä: 
-testaamista
-ulkonäköä

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
- Käyttäjä voi listata tekemänsä kotityöt (20.4.21: Tehty, ylläpitäjä näkee kaikkien.)
- Ylläpitäjä voi lisätä ja poistaa kotitöitä sekä määrittää kotityöstä näytettäviä tietoja (20.4.21: Kotitöitä ei poisteta, mutta ne siirtyvät
  eri sivuille näkyviin statuksen mukaan)
- Ylläpitäjä voi muokata käyttäjän raportoimaa ajankäyttöä (20.4.21: Tehty; kun ylläpitäjä kuittaa maksun kirjataan samalla tunnit "pysyviksi"
  siinä mielessä että palkka lasketaan ylläpitäjän kirjaaman ajan mukaan)
- Ylläpitäjä voi määrittää uusille kotitöille arvioidun suoritusajan (voi, mutta voivat muutkin. Tätä en aio tehdä erilaiseksi ylläpitäjälle)
- Ylläpitäjä voi poistaa käyttäjän raportoiman kotityön, esim kun palkka maksetaan, työ poistetaan. (20.4.21: Tehty, työ siirtyy maksettujen joukkoon)
- Ylläpitäjä näkee eri käyttäjien tekemät kotityöt (20.4.21: Tehty)

Repositorion nimi muutettu: uusi nimi Tsoha-kotityosovellus
Päivitty myös labtooliin.
