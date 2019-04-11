# labo-4-web-scraping-crawling
labo-4-web-scraping-crawling created by GitHub Classroom


## Web Crawling

# 1.0 Wat is Web Crawling
Een crawler is een computerprogramma dat automatisch documenten op internet zoekt. Crawlers zijn voornamelijk geprogrammeerd voor repetitieve acties, zodat browsen volledig geautomatiseerd is. Zoekmachines gebruiken het vaakst crawlers om door het WWW te bladeren en een index te maken. Andere crawlers zoeken echter verschillende soorten informatie, zoals RSS-feeds en e-mailadressen. De term crawler komt van de eerste zoekmachine voor internet, de webcrawler. Synoniemen zijn ook 'Bot' of 'Spider'. De meest bekende web crawler is de Googlebot.


# 2.0 Hoe werkt een crawler? 
In principe is een crawler als een bibliothecaris. Het zoekt naar informatie op het web, die het toewijst aan bepaalde categorieën, en indexeert en catalogiseert het zodat de gecrawlde informatie kan worden opgehaald en kan worden geëvalueerd. Terwijl de bibliothecaris zelfvoorzienend werkt en taken aan zijn team toewijst, verschilt de crawler doordat deze niet onafhankelijk is.

De werking van deze computerprogramma's moet worden vastgesteld voordat een dergelijke crawl wordt gestart. Elke bestelling wordt dus van tevoren gedefinieerd. De crawler voert deze instructies vervolgens automatisch uit. Klassiek wordt een index gemaakt met de resultaten van de crawler, die toegankelijk is via uitvoersoftware.
Welke informatie een crawler van het web verzamelt, is afhankelijk van de specifieke instructies. 
 
# 3.0 Is een Crawler wel veilig?
Zoekmachines crawlen het web door hun robots. Daarom noemen we alle "crawlers" van zoekmachines. Crawlers zijn slechts één type bot. Helaas zijn de meeste crawlers stoute programma's die zich niet goed gedragen, maar omdat ze "crawlers" zijn, nemen mensen aan dat ze iets goeds moeten doen (zoals het verzamelen van gegevens voor zoekmachines).

Niet elke zoekmachine is zoals Bing of Google. Sommige zoekmachines zijn privéhulpmiddelen die door bedrijven worden gebruikt voor hun eigen bedrijfsdoelen. 
Deze zoekmachines sturen geen bezoekers naar uw website op dezelfde manier als Bing, Google en andere zoekmachines.

Sommige zoekmachines worden door marketeers gebruikt om informatie over andere websites te verzamelen. En sommige zoekmachines worden gebruikt door criminele groepen (of spionageagentschappen) om potentiële hackers, uitbuiting en surveillance te identificeren.

De meerderheid van de zoekmachines die crawlers naar uw website sturen, zal u nooit bezoekers sturen. Deze zoekmachines verbinden de bronnen van uw webserver en voorkomen dat andere mensen uw site bezoeken.

Er is een vrijwillige standaard die crawler-ontwikkelaars kunnen kiezen om het Robots Exclusion Protocol te volgen . Dit protocol definieert een klein aantal richtlijnen dat u kunt specificeren in een tekstbestand op uw website (genaamd "robots.txt") dat goed opgevoede robots zullen zoeken en respecteren. U kunt hen vertellen om uit uw website te blijven of alleen bepaalde specifieke delen van uw website.

Grote zoekmachines vragen webmasters om het robots.txt-bestand te gebruiken om bepaalde soorten inhoud (zoals kalenderpagina's en pagina's met zoekresultaten op de site) te vermijden, die herhaaldelijk en niet nuttig zijn. U bent niet verplicht om de crawlers van deze pagina's te blokkeren, maar de zoekmachines kunnen minder aandacht schenken aan uw website als deze niet voldoet aan hun kwaliteitsnormen. En hun normen omvatten hoeveel verspillende inhoud die u publiceert.

# 3.1 Zijn Marketingtools  Rogue Crawlers
Elke crawler die alleen gegevens van uw website overneemt en geen tegenprestatie biedt, is een frauduleuze crawler. Sommige mensen zullen je vertellen dat rogue crawlers alleen die programma's zijn die de "robots.txt" -richtlijnen negeren, maar dat is niet altijd het geval. Sommige goed opgevoede crawlers zijn mogelijk nog steeds valse crawlers. Als ze uw site alleen bezoeken om gegevens te verzamelen die ze aan andere mensen kunnen verkopen of die hun exploitanten voor hun eigen voordeel kunnen gebruiken, maakt het niet uit of de crawlers zijn ontworpen om de "robots.txt" -standaard te respecteren.

Als een frauduleuze crawler "robots.txt" niet op uw website vindt, of als de richtlijnen niet precies zijn geschreven, omdat de programmeur van de crawler verwacht dat die richtlijnen worden geschreven, zal de crawler alles pakken wat hij heeft opgestuurd: dat zou kunnen afbeeldingen, volledige pagina's, scripts, gegevensbestanden en meer zijn.

Marketeers die hun eigen crawlers gebruiken, geven er niet om wat voor schade ze op uw website toebrengen. Ze zijn er alleen om informatie te verzamelen voor hun eigen voordeel. Veel van deze mensen beschouwen zichzelf als fijne, fatsoenlijke mensen. Sterker nog, ze zouden niet aarzelen om te stoppen en iemand te helpen die gestrand was op de weg of op straat gewond lag. Maar als het gaat om het verkrachten van het web voor eigen winst, hebben ze geen ethische normen.

# 3.0 Toepassingen
Het klassieke doel van een crawler is om een ​​index te maken. Aldus zijn crawlers de basis voor het werk van zoekmachines. Ze doorzoeken eerst het web op inhoud en maken de resultaten vervolgens beschikbaar voor gebruikers. Gerichte crawlers concentreren zich bijvoorbeeld op actuele, inhoud relevante websites bij het indexeren.

Maar webcrawlers worden ook voor andere disciplines gebruikt:
Prijsvergelijkingsportals zoeken naar informatie over specifieke producten op het web, zodat prijzen of gegevens nauwkeurig kunnen worden vergeleken.


Op het gebied van datamining kan een crawler openbaar beschikbare e-mail- of postadressen van bedrijven verzamelen.
Webanalysetools gebruiken crawlers of spiders om gegevens te verzamelen voor paginaweergaven of inkomende of uitgaande links .
Crawlers dienen om informatiehubs van gegevens te voorzien, bijvoorbeeld nieuwssites.
 
# 3.1 Toepassingen
Beautiful Soup is een Python-bibliotheek om gegevens uit HTML- en XML-bestanden te halen. Het werkt met uw favoriete parser om idiomatische manieren te bieden voor het navigeren, zoeken en wijzigen van de ontleedboom. Het bespaart programmeurs over het algemeen uren of dagen werk. Een ander bekende web crawler dat gebruikt kan worden in Python is ‘Scrapy’. Scrapy is een opensource webcrawling framework dat oorspronkelijk ontworpen werd voor webscraping maar het kan dus ook worden gebruikt als webcrawler voor algemene doeleinden. Scrapy is in handen van Scrapinghub. 

Niet alleen in Python bestaan web crawlers maar ook in bv Java. Eén van de meest gekend in Java is ‘Heritrix’. Hentrix is een web crawler geschreven door Internet Archive met als doeleind een web argief, de crawls worden gestart aan de hand van cli. Heritrix beschikbaar onder een vrije softwarelicentie.

 
 
# 4.0 Crawler vs. Scraper 
In tegenstelling tot een scraper, verzamelt een crawler alleen gegevens en bereidt deze voor. Schrapen is echter een black hat-techniek , die erop gericht is om gegevens in de vorm van inhoud van andere sites te kopiëren om het op die manier of een enigszins aangepaste vorm ervan op de eigen website te plaatsen. Hoewel een crawler meestal te maken heeft met metadata die op het eerste gezicht niet zichtbaar is voor de gebruiker, haalt een scraper tastbare inhoud uit.
 
# 5.0 Een crawler blokkeren
Als u niet wilt dat bepaalde crawlers door uw website bladeren, kunt u hun user-agent uitsluiten met robots.txt . Maar dat kan niet voorkomen dat inhoud wordt geïndexeerd door zoekmachines. De noindex- metatag of de canonieke tag is voor dit doel beter.

# 6.0 Betekenis voor zoekmachine-optimalisatie

Webcrawlers zoals de Googlebot bereiken hun doel om websites in de SERP te rangschikken door te crawlen en te indexeren. Ze volgen permanente links in het WWW en op websites. Per website heeft elke crawler een beperkt tijdsbestek en budget beschikbaar. Door de optimalisatie van de websitestructuur, zoals navigatie en bestandsgrootte, kunnen website-exploitanten het crawlbudget van de Googlebot beter benutten. Tegelijkertijd neemt het budget toe door een verscheidenheid aan inkomende links en een sterk bezochte website. De belangrijke instrumenten die nodig zijn voor het beheren van Crawlers, zoals de Googlebot, zijn de robots.txt-gegevens en de XML-sitemap die is opgeslagen in de Google Search Console.. In het SGR kan een sms worden verzonden of alle relevante delen van een website kunnen worden bereikt en geïndexeerd door de Googlebot.


## Web Scraping

# 1.0 Wat is Web Scraping

Web Scraping is bekend onder vele andere namen, afhankelijk van hoe een bedrijf het graag noemt, Screen Scraping, Web Data Extraction, Web Harvesting zijn een techniek die wordt gebruikt om grote hoeveelheden gegevens van websites te extraheren. 

De gegevens worden geëxtraheerd uit verschillende websites en opslagplaatsen en worden lokaal opgeslagen voor direct gebruik of analyse die later moet worden uitgevoerd. Gegevens worden opgeslagen in een lokaal bestandssysteem of databasetabellen, volgens de structuur van de geëxtraheerde gegevens. De meeste websites, die we regelmatig bekijken, laten ons toe alleen de inhoud te bekijken en staan ​​over het algemeen geen kopieer- of downloadmogelijkheid toe. 

Het handmatig kopiëren van de gegevens is net zo goed als het knippen van kranten en kan dagen en weken duren. Web scraping is de techniek om dit proces te automatiseren, zodat een intelligent script u kan helpen bij het extraheren van gegevens van webpagina's van uw keuze en deze in een gestructureerde indeling kunt opslaan.

Een webscraping-software laadt automatisch meerdere webpagina's één voor één en extraheert gegevens volgens de vereisten. Het is op maat gemaakt voor een specifieke website of een website die op basis van een reeks parameters kan worden geconfigureerd om met elke website te werken. Met een klik op de knop kunt u eenvoudig de gegevens die op een website beschikbaar zijn, opslaan in een bestand op uw computer.
In de wereld van vandaag doen intelligente bots webschrapen. 

In tegenstelling tot schermschrapen, waarbij alleen de pixels op het scherm worden gekopieerd, extraheren deze bots onderliggende HTML-code, evenals de gegevens die zijn opgeslagen in een database op de achtergrond.



# 2.0 Is web scraping niet zo onschuldig?
Het is algemeen bekend dat web scraping  een manier is om gegevens van websites te extraheren. Het is een dwang voor veel soorten bedrijven om gegevens te scrapen en te analyseren. Maar het is even waar dat veel mensen niet zeker zijn van de legaliteit van web scraping . 
Web scraping zelf is niet illegaal. Maar er zijn ook enkele wettelijke, morele en ethische beperkingen, die bedrijven weerhouden van het gebruik van webgegevens scrapers.

De intentie van scrapers zal ook niet altijd even onschuldig zijn. Bovendien is heel wat data op websites, zoals teksten en foto’s, auteursrechtelijk beschermd en mag deze dus niet zomaar weggeplukt worden. Hier heb je de toestemming van de oorspronkelijke auteur nodig.

 Het geautomatiseerde proces kopieert en plakt veel sneller dan een mens. Het gevaar hiervan is dat jouw website in een mum van tijd kan worden nagemaakt. Dit proces verloopt zó gedetailleerd, dat bezoekers van websites het ‘echte’ verkeer niet meer van het ‘web scraping’ verkeer kunnen onderscheiden.

Web scraping gaat ten koste van de echte content op websites. Officiële publicisten hebben namelijk het recht om hun eigen content te beheren, maar lang niet iedereen houdt zich aan de regels. De oplossing die daarvoor was bedacht, is de inzet van CAPTCHA’S. Je moet nu voordat je sommige websites betreedt even bewijzen dat je geen robot bent. Maar ook deze CAPTCHA’S houden helaas de allerslimste web scraping bots niet buiten de deur.


# 3.0 Verschillende benaderingen van webschrapen
# 3.1 DaaS of Data as a Service
Het uitbesteden van uw webgegevensextractie vereist een serviceprovider die met gegevens omgaat, is de meest aanbevolen en de gemakkelijkste manier om de honger naar gegevens van uw bedrijf te lessen. Wanneer uw gegevensprovider u helpt bij het extraheren en opschonen van gegevens, raakt u de noodzaak kwijt van een volledig apart toegewijd team om data lekken aan te pakken en kan u opgelucht blijven. Zowel de software als de infrastructuurbehoeften die de datatextractietechnieken van uw bedrijf nodig hebben, worden door hen verzorgd en aangezien deze bedrijven regelmatig gegevens voor klanten extraheren, zou u nooit een probleem hebben dat ze niet hebben opgelost of althans ten minste geconfronteerd. Het enige dat u hoeft te doen, is hen van uw vereisten voorzien en vervolgens achterover leunen terwijl zij hun magie draaien en u uw onschatbare gegevens meedelen.
 
# 3.2 In-house web scraping
U kunt ook doorgaan voor een interne gegevensextractie als uw bedrijf technisch rijk is. U zou niet alleen bekwame mensen nodig hebben die in webschrapingprojecten en experts in R en Python hebben gewerkt, maar u zou ook de omslachtige infrastructuur nodig hebben om uw team websites dag en nacht te laten slopen.
Webcrawlers breken zelfs bij de kleinste verandering in de webpagina's die ze targeten en dankzij deze web-scraping is het nooit een do en forget oplossing. U hebt het toegewijde team nodig om de hele tijd aan oplossingen te werken en soms anticiperen ze op een grote verandering in de manier waarop webpagina's gegevens opslaan en dan moeten ze daarop voorbereid zijn. Zowel het bouwen als onderhouden van een web scrapingteam zijn complexe taken en moeten alleen worden ondernomen als uw bedrijf over voldoende middelen beschikt.

# 3.3. Verticale specifieke oplossingen
Dataproviders die alleen op een specifieke branche-branche werken, zijn er in hordes en deze oplossingen voor verticale specifieke data-extractie zijn geweldig als u er een kunt vinden die aan uw gegevensbehoeften voldoet. Aangezien uw serviceprovider alleen in een enkel domein zou werken, is de kans groot dat zij zeer bekwaam zijn in dat domein. De gegevenssets kunnen variëren en de oplossingen die ze mogelijk bieden, zijn mogelijk zeer aanpasbaar op basis van uw behoeften. Ze kunnen u mogelijk verschillende pakketten aanbieden op basis van uw bedrijfsgrootte en budgetten.
 
# 4.0 Toepassingen
Bekende frameworks bij web scraping zijn Scrapy & Beautifulsoup, beide frameworks werden al aangehaald bij web crawling. Scrapy werd oorspronkelijk gemaakt als web scraper. 

Niet iedereen kan coderen dus zijn er ook web scrapers die je kan gebruiken zonder code, een voorbeeld hiervan is Octoparse. Octoparse gaat als volg te werk:

- Je gaat naar de website die je graag zou scrapen
- Selecteer de data die je graag wil binnentrekken 
- Start Octoparse en trek de data binnen 




