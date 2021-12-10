#!/usr/bin/env python
# coding: utf-8
---
title: "MANOVA"
output:
  html_document:
    theme: lumen
    toc: yes
    toc_depth: 2
    toc_float: 
      collapsed: FALSE 
    number_sections: true
    includes:
      in_header: ["../01. Includes/html/nocache.html", "../01. Includes/html/favicon.html", "../01. Includes/html/analytics.html"]
  keywords: [statistisch handboek, studiedata]
---
# <!-- ## CLOSEDBLOK: Functies.R -->

# In[1]:


library(here)
if (!exists("Substitute_var")) {
  ## Installeer packages en functies
  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)
}


# <!-- ## /CLOSEDBLOK: Functies.R -->
# 
# <!-- ## CLOSEDBLOK: CSS -->
# <style>
# `r htmltools::includeHTML(paste0(here::here(),"/01. Includes/css/Stylesheet_SHHO.css"))`
# </style>
# <!-- ## /CLOSEDBLOK: CSS -->
# 
# <!-- ## CLOSEDBLOK: Header.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Header.R -->
# 
# <!-- ## CLOSEDBLOK: Status.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Status.R -->
# 
# <!-- ## CLOSEDBLOK: Reticulate.R -->
# 
# <!-- ## /CLOSEDBLOK: Reticulate.R -->
# 
# <!-- ## OPENBLOK: Data-aanmaken.R -->

# In[ ]:


source(paste0(here::here(),"/01. Includes/data/58.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# Gebruik de *MANOVA* om te toetsen of groepen gebaseerd op één of meer onafhankelijke categorische variabelen van elkaar verschillen voor meerdere afhankelijke variabelen tegelijk. In de casus behorend bij deze toetspagina is er één onafhankelijke variabele die de groepen definieert. Er wordt dus een *one-way MANOVA* uitgevoerd.[^1]<sup>,</sup>[^20]
# 
# # Onderwijscasus
# <div id = "casus">
# 
# Bij de masteropleiding Bioinformatics worden studenten met een bachelor Biologie, Wiskunde en Informatica toegelaten. De decaan van de faculteit wil deze toelatingseisen evalueren en onderzoeken of het curriculum aansluit bij de studenten van deze vooropleidingen. Daarom vergelijkt zij de studenten van de drie vooropleidingen wat betreft hun gemiddelde cijfers in periode 1, 2 en 3. Op basis hiervan kan zij de toelaatbaarheid voor de drie bacheloropleidingen heroverwegen of overwegen om daarnaast een aantal specifiek te volgen bachelorvakken op te nemen in de ingangseisen.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil tussen de gemiddelde cijfers in periode 1, 2 en 3 voor studenten afkomstig van de bacheloropleidingen Biologie, Wiskunde en Informatica.
# 
# *H~A~*: Er is een verschil tussen de gemiddelde cijfers van ten minste een van de onderwijsperiodes (periode 1, 2 en 3) voor studenten afkomstig van de bacheloropleidingen Biologie, Wiskunde en Informatica.
# 
# </div>
# 
# # MANOVA
# 
# De *MANOVA* is de multivariate versie van de *ANOVA*. De *ANOVA* toetst een verschil in het gemiddelde van een afhankelijke variabele tussen verschillende groepen. De *MANOVA* vergelijkt ook een verschil tussen groepen, maar nu het verschil in gemiddelden van meerdere afhankelijke variabelen tegelijk. Om precies te zijn wordt er een lineaire combinatie van de afhankelijke variabelen gevonden waarvoor de groepen het meest van elkaar verschillen.
# 
# Als alternatief voor de *MANOVA* zou er ook voor elke afhankelijke variabele apart een *ANOVA* uitgevoerd kunnen worden. De *MANOVA* heeft twee voordelen ten opzichte van dit alternatief. Allereerst heeft de *MANOVA* een hoger onderscheidend vermogen[^3] om een verschil tussen groepen te vinden, omdat er rekening wordt gehouden met de onderlinge samenhang van de afhankelijke variabelen. Daarnaast heeft de *MANOVA* een kleinere type I fout. Dit is de kans dat de nulhypothese ten onrechte verworpen wordt en er dus een effect gevonden wordt dat er eigenlijk niet is. De reden hiervoor is dat het aantal toetsen verschilt. Bij de *MANOVA* is er slechts één toets, wat een type I fout van 5% oplevert voor een significantieniveau van 0,05. Bij het uitvoeren van meerdere *ANOVA's* is er een type I fout van 5% voor elke afhankelijke variabele. De overall type I fout - de kans dat bij minimaal een van de toetsen de nulhypothese ten onrechte verworpen wordt - is dan logischerwijs hoger dan 5%. De overall type I fout is te berekenen met de formule $1 - (1-\alpha)^p$ waarbij $p$ het aantal afhankelijke variabelen is en $\alpha$ het significantieniveau. In de huidige casus zijn er drie afhankelijke variabelen en wordt een significantieniveau van 0,05 gehanteerd. De overall type I fout voor het uitvoeren van meerdere *ANOVA's* zou dus $1 - 0,95^3 = 0,14$ zijn, wat bijna drie keer zo hoog is als de type I fout bij een *MANOVA*.[^20]
# 
# Net zoals bij de *ANOVA* is de *MANOVA* uit te voeren voor één of meerdere onafhankelijke variabelen. Bij de *one-way MANOVA* worden groepen gebaseerd op één onafhankelijke variabele vergeleken voor meerdere afhankelijke variabelen. Bij de *factoriële MANOVA* worden groepen vergeleken die gebaseerd zijn op meerdere onafhankelijke variabelen. Hierbij kunnen er ook interactie-effecten tussen de onafhankelijke variabelen optreden. In deze toetspagina wordt een voorbeeld van de *one-way MANOVA* uitgewerkt. Op vergelijkbare wijze kan een *factoriële MANOVA* uitgevoerd worden. Voor meer informatie over de aanpak bij meerdere onafhankelijke variabelen, zie de [toetspagina](29-Factoriele-ANOVA-R.html) van de *factoriële ANOVA*.
# 
# # Procedure
# 
# De procedure bij de *MANOVA* bestaat uit meerdere stappen. De eerste stap is de *MANOVA* zelf: hierbij wordt onderzocht of er een verschil tussen de groepen is voor minimaal één van de afhankelijke variabelen. Als er in deze stap geen significant resultaat is, dan is de conclusie dat er voor geen enkele afhankelijke variabele een verschil lijkt te zijn tussen de groepen. Als de *MANOVA* wel significant is, dan is de volgende stap om te onderzoeken voor welke afhankelijke variabele(n) er een verschil tussen de groepen is. 
# 
# Voer hiervoor een *ANOVA* uit voor elke afhankelijke variabele apart. Omdat er meerdere toetsen tegelijkertijd worden uitgevoerd, is de overall type I fout hoger. Daarom is het nuttig om een correctie op de p-waarde van de *ANOVA's* uit te voeren. Aangezien dit niet in de ANOVA-functie in R gedaan kan worden, moet dit handmatig. Een simpel uit te voeren correctie is de Bonferroni correctie. Hierbij wordt het significantieniveau gedeeld door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. In de huidige casus wordt het significantieniveau van 0,05 gedeeld door drie (gemiddelde cijfers van periode 1, 2 en 3) wat leidt tot een nieuw significantieniveau van 0,017.[^20] Er zijn ook andere opties voor een correctie op de p-waarden.[^13]
# 
# Zeer waarschijnlijk wordt er voor één of meerdere afhankelijke variabelen een significant verschil in gemiddelde van de groepen gevonden. De derde stap is in dat geval om voor deze significante *ANOVA's* post-hoc toetsen uit te voeren. Met post-hoc toetsen wordt bepaald welke specifieke groepen van elkaar verschillen voor die afhankelijke variabele. Hierbij worden er opnieuw meerdere toetsen tegelijkertijd uitgevoerd wat de overall type I fout verhoogt. Voer daarom weer een correctie voor meerdere toetsenuit. Bij de *one-way ANOVA* is de Tukey HSD correctie hiervoor een gebruikelijke optie; bij de *factoriële ANOVA* is de Games-Howell correctie een gebruikelijke optie. Er zijn ook andere opties voor een correctie op de p-waarden.[^13]
# 
# # Toetsstatistiek
# 
# Er zijn meerdere methoden om de toetsstatistiek van de *MANOVA* te berekenen. De vier meeste gebruikte versie zijn *Wilks's Lambda*, *Hotelling's Trace*, *Roy's Largest Root* en *Pillai's Trace*. Afhankelijk van allerlei karakteristieken van de data met betrekking tot bijvoorbeeld steekproefgroottes en assumpties is soms de ene toetsstatistiek en soms de andere toetsstatistiek de beste optie. Meer informatie hierover is te vinden in de boeken van Field[^22] en Tabachnick & Fidell[^20]. In het algemeen wordt *Wilks's Lambda* gebruikt, omdat deze in de meeste situaties het hoogste onderscheidend vermogen heeft. Bij een laag aantal observaties, verschillen in het aantal observaties per groep en afwijkingen van de assumptie van homogeniteit van variantie-covariantie matrices is *Pillai's Trace* vanwege zijn robuustheid een betere optie. De keuze voor een toetsstatistiek is echter iets om goed over na te denken en uiteindelijk aan de onderzoeker.[^20]
# 
# # Uitleg assumpties
# 
# Om een valide resultaat te vinden met de *MANOVA*, dient er aan een aantal assumpties voldaan te worden.[^1]<sup>,</sup>[^20] In deze sectie worden de assumpties allen toegelicht en worden de opties bij het niet voldoen aan de assumptie weergegeven. Verderop in de toetspagina worden de assumpties getoetst met de dataset van de onderwijscasus.
# 
# ## Outliers
# 
# Voordat gestart kan worden met de *MANOVA*, moet de data gescreend worden op de aanwezigheid van outliers. Outliers (uitbijters) zijn observaties die sterk afwijken van de overige observaties. Univariate outliers zijn observaties die afwijken voor één specifieke variabele, zoals een student die twintig jaar over zijn studie heeft gedaan. Multivariate outliers zijn observaties die afwijken door de combinatie van meerdere variabelen, zoals een persoon van 18 jaar met een inkomen van €100.000,-. De leeftijd van 18 jaar is geen outlier op zichzelf en een inkomen van €100.000,- is dat ook niet. Echter, de combinatie van beide zorgt ervoor dat de observatie vrij onwaarschijnlijk is.[^4]
# 
# Na het vinden van een outlier is de volgende stap om een goede oplossing voor te outlier te bedenken. Het is van belang hier goed over na te denken en niet zomaar een outlier te verwijderen met als enige argument dat het een outlier is. In het algemeen kan er onderscheid gemaakt worden tussen onmogelijke en onwaarschijnlijke outliers.[^5] Een onmogelijke outlier is een observatie die technisch gezien niet kan kloppen, bijvoorbeeld een leeftijd van 1000 jaar, een negatief salaris of een man die zwanger is. Bij deze outliers is het een optie om de waarde te vervangen als er een overduidelijke fout bij het invoeren van de data is gemaakt. Een andere optie is de waarde te verwijderen. Een onwaarschijnlijke outlier is een observatie die technisch gezien wel kan, maar heel erg afwijkt van de overige observaties. De rijksten der aarde zijn in de stad of het dorp waar zij wonen qua vermogen waarschijnlijk een outlier. Maar het zijn bestaande personen dus het verwijderen van de observatie zou hier foutief zijn. Opties in deze situatie zijn de variabele(n) te transformeren, de outlier gewoon mee te nemen in de analyse of de analyse met en zonder de outlier uit te voeren en beide te rapporteren. Ook is het niet verboden om de outlier toch te verwijderen, maar het is in dat geval wel van belang dit transparant te rapporteren en op een goede wijze te beargumenteren.[^5]
# 
# Bij de *MANOVA* zijn er twee nuttige methoden om outliers te vinden.[^23]
# 
# ### Boxplots en standaardiseren
# 
# Begin voor de analyse met het screenen van de variabelen in de dataset op de aanwezigheid van univariate outliers. Voor continue variabelen bestaat deze screening uit het visualiseren van de variabele met een boxplot en het standaardiseren[^6] van de variabele. Als een observatie een gestandaardiseerde score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. In dat geval wijkt de observatie namelijk meer dan drie standaardafwijkingen af van het gemiddelde van de variabele. Gebruik zowel de boxplot als de standaardisering om outliers te vinden voor de afhankelijke variabelen.[^5]
# 
# ### Mahalanobis afstand
# 
# Multivariate outliers zijn deelnemers[^19] met een combinatie van observaties op verschillende variabelen die erg afwijken van de overige deelnemers. Deze multivariate outliers kunnen geïdentificeerd worden met de Mahalanobis afstand. De Mahalanobis afstand is een maat die aangeeft in hoeverre de observaties van een deelnemer voor alle afhankelijke variabelen afwijken van de gemiddeldes van de afhankelijke variabelen. Het is een maat voor een afstand tussen twee punten als meerdere variabelen worden gebruikt. Gebruik de Mahalanobis afstand om te onderzoeken of er multivariate outliers zijn bij de afhankelijke variabelen.[^23] Bereken de Mahalanobis afstand voor elke deelnemer en vergelijk deze met de criteriumwaarde. De criteriumwaarde wordt bepaald op basis van de chi-kwadraat score bij een aantal vrijheidsgraden dat gelijk is aan het aantal variabelen en een significantieniveau van 0,001 (of een zelf gekozen significantieniveau). In de code wordt toegelicht hoe de criteriumwaarde bepaald kan worden.[^4]
# 
# ## Aantal observaties per groep
# 
# Om de *MANOVA* uit te voeren, moeten er voor elke groep meer observaties zijn dan het aantal afhankelijke variabelen. Dit is enerzijds een vereiste om de variantie-covariantie matrix te berekenen en anderzijds nodig voor het onderscheidend vermogen van de *MANOVA*. In de meeste gevallen wordt er voldaan aan deze assumptie. Echter, als er meerdere onafhankelijke variabelen zijn, kan het voorkomen dat voor een van de combinaties van de categorieën van de onafhankelijke variabelen er te weinig observaties zijn. Deze assumptie is op simpele wijze te toetsen door het aantal observaties per groep met een tabel te inspecteren. Als er niet genoeg observaties per groep zijn, dan zijn er meerdere oplossingen mogelijk. De groep kan verwijderd worden of samengevoegd worden met een andere groep. Daarnaast is meer data verzamelen ook een goede optie.[^20]
# 
# ## Multivariate normaliteit
# 
# Een assumptie van de *MANOVA* is dat de afhankelijke variabelen een multivariate normaalverdeling volgen. De multivariate normaalverdeling is de multivariate versie van de (univariate) normaalverdeling. Als variabelen een multivariate normaalverdeling volgen, dan is elke lineaire combinatie van de variabelen normaal verdeeld. Bij de *MANOVA* moet er voor elke groep een normale verdeling zijn voor elke afhankelijke variabele. Onderzoek de assumptie door voor elke groep een histogram te maken voor elke afhankelijke variabele. De *MANOVA* is redelijk robuust ten opzichte van een schending van de assumptie van multivariate normaliteit. Als het aantal vrijheidsgraden van de residuën groter is dan 20 en de afwijkingen van normaliteit zichtbaar in de histogrammen niet door outliers veroorzaakt worden, dan is de *MANOVA* robuust ten opzichte van de assumptie van multivariate normaliteiten kan de *MANOVA* gewoon uitgevoerd worden. Als dit niet het geval is, dan is het transformeren van de afhankelijke variabele(n) die afwijken van de normaalverdeling een optie.[^7] Er is geen nonparametrische variant voor de *MANOVA*. Als er geen geschikte transformatie gevonden kan worden, dan is het een optie om bij een *one-way MANOVA* voor de afhankelijke variabelen die afwijken van de normaalverdeling apart een [Kruskal Wallis toets](10-Kruskal-Wallis-toets-I-R.html). Voor de *factoriële MANOVA* is het in dit geval een optie om voor de afhankelijke variabelen die afwijken van de normaalverdeling apart de *ANOVA* uit te voeren als regressiemodel (zie hiervoor bijbehorened [toetspagina](29-Factoriele-ANOVA-R.html)).[^20]
# 
# ## Homogeniteit van variantie-covariantie matrices
# 
# <!-- ## TEKSTBLOK: Link2.R -->
# Een assumptie van de *ANOVA* is dat de variantie van de afhankelijke variabele ongeveer hetzelfde is in elke groep. Bij de *MANOVA* zijn er meerdere afhankelijke variabelen en is er dus ook een multivariate versie van deze assumptie die al deze afhankelijke variabelen betreft. Elke afhankelijke variabele heeft een variantie, maar onderling hebben de paren van afhankelijke variabelen ook een covariantie. Deze covariantie toont de sterkte van de samenhang tussen twee variabelen en is in feite een ongestandaardiseerde correlatie. De correlatie tussen twee variabelen toont de sterkte van de samenhang aan en ligt tussen de -1 en 1 en is een herberekening van de covariantie. Voor de *MANOVA* geldt dat de varianties en covarianties van de afhankelijke variabelen ongeveer even groot moeten zijn in elke groep. De varianties en covarianties kunnen wiskundig gebundeld worden in een matrix. De assumptie bij de *MANOVA* betreft daarom de homogeniteit van variantie-covariantie-matrices.[^20]
# 
# De assumptie van homogeniteit van variantie-covariantie-matrices wordt getoetst met *Box's M test*. Bij een p-waarde kleiner dan 0,01 zijn er significante verschillen tussen de variantie-covariantie matrices van de groepen en is er niet voldaan aan deze assumptie. Hierbij wordt er afgeweken van het gebruikelijke significantieniveau van 0,05, omdat *Box's M test* erg gevoelig voor verschillen is. Als het aantal observaties in elke groep even groot is, is de *MANOVA* redelijk robuust ten opzichte van een schending van deze assumptie en kan de *MANOVA* gewoon uitgevoerd worden. Als het aantal observaties echter niet gelijk is voor elke groep, zorgt een schending van deze assumptie wel voor problemen. In dat geval zijn er meerdere oplossingen nodig. Het aantal observaties kan per groep gelijkgetrokken worden door bepaalde observaties op willekeurige wijze te verwijderen. Het nadeel hiervan is dat minder observaties leidt tot een lager onderscheidend vermogen. Een andere optie is om in plaats van een *MANOVA* aparte *ANOVA's* uit te voeren voor elke afhankelijke variabele. Bij een *one-way MANOVA* kan dan voor de afhankelijke variabelen die niet voldoen aan de assumptie van homogeniteit van varianties apart een [Kruskal Wallis toets](10-Kruskal-Wallis-toets-I-R.html) uitgevoerd worden. Voor de *factoriële MANOVA* is het in dit geval een optie om voor de afhankelijke variabelen die niet voldoen aan de assumptie van homogeniteit van varianties apart de *ANOVA* uit te voeren als regressiemodel (zie hiervoor bijbehorende [toetspagina](29-Factoriele-ANOVA-R.html)).[^20]
# <!-- ## /TEKSTBLOK: Link2.R -->
# 
# ## Lineariteit
# 
# Bij de *MANOVA* wordt aangenomen dat er voor elke groep een lineaire relatie is tussen elk paar van afhankelijke variabelen. Een lineaire relatie houdt in dat de toename of afname van de ene variabele als gevolg van de toename van de andere variabele constant is: er is een rechte lijn door de data heen te trekken. Een voorbeeld van een lineaire en niet-lineaire relatie is weergegeven in Figuur 1. Bij de linkerfiguur kan er duidelijk een rechte lijn door de punten getrokken worden en is er dus sprake van een lineaire relatie. Bij de rechterfiguur is dit niet het geval, daar is er sprake van een curve in de relatie tussen de variabelen. Als er geen lineair verband is tussen de variabelen, dan is het onderscheidend vermogen van de *MANOVA* lager.[^20]<sup>,</sup>[^8]
# 
# De assumptie van lineariteit wordt onderzocht met behulp van scatter plots, zoals in onderstaande figuren. Maak per groep (op basis van de onafhankelijke variabele[n]) voor elk paar van afhankelijke variabelen een scatter plot en bekijk of er een lineaire relatie is. Als er geen lineaire relatie is, is het transformeren van de afwijkende variabele een optie. De variabele kan op verschillende manieren getransformeerd[^7] worden zodat er alsnog een lineaire relatie ontstaat. [^8]
# 
# <div class = "col-container">
#   <div class="col">
# <!-- ## CLOSEDBLOK: Lineariteit1.R -->

# In[ ]:


set.seed(12345)
x <- rnorm(100,0,2)
y <- 3 + 1.2 * x + rnorm(100,0,1)
dataset <- data.frame(Afhankelijke_variabele = y, Covariaat = x)

ggplot(dataset, aes(x = Covariaat, y = Afhankelijke_variabele)) +
    geom_point() + ylab("Variabele 2") + xlab("Variabele 1") +  
  ggtitle("Lineare relatie")


# <!-- ## /CLOSEDBLOK: Lineariteit1.R -->
#   </div>
#   <div class = "col">
# <!-- ## CLOSEDBLOK: Lineariteit2.R -->

# In[ ]:


set.seed(12345)
x <- rnorm(100,0,2)
y <- 3 + 1.2 * x^2 + rnorm(100,0,1)
dataset <- data.frame(Afhankelijke_variabele = y, Covariaat = x)

ggplot(dataset, aes(x = Covariaat, y = Afhankelijke_variabele)) +
    geom_point()  + ylab("Variabele 2") + xlab("Variabele 1") + 
  ggtitle("Niet-lineaire relatie")


# <!-- ## /CLOSEDBLOK: Lineariteit2.R -->
#   </div>
# </div>
# 
# *Figuur 1.  Voorbeeld van een lineaire (links) en niet-lineaire (rechts) relatie tussen twee variabelen.*
# 
# ## Multicollineariteit
# 
# Multicollineariteit houdt in dat er een hoge correlatie tussen twee of meerdere variabelen is. Er is perfecte multicollineariteit als één variabele een lineaire combinatie is van een of meerdere andere variabelen. In andere woorden, de variabele is precies te berekenen op basis van andere variabelen. In dat geval kan de *MANOVA* niet wiskundig bepaald worden en werkt de *MANOVA* niet. Dit komt zeer weinig voor en is vaak makkelijk op te lossen door goed naar de variabelen die het veroorzaken te kijken en een variabele te transformeren of te verwijderen.[^4]
# 
# Bij een hoog niveau van multicollineariteit kan de *MANOVA* wel uitgevoerd worden, is het onderscheidend vermogen[^3] lager. Daarnaast is het onlogisch om twee variabelen die sterk gecorreleerd zijn allebei aan de *MANOVA* toe te voegen, omdat de variabelen in feite hetzelfde meten. Multicollineariteit kan opgelost worden door een van de variabelen die het veroorzaakt te verwijderen. Een andere optie is een principale componenten analyse (PCA) uitvoeren op de afhankelijke variabelen zodat er een onderliggende variabele gecreëerd wordt (zie Field[^4] voor meer informatie).[^20]
# 
# Multicollineariteit wordt getoetst met de Variance Inflation Factor (VIF) die meet hoe sterk elke variabele gecorreleerd is met de andere variabelen. Als de VIF van een variabele hoger dan 10 is, is er multicollineariteit voor die variabele.[^4]<sup>,</sup>[^9] 
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^13] Bij de *MANOVA* is de interpretatie van verschillende effectmaten vrij complex.[^20] Daarom is het nuttiger om een effectmaat te gebruiken bij de tweede stap van de *MANOVA* waarin voor elke afhankelijke variabele een aparte *ANOVA* wordt uitgevoerd. De effectmaat voor de *ANOVA* is de *partial eta squared* (partial *η^2^*). Deze effectmaat berekent de proportie van de onverklaarde variantie (variantie die niet door de andere variabelen wordt verklaard) in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele.[^14] Als er meerdere onafhankelijke variabelen zijn, tellen de partial eta squareds van alle termen van het model dus niet per se op tot 1.[^14] Een indicatie om partial *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^15]
# 
# # Uitvoering
# 
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset ingeladen met daarin de gemiddelde cijfers voor periode 1, 2 en 3 en de bacheloropleiding en studentnummers van alle studenten van de master Bioinformatics. De dataset heet `Gemiddelde_cijfers_bioinformatics`. 
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 5 observaties
head(Gemiddelde_cijfers_bioinformatics)

## Laatste 5 observaties
tail(Gemiddelde_cijfers_bioinformatics)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 

# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# Inspecteer voor alle groepen het gemiddelde, de standaardafwijking, de mediaan en het aantal observaties voor de gemiddelde cijfers in periode 1, 2 en 3 om meer inzicht te krijgen. Gebruik hiervoor de functie `descr` en `stby` van het package `summarytools` om de beschrijvende statistieken per groep weer te geven. Voer de gewenste statistieken in met het argument `stats = c("mean","sd","med","n.valid")`.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-1.R -->

# In[ ]:


# Gemiddelde, standaardafwijking, mediaan en aantal observaties
library(summarytools)

with(Gemiddelde_cijfers_bioinformatics, 
     stby(data = cbind(Cijfers_P1, Cijfers_P2, Cijfers_P3), 
          list(Bacheloropleiding), 
          descr, 
          stats = c("mean", "sd", "med", "n.valid")))


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
# 
# Maak vervolgens een grafiek met de gemiddelden per bacheloropleiding voor de verschillende periodes. Maak hiervoor eerst een lange dataset met de functie `melt()` van het package `reshape`.

# In[ ]:


# Maak een lange dataset
library(reshape)

Gemiddelde_cijfers_bioinformatics_lang <- melt(Gemiddelde_cijfers_bioinformatics,
                                               id.vars = c("Studentnummer", 
                                                           "Bacheloropleiding"),
                                               measure.vars = c("Cijfers_P1", 
                                                                "Cijfers_P2", 
                                                                "Cijfers_P3"),
                                               variable_name = "Periode")

# Maak de grafiek
library(ggplot2)

ggplot(Gemiddelde_cijfers_bioinformatics_lang, 
       aes(x = Periode, y = value, group = Bacheloropleiding, colour = Bacheloropleiding)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Bacheloropleiding)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue", "darkgreen")) 


# *Figuur 2.  Gemiddelde cijfers voor periode 1, 2 en 3 voor studenten bioinformatics met als bacheloropleidingen Biologie, Informatica en Wiskunde.*

# Uit de beschrijvende statistieken en de visualisatie in Figuur 2 blijkt dat het gemiddelde cijfer in periode 1 en 2 voor de bacheloropleidingen Informatica en Wiskunde hoger ligt dan het gemiddelde cijfer voor de bacheloropleiding Biologie. In periode 3 is dit juist andersom.
# 
# # Toetsing assumpties
# 
# Gebruik de *MANOVA* om te onderzoeken of er een verschil is tussen de gemiddelde cijfers in periode 1, 2 en 3 voor studenten van de master Bioinformatics die afkomstig zijn van de vooropleidingen Wiskunde, Informatica en Biologie. Start met het toetsen van de assumpties en voer vervolgens de *ANCOVA* uit als hieraan voldaan is.
# 
# ## Outliers
# 
# ### Boxplots en standaardiseren
# 
# <!-- ## TEKSTBLOK: Outlier1.R -->
# Onderzoek of er univariate outliers zijn met behulp van boxplots en gestandaardiseerde scores voor de afhankelijke variabelen en tabellen voor onafhankelijke variabelen. Begin met de boxplot voor de variabelen `Cijfers_P1`, `Cijfers_P2` en `Cijfers_P3`.
# <!-- ## /TEKSTBLOK: Outlier1.R -->
# 
# <!-- ## OPENBLOK: Outlier2.R -->

# In[ ]:


# Maak een boxplot van de continue variabelen in de dataset
boxplot(Gemiddelde_cijfers_bioinformatics[,c("Cijfers_P1",
                                             "Cijfers_P2",
                                             "Cijfers_P3")])


# <!-- ## /OPENBLOK: Outlier2.R -->
# 
# Voor de drie variabelen zijn er geen onmogelijke scores en zijn er geen grote afwijkingen op basis van de boxplot. Onderzoek de gestandaardiseerde scores door een functie te schrijven die het aantal observaties per variabele telt met een gestandaardiseerde score hoger dan 3 of lager dan -3. Pas deze functie vervolgens toe op de drie afhankelijke variabelen in de dataset.
# 
# <!-- ## OPENBLOK: Outlier3.R -->

# In[ ]:


# Maak een functie om het aantal observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3 te tellen
Outlier_standaardiseren <- function(variabele){
  # Standaardiseer de variabele met de scale functie
  Z_score <- scale(variabele)
  # Tel het aantal observaties met een absolute score hoger dan 3
  Aantal_outliers <- sum(abs(Z_score) > 3)
  # Retourneer dit aantal
  return(Aantal_outliers)
}

# Tel voor de continue variabelen het aantal observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3
Outlier_standaardiseren(Gemiddelde_cijfers_bioinformatics$Cijfers_P1)
Outlier_standaardiseren(Gemiddelde_cijfers_bioinformatics$Cijfers_P2)
Outlier_standaardiseren(Gemiddelde_cijfers_bioinformatics$Cijfers_P3)


# <!-- ## /OPENBLOK: Outlier3.R -->
# 
# Er zijn bij de gemiddelde cijfers in periode 2 twee mogelijke outliers gevonden. Nu is het de vraag of deze gemiddelde cijfers in periode 2 onmogelijke of onwaarschijnlijke outliers zijn. In de boxplot is te zien dat het minimum van de observaties iets boven de vijf ligt en het maximum iets onder de negen. Voor een gemiddeld cijfer in een onderwijsperiode zijn dit geen ongeloofwaardige observaties, dus worden ze niet als outliers beschouwd. Daarom worden de observaties niet uit de dataset verwijderd.
# 
# Bacheloropleiding is de enige onafhankelijke variabele in deze dataset. Maak een tabel met de frequenties voor alle categoriëen van deze variabele om te onderzoeken of hier afwijkende waardes zijn.
# 
# <!-- ## OPENBLOK: Outlier4.R -->

# In[ ]:


table(Gemiddelde_cijfers_bioinformatics$Bacheloropleiding)


# <!-- ## /OPENBLOK: Outlier4.R -->
# 
# De categorieën van de variabele Opleiding zijn `Biologie`, `Informatica` en `Wiskunde`. Er zijn dus geen opmerkelijke waarden bij de variabele Bacheloropleiding.
# 
# ### Mahalanobis distance
# 
# <!-- ## TEKSTBLOK: Outlier7.R -->
# Onderzoek of er multivariate outliers zijn met behulp van de Mahalanobis distance met behulp van de functie `mahalanobis()`. De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van het gemiddelde van alle deelnemers voor alle afhankelijke variabele samen.
# 
# Neem een subset van de dataset met alleen de afhankelijke variabelen en gebruik deze voor de Mahalanobis afstand. Gebruik de functie `mahalanobis()` met als argumenten de dataset `Subset`, de gemiddeldes van elke kolom berekend met `colMeans(Subset)` en de covariantiematrix van de dataset berekend met `cov(Subset)`.
# 
# Bereken daarna de criteriumwaarde op basis van het gewenste significantieniveau en het aantal afhankelijke variabelen. Plot de Mahalanobis afstanden en tel het aantal deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde. Het gehanteerde significantieniveau is 0,001.
# <!-- ## /TEKSTBLOK: Outlier7.R -->
# 
# <!-- ## OPENBLOK: Outlier8.R -->

# In[ ]:


# Maak een subset van de dataset met alle afhankelijke variabelen
Subset <- Gemiddelde_cijfers_bioinformatics[,c("Cijfers_P1",
                                               "Cijfers_P2",
                                               "Cijfers_P3")]

# Bereken de Mahalanobis afstand voor elke deelnemer 
Mahalanobis_afstanden <- mahalanobis(Subset,
                                     colMeans(Subset),
                                     cov(Subset))

# Bepaal de criteriumwaarde voor de Mahalanobis afstand met de functie qchisq() met als eerste argument 1 - het significantieniveau en als tweede argument het aantal afhankelijke variabelen. In deze casus is het significantieniveau voor de Mahalanobis afstand 0.001 en het aantal afhankelijke variabelen berekend met ncol(Subset).
(Criteriumwaarde <- qchisq(1 - 0.001, ncol(Subset)))

# Plot de Mahalanobis afstanden
plot(Mahalanobis_afstanden, xlab = "Volgorde", ylab = "Mahalanobis afstanden")

# Tel het aantal Mahalanobis afstanden groter dan de criteriumwaarde
sum(Mahalanobis_afstanden > Criteriumwaarde)


# <!-- ## /OPENBLOK: Outlier8.R -->
# 
# <!-- ## TEKSTBLOK: Outlier9.R -->
# Er zijn geen deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde van `r Round_and_format(Criteriumwaarde)`, dus er lijken geen multivariate outliers te zijn op basis van de Mahalanobis afstand.
# <!-- ## /TEKSTBLOK: Outlier9.R -->
# 
# ## Aantal observaties per groep
# 
# Om de *MANOVA* uit te voeren, moeten er in elke groep meer observaties dan afhankelijke variabelen zijn. In de huidige casus zijn er drie afhankelijke variabelen en zijn er drie groepen op basis van de bacheloropleiding van de studenten van de master Bioinformatics. Maak een tabel met het aantal observaties per groep om de assumptie te onderzoeken.

# In[ ]:


table(Gemiddelde_cijfers_bioinformatics$Bacheloropleiding)


# Alle drie de groepen hebben meer dan 3 osbervaties, dus er is voldaan aan de assumptie van het aantal observaties per groep.
# 
# ## Multivariate normaliteit
# 
# De *MANOVA* vereist dat de verdeling van de afhankelijke variabele de normale verdeling benaderd in elke groep die gevormd wordt door de onafhankelijke variabelen. Onderzoek deze assumptie door per groep een histogram te maken van elke afhankelijke variabele.
# 
# ### Histogram
# 
# Visualiseer de verdelingen van de gemiddelde cijfers in periode 1, 2 en 3 binnen elke groep met behulp van een histogram[^24]. Focus bij het analyseren van een histogram op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke outliers. Een normale verdeling is symmetrisch, heeft één top en geen outliers.[^16]<sup>, </sup>[^17]
# 
# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


## Histogram met ggplot
ggplot(Gemiddelde_cijfers_bioinformatics,
  aes(x = Cijfers_P1)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 0.5,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Bacheloropleiding) +
  geom_density(alpha = .2, adjust = 1) +
  xlab("Gemiddeld cijfer periode 1") +
  ylab("Frequentiedichtheid")


# <!-- ## /OPENBLOK: AssLineariteit1.R -->

# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


## Histogram met ggplot
ggplot(Gemiddelde_cijfers_bioinformatics,
  aes(x = Cijfers_P2)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 0.5,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Bacheloropleiding) +
  geom_density(alpha = .2, adjust = 1) +
  xlab("Gemiddeld cijfer periode 2") +
  ylab("Frequentiedichtheid")


# <!-- ## /OPENBLOK: AssLineariteit1.R -->

# <!-- ## OPENBLOK: AssLineariteit2.R -->

# In[ ]:


## Histogram met ggplot
ggplot(Gemiddelde_cijfers_bioinformatics,
  aes(x = Cijfers_P3)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 0.5,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Bacheloropleiding) +
  geom_density(alpha = .2, adjust = 1) +
  xlab("Gemiddeld cijfer periode 3") +
  ylab("Frequentiedichtheid")


# <!-- ## /OPENBLOK: AssLineariteit2.R -->
# 
# *Figuur 3.  Histogrammen van de verdelingen van de gemiddelde cijfers in periode 1, 2 en 3 per bacheloropleiding.*
# 
# De verdelingen van alle combinaties van afhankelijke variabelen en groepen zijn te zien in Figuur 3. Voor alle combinaties van variabelen en groepen is de verdeling redelijk symmetrisch en eentoppig en zijn er geen outliers. De verdelingen zijn dus bij benadering normaal. Er is dus voldaan aan de assumptie van multivariate normaliteit.
# 
# Als er afwijkingen van de normaalverdeling zijn voor één of meerdere groepen, dan is de *MANOVA* nog steeds robuust als het aantal vrijheidsgraden van de residuën groter is dan 20. Dit aantal is te vinden door de *MANOVA* uit te voeren en dit aantal vrijheidsgraden te bekijken. Maak eerst een matrix met daarin de drie afhankelijke variabelen `Gemiddelde_cijfers_bioinformatics$Cijfers_P1`, `Gemiddelde_cijfers_bioinformatics$Cijfers_P2` en `Gemiddelde_cijfers_bioinformatics$Cijfers_P3`. Voer daarna de *MANOVA* uit met de functie `manova()` met als eerste argument de formule `Afhankelijke_variabelen ~ Bacheloropleiding` met links van de tilde de matrix met afhankelijke variabelen `Afhankelijke_variabelen` en rechts van de tilde de onafhankelijke variabele `Bacheloropleiding` en als tweede argument de dataset `data = Gemiddelde_cijfers_bioinformatics` en sla het resultaat op in het object `MANOVA`. Bereken ten slotte het aantal vrijheidsgraden van de residuën met `MANOVA$df.residual`

# In[ ]:


# Bind de afhankelijke variabelen in een matrix
Afhankelijke_variabelen <- cbind(Gemiddelde_cijfers_bioinformatics$Cijfers_P1,
                                 Gemiddelde_cijfers_bioinformatics$Cijfers_P2,
                                 Gemiddelde_cijfers_bioinformatics$Cijfers_P3)

# Voer de MANOVA uit
MANOVA <- manova(Afhankelijke_variabelen ~ Bacheloropleiding, 
                 data = Gemiddelde_cijfers_bioinformatics)

# Bereken de vrijheidsgraden van de residuën
MANOVA$df.residual


# Het aantal vrijheidsgraden van de residuën is `r MANOVA$df.residual` wat ruim meer is dan 20. Mocht er dus geen multivariate normaliteit zijn op basis van de histogrammen, dan is de *MANOVA* alsnog robuust ten opzichte van een schending van deze assumptie.
# 
# ## Homogeniteit van variantie-covariantie matrices
# 
# <!-- ## TEKSTBLOK: LeveneTest1.R -->
# Toets met *Box's M test* de assumptie homogeniteit van variantie-covariantie matrices. Gebruik hiervoor de functie `box_m` van het package `rstatix` met als argumenten de afhankelijke variabelen `Gemiddelde_cijfers_bioinformatics[,c("Cijfers_P1", "Cijfers_P2", "Cijfers_P3")]` en de onafhankelijke variabelen `Gemiddelde_cijfers_bioinformatics[,"Bacheloropleiding"]`.
# <!-- ## /TEKSTBLOK: LeveneTest1.R -->
# 
# <!-- ## OPENBLOK: Levenes-test.R -->

# In[ ]:


library(rstatix)

box_m(Gemiddelde_cijfers_bioinformatics[,c("Cijfers_P1",
                                           "Cijfers_P2",
                                           "Cijfers_P3")],
      Gemiddelde_cijfers_bioinformatics[,"Bacheloropleiding"])


# <!-- ## /OPENBLOK: Levenes-test.R -->
# 
# <!-- ## CLOSEDBLOK: Levenes-test.R -->

# In[ ]:


library(rstatix)

Box <- box_m(Gemiddelde_cijfers_bioinformatics[,c("Cijfers_P1",
                                                  "Cijfers_P2",
                                                  "Cijfers_P3")],
             Gemiddelde_cijfers_bioinformatics[,"Bacheloropleiding"])

vF_waarde <- Round_and_format(Box$statistic)
vF_p <- Round_and_format(Box$p.value)


# <!-- ## /CLOSEDBLOK: Levenes-test.R -->
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# * *F* = `r vF_waarde`, p-waarde = `r vF_p`, 
# * De p-waarde is groter dan 0,01, dus er is geen significant verschil gevonden tussen de groepen wat betreft de variantie-covariantie matrices. Er is dus aan de assumptie van homogeniteit van varianties voldaan.
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# 
# ## Lineariteit
# 
# Onderzoek of er voor elke bacheloropleiding een lineaire relatie is tussen elk paar van afhankelijke variabelen.
# 
# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


ggplot(Gemiddelde_cijfers_bioinformatics, aes(x = Cijfers_P1, y = Cijfers_P2)) +
    geom_point() + ylab("Cijfers Periode 2") + xlab("Cijfers Periode 1") + 
  facet_wrap(~ Bacheloropleiding)


# <!-- ## /OPENBLOK: AssLineariteit1.R -->
#   </div>
#   <div class="col">
# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


ggplot(Gemiddelde_cijfers_bioinformatics, aes(x = Cijfers_P1, y = Cijfers_P3)) +
    geom_point() + ylab("Cijfers Periode 3") + xlab("Cijfers Periode 1") + 
  facet_wrap(~ Bacheloropleiding)


# <!-- ## /OPENBLOK: AssLineariteit1.R -->
# 
# <!-- ## OPENBLOK: AssLineariteit2.R -->

# In[ ]:


ggplot(Gemiddelde_cijfers_bioinformatics, aes(x = Cijfers_P2, y = Cijfers_P3)) +
    geom_point() + ylab("Cijfers Periode 3") + xlab("Cijfers Periode 2") + 
  facet_wrap(~ Bacheloropleiding)


# <!-- ## /OPENBLOK: AssLineariteit2.R -->
# 
# *Figuur 4. Scatter plots van de relatie tussen elk paar van afhankelijke variabelen voor de bacheloropleidingen Biologie, Informatica en Wiskunde.*
# 
# Op basis van de scatter plots in Figuur 4 lijken er voor elke groep lineaire relaties te zijn tussen alle paren van afhankelijke variabelen. Er is dus aan de assumptie van lineariteit voldaan.
# 
# ## Multicollineariteit
# 
# <!-- ## TEKSTBLOK: AssMulticollineariteit1.R -->
# Onderzoek of er sprake is van multicollineariteit bij de afhankelijke variabelen met behulp van Variance Inflation Factors (VIFs). Bereken de VIFs voor elke afhankelijke variabele met de functie `VIF()` van het package `DescTools` waarbij de functie als argument `Multicollineariteit` heeft. Voer hiervoor eerst een regressiemodel waarbij de drie afhankelijke variabelen de predictors zijn. Dit is nodig omdat de functie `VIF()` de VIF berekend voor predictors van een regressiemodel. Voer het regressiemodel uit met de functie `lm()` met als eerste argument de vergelijking `log(Cijfers_P1*Cijfers_P3) ~ Cijfers_P1 + Cijfers_P2 + Cijfers_P3` met links van het tilde de zelfverzonnen afhankelijke variabele `log(Cijfers_P1*Cijfers_P3)` en rechts de predictors `Cijfers_P1`, `Cijfers_P2` en `Cijfers_P3`. Het tweede argument is de dataset `Gemiddelde_cijfers_bioinformatics`. De afhankelijke variabele is hier zelfverzonnen omdat de VIF niet afhankelijk is van deze variabele. De afhankelijke variabele kan dus ook op een andere manier gemaakt worden.
# <!-- ## /TEKSTBLOK: AssMulticollineariteit1.R -->

# <!-- ## OPENBLOK: AssMulticollineariteit2.R -->

# In[ ]:


library(DescTools)

# Maak een regressiemodel met de lm() functie met de afhankelijke variabelen als predictor
Multicollineariteit <- lm(log(Cijfers_P1*Cijfers_P3) ~ Cijfers_P1 + Cijfers_P2 + Cijfers_P3,
                           Gemiddelde_cijfers_bioinformatics)

# Bereken de VIF voor de predictors Cijfers_P1, Cijfers_P2 en Cijfers_P3
VIF(Multicollineariteit)


# <!-- ## /OPENBLOK: AssMulticollineariteit2.R -->
# 
# Geen enkele van de VIFs is hoger dan 10, dus er is voldaan aan de assumptie van multicollineariteit.
# 
# # MANOVA
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Voer de *MANOVA* uit om te onderzoeken of er verschillen zijn tussen studenten afkomstig van de bacheloropleidingen Biologie, Informatica en Wiskunde wat betreft hun gemiddelde cijfers in periode 1, 2 en 3 voor de master Bioinformatics. Maak eerst een matrix met daarin de drie afhankelijke variabelen `Gemiddelde_cijfers_bioinformatics$Cijfers_P1`, `Gemiddelde_cijfers_bioinformatics$Cijfers_P2` en `Gemiddelde_cijfers_bioinformatics$Cijfers_P3`. Voer daarna de *MANOVA* uit met de functie `manova()` met als eerste argument de formule `Afhankelijke_variabelen ~ Bacheloropleiding` met links van de tilde de matrix met afhankelijke variabelen `Afhankelijke_variabelen` en rechts van de tilde de onafhankelijke variabele `Bacheloropleiding` en als tweede argument de dataset `data = Gemiddelde_cijfers_bioinformatics` en sla het resultaat op in het object `MANOVA`. Geef vervolgens de resultaten weer met de toetsstatistiek *Wilks's Lambda* met behulp van de functie `summary.manova()` met als argumenten het MANOVA object `MANOVA` en `test = "Wilks"` om aan te geven dat *Wilks's Lambda* gebruikt moet worden.
# 
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


# Sla de afhankelijke variabelen op in een matrix
Afhankelijke_variabelen <- cbind(Gemiddelde_cijfers_bioinformatics$Cijfers_P1,
                                 Gemiddelde_cijfers_bioinformatics$Cijfers_P2,
                                 Gemiddelde_cijfers_bioinformatics$Cijfers_P3)

# Voer de MANOVA uit
MANOVA <- manova(Afhankelijke_variabelen ~ Bacheloropleiding, 
                 data = Gemiddelde_cijfers_bioinformatics)

# Laat de resultaten zien voor de toetsstatistiek Wilks's Lambda
summary.manova(MANOVA, test = "Wilks")


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# <!-- ## CLOSEDBLOK: Uitvoering3.R -->

# In[ ]:


# Sla de afhankelijke variabelen op in een matrix
Afhankelijke_variabelen <- cbind(Gemiddelde_cijfers_bioinformatics$Cijfers_P1,
                                 Gemiddelde_cijfers_bioinformatics$Cijfers_P2,
                                 Gemiddelde_cijfers_bioinformatics$Cijfers_P3)

# Voer de MANOVA uit
MANOVA <- manova(Afhankelijke_variabelen ~ Bacheloropleiding, 
                 data = Gemiddelde_cijfers_bioinformatics)

# Laat de resultaten zien voor de toetsstatistiek Wilks's Lambda
Res_MANOVA <- summary.manova(MANOVA, test = "Wilks")$stats


vWilks <- Round_and_format(Res_MANOVA[1, 2])
vF <- Round_and_format(Res_MANOVA[1, 3])
vDF1 <- Round_and_format(Res_MANOVA[1, 4])
vDF2 <- Round_and_format(Res_MANOVA[1, 5])


# <!-- ## /CLOSEDBLOK: Uitvoering3.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets2.R -->
# 
# * Er is een significant effect van de variabele Bacheloropleiding op een lineaire combinatie van de afhankelijke variabelen Cijfers_P1, Cijfers P2 en Cijfers_P3 (*&Lambda;* = `r vWilks`, *F* (`r vDF1`,`r vDF2`) = `r vF`, *p* < 0,0001)
# * De p-waarde is kleiner dan 0,05, dus de nulhypothese dat er geen interactie-effect is wordt verworpen.[^18] 
# * Omdat de *MANOVA* een significant resultaat laat zien, kan er voor elke afhankelijke variabele apart een *ANOVA* uitgevoerd worden
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets2.R -->

# # ANOVA's voor elke afhankelijke variabele
# 
# <!-- ## TEKSTBLOK: ANOVA-toets2_1.R -->
# Voer voor de afhankelijke variabelen Cijfers_P1, Cijfers_P2 en Cijfers_P3 apart een *ANOVA* uit. Om de *ANOVA* uit te voeren, moeten eerst de assumptie van normaliteit en homogeniteit van varianties getoetst worden, voor meer informatie zie de toetspagina's van de [one-way ANOVA](05-One-way-ANOVA-R.html) en de [factoriële ANOVA](29-Factoriele-ANOVA-R.html). De assumptie van normaliteit is al getoetst voordat de *MANOVA* is uitgevoerd. Hieruit bleek dat de verdeling voor elke groep voor elke afhankelijke variabele de normaalverdeling benaderd, dus er is ook voor de *ANOVA* aan deze assumptie voldaan. De assumptie van homogeniteit van varianties moet wel getoetst worden, omdat bij de *MANOVA* de homogeniteit van variantie-covariantie matrices getoetst wordt.
# 
# Toets de assumptie van homogeniteit van varianties met de *Levene's test*. Gebruik hiervoor de functie `leveneTest()` van het package `car` met als eerste argument de vergelijking `Cijfers_P1 ~ Bacheloropleiding` met links van de tilde de afhankelijke variabele `Cijfers_P1` (of `Cijfers_P2` of `Cijfers_P3`) en rechts van de tilde de onafhankelijke variabele `Bacheloropleiding` en als tweede argument de dataset `Gemiddelde_cijfers_bioinformatics`.
# <!-- ## /TEKSTBLOK: ANOVA-toets2_1.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets2_2.R -->

# In[ ]:


library(car)

leveneTest(Cijfers_P1 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)
leveneTest(Cijfers_P2 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)
leveneTest(Cijfers_P3 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)


# <!-- ## /OPENBLOK: ANOVA-toets2_2.R -->

# Voor alle drie de afhankelijke variabelen is de *Levene's test* niet significant, dus alle variabelen voldoen aan de assumptie van homogeniteit van varianties. De *ANOVA's* kunnen uitgevoerd worden.
# 
# <!-- ## TEKSTBLOK: ANOVA-toets2_3.R -->
# Gebruik hiervoor de functie `aov()` met als eerste argument de vergelijking `Cijfers_P1 ~ Bacheloropleiding` met links van de tilde de afhankelijke variabele `Cijfers_P1` (of `Cijfers_P2` of `Cijfers_P3`) en rechts van de tilde de onafhankelijke variabele `Bacheloropleiding` en als tweede argument de dataset `Gemiddelde_cijfers_bioinformatics` en sla het resultaat op. Om te corrigeren voor het feit dat er drie toetsen tegelijkertijd uitgevoerd worden, wordt een Bonferroni correctie uitgevoerd door het significantieniveau van 0,05 door het aantal toetsen (drie) te delen. Dit levert een nieuw significantieniveau van 0,017 (0,05 / 3 = 0,017) op. Waar normaliter de p-waarde van de *ANOVA* met het significantieniveau 0,05 vergeleken wordt, wordt de p-waarde nu met het significantieniveau 0,017 vergeleken. Laat vervolgens de resultaten zien met de functie `summary()` met als argument het ANOVA object. Bereken daarna de effectmaat *partial eta squared* met de functie `EtaSq()` van het package `DescTools` als argument het ANOVA object.
# <!-- ## /TEKSTBLOK: ANOVA-toets2_3.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets3.R -->

# In[ ]:


library(DescTools)

# Voer de ANOVA's uit
ANOVA_P1 <- aov(Cijfers_P1 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)
ANOVA_P2 <- aov(Cijfers_P2 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)
ANOVA_P3 <- aov(Cijfers_P3 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)

# Laat de resultaten zien
summary(ANOVA_P1)
summary(ANOVA_P2)
summary(ANOVA_P3)

# Bereken de effectmaat
EtaSq(ANOVA_P1)
EtaSq(ANOVA_P2)
EtaSq(ANOVA_P3)


# <!-- ## /OPENBLOK: ANOVA-toets3.R -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets4.R -->

# In[ ]:


library(DescTools)

ANOVA_P1 <- aov(Cijfers_P1 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)
ANOVA_P2 <- aov(Cijfers_P2 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)
ANOVA_P3 <- aov(Cijfers_P3 ~ Bacheloropleiding, Gemiddelde_cijfers_bioinformatics)

Res_P1 <- summary(ANOVA_P1)[[1]]
Res_P2 <- summary(ANOVA_P2)[[1]]
Res_P3 <- summary(ANOVA_P3)[[1]]

Eta_P1 <- Round_and_format(EtaSq(ANOVA_P1)[1,2])
Eta_P2 <- Round_and_format(EtaSq(ANOVA_P2)[1,2])
Eta_P3 <- Round_and_format(EtaSq(ANOVA_P3)[1,2])

F_P1 <- Round_and_format(Res_P1$`F value`[1])
F_P2 <- Round_and_format(Res_P2$`F value`[1])
F_P3 <- Round_and_format(Res_P3$`F value`[1])

DF1_P1 <- Res_P1$Df[1]
DF1_P2 <- Res_P2$Df[1]
DF1_P3 <- Res_P3$Df[1]

DF2_P1 <- Res_P1$Df[2]
DF2_P2 <- Res_P2$Df[2]
DF2_P3 <- Res_P3$Df[2]


# <!-- ## /CLOSEDBLOK: ANOVA-toets4.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets5.R -->
# * Er is een significant verschil tussen de bacheloropleidingen wat betreft het gemiddelde cijfer in periode 1, *F* (`r DF1_P1`,`r DF2_P1`) = `r F_P1`, *p* < 0,0001, *η^2^* = `r Eta_P1`
# * Er is een significant verschil tussen de bacheloropleidingen wat betreft het gemiddelde cijfer in periode 2, *F* (`r DF1_P2`,`r DF2_P2`) = `r F_P2`, *p* < 0,0001, *η^2^* = `r Eta_P2`
# * Er is een significant verschil tussen de bacheloropleidingen wat betreft het gemiddelde cijfer in periode 3, *F* (`r DF1_P3`,`r DF2_P3`) = `r F_P3`, *p* < 0,0001, *η^2^* = `r Eta_P3`
# * Voor alle drie de perioden is er een significant verschil tussen de gemiddelde cijfers van de drie bacheloropleidingen. Er kunnen voor iedere periode dus post-hoc toetsen uitgevoerd worden
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets5.R -->
# 
# # Post-hoc toetsen
# 
# <!-- ## TEKSTBLOK: PHtest1.R -->
# Voer post-hoc toetsen uit om te onderzoeken welke bacheloropleidingen van elkaar verschillen voor de gemiddelde cijfers in periode 1, 2 en 3. Gebruik hiervoor de functie `TukeyHSD()` met als argument het ANOVA-object van bijvoorbeeld periode 1 `ANOVA_P1`.
# <!-- ## /TEKSTBLOK: PHtest1.R -->
# 
# <!-- ## OPENBLOK: PHtest2.R -->

# In[ ]:


TukeyHSD(ANOVA_P1)
TukeyHSD(ANOVA_P2)
TukeyHSD(ANOVA_P3)


# <!-- ## /OPENBLOK: PHtest2.R -->
# 
# <!-- ## CLOSEDBLOK: PHtest3.R -->

# In[ ]:


PH_P1 <- TukeyHSD(ANOVA_P1)[[1]]
PH_P2 <- as.data.frame(TukeyHSD(ANOVA_P2)[[1]])
PH_P3 <- as.data.frame(TukeyHSD(ANOVA_P3)[[1]])


# <!-- ## /CLOSEDBLOK: PHtest3.R -->
# 
# <!-- ## TEKSTBLOK: PHtest4.R -->
# De resultaten van de post-hoc toetsen voor de gemiddelde cijfers van periode 1 zijn[^18]:
# 
# * Informatica versus Biologie: het verschil in gemiddelde (Informatica - Biologie) is `r Round_and_format(PH_P1[1,1])`, dit is een significant verschil (*p* < 0,0001).
# * Wiskunde versus Biologie: het verschil in gemiddelde (Wiskunde - Biologie) is `r Round_and_format(PH_P1[2,1])`, dit is een significant verschil (*p* < 0,0001).
# * Wiskunde versus Informatica: het verschil in gemiddelde (Wiskunde - Informatica) is `r Round_and_format(PH_P1[3,1])`, dit is geen significant verschil (*p* = `r Round_and_format(PH_P1[3,4])`).
# 
# De resultaten van de post-hoc toetsen voor de gemiddelde cijfers van periode 2 zijn:
# 
# * Informatica versus Biologie: het verschil in gemiddelde (Informatica - Biologie) is `r Round_and_format(PH_P2[1,1])`, dit is een significant verschil (*p* < 0,0001).
# * Wiskunde versus Biologie: het verschil in gemiddelde (Wiskunde - Biologie) is `r Round_and_format(PH_P2[2,1])`, dit is een significant verschil (*p* < 0,0001).
# * Wiskunde versus Informatica: het verschil in gemiddelde (Wiskunde - Informatica) is `r Round_and_format(PH_P2[3,1])`, dit is geen significant verschil (*p* = `r Round_and_format(PH_P2[3,4])`).
# 
# De resultaten van de post-hoc toetsen voor de gemiddelde cijfers van periode 3 zijn:
# 
# * Informatica versus Biologie: het verschil in gemiddelde (Informatica - Biologie) is `r Round_and_format(PH_P3[1,1])`, dit is een significant verschil (*p* < 0,0001).
# * Wiskunde versus Biologie: het verschil in gemiddelde (Wiskunde - Biologie) is `r Round_and_format(PH_P3[2,1])`, dit is een significant verschil (*p* < 0,0001).
# * Wiskunde versus Informatica: het verschil in gemiddelde (Wiskunde - Informatica) is `r Round_and_format(PH_P3[3,1])`, dit is geen significant verschil (*p* = `r Round_and_format(PH_P3[3,4])`).
# 
# <!-- ## /TEKSTBLOK: PHtest4.R -->
# 
# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.R -->
# DE *MANOVA* is uitgevoerd om te onderzoeken of er verschillen zijn in de gemiddelde cijfers van masterstudenten Bioinformatics voor periode 1, 2 en 3 tussen studenten afkomstig van de bacheloropleidingen Biologie, Informatica en Wiskunde. Uit de resultaten van de *MANOVA* blijkt er een significant verschil te zijn tussen de drie bacheloropleidingen voor de gemiddelde cijfers voor minimaal één van de onderwijsperiodes, *&Lambda;* = `r vWilks`, *F* (`r vDF1`,`r vDF2`) = `r vF`, *p* < 0,0001.
# 
# Vervolgens zijn er voor elke onderwijsperiode *ANOVA's* uitgevoerd om te toetsen of de gemiddelden verschillen per bacheloropleiding. Er is een Bonferroni-correctie gebruikt omdat er drie afhankelijke variabelen tegelijkertijd getoetst worden. Er is een significant verschil tussen de bacheloropleidingen wat betreft het gemiddelde cijfer in periode 1 (*F* (`r DF1_P1`,`r DF2_P1`) = `r F_P1`, *p* < 0,0001, *η^2^* = `r Eta_P1`), periode 2 (*F* (`r DF1_P2`,`r DF2_P2`) = `r F_P2`, *p* < 0,0001, *η^2^* = `r Eta_P2`) en periode 3 (*F* (`r DF1_P3`,`r DF2_P3`) = `r F_P3`, *p* < 0,0001, *η^2^* = `r Eta_P3`). De post-hoc toetsen laten zien dat er voor alle drie de perioden geen significante verschillen zijn tussen de bacheloropleidingen Wiskunde en Informatica, maar wel significante verschillen tussen Wiskunde en Biologie en Informatica en Biologie. Uit de resultaten van de post-hoc toetsen en Figuur 5 is af te leiden dat de studenten van de bacheloropleidingen Wiskunde en Informatica een hoger gemiddeld cijfer behalen in periode 1 en 2 en dat studenten van de bacheloropleiding Biologie een hoger gemiddeld cijfer behalen in periode 3. Het lijkt er dus op dat het per periode verschilt welke bacheloropleiding studenten het beste voorbereid op de master.
# 
# <!-- ## /TEKSTBLOK: Rapportage.R -->

# <!-- ## CLOSEDBLOK: Rapportage1.R -->

# In[ ]:


library(reshape)

Gemiddelde_cijfers_bioinformatics_lang <- melt(Gemiddelde_cijfers_bioinformatics,
                                               id.vars = c("Studentnummer", 
                                                           "Bacheloropleiding"),
                                               measure.vars = c("Cijfers_P1", 
                                                                "Cijfers_P2", 
                                                                "Cijfers_P3"),
                                               variable_name = "Periode")

library(ggplot2)

ggplot(Gemiddelde_cijfers_bioinformatics_lang, 
       aes(x = Periode, y = value, group = Bacheloropleiding, colour = Bacheloropleiding)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Bacheloropleiding)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue","darkgreen")) 


# <!-- ## /CLOSEDBLOK: Rapportage1.R -->
# 
# *Figuur 5.  Gemiddelde cijfers voor periode 1, 2 en 3 voor studenten bioinformatics met als bacheloropleidingen Biologie, Informatica en Wiskunde.*
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *One-way MANOVA in SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/one-way-manova-using-spss-statistics.php
# [^2]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.  
# [^3]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 86.
# [^4]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 293-356.
# [^5]: Universiteit van Amsterdam (13 augustus 2016). *Outliers*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).  
# [^6]: Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$.
# [^7]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^8]: Universiteit van Amsterdam (7 juli 2014). *Lineariteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Lineariteit).
# [^9]: Stat 501. *12.4 - Detecting Multicollinearity Using Variance Inflation Factors*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat501/lesson/12/12.4).
# [^10]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. 
# Sage. Pagina 507-542.
# [^13]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^14]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 54 - 55.
# [^15]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited. Pagina 84.
# [^16]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^17]: Outliers kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de outliers valide outliers zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van outliers kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde outliers te melden in een rapport. 
# [^18]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^20]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 285 - 354.
# [^21]: Wikipedia (2020). [Multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)
# [^22]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 623-664.
# [^23]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 72 - 77.
# [^24]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
