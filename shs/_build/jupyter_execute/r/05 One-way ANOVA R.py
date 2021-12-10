#!/usr/bin/env python
# coding: utf-8
---
title: "One-way ANOVA"
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

# In[ ]:


options(width = 80)
## Zodat de TukeyHSD naast elkaar geprint wordt


# <!-- ## OPENBLOK: Data-aanmaken.R -->

# In[ ]:


source(paste0(here::here(),"/01. Includes/data/05.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik de *one-way ANOVA* bij het toetsen of de gemiddelden van twee of meer onafhankelijke groepen verschillen.[^1] 
# 
# # Onderwijscasus
# <div id = "casus">
# Om wervingsactiviteiten beter af te stemmen op de aankomende studenten, wil het hoofd van de afdeling Communicatie weten wat de reistijd (in minuten) is van studenten van verschillende opleidingen. Hij heeft daarom data verzameld over de reistijd van uitwonende studenten voor de opleidingen: Arabische Taal en Cultuur, Filosofie en Geschiedenis. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: De reistijden van de studenten van de drie opleidingen komen uit dezelfde verdeling en hebben dus een gezamenlijk gemiddelde
# 
# *H~A~*: De reistijden van de studenten van de drie opleidingen komen niet uit dezelfde verdeling en hebben dus een verschillend gemiddelde

# # Uitleg assumpties
# Om een valide toetsresultaat te bereiken moet de data aan een aantal voorwaarden voldoen. Controleer of de steekproef aan de volgende assumpties voldoet: normaliteit, homogeniteit van varianties en onafhankelijkheid.
# 
# De *one-way ANOVA* is een robuuste toets: als er niet voldaan is aan de assumptie van normaliteit of homogeniteit van varianties, dan kan de *one-way ANOVA* in bepaalde gevallen nog steeds uitgevoerd en geïnterpreteerd worden.[^2] Hierdoor kan het wel zijn dat de toets minder onderscheidend vermogen heeft, dan wanneer de assumpties niet geschonden worden.[^3]<sup>, </sup>[^4] Als er grote afwijkingen zijn van normaliteit of homogeniteit van varianties, is de [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) een alternatief voor de *one-way ANOVA*.[^5]<sup>, </sup>[^6]
# 
# ## Normaliteit
# De assumptie van normaliteit houdt bij de *one-way ANOVA* in dat de afhankelijke variabele normaal verdeeld is voor elke groep. Controleer de assumptie van normaliteit voor elke groep met de volgende stappen:  
# 1. Controleer de data visueel met een histogram, een boxplot of een Q-Q plot.   
# 2. Toets of de data normaal verdeeld zijn met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (n < 50) met de *Shapiro-Wilk test*.[^7]<sup>, </sup>[^8]  
# 
# De eerste stap heeft als doel een goede indruk te krijgen van de verdeling van de steekproef. In de tweede stap wordt de assumptie van normaliteit getoetst. De statistische toets laat zien of de verdeling van de observaties van een groep voldoet aan de assumptie van normaliteit. Voor alle groepen moet er voldaan zijn aan de assumptie van normaliteit.
# 
# Als er niet voldaan is aan normaliteit, is het transformeren van de data een optie.[^2] Een andere optie is het gebruik van de nonparametrische [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) waar normaliteit geen assumptie is.[^3] De *one-way ANOVA* is echter ook een robuuste toets ten opzichte van de assumptie van normaliteit. Als elke groep een aantal observaties (*n*) heeft dat groter dan 100 is,  ga er dan vanuit dat de *one-way ANOVA* robuust genoeg is om uit te voeren zonder dat de afhankelijke variabele een normale verdeling volgt.
# 
# ## Homogeniteit van varianties
# Toets met de *Levene's Test (for equality of variance)* of de variantie van iedere groep ongeveer hetzelfde is. Bij een p-waarde kleiner dan 0,05 is de variantie van de groepen significant verschillend.[^10] De *one-way ANOVA* is in bepaalde gevallen robuust als er geen homogeniteit van varianties is. Als de ratio van de grootste en kleinste steekproefgrootte van alle groepen kleiner dan 10 is en de ratio van de grootste en kleinste variantie van alle groepen kleiner dan 4 is, dan kan de *one-way ANOVA* gewoon uitgevoerd worden.[^19] Voer de [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) toets uit als er niet aan deze voorwaarden voor robuustheid is voldaan.
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^11] Voor de *one-way ANOVA* wordt de effectmaat eta squared vaak gebruikt.
# 
# De effectmaat eta squared (*η^2^*) berekent de proportie van de variantie in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele. In deze casus berekent het de proportie van de variantie in de lengte van de reistijd die verklaard kan worden door de opleiding. Een indicatie om *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^12]<sup>,</sup>[^13]
# 
# # Post-hoc toetsen
# De *one-way ANOVA* toetst of de groepen afkomstig zijn van eenzelfde verdeling met een gezamenlijk gemiddelde of van verschillende verdeling met een eigen gemiddelde. Voer een post-hoc toets uit om te bepalen welke groepen significant verschillen. De post-hoc toetsen voeren meestal een correctie voor de p-waarden uit, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout).
# 
# Er zijn meerdere post-hoc toetsen. De keuze voor een toets hangt onder andere af van het wel of niet schenden van de assumptie van homogeniteit van varianties:   
# * Gebruik de Tukey Honestly Significant Difference post-hoc toets bij gelijke variantie.[^14]  
# * Gebruik de Games-Howell post-hoc toets bij ongelijke variantie.[^15]  
# 
# # Toetsing assumpties
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset ingeladen met de reistijden van uitwonende studenten per opleiding genaamd `Reistijd_per_opleiding`. 
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
head(Reistijd_per_opleiding)

## Laatste 5 observaties
tail(Reistijd_per_opleiding)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# <!-- ## TEKSTBLOK: Data-bekijken2.R-->
# De dataset bevat gegevens van studenten van verschillende opleidingen. Gebruik `unique()` om te onderzoeken welke opleidingen er in de data aanwezig zijn. 
# <!-- ## /TEKSTBLOK: Data-bekijken2.R-->
# <!-- ## OPENBLOK: Data-bekijken2.R -->

# In[ ]:


## Unieke opleidingen
unique(Reistijd_per_opleiding$Opleiding)


# <!-- ## /OPENBLOK: Data-bekijken2.R -->
# 
# Selecteer de drie groepen en sla deze op in een vector om deze makkelijker aan te kunnen roepen. 
# <!-- ## OPENBLOK: Data-selecteren.R -->

# In[ ]:


Reistijd_ATC <- Reistijd_per_opleiding$Reistijd[Reistijd_per_opleiding$Opleiding == "Arabische Taal en Cultuur"]
Reistijd_FIL <- Reistijd_per_opleiding$Reistijd[Reistijd_per_opleiding$Opleiding == "Filosofie"]
Reistijd_GSC <- Reistijd_per_opleiding$Reistijd[Reistijd_per_opleiding$Opleiding == "Geschiedenis"]


# <!-- ## /OPENBLOK: Data-selecteren.R -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# Bekijk de beschrijvende statistieken per groep om meer inzicht te krijgen in de data. Gebruik hiervoor de functie `descr` en `stby` van het package `summarytools` om de beschrijvende statistieken per groep weer te geven. Voer de gewenste statistieken in met het argument `stats = c("mean", "sd", "n.valid")`.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-inladen.R -->
# 
# <!-- ## /OPENBLOK: Data-beschrijven-inladen.R -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-1.R -->

# In[ ]:


library(summarytools)

with(Reistijd_per_opleiding, 
     stby(data = Reistijd, 
          list(Opleiding), 
          descr, 
          stats = c("mean", "sd", "n.valid")))


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
# 
# <!-- ## CLOSEDBLOK: Data-beschrijven-11.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Data-beschrijven-11.R -->
# 
# <!-- ## CLOSEDBLOK: Data-beschrijven.R -->

# In[ ]:


vM_ATC  <- Round_and_format(mean(Reistijd_ATC))
vSD_ATC <- Round_and_format(sd(Reistijd_ATC))
vN_ATC  <- Round_and_format(length(Reistijd_ATC))

vM_FIL  <- Round_and_format(mean(Reistijd_FIL))
vSD_FIL <- Round_and_format(sd(Reistijd_FIL))
vN_FIL  <- Round_and_format(length(Reistijd_FIL))

vM_GSC  <- Round_and_format(mean(Reistijd_GSC))
vSD_GSC <- Round_and_format(sd(Reistijd_GSC))
vN_GSC  <- Round_and_format(length(Reistijd_GSC))


# <!-- ## /CLOSEDBLOK: Data-beschrijven.R -->
# 
# <!-- ## TEKSTBLOK: Datatekst-beschrijven.R -->
# * Gemiddelde reistijd Arabische Taal en Cultuur (standaarddeviatie): `r vM_ATC` (`r vSD_ATC`). *n* = `r vN_ATC`  
# * Gemiddelde reistijd Filosofie (standaarddeviatie): `r vM_FIL` (`r vSD_FIL`). *n* = `r vN_FIL`.
# * Gemiddelde reistijd Geschiedenis (standaarddeviatie): `r vM_GSC` (`r vSD_GSC`). *n* = `r vN_GSC`.
# 
# <!-- ## /TEKSTBLOK: Datatekst-beschrijven.R -->
# 
# ## Visuele inspectie van normaliteit
# Geef de verdeling van de reistijd voor elke opleiding visueel weer met een histogram, Q-Q plot en boxplot.
# 
# ### Histogram
# 
# Focus bij het analyseren van een histogram[^20] op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters. Een normale verdeling is symmetrisch, heeft één top en geen uitbijters.[^16]<sup>, </sup>[^17]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot
library(ggplot2)

ggplot(Reistijd_per_opleiding,
  aes(x = Reistijd)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 5,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Opleiding) +
  geom_density(alpha = .2, adjust = 1) +
  ylab("Frequentiedichtheid") +
  labs(title = "Reistijd per opleiding")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# De verdelingen van de opleidingen Filosofie en Geschiedenis lijken twee toppen te hebben. Alle drie de opleidingen hebben een niet geheel symmetrische verdeling, maar vertonen ook geen uitbijters. De verdeling van de opleiding Arabische taal en Cultuur is bij benadering normaal; voor de opleidingen Filosofie en Geschiedenis zijn lichte afwijkingen van de normale verdeling te zien.
# 
# ### Q-Q plot
# <!-- ## TEKSTBLOK: QQplot.R-->
# Gebruik `qqnorm()` en `qqline()` met `pch = 1`om een Q-Q plot te maken, met als datapunten kleine cirkels.
# <!-- ## /TEKSTBLOK: QQplot.R-->
# 
# Als over het algemeen de meeste datapunten op de lijn liggen, neem dan aan dat de data normaal verdeeld is.
# <div class = "col-container">
#   <div class="col">
# <!-- ## OPENBLOK: QQplot1.R -->

# In[ ]:


qqnorm(
 Reistijd_ATC, pch = 1,
 main = "Normaal Q-Q plot van reistijd Arabische Taal en Cultuur",
 ylab = "Kwantielen in data",
 xlab = "Theoretische kwantielen")

qqline(Reistijd_ATC)


# <!-- ## /OPENBLOK: QQplot1.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot2.R -->

# In[ ]:


qqnorm(
 Reistijd_FIL, pch = 1,
 main = "Normaal Q-Q plot van reistijd Filosofie",
 ylab = "Kwantielen in data",
 xlab = "Theoretische kwantielen")

qqline(Reistijd_FIL)


# <!-- ## /OPENBLOK: QQplot2.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot3.R -->

# In[ ]:


qqnorm(
 Reistijd_GSC, pch = 1,
 main = "Normaal Q-Q plot van reistijd Geschiedenis",
 ylab = "Kwantielen in data",
 xlab = "Theoretische kwantielen")

qqline(Reistijd_GSC)


# <!-- ## OPENBLOK: QQplot3.R -->
#   </div>
# </div>
# Bij alle drie de verdelingen liggen de meeste datapunten op of vlakbij de lijn. Hoewel er bij de uiteinden van de verdeling wat afwijkingen zijn, duidt deze grafiek op een goede benadering van de normaalverdeling voor de drie verdelingen.

# ### Boxplot
# De box geeft de middelste 50% van de reistijd weer. De zwarte lijn binnen de box is de mediaan. In de staarten of snorreharen zitten de eerste 25% en de laatste 25%. Cirkels visualiseren mogelijke uitbijters.[^16]<sup>, </sup>[^17] Hoe meer de boxen overlappen, hoe waarschijnlijker er geen significant verschil is tussen de groepen. 
# 
# <!-- ## OPENBLOK: Boxplot.R -->

# In[ ]:


library(graphics)
boxplot(Reistijd ~ Opleiding, Reistijd_per_opleiding)


# <!-- ## /OPENBLOK: Boxplot.R -->
# 
# De boxplotten geven de spreiding weer van de gemiddelde reistijd van uitwonende studenten voor de opleidingen Arabische Taal en Cultuur, Filosofie en Geschiedenis. De boxplotten Arabische Taal en Cultuur en Geschiedenis zien er symmetrisch uit; de boxen zijn even hoog boven als onder de mediaan en de snorreharen zijn onder en boven even groot. De boxplot van Filosofie is boven de mediaan groter dan onder de mediaan, de data kan wat scheef verdeeld zijn. De mediaan Arabische Taal en Cultuur ligt hoger dan de twee andere opleidingen.
# 
# ## Toetsen van normaliteit
# Om te controleren of de data normaal verdeeld is, kan de normaliteit getoetst worden. Twee veelgebruikte toetsen zijn: de *Kolmogorov-Smirnov test* en de *Shapiro-Wilk test*.
# 
# ### Kolmogorov-Smirnov
# De *Kolmogorov-Smirnov test* toetst het verschil tussen twee verdelingen. Standaard toetst deze toets het verschil tussen een normale verdeling en de verdeling van de steekproef. De Lilliefors correctie is vereist als het gemiddelde en de standaardafwijking niet van tevoren bekend of bepaald zijn, wat meestal het geval is bij een steekproef. Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.
# 
# <!-- ## TEKSTBLOK: Lilliefors-test1.R -->
# 
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


lillie.test(Reistijd_ATC)


# <!-- ## OPENBLOK: Lilliefors-test-1.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-2.R -->

# In[ ]:


lillie.test(Reistijd_FIL)


# <!-- ## OPENBLOK: Lilliefors-test-2.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-3.R -->

# In[ ]:


lillie.test(Reistijd_GSC)


# <!-- ## /OPENBLOK: Lilliefors-test-3.R -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor elke groep; er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. [^18] De *one-way ANOVA* kan uitgevoerd worden.
# 
# ### Shapiro-Wilk Test
# De *Shapiro-Wilk test* is een soortgelijke toets als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (*n* < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.
# 
# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-3.R -->
# ``` {r Shapiro-Wilk Test-3, warning=FALSE}
# shapiro.test(Reistijd_GSC)
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-3.R -->
#   </div>
#   <div class= "col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-2.R -->
# ``` {r Shapiro-Wilk Test-2, warning=FALSE}
# shapiro.test(Reistijd_FIL)
# ```
# <!-- ## OPENBLOK: Shapiro-Wilk-test-2.R -->
#   </div>
#   <div class= "col"> 
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.R -->
# ``` {r Shapiro-Wilk Test-1, warning=FALSE}
# shapiro.test(Reistijd_ATC)
# ```
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.R -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor elke groep, dus er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. De *one-way ANOVA* kan uitgevoerd worden.
# 
# ## Toetsen van Homogeniteit van varianties
# Toets met de *Levene's test* de homogeniteit van varianties. Gebruik hiervoor de functie `leveneTest()` van het package `car` met als eerst argument de afhankelijke variabele `Reistijd_per_opleiding$Reistijd` en als tweede argument de onafhankelijke variabele `Reistijd_per_opleiding$Opleiding`.
# 
# <!-- ## OPENBLOK: Levenes-test.R -->

# In[ ]:


library(car)
leveneTest(Reistijd_per_opleiding$Reistijd, Reistijd_per_opleiding$Opleiding)


# <!-- ## /OPENBLOK: Levenes-test.R -->
# <!-- ## CLOSEDBLOK: Levenes-test.R -->

# In[ ]:


L <- leveneTest(Reistijd_per_opleiding$Reistijd, Reistijd_per_opleiding$Opleiding)
vF_waarde <- Round_and_format(L$`F value`[1])
vF_p <- Round_and_format(L$`Pr(>F)`[1])
vDF1 <- Round_and_format(L$`Df`[1])
vDF2 <- Round_and_format(L$`Df`[2])


# <!-- ## /CLOSEDBLOK: Levenes-test.R -->
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# * *F*~`r vDF1`~~,~~`r vDF2`~ = `r vF_waarde`, p-waarde = `r vF_p`, 
# * De p-waarde is groter dan 0,05, dus er is geen significant verschil gevonden tussen de groepen in variantie.
# * Vrijheidsgraden bestaan uit twee cijfers: het eerste cijfer (het aantal groepen - 1 = `r vDF1`) en het tweede cijfer (*n~1~* + *n~2~*+*n~3~* - 3 = `r vDF2`).  
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# 
# # One-way ANOVA 
# Voer de *one-way ANOVA* uit om de vraag te beantwoorden of de gemiddelde reistijd van de studenten per opleiding verschilt.  
# <!-- ## TEKSTBLOK: ANOVA-toets.R -->
# Gebruik `aov()` om een ANOVA-object (`aov`) te creëren. Het eerste argument bestaat uit de afhankelijke variabele `Reistijd` en de groepvariabele `Opleiding`; het tweede argument bevat de dataset `Reistijd_per_opleiding`.  Geef het resultaat weer met `summary()`.
# <!-- ## /TEKSTBLOK: ANOVA-toets.R -->
# <!-- ## OPENBLOK: ANOVA-toets.R -->

# In[ ]:


res.aov <- aov(Reistijd ~ Opleiding, Reistijd_per_opleiding)
summary(res.aov)


# <!-- ## /OPENBLOK: ANOVA-toets.R -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets.R -->

# In[ ]:


ANOVA <- summary(res.aov)
vF_waarde <- Round_and_format(ANOVA[[1]]$`F value`[1])


# <!-- ## /CLOSEDBLOK: ANOVA-toets.R -->
# 
# <!-- ## TEKSTBLOK: Eta-squared-tekst.R -->
# Gebruik `EtaSq()` van het package `DescTools` met als argument het ANOVA_object `res.aov` om de effectmaat eta squared te berekenen.
# <!-- ## /TEKSTBLOK: Eta-squared-tekst.R -->
# 
# <!-- ## OPENBLOK: Eta-squared.R --> 

# In[ ]:


library(DescTools)
EtaSq(res.aov)


# <!-- ## /OPENBLOK: Eta-squared.R -->
# <!-- ## CLOSEDBLOK: Eta-squared.R -->

# In[ ]:


Esq <- Round_and_format(EtaSq(res.aov)[1])


# <!-- ## /CLOSEDBLOK: Eta-squared.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets1.R -->
# * *F* ~`r vDF1`~~,~~`r vDF2`~ = `r vF_waarde`, *p* < 0,0001, *η^2^* = `r Esq`.
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^18] 
# * Vrijheidsgraden: het aantal groepen - 1 = `r vDF1`; *n~1~* + *n~2~* + *n~3~*- 3 = `r vDF2`.
# * De sterkte van het effect van de type opleiding op de reistijd is groot.
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets1.R -->
# 
# # Post-hoc toets: Tukey's toets
# 
# <!-- ## TEKSTBLOK: Tukey-HSD.R -->
# Voer een Tukey Honestly Significant Difference post-hoc toets uit om te bepalen welke van de type opleidingen in reistijd verschillen. Deze post-hoc toets wordt gebruikt omdat er voldaan is aan de assumptie van homogeniteit van varianties. Gebruik `TukeyHSD()` op de uitkomsten van de *one-way ANOVA*, het ANOVA-object `res.aov`.
# <!-- ## /TEKSTBLOK: Tukey-HSD.R -->
# 
# <!-- ## OPENBLOK: Tukey-HSD.R -->

# In[ ]:


TukeyHSD(res.aov)


# <!-- ## /OPENBLOK: Tukey-HSD.R -->
# <!-- ## CLOSEDBLOK: Tukey-HSD.R -->

# In[ ]:


THSD <- TukeyHSD(res.aov)
vATCvsFIL <- Round_and_format(THSD$Opleiding[1,1])
vATCvsGSC <- Round_and_format(THSD$Opleiding[2,1])
vFILvsGSC <- Round_and_format(THSD$Opleiding[3,1])
vpFILvsGSC <- Round_and_format(THSD$Opleiding[3,4])


# <!-- ## /CLOSEDBLOK: Tukey-HSD.R -->
# <!-- ## TEKSTBLOK: Tukey-HSD1.R -->
# 
# * Het verschil tussen Filosofie en Arabische Taal en Cultuur is *MD* = `r vATCvsFIL`, *p* < 0,0001.  
# * Het verschil tussen Geschiedenis en Arabische Taal en Cultuur is *MD* = `r vATCvsGSC`, *p* < 0,0001.
# * Het verschil tussen Geschiedenis en Filosofie is *MD* = `r vFILvsGSC`, *p* = `r vpFILvsGSC`.  
# 
# <!-- ## /TEKSTBLOK: Tukey-HSD1.R -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# Een *one-way ANOVA* is uitgevoerd om te toetsen of de gemiddelde reistijd van de studenten per opleiding gelijk is aan elkaar. De opleidingen zijn Arabische Taal en Cultuur (*M~atc~* = `r vM_ATC`, *SD~atc~* = `r vSD_ATC`), Filosofie (*M~fil~* = `r vM_FIL`, *SD~fil~* = `r vSD_FIL`) en Geschiedenis (*M~gsc~* = `r vM_GSC`, *SD~fil~* = `r vSD_GSC`); beschrijvende statistieken zijn ook te vinden in Tabel 1. De gemiddelde reistijd van de groepen verschilt significant van elkaar, *F*(`r vDF1`, `r vDF2`) = `r vF_waarde`, *p* < 0,0001, *η^2^* = `r Esq`. De sterkte van het effect van de type opleiding op de reistijd is groot.
# 
# | Opleiding     | N          | M          | SD          |
# | ------------- | ---------- | ---------- | ----------- |
# | Arabisch      | `r vN_ATC` | `r vM_ATC` | `r vSD_ATC` |
# | Filosofie     | `r vN_FIL` | `r vM_FIL` | `r vSD_FIL` |
# | Geschiedenis  | `r vN_GSC` | `r vM_GSC` | `r vSD_GSC` |
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# *Tabel 1. Groepsgrootte, gemiddelde reistijd en standaarddeviatie per opleiding*
# <!-- ## TEKSTBLOK: Rapportage-tukey.R -->
# 
# De Tukey Honest Significant Differences post-hoc toets is uitgevoerd om te toetsen welke van de drie gemiddelden significant verschillen. De gemiddelde reistijd van studenten Filosofie is significant lager dan de reistijd van studenten Arabische Taal en Cultuur (*MD* = `r vATCvsFIL`, *p* < 0,0001). De reistijd voor studenten Geschiedenis is ook significant lager dan de reistijd voor studenten Arabische Taal en Cultuur (*MD* = `r vATCvsGSC`, *p* < 0,0001). De reistijd van studenten Geschiedenis en studenten Filosofie is niet significant verschillend (*MD* = `r vFILvsGSC`, *p* = `r vpFILvsGSC`). Aan de hand van de resultaten kan geconcludeerd worden dat de studenten van Arabische Taal en Cultuur langer moeten reizen dan de andere twee opleidingen en dat er geen verschil lijkt te zijn in de reistijd van de studenten Filosofie en Geschiedenis.
# <!-- ## /TEKSTBLOK: Rapportage-tukey.R -->

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Van Geloven, N. (25 mei 2016). *One-way ANOVA*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/One-way_ANOVA).
# [^2]: Universiteit van Amsterdam (8 juli 2014). *One-way ANOVA*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/One-way_ANOVA).
# [^3]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.  
# [^4]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^5]: Van Geloven, N. (21 maart 2018). *Kruskal Wallis*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Kruskal_Wallis).
# [^6]: De [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) maakt een rangschikking van de data. Hierdoor is de toets verdelingsvrij en is normaliteit geen assumptie. Ook zijn uitbijters minder van invloed op het eindresultaat. Toch wordt er voor deze toets minder vaak gekozen, omdat bij het maken van een rankschikking de dataset informatie verliest. Als de data wel normaal verdeeld zijn, heeft de [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) minder onderscheidend vermogen dan wanneer de *one-way ANOVA* uitgevoerd zou worden.
# [^7]: Laerd statistics (2018). *Testing for Normality using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php. 
# [^8]: Universiteit van Amsterdam (14 juli 2014). *Normaliteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).
# [^9]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^10]: Wikipedia (7 september 2019). *Analysis of variance*. https://en.wikipedia.org/wiki/Analysis_of_variance.
# [^11]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^12]: Watson, P. (30 oktober 2019). *Rules of thumb on magnitudes of effect sizes*. [MRC Cognition and Brain Sciences Unit Wiki](http://imaging.mrc-cbu.cam.ac.uk/statswiki/FAQ/effectSize).
# [^13]: Eta-squared. (2019 May 14). Retrieved from: https://en.wikiversity.org/wiki/Eta-squared.
# [^14]: Universiteit van Amsterdam (26 augustus 2014). *MANOVA*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/MANOVA).
# [^15]: Marshall, E., & Boggis, E. (2016). *The statistics tutor’s quick guide to commonly used statistical tests*. http://www.statstutor.ac.uk/resources/uploaded/tutorsquickguidetostatistics.pdf. 
# [^16]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^17]: Uitbijters kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de uitbijters valide uitbijters zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van uitbijters kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde uitbijters te melden in een rapport. 
# [^18]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^19]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 86.
# [^20]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
# 
