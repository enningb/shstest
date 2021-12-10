#!/usr/bin/env python
# coding: utf-8
---
title: "Bhapkar toets"
output:
  html_document:
    theme: lumen
    toc: yes
    toc_depth: 2
    toc_float: 
      collapsed: FALSE 
    number_sections: true
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


source(paste0(here::here(),"/01. Includes/data/18.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# <!-- ## TEKSTBLOK: Link1.R -->
# Gebruik de *Bhapkar toets* om te toetsen of er verschillen zijn voor een nominale[^1] variabele tussen twee gepaarde groepen.[^2]<sup>, </sup>[^3] Als de nominale variabele twee categorieën heeft, kan ook de [McNemar toets](12-McNemar-toets-I-R.html) gebruikt worden.
# <!-- ## /TEKSTBLOK: Link1.R -->
# 
# # Onderwijscasus
# <div id = "casus">
# 
# De studieadviseur van de bachelor Leisure & Events Management geeft halverwege het eerste studiejaar een voorlopig BSA-advies aan alle eerstejaars studenten. Studenten ontvangen een positief, negatief of uitgesteld BSA.  Daarnaast voert zij met alle studenten persoonlijke gesprekken om het advies toe te lichten en een plan voor de rest van het studiejaar te maken. De studieadviseur wil graag onderzoeken of er verschillen zijn tussen het voorlopige BSA-advies halverwege het jaar en het definitieve advies aan het einde van het jaar zodat ze de effectiviteit van de persoonlijke gesprekken kan beoordelen.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil tussen de verdeling van de voorlopige BSA adviezen en de definitieve BSA adviezen.
# 
# *H~A~*: Er is een verschil tussen de verdeling van de voorlopige BSA adviezen en de definitieve BSA adviezen.
# 
# </div>
# 
# # Assumpties
# 
# Om de *Bhapkar toets* uit te voeren, moeten de data aan een aantal voorwaarden voldoen. Er dient een categorische variabele te zijn met twee of meer categorieën en een binaire variabele die de twee gepaarde groepen weergeeft. Daarnaast mag er geen overlap zijn tussen de categorieën van de categorische variabele: elke observatie past slechts in een van beide categorieën.[^2]<sup>, </sup>[^3]
# 
# # Frequentiematrix
# 
# De *Bhapkar toets* gaat uit van een frequentiematrix, een matrix waarin de rijen de eerste meting van de steekproef bevat en de kolommen de tweede meting. Een voorbeeld bij de casus is weergegeven in Tabel 1.
# 
# <!-- ## OPENBLOK: Groepsgrootte1.R -->

# In[ ]:


## Sla de voorlopige en definitieve BSA-adviezen op
Voorlopig <- BSA_LEM$BSA_advies[BSA_LEM$Soort_BSA == "Voorlopig"]
Definitief <- BSA_LEM$BSA_advies[BSA_LEM$Soort_BSA == "Definitief"]

## Maak een frequentiematrix
BSA_frequentiematrix <- table(Voorlopig, Definitief)


# <!-- ## /OPENBLOK: Groepsgrootte1.R -->
# 
# <!-- ## TEKSTBLOK: Groepsgrootte2.R -->
# 
# ||                      | Definitief    |  |  |
# |-------------| -------------------- | -------------| ------------| ------------| 
# ||                      | Positief | Negatief| Uitgesteld |
# |**Voorlopig**| Positief      | `r BSA_frequentiematrix["Positief","Positief"]` | `r BSA_frequentiematrix["Positief","Negatief"]`     | `r BSA_frequentiematrix["Positief","Uitgesteld"]` |
# |            | Negatief | `r BSA_frequentiematrix["Negatief","Positief"]` | `r BSA_frequentiematrix["Negatief","Negatief"]`     | `r BSA_frequentiematrix["Negatief","Uitgesteld"]` |
# |            | Uitgesteld | `r BSA_frequentiematrix["Uitgesteld","Positief"]` | `r BSA_frequentiematrix["Uitgesteld","Negatief"]`     | `r BSA_frequentiematrix["Uitgesteld","Uitgesteld"]` |
# *Tabel 1. Frequentiematrix van de voorlopige en definitieve BSA-adviezen voor studenten van de bachelor Leisure & Event Management.*
# 
# De cel linksboven bevat het aantal studenten dat zowel bij het voorlopige BSA als het definitieve BSA advies een positief advies heeft ontvangen; dit zijn `r BSA_frequentiematrix["Positief","Positief"]` studenten. De cel in het midden van de frequentiematrix laat het aantal studenten zien dat zowel bij het voorlopige BSA als het definitieve BSA advies een negatief advies heeft ontvangen; dit zijn `r BSA_frequentiematrix["Negatief","Negatief"]` studenten. De cel rechtsonder bevat het aantal studenten dat zowel bij het voorlopige BSA als het definitieve BSA advies een uitgesteld advies heeft ontvangen; dit is `r BSA_frequentiematrix["Uitgesteld","Uitgesteld"]` student. Deze drie cellen staan op de diagonaal van de tabel en worden daarom de *diagonale elementen* genoemd.
# 
# Er zijn ook cellen die niet onder de diagonale elementen van de frequentiematrix vallen. Deze cellen bevatten studenten waarbij het voorlopige BSA advies verschilt van het definitieve advies. In de cel rechtsboven bijvoorbeeld staat het aantal studenten dat een positief voorlopig BSA advies en een uitgesteld definitief BSA advies heeft ontvangen; dit zijn `r BSA_frequentiematrix["Positief","Uitgesteld"]` studenten. De cel linksonder bevat het aantal studenten dat een uitgesteld voorlopig BSA advies en een positief definitief BSA advies heeft ontvangen; dit zijn `r BSA_frequentiematrix["Uitgesteld","Positief"]` studenten.
# <!-- ## /TEKSTBLOK: Groepsgrootte2.R -->

# # De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken1.R -->
# Er is een dataset ingeladen genaamd `BSA_LEM`. In deze dataset is voor elke student aangegeven wat het voorlopige en definitieve BSA advies is.
# 
# <!-- ## /TEKSTBLOK: Data-bekijken1.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.R -->

# In[ ]:


## Eerste 6 observaties
head(BSA_LEM)

## Laatste 6 observaties
tail(BSA_LEM)


# <!-- ## /OPENBLOK: Data-bekijken2.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Soort_BSA` en `BSA_advies`. In feite laat deze tabel de frequentie van het positieve, negatieve en uitgestelde BSA-advies zien voor de voorlopige en definitieve BSA. Maak de kruistabel met de functie `table()` met als argumenten de variabele `BSA_LEM$Soort_BSA`, die weergeeft of het om het voorlopige of definitieve advies gaat, en de variabele `BSA_LEM$BSA_advies`, die het BSA-advies aangeeft.
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:


## Maak een kruistabel
BSA_kruistabel <- table(BSA_LEM$Soort_BSA, BSA_LEM$BSA_advies)

## Print de kruistabel 
print(BSA_kruistabel)

## Print een tabel met proporties, tweede argument 1 zorgt ervoor dat de 
## proporties per rij berekend worden
prop.table(BSA_kruistabel, 1)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# De kruistabel en de kruistabel met proporties laten zien dat het aantal positieve BSA-adviezen hoger is bij het definitieve advies en het aantal negatieve BSA-adviezen juist lager. Het aantal uitgestelde BSA-adviezen is iets lager bij het definitieve advies.
# 
# # Uitvoering
# 
# ## Bhapkar toets
# 
# <!-- ## TEKSTBLOK: Bhapkar-toets1.R -->
# Voer de *Bhapkar toets* uit om te onderzoeken of er een verschil is tussen de verdeling van de voorlopige en definitieve BSA-adviezen voor studenten van de bachelor Leisure & Events Management. Gebruik de functie `bhapkar()` van het package `irr` met als argument een matrix met daarin de voorlopige BSA-adviezen `Voorlopig` en de definitieve BSA-adviezen `Definitief`.
# <!-- ## /TEKSTBLOK: Bhapkar-toets1.R -->
# 
# <!-- ## OPENBLOK: Bhapkar-toets2.R -->

# In[ ]:


## Laad het package van de Bhapkar toets in
library(irr)

## Sla de voorlopige en definitieve BSA-adviezen op in een vector
Voorlopig <- BSA_LEM$BSA_advies[BSA_LEM$Soort_BSA == "Voorlopig"]
Definitief <- BSA_LEM$BSA_advies[BSA_LEM$Soort_BSA == "Definitief"]

## Voer de Bhapkar toets uit
bhapkar(cbind(Voorlopig, Definitief))


# <!-- ## /OPENBLOK: Bhapkar-toets2.R -->
# 
# <!-- ## CLOSEDBLOK: Bhapkar-toets3.R -->

# In[ ]:


bhapkar <- bhapkar(cbind(Voorlopig, Definitief))
vChi2 <- Round_and_format(bhapkar$statistic)


# <!-- ## /CLOSEDBLOK: Bhapkar-toets3.R -->
# 
# <!-- ## TEKSTBLOK: Bhapkar-toets5.R -->
# * *&chi;^2^* = `r vChi2`, *p* = 0,004
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^6]
# * De verdelingen van de voorlopige en definitieve BSA-adviezen zijn verschillend.
# 
# <!-- ## /TEKSTBLOK: Bhapkar-toets5.R -->

# # Rapportage
# 
# <!-- ## CLOSEDBLOK: posthoc3.R -->

# In[ ]:


## Maak een kruistabel
BSA_kruistabel <- table(BSA_LEM$Soort_BSA, BSA_LEM$BSA_advies)

## Print de kruistabel 
print(BSA_kruistabel)

## Print een tabel met proporties, tweede argument 1 zorgt ervoor dat de 
## proporties per rij berekend worden
propBSA_kruistabel <- prop.table(BSA_kruistabel, 1)


# <!-- ## /CLOSEDBLOK: posthoc3.R -->

# <!-- ## TEKSTBLOK: Bhapkar-toets6.R -->
# De *Bhapkar toets* is uitgevoerd om uit te vinden of er een verschil tussen de verdeling van de voorlopige en definitieve BSA-adviezen van de studenten van de bachelor Leisure & Events Management. Uit de *Bhapkar toets* blijkt dat er een significant verschil is tussen de verdelingen van de voorlopige en definitieve BSA-adviezen, *&chi;^2^* = `r vChi2`, *p* < 0,0001. De frequenties en bijbehorende percentages voor de voorlopige en definitieve BSA-adviezen zijn te vinden in Tabel 2. Op basis van de resultaten en deze tabel is te zien dat er bij de definitieve BSA-adviezen meer positieve en minder negatieve BSA-adviezen zijn dan bij de voorlopige adviezen. Daarnaast is het aantal uitgestelde BSA-adviezen iets lager bij de definitieve adviezen. De persoonlijke gesprekken met de studieadviseur lijken er dus voor te zorgen dat er meer positieve en minder negatieve en uitgestelde BSA-adviezen zijn.
# 
# ||                      | BSA-advies    | |
# |-------------| -------------------- | -------------| ------------| 
# |                      | Positief | Negatief| Uitgesteld |
# | Voorlopig |  `r BSA_kruistabel["Voorlopig","Positief"]` (`r Round_and_format(100*propBSA_kruistabel["Voorlopig","Positief"])`%) | `r BSA_kruistabel["Voorlopig","Negatief"]` (`r Round_and_format(100*propBSA_kruistabel["Voorlopig","Negatief"])`%) | `r BSA_kruistabel["Voorlopig","Uitgesteld"]` (`r Round_and_format(100*propBSA_kruistabel["Voorlopig","Uitgesteld"])`%) |
# | Definitief |  `r BSA_kruistabel["Definitief","Positief"]` (`r Round_and_format(100*propBSA_kruistabel["Definitief","Positief"])`%) | `r BSA_kruistabel["Definitief","Negatief"]` (`r Round_and_format(100*propBSA_kruistabel["Definitief","Negatief"])`%) | `r BSA_kruistabel["Definitief","Uitgesteld"]` (`r Round_and_format(100*propBSA_kruistabel["Definitief","Uitgesteld"])`%) |
# *Tabel 2. Kruistabel en rijpercentages voor de voorlopige en definitieve BSA-adviezen van studenten van de bachelor Leisure & Events Management.*
# 
# <!-- ## /TEKSTBLOK: Bhapkar-toets6.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# [^2]: Sun, X., & Yang, Z., (2008) *Generalized McNemar’s Test for Homogeneity of the Marginal Distributions*. [SAS Global Forum 2008](https://support.sas.com/resources/papers/proceedings/pdfs/sgf2008/382-2008.pdf)
# [^3]: Uebersax, J. (30 augustus 2006). [*McNemar Tests of Marginal Homogeneity*](https://www.john-uebersax.com/stat/mcnemar.htm)
# [^5]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^6]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^7]: Statistics How To (29 oktober 2017). *False Discovery Rate: Simple Definition, Adjusting for FDR*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/false-discovery-rate/). 
# [^8]: Statistics How To (12 oktober 2015). *Benjamini-Hochberg Procedure*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/benjamini-hochberg-procedure/). 
# [^9]: De exacte [McNemar toets](12-McNemar-toets-R.html) wordt gebruikt als het aantal observaties in de niet-diagonale elementen van de confusiematrix kleiner dan 11 is. Voor meer informatie, zie de toetspagina van de [McNemar toets](12 McNemar toets R.Rmd).
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
