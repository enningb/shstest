#!/usr/bin/env python
# coding: utf-8
---
title: "Wilcoxon signed rank toets"
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


source(paste0(here::here(),"/01. Includes/data/22.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik de *Wilcoxon signed rank toets* om te toetsen of twee gepaarde groepen van elkaar verschillen op een ordinale[^10] variabele. Als de variabele beter als nominaal[^11] beschouwd kan worden, is de *McNemar toets* een alternatief. Bij de *McNemar toets* wordt echter geen rekening gehouden met de ordening van de categorieën van de ordinale variabele: de variabele wordt behandeld als een nominale variabele.
# 
# # Onderwijscasus
# <div id ="casus">
# De hoofddocent van het vak ‘Speech schrijven’ van de bachelor Politicologie is benieuwd naar de effectiviteit van zijn eigen vak. Daarom laat hij studenten bij de eerste bijeenkomst van het vak een speech schrijven die zij beoordeelt als onvoldoende, voldoende, goed of uitstekend. Gedurende het vak leren studenten het schrijven van speeches vanuit verschillende perspectieven. Aan het einde van het vak schrijven studenten wederom een speech die op dezelfde wijze door de hoofddocent beoordeeld wordt. Op deze manier kan hij onderzoeken of zijn lessen ervoor zorgen dat studenten beter worden in het schrijven van speeches.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil tussen de (som van rangschikkingen van de) beoordelingen van de speeches geschreven door studenten aan het begin en aan het eind van het vak.
# 
# *H~A~*: Er is een verschil tussen de (som van rangschikkingen van de) beoordelingen van de speeches geschreven door studenten aan het begin en aan het eind van het vak. De beoordelingen zijn hoger voor een van de twee meetmomenten.
#  
# </div>
# 
# # Assumpties
# 
# Het meetniveau van de afhankelijke variabele is ordinaal[^10] of continu.[^1] In deze toetspagina staat een casus met ordinale data centraal; een casus met continue data met bijbehorende uitwerking zijn te vinden in [de Wilcoxon signed rank toets I](07-Wilcoxon-signed-rank-toets-I-R.html).
# 
# Om de *Wilcoxon signed rank toets* uit te voeren met een ordinale afhankelijke variabele, moet deze variabele omgezet worden in getallen. Wanneer er vier categorieën zijn, worden ze genummerd van 1 tot en met 4 op basis van de ordening van de variabele. De categorieën onvoldoende, voldoende, goed en uitstekend worden dan omgezet in respectievelijk 1, 2, 3 en 4. Met behulp van deze getallen worden verschilscores berekend per deelnemer[^19]. Een persoon die van voldoende naar uitstekend gaat, krijgt als verschilscore 2. Hierbij wordt impliciet aangenomen dat de afstand tussen alle categorieën even groot is. In andere woorden, het verschil tussen onvoldoende en voldoende is even groot als het verschil tussen voldoende en goed en tussen goed en uitstekend. Bij de [Bhapkar toets](18-Bhapkar-toets-R.html) wordt deze aanname niet gedaan, maar wordt de ordinale variabele als nominaal[^11] beschouwd. De *Wilcoxon signed rank toets* maakt een rangschikking van de absolute waarden van de verschilscores en telt vervolgens de rangschikkingen op voor de positieve en negatieve verschilscores. Het verschil tussen de som van de positieve en negatieve rangschikkingen bepaalt de significantie van de toets.  
# 
# # Effectmaat
# 
# De p-waarde geeft aan of een (mogelijk) verschil tussen twee groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^6] 
# 
# De *Wilcoxon signed rank toets* heeft als effectmaat *r*. Een indicatie om *r* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^8] De effectmaat *r* wordt voor de *Wilcoxon signed rank toets* berekend door de *z*-waarde behorend bij de p-waarde van de toets te delen door de wortel van het aantal deelnemers, i.e. $\frac{z}{\sqrt{N}}$.[^8] Een correlatie tussen twee variabelen wordt vaak ook aangeduid met het symbool *r*. Beide zijn effectmaten, maar er is verder geen verband tussen de correlatie en de effectmaat van de *Wilcoxon signed rank toets*.
# 
# # Uitvoering
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Er is data ingeladen met de beoordeling van studenten van het vak 'Speech schrijven' aan het begin en eind van het vak. Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Beoordelingen_speech_schrijven)

## Laatste 6 observaties
tail(Beoordelingen_speech_schrijven)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Meetmoment` en `Beoordeling`. In feite laat dit zien welke beoordelingen studenten krijgen aan het begin en eind van de cursus. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Beoordelingen_speech_schrijven$Meetmoment`, die weergeeft of de speech aan het begin of eind van de cursus is geschreven en de variabele `Beoordelingen_speech_schrijven$Beoordeling` die de beoordeling weergeeft.
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:


## Maak een kruistabel
Beoordelingen_kruistabel <- table(Beoordelingen_speech_schrijven$Meetmoment, Beoordelingen_speech_schrijven$Beoordeling)

## Bepaal de volgorde van de beoordelingen
Volgorde <- c("Onvoldoende", "Voldoende", "Goed", "Uitstekend")

## Print de kruistabel 
print(Beoordelingen_kruistabel[,Volgorde])

## Print een tabel met proporties; het tweede argument `1` zorgt ervoor dat de 
## proporties per kolom berekend worden
prop.table(Beoordelingen_kruistabel[,Volgorde], 1)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# De kruistabel laat zien dat er aan het eind van het vak meer speeches als goed en uitstekend worden beoordeeld en minder speeches als onvoldoende of voldoende. Dit is ook te zien in de kruistabel met proporties.
# 
# Naast de kruistabel, is de confusiematrix ook relevant om te bekijken. Bij een confusiematrix worden de beoordelingen van studenten aan het begin en eind van de cursus tegen elkaar uitgezet. Sla daarom de variabele `Beoordeling` apart op in twee vectoren: een voor het begin van het vak en een voor het eind. Maak daarna de confusiematrix.
# 
# <!-- ## OPENBLOK: Data-beschrijven.R -->

# In[ ]:


## Definieer de groepen
Begin <- Beoordelingen_speech_schrijven$Beoordeling[Beoordelingen_speech_schrijven$Meetmoment == "Begin"]
Eind <- Beoordelingen_speech_schrijven$Beoordeling[Beoordelingen_speech_schrijven$Meetmoment == "Eind"]

## Bepaal de volgorde van de beoordelingen
Volgorde <- c("Onvoldoende", "Voldoende", "Goed", "Uitstekend")

## Maak een confusiematrix
Beoordelingen_confusiematrix <- table(Begin, Eind)

## Print de confusiematrix 
print(Beoordelingen_confusiematrix[Volgorde, Volgorde])


# <!-- ## /OPENBLOK: Data-beschrijven.R -->
# 
# De confusiematrix geeft informatie over de verschillen tussen de beoordelingen aan het begin en eind van het vak. Er zijn bijvoorbeeld 16 studenten die aan het begin goed als beoordeling ontvingen en aan het eind de beoordeling uitstekend.

# ## De data visualiseren
# 
# Maak een staafdiagram om de verdeling van de beoordelingen aan het begin en eind van het vak visueel weer te geven.
# 
# <!-- ## OPENBLOK: Histogram1.R -->

# In[ ]:


## Histogram met ggplot2
library(ggplot2)

ggplot(Beoordelingen_speech_schrijven,
  aes(Beoordeling)) +
  geom_bar(color = "grey30",
                 fill = "#0089CF") +
  scale_x_discrete(limits = c("Onvoldoende", "Voldoende", "Goed", "Uitstekend")) +
  facet_wrap(~ Meetmoment, labeller = labeller(Meetmoment = c(Begin = "Begin van het vak", Eind = "Eind van het vak"))) +
  ylab("Frequentie") +
  labs(title = "Beoordeling van het speech schrijven aan het begin en eind van het vak")


# <!-- ## /OPENBLOK: Histogram1.R -->
# 
# Aan het eind van het vak zijn er meer speeches als goed en uitstekend beoordeeld in vergelijking tot het begin van het vak. Daarnaast zijn er minder speeches als onvoldoende en voldoende beoordeeld.

# ## Wilcoxon signed rank toets
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets.R -->
# Voer de *Wilcoxon signed rank toets* uit om de vraag te beantwoorden of de beoordelingen van het schrijven van speeches bij het vak 'Speech schrijven' verschillen tussen het begin en eind van het vak. Zet eerst de categorische variabele `Beoordeling` om in een numerieke variabele door de categorieën onvoldoende, voldoende, goed en uitstekend om te zetten in respectievelijk 1, 2, 3 en 4. Gebruik daarna de functie `wilcox.test()` met als eerste argument `Beoordeling ~ Meetmoment` waarin `Beoordeling` de afhankelijke variabele is en `Meetmoment` de onafhankelijke variabele is die twee meetmomenten aangeeft. Gebruik het argument `paired = TRUE` om aan te geven dat de twee meetmomenten aan elkaar gepaard zijn.  Toets tweezijdig door het argument `alternative = "two.sided"` te gebruiken.
# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets.R -->

# In[ ]:


# Zet de categorieën om in getallen
Beoordelingen_speech_schrijven$Beoordeling_numeriek[Beoordelingen_speech_schrijven$Beoordeling == "Onvoldoende"] <- 1
Beoordelingen_speech_schrijven$Beoordeling_numeriek[Beoordelingen_speech_schrijven$Beoordeling == "Voldoende"] <- 2
Beoordelingen_speech_schrijven$Beoordeling_numeriek[Beoordelingen_speech_schrijven$Beoordeling == "Goed"] <- 3
Beoordelingen_speech_schrijven$Beoordeling_numeriek[Beoordelingen_speech_schrijven$Beoordeling == "Uitstekend"] <- 4

# Maak de variabele numeriek
Beoordelingen_speech_schrijven$Beoordeling_numeriek <- as.numeric(Beoordelingen_speech_schrijven$Beoordeling_numeriek)

# Voer de wilcoxon signed rank toets uit
wilcox.test(Beoordeling_numeriek ~ Meetmoment, Beoordelingen_speech_schrijven, 
            paired = TRUE, alternative = "two.sided")


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets2.R -->
# Bereken de effectmaat *r* vervolgens op basis van de p-waarde van de *Wilcoxon signed rank toets*.

# In[ ]:


# Sla de p-waarde op
pwaarde <- wilcox.test(Beoordeling_numeriek ~ Meetmoment, Beoordelingen_speech_schrijven, 
            paired = TRUE, alternative = "two.sided")$p.value

# Bereken de effectgrootte voor een tweezijdige toets
r <- abs(qnorm(pwaarde/2)) / sqrt(length(Beoordelingen_speech_schrijven))
# Bereken de effectgrootte voor een eenzijdige toets
#r <- abs(qnorm(pwaarde)) / sqrt(length(Beoordelingen_speech_schrijven))

# Print de effectgrootte
paste("De effectmaat is", r)


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets2.R -->
# 
# Bereken de aantallen en de sommen van positieve en negatieve rangschikkingen op basis van de verschilscores.
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets3.R -->

# In[ ]:


# Bereken de verschilscores
Verschilscores <- Beoordelingen_speech_schrijven$Beoordeling_numeriek[Beoordelingen_speech_schrijven$Meetmoment == "Eind"] - Beoordelingen_speech_schrijven$Beoordeling_numeriek[Beoordelingen_speech_schrijven$Meetmoment == "Begin"]

# Rangschik de absolute waarden van de verschilscores
Rangschikkingen <- rank(abs(Verschilscores))

# Maak een vector met daarin de tekens (plus of min) van de verschilscores)
Tekens <- sign(Verschilscores)

# Bereken het aantal en de som van de positieve rangschikkingen
N_positief <- length(Tekens[Tekens == 1])
Som_positief <- sum(Rangschikkingen[Tekens == 1])

# Bereken het aantal en de som van de negatieve rangschikkingen
N_negatief <- length(Tekens[Tekens == -1])
Som_negatief <- sum(Rangschikkingen[Tekens == -1])

# Print de resultaten
N_positief
Som_positief
N_negatief
Som_negatief


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets3.R -->

# <!-- ## CLOSEDBLOK: Wilcoxon-signed-rank-toets.R -->

# In[ ]:


wilcox <- wilcox.test(Beoordeling_numeriek ~ Meetmoment, Beoordelingen_speech_schrijven, 
            paired = TRUE, alternative = "two.sided")
vVstatistic <- Round_and_format(wilcox$statistic)


# <!-- ## /CLOSEDBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets4.R -->
# * *V* = `r vVstatistic`, *p* < 0,0001 , *r* = `r Round_and_format(r)`
# * p-waarde < 0,05, dus de H~0~ wordt verworpen[^9]
# * Het aantal positieve rangschikkingen is `r N_positief`; de som is `r format(round(Som_positief), scientific = FALSE)`
# * Het aantal negatieve rangschikkingen is `r N_negatief`; de som is `r round(Som_negatief)`
# * De som van de positieve rangschikkingen is hoger dan de som van de negatieve rangschikkingen. Er zijn dus hogere beoordelingen aan het eind van het vak in vergelijking tot het begin van het vak.
# * Effectmaat is `r Round_and_format(r)`, dus een groot effect

# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets4.R -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *Wilcoxon signed rank toets* is uitgevoerd om de vraag te beantwoorden of er verschil is tussen de beoordelingen van het schrijven van speeches aan het begin en eind van het vak 'Speech schrijven'. De resultaten van de toets laten zien dat er een significant verschil is tussen het de beoordelingen aan het begin en eind van het vak, *V* = `r vVstatistic`, *p* < 0,0001, *r* = `r Round_and_format(r)`. Er zijn `r N_positief` studenten met een hogere beoordeling aan het eind van het vak (som van rangschikkingen is `r format(round(Som_positief), scientific = FALSE)`) en er zijn `r N_negatief` studenten met een lagere beoordeling aan het eind van het vak. Studenten lijken dus beter speeches te schrijven aan het eind vak het vak.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Wilcoxon Signed-Rank Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/wilcoxon-signed-rank-test-using-spss-statistics.php
# [^6]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^8]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^9]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^10]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^11]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# 
