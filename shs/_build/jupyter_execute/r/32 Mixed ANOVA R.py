#!/usr/bin/env python
# coding: utf-8
---
title: "Mixed ANOVA"
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


source(paste0(here::here(),"/01. Includes/data/32.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik de *mixed ANOVA* om te toetsen of de gemiddelden van groepen op basis van twee of meer onafhankelijke categorische variabelen van elkaar verschillen waarbij er zowel between-subjects als within-subjects variabelen zijn.[^1] 

# # Onderwijscasus
# <div id = "casus">
# 
# De masteropleiding Sustainable Change Management is een experiment gestart waarbij studenten die niet direct toelaatbaar zijn voor de opleiding een premasterprogramma van een half jaar kunnen volgen om alsnog toegelaten te worden. Om dit experiment te evalueren wil de opleidingsdirecteur onderzoeken of 
# er verschillen zijn tussen de resultaten van premasterstudenten en direct toelaatbare studenten. Daarom vraagt hij te onderzoeken of er verschillen zijn tussen de toelaatbare en premasterstudenten voor de kernvakken Sustainable Innovation, Organizational Change Management en Organizational Psychology en de masterthesis. Op basis van deze analyse kan de opleidingsdirecteur zien of het premasterprogramma goed aansluit bij het masterprogramma en waar eventuele tekortkomingen zitten.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is. Bij *mixed ANOVA* zijn er hypotheses op te stellen voor de verschillen tussen groepen van elke onafhankelijke variabele apart (hoofdeffecten) en een hypothese voor de interactie tussen twee of meerdere onafhankelijke variabelen (interactie-effect).
# 
# *H~0~*: Het gemiddelde cijfer is gelijk voor direct toelaatbare studenten en premasterstudenten, i.e. er is geen hoofdeffect van Premaster op Cijfer.
# 
# *H~A~*: Het gemiddelde cijfer is niet gelijk voor direct toelaatbare studenten en premasterstudenten, i.e. er is geen hoofdeffect van Premaster op Cijfer.
# 
# *H~0~*: Het gemiddelde cijfer is gelijk voor de vakken Sustainable Innovation, Organizational Change Management en Organizational Psychology en de masterthes, i.e. er is een hoofdeffect van Vak op Cijfer.
# 
# *H~A~*: Het gemiddelde cijfer is niet gelijk voor de vakken Sustainable Innovation, Organizational Change Management en Organizational Psychology en de masterthes, i.e. er is een hoofdeffect van Vak op Cijfer.
# 
# *H~0~*: Er is geen interactie-effect tussen de variabelen Vak en Premaster op het gemiddeld cijfer.
# 
# *H~A~*: Er is een interactie-effect tussen de variabelen Vak en Premaster op het gemiddeld cijfer.
# 
# </div>
# 
# # Within en between-subjects variabelen
# 
# Binnen de *ANOVA* familie zijn er verschillende soorten analyses die afhangen van het type onafhankelijke variabele dat wordt gebruikt. Een onafhankelijke variabele kan een between-subjects en within-subjects variabele zijn. Between-subjects houdt in dat elke categorie van de variabele andere deelnemers[^19] bevat; elke deelnemer zit slechts in één van de categoriëen. Een voorbeeld van een between-subjects variabele is Geslacht: de deelnemer zit in de categorie man of categorie vrouw en kan niet in beide zitten. Een within-subjects variabele kan op twee manieren ontworpen worden. De eerste manier is dat elke deelnemer in elke categorie zit doordat hij of zij in elke categorie gemeten is (herhaalde metingen). Een voorbeeld hiervan is de variabele onderwijsperiode: de deelnemer wordt in elke onderwijsperiode gemeten wat betreft zijn gemiddelde cijfer. De tweede manier is dat deelnemers in elke categorie aan elkaar gematcht worden. Dit betekent dat er op basis van achtergrondkenmerken deelnemers aan elkaar gekoppeld worden die erg op elkaar lijken. Een herhaalde meting wordt op deze manier als het ware nagebootst. Een voorbeeld hiervan is het matchen van studenten bij verschillende opleidingen op basis van kenmerken als geslacht, leeftijd, vooropleiding en gemiddeld eindexamencijfer middelbare school.
# 
# Het soort onafhankelijke variabelen bepaalt het type *ANOVA* dat gebruikt moet worden. Bij één between-subjects variabele is de [one-way ANOVA](05-One-way-ANOVA-R.html) de juiste toets en bij één within-subjects variabele is de [repeated measures ANOVA](04-Repeated-measures-ANOVA-R.html) de juiste toets. Bij meerdere variabelen wordt het iets complexer. Als alle variabelen between-subjects variabelen zijn is de [factoriële ANOVA](29-Factoriele-ANOVA-R.html) de juiste toets. Als alle variabelen within-subjects variabelen zijn, is de [factoriële repeated measures ANOVA](30-Factoriele-repeated-measures-ANOVA-R.html) de juiste toets. Als er een combinatie is van within-subjects en between-subjects variabelen, dan is de *mixed ANOVA* (de huidige toetspagina) de juiste toets. Bekijk dus van tevoren wat voor soort onafhankelijke variabelen worden gebruikt om de juiste toets te bepalen.
# 
# # Hoofdeffecten en interacties
# 
# Bij *mixed ANOVA* wordt onderzocht of er verschillen zijn tussen groepen die gemaakt worden op basis van meerdere categorische onafhankelijke variabelen die between-subjects en within-subjects zijn. Dit wordt toegelicht met een versimpelde vorm van de huidige casus met twee onafhankelijke variabelen Vak en Premaster en een afhankelijke variabele Cijfer. De onafhankelijke variabele Vak bestaat uit twee groepen (theorie en praktijk) en de onafhankelijke variabele Periode bestaat ook uit twee groepen (A en B). Binnen *mixed ANOVA* wordt een onderscheid gemaakt tussen hoofdeffecten en interactie-effecten. Een hoofdeffect houdt in dat er een verschil is tussen de groepen van één van de onafhankelijke variabelen. In andere woorden, de onafhankelijke variabele heeft effect op de afhankelijke variabele. Voor het bedachte experiment houdt een hoofdeffect van de variabele Vak in dat er een verschil is in het gemiddelde van vak A en vak B. Een hoofdeffect van de variabele Premaster houdt in dat er een verschil is in het gemiddelde van de groep Premaster en de groep Geen Premaster.[^10]
# 
# Een grafische weergave van hoofdeffecten is te zien in Figuur 1. In de figuur is de relatie tussen de variabelen Premaster en Cijfer weergegeven voor de vakken A en B. Het hoofdeffect van de variabele Premaster is te zien door het gemiddelde van de groep Premaster te vergelijken met het gemiddelde van de groep Geen Premaster. Beide gemiddelden zijn weergegeven met groene driehoeken: de groep Premaster heeft een gemiddelde van 6 en de groep Geen Premaster een gemiddelde van 8. Er is dus een verschil in gemiddelde tussen de groepen van onafhankelijke variabele Premaster, wat betekent dat er een hoofdeffect van de variabele Premaster is. Op dezelfde manier kan een mogelijk hoofdeffect van de variabele Vak onderzocht worden. Het gemiddelde van vak A is weergegeven met een oranje vierkant en het gemiddelde van vak B met een blauw vierkant. Het gemiddelde van vak A (8) ligt hoger dan het gemiddelde van vak B (6), dus er is ook een hoofdeffect van onafhankelijke variabele Vak. Beide onafhankelijke variabelen hebben dus een effect op de afhankelijke variabele Cijfer.
# 
# <!-- ## CLOSEDBLOK: Uitleg1.R -->

# In[ ]:


Premaster <- c(1,3,1,3)
Vak <- c("A", "A","B", "B")
Cijfer <- c(5,7,7,9)
dat <- cbind.data.frame(Premaster,Vak,Cijfer)
ggplot(dat, aes(x = Premaster, y = Cijfer, group = Vak, colour = Vak)) + geom_line() + geom_point(size = 2) + scale_color_manual(values = c("darkorange","deepskyblue")) + scale_x_continuous(breaks = c(1,3), labels = c("Premaster", "Geen Premaster")) + annotate("point", x = 2, y = 8, colour = "deepskyblue", fill = "deepskyblue", shape = 22, size = 3) + annotate("point", x = 2, y = 6, colour = "darkorange", fill = "darkorange", shape = 22, size = 3) + annotate("point", x = 1, y = 6, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) + annotate("point", x = 3, y = 8, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) 


# <!-- ## /CLOSEDBLOK: Uitleg1.R -->
# 
# *Figuur 1.  Illustratie van hoofdeffecten bij mixed ANOVA voor een casus met afhankelijke variabele Cijfer en onafhankelijke variabelen Vak en Premaster. In deze grafiek zijn er hoofdeffecten voor de variabelen Vak en Premaster., maar geen interactie-effecten.*
# 
# Een interactie-effect houdt in dat het effect van de ene onafhankelijke variabele op de afhankelijke variabele afhangt van de andere onafhankelijke variabele(n). Er is als het ware een interactie tussen de onafhankelijke variabelen die het effect op de afhankelijke variabele bepaalt. In het bedachte experiment zou dit betekenen dat het effect van onafhankelijke variabele Premaster op Cijfer verschillend is voor vak A en vak B. Een voorbeeld van dit interactie-effect is te zien in Figuur 2. In deze figuur is zichtbaar dat er bij vak A geen verschil is tussen de groepen Premaster en Geen Premaster wat betreft het cijfer, maar dat er voor vak B wel een verschil is. Bij vak B is er voor de groep Geen Premaster een hoger gemiddeld cijfer (9) dan voor de groep Premaster (7). Het effect van de onafhankelijke variabele Premaster op Cijfer hangt af van de variabele Vak, dus er is een interactie-effect van de variabelen Premaster en Vak op de afhankelijke variabele Cijfer.
# 
# <!-- ## CLOSEDBLOK: Uitleg2.R -->

# In[ ]:


Premaster <- c(1,3,1,3)
Vak <- c("A", "A","B", "B")
Cijfer <- c(6,6,7,9)
dat <- cbind.data.frame(Premaster,Vak,Cijfer)
ggplot(dat, aes(x = Premaster, y = Cijfer, group = Vak, colour = Vak)) + geom_line() + geom_point(size = 2) + scale_color_manual(values = c("darkorange","deepskyblue")) + scale_x_continuous(breaks = c(1,3), labels = c("Premaster", "Geen Premaster")) + annotate("point", x = 2, y = 8, colour = "deepskyblue", fill = "deepskyblue", shape = 22, size = 3) + annotate("point", x = 2, y = 6, colour = "darkorange", fill = "darkorange", shape = 22, size = 3) + annotate("point", x = 1, y = 6.5, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) + annotate("point", x = 3, y = 7.5, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) 


# <!-- ## /CLOSEDBLOK: Uitleg2.R -->
# 
# *Figuur 2.  Illustratie van interactie-effecten bij mixed ANOVA voor een casus met de afhankelijke variabele Cijfer en de onafhankelijke variabelen Vak en Premaster. In deze grafiek is er een interactie-effect van de onafhankelijke variabelen Vak en Premaster op de afhankelijke variabele Cijfer.*
# 
# In Figuur 1 waren er hoofdeffecten van de variabelen Vak en Premaster gevonden, maar was het interactie-effect nog niet onderzocht. In deze figuur is er geen sprake van een interactie-effect, omdat het effect van Premaster op Cijfer hetzelfde is voor vak A en vak B en dus niet afhangt van de variabele Vak. Voor beide vakken (A en B) is het verschil tussen de groepen Premaster en Geen Premaster twee punten. Hier is dus geen sprake van een interactie-effect. Bij grafieken is er een interactie-effect als de twee (of meerdere) lijnen niet parallel lopen. Op deze manier kan snel onderzocht worden of er een interactie-effect is en wat de invloed van het interactie-effect is.
# 
# Bij *mixed ANOVA* worden bovenstaande grafieken gebruikt om de resultaten te interpreteren. De hoofdeffecten en interactie-effecten worden eerst statistisch getoetst en daarna geïnterpreteerd met onder andere deze grafieken. De aanpak is als volgt.[^10] Eerst wordt getoetst of er sprake is van een interactie-effect tussen de onafhankelijke variabelen. Als dit niet het geval is, kunnen de hoofdeffecten geïnterpreteerd worden. Als er wel een interactie-effect is, kunnen de hoofdeffecten niet geïnterpreteerd worden. De volgende stap is dan een *simple effects analyse* waarbij het effect van de ene onafhankelijke variabele op de afhankelijke variabele wordt getoetst voor alle groepen van de andere onafhankelijke variabele die deel uitmaakt van het interactie-effect. Voor Figuur 2 zou dit betekenen dat het effect van Premaster op Gemiddeld_cijfer apart getoetst wordt voor de vakken A en B van de variabele Vak. Het interactie-effect kan op deze manier geïnterpreteerd worden, samen met de grafische weergave zoals te zien in Figuur 2.
# 
# # Uitleg assumpties
# 
# Voor een valide toetsresultaat bij de *mixed ANOVA* moet er aan een aantal assumpties voldaan worden. De steekproef moet bestaan uit onafhankelijke deelnemers, de afhankelijke variabele moet normaal verdeeld zijn voor elke combinatie van groepen van de onafhankelijke variabelen. Daarnaast moet er sphericiteit zijn voor de within-subjects variabelen en homogeniteit van varianties voor de betwee-subjects variabelen bij elke combinatie van categorieën van de within-subjects variabelen.[^1]<sup>,</sup>[^22] In deze sectie worden de assumpties allen toegelicht en worden de opties bij het niet voldoen aan de assumptie weergegeven. Verderop in de toetspagina worden de assumpties getoetst met de dataset van de onderwijscasus.
# 
# ## Normaliteit
# Controleer de assumptie van normaliteit voor elke groep met de volgende stappen:  
# 1. Controleer de data visueel met een histogram, een boxplot of een Q-Q plot.   
# 2. Toets of de data normaal verdeeld zijn met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (n < 50) met de *Shapiro-Wilk test*.[^7]<sup>, </sup>[^8]  
# 
# <!-- ## TEKSTBLOK: Link1.R -->
# De *mixed ANOVA* is redelijk robuust ten opzichte van een schending van de assumptie van normaliteit. Als er kleine afwijkingen zijn, heeft dat relatief kleine gevolgen voor de validiteit van de toets. Bij grotere afwijkingen is het transformeren van de afhankelijke variabele een optie.[^2] Als dit niet werkt, dan is het een optie om de *mixed ANOVA* te splitsen door een losse *ANOVA* uit te voeren voor elke groep van de within-subjects variabele. Voor de groep waarin er afwijkingen van normaliteit zijn, kan dan de [Kruskal Wallis toets](10-Kruskal-Wallis-toets-I-R.html) uitgevoerd worden. Deze toets heeft minder onderscheidend vermogen dan de *ANOVA* maar hoeft niet aan de assumptie van normaliteit te voldoen.
# <!-- ## /TEKSTBLOK: Link1.R -->
# 
# ## Sphericiteit
# De assumptie van sphericiteit houdt in dat de variantie van de verschilscores tussen groepen ongeveer aan elkaar gelijk zijn.[^11] Bij een *mixed ANOVA* met meerdere onafhankelijke variabelen zijn er verschilscores te maken voor elke individuele onafhankelijke variabele en voor alle combinaties van interactie-effecten tussen de onafhankelijke variabelen. In de huidige casus zijn er voor de variabele Vak zes verschilscores te maken: Sustainable Innovation - Organizational Change Management, Sustainable Innovation - Organizational Psychology, Sustainable Innovation - masterthesis, Organizational Change Management - Organizational Psychology, Organizational Change Management - masterthesis en Organizational Psychology - masterthesis. De variantie van deze zes verschilscores moet dus ongeveer gelijk zijn om aan de assumptie te voldoen.
# 
# Toets deze assumptie met *Mauchly's test*. Als de onafhankelijke variabele niet aan de assumptie voldoet, geeft de gewone *mixed ANOVA* een verkeerd resultaat. Er zijn echter correcties die gebruikt kunnen worden als er niet aan sphericiteit voldaan is. Een voorbeeld van mogelijke output van *Mauchly's test* in R voor de huidige toetspagina is hieronder weergegeven.
# 
# <!-- ## CLOSEDBLOK: Sphericiteit.R -->

# In[ ]:


cat("$`Mauchly's Test for Sphericity`
  Effect         W           p p<.05
2    Vak 0.8732982 0.005073887     *

$`Sphericity Corrections`
  Effect       GGe        p[GG] p[GG]<.05       HFe        p[HF] p[HF]<.05
2    Vak   0.47683     0.05279         *   0.56298      0.04692         ")


# <!-- ## /CLOSEDBLOK: Sphericiteit.R -->
# 
# <!-- ## TEKSTBLOK: Sphericiteit1.R -->
# Bij een p-waarde kleiner dan 0,05, toont *Mauchly's test* dat de assumptie van sphericiteit geschonden is. In de output is dit te zien aan de p-waarde van 0,0051 onder ` $Mauchly's Test for Sphericity `. Er zijn twee mogelijke correcties als er geen sphericiteit is: de Greenhouse-Geisser (GG) en Huynh-Feldt (HF) correctie. De Greenhouse-Geisser correctie staat bekend als conservatief, wat betekent dat de correctie een relatief lage kans op een type I fout heeft. In andere woorden, het zal niet vaak gebeuren dat deze correctie een significant effect aantoont wanneer dat er in werkelijkheid niet is. De Huynh-Feldt correctie staat echter bekend als liberaal, wat betekent dat er een relatief hoge kans op een type I fout is. De toetsstatistiek en p-waarde van beide correcties zijn in de output te vinden onder ` $Sphericity Corrections `.
# <!-- ## TEKSTBLOK: Sphericiteit1.R -->
# 
# Houd de volgende richtlijnen aan bij het interpreteren van de *repeated measures ANOVA* als er niet aan sphericiteit is voldaan:
# 
# * Als beide correcties significant zijn, rapporteer de (conservatieve) Greenhouse-Geisser correctie.
# * Als beide correcties niet significant zijn, rapporteer de (liberale) Huynh-Feldt correctie.
# * Als de een significant is en de ander niet, bereken de gemiddelde p-waarde van beide correcties.
#     * Als deze p-waarde significant is, rapporteer dan de significante correctie.
#     * Als deze p-waarde niet significant is, rapporteer dan de niet significante correctie.
# 
# In de voorbeeldoutput is de p-waarde van de Greenhouse-Geisser correctie groter dan 0,05 en de p-waarde van de Huynh-Feldt correctie kleiner dan 0,05. Het gemiddelde van beide p-waarden is 0,049855, wat betekent dat er een significant resultaat is. Rapporteer in dit geval dus de (significante) Huynh-Feldt correctie, i.e. *F* = 0,56, *p* < 0,05.  
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^11] Voor de *mixed ANOVA* wordt de effectmaat *partial eta squared* vaak gebruikt.[^4]
# 
# De effectmaat *partial eta squared* (partial *η^2^*) berekent de proportie van de onverklaarde variantie (variantie die niet door de andere variabelen wordt verklaard) in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele.[^4] Voor de variabele Premaster geeft de partial eta squared dus de proportie verklaarde variantie weer van de variantie die niet verklaard is door de variabele Vak en de interactie tussen de variabele Premaster en Vak. De partial eta squared van alle termen van het model tellen dus niet per se op tot 1.[^4] Een indicatie om partial *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^5]
# 
# # Post-hoc toetsen
# 
# De eerste stap van de *mixed ANOVA* is het toetsen van hoofdeffecten en interactie-effecten. De volgende stap bestaat uit het bepalen welke groepen van elkaar verschillen, zowel bij *simple effects analyse* als bij het interpreteren van hoofdeffecten, en wordt gedaan met post-hoc toetsen. De post-hoc toetsen voeren meestal een correctie voor de p-waarden uit, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout. Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^11] Let er bij de *mixed ANOVA* op dat de post-hoc toetsen afhangen van het soort onafhankelijke variabele. Bij within-subjects variabelen hoort een gepaarde post-hoc toets en bij between-subjects hoort een ongepaarde post-hoc toets.[^11]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset ingeladen met de cijfers per vak en informatie over het volgen van een premaster voor studenten van de master Sustainable Change Management. De dataset heet `Resultaten_SCM`. 
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 5 observaties
head(Resultaten_SCM)

## Laatste 5 observaties
tail(Resultaten_SCM)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 

# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# Inspecteer voor alle groepen het gemiddelde, de standaardafwijking, de mediaan en het aantal observaties om meer inzicht te krijgen. Gebruik hiervoor de functie `descr` en `stby` van het package `summarytools` om de beschrijvende statistieken per groep weer te geven. Voer de gewenste statistieken in met het argument `stats = c("mean","sd","med","n.valid")`.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-1.R -->

# In[ ]:


# Gemiddelde, standaardafwijking, mediaan en aantal observaties
library(summarytools)

with(Resultaten_SCM, 
     stby(data = Cijfer, 
          list(Vak, Premaster), 
          descr, 
          stats = c("mean", "sd", "med", "n.valid")))


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
# 
# Maak vervolgens een grafiek met de gemiddelden voor de verschillende groepen.
# 
# <!-- ## OPENBLOK: Data-beschrijven2.R -->

# In[ ]:


library(ggplot2)

ggplot(Resultaten_SCM, 
       aes(x = Premaster, y = Cijfer, group = Vak, colour = Vak)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Vak)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue","darkgreen","purple")) 


# <!-- ## /OPENBLOK: Data-beschrijven2.R -->
# 
# *Figuur 3.  Gemiddelde cijfers per groep op basis van de variabelen Vak en Premaster voor de dataset Resultaten_SCM.*
# 
# Op basis van de beschrijvende statistieken en de grafiek (Figuur 3) lijken er verschillen tussen de groepen te zijn. Studenten vanuit de premaster hebben een lager gemiddeld cijfer voor de vakken Organizational Change Management en Organizational Psychologie en de masterthesis, maar een hoger gemiddeld cijfer voor het vak Sustainable Innovation. De lijnen van de vaksoorten theorie en praktijk lopen niet parallel dus er lijkt een interactie-effect te zijn. De *mixed ANOVA* zal dit interactie-effect toetsen.
# 
# ## Normaliteit
# 
# De *mixed ANOVA* vereist dat de verdeling van de afhankelijke variabele de normale verdeling benaderd in elke groep die gevormd wordt door de onafhankelijke variabelen. Toets deze assumptie met behulp van een histogram en de *Kolmogorov-Smirnov* en *Shapiro-Wilk test*.
# 
# ### Histogram
# 
# Visualiseer de verdeling van de gemiddelde cijfers binnen elke groep met behulp van een histogram.[^9] Focus bij het analyseren van een histogram op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke outliers. Een normale verdeling is symmetrisch, heeft één top en geen outliers.[^16]<sup>, </sup>[^17]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot
ggplot(Resultaten_SCM,
  aes(x = Cijfer)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 0.5,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Premaster + Vak) +
  geom_density(alpha = .2, adjust = 1) +
  ylab("Cijfer")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# *Figuur 4.  Histogrammen van de verdelingen van de gemiddelde cijfers per groep op basis van de variabelen Vak en Premaster.*
# 
# De verdelingen van de acht groepen, te zien in Figuur 4, zijn redelijk symmetrisch, hebben geen outliers en zijn allen eentoppig. De verdelingen zijn dus bij benadering normaal.
# 
# ### Toetsen van normaliteit
# Voer een toets uit om te controleren of de data normaal verdeeld zijn. Twee veelgebruikte toetsen zijn: de *Kolmogorov-Smirnov test* en de *Shapiro-Wilk test*.
# 
# #### Kolmogorov-Smirnov test
# De *Kolmogorov-Smirnov test* toetst het verschil tussen twee verdelingen. Standaard toetst deze toets het verschil tussen een normale verdeling en de verdeling van de steekproef. De Lilliefors correctie is vereist als het gemiddelde en de standaardafwijking niet van tevoren bekend of bepaald zijn, wat meestal het geval is bij een steekproef. Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.[^18]
# 
# <!-- ## OPENBLOK: KStest.R -->

# In[ ]:


library("nortest")

with(Resultaten_SCM, 
     by(data = Cijfer, 
        list(Vak, Premaster), 
        lillie.test))


# <!-- ## /OPENBLOK: KStest.R -->
# 
# De p-waarde is groter dan 0,05 voor elke groep; er zijn dus geen significante verschillen gevonden tussen de verdelingen van de steekproef en de normale verdeling. De *mixed ANOVA* kan uitgevoerd worden.
# 
# #### Shapiro-Wilk test
# De *Shapiro-Wilk test* is een soortgelijke toets als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (*n* < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.[^18]
# 
# <!-- ## OPENBLOK: Shapiro-Wilk-test.R -->

# In[ ]:


with(Resultaten_SCM, 
     by(data = Cijfer, 
        list(Vak, Premaster), 
        shapiro.test))


# <!-- ## /OPENBLOK: Shapiro-Wilk-test.R -->
# 
# De p-waarde is groter dan 0,05 voor elke groep; er zijn dus geen significante verschillen gevonden tussen de verdelingen van de steekproef en de normale verdeling. De *mixed ANOVA* kan uitgevoerd worden.
# 
# ## Sphericiteit
# 
# <!-- ## TEKSTBLOK: LeveneTest1.R -->
# Toets met *Mauchly's test* de assumptie van sphericiteit. Gebruik de functie `ezANOVA()$Mauchly's Test for Sphericity` van het package `ez` met als argumenten de dataset `Resultaten_SCM`, de afhankelijke variabele `dv = Cijfer`, de variabele die de deelnemers aangeeft `wid = Studentnummer`, de within-subjects variabele `within = Vak` en de between-subjects variabele `between = Premaster`.
# <!-- ## /TEKSTBLOK: LeveneTest1.R -->
# 
# <!-- ## OPENBLOK: Levenes-test.R -->

# In[ ]:


library(ez)

ezANOVA(Resultaten_SCM, 
        dv = Cijfer, 
        wid = Studentnummer,
        within = Vak,
        between = Premaster)$`Mauchly's Test for Sphericity`


# <!-- ## /OPENBLOK: Levenes-test.R -->
# 
# <!-- ## CLOSEDBLOK: Levenes-test.R -->

# In[ ]:



obj <- ezANOVA(Resultaten_SCM, 
        dv = Cijfer, 
        wid = Studentnummer,
        within = Vak,
        between = Premaster)$`Mauchly's Test for Sphericity`

Mauchly_W_Periode <- Round_and_format(obj$W[1])
p_Periode <- Round_and_format(obj$p[1])


# <!-- ## /CLOSEDBLOK: Levenes-test.R -->
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# * Voor de onafhankelijke variabele Vak is er voldaan aan de assumptie van sphericiteit, *W* = `r Mauchly_W_Periode`, *p* = `r p_Periode`[^18]
# * Er hoeft geen correctie uitgevoerd te worden voor de *mixed ANOVA*
# * De interactieterm tussen de within-subjects variabele Vak en de between-subjects variabele Premaster wordt in de output weergegeven, maar hoeft niet geïnterpreteerd te worden. Alleen interactietermen tussen twee of meerdere within-subjects variabelen moeten geïnterpreteerd worden voor sphericiteit. De oplettende lezer ziet ook dat het resultaat van *Macuhly's test* precies hetzelfde is voor beide effecten.

# <!-- ## TEKSTBLOK: Levenes-test.R -->
# 
# ## Homogeniteit van varianties
# 
# <!-- ## TEKSTBLOK: Levenes-test2.R -->
# Toets met de *Levene's test* de assumptie homogeniteit van varianties voor alle vier de vakken. Maak eerst per vak een dataset. Voer daarna de *Levene's test* uit met de functie `leveneTest` van het package `car` met het argument `Cijfer ~ Premaster` met daarin de afhankelijke variabele `Cijfer` en de onafhankelijke variabele `Premaster` en het argument `data = Resultaten_SCM_SI` om de dataset aan te geven.
# <!-- ## /TEKSTBLOK: Levenes-test2.R -->
# 
# <!-- ## OPENBLOK: Levenes-test3.R -->

# In[ ]:


library(car)

# Maak een dataset voor de vier vakken
Resultaten_SCM_SI <- Resultaten_SCM[Resultaten_SCM$Vak == "Sustainable Innovation",]
Resultaten_SCM_OC <- Resultaten_SCM[Resultaten_SCM$Vak == "Organizational Change Management",]
Resultaten_SCM_OP <- Resultaten_SCM[Resultaten_SCM$Vak == "Organizational Psychology",]
Resultaten_SCM_TH <- Resultaten_SCM[Resultaten_SCM$Vak == "Thesis",]

# Voer voor alle vier de vakken de Levene's test uit
leveneTest(Cijfer ~ Premaster, data = Resultaten_SCM_SI)
leveneTest(Cijfer ~ Premaster, data = Resultaten_SCM_OC)
leveneTest(Cijfer ~ Premaster, data = Resultaten_SCM_OP)
leveneTest(Cijfer ~ Premaster, data = Resultaten_SCM_TH)


# <!-- ## /OPENBLOK: Levenes-test3.R -->
# 
# Voor alle vier de vakken is de p-waarde groter dan 0,05, dus er zijn geen significante verschillen gevonden tussen de variantie in cijfers van de groep Premaster en de groep Geen Premaster.[^18] Dit betekent dat er voor alle vakken voldaan is aan de assumptie van homogeniteit van varianties. De *mixed ANOVA* kan uitgevoerd worden.
# 
# # Mixed ANOVA 
# 
# <!-- ## TEKSTBLOK: ANOVA-toets.R -->
# Voer de *mixed ANOVA* uit om de vraag te beantwoorden of er verschillen zijn tussen premasterstudenten en direct toelaatbare studenten en tussen de vakken Sustainable Innovation, Organizational Change Management, Organizational Psychology en de masterthesis voor de master Sustainable Change Management. Gebruik de functie `ezANOVA()` van het package `ez` met als argumenten de dataset `Resultaten_SCM`, de afhankelijke variabele `dv = Cijfer`, de variabele die de deelnemers aangeeft `wid = Studentnummer`, de within-subjects variabele `within = Vak`, de between-subjects variabele `between = Premaster` en het argument `detailed = TRUE` dat nodig is om later de effectmaat te berekenen.
# <!-- ## /TEKSTBLOK: ANOVA-toets.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets1.R -->

# In[ ]:


library(ez)

Mixed_ANOVA <- ezANOVA(Resultaten_SCM,
                       dv = Cijfer, 
                       wid = Studentnummer,
                       within = Vak,
                       between = Premaster,
                       detailed = TRUE)

Mixed_ANOVA


# <!-- ## /OPENBLOK: ANOVA-toets1.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets2.R -->
# Bereken de effectmaat partial eta squared met behulp van de functie `anova_out()` van het package `scoRsch` met als argument het ANOVA-object `Mixed_ANOVA`. Deze functie geeft de output van de *mixed ANOVA* op een andere manier weer en laat ook de partial eta squared zien.
# <!-- ## /TEKSTBLOK: ANOVA-toets2.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets3.R -->

# In[ ]:


library(schoRsch)

anova_out(Mixed_ANOVA)


# <!-- ## /OPENBLOK: ANOVA-toets3.R -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets4.R -->

# In[ ]:


MA <- ezANOVA(Resultaten_SCM, 
        dv = Cijfer, 
        wid = Studentnummer,
        within = Vak,
        between = Premaster,
        detailed = TRUE)$ANOVA

vF_waarde <- Round_and_format(MA$F[4])
vDF1 <- Round_and_format(MA$DFn[4])
vDF2 <- Round_and_format(MA$DFd[4])

pes <- anova_out(Mixed_ANOVA)[[1]]

vEsq <- Round_and_format(as.numeric(as.character(pes$petasq[4])))


# <!-- ## /CLOSEDBLOK: ANOVA-toets4.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets5.R -->
# 
# * Er is een significant interactie-effect van Vak en Premaster op Cijfer, *F* (`r vDF1`,`r vDF2`) = `r vF_waarde`, *p* < 0,0001, partial *η^2^* = `r vEsq`.
# * De p-waarde is kleiner dan 0,05, dus de nulhypothese dat er geen interactie-effect is wordt verworpen.[^18] 
# * Er is een groot effect van de interactie tussen Vak en Premaster op Cijfer
# * Omdat er een significant interactie-effect is, hoeven de hoofdeffecten niet geïnterpreteerd te worden. De volgende stap is een *simple effects analyse* om te interactie verder te onderzoeken.
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets5.R -->
# 
# ## Simple effects analyse
# 
# Voer een *simple effects analyse* uit om het interactie-effect te interpreteren. Vergelijk eerst de verschillen tussen de vier vakken voor elke categorie van de variabele Premaster (Premaster en Geen Premaster dus). Vergelijk daarna de verschillen tussen de groepen Premaster en Geen Premaster voor elk vak.
# 
# ### Vak
# 
# <!-- ## TEKSTBLOK: SimEff1.R -->
# Maak eerst een aparte dataset voor de groepen Premaster en Geen Premaster, voer vervolgens de post-hoc toets uit en bereken de gemiddelden per onderwijsperiode. Gebruik voor de post-hoc toetsen de functie `pairwise.t.test()` met als argumenten de afhankelijk variabele `Premaster_Resultaten_SCM$Cijfer`, de onafhankelijke variabele `Premaster_Resultaten_SCM$Vak`, het argument `paired = TRUE` omdat er een gepaarde vergelijking gemaakt wordt en de gebruikte methode om te corrigeren voor meerdere toetsen `p.adjust.method = "bonferroni"`.
# <!-- ## /TEKSTBLOK: SimEff1.R -->
# 
# <!-- ## OPENBLOK: SimEff2.R -->

# In[ ]:


# Maak een dataset voor de groep Premaster en de groep Geen Premaster
Premaster_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Premaster == "Premaster",]

Geen_Premaster_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Premaster == "Geen premaster",]

# Voer de post-hoc toetsen uit
pairwise.t.test(Premaster_Resultaten_SCM$Cijfer,
                Premaster_Resultaten_SCM$Vak,
                paired = TRUE,
                p.adjust.method = "bonferroni")

pairwise.t.test(Geen_Premaster_Resultaten_SCM$Cijfer,
                Geen_Premaster_Resultaten_SCM$Vak,
                paired = TRUE,
                p.adjust.method = "bonferroni")

# Bereken het gemiddelde per groep voor beide datasets
with(Premaster_Resultaten_SCM, 
     by(data = Cijfer, 
        list(Vak), 
        mean))

with(Geen_Premaster_Resultaten_SCM, 
     by(data = Cijfer, 
        list(Vak), 
        mean))


# <!-- ## /OPENBLOK: SimEff2.R -->
# 
# <!-- ## CLOSEDBLOK: SimEff3.R -->
# ````{r, echo=FALSE}
# # Maak een dataset voor de groep Premaster en de groep Geen Premaster
# Premaster_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Premaster == "Premaster",]
# 
# Geen_Premaster_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Premaster == "Geen premaster",]
# 
# # Voer de post-hoc toetsen uit
# Posthoc_Premaster <- pairwise.t.test(Premaster_Resultaten_SCM$Cijfer,
#                 Premaster_Resultaten_SCM$Vak,
#                 paired = TRUE,
#                 p.adjust.method = "bonferroni")$p.value
# 
# Posthoc_Geen_Premaster <- pairwise.t.test(Geen_Premaster_Resultaten_SCM$Cijfer,
#                 Geen_Premaster_Resultaten_SCM$Vak,
#                 paired = TRUE,
#                 p.adjust.method = "bonferroni")$p.value
# 
# # Bereken het gemiddelde per groep voor beide datasets
# Mean_Premaster <- with(Premaster_Resultaten_SCM, 
#      by(data = Cijfer, 
#         list(Vak), 
#         mean))
# 
# Mean_Geen_Premaster <- with(Geen_Premaster_Resultaten_SCM, 
#      by(data = Cijfer, 
#         list(Vak), 
#         mean))
# 
# ```
# <!-- ## /CLOSEDBLOK: SimEff3.R -->
# 
# <!-- ## TEKSTBLOK: SimEff4.R -->
# Voor de premasterstudenten zijn de volgende vergelijkingen getoetst[^18]:
# 
# * Organizational Change Management versus Organizational Psychology: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(Mean_Premaster[1])`) en Organizational Psychology (`r Round_and_format(Mean_Premaster[2])`) zijn significant verschillend (*p* = `r Round_and_format(Posthoc_Premaster[1,1])`)
# * Organizational Change Management versus Sustainable Innovation: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(Mean_Premaster[1])`) en Sustainable Innovation (`r Round_and_format(Mean_Premaster[3])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Change Management versus Thesis: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(Mean_Premaster[1])`) en Thesis (`r Round_and_format(Mean_Premaster[4])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Psychology versus Sustainable Innovation: het gemiddelde cijfer in Organizational Psychology (`r Round_and_format(Mean_Premaster[2])`) en Sustainable Innovation (`r Round_and_format(Mean_Premaster[3])`) zijn niet significant verschillend (*p* = `r Round_and_format(Posthoc_Premaster[2,2])`)
# * Organizational Psychology versus Thesis: het gemiddelde cijfer in Organizational Psychology (`r Round_and_format(Mean_Premaster[2])`) en Thesis (`r Round_and_format(Mean_Premaster[4])`) zijn significant verschillend (*p* < 0,0001)
# * Sustainable Innovation versus Thesis: het gemiddelde cijfer in Sustainable Innovation (`r Round_and_format(Mean_Premaster[3])`) en Thesis (`r Round_and_format(Mean_Premaster[4])`) zijn significant verschillend (*p* = `r Round_and_format(Posthoc_Premaster[3,3])`)

# Voor de studenten die geen premaster hebben gevolgd zijn de volgende vergelijkingen getoetst[^18]:
# 
# * Organizational Change Management versus Organizational Psychology: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(Mean_Premaster[1])`) en Organizational Psychology (`r Round_and_format(Mean_Premaster[2])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Change Management versus Sustainable Innovation: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(Mean_Premaster[1])`) en Sustainable Innovation (`r Round_and_format(Mean_Premaster[3])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Change Management versus Thesis: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(Mean_Premaster[1])`) en Thesis (`r Round_and_format(Mean_Premaster[4])`) zijn significant verschillend (*p* = `r Round_and_format(Posthoc_Premaster[3,1])`)
# * Organizational Psychology versus Sustainable Innovation: het gemiddelde cijfer in Organizational Psychology (`r Round_and_format(Mean_Premaster[2])`) en Sustainable Innovation (`r Round_and_format(Mean_Premaster[3])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Psychology versus Thesis: het gemiddelde cijfer in Organizational Psychology (`r Round_and_format(Mean_Premaster[2])`) en Thesis (`r Round_and_format(Mean_Premaster[4])`) zijn niet significant verschillend (*p* = `r Round_and_format(Posthoc_Premaster[3,2])`)
# * Sustainable Innovation versus Thesis: het gemiddelde cijfer in Sustainable Innovation (`r Round_and_format(Mean_Premaster[3])`) en Thesis (`r Round_and_format(Mean_Premaster[4])`) zijn significant verschillend (*p* < 0,0001)
# 
# <!-- ## /TEKSTBLOK: SimEff4.R -->
# 
# ### Premaster
# 
# <!-- ## TEKSTBLOK: SimEff5.R -->
# Maak eerst aparte datasets voor de vakken Organization Change Management (OC), Organizational Psychology (OP), Sustainable Innovation (SI) en de masterthesis (TH) en voer vervolgens de post-hoc toets uit. Gebruik voor de post-hoc toetsen de functie `pairwise.t.test()` met als argumenten de afhankelijk variabele `OC_Resultaten_SCM$Cijfer`, de onafhankelijke variabele `OC_Resultaten_SCM$Vak`, het argument `paired = FALSE` omdat er een ongepaarde vergelijking gemaakt wordt en de gebruikte methode om te corrigeren voor meerdere toetsen `p.adjust.method = "bonferroni"`.
# <!-- ## /TEKSTBLOK: SimEff5.R -->
# 
# <!-- ## OPENBLOK: SimEff6.R -->

# In[ ]:


# Maak een dataset voor de vier vakken
OC_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Vak == "Organizational Change Management",]
OP_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Vak == "Organizational Psychology",]
SI_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Vak == "Sustainable Innovation",]
TH_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Vak == "Thesis",]

# voer de post-hoc toetsen uit
pairwise.t.test(OC_Resultaten_SCM$Cijfer,
                OC_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")

pairwise.t.test(OP_Resultaten_SCM$Cijfer,
                OP_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")

pairwise.t.test(SI_Resultaten_SCM$Cijfer,
                SI_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")

pairwise.t.test(TH_Resultaten_SCM$Cijfer,
                TH_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")

# Bereken het gemiddelde per groep
with(Resultaten_SCM, 
     by(data = Cijfer, 
        list(Premaster, Vak), 
        mean))


# <!-- ## /OPENBLOK: SimEff6.R -->
# 
# <!-- ## CLOSEDBLOK: SimEff7.R -->

# In[ ]:


# Maak een dataset voor de vier vakken
OC_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Vak == "Organizational Change Management",]
OP_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Vak == "Organizational Psychology",]
SI_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Vak == "Sustainable Innovation",]
TH_Resultaten_SCM <- Resultaten_SCM[Resultaten_SCM$Vak == "Thesis",]

# voer de post-hoc toetsen uit
posthoc_OC <- pairwise.t.test(OC_Resultaten_SCM$Cijfer,
                OC_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")$p.value

posthoc_OP <- pairwise.t.test(OP_Resultaten_SCM$Cijfer,
                OP_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")$p.value

posthoc_SI <- pairwise.t.test(SI_Resultaten_SCM$Cijfer,
                SI_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")$p.value

posthoc_TH <- pairwise.t.test(TH_Resultaten_SCM$Cijfer,
                TH_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")$p.value

# Bereken het gemiddelde per groep
Mean_Vak <- with(Resultaten_SCM, 
     by(data = Cijfer, 
        list(Premaster, Vak), 
        mean))


# <!-- ## /CLOSEDBLOK: SimEff7.R -->
# 
# <!-- ## TEKSTBLOK: SimEff8.R -->
# * Organizational Change Management: het gemiddelde cijfer voor de groep Premaster (`r Round_and_format(Mean_Vak[1,1])`) en voor de groep Geen Premaster (`r Round_and_format(Mean_Vak[2,1])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Psychology: het gemiddelde cijfer voor de groep Premaster (`r Round_and_format(Mean_Vak[1,2])`) en voor de groep Geen Premaster (`r Round_and_format(Mean_Vak[2,2])`) zijn significant verschillend (*p* < 0,0001)
# * Sustainable Innovation: het gemiddelde cijfer voor de groep Premaster (`r Round_and_format(Mean_Vak[1,3])`) en voor de groep Geen Premaster (`r Round_and_format(Mean_Vak[2,3])`) zijn significant verschillend (*p* < 0,0001)
# * Thesis: het gemiddelde cijfer voor de groep Premaster (`r Round_and_format(Mean_Vak[1,4])`) en voor de groep Geen Premaster (`r Round_and_format(Mean_Vak[2,4])`) zijn niet significant verschillend (*p* = `r Round_and_format(posthoc_TH)`)
# 
# <!-- ## /TEKSTBLOK: SimEff8.R -->

# ## Illustratie van post-hoc toetsing bij hoofdeffecten zonder interactie-effect
# 
# <!-- ## TEKSTBLOK: PHtest1.R -->
# In de huidige casus worden de hoofdeffecten niet geïnterpreteerd vanwege het significante interactie-effect. Om toch te illustreren hoe het interpreteren van hoofdeffecten zonder een significant interactie-effect werkt, wordt de bijbehorende post-hoc toetsing toch geïllustreerd. Hiervoor wordt  een nieuwe dataset `Hoofdeffecten_Resultaten_SCM` gebruikt. 
# 
# <!-- ## /TEKSTBLOK: PHtest1.R -->
# 
# <!-- ## OPENBLOK: PHtest2.R -->

# In[ ]:


library(ez)

## Voer de mixed ANOVA uit
Mixed_ANOVA_H <- ezANOVA(Hoofdeffecten_Resultaten_SCM,
                       dv = Cijfer, 
                       wid = Studentnummer,
                       within = Vak,
                       between = Premaster,
                       detailed = TRUE)

## Geef de resultaten weer
Mixed_ANOVA_H

library(schoRsch)

## Geef met deze functie opnieuw de resultaten weer om de effectmaat partial eta squared te vinden
anova_out(Mixed_ANOVA_H)


# <!-- ## /OPENBLOK: PHtest2.R -->
# 
# <!-- ## CLOSEDBLOK: PHtest3.R -->

# In[ ]:


MA_H <- ezANOVA(Hoofdeffecten_Resultaten_SCM, 
        dv = Cijfer, 
        wid = Studentnummer,
        within = Vak,
        between = Premaster,
        detailed = TRUE)$ANOVA

vF_waarde_H <- Round_and_format(MA_H$F[4])
vDF1_H <- Round_and_format(MA_H$DFn[4])
vDF2_H <- Round_and_format(MA_H$DFd[4])

pes_H <- anova_out(Mixed_ANOVA_H)[[1]]

vEsq_H <- Round_and_format(as.numeric(as.character(pes_H$petasq[4])))
vp_H <- Round_and_format(MA_H$p[3])


# <!-- ## /CLOSEDBLOK: PHtest3.R -->
# 
# <!-- ## TEKSTBLOK: PHtest4.R -->
# Er is geen significant interactie-effect van Vak en Premaster op Cijfer, *F* (`r vDF1_H`,`r vDF2_H`) = `r vF_waarde_H`, *p* = `vp_H`, *η^2^* = `r vEsq_H`.[^18] De hoofdeffecten van Vak (*p* < 0,0001) en Premaster (*p* < 0,0001) zijn wel significant.[^18] Voer daarom post-hoc toetsen uit voor beide variabelen. 
# 
# Gebruik voor de post-hoc toetsen de functie `pairwise.t.test()` met als argumenten de afhankelijk variabele `Hoofdeffecten_Resultaten_SCM$Cijfers`, de onafhankelijke variabele `Hoofdeffecten_Resultaten_SCM$Vak` of `Hoofdeffecten_Resultaten_SCM$Premaster` en de gebruikte methode om te corrigeren voor meerdere toetsen `p.adjust.method = "bonferroni"`. Voer voor de variabele Vak een gepaarde post-hoc toets uit met het argument `paired = TRUE` en voor de variabele Premaster een ongepaarde post-hoc toets uit met het argument `paired = FALSE`.
# 
# <!-- ## /TEKSTBLOK: PHtest4.R -->
# 
# <!-- ## OPENBLOK: PHtest5.R -->

# In[ ]:


# Voer de post-hoc toetsen uit voor de variabele Vak
pairwise.t.test(Hoofdeffecten_Resultaten_SCM$Cijfer,
                Hoofdeffecten_Resultaten_SCM$Vak,
                paired = TRUE,
                p.adjust.method = "bonferroni")

# Bereken het gemiddelde cijfer voor de vakken
with(Hoofdeffecten_Resultaten_SCM, 
     by(data = Cijfer, 
        list(Vak), 
        mean))

# Voer de post-hoc toetsen uit voor de variabele Premaster
pairwise.t.test(Hoofdeffecten_Resultaten_SCM$Cijfer,
                Hoofdeffecten_Resultaten_SCM$Premaster,
                paired = FALSE,
                p.adjust.method = "bonferroni")

# Bereken het gemiddelde cijfer voor de groep Premaster en de groep Geen Premaster
with(Hoofdeffecten_Resultaten_SCM, 
     by(data = Cijfer, 
        list(Premaster), 
        mean))


# <!-- ## /OPENBLOK: PHtest5.R -->
# 
# <!-- ## CLOSEDBLOK: PHtest6.R -->
# ````{r, echo=FALSE}
# PH_Vak <- pairwise.t.test(Hoofdeffecten_Resultaten_SCM$Cijfer,
#                 Hoofdeffecten_Resultaten_SCM$Vak,
#                 p.adjust.method = "bonferroni")$p.value
# 
# PH_Premaster <- pairwise.t.test(Hoofdeffecten_Resultaten_SCM$Cijfer,
#                 Hoofdeffecten_Resultaten_SCM$Premaster,
#                 p.adjust.method = "bonferroni")$p.value
# 
# # Bereken het gemiddelde cijfer voor
# H_mean_Vak <- with(Hoofdeffecten_Resultaten_SCM, 
#      by(data = Cijfer, 
#         list(Vak), 
#         mean))
# 
# # Bereken het gemiddelde cijfer voor de
# H_mean_Premaster <- with(Hoofdeffecten_Resultaten_SCM, 
#      by(data = Cijfer, 
#         list(Premaster), 
#         mean))
# 
# ```
# <!-- ## /CLOSEDBLOK: PHtest6.R -->
# 
# <!-- ## TEKSTBLOK: PHtest7.R -->
# De verschillen voor de groepen van de onafhankelijke variabele Premaster zijn[^18]:
# 
# * Het gemiddelde cijfer voor de groep Premaster (`r Round_and_format(H_mean_Premaster[2])`) en voor het praktijkvak (`r Round_and_format(H_mean_Premaster[1])`) zijn significant verschillend (*p* < 0,0001)
# 
# De verschillen voor de groepen van de onafhankelijke variabele Vak zijn[^18]:
# 
# * Organizational Change Management versus Organizational Psychology: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(H_mean_Vak[1])`) en Organizational Psychology (`r Round_and_format(H_mean_Vak[2])`) zijn significant verschillend (*p* = 0,010)
# * Organizational Change Management versus Sustainable Innovation: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(H_mean_Vak[1])`) en Sustainable Innovation (`r Round_and_format(H_mean_Vak[3])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Change Management versus Thesis: het gemiddelde cijfer in Organizational Change Management (`r Round_and_format(H_mean_Vak[1])`) en Thesis (`r Round_and_format(H_mean_Vak[4])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Psychology versus Sustainable Innovation: het gemiddelde cijfer in Organizational Psychology (`r Round_and_format(H_mean_Vak[2])`) en Sustainable Innovation (`r Round_and_format(H_mean_Vak[3])`) zijn significant verschillend (*p* < 0,0001)
# * Organizational Psychology versus Thesis: het gemiddelde cijfer in Organizational Psychology (`r Round_and_format(H_mean_Vak[2])`) en Thesis (`r Round_and_format(H_mean_Vak[4])`) zijn significant verschillend (*p* < 0,0001)
# * Sustainable Innovation versus Thesis: het gemiddelde cijfer in Sustainable Innovation (`r Round_and_format(H_mean_Vak[3])`) en Thesis (`r Round_and_format(H_mean_Vak[4])`) zijn significant verschillend (*p* < 0,0001)
# 
# <!-- ## /TEKSTBLOK: PHtest7.R -->
# 
# Visualiseer de gemiddelden per groep om de resultaten ook visueel weer te geven. In de grafiek in Figuur 5 is te zien dat de lijnen redelijk parallel lopen wat overeenkomt met het feit dat er geen significant interactie-effect is. Het hoofdeffect van de variabele Premaster is duidelijk zichtbaar: de gemiddeldes van de groep Geen Premaster liggen voor alle vakken hoger dan de gemiddeldes van de groep Premaster. Dit komt overeen met het significante verschil tussen beide groepen op de post-hoc toets. Het hoofdeffect van de variabele Vak is ook zichtbaar. De masterthesis heeft het hoogste gemiddelde cijfer en het vak Sustainable Innovation het laagste gemiddelde cijfer. De vakken Organizational Change Management en Organizational Psychology liggen qua gemiddelde ertussenin. Uit de post-hoc toetsen blijkt dat al deze verschillen significant zijn.
# 
# <!-- ## OPENBLOK: PHtest8.R -->

# In[ ]:


library(ggplot2)

ggplot(Hoofdeffecten_Resultaten_SCM, 
       aes(x = Vak, y = Cijfer, group = Premaster, colour = Premaster)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Premaster)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue")) +
  scale_x_discrete(labels = c("OC", "OP", "SI",  "TH"))


# <!-- ## /OPENBLOK: PHtest8.R -->
# 
# *Figuur 5.  Gemiddelde cijfers per groep op basis van Vak en Premaster voor de dataset Hoofdeffecten_Resultaten_SCM. De afkortingen staan voor de vakken Organizational Change Management (OC), Organizational Psychology (OP), Sustainable Innovation (SI) en de masterthesis (TH).*
# 
# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *mixed ANOVA* is uitgevoerd om te toetsen of er verschillen zijn tussen premasterstudenten en direct toelaatbare studenten en tussen de vakken Organizational Change Management, Organizational Psychology, Sustainable Innovation en de masterthesis wat betreft de cijfers van studenten van de master Sustainable Change Management. De resultaten lieten zien dat er een significant interactie-effect was tussen de variabelen Vak en Premaster op de gemiddelde cijfers van de studenten, *F* (`r vDF1`,`r vDF2`) = `r vF_waarde`, *p* < 0,0001, *η^2^* = `r vEsq`. 
# 
# Om dit effect verder te onderzoeken, is er een *simple effects analyse* uitgevoerd met behulp van post-hoc toetsen met een Bonferroni-correctie voor meerdere toetsen. Uit deze analyse bleek dat er voor de drie vakken een significant verschil is tussen de gemiddelde cijfers van de premasterstudenten en direct toelaatbare studenten, maar dat er geen significant verschil is bij de masterthesis. Premasterstudenten hebben hogere cijfers bij het vak Sustainable Innovation, maar lagere cijfers bij de vakken Organizational Change Management en Organizational Psychology. Voor de direct toelaatbare studenten zijn er significante verschillen voor alle vergelijkingen van vakken behalve de vergelijking tussen de gemiddelde cijfers voor het vak Organizational Psychology en de masterthesis. Voor premasterstudenten zijn er significante verschillen voor alle vergelijkingen van vakken behalve de vergelijking van de gemiddelde cijfers voor de vakken Organizational Psychology en Sustainable Innovation. In Figuur 6 zijn de gemiddeldes voor alle groepen weergegeven om de resultaten te ondersteunen.
# 
# Samenvattend suggereren de resultaten dat het afhankelijk is van het vak of premasterstudenten even goed, beter of minder goede cijfers halen voor de vakken van de master Sustainable Change Management.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Rapportage2.R -->

# In[ ]:


library(ggplot2)

ggplot(Resultaten_SCM, 
       aes(x = Vak, y = Cijfer, group = Premaster, colour = Premaster)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Premaster)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue"))  +
  scale_x_discrete(labels = c("OC", "OP", "SI",  "TH"))


# <!-- ## /CLOSEDBLOK: Rapportage2.R -->
# 
# *Figuur 6.  Gemiddelde cijfers per groep op basis van Vak en Premaster voor de dataset Resultaten_SCM. De afkortingen staan voor de vakken Organizational Change Management (OC), Organizational Psychology (OP), Sustainable Innovation (SI) en de masterthesis (TH).*

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd statistics (2018). *Mixed ANOVA using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/mixed-anova-using-spss-statistics.php. 
# 
# [^2]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^3]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 86.
# [^4]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 54 - 55.
# [^5]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited. Pagina 84.
# [^6]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. 
# Sage. Pagina 458-460.
# [^7]: Laerd statistics (2018). *Testing for Normality using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php. 
# [^8]: Universiteit van Amsterdam (14 juli 2014). *Normaliteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).
# [^9]: De breedte van de staven van het histogram worden hier automatisch bepaald, maar kunnen handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^10]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. 
# Sage. Pagina 507-542.
# [^11]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# 
# [^16]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^17]: Outliers kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de outliers valide outliers zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van outliers kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde outliers te melden in een rapport. 
# [^18]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^21]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^22]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 591 - 622.
# 
