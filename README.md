# Kotityösovellukseni

Päivitetty 2.5.2021: 

Sovellusta voi testata herokussa: https://tsoha-visitors666.herokuapp.com/

Voi joko kirjautua olemassaolevilla tunnuksilla (käyttäjä: testipossu, salasana: huulirasva) tai luoda oman tunnuksen ja kirjautua sillä.
Jos haluaa testata ylläpitäjän toiminnallisuutta, tulee kirjautua ylläpitäjänä käyttäjä: adminpossu, salasana: possuhallitsee. 

Sovelluksen käyttö tulisi olla aika itseohjautuvaa ja käyttöliittymän tukemaa. Toivon, että käyttäjälle on selvää miten sovellus toimii. Olen testannut
sovellusta melko paljon, mutta toki silti on mahdollista, että löytyy jotain bugeja joita en ole havainnut. Toivon, että kurssin päättymisen jälkeenkin
näistä bugin havaitsija (tai kurssin ohjaaja) tekisi githubiin issuen, jotta voisin sovellusta tarvittaessa korjata.

Alla oleva suunnitelma osoittautui hyväksy ohjenuoraksi sovelluksen kehittämiseen. Sovellukseen tulee kirjautua, jotta pääsee näkemään vapaita
kotitöitä sekä ilmoittamaan uusista, joko tekemättömistä tai tehdyistä kotitöistä. Käyttäjä voi sovelluksessa seurata ja päivittää valitsemiaan/tekemiään
kotitöitä. Käyttäjä voi myös seurata miten ylläpitäjä hyväksyy/maksaa tehtyjä kotitöitä. Lomakkeilla on logiikkaa, joka takaa ettei tyhjiä tai pahasti 
virheellisiä syötteitä lähetetä käyttäjän toimesta. Ylläpitäjä rooli on ainoa, joka voi merkata kotitöitä hyväksytyiksi ja maksetuiksi. Ylläpitäjä näkee
kaikkien käyttäjien keskeneräiset kotityöt, käyttäjät itse näkevät vain omansa. Kotityön vaiheet voi mennä kumpaan suuntaan vaan ja hypätä joitain vaiheita
yli - tämä on tarkoituksellista. Esimerkiksi jos kotityö ei ole kunnolla tehty, eikä sitä voi hyväksyä, sen voi siirtää takaisin vapaaksi. Sovelluksen ulkoasu on lapsille mieleinen. Sovellus vaikuttaa toimivan hyvin myös mobiililaitteella.

----------------------------------------------------------------------------------------------------------------------------------------
## Suunnitelma:
Minulla on useampia lapsia, ja jatkuvana ongelmana on se, etten muista kuka lapsi on milloinkin 
tehnyt mitäkin ja viikkorahojen maksu ei mene oikein. Sovelluksen tavoitteena on ratkaista tämä ongelma.
Tarkoitus on, että voin itse ylläpitäjänä listata tehtäviä töitä sovellukseen, mutta myös lapset (käyttäjät)
voivat itse lisätä töitä joita ovat tehneet. Ajattelin, että parasta olisi, ettei dataa tule liikaa tauluihin,
että kun maksan kotityöt, deletoin kotityöt joista palkka maksetaan. Toki maksun voisi merkitä myös jollakin
tavalla johonkin tauluun kuitatuksi.

### Kotityö-sovellus

- Käyttäjä voi kirjautua sisään ja ulos ja luoda uuden tunnuksen (10.4.21: Tehty)
- Käyttäjä näkee tehtävänä olevat kotityöt ja voi valita jonkun jolloin siitä näytetään lisätietoja (10.4.21: Tehty)
- Käyttäjä voi kuitata työn tehdyksi ja kirjata käytetyn ajan (10.4.21: Tehty)
- Käyttäjä voi etsiä kotitöitä yksittäisillä hakusanoilla (Tekemättä, kenties olisi tarpeellinen jos töitä kertyy paljon)
- Käyttäjä voi listata tekemänsä kotityöt (20.4.21: Tehty, ylläpitäjä näkee kaikkien.)
- Ylläpitäjä voi lisätä ja poistaa kotitöitä sekä määrittää kotityöstä näytettäviä tietoja (20.4.21: Kotitöitä ei poisteta, mutta ne siirtyvät
  eri sivuille näkyviin statuksen mukaan)
- Ylläpitäjä voi muokata käyttäjän raportoimaa ajankäyttöä (20.4.21: Tehty; kun ylläpitäjä kuittaa maksun kirjataan samalla tunnit "pysyviksi"
  siinä mielessä että palkka lasketaan ja maksetaan ylläpitäjän kirjaaman ajan mukaan)
- Ylläpitäjä voi määrittää uusille kotitöille arvioidun suoritusajan (voi, mutta voivat muutkin. Tätä en aio tehdä erilaiseksi ylläpitäjälle koska kyse vain arviosta)
- Ylläpitäjä voi poistaa käyttäjän raportoiman kotityön, esim kun palkka maksetaan, työ poistetaan. (20.4.21: Tehty, työ siirtyy maksettujen joukkoon)
- Ylläpitäjä näkee eri käyttäjien tekemät kotityöt (20.4.21: Tehty)

#### Lisäksi tehty vielä (päivitetty 2.5.2021):
- Tietoturva-asioita
- Ulkonäkö kivemmaksi
- Lomakkeiden syötteiden käsittelyä

Repositorion nimi muutettu: uusi nimi Tsoha-kotityosovellus
Päivitty myös labtooliin.

## Kehitysideoita

Kun sovellusta käytetään, voi jatkokehitystä tehdä havaintojen pohjalta. Ajankohtaiseksi ainakin tullee jossain vaiheessa maksettujen kotitöiden poistaminen
tietokannasta - tämä toiminnallisuus tulisi toteuttaa ylläpitäjälle.
