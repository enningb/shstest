#!/usr/bin/env python
# coding: utf-8
---
title: "Factoriële ANOVA"
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


source(paste0(here::here(),"/01. Includes/data/29.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik de *factoriële ANOVA* bij het toetsen of de gemiddelden van groepen op basis van twee of meer onafhankelijke categorische variabelen van elkaar verschillen.[^1] 
# 
# # Onderwijscasus
# <div id = "casus">
# Bij de bacheloropleiding Psychologie van een universiteit is besloten om naast studenten met een vwo-opleiding studenten met een propedeuse voor de hbo-opleiding Psychologie ook toe te laten. De opleidingsdirecteur van de bachelor wil graag evalueren of deze hbo-p studenten het niveau van de opleiding aankunnen, maar is ook benieuwd of man-vrouw verschillen hierbij een rol spelen. Daarom vergelijkt zij de verschillen in het gemiddeld cijfer van het eerste studiejaar voor studenten met een hbo-p vooropleiding, vwo vooropleiding en overige vooropleidingen en of dit verschillend is voor mannen en vrouwen.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is. Bij *factoriële ANOVA* zijn er hypotheses op te stellen voor de verschillen tussen groepen van elke onafhankelijke variabele apart (hoofdeffecten) en een hypothese voor de interactie tussen twee of meerdere onafhankelijke variabelen (interactie-effect).
# 
# *H~0~*: Het gemiddelde cijfer is gelijk voor mannen en vrouwen, i.e. er is geen hoofdeffect van Geslacht op Gemiddeld_cijfer.
# 
# *H~A~*: Het gemiddelde cijfer is niet gelijk voor mannen en vrouwen, i.e. er is een hoofdeffect van Geslacht op Gemiddeld_cijfer.
# 
# *H~0~*: Het gemiddelde cijfer is gelijk voor studenten met een hbo-p, vwo en overige vooropleiding, i.e. er is geen hoofdeffect van Vooropleiding op Gemiddeld_cijfer.
# 
# *H~A~*: Het gemiddelde cijfer is niet gelijk voor studenten met een hbo-p, vwo en overige vooropleiding, i.e. er is een hoofdeffect van Vooropleiding op Gemiddeld_cijfer.
# 
# *H~0~*: Er is geen interactie-effect tussen de variabelen Geslacht en Vooropleiding op het gemiddelde cijfer.
# 
# *H~A~*: Er is een interactie-effect tussen de variabelen Geslacht en Vooropleiding op het gemiddelde cijfer.
# 
# </div>

# # Hoofdeffecten en interacties
# 
# Bij *factoriële ANOVA* wordt onderzocht of er verschillen zijn tussen groepen die gemaakt worden op basis van meerdere categorische onafhankelijke variabelen. Dit wordt toegelicht met een versimpelde vorm van de huidige casus met twee onafhankelijke variabelen Vooropleiding en Geslacht en een afhankelijke variabele Gemiddeld_cijfer. De onafhankelijke variabele Vooropleiding bestaat uit twee groepen (hbo-p en vwo) en de onafhankelijke variabele Geslacht bestaat ook uit twee groepen (man en vrouw). Binnen *factoriële ANOVA* wordt een onderscheid gemaakt tussen hoofdeffecten en interactie-effecten. Een hoofdeffect houdt in dat er een verschil is tussen de groepen van één van de onafhankelijke variabelen. In andere woorden, de onafhankelijke variabele heeft effect op de afhankelijke variabele. Voor het bedachte experiment houdt een hoofdeffect van de variabele Vooropleiding in dat er een verschil is in het gemiddelde van groep hbo-p en groep vwo. Een hoofdeffect van de variabele Geslacht houdt in dat er een verschil is in het gemiddelde van groep man en groep vrouw.[^10]
# 
# Een grafische weergave van hoofdeffecten is te zien in Figuur 1. In de figuur is de relatie tussen de variabelen Vooropleiding en Gemiddeld_cijfer weergegeven voor mannen en vrouwen. Het hoofdeffect van de variabele Vooropleiding is te zien door het gemiddelde van groep hbo-p te vergelijken met het gemiddelde van groep vwo. Beide gemiddelden zijn weergegeven met groene driehoeken: groep hbo-p heeft een gemiddelde van 6 en groep vwo een gemiddelde van 8. Er is dus een verschil in gemiddelde tussen de groepen van onafhankelijke variabele Vooropleiding, wat betekent dat er een hoofdeffect van de variabele Vooropleiding is. Op dezelfde manier kan een mogelijk hoofdeffect van de variabele Geslacht onderzocht worden. Het gemiddelde van groep man is weergegeven met een oranje vierkant en het gemiddelde van groep vrouw met een blauw vierkant. Het gemiddelde van groep vrouw (8) ligt hoger dan het gemiddelde van groep man (6), dus er is ook een hoofdeffect van onafhankelijke variabele Geslacht. Beide onafhankelijke variabelen hebben dus een effect op de afhankelijke variabele Gemiddeld_cijfer.
# 
# <!-- ## CLOSEDBLOK: Uitleg1.R -->

# In[ ]:


Vooropleiding <- c(1,3,1,3)
Geslacht <- c("Man", "Man","Vrouw", "Vrouw")
Gemiddeld_cijfer <- c(5,7,7,9)
dat <- cbind.data.frame(Vooropleiding,Geslacht,Gemiddeld_cijfer)
ggplot(dat, aes(x = Vooropleiding, y = Gemiddeld_cijfer, group = Geslacht, colour = Geslacht)) + geom_line() + geom_point(size = 2) + scale_color_manual(values = c("darkorange", "deepskyblue")) + scale_x_continuous(breaks = c(1,3), labels = c("hbo-p", "vwo")) + annotate("point", x = 2, y = 8, colour = "deepskyblue", fill = "deepskyblue", shape = 22, size = 3) + annotate("point", x = 2, y = 6, colour = "darkorange", fill = "darkorange", shape = 22, size = 3) + annotate("point", x = 1, y = 6, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) + annotate("point", x = 3, y = 8, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) 


# <!-- ## /CLOSEDBLOK: Uitleg1.R -->
# 
# *Figuur 1.  Illustratie van hoofdeffecten bij factoriële ANOVA voor een casus met afhankelijke variabele Gemiddeld_cijfer en onafhankelijke variabelen Vooropleiding en Geslacht. In deze grafiek zijn er hoofdeffecten voor de variabelen Vooropleiding en Geslacht, maar geen interactie-effecten.*
# 
# Een interactie-effect houdt in dat het effect van de ene onafhankelijke variabele op de afhankelijke variabele afhangt van de andere onafhankelijke variabele(n). Er is als het ware een interactie tussen de onafhankelijke variabelen die het effect op de afhankelijke variabele bepaalt. In het bedachte experiment zou dit betekenen dat het effect van onafhankelijke variabele Vooropleiding op Gemiddeld_cijfer verschillend is voor de groepen man en vrouw. Een voorbeeld van dit interactie-effect is te zien in Figuur 2. In deze figuur is zichtbaar dat er bij mannen geen verschil is tussen de groepen hbo-p en vwo wat betreft het gemiddelde cijfer, maar dat er voor vrouwen wel een verschil is. Bij vrouwen heeft de groep vwo een hoger gemiddeld cijfer (9) dan de groep hbo-p (7). Het effect van de onafhankelijke variabele Vooropleiding op Gemiddeld_cijfer hangt af van de variabele Geslacht, dus er is een interactie-effect van de variabelen Vooropleiding en Geslacht op de afhankelijke variabele Gemiddeld_cijfer.
# 
# <!-- ## CLOSEDBLOK: Uitleg2.R -->

# In[ ]:


Vooropleiding <- c(1,3,1,3)
Geslacht <- c("Man", "Man","Vrouw", "Vrouw")
Gemiddeld_cijfer <- c(6,6,7,9)
dat <- cbind.data.frame(Vooropleiding,Geslacht,Gemiddeld_cijfer)
ggplot(dat, aes(x = Vooropleiding, y = Gemiddeld_cijfer, group = Geslacht, colour = Geslacht)) + geom_line() + geom_point(size = 2) + scale_color_manual(values = c("darkorange", "deepskyblue")) + scale_x_continuous(breaks = c(1,3), labels = c("hbo-p", "vwo")) + annotate("point", x = 2, y = 8, colour = "deepskyblue", fill = "deepskyblue", shape = 22, size = 3) + annotate("point", x = 2, y = 6, colour = "darkorange", fill = "darkorange", shape = 22, size = 3) + annotate("point", x = 1, y = 6.5, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) + annotate("point", x = 3, y = 7.5, colour = "forestgreen", fill = "forestgreen", shape = 24, size = 3) 


# <!-- ## /CLOSEDBLOK: Uitleg2.R -->
# 
# *Figuur 2.  Illustratie van interactie-effecten bij factoriële ANOVA voor een casus met de afhankelijke variabele Gemiddeld_cijfer en de onafhankelijke variabelen Vooropleiding en Geslacht. In deze grafiek is er een interactie-effect van de onafhankelijke variabelen Vooropleiding en Geslacht op de afhankelijke variabele Gemiddeld_cijfer.*
# 
# In Figuur 1 waren er hoofdeffecten van de variabelen Vooropleiding en Geslacht gevonden, maar was het interactie-effect nog niet onderzocht. In deze figuur is er geen sprake van een interactie-effect, omdat het effect van Vooropleiding op Gemiddeld_cijfer hetzelfde is voor mannen en vrouwen en dus niet afhangt van de variabele Geslacht. Voor beide groepen (mannen en vrouwen) is het verschil tussen hbo-p en vwo twee punten. Hier is dus geen sprake van een interactie-effect. Bij grafieken is er een interactie-effect als de twee (of meerdere) lijnen niet parallel lopen. Op deze manier kan snel onderzocht worden of er een interactie-effect is en wat de invloed van het interactie-effect is.
# 
# Bij *factoriële ANOVA* worden bovenstaande grafieken gebruikt om de resultaten te interpreteren. De hoofdeffecten en interactie-effecten worden eerst statistisch getoetst en daarna geïnterpreteerd met onder andere deze grafieken. De aanpak is als volgt.[^10] Eerst wordt getoetst of er sprake is van een interactie-effect tussen de onafhankelijke variabelen. Als dit niet het geval is, kunnen de hoofdeffecten geïnterpreteerd worden. Als er wel een interactie-effect is, kunnen de hoofdeffecten niet geïnterpreteerd worden. De volgende stap is dan een *simple effects analyse* waarbij het effect van de ene onafhankelijke variabele op de afhankelijke variabele wordt getoetst voor alle groepen van de andere onafhankelijke variabele die deel uitmaakt van het interactie-effect. Voor Figuur 2 zou dit betekenen dat het effect van Vooropleiding op Gemiddeld_cijfer apart getoetst wordt voor mannen en vrouwen. Het interactie-effect kan op deze manier geïnterpreteerd worden, samen met de grafische weergave zoals te zien in Figuur 2.
# 
# # Uitleg assumpties
# 
# Voor een valide toetsresultaat bij de *factoriële ANOVA* moet er aan een aantal assumpties voldaan worden. De steekproef moet bestaan uit onafhankelijke deelnemers[^19], de afhankelijke variabele moet normaal verdeeld zijn voor elke combinatie van groepen van de onafhankelijke variabelen en er moet homogeniteit van varianties zijn.[^1]
# 
# ## Normaliteit
# Controleer de assumptie van normaliteit voor elke groep met de volgende stappen:  
# 1. Controleer de data visueel met een histogram, een boxplot of een Q-Q plot.   
# 2. Toets of de data normaal verdeeld zijn met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (n < 50) met de *Shapiro-Wilk test*.[^7]<sup>, </sup>[^8]  
# 
# <!-- ## TEKSTBLOK: Link1.R -->
# De *factoriële ANOVA* is redelijk robuust ten opzichte van een schending van de assumptie van normaliteit. Als er kleine afwijkingen zijn, heeft dat relatief kleine gevolgen voor de validiteit van de toets. Bij grotere afwijkingen is het transformeren van de afhankelijke variabele een optie.[^2] Als dit niet werkt, dan is het een optie om de *factoriële ANOVA* uit te voeren als *multipele lineaire regressie* en te bootstrappen; zie bijbehorende [toetspagina](28-Multipele-lineaire-regressie-R.html).
# <!-- ## /TEKSTBLOK: Link1.R -->
# 
# ## Homogeniteit van Varianties
# Toets met de *Levene's Test (for equality of variance)* of de variantie van iedere groep ongeveer hetzelfde is. Bij een p-waarde kleiner dan 0,05 is de variantie van de groepen significant verschillend.[^10]
# 
# <!-- ## TEKSTBLOK: Link2.R -->
# De *factoriële ANOVA* is ook redelijk robuust ten opzichte van een schending van de assumptie van homogeniteit van varianties als de steekproefgroottes groot zijn en niet veel van elkaar verschillen. Als de ratio van de grootste en kleinste steekproefgrootte van alle groepen kleiner dan 10 is en de ratio van de grootste en kleinste variantie van alle groepen kleiner dan 4 is, dan kan de *factoriële ANOVA* gewoon uitgevoerd worden.[^3]  Als dit niet het geval is, dan is  het een optie om de *factoriële ANOVA* uit te voeren als *multipele lineaire regressie* en te bootstrappen; zie bijbehorende [toetspagina](28-Multipele-lineaire-regressie-R.html).
# <!-- ## /TEKSTBLOK: Link2.R -->
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^11] Voor de *factoriële ANOVA* wordt de effectmaat *partial eta squared* vaak gebruikt.[^4]
# 
# De effectmaat *partial eta squared* (partial *η^2^*) berekent de proportie van de onverklaarde variantie (variantie die niet door de andere variabelen wordt verklaard) in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele.[^4] Voor de variabele Vooropleiding geeft de partial eta squared dus de proportie verklaarde variantie weer van de variantie die niet verklaard is door de variabele Geslacht en de interactie tussen de variabele Vooropleiding en Geslacht. De partial eta squared van alle termen van het model tellen dus niet per se op tot 1.[^4] Een indicatie om partial *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^5]
# 
# # Post-hoc toetsen
# 
# De eerste stap van de *factoriële ANOVA* is het toetsen van hoofdeffecten en interactie-effecten. De volgende stap bestaat uit het bepalen welke groepen van elkaar verschillen, zowel bij *simple effects analyse* als het interpreteren van hoofdeffecten, en wordt gedaan met post-hoc toetsen. De post-hoc toetsen voeren meestal een correctie voor de p-waarden uit, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). Gebruik bij *factoriële ANOVA* de Games-Howell post-hoc toets, omdat deze te gebruiken is bij ongelijke varianties. De Bonferroni correctie is een optie als het doel is om de type I fout heel laag te houden.[^6] Er zijn ook nog andere opties voor een correctie op de p-waarden.[^11] In deze toetspagina wordt de Games-Howell post-hoc toets gebruikt.
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset ingeladen met de gemiddelde cijfers voor eerstejaars studenten van de bachelor Psychologie genaamd `Gemiddelde_cijfers_psychologie`. 
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
head(Gemiddelde_cijfers_psychologie)

## Laatste 5 observaties
tail(Gemiddelde_cijfers_psychologie)


# <!-- ## /OPENBLOK: Data-bekijken.R -->

# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# Inspecteer voor alle groepen het gemiddelde, de standaardafwijking, de mediaan en het aantal observaties om meer inzicht te krijgen. Gebruik hiervoor de functie `descr` en `stby` van het package `summarytools` om de beschrijvende statistieken per groep weer te geven. Voer de gewenste statistieken in met het argument `stats = c("mean","sd","med","n.valid")`.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-1.R -->

# In[ ]:


# Gemiddelde, standaardafwijking, mediaan en aantal observaties
library(summarytools)

with(Gemiddelde_cijfers_psychologie, 
     stby(data = Gemiddeld_cijfer, 
          list(Geslacht, Vooropleiding), 
          descr, 
          stats = c("mean", "sd", "med", "n.valid")))


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
# 
# Maak vervolgens een grafiek met de gemiddelden voor de verschillende groepen.
# 
# <!-- ## OPENBLOK: Data-beschrijven2.R -->

# In[ ]:


library(ggplot2)

ggplot(Gemiddelde_cijfers_psychologie, 
       aes(x = Vooropleiding, y = Gemiddeld_cijfer, group = Geslacht, colour = Geslacht)) + 
  stat_summary(fun = mean, geom = "point") +  
  stat_summary(fun = mean, geom = "line", aes(group = Geslacht)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue")) 


# <!-- ## /OPENBLOK: Data-beschrijven2.R -->
# 
# *Figuur 3.  Gemiddelde van de gemiddelde cijfers per groep op basis van Vooropleiding en Geslacht voor de dataset Gemiddelde_cijfers_psychologie.*
# 
# Op basis van de beschrijvende statistieken en de grafiek (Figuur 3) lijken er verschillen tussen de groepen te zijn. Vrouwen hebben voor alle vooropleidingen een hoger gemiddeld cijfer dan mannen. Voor vrouwen zijn er kleine verschillen tussen de vooropleidingen, maar voor mannen zijn deze verschillen groter. De mannelijke studenten afkomstig van het hbo-p hebben een substantieel lager gemiddelde dan mannelijke studenten afkomstig van het vwo of overige vooropleidingen. De lijnen van mannen en vrouwen lopen niet parallel dus er lijkt een interactie-effect te zijn. De *factoriële ANOVA* zal dit interactie-effect toetsen.

# ## Normaliteit
# 
# De *factoriële ANOVA* vereist dat de verdeling van de afhankelijke variabele de normale verdeling benaderd in elke groep die gevormd wordt door de onafhankelijke variabelen. Toets deze assumptie met behulp van een histogram en de *Kolmogorov-Smirnov* en *Shapiro-Wilk test*.
# 
# ### Histogram
# 
# Visualiseer de verdeling van de gemiddelde cijfers binnen elke groep met behulp van een histogram.[^9] Focus bij het analyseren van een histogram op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke outliers. Een normale verdeling is symmetrisch, heeft één top en geen outliers.[^16]<sup>, </sup>[^17]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot
ggplot(Gemiddelde_cijfers_psychologie,
  aes(x = Gemiddeld_cijfer)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 0.5,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Vooropleiding + Geslacht) +
  geom_density(alpha = .2, adjust = 1) +
  ylab("Gemiddeld cijfer")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# *Figuur 4.  Histogrammen van de verdelingen van de gemiddelde cijfers per groep op basis van Vooropleiding en Geslacht.*
# 
# De verdelingen van de zes groepen, te zien in Figuur 4, zijn redelijk symmetrisch, hebben geen outliers en zijn allen eentoppig. De verdelingen zijn dus bij benadering normaal.
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

with(Gemiddelde_cijfers_psychologie, 
     by(data = Gemiddeld_cijfer, 
        list(Geslacht, Vooropleiding), 
        lillie.test))


# <!-- ## /OPENBLOK: KStest.R -->
# 
# De p-waarde is groter dan 0,05 voor elke groep; er zijn dus geen significante verschillen gevonden tussen de verdelingen van de steekproef en de normale verdeling. De *factoriële ANOVA* kan uitgevoerd worden.
# 
# #### Shapiro-Wilk test
# De *Shapiro-Wilk test* is een soortgelijke toets als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (*n* < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.[^18]
# 
# <!-- ## OPENBLOK: Shapiro-Wilk-test.R -->

# In[ ]:


library("nortest")

with(Gemiddelde_cijfers_psychologie, 
     by(data = Gemiddeld_cijfer, 
        list(Geslacht, Vooropleiding), 
        shapiro.test))


# <!-- ## /OPENBLOK: Shapiro-Wilk-test.R -->
# 
# De p-waarde is groter dan 0,05 voor elke groep; er zijn dus geen significante verschillen gevonden tussen de verdelingen van de steekproef en de normale verdeling. De *factoriële ANOVA* kan uitgevoerd worden.
# 
# ## Homogeniteit van varianties
# 
# <!-- ## TEKSTBLOK: LeveneTest1.R -->
# Toets met de *Levene's test* de assumptie homogeniteit van varianties. Gebruik hiervoor de functie `leveneTest` van het package `car` met het argument `Gemiddeld_cijfer ~ Vooropleiding*Geslacht` met daarin de afhankelijke variabele `Gemiddeld_cijfer` en de onafhankelijke variabelen `Vooropleiding*Geslacht` (het vermenigvuldigingsteken zorgt ervoor dat de variabelen apart van elkaar en als interactie mee worden genomen) en het argument `data = Gemiddelde_cijfers_psychologie`.
# <!-- ## /TEKSTBLOK: LeveneTest1.R -->
# 
# <!-- ## OPENBLOK: Levenes-test.R -->

# In[ ]:


library(car)
leveneTest(Gemiddeld_cijfer ~ Vooropleiding*Geslacht, 
           data = Gemiddelde_cijfers_psychologie)


# <!-- ## /OPENBLOK: Levenes-test.R -->
# 
# <!-- ## CLOSEDBLOK: Levenes-test.R -->

# In[ ]:


L <- leveneTest(Gemiddeld_cijfer ~ Vooropleiding*Geslacht, data = Gemiddelde_cijfers_psychologie)

vF_waarde <- Round_and_format(L$`F value`[1])
vF_p <- Round_and_format(L$`Pr(>F)`[1])
vDF1 <- Round_and_format(L$`Df`[1])
vDF2 <- Round_and_format(L$`Df`[2])


# <!-- ## /CLOSEDBLOK: Levenes-test.R -->
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# * *F*(`r vDF1`,`r vDF2`) = `r vF_waarde`, p-waarde = `r vF_p`, 
# * De p-waarde is groter dan 0,05, dus er is geen significant verschil gevonden tussen de groepen in variantie.[^18] Er is dus aan de assumptie van homogeniteit van varianties voldaan.
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->

# # Factoriële ANOVA 
# Voer de *factoriële ANOVA* uit om de vraag te beantwoorden of er verschillen zijn tussen mannen en vrouwen en studenten met een hbo-p vooropleiding, vwo vooropleiding of overige vooropleiding wat betreft het gemiddelde cijfer in het eerste jaar van de bachelor Psychologie.
# 
# <!-- ## TEKSTBLOK: ANOVA-toets.R -->
# Gebruik `aov()` om een ANOVA-object (`ANOVA_object`) te creëren. Het eerste argument bestaat uit de afhankelijke variabele `Gemiddeld_cijfer` en de onafhankelijke variabele `Geslacht`, de onafhankelijke variabele `Vooropleiding` en de interactie tussen beide variabelen `Geslacht:Vooropleiding`. Het tweede argument bevat de dataset `data = Gemiddelde_cijfers_psychologie`. Geef de resultaten weer met de functie `summary()`.
# <!-- ## /TEKSTBLOK: ANOVA-toets.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets.R -->

# In[ ]:


ANOVA_object <- aov(Gemiddeld_cijfer ~ Geslacht + Vooropleiding + Geslacht:Vooropleiding, 
                    data = Gemiddelde_cijfers_psychologie)

summary(ANOVA_object)


# <!-- ## /OPENBLOK: ANOVA-toets.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets2.R -->
# Bereken vervolgens de effectmaat partial eta squared met behulp van de functie `EtaSq` van het package `DescTools` met als argument het ANOVA-object `ANOVA_object`.
# <!-- ## /TEKSTBLOK: ANOVA-toets2.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets3.R -->

# In[ ]:


library(DescTools)
EtaSq(ANOVA_object)


# <!-- ## /OPENBLOK: ANOVA-toets3.R -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets4.R -->

# In[ ]:


FA <- summary(ANOVA_object)[[1]]
pes <- EtaSq(ANOVA_object)

vF_waarde <- Round_and_format(FA$`F value`[3])
vDF1 <- Round_and_format(FA$Df[3])
vDF2 <- Round_and_format(FA$Df[4])
Esq <- Round_and_format(pes[3,2])


# <!-- ## /CLOSEDBLOK: ANOVA-toets4.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets5.R -->
# 
# * Er is een significant interactie-effect van Vooropleiding en Geslacht op Gemiddeld_cijfer, *F* (`r vDF1`,`r vDF2`) = `r vF_waarde`, *p* < 0,0001, *η^2^* = `r Esq`.
# * De p-waarde is kleiner dan 0,05, dus de nulhypothese dat er geen interactie-effect is wordt verworpen.[^18] 
# * Er is een klein tot gemiddeld effect van de interactie tussen Vooropleiding en Geslacht op Gemiddeld_cijfer.
# * Omdat er een significant interactie-effect is, hoeven de hoofdeffecten niet geïnterpreteerd te worden. De volgende stap is een *simple effects analyse* om te interactie verder te onderzoeken.
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets5.R -->
# 
# ## Simple effects analyse
# 
# Voer een *simple effects analyse* uit om het interactie-effect te interpreteren. Vergelijk eerst de verschillen tussen de drie vooropleidingen voor elke categorie van de variabele Geslacht (mannen en vrouwen dus). Vergelijk daarna de verschillen tussen mannen en vrouwen van elke categorie van de variabele Vooropleiding (hbo-p, vwo of overig).
# 
# ### Vooropleiding
# 
# <!-- ## TEKSTBLOK: SimEff1.R -->
# Maak eerst een aparte dataset voor mannen en vrouwen aan en voer vervolgens de Games-Howell post hoc toets uit met behulp van de functie `posthocTGH()$output` van het package `userfriendlyscience`. Het eerste argument is de afhankelijke variabele (bijvoorbeeld `Mannen_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer`), het tweede argument is de onafhankelijke variabele (bijvoorbeeld `Mannen_Gemiddelde_cijfers_psychologie$Vooropleiding`) en het derde argument `method = "games-howell"` om aan te geven dat de Games-Howell post-hoc toets uitgevoerd moet worden.
# <!-- ## /TEKSTBLOK: SimEff1.R -->
# 
# <!-- ## OPENBLOK: SimEff2.R -->

# In[ ]:


library(userfriendlyscience)

# Maak een dataset met mannen en een dataset met vrouwen
Mannen_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Geslacht == "Man",]

Vrouwen_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Geslacht == "Vrouw",]

# Voer voor beide datasets de Games-Howell post-hoc toets uit
Games_Howell_Mannen <- posthocTGH(Mannen_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Mannen_Gemiddelde_cijfers_psychologie$Vooropleiding,
           method = "games-howell")$output

Games_Howell_Vrouwen <- posthocTGH(Vrouwen_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Vrouwen_Gemiddelde_cijfers_psychologie$Vooropleiding,
           method = "games-howell")$output

# Geef de resultaten weer van de Games-Howell post-hoc toets
Games_Howell_Mannen$games.howell
Games_Howell_Vrouwen$games.howell


# <!-- ## /OPENBLOK: SimEff2.R -->
# 
# <!-- ## CLOSEDBLOK: SimEff3.R -->
# ````{r, echo=FALSE}
# # Maak een dataset met mannen en een dataset met vrouwen
# Mannen_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Geslacht == "Man",]
# 
# Vrouwen_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Geslacht == "Vrouw",]
# 
# # Voer voor beide datasets de Games-Howell post-hoc toets uit
# Games_Howell_Mannen <- posthocTGH(Mannen_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
#            Mannen_Gemiddelde_cijfers_psychologie$Vooropleiding,
#            method = "games-howell")$output
# 
# Games_Howell_Vrouwen <- posthocTGH(Vrouwen_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
#            Vrouwen_Gemiddelde_cijfers_psychologie$Vooropleiding,
#            method = "games-howell")$output
# 
# # Geef de resultaten weer van de Games-Howell post-hoc toets
# GH_man <- Games_Howell_Mannen$games.howell
# GH_vrouw <- Games_Howell_Vrouwen$games.howell
# 
# ```
# <!-- ## /CLOSEDBLOK: SimEff3.R -->
# 
# <!-- ## TEKSTBLOK: SimEff4.R -->
# Voor mannen zijn de volgende vergelijkingen getoetst[^18]:
# 
# * Hbo-p versus vwo: het verschil in gemiddelde (vwo - hbo-p) is `r Round_and_format(GH_man$diff[1])`, dit is een significant verschil (*p* < 0,0001).
# * Hbo-p versus overig: het verschil in gemiddelde (overig - hbo-p) is `r Round_and_format(GH_man$diff[2])`, dit is een significant verschil (*p* < 0,01).
# * Vwo versus overig: het verschil in gemiddelde (overig - vwo) is `r Round_and_format(GH_man$diff[3])`, dit is geen significant verschil (*p* = `r Round_and_format(GH_man$p[3])`).
# 
# Voor vrouwen zijn de volgende vergelijkingen getoetst[^18]:
# 
# * Hbo-p versus vwo: het verschil in gemiddelde (vwo - hbo-p) is `r Round_and_format(GH_vrouw$diff[1])`, dit is geen significant verschil (*p* = `r Round_and_format(GH_vrouw$p[1])`).
# * Hbo-p versus overig: het verschil in gemiddelde (overig - hbo-p) is `r Round_and_format(GH_vrouw$diff[2])`, dit is geen significant verschil (*p* = `r Round_and_format(GH_vrouw$p[2])`).
# * Vwo versus overig: het verschil in gemiddelde (overig - vwo) is  `r Round_and_format(GH_vrouw$diff[3])`, dit is geen significant verschil (*p* = 1,00).
# 
# <!-- ## /TEKSTBLOK: SimEff4.R -->

# ### Geslacht
# 
# <!-- ## TEKSTBLOK: SimEff5.R -->
# Maak eerst aparte datasets voor studenten met een hbo-p, vwo en overige vooropleiding en voer vervolgens de Games-Howell post hoc toets uit met behulp van de functie `posthocTGH()$output` van het package `userfriendlyscience`. Het eerste argument is de afhankelijke variabele (bijvoorbeeld `Hbo_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer`), het tweede argument is de onafhankelijke variabele (bijvoorbeeld `Hbo_Gemiddelde_cijfers_psychologie$Geslacht`) en het derde argument `method = "games-howell"` om aan te geven dat de Games-Howell post-hoc toets uitgevoerd moet worden.
# <!-- ## /TEKSTBLOK: SimEff5.R -->
# 
# <!-- ## OPENBLOK: SimEff6.R -->

# In[ ]:


library(userfriendlyscience)

# Maak een dataset met studenten met een hbo-p, vwo en overige vooropleiding
Hbo_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Vooropleiding == "hbo",]

Vwo_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Vooropleiding == "vwo",]

Overig_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Vooropleiding == "overig",]

# Voer voor de drie datasets de Games-Howell post-hoc toets uit
Games_Howell_hbo <- posthocTGH(Hbo_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Hbo_Gemiddelde_cijfers_psychologie$Geslacht,
           method = "games-howell")$output

Games_Howell_vwo <- posthocTGH(Vwo_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Vwo_Gemiddelde_cijfers_psychologie$Geslacht,
           method = "games-howell")$output

Games_Howell_overig <- posthocTGH(Overig_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Overig_Gemiddelde_cijfers_psychologie$Geslacht,
           method = "games-howell")$output

# Geef de resultaten weer van de Games-Howell post-hoc toets
Games_Howell_hbo$games.howell
Games_Howell_vwo$games.howell
Games_Howell_overig$games.howell


# <!-- ## /OPENBLOK: SimEff6.R -->
# 
# <!-- ## CLOSEDBLOK: SimEff7.R -->

# In[ ]:


# Maak een dataset met studenten met een hbo-p, vwo en overige vooropleiding
Hbo_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Vooropleiding == "hbo",]

Vwo_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Vooropleiding == "vwo",]

Overig_Gemiddelde_cijfers_psychologie <- Gemiddelde_cijfers_psychologie[Gemiddelde_cijfers_psychologie$Vooropleiding == "overig",]

# Voer voor de drie datasets de Games-Howell post-hoc toets uit
Games_Howell_hbo <- posthocTGH(Hbo_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Hbo_Gemiddelde_cijfers_psychologie$Geslacht,
           method = "games-howell")$output

Games_Howell_vwo <- posthocTGH(Vwo_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Vwo_Gemiddelde_cijfers_psychologie$Geslacht,
           method = "games-howell")$output

Games_Howell_overig <- posthocTGH(Overig_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Overig_Gemiddelde_cijfers_psychologie$Geslacht,
           method = "games-howell")$output

# Geef de resultaten weer van de Games-Howell post-hoc toets
GH_hbo <- Games_Howell_hbo$games.howell
GH_vwo <- Games_Howell_vwo$games.howell
GH_overig <- Games_Howell_overig$games.howell


# <!-- ## /CLOSEDBLOK: SimEff7.R -->
# 
# <!-- ## TEKSTBLOK: SimEff8.R -->
# * Hbo-p: het verschil in gemiddelde (vrouw - man) is `r Round_and_format(GH_hbo$diff[1])`, dit is een significant verschil (*p* < 0,0001).[^18]
# * Vwo: het verschil in gemiddelde (vrouw - man) is `r Round_and_format(GH_vwo$diff[1])`, dit is geen significant verschil (*p* = `r Round_and_format(GH_vwo$p[1])`).[^18]
# * Overig: het verschil in gemiddelde (vrouw - man) is `r Round_and_format(GH_overig$diff[1])`, dit is geen significant verschil (*p* = `r Round_and_format(GH_overig$p[1])`).[^18]
# 
# <!-- ## /TEKSTBLOK: SimEff8.R -->

# ## Illustratie van post-hoc toetsing bij hoofdeffecten zonder interactie-effect
# 
# <!-- ## TEKSTBLOK: PHtest1.R -->
# In de huidige casus worden de hoofdeffecten niet geïnterpreteerd vanwege het significante interactie-effect. Om toch te illustreren hoe het interpreteren van hoofdeffecten zonder een significant interactie-effect werkt, wordt de bijbehorende post-hoc toetsing toch geïllustreerd. Hiervoor wordt  een nieuwe dataset `Hoofdeffecten_Gemiddelde_cijfers_psychologie` gebruikt. 
# 
# <!-- ## /TEKSTBLOK: PHtest1.R -->
# 
# <!-- ## OPENBLOK: PHtest2.R -->

# In[ ]:


ANOVA_object_hoofdeffect <- aov(Gemiddeld_cijfer ~ Geslacht + Vooropleiding + Geslacht:Vooropleiding,
                                data = Hoofdeffecten_Gemiddelde_cijfers_psychologie)

summary(ANOVA_object_hoofdeffect)


# <!-- ## /OPENBLOK: PHtest2.R -->
# 
# <!-- ## CLOSEDBLOK: PHtest3.R -->

# In[ ]:


FA <- summary(ANOVA_object_hoofdeffect)[[1]]
pes <- EtaSq(ANOVA_object_hoofdeffect)

vF_waarde <- Round_and_format(FA$`F value`[3])
vDF1 <- Round_and_format(FA$Df[3])
vDF2 <- Round_and_format(FA$Df[4])
vP <- Round_and_format(FA$`Pr(>F)`[3])


# <!-- ## /CLOSEDBLOK: PHtest3.R -->
# 
# <!-- ## TEKSTBLOK: PHtest4.R -->
# Er is geen significant interactie-effect van Vooropleiding en Geslacht op Gemiddeld_cijfer, *F* (`r vDF1`,`r vDF2`) = `r vF_waarde`, *p* = `r vP`.[^18] De hoofdeffecten van Geslacht (*p* < 0,01) en Vooropleiding (*p* < 0,0001) zijn wel significant.[^18] Voer daarom de Games_howell post-hoc toets uit voor beide variabelen. Gebruik hiervoor de functie `posthocTGH()$output` van het package `userfriendlyscience`. Het eerste argument is de afhankelijke variabele `Hoofdeffecten_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer`, het tweede argument is de onafhankelijke variabele (bijvoorbeeld `Hoofdeffecten_Gemiddelde_cijfers_psychologie$Geslacht`) en het derde argument `method = "games-howell"` om aan te geven dat de Games-Howell post-hoc toets uitgevoerd moet worden.
# <!-- ## /TEKSTBLOK: PHtest4.R -->
# 
# <!-- ## OPENBLOK: PHtest5.R -->

# In[ ]:


library(userfriendlyscience)

# Voer de post-hoc toets uit voor de onafhankelijke variabele Vooropleiding
Games_Howell_vooropleiding <- posthocTGH(Hoofdeffecten_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Hoofdeffecten_Gemiddelde_cijfers_psychologie$Vooropleiding,
           method = "games-howell")$output

# Voer de post-hoc toets uit voor de onafhankelijke variabele Geslacht
Games_Howell_geslacht <- posthocTGH(Hoofdeffecten_Gemiddelde_cijfers_psychologie$Gemiddeld_cijfer,
           Hoofdeffecten_Gemiddelde_cijfers_psychologie$Geslacht,
           method = "games-howell")$output

# Geef de resultaten weer van de Games-Howell post-hoc toets
Games_Howell_vooropleiding$games.howell
Games_Howell_geslacht$games.howell


# <!-- ## /OPENBLOK: PHtest5.R -->
# 
# <!-- ## CLOSEDBLOK: PHtest6.R -->
# ````{r, echo=FALSE}
# 
# GH_Vooropleiding <- Games_Howell_vooropleiding$games.howell
# GH_Geslacht <- Games_Howell_geslacht$games.howell
# 
# 
# ```
# <!-- ## /CLOSEDBLOK: PHtest6.R -->
# 
# <!-- ## TEKSTBLOK: PHtest7.R -->
# De verschillen voor de groepen van de onafhankelijke variabele Vooropleiding zijn[^18]:
# 
# * Hbo-p versus vwo: het verschil in gemiddelde (vwo - hbo-p) is `r Round_and_format(GH_Vooropleiding$diff[1])`, dit is een significant verschil (*p* < 0,0001).
# * Hbo-p versus overig: het verschil in gemiddelde (overig - hbo-p) is `r Round_and_format(GH_Vooropleiding$diff[2])`, dit is een significant verschil (*p* < 0,001).
# * Vwo versus overig: het verschil in gemiddelde (overig - vwo) is `r Round_and_format(GH_Vooropleiding$diff[3])`, dit is geen significant verschil (*p* = `r Round_and_format(GH_Vooropleiding$p[3])`).
# 
# De verschillen voor de groepen van de onafhankelijke variabele Geslacht zijn[^18]:
# 
# * Man versus Vrouw: het verschil in gemiddelde (vrouw - man) is `r Round_and_format(GH_Geslacht$diff[1])`, dit is een significant verschil (*p* = 0,009).
# 
# <!-- ## /TEKSTBLOK: PHtest7.R -->
# 
# Visualiseer de gemiddelden per groep om de resultaten ook visueel weer te geven. In de grafiek in Figuur 5 is te zien dat de lijnen redelijk parallel lopen wat overeenkomt met het feit dat er geen significant interactie-effect is. Het hoofdeffect van de variabele Geslacht is duidelijk zichtbaar: de gemiddeldes van vrouwen liggen voor alle vooropleiding hoger dan de gemiddeldes van mannen. Dit komt overeen met het significante verschil tussen beide groepen op de post-hoc toets. Het hoofdeffect van de variabele Vooropleiding is ook zichtbaar: de gemiddeldes voor de groepen vwo en overig verschillen onderling niet veel, maar liggen hoger dan het gemiddelde van de groep hbo-p. De post-hoc toetsen wijzen dat ook uit met een significant verschil tussen hbo-p en vwo, een significant verschil tussen hbo-p en overig en geen significant verschil tussen vwo en overig.
# 
# <!-- ## OPENBLOK: PHtest8.R -->

# In[ ]:


ggplot(Hoofdeffecten_Gemiddelde_cijfers_psychologie, 
       aes(x = Vooropleiding, y = Gemiddeld_cijfer, group = Geslacht, colour = Geslacht)) + 
  stat_summary(fun = mean, geom = "point") + 
  stat_summary(fun = mean, geom = "line", aes(group = Geslacht)) + 
  scale_color_manual(values = c("darkorange", "deepskyblue")) 


# <!-- ## /OPENBLOK: PHtest8.R -->
# 
# *Figuur 5.  Gemiddelde van de gemiddelde cijfers per groep op basis van Vooropleiding en Geslacht voor de dataset Hoofdeffecten_Gemiddelde_cijfers_psychologie.*
# 
# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *factoriële ANOVA* is uitgevoerd om te toetsen of er verschillen zijn tussen mannen en vrouwen en studenten met een hbo-p vooropleiding, vwo vooropleiding of overige vooropleiding wat betreft het gemiddelde cijfer in het eerste jaar van de bachelor Psychologie. De resultaten lieten zien dat er een significant interactie-effect was tussen Vooropleiding en Geslacht op de gemiddelde cijfers van de studenten, *F* (`r vDF1`,`r vDF2`) = `r vF_waarde`, *p* < 0,0001, *η^2^* = `r Esq`. 
# 
# Om dit effect verder te onderzoeken, is er een *simple effects analyse* uitgevoerd met behulp van de Games-Howell post-hoc toets. Uit deze analyse bleek dat mannen met een vwo vooropleiding een significant hoger gemiddeld cijfer hadden dan mannen met een hbo-p vooropleiding (*p* < 0,0001), dat mannen met een overige vooropleiding ook een significant hoger gemiddeld cijfer hadden dan mannen met een hbo-p vooropleiding (*p* < 0,01) en dat er geen significant verschil was tussen mannen met een vwo en overige vooropleiding. Bij vrouwen was er geen enkel significant verschil tussen de groepen met een vwo, hbo-p of overige vooropleiding. Bij studenten met een hbo-p vooropleiding hadden vrouwen significant hogere gemiddelde cijfers (*p* < 0,0001) dan mannen, maar waren er geen significante verschillen voor studenten met een vwo of overige vooropleiding. In Figuur 6 zijn de gemiddeldes voor alle groepen weergegeven om de resultaten te ondersteunen. 
# 
# Samenvattend suggereren de resultaten dat er bij vrouwen geen verschillen zijn in gemiddeld cijfer tussen de studenten afkomstig van verschillende vooropleidingen, maar dat bij mannen studenten met een hbo-p vooropleiding minder goed presteren dan studenten met een vwo of overige vooropleiding. Daarnaast presteren vrouwen afkomstig van het hbo-p beter dan mannen afkomstig van het hbo-p, maar zijn er geen man-vrouw verschillen voor de studenten met een vwo of overige vooropleiding.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# 

# <!-- ## CLOSEDBLOK: Rapportage2.R -->

# In[ ]:


ggplot(Gemiddelde_cijfers_psychologie, aes(x = Vooropleiding, y = Gemiddeld_cijfer, group = Geslacht, colour = Geslacht)) + stat_summary(fun = mean, geom = "point") + stat_summary(fun = mean, geom = "line", aes(group = Geslacht)) + scale_color_manual(values = c("darkorange", "deepskyblue")) 


# <!-- ## /CLOSEDBLOK: Rapportage2.R -->
# 
# *Figuur 6.  Gemiddelde van de gemiddelde cijfers per groep op basis van Vooropleiding en Geslacht voor de dataset Gemiddelde_cijfers_psychologie.*

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd statistics (2018). *Two-way ANOVA in SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/two-way-anova-using-spss-statistics.php. 
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
