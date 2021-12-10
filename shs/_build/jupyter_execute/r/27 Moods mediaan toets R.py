#!/usr/bin/env python
# coding: utf-8
---
title: "Mood's mediaan toets"
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


source(paste0(here::here(),"/01. Includes/data/08.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# # Toepassing
# <!-- ## TEKSTBLOK: link1.R-->
# Gebruik *Mood's mediaan toets* om de medianen van twee ongepaarde groepen te vergelijken.[^1]<sup>,</sup>[^2] Deze toets wordt gebruikt als er niet aan de assumpties is voldaan bij sterkere toetsen zoals de [ongepaarde t-toets](02-Ongepaarde-t-toets-R.html) en de [Mann-Whitney U toets](08-Mann-Whitney-U-toetsI-R.html). Als de verdelingen van beide groepen bij benadering normaal verdeeld zijn, dan kan de [ongepaarde t-toets](02-Ongepaarde-t-toets-R.html) gebruikt worden om de gemiddelden te vergelijken. Als de verdelingen van beide groepen dezelfde vorm hebben, kan de [Mann-Whitney U toets](08-Mann-Whitney-U-toetsI-R.html) gebruikt worden om de medianen te vergelijken.[^3] De [Mann-Whitney U toets](08-Mann-Whitney-U-toetsI-R.html) heeft in dat geval een hoger onderscheidend vermogen[^2].

# <!-- ## /TEKSTBLOK: link1.R-->

# # Onderwijscasus
# <div id ="casus">
# De onderwijsdirecteur van de opleiding Business Administration van een hogeschool vraagt zich af of er verschil is in de studieresultaten van studenten met een Nederlandse vooropleiding en een buitenlandse vooropleiding. Met name in het tweede studiejaar lijken er verschillen op te treden die hij wil begrijpen om mogelijke interventies met zijn docenten te bespreken. Hij vraagt zich af: ‘Verschilt het aantal studiepunten in het tweede studiejaar van studenten met een Nederlandse vooropleiding van het aantal studiepunten in het tweede studiejaar van studenten met een buitenlandse vooropleiding?
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: De verdeling van het behaalde aantal studiepunten in het tweede jaar van studenten met een buitenlandse vooropleiding is hetzelfde als de verdeling van studenten met een Nederlandse vooropleiding. 
# 
# *H~A~*: De verdeling van het behaalde aantal studiepunten in het tweede jaar van studenten met een buitenlandse vooropleiding is anders dan de verdeling van studenten met een Nederlandse vooropleiding.
# </div>
# 
# # Assumpties
# 
# Het meetniveau van de afhankelijke variabele is continu.[^5]<sup>,</sup>[^6] 
# 
# ## Groepsgroottes
# 
# <!-- ## TEKSTBLOK: link2.R-->
# *Mood's mediaan toets* toetst het verschil tussen de medianen van twee ongepaarde groepen. Eerst wordt de mediaan berekend van de samengevoegde observaties van beide groepen. Daarna worden voor beide ongepaarde groepen het aantal observaties groter dan en kleiner dan of gelijk aan de mediaan geteld. Dit levert een kruistabel op die vervolgens getoetst kan worden met de [Chi-kwadraat toets voor onafhankelijkheid](13-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fishers-exact-toets-R.html). Een voorbeeld van zo'n kruistabel is te zien in Tabel 1.
# <!-- ## /TEKSTBLOK: link2.R-->
# 
# |                      | Groep 1    | Groep 2 | 
# | -------------------- | ---------- | ------------| 
# | Aantal observaties groter dan mediaan  | 20   | 25          | 
# | Aantal observaties kleiner dan of gelijk aan mediaan  | 30   | 40          |
# *Tabel 1. Kruistabel met aantal observaties groter dan en kleiner dan of gelijk aan mediaan voor twee ongepaarde groepen.*
# 
# <!-- ## TEKSTBLOK: link3.R-->
# Een assumptie van de *Chi-kwadraat toets voor onafhankelijk* is dat niet meer dan 20% van de cellen van de kruistabel een verwacht aantal observaties van vijf of minder heeft. Als dit niet het geval is, is *Fisher's exact toets* een beter alternatief. Zie de toetspagina van de [Chi-kwadraat toets voor onafhankelijkheid](13-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fishers-exact-toets-R.html) voor een uitgebreide uitleg over deze assumptie. 
# <!-- ## /TEKSTBLOK: link3.R-->
# 
# # Uitvoering 
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset `Studiepunten_studiejaar2` ingeladen met het aantal punten dat studenten in het tweede jaar halen.
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Studiepunten_studiejaar2)
## Eerste 6 observaties
tail(Studiepunten_studiejaar2)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# Bekijk de grootte, de mediaan en de kwantielen van het aantal studiepunten met `length()` en `quantile()`. De mediaan en kwantielen worden vaak gebruikt als maat wanneer een verdeling niet symmetrisch is.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# <!-- ## OPENBLOK: Data-selecteren.R -->

# In[ ]:


Vooropleiding_Nederlands <- Studiepunten_studiejaar2$Vooropleiding == "Nederlands"


# <!-- ## /OPENBLOK: Data-selecteren.R -->
# 
# <!-- ## OPENBLOK: Numpy-inladen.R -->
# 
# <!-- ## /OPENBLOK: Numpy-inladen.R -->
# 
# <div class="col-container">
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-1.R -->

# In[ ]:


length(Studiepunten_studiejaar2$Studiepunten[Vooropleiding_Nederlands])
quantile(Studiepunten_studiejaar2$Studiepunten[Vooropleiding_Nederlands])


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
#   </div>
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-2.R -->
# ``````{r Data beschrijven 2, collapse=TRUE}
# length(Studiepunten_studiejaar2$Studiepunten[!Vooropleiding_Nederlands])
# quantile(Studiepunten_studiejaar2$Studiepunten[!Vooropleiding_Nederlands])
# ```
# <!-- ## /OPENBLOK: Data-beschrijven-2.R -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven-3.R -->
# ``` {r data beschrijven als object, include=FALSE, echo=TRUE}
# Vooropleiding_Nederlands <- Studiepunten_studiejaar2$Vooropleiding == "Nederlands"
# 
# vN_NL <- length(Studiepunten_studiejaar2$Studiepunten[Vooropleiding_Nederlands])
# vQ_NL <- quantile(Studiepunten_studiejaar2$Studiepunten[Vooropleiding_Nederlands])
# 
# vN_Inter <- length(Studiepunten_studiejaar2$Studiepunten[!Vooropleiding_Nederlands])
# vQ_Inter <- quantile(Studiepunten_studiejaar2$Studiepunten[!Vooropleiding_Nederlands])
# 
# vN_NL <- Round_and_format(vN_NL)
# vN_Inter <- Round_and_format(vN_Inter)
# 
# vQ1_NL <- Round_and_format(vQ_NL[2])
# vQ1_Inter <- Round_and_format(vQ_Inter[2])
# 
# vMed_NL <- Round_and_format(vQ_NL[3])
# vMed_Inter <- Round_and_format(vQ_Inter[3])
# 
# vQ3_NL <- Round_and_format(vQ_NL[4])
# vQ3_Inter <- Round_and_format(vQ_Inter[4])
# ```
# <!-- ## /CLOSEDBLOK: Data-beschrijven-3.R -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven2.R -->
# * Mediaan studenten Nederlandse vooropleiding: `r vMed_NL`, *n* = `r vN_NL`.
# * Mediaan studenten buitenlandse vooropleiding: `r vMed_Inter`, *n* = `r vN_Inter`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven2.R -->

# ## De data visualiseren
# 
# Maak een histogram[^18] om de verdeling van het aantal studiepunten in het tweede jaar voor studenten met een Nederlandse en buitenlandse vooropleiding visueel weer te geven.
# 
# <!-- ## OPENBLOK: Histogram1.R -->

# In[ ]:


## Histogram met ggplot2
library(ggplot2)

ggplot(Studiepunten_studiejaar2,
  aes(x = Studiepunten)) +
  geom_histogram(aes(y = ..density..),
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Vooropleiding, labeller = labeller(Vooropleiding = c(Nederlands = "Nederlandse vooropleiding", buitenlands = "Buitenlandse vooropleiding"))) +
  ylab("Frequentie") +
  labs(title = "Studiepunten van studenten Business Administration in het tweede jaar ")


# <!-- ## /OPENBLOK: Histogram1.R -->
# 
# Beide histogrammen bevatten een grote groep studenten met een laag aantal studiepunten (twaalf of minder). De overige studenten volgen een ietwat scheve verdeling met de top rond de vijftig studiepunten. De verdelingen van beide groepen studenten hebben echter niet dezelfde vorm. De frequentiedichtheid van het aantal studenten rond de vijftig studiepunten is veel hoger voor de studenten met Nederlandse vooropleiding, terwijl de frequentiedichtheid van het aantal studenten met twaalf of minder studiepunten juist hoger is voor de studenten met een buitenlandse vooropleiding.

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: groepsgrootte1.R -->
# Maak een kruistabel met het aantal observaties hoger en lager dan de mediaan voor beide ongepaarde groepen. Bereken vervolgens de verwachte aantallen observaties met `chisq.test()$expected` met als argument de kruistabel `Kruistabel`.
# <!-- ## /TEKSTBLOK: groepsgrootte1.R -->
# 
# <!-- ## OPENBLOK: groepsgrootte2.R -->

# In[ ]:


# Bereken de mediaan van alle observaties samengevoegd
Mediaan <- median(Studiepunten_studiejaar2$Studiepunten)

# Bepaal voor elke observatie of deze hoger of lager/gelijk aan de mediaan is
Index_hoger_lager <- Studiepunten_studiejaar2$Studiepunten > Mediaan 

# Maak een kruistabel
Kruistabel <- table(Index_hoger_lager, Studiepunten_studiejaar2$Vooropleiding)

# Print de kruistabel
print(Kruistabel)

# Bereken de verwachte aantallen observaties
chisq.test(Kruistabel)$expected


# <!-- ## /OPENBLOK: groepsgrootte2.R -->

# Geen van de verwachte aantallen observaties is kleiner dan vijf, dus er is voldaan aan de assumptie over de groepsgroottes. Voer *Mood's mediaan toets* uit met behulp van de *Chi-kwadraat toets*.

# ## Mood's mediaan toets

# <!-- ## TEKSTBLOK: Moods-mediaan-toets-1.R -->
# Gebruik de functie `mood.medtest()` van het package `RVAideMemoire` om *Mood's mediaan toets* uit te voeren. Het eerste argument `Studiepunten ~ Vooropleiding` bevat de afhankelijke variabele `Studiepunten` en de variabele `Vooropleiding` die beide ongepaarde groepen aangeeft, het tweede argument bevat de dataset `Studiepunten_studiejaar2` en het derde argument `exact= FALSE` geeft aan dat de *Chi-kwadraat toets voor onafhankelijkheid* uitgevoerd moet worden. Gebruik `exact = TRUE` om *Fisher's exact toets* uit te voeren.
# 
# <!-- ## /TEKSTBLOK: Moods-mediaan-toets-1.R -->
# 
# <!-- ## OPENBLOK: Moods-mediaan-toets-2.R -->

# In[ ]:


library(RVAideMemoire)
mood.medtest(Studiepunten ~ Vooropleiding, Studiepunten_studiejaar2, exact = FALSE)


# <!-- ## /OPENBLOK: Moods-mediaan-toets-2.R -->
# <!-- ## CLOSEDBLOK: Moods-mediaan-toets-3.R -->

# In[ ]:


library(RVAideMemoire)
mmt <- mood.medtest(Studiepunten ~ Vooropleiding, Studiepunten_studiejaar2, exact = FALSE)

library(DescTools)
hle <- HodgesLehmann(Studiepunten_studiejaar2$Studiepunten[Vooropleiding_Nederlands], Studiepunten_studiejaar2$Studiepunten[!Vooropleiding_Nederlands], conf.level = 0.95)

vChi2 <- Round_and_format(mmt$statistic)
vdf <- mmt$parameter
vW_est <- Round_and_format(hle[1])
vW_lb <- Round_and_format(hle[2])
vW_ub <- Round_and_format(hle[3])


# <!-- ## /CLOSEDBLOK: Moods-mediaan-toets-3.R -->
# 
# <!-- ## TEKSTBLOK: Moods-mediaan-toets-3.R -->
# Bereken vervolgens de mediaan van de verschilscores en bijbehorend 95%-betrouwbaarheidsinterval.[^7]<sup>,</sup>[^8] Gebruik hiervoor de functie `HodgesLehmann()` van het package `DescTools` met als argumenten het aantal studiepunten van studenten met Nederlandse vooropleiding `Studiepunten_studiejaar2$Studiepunten[Vooropleiding_Nederlands]`, het aantal studiepunten van studenten met een buitenlandse vooropleiding `Studiepunten_studiejaar2$Studiepunten[!Vooropleiding_Nederlands]` en `conf.level = 0.95` om het 95%-betrouwbaarheidsinterval te schatten.[^9]    
# <!-- ## /TEKSTBLOK: Moods-mediaan-toets-3.R -->
# 
# <!-- ## OPENBLOK: Moods-mediaan-toets-4.R -->

# In[ ]:


library(DescTools)
HodgesLehmann(Studiepunten_studiejaar2$Studiepunten[Vooropleiding_Nederlands], Studiepunten_studiejaar2$Studiepunten[!Vooropleiding_Nederlands], conf.level = 0.95)


# <!-- ## /OPENBLOK: Moods-mediaan-toets-4.R -->

# <!-- ## TEKSTBLOK: Moods-mediaan-toets-4.R -->
# * &chi;^2^ ~`r vdf`~ = `r vChi2`, *p* = < 0,0001
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^9]
# * De mediaan van de verschilscores is `r vW_est` met een 
# 95%-betrouwbaarheidsinterval  van `r vW_lb` tot `r vW_ub`. De mediaan van de verschillen tussen  studenten met een Nederlandse en buitenlandse vooropleiding is dus `r vW_est` studiepunten.
# 
# <!-- ## /TEKSTBLOK: Moods-mediaan-toets-4.R -->

# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# *Mood's mediaan toets* is uitgevoerd om te toetsen of de mediaan van het behaald aantal studiepunten in het tweede jaar van de bachelor Business Administration hetzelfde is voor studenten met buitenlandse vooropleiding als voor studenten met Nederlandse vooropleiding. De resultaten van de toets laten zien dat er een significant verschil is tussen beide medianen, &chi;^2^ ~`r vdf`~ = `r vChi2`, *p* = < 0,0001. Het geschatte mediaan van de verschilscores is `r vW_est` met bijbehorend 95%-betrouwbaarheidsinterval van `r vW_lb` tot `r vW_ub`. Studenten met een Nederlandse vooropleiding lijken dus meer studiepunten te behalen in het tweede jaar dan studenten met een buitenlandse vooropleiding.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->

# [^1]: Statistics How To (28 februari 2016). *Mood’s Median Test: Definition, Run the Test and Interpret Results*. [Statistics How to](https://www.statisticshowto.com/moods-median-test/).
# [^2]: Brown, G. W., & Mood, A. M. (1951). *On median tests for linear hypotheses*. In *Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability*. The Regents of the University of California.
# [^3]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.
# [^4]: Divine, G. W., Norton, H. J., Barón, A. E., & Juarez-Colunga, E. (2018). *The Wilcoxon–Mann–Whitney procedure fails as a test of medians*. The American Statistician, 72(3), 278-286.
# [^5]: SPSS Tutorials. *SPSS Median Test for 2 Independent Medians*. Bezocht op 22 april 2020. [Statistics How to](https://www.statisticshowto.com/moods-median-test/).
# [^6]: *Mood's mediaan toets* kan ook uitgevoerd worden om de medianen te vergelijken van twee of meer ordinale variabelen. Echter, de [Mann-Whitney U toets](08-Mann-Whitney-U-toetsiI-R.html) of de [Kruskal Wallis toets](10-Kruskal-Wallis-toets-I-R.html) zijn dan alternatieven met een hoger onderscheidend vermogen.
# [^7]: De mediaan van de verschilscores kan bij twee ongepaarde steekproeven bijvoorbeeld geschat worden door alle *m x n* verschilscores te berekenen tussen *m* observaties uit de ene steekproef en *n* observaties uit de andere steekproef. De mediaan van deze *m x n* verschilscores is dan de schatting.
# [^8]: Wikipedia (10 maart 2020). *Hogdes-Lehmann estimator. *[https://en.wikipedia.org/wiki/Hodges%E2%80%93Lehmann_estimator](https://en.wikipedia.org/wiki/Hodges%E2%80%93Lehmann_estimator) 
# [^9]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
