#!/usr/bin/env python
# coding: utf-8
---
title: "Kruskal Wallis toets"
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


source(paste0(here::here(),"/01. Includes/data/10.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# <!-- ## TEKSTBLOK: link1.R -->
# Gebruik de *Kruskal Wallis toets* om te toetsen of de gemiddelde rangnummers[^19] van de verdelingen van twee of meer groepen van elkaar verschillen.[^1]<sup>, </sup>[^17] De *Kruskal Wallis toets* kan een alternatief zijn voor de [one-way ANOVA](05-One-way-ANOVA-R.html).[^2] De *Kruskal Wallis toets* hoeft niet te voldoen aan de assumptie van normaliteit van de verdelingen van elke groep. Daarnaast hebben uitbijters bij de *Kruskal Wallis toets*  minder invloed op het eindresultaat dan bij de [one-way ANOVA](05-One-way-ANOVA-R.html). Daarentegen, als de data wel normaal verdeeld is, heeft de *Kruskal Wallis toets* minder onderscheidend vermogen[^4] dan de [one-way ANOVA](05-One-way-ANOVA-R.html).[^3] Vandaar dat ondanks de voordelen van de grotere robuustheid er toch minder vaak voor de *Kruskal Wallis toets* gekozen wordt. 
# <!-- ## /TEKSTBLOK: link1.R -->
# 
# # Onderwijscasus
# <div id="casus">
# De opleidingsdirecteur van de tweejarige Masteropleiding Arbeidsrecht is geïnteresseerd in de afstudeersnelheid van haar studenten. Zij vraagt zich af of er een verschil zit in het type vooropleiding dat de studenten hebben gehaald en de hoeveel studiepunten die de studenten behalen in het eerste jaar. Zij kijkt naar de vier meest gangbare vooropleidingen die de studenten doorlopen voordat ze met de Master Arbeidsrecht beginnen: de Bachelors Fiscaal Recht, Notarieel Recht en Rechtsgeleerdheid en de Premaster. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het gemiddelde rangnummer van de verdeling van het aantal behaalde studiepunten in het eerste jaar van de master Arbeidsrecht is gelijk voor de studenten met als vooropleidingen Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster.
# 
# *H~A~*: Het gemiddelde rangnummer van de verdeling van het aantal behaalde studiepunten in het eerste jaar van de master Arbeidsrecht is niet gelijk voor de studenten met als vooropleiding Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster.
# 
# </div>
# 
# # Assumpties
# <!-- ## TEKSTBLOK: link2.R -->
# Het meetniveau van de afhankelijke variabele is ordinaal[^16] of continu.[^6] In deze toetspagina staat een casus met continue data centraal; een casus met ordinale data met bijbehorende uitwerking is te vinden in de [Kruskal Wallis toets II](25-Kruskall-Wallis-toets-II-R.html). 
# <!-- ## /TEKSTBLOK: link2.R -->
# 
# # Post-hoc toets 
# <!-- ## TEKSTBLOK: link3.R -->
# De *Kruskal Wallis toets* toetst of twee of meerdere groepen van elkaar verschillen. Een post-hoc toets specificeert of groep significant van een andere groep verschilt. Gebruik de [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-R.html) als post-hoc toets. Hoewel het minder gebruikelijk is, is *Moods'mediaan toets* ook een optie als post-hoc toets. Deze toets toetst het verschil tussen de medianen van twee ongepaarde groepen. De [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-R.html) toetst het verschil tussen de verdelingen van twee ongepaarde groepen.
# <!-- ## /TEKSTBLOK: link3.R -->
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout.[^9] Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^5]
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^2] 
# 
# Bij de *Kruskal Wallis toets* wordt eta-squared (*η^2^*) als effectmaat gebruikt.[^10] De effectmaat eta squared (*η^2^*) berekent de proportie van de variantie in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele. In deze casus berekent het de proportie van de variantie in het aantal studiepunten wat verklaard kan worden door de vooropleiding. Een indicatie om *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^11]
# 

# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset `Resultaten_Arbeidsrecht` ingeladen met studieresultaten van het eerste jaar van de master Arbeidsrecht per vooropleiding: Fiscaal Recht, Notarieel Recht, Rechtsgeleerdheid en de Premaster.
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Resultaten_Arbeidsrecht)

## Laatste 6 observaties
tail(Resultaten_Arbeidsrecht)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken2.R-->
# De dataset bevat gegevens van studenten van verschillende opleidingen. Gebruik `unique()` om te onderzoeken welke opleidingen er in de data aanwezig zijn. 
# <!-- ## /TEKSTBLOK: Data-bekijken2.R-->
# 
# <!-- ## OPENBLOK: Data-bekijken-2.R -->

# In[ ]:


## Unieke opleidingen
unique(Resultaten_Arbeidsrecht$Vooropleiding)


# <!-- ## /OPENBLOK: Data-bekijken-2.R -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken3.R-->
# Inspecteer voor het aantal EC per vooropleiding de mediaan, de kwartielen en het aantal observaties. Gebruik de mediaan en kwartielen omdat de beoordelingen waarschijnlijk niet normaal verdeeld zijn. Gebruik hiervoor de functie `descr` en `stby` van het package `summarytools` om de beschrijvende statistieken per groep weer te geven. Voer de gewenste statistieken in met het argument `stats = c("q1","med","q3","n.valid")`.
# 
# <!-- ## /TEKSTBLOK: Data-bekijken3.R-->
# 
# <!-- ## OPENBLOK: Data-beschrijven.R -->
# ``` {r data beschrijven, warning=FALSE, message=FALSE}
# library(summarytools)
# 
# ## Mediaan, kwartielen en groepsgroottes
# with(Resultaten_Arbeidsrecht, 
#      stby(data = EC_Jaar1, 
#           list(Vooropleiding), 
#           descr, 
#           stats = c("q1", "med", "q3", "n.valid")))
# ```
# <!-- ## /OPENBLOK: Data-beschrijven.R -->
# <!-- ## CLOSEDBLOK: Data-beschrijven.R -->
# ``` {r data beschrijven als object, include=FALSE, echo=TRUE}
# x <- with(Resultaten_Arbeidsrecht,
#           stby(data = EC_Jaar1,
#                list(Vooropleiding),
#                descr,
#                stats = c("q1", "med", "q3", "n.valid")))
# 
# vN_FIS <- Round_and_format(x[[1]][4])
# vN_NOT <- Round_and_format(x[[2]][4])
# vN_RCH <- Round_and_format(x[[4]][4])
# vN_PM <- Round_and_format(x[[3]][4])
# 
# vQ1_FIS <- Round_and_format(x[[1]][1])
# vQ1_NOT <- Round_and_format(x[[2]][1])
# vQ1_RCH <- Round_and_format(x[[4]][1])
# vQ1_PM <- Round_and_format(x[[3]][1])
# 
# vMed_FIS <- Round_and_format(x[[1]][2])
# vMed_NOT <- Round_and_format(x[[2]][2])
# vMed_RCH <- Round_and_format(x[[4]][2])
# vMed_PM <- Round_and_format(x[[3]][2])
# 
# vQ3_FIS <- Round_and_format(x[[1]][3])
# vQ3_NOT <- Round_and_format(x[[2]][3])
# vQ3_RCH <- Round_and_format(x[[4]][3])
# vQ3_PM <- Round_and_format(x[[3]][3])
# ```
# <!-- ## /CLOSEDBLOK: Data-beschrijven.R -->
# <!-- ## TEKSTBLOK: Data-beschrijven.R-->
# * Mediaan Fiscaal Recht is `r vMed_FIS`, *n* = `r vN_FIS`.
# * Mediaan Notarieel Recht is `r vMed_NOT`, *n* = `r vN_NOT`.
# * Mediaan Premaster is `r vMed_PM`, *n* = `r vN_PM`.
# * Mediaan Rechtsgeleerdheid is `r vMed_RCH`, *n* = `r vN_RCH`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.R-->
# 
# ## De data visualiseren
# 
# Geef de verdeling van de verschillende vooropleidingen visueel weer met een histogram.[^18]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot
library(ggplot2)

ggplot(Resultaten_Arbeidsrecht,
  aes(x = EC_Jaar1)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 1,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Vooropleiding) +
  ylab("Frequentiedichtheid") +
  xlab("Aantal studiepunten jaar 1")
  labs(title = "Beoordelingen")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# Allereerst valt op dat de verdeling enigszins discreet is. Aangezien er in deze casus zes studiepunten per vak te verdienen zijn met een totaal van 60 in het eerste jaar, bestaan de histogrammen uit staven waartussen de verschillen zes studiepunten zijn. De verdeling van alle vier de vooropleidingen zijn niet normaal maar scheef verdeeld. Met uitzondering van de vooropleiding Rechtsgeleerdheid ligt de top op 60 studiepunten en is er een staart links daarvan.
# 
# ## Kruskal Wallis toets
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-1.R -->
# Voer de *Kruskal Wallis toets* uit om te onderzoeken of er verschillen zijn in het aantal studiepunten in het eerste jaar tussen de studenten van de master Arbeidsrecht met vier verschillende vooropleidingen   Gebruik de functie `kruskal.test()` met als eerste argument de afhankelijke variabele `EC_Jaar1` en de variabele die de groep definiëert: `Vooropleiding`. Het tweede argument is het dataframe `Resultaten_Arbeidsrecht`. 
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-1.R -->
# 
# <!-- ## OPENBLOK: Kruskal-Wallis-test-2.R -->

# In[ ]:


kruskal.test(EC_Jaar1 ~ Vooropleiding, Resultaten_Arbeidsrecht)


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-2.R -->
# 
# Bereken de effectmaat *&eta;^2^* vervolgens op basis van de *&chi;^2^*-waarde van de *Kruskal-Wallis toets*.
# <!-- ## OPENBLOK: Kruskal-Wallis-test-3.R -->

# In[ ]:


# Sla de teststatistiek op
KW_teststatistiek <- kruskal.test(EC_Jaar1 ~ Vooropleiding, Resultaten_Arbeidsrecht)$statistic

# Bereken eta squared
Eta_squared <- KW_teststatistiek / (nrow(Resultaten_Arbeidsrecht) - 1)

# Print de effectgrootte
paste("Eta squared is",Eta_squared)


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-3.R -->

# <!-- ## CLOSEDBLOK: Kruskal-Wallis-test-4.R -->

# In[ ]:


Ktest <- kruskal.test(EC_Jaar1 ~ Vooropleiding, Resultaten_Arbeidsrecht)
vK_DF <- Round_and_format(Ktest$parameter)
vK_Chi2 <- Round_and_format(Ktest$statistic)
vK_P <- Round_and_format(Ktest$p.value)


# <!-- ## /CLOSEDBLOK: Kruskal-Wallis-test-4.R -->
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-5.R -->
# * *df*: het aantal groepen - 1 = `r vK_DF`  
# * *H* = `r vK_Chi2`, *df* = `r vK_DF`, *p* < 0,0001, *&eta;^2^* = `r Round_and_format(Eta_squared)`  [^13]  
# * p-waarde < 0,05, dus de H~0~ wordt verworpen[^14]
# * Eta squared is `r Round_and_format(Eta_squared)` wat duidt op een gemiddeld tot groot effect 
# 
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-5.R -->

# ## Post-hoc toets: Mann-Whitney U toets
# <!-- ## TEKSTBLOK: Mann-Whitney-U-test.R -->
# Gebruik de [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-R.html) als post-hoc toets om te bepalen welke groepen significant verschillen. Gebruik de functie `pairwise.wilcox.test()` met als eerste argument de afhankelijke variabele `Resultaten_Arbeidsrecht$EC_Jaar1` en als tweede argument de definitie van de groepen `Resultaten_Arbeidsrecht$Vooropleiding`. Pas de *Bonferroni correctie* toe met `p.adjust.method = "bonferroni"`. Naast de p-waarde worden bij de [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-R.html) de gemiddelde rangnummers en de effectmaat *r* gerapporteerd. Voor meer informatie, zie de toetspagina van de [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-R.html).
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-test.R -->
# <!-- ## OPENBLOK: Mann-Whitney-U-test.R -->
# ``` {r pairwise wilcox test}
# pairwise.wilcox.test(Resultaten_Arbeidsrecht$EC_Jaar1, Resultaten_Arbeidsrecht$Vooropleiding, p.adjust.method = "bonferroni")
# ```
# <!-- ## /OPENBLOK: Mann-Whitney-U-test.R -->
# 
# <!-- ## CLOSEDBLOK: Mann-Whitney-U-test1.R -->
# ``` {r pairwise wilcox test closed}
# posthoc <-pairwise.wilcox.test(Resultaten_Arbeidsrecht$EC_Jaar1, Resultaten_Arbeidsrecht$Vooropleiding, p.adjust.method = "bonferroni")$p.value
# ```
# <!-- ## /CLOSEDBLOK: Mann-Whitney-U-test1.R -->
# 
# <!-- ## TEKSTBLOK: link4.R -->
# De [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-R.html) gebruikt het gemiddelde rangnummer van twee ongepaarde groepen om de significantie van de toets te bepalen. Met behulp van het gemiddelde rangnummer kan bepaald worden welke groep hogere rangnummers heeft wat een benadering is voor het verschil tussen twee verdelingen.[^15] In deze casus heeft de vooropleiding met een hoger rangnummer dus over het algemeen studenten met een hoger aantal studiepunten. Bereken en rapporteer daarom het gemiddelde rangnummer.
# <!-- ## /TEKSTBLOK: link4.R -->
# 
# <!-- ## OPENBLOK: Mann-Whitney-U-test2.R -->

# In[ ]:


# Maak een functie om het gemiddelde rangnummer te berekenen voor een vergelijking van twee groepen
Gemiddeld_rangnummer <- function(Vooropleiding_1, Vooropleiding_2){
  
  # Bind alle observaties in een variabele
  Aantal_studiepunten <- c(Vooropleiding_1, Vooropleiding_2)
  
  # Maak een variabele die aangeeft in welke groep de observatie zit
  Groepsindicator <- c(rep(1, length(Vooropleiding_1)), rep(2, length(Vooropleiding_2)))
  
  # Bereken de rangnummers van alle observaties
  Rangschikkingen <- rank(Aantal_studiepunten)
  
  # Bereken het gemiddelde rangnummer voor beide vooropleidingen
  Gemiddeld_rangnummer_Vooropleiding_1 <- mean(Rangschikkingen[Groepsindicator == 1])
  Gemiddeld_rangnummer_Vooropleiding_2 <- mean(Rangschikkingen[Groepsindicator == 2])
  
  # Retourneer beide gemiddelde rangnummers
  return(list(Groep_1 = Gemiddeld_rangnummer_Vooropleiding_1, Groep_2 = Gemiddeld_rangnummer_Vooropleiding_2))
}


# Definieer variabelen die observaties bevatten voor de verschillende vooropleidingen
Studiepunten_Fiscaal_Recht <- Resultaten_Arbeidsrecht$EC_Jaar1[Resultaten_Arbeidsrecht$Vooropleiding == "Fiscaal Recht"]

Studiepunten_Notarieel_Recht <- Resultaten_Arbeidsrecht$EC_Jaar1[Resultaten_Arbeidsrecht$Vooropleiding == "Notarieel Recht"]

Studiepunten_Premaster <- Resultaten_Arbeidsrecht$EC_Jaar1[Resultaten_Arbeidsrecht$Vooropleiding == "Premaster"]

Studiepunten_Rechtsgeleerdheid <- Resultaten_Arbeidsrecht$EC_Jaar1[Resultaten_Arbeidsrecht$Vooropleiding == "Rechtsgeleerdheid"]


# Bereken de gemiddelde rangnummers voor elke vergelijking
Gem_FR_NR <- Gemiddeld_rangnummer(Studiepunten_Fiscaal_Recht, 
                                  Studiepunten_Notarieel_Recht)

Gem_FR_PM <- Gemiddeld_rangnummer(Studiepunten_Fiscaal_Recht, 
                                  Studiepunten_Premaster)

Gem_FR_RG <- Gemiddeld_rangnummer(Studiepunten_Fiscaal_Recht, 
                                  Studiepunten_Rechtsgeleerdheid)

Gem_NR_PM <- Gemiddeld_rangnummer(Studiepunten_Notarieel_Recht, 
                                  Studiepunten_Premaster)

Gem_NR_RG <- Gemiddeld_rangnummer(Studiepunten_Notarieel_Recht,
                                  Studiepunten_Rechtsgeleerdheid)

Gem_PM_RG <- Gemiddeld_rangnummer(Studiepunten_Premaster, 
                                  Studiepunten_Rechtsgeleerdheid)


# <!-- ## /OPENBLOK: Mann-Whitney-U-test2.R -->
# 
# <!-- ## TEKSTBLOK: Mann-Whitney-U-test3.R -->
# | Vergelijking | p-waarde     | Gemiddeld rangnummer (links)  | Gemiddeld rangnummer (rechts)     |
# | -------------  | ----------  | ---------- | -------- |
# | FR vs. NR    | 1,00 `r #Round_and_format(posthoc[1,1])` |  `r Round_and_format(Gem_FR_NR[[1]])` | `r Round_and_format(Gem_FR_NR[[2]])` |
# | FR vs. PM    | 0,10 `r #Round_and_format(posthoc[2,1])` |  `r Round_and_format(Gem_FR_PM[[1]])` | `r Round_and_format(Gem_FR_PM[[2]])` |
# | FR vs. RG    | < 0,0001 `r #Round_and_format(posthoc[3,1])` |  `r Round_and_format(Gem_FR_RG[[1]])` | `r Round_and_format(Gem_FR_RG[[2]])` |
# | NR vs. PM    | 0,02 `r #Round_and_format(posthoc[2,2])` |  `r Round_and_format(Gem_NR_PM[[1]])` | `r Round_and_format(Gem_NR_PM[[2]])` |
# | NR vs. RG    | < 0,0001 `r #Round_and_format(posthoc[3,2])` |  `r Round_and_format(Gem_NR_RG[[1]])` | `r Round_and_format(Gem_NR_RG[[2]])` |
# | PM vs. RG    | 0,03`r #Round_and_format(posthoc[3,3])` |  `r Round_and_format(Gem_PM_RG[[1]])` | `r Round_and_format(Gem_PM_RG[[2]])` |
# *Tabel 1. Resultaten post-hoc toetsen voor vergelijking Fiscaal Recht (FR), Notarieel Recht (NR), Premaster (PM) en Rechtsgeleerdheid (RG).*
# 
# Als voorbeeld wordt de bovenste rij van Tabel 1 in woorden uitgelegd. Er is geen significant verschil gevonden tussen Fiscaal Recht (Gemiddeld rangnummer = `r Round_and_format(Gem_FR_NR[[1]])`,  *n*=`r vN_FIS`) en Notarieel Recht (Gemiddeld rangnummer = `r Round_and_format(Gem_FR_NR[[2]])`,  *n*=`r vN_NOT`), *p*=1,00.
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-test3.R -->

# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *Kruskal Wallis toets* is uitgevoerd om te toetsen of er verschillen zijn tussen de studenten van de Master Arbeidsrecht met als vooropleiding Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster wat betreft de verdeling van het aantal studiepunten dat de studenten in het eerste jaar behalen. Uit de resultaten kan afgelezen worden dat er een significant verschil is tussen de verdelingen van het aantal studiepunten voor de verschillende vooropleidingen, *H* = `r vK_Chi2`, *df* = `r vK_DF` ,*p* < 0,0001, *&eta;^2^* = `r Round_and_format(Eta_squared)`. De resultaten ondersteunen de conclusie dat er een verschil is tussen studenten van de vier verschillende vooropleidingen wat betreft de verdeling van de hoeveelheid studiepunten die studenten behalen tijdens het eerste jaar van de master Arbeidsrecht.  
# 
# De [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-R.html) is uitgevoerd als post-hoc toets om te onderzoeken welke vooropleidingen van elkaar verschillen qua aantal studiepunten dat studenten behalen.  De *Bonferroni correctie* is gebruikt om de Type I fout te voorkomen die gepaard gaat met het veelvuldig toetsen. De studenten met Rechtsgeleerdheid als vooropleiding behalen significant minder punten bij de Master Arbeidsrecht, dan de studenten met een andere vooropleiding. Er is ook een significant verschil gevonden tussen de behaalde studiepunten van studenten met de vooropleiding Notarieel Recht en de Premaster, waarbij de studenten van de Premaster minder punten behaalden dan de studenten van Notarieel Recht. Er zijn geen significante verschillen gevonden tussen de vooropleidingen Fiscaal Recht en Notarieel Recht, en Fiscaal Recht en Premaster. De gemiddelde rangnummers en p-waarden van de post-hoc toetsen zijn te vinden in Tabel 1. 
# 
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: De toets rangschikt de datapunten van laag naar hoog en geeft elke datapunt een rangnummer. Vervolgens wordt per groep het gemiddelde berekend van de rangnummers. Deze gemiddelden wordt met elkaar vergeleken. Voor meer informatie lees: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^2]: Van Geloven, N. (21 maart 2018). *Kruskal Wallis*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Kruskal_Wallis). 
# [^3]: Universiteit van Amsterdam (7 juli 2014). *Kruskal-Wallis Test*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Kruskal-Wallis_Test). 
# [^4]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.
# [^5]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^6]: Van Geloven, N. (21 November 2017). *KEUZE TOETS*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/KEUZE_TOETS).
# [^9]: Universiteit van Amsterdam (7 juli 2014). *Kruskal-Wallis Test*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Kruskal-Wallis_Test).
# [^10]: De effectmaat *&eta;^2^* wordt voor de *Kruskal-Wallis toets* berekend door de *&chi;^2^*-waarde te delen door het totaal aantal observaties minus één, i.e. $\frac{\chi^2}{N-1} $.
# [^11]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^13]: De test-statistiek *H* volgt bij benadering de chi-kwadraat verdeling. Onder deze hypothese is *H* chi-kwadraat, vandaar dat dit in de output uitgedrukt wordt in chi-kwadraat.
# [^14]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met Type I en Type II fouten. 
# [^15]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^16]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^17]:  Laerd statistics (2018). *Kruskal-Wallis H Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/kruskal-wallis-h-test-using-spss-statistics.php.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^19]: Bij de *Kruskal Wallis toets* en andere nonparametrische toetsen wordt de data eerst gerangschikt zodat elke observatie een rangnummer toegewezen krijgt. Deze rangnummers worden vervolgens gebruikt om de toets uit te voeren.
# 
