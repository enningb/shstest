#!/usr/bin/env python
# coding: utf-8
---
title: "Factoriële repeated measures ANOVA"
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


source(paste0(here::here(),"/01. Includes/data/30.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik de *factoriële repeated measures ANOVA* om te toetsen of de gemiddelden van groepen op basis van twee of meer onafhankelijke categorische variabelen van elkaar verschillen waarbij de deelnemers[^19] gemeten zijn voor elke categorie van de onafhankelijke variabelen (herhaalde metingen).[^1] De onafhankelijke variabelen zijn bij de *factoriële  repeated measures ANOVA* allemaal within-subjects variabelen.

# # Onderwijscasus
# <div id = "casus">
# 
# De opleidingsdirecteur van de bachelor Leisure Management van een hogeschool wil onderzoeken of de manier van toetsing invloed heeft op de resultaten van studenten in het eerste studiejaar. In het eerste studiejaar volgen de studenten in elke onderwijsperiode een theoretisch vak dat wordt afgesloten met een tentamen en een praktijkvak dat wordt afgesloten met een casus. Om het onderwijs te verbeteren wil de opleidingsdirecteur uitzoeken of er verschillen zijn tussen de vier onderwijsperiodes qua gemiddelde cijfers. Daarnaast is zij nieuwsgierig of er een verschil is tussen de becijfering van de theoretische en praktische vakken, en of deze verschillen afhangen van de onderwijsperiode.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is. Bij *factoriële repeated measures ANOVA* zijn er hypotheses op te stellen voor de verschillen tussen groepen van elke onafhankelijke variabele apart (hoofdeffecten) en een hypothese voor de interactie tussen twee of meerdere onafhankelijke variabelen (interactie-effect).
# 
# *H~0~*: Het gemiddelde cijfer is gelijk voor theoretische en praktijkvakken, i.e. er is geen hoofdeffect van Vaksoort op Gemiddeld cijfer.
# 
# *H~A~*: Het gemiddelde cijfer is niet gelijk voor theoretische en praktijkvakken, i.e. er is een hoofdeffect van Vaksoort op Gemiddeld cijfer.
# 
# *H~0~*: Het gemiddelde cijfer is gelijk in onderwijsperiode 1, 2, 3 en 4, i.e. er is geen hoofdeffect van Periode op Gemiddeld cijfer.
# 
# *H~A~*: Het gemiddelde cijfer is niet gelijk in onderwijsperiode 1, 2, 3 en 4, i.e. er is een hoofdeffect van Periode op Gemiddeld cijfer.
# 
# *H~0~*: Er is geen interactie-effect tussen de variabelen Vaksoort en Periode op het gemiddeld cijfer.
# 
# *H~A~*: Er is een interactie-effect tussen de variabelen Vaksoort en Periode op het gemiddeld cijfer.
# 
# </div>
# 
# # Within en between-subjects variabelen
# 
# Binnen de *ANOVA* familie zijn er verschillende soorten analyses die afhangen van het type onafhankelijke variabele dat wordt gebruikt. Een onafhankelijke variabele kan een between-subjects en within-subjects variabele zijn. Between-subjects houdt in dat elke categorie van de variabele andere deelnemers bevat; elke deelnemer zit slechts in één van de categoriëen. Een voorbeeld van een between-subjects variabele is Geslacht: de deelnemer zit in de categorie man of categorie vrouw en kan niet in beide zitten. Een within-subjects variabele kan op twee manieren ontworpen worden. De eerste manier is dat elke deelnemer in elke categorie zit doordat hij of zij in elke categorie gemeten is (herhaalde metingen). Een voorbeeld hiervan is de variabele onderwijsperiode: de deelnemer wordt in elke onderwijsperiode gemeten wat betreft zijn gemiddelde cijfer. De tweede manier is dat deelnemers in elke categorie aan elkaar gematcht worden. Dit betekent dat er op basis van achtergrondkenmerken deelnemers aan elkaar gekoppeld worden die erg op elkaar lijken. Een herhaalde meting wordt op deze manier als het ware nagebootst. Een voorbeeld hiervan is het matchen van studenten bij verschillende opleidingen op basis van kenmerken als geslacht, leeftijd, vooropleiding en gemiddeld eindexamencijfer middelbare school.
# 
# Het soort onafhankelijke variabelen bepaalt het type *ANOVA* dat gebruikt moet worden. Bij één between-subjects variabele is de [one-way ANOVA](05-One-way-ANOVA-R.html) de juiste toets en bij één within-subjects variabele is de [repeated measures ANOVA](04-Repeated-measures-ANOVA-R.html) de juiste toets. Bij meerdere variabelen wordt het iets complexer. Als alle variabelen between-subjects variabelen zijn is de [factoriële ANOVA](29-Factoriele-ANOVA-R.html) de juiste toets. Als alle variabelen within-subjects variabelen zijn, is de *factoriële repeated measures ANOVA* (de huidige toetspagina) de juiste toets. Als er een combinatie is van within-subjects en between-subjects variabelen, dan is de [mixed ANOVA](32-Mixed-ANOVA-R.html) de juiste toets. Bekijk dus van tevoren wat voor soort onafhankelijke variabelen worden gebruikt om de juiste toets te bepalen.
# 
# # Hoofdeffecten en interacties
# 
# Bij *factoriële repeated measures ANOVA* wordt onderzocht of er verschillen zijn tussen groepen die gemaakt worden op basis van meerdere categorische onafhankelijke variabelen met herhaalde metingen. Dit wordt toegelicht met een versimpelde vorm van de huidige casus met twee onafhankelijke variabelen Vaksoort en Periode en een afhankelijke variabele Cijfer. De onafhankelijke variabele Vaksoort bestaat uit twee groepen (theorie en praktijk) en de onafhankelijke variabele Periode bestaat ook uit twee groepen (1 en 2). Binnen *factoriële repeated measures ANOVA* wordt een onderscheid gemaakt tussen hoofdeffecten en interactie-effecten. Een hoofdeffect houdt in dat er een verschil is tussen de groepen van één van de onafhankelijke variabelen. In andere woorden, de onafhankelijke variabele heeft effect op de afhankelijke variabele. Voor het bedachte experiment houdt een hoofdeffect van de variabele Vaksoort in dat er een verschil is in het gemiddelde van groep theorie en groep praktijk. Een hoofdeffect van de variabele Periode houdt in dat er een verschil is in het gemiddelde van periode1 en peridoe 2.[^10]
# 
# Een grafische weergave van hoofdeffecten is te zien in Figuur 1. In de figuur is de relatie tussen de variabelen Periode en Cijfer weergegeven voor de vaksoorten theorie en praktijk. Het hoofdeffect van de variabele Periode is te zien door het gemiddelde van periode 1 te vergelijken met het gemiddelde van periode 2. Beide gemiddelden zijn weergegeven met groene driehoeken: periode 1 heeft een gemiddelde van 6 en periode 2 een gemiddelde van 8. Er is dus een verschil in gemiddelde tussen de groepen van onafhankelijke variabele Periode, wat betekent dat er een hoofdeffect van de variabele Periode is. Op dezelfde manier kan een mogelijk hoofdeffect van de variabele Vaksoort onderzocht worden. Het gemiddelde van groep theorie is weergegeven met een oranje vierkant en het gemiddelde van groep praktijk met een blauw vierkant. Het gemiddelde van groep praktijk (8) ligt hoger dan het gemiddelde van groep theorie (6), dus er is ook een hoofdeffect van onafhankelijke variabele Vaksoort. Beide onafhankelijke variabelen hebben dus een effect op de afhankelijke variabele Cijfer.
# 
# <!-- ## CLOSEDBLOK: Uitleg1.R -->

# In[ ]:


Periode <- c(1,3,1,3)
Vaksoort <- c("Theorie", "Theorie","Praktijk", "Praktijk")
Cijfer <- c(5,7,7,9)
dat <- cbind.data.frame(Periode,Vaksoort,Cijfer)
ggplot(dat, aes(x = Periode, y = Cijfer, group = Vaksoort, colour = Vaksoort)) + geom_line() + geom_point(size = 2) + scale_color_manual(values = c("deepskyblue","darkorange")) + scale_x_continuous(breaks = c(1,3), labels = c("1", "2")) + annotate("point", x = 2, y = 8, colour = "deepskyblue", fill = "deepskyblue", shape = 22, size = 3) + annotate("point", x = 2, y = 6, colour = "darkorange", fill = "darkorange", shape = 22, size = 3) + annotate("point", x = 1, y = 6, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) + annotate("point", x = 3, y = 8, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) 


# <!-- ## /CLOSEDBLOK: Uitleg1.R -->
# 
# *Figuur 1.  Illustratie van hoofdeffecten bij factoriële repeated measures ANOVA voor een casus met afhankelijke variabele Cijfer en onafhankelijke variabelen Vaksoort en Periode. In deze grafiek zijn er hoofdeffecten voor de variabelen Vaksoort en Periode, maar geen interactie-effecten.*
# 
# Een interactie-effect houdt in dat het effect van de ene onafhankelijke variabele op de afhankelijke variabele afhangt van de andere onafhankelijke variabele(n). Er is als het ware een interactie tussen de onafhankelijke variabelen die het effect op de afhankelijke variabele bepaalt. In het bedachte experiment zou dit betekenen dat het effect van onafhankelijke variabele Periode op Cijfer verschillend is voor de groepen theorie en praktijk. Een voorbeeld van dit interactie-effect is te zien in Figuur 2. In deze figuur is zichtbaar dat er bij de groep theorie geen verschil is tussen de periode 1 en 2 wat betreft het cijfer, maar dat er voor de groep praktijk wel een verschil is. Bij de groep praktijk is er in periode 2 een hoger gemiddeld cijfer (9) dan in periode 1 (7). Het effect van de onafhankelijke variabele Periode op Cijfer hangt af van de variabele Vaksoort, dus er is een interactie-effect van de variabelen Periode en Vaksoort op de afhankelijke variabele Cijfer.
# 
# <!-- ## CLOSEDBLOK: Uitleg2.R -->

# In[ ]:


Periode <- c(1,3,1,3)
Vaksoort <- c("Theorie", "Theorie","Praktijk", "Praktijk")
Cijfer <- c(6,6,7,9)
dat <- cbind.data.frame(Periode,Vaksoort,Cijfer)
ggplot(dat, aes(x = Periode, y = Cijfer, group = Vaksoort, colour = Vaksoort)) + geom_line() + geom_point(size = 2) + scale_color_manual(values = c("deepskyblue","darkorange")) + scale_x_continuous(breaks = c(1,3), labels = c("1", "2")) + annotate("point", x = 2, y = 8, colour = "deepskyblue", fill = "deepskyblue", shape = 22, size = 3) + annotate("point", x = 2, y = 6, colour = "darkorange", fill = "darkorange", shape = 22, size = 3) + annotate("point", x = 1, y = 6.5, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) + annotate("point", x = 3, y = 7.5, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) 


# <!-- ## /CLOSEDBLOK: Uitleg2.R -->
# 
# *Figuur 2.  Illustratie van interactie-effecten bij factoriële repeated measures ANOVA voor een casus met de afhankelijke variabele Cijfer en de onafhankelijke variabelen Vaksoort en Periode. In deze grafiek is er een interactie-effect van de onafhankelijke variabelen Vaksoort en Periode op de afhankelijke variabele Cijfer.*
# 
# In Figuur 1 waren er hoofdeffecten van de variabelen Vaksoort en Periode gevonden, maar was het interactie-effect nog niet onderzocht. In deze figuur is er geen sprake van een interactie-effect, omdat het effect van Periode op Cijfer hetzelfde is voor de groepen theorie en praktijk en dus niet afhangt van de variabele Vaksoort. Voor beide groepen (theorie en praktijk) is het verschil tussen periode 1 en 2 twee punten. Hier is dus geen sprake van een interactie-effect. Bij grafieken is er een interactie-effect als de twee (of meerdere) lijnen niet parallel lopen. Op deze manier kan snel onderzocht worden of er een interactie-effect is en wat de invloed van het interactie-effect is.
# 
# Bij *factoriële repeated measures ANOVA* worden bovenstaande grafieken gebruikt om de resultaten te interpreteren. De hoofdeffecten en interactie-effecten worden eerst statistisch getoetst en daarna geïnterpreteerd met onder andere deze grafieken. De aanpak is als volgt.[^10] Eerst wordt getoetst of er sprake is van een interactie-effect tussen de onafhankelijke variabelen. Als dit niet het geval is, kunnen de hoofdeffecten geïnterpreteerd worden. Als er wel een interactie-effect is, kunnen de hoofdeffecten niet geïnterpreteerd worden. De volgende stap is dan een *simple effects analyse* waarbij het effect van de ene onafhankelijke variabele op de afhankelijke variabele wordt getoetst voor alle groepen van de andere onafhankelijke variabele die deel uitmaakt van het interactie-effect. Voor Figuur 2 zou dit betekenen dat het effect van Periode op Gemiddeld_cijfer apart getoetst wordt voor de groepen theorie en praktijk van de variabele Vaksoort. Het interactie-effect kan op deze manier geïnterpreteerd worden, samen met de grafische weergave zoals te zien in Figuur 2.
# 
# # Uitleg assumpties
# 
# Voor een valide toetsresultaat bij de *factoriële repeated measures ANOVA* moet er aan een aantal assumpties voldaan worden. De steekproef moet bestaan uit onafhankelijke deelnemers, de afhankelijke variabele moet normaal verdeeld zijn voor elke combinatie van groepen van de onafhankelijke variabelen en er moet sphericiteit zijn.[^1] In deze sectie worden de assumpties allen toegelicht en worden de opties bij het niet voldoen aan de assumptie weergegeven. Verderop in de toetspagina worden de assumpties getoetst met de dataset van de onderwijscasus.
# 
# ## Normaliteit
# Controleer de assumptie van normaliteit voor elke groep met de volgende stappen:  
# 1. Controleer de data visueel met een histogram, een boxplot of een Q-Q plot.   
# 2. Toets of de data normaal verdeeld zijn met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (n < 50) met de *Shapiro-Wilk test*.[^7]<sup>, </sup>[^8]  
# 
# <!-- ## TEKSTBLOK: Link1.R -->
# De *factoriële repeated measures ANOVA* is redelijk robuust ten opzichte van een schending van de assumptie van normaliteit. Als er kleine afwijkingen zijn, heeft dat relatief kleine gevolgen voor de validiteit van de toets. Bij grotere afwijkingen is het transformeren van de afhankelijke variabele een optie.[^2] Als dit niet werkt, dan is het een optie om [Friedman's ANOVA](09-Friedmans-ANOVA-I-R.html). Dit is een nonparametrische versie van de *repeated measures ANOVA* en hoeft niet te voldoen aan de assumptie van normaliteit en sphericiteit. De *factoriële repeated measures ANOVA* heeft echter een hoger onderscheidend vermogen als aan alle assumpties is voldaan, dus in dat geval heeft deze toets de voorkeur.[^21]
# <!-- ## /TEKSTBLOK: Link1.R -->
# 
# ## Sphericiteit
# De assumptie van sphericiteit houdt in dat de variantie van de verschilscores tussen groepen ongeveer aan elkaar gelijk zijn.[^11] Bij een *repeated measures ANOVA* met meerdere onafhankelijke variabelen zijn er verschilscores te maken voor elke individuele onafhankelijke variabele en voor alle combinaties van interactie-effecten tussen de onafhankelijke variabelen. In de huidige casus zijn er voor de variabele Periode zes verschilscores te maken: periode 1 - periode 2, periode 1 - periode 3, periode 1 - periode 4, periode 2 - periode 3, periode 2 - periode 4 en periode 3 - periode 4. De variantie van deze zes verschilscores moet dus ongeveer gelijk zijn om aan de assumptie te voldoen.
# 
# Voor de variabele Vaksoort is er slechts één verschilscore (theorie - praktijk). Omdat er maar één verschilscore is, is de variantie per definitie gelijk voor alle verschilscores van deze variabele. Er is namelijk geen andere verschilscore om de variantie mee te vergelijken. Het interactie-effect tussen Vaksoort en Periode zorgt voor acht (4 perioden keer 2 vaksoorten) groepen op basis waarvan verschilscores zijn te maken voor alle combinaties van groepen. De variantie van al deze verschilscores moet ongeveer aan elkaar gelijk zijn.  
# 
# Toets deze assumptie met *Mauchly's test*. Als de onafhankelijke variabelen niet aan de assumptie voldoen, geeft de gewone *repeated measures ANOVA* een verkeerd resultaat. Er zijn echter correcties die gebruikt kunnen worden als er niet aan sphericiteit voldaan is. Een voorbeeld van mogelijke output van *Mauchly's test* in R voor de huidige toetspagina is hieronder weergegeven.
# 
# <!-- ## CLOSEDBLOK: Sphericiteit.R -->

# In[ ]:


cat("$ANOVA
            Effect DFn DFd           F            p p<.05         ges
2         Vaksoort   1 119 199.5442986 3.304785e-27     * 0.153803985
3          Periode   3 357  32.6506324 1.133681e-18     * 0.086040949
4 Vaksoort:Periode   3 357  12.17163   0.0538726     * 0.03945583

$`Mauchly's Test for Sphericity`
            Effect         W         p p<.05
3          Periode 0.9839122 0.8615531      
4 Vaksoort:Periode 0.9695177 0.0060169     * 

$`Sphericity Corrections`
            Effect       GGe        p[GG] p[GG]<.05      HFe        p[HF] p[HF]<.05
3          Periode 0.9892596 1.692938e-18         * 1.017342 1.133681e-18         *
4 Vaksoort:Periode 0.9787132 0.0553387              1.006161 0.0430724          ")


# <!-- ## /CLOSEDBLOK: Sphericiteit.R -->
# 
# <!-- ## TEKSTBLOK: Sphericiteit1.R -->
# 
# De output bestaat uit drie delen die zijn aangegeven met een dollarteken ($). Het eerste deel (ANOVA) bestaat uit het resultaat van de *factoriële repeated measures ANOVA* als er aan de assumptie van sphericiteit is voldaan. Het tweede deel van de output (Mauchly's Test for Sphericity) bestaat uit het resultaat van *Mauchly's test* voor de variabele Periode en de interactieterm tussen variabelen Vaksoort en Periode (`Vaksoort:Periode`). Het derde deel (Sphericity Corrections) bestaat uit de resultaten gecorrigeerd voor het feit dat er niet is voldaan aan de assumptie van sphericiteit.
# 
# Bij een p-waarde kleiner dan 0,05, toont *Mauchly's test* dat de assumptie van sphericiteit geschonden is. In de output is er voldaan aan de assumptie van sphericiteit voor de variabele Periode (*p* = 0,862). Voor deze onafhankelijke variabele hoeft er dus geen correctie gebruikt te worden en kan de output bij `$ANOVA` bekeken worden om de significantie te bepalen. Er is geen resultaat van *Mauchly's test* voor de variabele Vaksoort, omdat hier maar één verschilscore is en er dus per definitie aan de assumptie is voldaan. Voor de interactieterm moet dus een correctie gevonden worden. *Mauchly's test* laat ten slotte zien dat er niet voldaan is aan de assumptie van sphericiteit voor de interactieterm tussen Vaksoort en Periode (*p* = 0,006). 
# 
# Er zijn twee mogelijke correcties als er geen sphericiteit is: de Greenhouse-Geisser (GG) en Huynh-Feldt (HF) correctie. De Greenhouse-Geisser correctie staat bekend als conservatief, wat betekent dat de correctie een relatief lage kans op een type I fout heeft. In andere woorden, het zal niet vaak gebeuren dat deze correctie een significant effect aantoont als dat er in werkelijkheid niet is. De Huynh-Feldt correctie staat echter bekend als liberaal, wat betekent dat er een relatief hoge kans op een type I fout is. De toetsstatistiek en p-waarde van beide correcties zijn in de output te vinden onder Sphericity Corrections.
# <!-- ## TEKSTBLOK: Sphericiteit1.R -->
# 
# Houd de volgende richtlijnen aan bij het interpreteren van de *factoriële repeated measures ANOVA* als er niet aan sphericiteit is voldaan:
# 
# * Als beide correcties significant zijn, rapporteer de (conservatieve) Greenhouse-Geisser correctie.
# * Als beide correcties niet significant zijn, rapporteer de (liberale) Huynh-Feldt correctie.
# * Als de een significant is en de ander niet, bereken de gemiddelde p-waarde van beide correcties.
#     * Als deze p-waarde significant is, rapporteer dan de significante correctie.
#     * Als deze p-waarde niet significant is, rapporteer dan de niet significante correctie.
# 
# In de voorbeeldoutput is voor het interactie-effect tussen Vaksoort en Periode de p-waarde van de Greenhouse-Geisser correctie (`0.0553387`) groter dan 0,05 en de p-waarde van de Huynh-Feldt correctie (`0.0430724`) kleiner dan 0,05. Het gemiddelde van beide p-waarden is 0,0492056, wat betekent dat er een significant resultaat is. Rapporteer in dit geval dus de (significante) Huynh-Feldt correctie, i.e. *F* = 1,01, *p* = 0,049.  
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^11] Voor de *factoriële repeated measures ANOVA* wordt de effectmaat *partial eta squared* vaak gebruikt.[^4]
# 
# De effectmaat *partial eta squared* (partial *η^2^*) berekent de proportie van de onverklaarde variantie (variantie die niet door de andere variabelen wordt verklaard) in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele.[^4] Voor de variabele Vooropleiding geeft de partial eta squared dus de proportie verklaarde variantie weer van de variantie die niet verklaard is door de variabele Geslacht en de interactie tussen de variabelen Vooropleiding en Geslacht. De partial eta squared van alle termen van het model tellen dus niet per se op tot 1.[^4] Een indicatie om partial *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^5]
# 
# # Post-hoc toetsen
# 
# De eerste stap van de *factoriële repeated measures ANOVA* is het toetsen van hoofdeffecten en interactie-effecten. De volgende stap bestaat uit het bepalen welke groepen van elkaar verschillen, zowel bij *simple effects analyse* als bij het interpreteren van hoofdeffecten, en wordt gedaan met post-hoc toetsen. De post-hoc toetsen voeren meestal een correctie voor de p-waarden uit, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout. Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^11]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset ingeladen met de cijfers per periode per vaksoort voor eerstejaars studenten van de bachelor Leisure Management genaamd `Resultaten_Leisure_Management`. 
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
head(Resultaten_Leisure_Management)

## Laatste 5 observaties
tail(Resultaten_Leisure_Management)


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

with(Resultaten_Leisure_Management, 
     stby(data = Cijfers, 
          list(Vaksoort, Periode), 
          descr, 
          stats = c("mean", "sd", "med", "n.valid")))


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
# 
# Maak vervolgens een grafiek met de gemiddelden voor de verschillende groepen.
# 
# <!-- ## OPENBLOK: Data-beschrijven2.R -->

# In[ ]:


library(ggplot2)

ggplot(Resultaten_Leisure_Management, 
       aes(x = Periode, y = Cijfers, group = Vaksoort, colour = Vaksoort)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Vaksoort)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue")) 


# <!-- ## /OPENBLOK: Data-beschrijven2.R -->
# 
# *Figuur 3.  Gemiddelde cijfers per groep op basis van Vaksoort en Periode voor de dataset Resultaten_Leisure_Management.*
# 
# Op basis van de beschrijvende statistieken en de grafiek (Figuur 3) lijken er verschillen tussen de groepen te zijn. De praktijkvakken hebben in elke periode een hoger gemiddelde dan de theorievakken. In periode 1 en 2 is het verschil tussen beide soorten vakken een stuk groter dan in periode 3 en 4. Voor theorievakken is het cijfer in periode 3 en 4 een stuk hoger dan in periode 1 en 2, maar voor praktijkvakken is dit verschil niet groot. De lijnen van de vaksoorten theorie en praktijk lopen niet parallel dus er lijkt een interactie-effect te zijn. De *factoriële repeated measures ANOVA* zal dit interactie-effect toetsen.
# 
# ## Normaliteit
# 
# De *factoriële repeated measures ANOVA* vereist dat de verdeling van de afhankelijke variabele de normale verdeling benaderd in elke groep die gevormd wordt door de onafhankelijke variabelen. Toets deze assumptie met behulp van een histogram en de *Kolmogorov-Smirnov* en *Shapiro-Wilk test*.
# 
# ### Histogram
# 
# Visualiseer de verdeling van de gemiddelde cijfers binnen elke groep met behulp van een histogram.[^9] Focus bij het analyseren van een histogram op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke outliers. Een normale verdeling is symmetrisch, heeft één top en geen outliers.[^16]<sup>, </sup>[^17]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot
ggplot(Resultaten_Leisure_Management,
  aes(x = Cijfers)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 0.5,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Periode + Vaksoort) +
  geom_density(alpha = .2, adjust = 1) +
  ylab("Cijfer")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# *Figuur 4.  Histogrammen van de verdelingen van de gemiddelde cijfers per groep op basis van Vaksoort en Periode.*
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

with(Resultaten_Leisure_Management, 
     by(data = Cijfers, 
        list(Vaksoort, Periode), 
        lillie.test))


# <!-- ## /OPENBLOK: KStest.R -->
# 
# De p-waarde is groter dan 0,05 voor elke groep; er zijn dus geen significante verschillen gevonden tussen de verdelingen van de steekproef en de normale verdeling. De *factoriële repeated measures ANOVA* kan uitgevoerd worden.
# 
# #### Shapiro-Wilk test
# De *Shapiro-Wilk test* is een soortgelijke toets als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (*n* < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.[^18]
# 
# <!-- ## OPENBLOK: Shapiro-Wilk-test.R -->

# In[ ]:


with(Resultaten_Leisure_Management, 
     by(data = Cijfers, 
        list(Vaksoort, Periode), 
        shapiro.test))


# <!-- ## /OPENBLOK: Shapiro-Wilk-test.R -->
# 
# De p-waarde is groter dan 0,05 voor elke groep; er zijn dus geen significante verschillen gevonden tussen de verdelingen van de steekproef en de normale verdeling. De *factoriële repeated measures ANOVA* kan uitgevoerd worden.
# 
# ## Sphericiteit
# 
# <!-- ## TEKSTBLOK: LeveneTest1.R -->
# Toets met *Mauchly's test* de assumptie van sphericiteit. Gebruik de functie `ezANOVA()$Mauchly's Test for Sphericity` van het package `ez` met als argumenten de dataset `Resultaten_Leisure_Management`, de afhankelijke variabele `dv = Cijfers`, de variabele die de deelnemers aangeeft `wid = Studentnummer` en de onafhankelijke variabelen `within = list(Vaksoort, Periode)`.
# <!-- ## /TEKSTBLOK: LeveneTest1.R -->
# 
# <!-- ## OPENBLOK: Levenes-test.R -->

# In[ ]:


library(ez)

ezANOVA(Resultaten_Leisure_Management, 
        dv = Cijfers, 
        wid = Studentnummer,
        within = list(Vaksoort, Periode))$`Mauchly's Test for Sphericity`


# <!-- ## /OPENBLOK: Levenes-test.R -->
# 
# <!-- ## CLOSEDBLOK: Levenes-test.R -->

# In[ ]:



obj <- ezANOVA(Resultaten_Leisure_Management, 
        dv = Cijfers, 
        wid = Studentnummer,
        within = list(Vaksoort, Periode))$`Mauchly's Test for Sphericity`

Mauchly_W_Periode <- Round_and_format(obj$W[1])
Mauchly_W_Int <- Round_and_format(obj$W[2])
p_Periode <- Round_and_format(obj$p[1])
p_Int <- Round_and_format(obj$p[2])


# <!-- ## /CLOSEDBLOK: Levenes-test.R -->
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# * Voor de onafhankelijke variabele Periode is er voldaan aan de assumptie van sphericiteit, *W* = `r Mauchly_W_Periode`, *p* = `r p_Periode`[^18]
# * Voor de interactieterm van Periode en Vaksoort is er voldaan aan de assumptie van sphericiteit, *W* = `r Mauchly_W_Int`, *p* = `r p_Int`
# * Er hoeft in beide gevallen geen correctie uitgevoerd te worden voor de *factoriële repeated measures ANOVA*
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# 
# # Factoriële repeated measures ANOVA 
# 
# <!-- ## TEKSTBLOK: ANOVA-toets.R -->
# Voer de *factoriële repeated measures ANOVA* uit om de vraag te beantwoorden of er verschillen zijn tussen theorie- en praktijkvakken en tussen de vier onderwijsperioden wat betreft de cijfers van eerstejaars studenten van de bachelor Leisure Management. Gebruik de functie `ezANOVA()` van het package `ez` met als argumenten de dataset `Resultaten_Leisure_Management`, de afhankelijke variabele `dv = Cijfers`, de variabele die de deelnemers aangeeft `wid = Studentnummer` en de onafhankelijke variabelen `within = list(Vaksoort, Periode)`.
# <!-- ## /TEKSTBLOK: ANOVA-toets.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets.R -->

# In[ ]:


library(ez)

ezANOVA(Resultaten_Leisure_Management, 
        dv = Cijfers, 
        wid = Studentnummer,
        within = list(Vaksoort, Periode))


# <!-- ## /OPENBLOK: ANOVA-toets.R -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets4.R -->

# In[ ]:


FRM <- ezANOVA(Resultaten_Leisure_Management, 
        dv = Cijfers, 
        wid = Studentnummer,
        within = list(Vaksoort, Periode))$ANOVA

vF_waarde <- Round_and_format(FRM$F[3])
vDF1 <- Round_and_format(FRM$DFn[3])
vDF2 <- Round_and_format(FRM$DFd[3])
vEsq <- Round_and_format(FRM$ges[3])


# <!-- ## /CLOSEDBLOK: ANOVA-toets4.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets5.R -->
# 
# * Er is een significant interactie-effect van Vaksoort en Periode op Cijfers, *F* (`r vDF1`,`r vDF2`) = `r vF_waarde`, *p* < 0,0001, *η^2^* = `r vEsq`.
# * De p-waarde is kleiner dan 0,05, dus de nulhypothese dat er geen interactie-effect is wordt verworpen.[^18] 
# * Er is een klein tot gemiddeld effect van de interactie tussen Vaksoort en Periode op Cijfers
# * Omdat er een significant interactie-effect is, hoeven de hoofdeffecten niet geïnterpreteerd te worden. De volgende stap is een *simple effects analyse* om te interactie verder te onderzoeken.
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets5.R -->
# 
# ## Simple effects analyse
# 
# Voer een *simple effects analyse* uit om het interactie-effect te interpreteren. Vergelijk eerst de verschillen tussen de vier onderwijsperioden voor elke categorie van de variabele Vaksoort (theorie- en praktijkvakken dus). Vergelijk daarna de verschillen tussen theorie- en praktijkvakken voor elke onderwijsperiode.
# 
# ### Periode
# 
# <!-- ## TEKSTBLOK: SimEff1.R -->
# Maak eerst een aparte dataset voor de groepen theorie en praktijk, voer vervolgens de post-hoc toets uit en bereken de gemiddelden per onderwijsperiode. Gebruik voor de post-hoc toetsen de functie `pairwise.t.test()` met als argumenten de afhankelijk variabele `Theorie_Resultaten_Leisure_Management$Cijfers`, de onafhankelijke variabele `Theorie_Resultaten_Leisure_Management$Periode`, het argument `paired = TRUE` omdat er een gepaarde vergelijking gemaakt wordt  en de gebruikte methode om te corrigeren voor meerdere toetsen `p.adjust.method = "bonferroni"`.
# <!-- ## /TEKSTBLOK: SimEff1.R -->
# 
# <!-- ## OPENBLOK: SimEff2.R -->

# In[ ]:


# Maak een dataset met theorievakken en een dataset met praktijkvakken
Theorie_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Vaksoort == "Theorie",]

Praktijk_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Vaksoort == "Praktijk",]

# Voer de post-hoc toetsen uit
pairwise.t.test(Theorie_Resultaten_Leisure_Management$Cijfers,
                Theorie_Resultaten_Leisure_Management$Periode,
                paired = TRUE,
                p.adjust.method = "bonferroni")

pairwise.t.test(Praktijk_Resultaten_Leisure_Management$Cijfers,
                Praktijk_Resultaten_Leisure_Management$Periode,
                paired = TRUE,
                p.adjust.method = "bonferroni")

# Bereken het gemiddelde per groep voor beide datasets
with(Theorie_Resultaten_Leisure_Management, 
     by(data = Cijfers, 
        list(Periode), 
        mean))

with(Praktijk_Resultaten_Leisure_Management, 
     by(data = Cijfers, 
        list(Periode), 
        mean))


# <!-- ## /OPENBLOK: SimEff2.R -->
# 
# <!-- ## CLOSEDBLOK: SimEff3.R -->
# ````{r, echo=FALSE}
# # Maak een dataset met theorievakken en een dataset met praktijkvakken
# Theorie_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Vaksoort == "Theorie",]
# 
# Praktijk_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Vaksoort == "Praktijk",]
# 
# # Voer de post-hoc toetsen uit
# Posthoc_Periode_Theorie <- pairwise.t.test(Theorie_Resultaten_Leisure_Management$Cijfers,
#                 Theorie_Resultaten_Leisure_Management$Periode,
#                 paired = TRUE,
#                 p.adjust.method = "bonferroni")$p.value
# 
# Posthoc_Periode_Praktijk <- pairwise.t.test(Praktijk_Resultaten_Leisure_Management$Cijfers,
#                 Praktijk_Resultaten_Leisure_Management$Periode,
#                 paired = TRUE,
#                 p.adjust.method = "bonferroni")$p.value
# 
# # Bereken het gemiddelde per groep voor beide datasets
# Mean_T <- with(Theorie_Resultaten_Leisure_Management, 
#      by(data = Cijfers, 
#         list(Periode), 
#         mean))
# 
# Mean_P <- with(Praktijk_Resultaten_Leisure_Management, 
#      by(data = Cijfers, 
#         list(Periode), 
#         mean))
# 
# ```
# <!-- ## /CLOSEDBLOK: SimEff3.R -->
# 
# <!-- ## TEKSTBLOK: SimEff4.R -->
# Voor de theorievakken  zijn de volgende vergelijkingen getoetst[^18]:
# 
# * Onderwijsperiode 1 versus 2: het gemiddelde cijfer in periode 1 (`r Round_and_format(Mean_T[1])`) en periode 2 (`r Round_and_format(Mean_T[2])`) zijn niet significant verschillend (*p* = 1,00)
# * Onderwijsperiode 1 versus 3: het gemiddelde cijfer in periode 1 (`r Round_and_format(Mean_T[1])`) en periode 3 (`r Round_and_format(Mean_T[3])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 1 versus 4: het gemiddelde cijfer in periode 1 (`r Round_and_format(Mean_T[1])`) en periode 4 (`r Round_and_format(Mean_T[4])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 2 versus 3: het gemiddelde cijfer in periode 2 (`r Round_and_format(Mean_T[2])`) en periode 3 (`r Round_and_format(Mean_T[3])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 2 versus 4: het gemiddelde cijfer in periode 2 (`r Round_and_format(Mean_T[2])`) en periode 4 (`r Round_and_format(Mean_T[4])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 3 versus 4: het gemiddelde cijfer in periode 3 (`r Round_and_format(Mean_T[3])`) en periode 4 (`r Round_and_format(Mean_T[4])`) zijn niet significant verschillend (*p* = 1,00)

# Voor de praktijkvakken zijn de volgende vergelijkingen getoetst[^18]:
# 
# * Onderwijsperiode 1 versus 2: het gemiddelde cijfer in periode 1 (`r Round_and_format(Mean_P[1])`) en periode 2 (`r Round_and_format(Mean_P[2])`) zijn niet significant verschillend (*p* = 1,00)
# * Onderwijsperiode 1 versus 3: het gemiddelde cijfer in periode 1 (`r Round_and_format(Mean_P[1])`) en periode 3 (`r Round_and_format(Mean_P[3])`) zijn niet significant verschillend (*p* = `r Round_and_format(Posthoc_Periode_Praktijk[2,1],3)`)
# * Onderwijsperiode 1 versus 4: het gemiddelde cijfer in periode 1 (`r Round_and_format(Mean_P[1])`) en periode 4 (`r Round_and_format(Mean_P[4])`) zijn niet significant verschillend (*p* = 1,00)
# * Onderwijsperiode 2 versus 3: het gemiddelde cijfer in periode 2 (`r Round_and_format(Mean_P[2])`) en periode 3 (`r Round_and_format(Mean_P[3])`) zijn niet significant verschillend (*p* = `r Round_and_format(Posthoc_Periode_Praktijk[2,2],3)`)
# * Onderwijsperiode 2 versus 4: het gemiddelde cijfer in periode 2 (`r Round_and_format(Mean_P[2])`) en periode 4 (`r Round_and_format(Mean_P[4])`) zijn niet significant verschillend (*p* = 1,00)
# * Onderwijsperiode 3 versus 4: het gemiddelde cijfer in periode 3 (`r Round_and_format(Mean_P[3])`) en periode 4 (`r Round_and_format(Mean_P[4])`) zijn niet significant verschillend (*p* = `r Round_and_format(Posthoc_Periode_Praktijk[3,3],3)`)
# 
# <!-- ## /TEKSTBLOK: SimEff4.R -->
# 
# ### Vaksoort
# 
# <!-- ## TEKSTBLOK: SimEff5.R -->
# Maak eerst aparte datasets voor periode 1, 2, 3 en 4 en voer vervolgens de post-hoc toets uit. Gebruik voor de post-hoc toetsen de functie `pairwise.t.test()` met als argumenten de afhankelijk variabele `P1_Resultaten_Leisure_Management$Cijfers`, de onafhankelijke variabele `P1_Resultaten_Leisure_Management$Vaksoort`, het argument `paired = TRUE` omdat er een gepaarde vergelijking gemaakt wordt  en de gebruikte methode om te corrigeren voor meerdere toetsen `p.adjust.method = "bonferroni"`.
# <!-- ## /TEKSTBLOK: SimEff5.R -->
# 
# <!-- ## OPENBLOK: SimEff6.R -->

# In[ ]:


# Maak een dataset voor elke onderwijsperiode
P1_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Periode == "1",]

P2_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Periode == "2",]

P3_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Periode == "3",]

P4_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Periode == "4",]

# voer de post-hoc toetsen uit
pairwise.t.test(P1_Resultaten_Leisure_Management$Cijfers,
                P1_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")

pairwise.t.test(P2_Resultaten_Leisure_Management$Cijfers,
                P2_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")

pairwise.t.test(P3_Resultaten_Leisure_Management$Cijfers,
                P3_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")

pairwise.t.test(P4_Resultaten_Leisure_Management$Cijfers,
                P4_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")

# Bereken het gemiddelde per groep
with(Resultaten_Leisure_Management, 
     by(data = Cijfers, 
        list(Periode, Vaksoort), 
        mean))


# <!-- ## /OPENBLOK: SimEff6.R -->
# 
# <!-- ## CLOSEDBLOK: SimEff7.R -->

# In[ ]:


# Maak een dataset met theorievakken en een dataset met praktijkvakken
P1_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Periode == "1",]

P2_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Periode == "2",]

P3_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Periode == "3",]

P4_Resultaten_Leisure_Management <- Resultaten_Leisure_Management[Resultaten_Leisure_Management$Periode == "4",]

# voer de post-hoc toetsen uit
posthoc_P1 <- pairwise.t.test(P1_Resultaten_Leisure_Management$Cijfers,
                P1_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")$p.value

posthoc_P2 <- pairwise.t.test(P2_Resultaten_Leisure_Management$Cijfers,
                P2_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")$p.value

posthoc_P3 <- pairwise.t.test(P3_Resultaten_Leisure_Management$Cijfers,
                P3_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")$p.value

posthoc_P4 <- pairwise.t.test(P4_Resultaten_Leisure_Management$Cijfers,
                P4_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")$p.value

# Bereken het gemiddelde per groep voor beide datasets
Mean_Vaksoort <- with(Resultaten_Leisure_Management, 
     by(data = Cijfers, 
        list(Periode, Vaksoort), 
        mean))


# <!-- ## /CLOSEDBLOK: SimEff7.R -->
# 
# <!-- ## TEKSTBLOK: SimEff8.R -->
# * Onderwijsperiode 1: het gemiddelde cijfer voor het theorievak (`r Round_and_format(Mean_Vaksoort[1,2])`) en voor het praktijkvak (`r Round_and_format(Mean_Vaksoort[1,1])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 2: het gemiddelde cijfer voor het theorievak (`r Round_and_format(Mean_Vaksoort[2,2])`) en voor het praktijkvak (`r Round_and_format(Mean_Vaksoort[2,1])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 3: het gemiddelde cijfer voor het theorievak (`r Round_and_format(Mean_Vaksoort[3,2])`) en voor het praktijkvak (`r Round_and_format(Mean_Vaksoort[3,1])`) zijn niet significant verschillend (*p* = `r Round_and_format(posthoc_P3,3)`)
# * Onderwijsperiode 4: het gemiddelde cijfer voor het theorievak (`r Round_and_format(Mean_Vaksoort[4,2])`) en voor het praktijkvak (`r Round_and_format(Mean_Vaksoort[4,1])`) zijn niet significant verschillend (*p* = `r Round_and_format(posthoc_P4,3)`)
# 
# <!-- ## /TEKSTBLOK: SimEff8.R -->

# ## Illustratie van post-hoc toetsing bij hoofdeffecten zonder interactie-effect
# 
# <!-- ## TEKSTBLOK: PHtest1.R -->
# In de huidige casus worden de hoofdeffecten niet geïnterpreteerd vanwege het significante interactie-effect. Om toch te illustreren hoe het interpreteren van hoofdeffecten zonder een significant interactie-effect werkt, wordt de bijbehorende post-hoc toetsing toch geïllustreerd. Hiervoor wordt  een nieuwe dataset `Hoofdeffecten_Resultaten_Leisure_Management` gebruikt. 
# 
# <!-- ## /TEKSTBLOK: PHtest1.R -->
# 
# <!-- ## OPENBLOK: PHtest2.R -->

# In[ ]:


library(ez)

ezANOVA(Hoofdeffecten_Resultaten_Leisure_Management, 
        dv = Cijfers, 
        wid = Studentnummer,
        within = list(Vaksoort, Periode))


# <!-- ## /OPENBLOK: PHtest2.R -->
# 
# <!-- ## CLOSEDBLOK: PHtest3.R -->

# In[ ]:



FRM_H <- ezANOVA(Hoofdeffecten_Resultaten_Leisure_Management, 
        dv = Cijfers, 
        wid = Studentnummer,
        within = list(Vaksoort, Periode))$ANOVA

vF_waarde_H <- Round_and_format(FRM_H$F[3])
vDF1_H <- Round_and_format(FRM_H$DFn[3])
vDF2_H <- Round_and_format(FRM_H$DFd[3])
vEsq_H <- Round_and_format(FRM_H$ges[3])
vp_H <- Round_and_format(FRM_H$p[3])


# <!-- ## /CLOSEDBLOK: PHtest3.R -->

# <!-- ## TEKSTBLOK: PHtest4.R -->
# Er is geen significant interactie-effect van Vaksoort en Periode op Cijfers, *F* (`r vDF1_H`,`r vDF2_H`) = `r vF_waarde_H`, *p* = `vp_H`, *η^2^* = `r vEsq_H`.[^18] De hoofdeffecten van Vaksoort (*p* < 0,0001) en Periode (*p* < 0,0001) zijn wel significant.[^18] Voer daarom post-hoc toetsen uit voor beide variabelen. 
# 
# Gebruik voor de post-hoc toetsen de functie `pairwise.t.test()` met als argumenten de afhankelijk variabele `Hoofdeffecten_Resultaten_Leisure_Management$Cijfers`, de onafhankelijke variabele `Hoofdeffecten_Resultaten_Leisure_Management$Vaksoort` of `Hoofdeffecten_Resultaten_Leisure_Management$Periode`, het argument `paired = TRUE` omdat er een gepaarde vergelijking gemaakt wordt en de gebruikte methode om te corrigeren voor meerdere toetsen `p.adjust.method = "bonferroni"`.
# 
# <!-- ## /TEKSTBLOK: PHtest4.R -->
# 
# <!-- ## OPENBLOK: PHtest5.R -->

# In[ ]:


# Voer de post-hoc toetsen uit voor de variabele Vaksoort
pairwise.t.test(Hoofdeffecten_Resultaten_Leisure_Management$Cijfers,
                Hoofdeffecten_Resultaten_Leisure_Management$Vaksoort,
                paired = TRUE,
                p.adjust.method = "bonferroni")

# Bereken het gemiddelde cijfer voor beide vaksoorten
with(Hoofdeffecten_Resultaten_Leisure_Management, 
     by(data = Cijfers, 
        list(Vaksoort), 
        mean))

# Voer de post-hoc toetsen uit voor de variabele Periode
pairwise.t.test(Hoofdeffecten_Resultaten_Leisure_Management$Cijfers,
                Hoofdeffecten_Resultaten_Leisure_Management$Periode,
                paired = TRUE,
                p.adjust.method = "bonferroni")

# Bereken het gemiddelde cijfer voor de vier perioden
with(Hoofdeffecten_Resultaten_Leisure_Management, 
     by(data = Cijfers, 
        list(Periode), 
        mean))


# <!-- ## /OPENBLOK: PHtest5.R -->
# 
# <!-- ## CLOSEDBLOK: PHtest6.R -->
# ````{r, echo=FALSE}
# PH_Vaksoort <- pairwise.t.test(Hoofdeffecten_Resultaten_Leisure_Management$Cijfers,
#                 Hoofdeffecten_Resultaten_Leisure_Management$Vaksoort,
#                 paired = TRUE,
#                 p.adjust.method = "bonferroni")$p.value
# 
# PH_Periode <- pairwise.t.test(Hoofdeffecten_Resultaten_Leisure_Management$Cijfers,
#                 Hoofdeffecten_Resultaten_Leisure_Management$Periode,
#                 paired = TRUE,
#                 p.adjust.method = "bonferroni")$p.value
# 
# # Bereken het gemiddelde cijfer voor beide vaksoorten
# H_mean_Vaksoort <- with(Hoofdeffecten_Resultaten_Leisure_Management, 
#      by(data = Cijfers, 
#         list(Vaksoort), 
#         mean))
# 
# # Bereken het gemiddelde cijfer voor de vier perioden
# H_mean_Periode <- with(Hoofdeffecten_Resultaten_Leisure_Management, 
#      by(data = Cijfers, 
#         list(Periode), 
#         mean))
# 
# ```
# <!-- ## /CLOSEDBLOK: PHtest6.R -->
# 
# <!-- ## TEKSTBLOK: PHtest7.R -->
# De verschillen voor de groepen van de onafhankelijke variabele Vaksoort zijn[^18]:
# 
# * Het gemiddelde cijfer voor het theorievak (`r Round_and_format(H_mean_Vaksoort[2])`) en voor het praktijkvak (`r Round_and_format(H_mean_Vaksoort[1])`) zijn significant verschillend (*p* < 0,0001)
# 
# De verschillen voor de groepen van de onafhankelijke variabele Periode zijn[^18]:
# 
# * Onderwijsperiode 1 versus 2: het gemiddelde cijfer in periode 1 (`r Round_and_format(H_mean_Periode[1])`) en periode 2 (`r Round_and_format(H_mean_Periode[2])`) zijn niet significant verschillend (*p* = 1,00)
# * Onderwijsperiode 1 versus 3: het gemiddelde cijfer in periode 1 (`r Round_and_format(H_mean_Periode[1])`) en periode 3 (`r Round_and_format(H_mean_Periode[3])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 1 versus 4: het gemiddelde cijfer in periode 1 (`r Round_and_format(H_mean_Periode[1])`) en periode 4 (`r Round_and_format(H_mean_Periode[4])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 2 versus 3: het gemiddelde cijfer in periode 2 (`r Round_and_format(H_mean_Periode[2])`) en periode 3 (`r Round_and_format(H_mean_Periode[3])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 2 versus 4: het gemiddelde cijfer in periode 2 (`r Round_and_format(H_mean_Periode[2])`) en periode 4 (`r Round_and_format(H_mean_Periode[4])`) zijn significant verschillend (*p* < 0,0001)
# * Onderwijsperiode 3 versus 4: het gemiddelde cijfer in periode 3 (`r Round_and_format(H_mean_Periode[3])`) en periode 4 (`r Round_and_format(H_mean_Periode[4])`) zijn niet significant verschillend (*p* = 1,00)
# 
# <!-- ## /TEKSTBLOK: PHtest7.R -->
# 
# Visualiseer de gemiddelden per groep om de resultaten ook visueel weer te geven. In de grafiek in Figuur 5 is te zien dat de lijnen redelijk parallel lopen wat overeenkomt met het feit dat er geen significant interactie-effect is. Het hoofdeffect van de variabele Vaksoort is duidelijk zichtbaar: de gemiddeldes van de praktijkvakken liggen voor alle onderwijsperioden hoger dan de gemiddeldes van de theorievakken. Dit komt overeen met de significante verschillen voor elke periode tussen beide groepen op de post-hoc toets. Het hoofdeffect van de variabele Periode is ook zichtbaar. De gemiddeldes van periode 1 en 2 verschillen niet veel van elkaar, net zoals de gemiddeldes van periode 3 en 4. De gemiddelde cijfers in periode 3 en 4 zijn echter een stuk hoger dan de gemiddelde cijfers in periode 1 en 2, wat ook bevestigd wordt door de significante post-hoc toetsen voor deze vergelijkingen.
# 
# <!-- ## OPENBLOK: PHtest8.R -->

# In[ ]:


library(ggplot2)

ggplot(Hoofdeffecten_Resultaten_Leisure_Management, 
       aes(x = Periode, y = Cijfers, group = Vaksoort, colour = Vaksoort)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Vaksoort)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue")) 


# <!-- ## /OPENBLOK: PHtest8.R -->
# 
# *Figuur 5.  Gemiddelde cijfers per groep op basis van Vaksoort en Periode voor de dataset Hoofdeffecten_Resultaten_Leisure_Management.*
# 
# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *factoriële repeated measures ANOVA* is uitgevoerd om te toetsen of er verschillen zijn tussen theorie- en praktijkvakken en tussen de vier onderwijsperioden wat betreft de cijfers van eerstejaars studenten van de bachelor Leisure Management. De resultaten lieten zien dat er een significant interactie-effect was tussen Vaksoort en Periode op de gemiddelde cijfers van de studenten, *F* (`r vDF1`,`r vDF2`) = `r vF_waarde`, *p* < 0,0001, *η^2^* = `r vEsq`. 
# 
# Om dit effect verder te onderzoeken, is er een *simple effects analyse* uitgevoerd met behulp van post-hoc toetsen met een Bonferroni-correctie voor meerdere toetsen. Uit deze analyse bleek dat de gemiddelde cijfers voor theorievakken alleen in periode 1 en 2 significant lager zijn dan de gemiddelde cijfers van de praktijkvakken. In periode 3 en 4 zijn er geen significante verschillen tussen beide vaksoorten. Ook zijn er voor praktijkvakken geen significante verschillen tussen de gemiddelde cijfers van de vier perioden. Voor de theorievakken zijn de gemiddelde cijfers in periode 1 en 2 significant lager in vergelijking tot de gemiddelde cijfers in periode 3 en 4. De gemiddelde cijfers verschillen niet significant tussen periode 1 en 2 en tussen periode 3 en 4 voor theorievakken. In Figuur 6 zijn de gemiddeldes voor alle groepen weergegeven om de resultaten te ondersteunen.
# 
# Samenvattend suggereren de resultaten dat er in periode 1 en 2 hogere cijfers worden gehaald voor de praktijkvakken, maar dat dit verschil er niet meer is in periode 3 en 4.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Rapportage2.R -->

# In[ ]:


library(ggplot2)

ggplot(Resultaten_Leisure_Management, 
       aes(x = Periode, y = Cijfers, group = Vaksoort, colour = Vaksoort)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Vaksoort)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue")) 


# <!-- ## /CLOSEDBLOK: Rapportage2.R -->
# 
# *Figuur 6.  Gemiddelde cijfers per groep op basis van Vaksoort en Periode voor de dataset Resultaten_Leisure_Management.*

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd statistics (2018). *Two-way repeated measures ANOVA using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/two-way-repeated-measures-anova-using-spss-statistics.php. 
# 
# 

# [^2]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^3]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 86.
# [^4]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 54 - 55.
# [^5]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited. Pagina 84.
# [^6]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. 
# Sage. Pagina 458-460.
# [^7]: Laerd statistics (2018). *Testing for Normality using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php. 
# [^8]: Universiteit van Amsterdam (14 juli 2014). *Normaliteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).
# [^9]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^10]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. 
# Sage. Pagina 507-542.
# [^11]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# 
# [^16]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^17]: Outliers kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de outliers valide outliers zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van outliers kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde outliers te melden in een rapport. 
# [^18]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# 
# [^21]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# 
# 
