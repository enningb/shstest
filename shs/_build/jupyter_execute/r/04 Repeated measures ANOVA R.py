#!/usr/bin/env python
# coding: utf-8
---
title: "Repeated measures ANOVA"
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


source(paste0(here::here(),"/01. Includes/data/04.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik de *repeated measures ANOVA* om gemiddelden te vergelijken van een groep bij twee of meer herhaalde metingen of om gemiddelden van twee of meer gepaarde groepen te vergelijken.[^1] 
# 
# # Onderwijscasus
# <div id = "casus">
# 
# De opleidingsdirecteur van de bachelor Technische Natuurkunde van een universiteit hoort vanuit de opleidingscommissie dat de eerstejaars studenten de studielast van de eerste onderwijsperiode als erg hoog ervaren. Om te onderzoeken hoe deze ervaren studielast verminderd kan worden, wil hij onderzoeken hoeveel tijd de studenten per week besteden aan hun vakken. Met behulp van een vragenlijst over de studiebelasting in het eerste jaar verzamelt hij gegevens van het aantal uur per week dat eerstejaars studenten besteden aan de vakken in de eerste onderwijsperiode: Lineaire Algebra, Relativiteitstheorie en Kosmologie. Op deze manier kan hij onderzoeken of er verschillen in de tijdsbesteding aan de verschillende vakken zijn en om te bepalen van welke vakken de studielast aangepast moet worden.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het gemiddeld aantal studieuren per week van eerstejaars studenten van de bachelor Technische Natuurkunde is hetzelfde voor de drie vakken in de eerste onderwijsperiode
# 
# *H~A~*: Het gemiddeld aantal studieuren per week van eerstejaars studenten van de bachelor Technsiche Natuurkunde is niet hetzelfde voor de drie vakken in de eerste onderwijsperiode
# 
# </div>
# 
# # Assumpties
# Om een valide toetsresultaat te bereiken met de *repeated measures ANOVA* moet de data aan een aantal voorwaarden voldoen: normaliteit, sphericiteit en onafhankelijkheid.[^1] Onafhankelijkheid houdt in dat de herhaalde metingen van de deelnemers[^12] onafhankelijk van elkaar zijn.
# 
# ## Normaliteit
# <!-- ## TEKSTBLOK: link1.R -->
# De assumptie van normaliteit houdt in dat er een normale verdeling van de afhankelijke variabele is in elke groep van metingen. Controleer daarom de assumptie van normaliteit voor elke groep van metingen met de volgende stappen:  
# 1. Controleer de data visueel met een histogram, een boxplot of een Q-Q plot.   
# 2. Toets of de data normaal verdeeld is met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (n < 50) met de *Shapiro-Wilk test*.[^4]<sup>, </sup>[^5]  
# <!-- ## /TEKSTBLOK: link1.R -->
# 
# De eerste stap heeft als doel een goede indruk te krijgen van de verdeling van de steekproef. In de tweede stap wordt de assumptie van normaliteit getoetst. De statistische toets laat zien of de verdeling van de observaties van een groep voldoet aan de assumptie van normaliteit. Voor alle groepen moet er voldaan zijn aan de assumptie van normaliteit.
# 
# Als er niet voldaan is aan normaliteit, is het transformeren van de data een optie.[^2] Een andere optie is het gebruik van de nonparametrische [Friedman's ANOVA](09-Friedmans-ANOVA-R.html) waar normaliteit geen assumptie is.[^3] De *repeated measures ANOVA* is echter ook een robuuste toets ten opzichte van de assumptie van normaliteit. Als elke groep een aantal observaties (*n*) heeft dat groter dan 100 is,  ga er dan vanuit dat de *repeated measures ANOVA* robuust genoeg is om uit te voeren zonder dat de afhankelijke variabele een normale verdeling volgt.
# 
# ## Sphericiteit
# De assumptie van sphericiteit houdt in dat de variantie van de verschilscores tussen groepen van metingen ongeveer aan elkaar gelijk zijn.[^6] In deze casus zijn dat de verschilscores tussen de drie vakken: Lineaire Algebra minus Relativiteitstheorie, Relativiteitstheorie minus Kosmologie en Kosmologie minus Lineaire Algebra. Toets deze assumptie met *Mauchly's test*. Wanneer de data niet aan de assumptie voldoen, geeft de gewone *repeated measures ANOVA* een verkeerd resultaat. Er zijn echter correcties die gebruikt kunnen worden wanneer de data niet aan sphericiteit voldoen. Een voorbeeld van mogelijke output van *Mauchly's test* in R is hieronder weergegeven.
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
# Bij een p-waarde kleiner dan 0,05, toont *Mauchly's test* dat de assumptie van sphericiteit geschonden is. In de output is dit te zien aan de p-waarde van 0,0051 onder ` $Mauchly's Test for Sphericity `. Er zijn twee mogelijke correcties wanneer er geen sphericiteit is: de Greenhouse-Geisser (GG) en Huynh-Feldt (HF) correctie. De Greenhouse-Geisser correctie staat bekend als conservatief, wat betekent dat de correctie een relatief lage kans op een type I fout heeft. In andere woorden, het zal niet vaak gebeuren dat deze correctie een significant effect aantoont wanneer dat er in werkelijkheid niet is. De Huynh-Feldt correctie staat echter bekend als liberaal, wat betekent dat er een relatief hoge kans op een type I fout is. De teststatistiek en p-waarde van beide correcties zijn in de output te vinden onder ` $Sphericity Corrections `.
# <!-- ## /TEKSTBLOK: Sphericiteit1.R -->
# 
# Houd de volgende richtlijnen aan bij het interpreteren van de *repeated measures ANOVA* wanneer niet aan sphericiteit is voldaan:
# 
# * Wanneer beide correcties significant zijn, rapporteer de (conservatieve) Greenhouse-Geisser correctie.
# * Wanneer beide correcties niet significant zijn, rapporteer de (liberale) Huynh-Feldt correctie.
# * Wanneer de een significant is en de ander niet, bereken de gemiddelde p-waarde van beide correcties.
#     * Wanneer deze p-waarde significant is, rapporteer dan de significante correctie.
#     * Wanneer deze p-waarde niet significant is, rapporteer dan de niet significante correctie.
# 
# In de voorbeeldoutput is de p-waarde van de Greenhouse-Geisser correctie groter dan 0,05 en de p-waarde van de Huynh-Feldt correctie kleiner dan 0,05. Het gemiddelde van beide p-waarden is 0,049855, wat betekent dat er een significant resultaat is. Rapporteer in dit geval dus de (significante) Huynh-Feldt correctie, i.e. *F* = 0,56, *p* < 0,05.  

# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen van metingen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^6] Voor de *repeated measures ANOVA* wordt de effectmaat eta squared vaak gebruikt.
# 
# ## Eta squared
# De effectmaat eta squared (*η^2^*) berekent de proportie van de variantie in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele. In deze casus berekent het de proportie van de variantie in het aantal uren studeren die verklaard kan worden door het vak in de eerste onderwijsperiode. Een indicatie om *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^7]
# 
# # Post-hoc toetsen
# De *repeated measures ANOVA* toetst of één of meerdere van de gemiddelden anders is dan de andere gemiddelden. Voer een post-hoc toets uit om te bepalen welke groepen van metingen significant verschillen.
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout. Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^6]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset `Studieuren_technische_natuurkunde` ingeladen met het aantal studieuren van eerstejaars studenten van de bachelor Technische Natuurkunde voor de drie vakken in de eerste onderwijsperiode.
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken1.R -->

# In[ ]:


## Eerste 5 observaties
head(Studieuren_technische_natuurkunde)

## Laatste 5 observaties
tail(Studieuren_technische_natuurkunde)


# <!-- ## /OPENBLOK: Data-bekijken1.R -->
# 
# Selecteer de drie groepen van metingen en sla deze op in een vector om deze makkelijker aan te kunnen roepen. 
# <!-- ## OPENBLOK: Data-selecteren.R -->

# In[ ]:


Studieuren_lineaire_algebra <- Studieuren_technische_natuurkunde$Studieuren[Studieuren_technische_natuurkunde$Vak == "Lineaire Algebra"]
Studieuren_relativiteitstheorie <- Studieuren_technische_natuurkunde$Studieuren[Studieuren_technische_natuurkunde$Vak == "Relativiteitstheorie"]
Studieuren_kosmologie <- Studieuren_technische_natuurkunde$Studieuren[Studieuren_technische_natuurkunde$Vak == "Kosmologie"]


# <!-- ## /OPENBLOK: Data-selecteren.R -->

# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# Inspecteer de data met `mean()`, `sd()` en `length()` om meer inzicht te krijgen in de data.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# 
# <!-- ## OPENBLOK: numpy1.R -->
# <!-- ## /OPENBLOK: numpy1.R -->

# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven1.R -->

# In[ ]:


# Gemiddelde
mean(Studieuren_lineaire_algebra)
# Standaardafwijking
sd(Studieuren_lineaire_algebra)
# Aantal observaties
length(Studieuren_lineaire_algebra)


# <!-- ## /OPENBLOK: Data-beschrijven1.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Data-beschrijven2.R -->

# In[ ]:


# Gemiddelde
mean(Studieuren_relativiteitstheorie)
# Standaardafwijking
sd(Studieuren_relativiteitstheorie)
# Aantal observaties
length(Studieuren_relativiteitstheorie)


# <!-- ## /OPENBLOK: Data-beschrijven2.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Data-beschrijven3.R -->

# In[ ]:


# Gemiddelde
mean(Studieuren_kosmologie)
# Standaardafwijking
sd(Studieuren_kosmologie)
# Aantal observaties
length(Studieuren_kosmologie)


# <!-- ## /OPENBLOK: Data-beschrijven3.R -->
#   </div>
# </div>

# <!-- ## CLOSEDBLOK: Data-beschrijven4.R -->

# In[ ]:


vM_LA  <- Round_and_format(mean(Studieuren_lineaire_algebra))
vSD_LA <- Round_and_format(sd(Studieuren_lineaire_algebra))
vN_LA  <- Round_and_format(length(Studieuren_lineaire_algebra))

vM_RT  <- Round_and_format(mean(Studieuren_relativiteitstheorie))
vSD_RT <- Round_and_format(sd(Studieuren_relativiteitstheorie))
vN_RT  <- Round_and_format(length(Studieuren_relativiteitstheorie))

vM_KL  <- Round_and_format(mean(Studieuren_kosmologie))
vSD_KL <- Round_and_format(sd(Studieuren_kosmologie))
vN_KL  <- Round_and_format(length(Studieuren_kosmologie))


# <!-- ## /CLOSEDBLOK: Data-beschrijven4.R -->
# 
# <!-- ## TEKSTBLOK: Datatekst-beschrijven.R -->
# * Gemiddeld aantal studieuren Lineaire Algebra (standaarddeviatie): `r vM_LA` (`r vSD_LA`), *n* = `r vN_LA`  
# * Gemiddeld aantal studieuren Relativiteitstheorie (standaarddeviatie): `r vM_RT` (`r vSD_RT`), *n* = `r vN_RT`  
# * Gemiddeld aantal studieuren Kosmologie (standaarddeviatie): `r vM_KL` (`r vSD_KL`), *n* = `r vN_KL`
# 
# <!-- ## /TEKSTBLOK: Datatekst-beschrijven.R -->
# 
# ## Visuele inspectie van normaliteit
# Geef de verdeling van de studieuren voor elke groep visueel weer met een histogram, Q-Q plot en boxplot.
# 
# ### Histogram
# 
# Focus bij het analyseren van een histogram[^18] op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters. Een normale verdeling is symmetrisch, heeft één top en geen uitbijters.[^9]<sup>, </sup>[^10]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot
library(ggplot2)

ggplot(Studieuren_technische_natuurkunde,
  aes(x = Studieuren)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 2,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Vak) +
  geom_density(alpha = .2, adjust = 1) +
  ylab("Frequentiedichtheid") +
  labs(title = "Aantal studieuren")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# Alle drie de verdelingen hebben één top en lijken geen uitbijters te hebben. Tevens zijn de verdelingen redelijk symmetrisch. Deze verdelingen benaderen de normaalverdeling.
# 
# ### Q-Q plot
# <!-- ## TEKSTBLOK: QQplot.R-->
# Gebruik `qqnorm()` en `qqline()` met `pch = 1`om een Q-Q plot te maken, met als datapunten kleine cirkels.
# <!-- ## /TEKSTBLOK: QQplot.R-->
# 
# Als over het algemeen de meeste datapunten op de lijn liggen, neem dan aan dat de data normaal verdeeld zijn.
# <div class = "col-container">
#   <div class="col">
# <!-- ## OPENBLOK: QQplot1.R -->

# In[ ]:


qqnorm(
 Studieuren_lineaire_algebra, pch = 1,
 main = "Normaal Q-Q plot van aantal studieuren Lineaire Algebra",
 ylab = "Kwantielen in data",
 xlab = "Theoretische kwantielen")
qqline(Studieuren_lineaire_algebra)


# <!-- ## /OPENBLOK: QQplot1.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot2.R -->

# In[ ]:


qqnorm(
 Studieuren_relativiteitstheorie, pch = 1,
 main = "Normaal Q-Q plot van aantal studieuren Relativiteitstheorie",
 ylab = "Kwantielen in data",
 xlab = "Theoretische kwantielen")
qqline(Studieuren_relativiteitstheorie)


# <!-- ## /OPENBLOK: QQplot2.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot3.R -->

# In[ ]:


qqnorm(
 Studieuren_kosmologie, pch = 1,
 main = "Normaal Q-Q plot van aantal studieuren Kosmologie",
 ylab = "Kwantielen in data",
 xlab = "Theoretische kwantielen")


qqline(Studieuren_kosmologie)


# <!-- ## /OPENBLOK: QQplot3.R -->
#   </div>
# </div>
# 
# Bij alle drie de Q-Q plots liggen de punten rond de lijn die normaliteit aangeeft; vermoedelijk zijn de studieuren voor elke groep normaal verdeeld.
# 
# ### Boxplot
# De box geeft de middelste 50% van het aantal studieuren per week weer. De zwarte lijn binnen de box is de mediaan. In de staarten of snorreharen zitten de eerste 25% en de laatste 25%. Cirkels visualiseren mogelijke uitbijters.[^9]<sup>, </sup>[^10] Hoe meer de boxen overlappen, hoe waarschijnlijker er geen significant verschil is tussen de groepen van metingen. 
# 
# <!-- ## OPENBLOK: Boxplot.R -->

# In[ ]:


library(graphics)
boxplot(Studieuren ~ Vak, Studieuren_technische_natuurkunde)


# <!-- ## /OPENBLOK: Boxplot.R -->
# 
# De boxplotten geven de spreiding weer van het aantal studieuren voor de drie vakken in de eerste onderwijsperiode: Kosmologie, Lineaire Algebra en Relativiteitstheorie. In het algemeen lijken de vakken een symmetrische verdeling te hebben. De medianen van Kosmologie en Lineaire Algebra liggen een stuk lager dan de mediaan van Relativiteitstheorie. Kosmologie en Relativiteitstheorie hebben mogelijke uitbijters. 

# ## Toetsen van normaliteit
# Om te controleren of de verdelingen van de studieuren voor elk vak normaal verdeeld zijn, kan de normaliteit getoetst worden. Twee veelgebruikte toetsen zijn: de *Kolmogorov-Smirnov test* en de *Shapiro-Wilk test*.
# 
# ### Kolmogorov-Smirnov
# De *Kolmogorov-Smirnov test* toetst het verschil tussen twee verdelingen. Standaard toetst deze test het verschil tussen een normale verdeling en de verdeling van de steekproef. De Lilliefors correctie is vereist als het gemiddelde en de standaardafwijking niet van tevoren bekend of bepaald zijn, wat meestal het geval is bij een steekproef. Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.
# 
# <!-- ## TEKSTBLOK: Lilliefors-test1.R -->
# <!-- ## /TEKSTBLOK: Lilliefors-test1.R -->
# 
# <!-- ## OPENBLOK: Library-nortest.R -->

# In[ ]:


library("nortest")


# <!-- ## /OPENBLOK: Library-nortest.R -->
# 
# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Lilliefors-test-1.R -->

# In[ ]:


lillie.test(Studieuren_lineaire_algebra)


# <!-- ## /OPENBLOK: Lilliefors-test-1.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-2.R -->

# In[ ]:


lillie.test(Studieuren_relativiteitstheorie)


# <!-- ## /OPENBLOK: Lilliefors-test-2.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-3.R -->

# In[ ]:


lillie.test(Studieuren_kosmologie)


# <!-- ## /OPENBLOK: Lilliefors-test-3.R -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor elk vak; er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. [^11] De *repeated measures ANOVA* kan uitgevoerd worden.
# 
# ### Shapiro-Wilk Test
# De *Shapiro-Wilk test* is een soortgelijke toets als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (n < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.
# 
# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.R -->
# ``` {r Shapiro-Wilk Test-3, warning=FALSE}
# shapiro.test(Studieuren_lineaire_algebra)
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-1.R -->
#   </div>
#   <div class= "col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-2.R -->
# ``` {r Shapiro-Wilk Test-2, warning=FALSE}
# shapiro.test(Studieuren_relativiteitstheorie)
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-2.R -->
#   </div>
#   <div class= "col"> 
# <!-- ## OPENBLOK: Shapiro-Wilk-test-3.R -->
# ``` {r Shapiro-Wilk Test-1, warning=FALSE}
# shapiro.test(Studieuren_kosmologie)
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-3.R -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor elk vak, dus er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling.[^11] De *repeated measures ANOVA* kan uitgevoerd worden.

# ## Repeated measures ANOVA 
# 
# <!-- ## TEKSTBLOK: repeatedmeasuresANOVA1.R -->
# Voer de *repeated measures ANOVA* uit om de vraag te beantwoorden of er verschillen zijn tussen het aantal studieuren voor de vakken in de eerste onderwijsperiode van het eerste jaar van de bachelor Technische Natuurkunde. Gebruik de functie `ezANOVA()` van het package `ez` met als argumenten de dataset `Studieuren_technische_natuurkunde`, de afhankelijke variabele `dv = Studieuren`, de variabele die de deelnemers aangeeft `wid = Studentnummer` en de onafhankelijke variabele `within = Vak`.
# <!-- ## /TEKSTBLOK: repeatedmeasuresANOVA1.R -->
# 
# <!-- ## OPENBLOK: repeatedmeasuresANOVA2.R -->

# In[ ]:


library(ez)
ezANOVA(Studieuren_technische_natuurkunde, dv = Studieuren, wid = Studentnummer,
               within = Vak)


# <!-- ## /OPENBLOK: repeatedmeasuresANOVA2.R -->
# 
# <!-- ## CLOSEDBLOK: repeatedmeasuresANOVA3.R -->

# In[ ]:


library(ez)
obj <- ezANOVA(Studieuren_technische_natuurkunde, dv = Studieuren, wid = Studentnummer,
               within = Vak)
Mauchly_W <- Round_and_format(obj$`Mauchly's Test for Sphericity`$W)
v_F <- Round_and_format(obj$ANOVA$F)
eta2 <- Round_and_format(obj$ANOVA$ges)


# <!-- ## /CLOSEDBLOK: repeatedmeasuresANOVA3.R -->
# 
# <!-- ## TEKSTBLOK: repeatedmeasuresANOVA4.R -->
# 
# * *Mauchly's test* toont aan dat de assumptie van sphericiteit stand houdt in deze casus ($\chi^2$ = `r Mauchly_W`, *p* = 0,297). Er is geen correctie nodig.
# * De resultaten van de repeated measures ANOVA zijn *F* = `r v_F`, *p* < 0,0001, *η^2^* = `r eta2`
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^11]
# * Er is een significant verschil tussen het aantal studieuren voor de drie vakken in de eerste onderwijsperiode; het effect van de verschillende vakken op het aantal studieuren is groot.
# 
# <!-- ## /TEKSTBLOK: repeatedmeasuresANOVA4.R -->
# 
# ## Post-hoc toets
# <!-- ## TEKSTBLOK: posthoc1.R -->
# Voer post-hoc toetsen uit om te onderzoeken welke vakken uit de eerste onderwijsperiode van elkaar verschillen wat betreft het aantal studieuren dat eerstejaars studenten van de bachelor Technische Natuurkunde hieraan besteden. Gebruik hiervoor de functie `pairwise.t.test()` met als argumenten de afhankelijk variabele `Studieuren_technische_natuurkunde$Studieuren`, de onafhankelijke variabele `Studieuren_technische_natuurkunde$Vak`, het argument `paired = TRUE` om aan te geven dat er een gepaarde vergelijking gemaakt wordt en de gebruikte methode om te corrigeren voor meerdere toetsen `p.adjust.method = "bonferroni"`.
# <!-- ## /TEKSTBLOK: posthoc1.R -->
# 
# <!-- ## OPENBLOK: posthoc2.R -->

# In[ ]:


# Bereken de verschillen in gemiddelde tussen de drie vakken
Verschil_gemiddelde_LA_RT <- mean(Studieuren_lineaire_algebra) - mean(Studieuren_relativiteitstheorie)
Verschil_gemiddelde_RT_KL <- mean(Studieuren_relativiteitstheorie) - mean(Studieuren_kosmologie)
Verschil_gemiddelde_KL_LA <- mean(Studieuren_kosmologie) - mean(Studieuren_lineaire_algebra)

# Bereken de p-waarden van de post-hoc toets
pairwise.t.test(Studieuren_technische_natuurkunde$Studieuren, 
                Studieuren_technische_natuurkunde$Vak,
                paired = TRUE,
                p.adjust.method = "bonferroni")


# <!-- ## /OPENBLOK: posthoc2.R -->
# 
# <!-- ## CLOSEDBLOK: posthoc3.R -->

# In[ ]:


# Bereken de verschillen in gemiddelde tussen de drie vakken
Mu_diff_LA_RT <- Round_and_format(mean(Studieuren_lineaire_algebra) - mean(Studieuren_relativiteitstheorie))
Mu_diff_RT_KL <- Round_and_format(mean(Studieuren_relativiteitstheorie) - mean(Studieuren_kosmologie))
Mu_diff_KL_LA <- Round_and_format(mean(Studieuren_kosmologie) - mean(Studieuren_lineaire_algebra))

# Bereken de p-waarden van de post-hoc toets
phtest <- pairwise.t.test(Studieuren_technische_natuurkunde$Studieuren, 
                Studieuren_technische_natuurkunde$Vak,
                paired = TRUE,
                p.adjust.method = "bonferroni")


# <!-- ## /CLOSEDBLOK: posthoc3.R -->
# 
# <!-- ## TEKSTBLOK: posthoc4.R -->
# * Er is een significant verschil tussen Lineaire algebra en Relativiteitstheorie, *MD* = `r Mu_diff_LA_RT`, *p* < 0,0001
# * Er is een significant verschil tussen Relativiteitstheorie en Kosmologie, *MD* = `r Mu_diff_RT_KL`, *p* < 0,0001
# * Er is een significant verschil tussen Kosmologie en Lineaire algebra, *MD* = `r Mu_diff_KL_LA`, *p* = 0,012
# 
# <!-- ## /TEKSTBLOK: posthoc4.R -->

# # Rapportage
# 
# <!-- ## TEKSTBLOK: rapportage.R -->
# Een *repeated measures ANOVA* is uitgevoerd om te onderzoeken of er verschillen zijn tussen het aantal studieuren dat eerstejaars studenten van de bachelor Technische Natuurkunde besteden aan de vakken in de eerste onderwijsperiode. De vakken zijn Lineaire Algebra, Relativiteitstheorie en Kosmologie; beschrijvende statistieken zijn te vinden in Tabel 1. De data voldoet aan de assumptie van sphericiteit ($\chi^2$ = `r Mauchly_W`, p = 0,0297), daarom is er geen correctie gebruikt. Het aantal studieuren voor de drie vakken in de eerste onderwijsperiode verschilt significant van elkaar, *F* = `r v_F`, p < 0,0001, *η^2^* = `r eta2`. De sterkte van het effect van het vak op het aantal studieuren is groot. Post-hoc toetsen - waarbij een Bonferroni correctie is toegepast om te corrigeren voor meerdere toetsen -  tonen aan dat het aantal studieuren voor het vak Relativiteitstheorie significant verschilt van het aantal studieuren voor zowel het vak Lineaire Algebra als Kosmologie (voor beide p < 0,0001) en dat er een significant verschil is tussen de vakken Lineaire Algebra en Kosmologie (p = 0,012). De resultaten suggereren dat eerstejaars studenten van de bachelor Technische Natuurkunde de meeste uren steken in het vak Relativiteitstheorie en daarna iets meer uren in het vak Kosmologie dan dan in het vak Lineaire Algebra.
# 
# | Opleiding     | M          | SD          | N          |
# | ------------- | ---------- | ---------- | ----------- |
# | Lineaire Algebra      | `r vM_LA` | `r vSD_LA` | `r vN_LA` |
# | Relativiteitstheorie  | `r vM_RT` | `r vSD_RT` | `r vN_RT` |
# | Kosmologie            | `r vM_KL` | `r vSD_KL` | `r vN_KL` |
# *Tabel 1. Het gemiddelde aantal studieuren, bijbehorende standaarddeviatie en groepsgrootte voor de vakken in de eerste onderwijsperiode van de bachelor Technische Natuurkunde.*
# <!-- ## /TEKSTBLOK: rapportage.R -->
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Universiteit van Amsterdam (26 augustus 2014). *Repeated-Measures ANOVA*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Repeated-Measures_ANOVA).
# [^2]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^3]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^4]: Laerd statistics (2018). *Testing for Normality using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php. 
# [^5]: Universiteit van Amsterdam (14 juli 2014). *Normaliteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).
# [^6]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^7]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^9]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^10]: Uitbijters kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de uitbijters valide uitbijters zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van uitbijters kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde uitbijters te melden in een rapport. 
# [^11]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^12]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
