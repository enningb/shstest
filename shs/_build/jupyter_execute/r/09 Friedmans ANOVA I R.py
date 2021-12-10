#!/usr/bin/env python
# coding: utf-8
---
title: "Friedman's ANOVA"
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


source(paste0(here::here(),"/01. Includes/data/09.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# <!-- ## TEKSTBLOK: Link1.R -->
# Gebruik *Friedman's ANOVA* om de gemiddelde rangnummers[^13] te vergelijken voor de verdelingen van drie of meer herhaalde metingen van één groep of voor de verdelingen van drie of meer gepaarde groepen.[^1]<sup>, </sup>[^2] *Friedman's ANOVA* is een alternatief voor de [repeated measures ANOVA](04-Repeated-measures-ANOVA-R.html) wanneer de data niet aan de assumptie van normaliteit voldoet. Daarnaast hebben uitbijters minder invloed op het resultaat van *Friedman's ANOVA* in vergelijking tot de [repeated measures ANOVA](04-Repeated-measures-ANOVA-R.html). Echter, als de data aan de assumpties van de [repeated measures ANOVA](04-Repeated-measures-ANOVA-R.html) voldoet, heeft die toets een hoger onderscheidend vermogen dan *Friedman's ANOVA*.[^3]
# 
# <!-- ## /TEKSTBLOK: Link1.R -->

# # Onderwijscasus
# <div id = "casus">
# 
# Uit de Nationale Studenten Enquête (NSE) blijkt dat studenten ontevreden zijn over het horeca-aanbod op de campus van hun hogeschool. De vastgoedmanager van de  Facultaire Dienst (FD) van deze hogeschool is nieuwsgierig hoe de verschillende eetgelegenheden op de campus gewaardeerd worden door studenten om zo te inventarisen op welke manier het horeca-aanbod verbeterd kan worden. Als vervolgonderzoek op de NSE wordt een groep studenten gevraagd om de eetgelegenheden op de campus te beoordelen (met een cijfer tussen 1 en 10). Aan de hand daarvan vergelijkt de vastgoedmanager eetgelegenheden in vier gebouwen: het hoofdgebouw, het bestuursgebouw, het sportcentrum en het cultuurcentrum Rembrandt. Met deze gegevens wil de vastgoedmanager onderzoeken of er verschillen zijn in de waarderingscijfers van de eetgelegenheden in de vier gebouwen. Als deze verschillen aanwezig zijn, is zij benieuwd welke eetgelegenheden van elkaar verschillen.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het gemiddelde rangnummer van de verdelingen van de beoordelingen van studenten is hetzelfde voor de eetgelegenheid in het hoofdgebouw, het bestuursgebouw, het sportcentrum en het cultuurcentrum Rembrandt.
# 
# *H~A~*: Het gemiddelde rangnummer van de verdelingen van de beoordelingen van studenten is niet hetzelfde voor de eetgelegenheid in het hoofdgebouw, het bestuursgebouw, het sportcentrum en het cultuurcentrum Rembrandt.
# 
# </div>
# 
# # Assumpties
# 
# Om een valide toetsresultaat te bereiken, moeten de data aan een aantal assumpties voldoen. Het meetniveau van de afhankelijke variabele is ordinaal[^14] of continu.[^4] In deze toetspagina staat een casus met continue data centraal; een casus met ordinale data met bijbehorende uitwerking is te vinden in [deze toetspagina](24-Friedmans-ANOVA-II-R.html). Bij herhaalde metingen van dezelfde observatie-eenheden, moet de groep observatie-eenheden drie of meer keren gemeten zijn en een willekeurige steekproef van de populatie zijn. Bij gepaarde groepen, moet elk paar bestaan uit drie of meer gepaarde observatie-eenheden en moet de steekproef met alle paren een willekeurige steekproef van de populatie zijn.[^4]

# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^5] Voor *Friedman's ANOVA* wordt de effectmaat *Kendall's W* vaak gebruikt.[^6]<sup>, </sup>[^7]<sup>, </sup>[^8] Een indicatie om *Kendall's W* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^6]

# # Post-hoc toetsen
# 
# <!-- ## TEKSTBLOK: Link2.R -->
# *Friedman's ANOVA* toetst of er verschillen zijn tussen de verdelingen van groepen. Voer een post-hoc toets uit om te bepalen welke groepen van elkaar verschillen. Gebruik de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) als post-hoc toets. De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) toetst of er een verschil tussen de verdelingen is van twee gepaarde groepen (i.e. of een van beide verdelingen hogere waardes heeft dan de andere verdeling). Hoewel het minder gebruikelijk is, is de [tekentoets](27-Tekentoets-II-R.html) ook een optie als post-hoc toets. Deze toets toetst het verschil tussen de medianen van twee gepaarde groepen.
# <!-- ## /TEKSTBLOK: Link2.R -->
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout. Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^5]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset `Beoordelingen_eetgelegenheden` ingeladen met de beoordelingen van de eetgelegenheden in het hoofdgebouw, bestuursgebouw, sportcentrum en cultuurcentrum.
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Beoordelingen_eetgelegenheden)

## Laatste 6 observaties
tail(Beoordelingen_eetgelegenheden)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken2.R-->
# De dataset bevat beoordelingen van studenten van eetgelegenheden in verschillende gebouwen. Gebruik `unique()` om te onderzoeken welke gebouwen er in de data aanwezig zijn. 
# <!-- ## /TEKSTBLOK: Data-bekijken2.R-->
# 
# <!-- ## OPENBLOK: Data-bekijken-2.R -->

# In[ ]:


## Unieke opleidingen
unique(Beoordelingen_eetgelegenheden$Eetgelegenheid)


# <!-- ## /OPENBLOK: Data-bekijken-2.R -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken3.R-->
# Inspecteer voor de beoordelingen per gebouw de mediaan, de kwartielen en het aantal observaties. Gebruik de mediaan en kwartielen omdat de beoordelingen waarschijnlijk niet normaal verdeeld zijn. Gebruik hiervoor de functie `descr` en `stby` van het package `summarytools` om de beschrijvende statistieken per groep weer te geven. Voer de gewenste statistieken in met het argument `stats = c("q1","med","q3","n.valid")`.
# 
# <!-- ## /TEKSTBLOK: Data-bekijken3.R-->
# 
# <!-- ## OPENBLOK: Data-beschrijven.R -->
# ``` {r data beschrijven, warning=FALSE, message=FALSE}
# library(summarytools)
# 
# ## Mediaan, kwartielen en groepsgroottes
# with(Beoordelingen_eetgelegenheden, 
#      stby(data = Beoordeling, 
#           list(Eetgelegenheid), 
#           descr, 
#           stats = c("q1", "med", "q3", "n.valid")))
# 
# ```
# <!-- ## /OPENBLOK: Data-beschrijven.R -->
# <!-- ## CLOSEDBLOK: Data-beschrijven.R -->
# ``` {r data beschrijven als object, include=FALSE, echo=TRUE}
# 
# x <- with(Beoordelingen_eetgelegenheden, 
#      stby(data = Beoordeling, 
#           list(Eetgelegenheid), 
#           descr, 
#           stats = c("q1", "med", "q3", "n.valid")))
# 
# vN_HG <- Round_and_format(x[[3]][4])
# vN_BG <- Round_and_format(x[[1]][4])
# vN_SC <- Round_and_format(x[[4]][4])
# vN_CC <- Round_and_format(x[[2]][4])
# 
# vQ1_HG <- Round_and_format(x[[3]][1])
# vQ1_BG <- Round_and_format(x[[1]][1])
# vQ1_SC <- Round_and_format(x[[4]][1])
# vQ1_CC <- Round_and_format(x[[2]][1])
# 
# vMed_HG <- Round_and_format(x[[3]][2])
# vMed_BG <- Round_and_format(x[[1]][2])
# vMed_SC <- Round_and_format(x[[4]][2])
# vMed_CC <- Round_and_format(x[[2]][2])
# 
# vQ3_HG <- Round_and_format(x[[3]][3])
# vQ3_BG <- Round_and_format(x[[1]][3])
# vQ3_SC <- Round_and_format(x[[4]][3])
# vQ3_CC <- Round_and_format(x[[2]][3])
# 
# ```
# <!-- ## /CLOSEDBLOK: Data-beschrijven.R -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.R-->
# * Hoofdgebouw: *Mdn* =  `r vMed_HG`, *Q1* = `r vQ1_HG`, *Q3* = `r vQ3_HG`, *n* = `r vN_HG`.
# * Bestuursgebouw: *Mdn* =  `r vMed_BG`, *Q1* = `r vQ1_BG`, *Q3* = `r vQ3_BG`, *n* = `r vN_BG`.
# * Sportcentrum: *Mdn* =  `r vMed_SC`, *Q1* = `r vQ1_SC`, *Q3* = `r vQ3_SC`, *n* = `r vN_SC`.
# * Cultuurcentrum: *Mdn* =  `r vMed_CC`, *Q1* = `r vQ1_CC`, *Q3* = `r vQ3_CC`, *n* = `r vN_CC`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.R-->
# 

# ## Histogram
# 
# Geef de verdeling van de beoordelingen per gebouw visueel weer met een histogram[^18].[^12]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot
library(ggplot2)

ggplot(Beoordelingen_eetgelegenheden,
  aes(x = Beoordeling)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 1,
                 color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Eetgelegenheid) +
  ylab("Frequentiedichtheid") +
  labs(title = "Beoordelingen")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# Bij alle vier de gebouwen lijken er afwijkingen te zijn van de (symmetrische) normale verdeling. De verdeling van het bestuursgebouw heeft een langere staart aan de rechterkant, terwijl de verdelingen van het hoofdgebouw en het sportcentrum juist een langere staart aan de linkerkant hebben. Bij het cultuurcentrum zijn er meer observaties links van het midden dan rechts van het midden, waardoor er ook een vorm van asymmetrie is. Daarom is het een goede optie om *Friedman's ANOVA* uit te voeren, omdat deze toets niet aan de assumptie van normaliteit hoeft te voldoen.
# 

# ## Friedman's ANOVA
# 
# <!-- ## TEKSTBLOK: ANOVA-toets.R -->
# Voer *Friedman's ANOVA* uit om de vraag te beantwoorden of er verschillen zijn tussen de (gemiddelde rangnummers van de) beoordelingen van de eetgelegenheden in de vier gebouwen op de campus van de hogeschool. Gebruik de functie `friedman.test()` met als argumenten de afhankelijke variabele `y = Beoordelingen_eetgelegenheden$Beoordeling`, de vier groepen die vergeleken worden (onafhankelijke variabele) `groups = Beoordelingen_eetgelegenheden$Kantine` en de variabele die de observatie-eenheden aangeeft `blocks = Beoordelingen_eetgelegenheden$Studentnummer`.
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets.R -->

# In[ ]:


friedman.test(y = Beoordelingen_eetgelegenheden$Beoordeling, 
              groups = Beoordelingen_eetgelegenheden$Eetgelegenheid,
              blocks = Beoordelingen_eetgelegenheden$Studentnummer)


# <!-- ## /OPENBLOK: ANOVA-toets.R -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets.R -->

# In[ ]:


obj <- friedman.test(y = Beoordelingen_eetgelegenheden$Beoordeling, 
              groups = Beoordelingen_eetgelegenheden$Eetgelegenheid,
              blocks = Beoordelingen_eetgelegenheden$Studentnummer)
vChi2 <- Round_and_format(obj$statistic)
vdf <- Round_and_format(obj$parameter)


# <!-- ## /CLOSEDBLOK: ANOVA-toets.R -->
# 
# Bereken vervolgens de effectmaat *Kendall's W* op basis van de *&chi;^2^* waarde van *Friedman's ANOVA*.
# <!-- ## OPENBLOK: ANOVA-toets2.R -->

# In[ ]:


# Sla de Chi-kwadraat waarde op
Chi2 <- friedman.test(y = Beoordelingen_eetgelegenheden$Beoordeling, 
              groups = Beoordelingen_eetgelegenheden$Eetgelegenheid,
              blocks = Beoordelingen_eetgelegenheden$Studentnummer)$statistic

# Sla het aantal observatie-eenheden op
N <- length(unique(Beoordelingen_eetgelegenheden$Studentnummer))  

# Sla het aantal groepen op
k <- length(unique(Beoordelingen_eetgelegenheden$Eetgelegenheid))

# Bereken de effectmaat
W <- Chi2 / (N * (k - 1))

# Print de effectmaat
paste("De effectmaat is", W)


# <!-- ## /OPENBLOK: ANOVA-toets2.R -->

# <!-- ## TEKSTBLOK: ANOVA-toets1.R -->
# * *&chi;^2^~3~* = `r vChi2`, *p* < 0,001, *W* = `r Round_and_format(W)`
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^10]
# * Er is een significant verschil tussen de beoordelingen van de eetgelegenheden in de vier gebouwen; het effect van de verschillende gebouwen op de beoordelingen van studenten is klein tot gemiddeld
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets1.R -->
# 
# ## Post-hoc toets
# <!-- ## TEKSTBLOK: posthoc1.R -->
# Voer post-hoc toetsen uit om te onderzoeken tussen welke gebouwen er verschillen zijn in de beoordelingen van studenten. De vier gebouwen zijn het hoofdgebouw, bestuursgebouw, sportcentrum en cultuurcentrum Rembrandt. Gebruik de [Wilcoxon signed-rank toets](07-Wilcoxon-signed-rank-toets-R.html) als post-hoc toets met bijbehorende functie `pairwise.wilcox.test()`. De ingevoerde argumenten van de functie zijn de afhankelijke variabele `Beoordelingen_eetgelegenheden$Beoordeling`, de onafhankelijke variabele `Beoordelingen_eetgelegenheden$Eetgelegenheid` die de groepen aangeeft, de gebruikte methode om te corrigeren voor meerdere toetsen `p.adjust.method = "bonferroni"`, het argument `paired = TRUE` om aan te geven dat er een gepaarde steekproef is en het argument `exact = FALSE` om de p-waarden niet op een exacte manier te berekenen. Gebruik het laatste argument omdat de exacte methode in bepaalde gevallen niet mogelijk is. Het significantieniveau is 0,05.[^10]
# <!-- ## /TEKSTBLOK: posthoc1.R -->
# 
# <!-- ## OPENBLOK: post-hoc2.R -->
# ``` {r pairwise wilcox test}
# pairwise.wilcox.test(Beoordelingen_eetgelegenheden$Beoordeling, Beoordelingen_eetgelegenheden$Eetgelegenheid, p.adjust.method = "bonferroni", paired = TRUE, exact = FALSE)
# ```
# <!-- ## /OPENBLOK: post-hoc2.R -->
# 
# Bereken de effectmaat *r* voor elke individuele post-hoc toets.[^11]
# 
# <!-- ## OPENBLOK: post-hoc4.R -->
# ``` {r pairwise wilcox test effectmaat}
# # Sla de p-waarden van de post-hoc toetsen op
# posthoc <- pairwise.wilcox.test(Beoordelingen_eetgelegenheden$Beoordeling, Beoordelingen_eetgelegenheden$Eetgelegenheid, p.adjust.method = "bonferroni", paired = TRUE, exact = FALSE)$p.value
# 
# # Effectmaat hoofdgebouw vs. bestuursgebouw
# (Effectmaat_HG_BG <- abs(qnorm(posthoc[2,1]/2)) / sqrt(length(unique(Beoordelingen_eetgelegenheden$Studentnummer))))
# 
# # Effectmaat hoofdgebouw vs. sportcentrum
# Effectmaat_HG_SC <- abs(qnorm(posthoc[3,3]/2)) / sqrt(length(unique(Beoordelingen_eetgelegenheden$Studentnummer)))
# 
# # Effectmaat hoofdgebouw vs. cultuurcentrum
# Effectmaat_HG_CC <- abs(qnorm(posthoc[2,2]/2)) / sqrt(length(unique(Beoordelingen_eetgelegenheden$Studentnummer)))
# 
# # Effectmaat bestuursgebouw vs. sportcentrum
# Effectmaat_BG_SC <- abs(qnorm(posthoc[3,1]/2)) / sqrt(length(unique(Beoordelingen_eetgelegenheden$Studentnummer)))
# 
# # Effectmaat bestuursgebouw vs. cultuurcentrum
# Effectmaat_BG_CC <- abs(qnorm(posthoc[1,1]/2)) / sqrt(length(unique(Beoordelingen_eetgelegenheden$Studentnummer)))
# 
# # Effectmaat sportcentrum vs. cultuurcentrum
# Effectmaat_SC_CC <- abs(qnorm(posthoc[3,2]/2)) / sqrt(length(unique(Beoordelingen_eetgelegenheden$Studentnummer)))
# 
# 
# ```
# <!-- ## /OPENBLOK: post-hoc4.R -->
# 
# <!-- ## TEKSTBLOK: Link4.R -->
# De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) gebruikt de som van positieve en negatieve rangnummers van de verschilscores om de significantie van de toets te bepalen. Deze sommen beschrijven het verschil tussen twee gepaarde groepen waarbij de groep met een hogere som van rangnummers ook hogere waarden op de afhankelijke variabele heeft. In deze casus heeft het gebouw met hogere rangnummers een hogere beoordeling door studenten. Bereken de som van de positieve en negatieve rangnummers voor alle vergelijkingen.
# <!-- ## /TEKSTBLOK: Link4.R -->
# 
# <!-- ## OPENBLOK: post-hoc5.R -->

# In[ ]:



# Definieer een functie die som positieve en negatieve rangnummers berekent
Sommen_rangnummers <- function(Beoordeling_gebouw_1, Beoordeling_gebouw_2){
  
  # Bereken verschilscores
  Verschilscores <- Beoordeling_gebouw_1 - Beoordeling_gebouw_2
  
  # Rangschik de absolute waarden van verschilscores
  Rangnummers <- rank(abs(Verschilscores))

  # Maak een vector met daarin de tekens (plus of min) van verschilscores
  Tekens <- sign(Verschilscores)

  # Bereken de som van de positieve rangnummers
  Som_positief <- sum(Rangnummers[Tekens == 1])

  # Bereken de som van de negatieve rangnummers
  Som_negatief <- sum(Rangnummers[Tekens == -1])
  
  # Retourneer som van positieve en negatieve rangnummers
  return(list(Positief = Som_positief, Negatief = Som_negatief))
}

# Definieer variabelen die beoordelingen bevatten per gebouw
Beoordeling_hoofdgebouw <- Beoordelingen_eetgelegenheden$Beoordeling[Beoordelingen_eetgelegenheden$Eetgelegenheid == "Hoofdgebouw"]

Beoordeling_bestuursgebouw <- Beoordelingen_eetgelegenheden$Beoordeling[Beoordelingen_eetgelegenheden$Eetgelegenheid == "Bestuursgebouw"]

Beoordeling_sportcentrum <- Beoordelingen_eetgelegenheden$Beoordeling[Beoordelingen_eetgelegenheden$Eetgelegenheid == "Sportcentrum"]

Beoordeling_cultuurcentrum <- Beoordelingen_eetgelegenheden$Beoordeling[Beoordelingen_eetgelegenheden$Eetgelegenheid == "Cultuurcentrum"]

# Bereken positieve en negatieve som van rangnummers

## Som rangnummers hoofdgebouw vs. bestuursgebouw
(Som_HG_BG <- Sommen_rangnummers(Beoordeling_hoofdgebouw, Beoordeling_bestuursgebouw))

## Som rangnummers hoofdgebouw vs. sportcentrum
Som_HG_SC <- Sommen_rangnummers(Beoordeling_hoofdgebouw, Beoordeling_sportcentrum)

## Som rangnummers hoofdgebouw vs. cultuurcentrum
Som_HG_CC <- Sommen_rangnummers(Beoordeling_hoofdgebouw, Beoordeling_cultuurcentrum)

## Som rangnummers bestuursgebouw vs. sportcentrum
Som_BG_SC <- Sommen_rangnummers(Beoordeling_bestuursgebouw, Beoordeling_sportcentrum)

## Som rangnummers bestuursgebouw vs. cultuurcentrum
Som_BG_CC <- Sommen_rangnummers(Beoordeling_bestuursgebouw, Beoordeling_cultuurcentrum)

## Som rangnummers sportcentrum vs. cultuurcentrum
Som_SC_CC <- Sommen_rangnummers(Beoordeling_sportcentrum, Beoordeling_cultuurcentrum)


# <!-- ## /OPENBLOK: post-hoc5.R -->
# 
# <!-- ## TEKSTBLOK: posthoc6.R -->
# 
# | Vergelijking | p-waarde     | Effectmaat        |  Som positieve rangnummers        | Som negatieve rangnummers     |
# | -------------  | ----------  | --------- | ---------- | -------- |
# | HG vs. BG    | 0,878`r #Round_and_format(posthoc[2,1])` | `r Round_and_format(Effectmaat_HG_BG)`| `r Round_and_format(Som_HG_BG[[1]])` | `r Round_and_format(Som_HG_BG[[2]])` |
# | HG vs. SC    | 1,000`r #Round_and_format(posthoc[3,3])` | `r Round_and_format(Effectmaat_HG_SC)`| `r Round_and_format(Som_HG_SC[[1]])` | `r Round_and_format(Som_HG_SC[[2]])` |
# | HG vs. CC    | 0,046`r #Round_and_format(posthoc[2,2])` | `r Round_and_format(Effectmaat_HG_CC)`| `r Round_and_format(Som_HG_CC[[1]])` | `r Round_and_format(Som_HG_CC[[2]])` |
# | BG vs. SC    | 0,108`r #Round_and_format(posthoc[3,1])` | `r Round_and_format(Effectmaat_BG_SC)`| `r Round_and_format(Som_BG_SC[[1]])` | `r Round_and_format(Som_BG_SC[[2]])` |
# | BG vs. CC    | 1,000`r #Round_and_format(posthoc[1,1])` | `r Round_and_format(Effectmaat_BG_CC)`| `r Round_and_format(Som_BG_CC[[1]])` | `r Round_and_format(Som_BG_CC[[2]])` |
# | SC vs. CC    | 0,013`r #Round_and_format(posthoc[3,2])` | `r Round_and_format(Effectmaat_SC_CC)`| `r Round_and_format(Som_SC_CC[[1]])` | `r Round_and_format(Som_SC_CC[[2]])` |

# *Tabel 1. Resultaten post-hoc toetsen voor vergelijking hoofdgebouw (HG), bestuursgebouw (BG), sportcentrum (SC) en cultuurcentrum (CC).*
# <!-- ## /TEKSTBLOK: posthoc6.R -->

# <!-- ## TEKSTBLOK: posthoc7.R -->
# De significante verschillen op de post-hoc toetsen zijn:
# 
# * De beoordelingen van het hoofdgebouw (Som = `r Round_and_format(Som_HG_CC[[1]])`) verschillen significant van het cultuurcentrum (Som = `r Round_and_format(Som_HG_CC[[2]])`), *p* = 0,046`r #Round_and_format(posthoc[2,2])`, *r* = `r Round_and_format(Effectmaat_HG_CC)`. De hogere som van rangnummers voor het hoofdgebouw duidt erop dat de beoordelingen van het hoofdgebouw beter zijn dan die van het cultuurcentrum.
# 
# * De beoordelingen van het sportcentrum (Som = `r Round_and_format(Som_SC_CC[[1]])`) verschillen significant van het cultuurcentrum (Som = `r Round_and_format(Som_SC_CC[[2]])`), *p* = 0,013 `r #Round_and_format(posthoc[3,2])`, *r* = `r Round_and_format(Effectmaat_SC_CC)`. De hogere som van rangnummers voor het sportcentrum duidt erop dat de beoordelingen van het sportcentrum beter zijn dan die van het cultuurcentrum.
# 
# <!-- ## /TEKSTBLOK: posthoc7.R -->
# 

# # Rapportage
# 
# <!-- ## TEKSTBLOK: rapportage.R -->
# *Friedman's ANOVA* is uitgevoerd om te onderzoeken of de beoordeling van eetgelegenheden door studenten verschilt voor vier gebouwen op de campus van een hogeschool. De vier gebouwen zijn het hoofdgebouw, het bestuursgebouw, het sportcentrum en cultuurcentrum Rembrandt; beschrijvende statistieken zijn te vinden in Tabel 1. De beoordelingen van de vier gebouwen verschillen significant van elkaar (*&chi;^2^~3~* = `r vChi2`, *p* < 0,001, *W* = `r Round_and_format(W)`). De sterkte van het effect van de verschillen in gebouwen op de beoordelingen van studenten is klein tot gemiddeld.
# 
# Post-hoc toetsen met een Bonferroni correctie voor meerdere toetsen zijn uitgevoerd voor alle vergelijkingen tussen twee gebouwen. Hieruit blijkt dat er alleen significante verschillen zijn tussen het hoofdgebouw en cultuurcentrum Rembrandt (*p* = 0,046), en tussen het sportcentrum  en cultuurcentrum Rembrandt (*p* = 0,013). De eetgelegenheid van het hoofdgebouw (Som = `r Round_and_format(Som_HG_CC[[1]])`) wordt beter beoordeld dan de eetgelegenheid in het cultuurcentrum Rembrandt (Som = `r Round_and_format(Som_HG_CC[[2]])`). En de eetgelegenheid van het sportcentrum (Som = `r Round_and_format(Som_SC_CC[[1]])`) wordt ook beter beoordeld dan de eetgelegenheid in het cultuurcentrum Rembrandt (Som = `r Round_and_format(Som_SC_CC[[2]])`). Verder zijn er geen significante verschillen tussen de beoordelingen van de eetgelegenheden op de campus.
# <!-- ## /TEKSTBLOK: rapportage.R -->
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Van Geloven, N. (4 oktober 2019). *Friedman toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Friedman_toets). 
# [^2]: Universiteit van Amsterdam (7 juli 2014). *Friedmans ANOVA*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Friedmans_ANOVA). 
# [^3]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^4]: Laerd statistics (2018). *Friedman Test in SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/friedman-test-using-spss-statistics.php. 
# [^5]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^6]: University of Sheffield. *Friedman test in SPSS*. [Mathematics and Statistics Help (MASH)](https://www.sheffield.ac.uk/polopoly_fs/1.714575!/file/stcp-marshall-FriedmanS.pdf). Bezocht op 13 maart 2020.
# [^7]: *Kendall's W* wordt berekend door de teststatistiek van *Friedman's ANOVA* (dit is de *&chi;^2^*) te delen door het aantal observatie-eenheden *N* en het aantal groepen *k* minus één, i.e. $W = \frac{\chi^2}{N(k-1)}$.
# [^8]: Kassambara, A. (2020). *rstatix: Pipe-Friendly Framework for Basic Statistical Tests*. [R package version 0.4.0.](https://CRAN.R-project.org/package=rstatix).
# [^10]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^11]: De effectmaat *r* wordt voor de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) berekend door de
# *z*-waarde behorend bij de *p*-waarde van de toets te delen door de wortel van
# het aantal observatie-eenheden, i.e. $\frac{z}{\sqrt{N}}$.
# [^12]: De breedte van de staven van het histogram worden hier automatisch bepaald, maar kunnen handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^13]: Bij *Friedman's ANOVA* en andere nonparametrische toetsen wordt de data eerst gerangschikt zodat elke observatie een rangnummer toegewezen krijgt. Deze rangnummers worden vervolgens gebruikt om de toets uit te voeren.
# [^14]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
