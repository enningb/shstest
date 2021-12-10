#!/usr/bin/env python
# coding: utf-8
---
title: "Mann-Whitney U toets"
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


source(paste0(here::here(),"/01. Includes/data/23.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# # Toepassing
# Gebruik de *Mann-Whitney U toets* om te toetsen of twee ongepaarde groepen van elkaar verschillen op een ordinale[^12] variabele.[^9] Als de variabele beter als nominaal[^13] beschouwd kan worden, is de *chi-kwadraat toets voor onafhankelijkheid* of de *Fisher-Freeman-Halton exact toets* (bij een laag aantal observaties) een alternatief. Bij deze toetsen wordt echter geen rekening gehouden met de ordening van de categorieën van de ordinale variabele: de variabele wordt behandeld als een nominale variabele.
# 
# # Onderwijscasus
# <div id ="casus">
# Bij de hbo lerarenopleiding Frans leren studenten bij het vak Gesprekstechnieken om gesprekken te voeren in een praktijksetting. Aan het einde van het vak worden zij beoordeeld op basis van een mentorgesprek met een acteur waarin zij de aangeleerde vaardigheden in de praktijk kunnen toepassen. De beoordelingen bestaan uit onvoldoende, voldoende en goed. In vakevaluaties wordt vaak door mannen aangegeven dat ze het vak als erg moeilijk ervaren. Daarom wil de hoofddocent graag uitzoeken of er verschillen zijn tussen mannen en vrouwen wat betreft de beoordeling van de gesprekstechnieken.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil tussen mannen en vrouwen wat betreft (het gemiddelde rangnummer van) de beoordelingen van gesprekstechnieken.
# 
# *H~A~*: Er is een verschil tussen mannen en vrouwen wat betreft (het gemiddelde rangnummer van) de beoordelingen van gesprekstechnieken. De beoordelingen zijn hoger voor mannen of vrouwen.
# </div>
# 
# # Assumpties
# 
# Het meetniveau van de afhankelijke variabele is ordinaal[^12] of continu.[^9] In deze toetspagina staat een casus met ordinale data centraal; een casus met continue data met bijbehorende uitwerking is te vinden in de [Mann-Whitney U toets I](08-Mann-Whitney-U-toets-I-R.html).
# 
# Om de *Mann-Whitney U toets* uit te voeren met een ordinale afhankelijke variabele, moet deze variabele omgezet worden in getallen. Wanneer er drie categorieën zijn, worden ze genummerd van 1 tot en met 3 op basis van de ordening van de variabele. De categorieën onvoldoende, voldoende en goed worden dan omgezet in respectievelijk 1, 2 en 3. Bij de *chi-kwadraat toets voor onafhankelijkheid* en de *Fisher-Freeman_Halton exact toets* wordt dit niet gedaan, maar wordt de ordinale variabele als nominaal[^13] beschouwd. De *Mann-Whitney U toets* maakt een rangschikking van alle observaties van beide groepen samengevoegd en telt vervolgens apart de rangnummers op voor de observaties in beide groepen. Met behulp van de groepsgroottes kan ook het gemiddelde rangnummer van beide groepen berekend worden. Het verschil tussen de gemiddelde rangnummers in beide groepen bepaalt de significantie van de toets.[^10]
# 
# # Effectmaat
# 
# De p-waarde geeft aan of een (mogelijk) verschil tussen twee groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^3] 
# 
# De *Mann-Whitney U toets* heeft als effectmaat *r*. Een indicatie om *r* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^5] De effectmaat *r* wordt voor de *Mann-Whitney U toets* berekend door de
# *z*-waarde behorend bij de *p*-waarde van de toets te delen door de wortel van
# het aantal observaties, i.e. $\frac{z}{\sqrt{N}}$.[^5] Een correlatie tussen twee variabelen wordt vaak ook aangeduid met het symbool *r*. Beide zijn effectmaten, maar er is verder geen verband tussen de correlatie en de effectmaat van de *Wilcoxon signed rank toets*.
# 
# # Uitvoering 
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset `Beoordelingen_gesprekstechnieken` ingeladen met de beoordelingen van studenten voor het vak Gesprekstechnieken.
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Beoordelingen_gesprekstechnieken)
## Eerste 6 observaties
tail(Beoordelingen_gesprekstechnieken)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Geslacht` en `Beoordeling`. In feite laat dit zien welke beoordelingen mannen en vrouwen krijgen. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Beoordelingen_gesprekstechnieken$Geslacht` en de variabele `Beoordelingen_gesprekstechnieken$Beoordeling`.
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:


## Maak een kruistabel
Beoordelingen_kruistabel <- table(Beoordelingen_gesprekstechnieken$Geslacht, Beoordelingen_gesprekstechnieken$Beoordeling)

## Bepaal de volgorde van de beoordelingen
Volgorde <- c("Onvoldoende", "Voldoende", "Goed")

## Print de kruistabel 
print(Beoordelingen_kruistabel[,Volgorde])

## Print een tabel met proporties; het tweede argument `1` zorgt ervoor dat de 
## proporties per kolom berekend worden
prop.table(Beoordelingen_kruistabel[,Volgorde], 1)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# De kruistabel en bijbehorende kruistabel met proporties laten zien dat de gesprekstechnieken van vrouwen relatief iets vaker als goed beoordeeld worden en iets minder vaak als onvoldoende in vergelijking met de gesprechtstechnieken van mannen.

# ## De data visualiseren
# 
# Maak een staafdiagram om de verdeling van de beoordelingen voor het van Gesprekstechnieken van mannen en vrouwen visueel weer te geven.
# 
# <!-- ## OPENBLOK: Histogram1.R -->

# In[ ]:


## Histogram met ggplot2
library(ggplot2)

ggplot(Beoordelingen_gesprekstechnieken,
  aes(Beoordeling)) +
  geom_bar(color = "grey30",
                 fill = "#0089CF") +
  scale_x_discrete(limits = c("Onvoldoende", "Voldoende", "Goed")) +
  facet_wrap(~ Geslacht) +
  ylab("Frequentie") +
  labs(title = "Beoordeling van gesprekstechnieken voor mannen en vrouwen")


# <!-- ## /OPENBLOK: Histogram1.R -->
# 
# Bij zowel mannen als vrouwen krijgen de meeste studenten de beoordeling goed. Het aantal studenten waarvan de gesprekstechnieken als onvoldoende wordt beoordeeld is bij beide groepen het laagst.
# 
# ## Mann-Whitney U toets
# <!-- ## TEKSTBLOK: Mann-Whitney-U-toets-1.R -->
# Voer de *Mann-Whitney U toets* uit om de vraag te beantwoorden of er verschillen zijn tussen de beoordelingen van de gesprekstechnieken van mannen en vrouwen. Zet eerst de categorische variabele `Beoordeling` om in een numerieke variabele door de categorieën onvoldoende, voldoende en goed om te zetten in respectievelijk 1, 2 en 3. Gebruik daarna de functie `wilcox.test()` met als eerste argument `Beoordeling ~ Geslacht` waarin `Beoordeling` de afhankelijke variabele is en `Geslacht` de onafhankelijke variabele. Voer daarna het argument `paired = FALSE` in omdat de steekproeven ongepaard zijn en het argument `alternative = "two.sided"` vanwege de tweezijdige alternatieve hypothese.[^11]

# <!-- ## /TEKSTBLOK: Mann-Whitney-U-toets-1.R -->
# 
# <!-- ## OPENBLOK: Mann-Whitney-U-toets-2.R -->

# In[ ]:


# Zet de categorieën om in getallen
Beoordelingen_gesprekstechnieken$Beoordeling_numeriek[Beoordelingen_gesprekstechnieken$Beoordeling == "Onvoldoende"] <- 1
Beoordelingen_gesprekstechnieken$Beoordeling_numeriek[Beoordelingen_gesprekstechnieken$Beoordeling == "Voldoende"] <- 2
Beoordelingen_gesprekstechnieken$Beoordeling_numeriek[Beoordelingen_gesprekstechnieken$Beoordeling == "Goed"] <- 3

# Maak de variabele numeriek
Beoordelingen_gesprekstechnieken$Beoordeling_numeriek <- as.numeric(Beoordelingen_gesprekstechnieken$Beoordeling_numeriek)

# Voer de wilcoxon signed rank toets uit
wilcox.test(Beoordeling_numeriek ~ Geslacht, 
            Beoordelingen_gesprekstechnieken, 
            paired = FALSE, 
            alternative = "two.sided")


# <!-- ## /OPENBLOK: Mann-Whitney-U-toets-2.R -->
# 
# <!-- ## CLOSEDBLOK: Mann-Whitney-U-toets-3.R -->

# In[ ]:


wcx <- wilcox.test(Beoordeling_numeriek ~ Geslacht, 
                   Beoordelingen_gesprekstechnieken, 
                   paired = FALSE, 
                   alternative = "two.sided")

vW_W <- Round_and_format_0decimals(wcx$statistic)
vW_P <- Round_and_format(wcx$p.value)
vN_man <- sum(Beoordelingen_gesprekstechnieken$Geslacht == "Man")
vN_vrouw <- sum(Beoordelingen_gesprekstechnieken$Geslacht == "Vrouw")


# <!-- ## /CLOSEDBLOK: Mann-Whitney-U-toets-3.R -->
# 
# Bereken vervolgens de effectmaat *r* op basis van de p-waarde van de *Mann-Whitney U toets*.
# 
# <!-- ## OPENBLOK: Mann-Whitney-U-toets-4.R -->

# In[ ]:


# Sla de p-waarde op
pwaarde <- wilcox.test(Beoordeling_numeriek ~ Geslacht,
                       Beoordelingen_gesprekstechnieken, 
                       paired = FALSE, 
                       alternative = "two.sided")$p.value

# Bereken de effectmaat van de tweezijdige toets
r <- qnorm(pwaarde/2) / sqrt(nrow(Beoordelingen_gesprekstechnieken))
# Bereken de effectmaat van de eenzijdige toets
#r <- qnorm(pwaarde) / sqrt(nrow(Studiepunten_studiejaar2))

# Print de effectmaat
paste("De effectmaat is", abs(r))


# <!-- ## /OPENBLOK: Mann-Whitney-U-toets-4.R -->
# 
# Bereken ten slotte het gemiddelde rangnummer van beide groepen. Beoordeel op basis van de gemiddelde rangnummers welke groep hogere waardes bevat.
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets3.R -->

# In[ ]:


# Maak een index met daarin alle mannen
Index_mannen <- Beoordelingen_gesprekstechnieken$Geslacht == "Man"

# Bereken de gemiddelde rangnummers
Rangnummer_mannen <- mean(rank(Beoordelingen_gesprekstechnieken$Beoordeling_numeriek)[Index_mannen])

Rangnummer_vrouwen <- mean(rank(Beoordelingen_gesprekstechnieken$Beoordeling_numeriek)[!Index_mannen])

# Print de gemiddelde rangnummers
Rangnummer_mannen
Rangnummer_vrouwen


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets3.R -->
# 
# <!-- ## TEKSTBLOK: Mann-Whitney-U-toets-4.R -->
# * *W* = `r vW_W`, *p* = `r vW_P`, *r* = `r Round_and_format(abs(r))`
# * *p*-waarde > 0,05, dus de H~0~ wordt niet verworpen.[^8]
# * Het gemiddelde rangnummer is `r Round_and_format(Rangnummer_mannen)` (*n*=`r vN_man`) voor mannen en `r Round_and_format(Rangnummer_vrouwen)` (*n*=`r vN_vrouw`) voor vrouwen. De verdeling van vrouwen bevat dus iets hogere waarden dan de verdeling van mannen, maar dit verschil is niet significant.
# 
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-toets-4.R -->

# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *Mann-Whitney U toets* is uitgevoerd om te toetsen of de beoordeling van gesprekstechnieken bij het vak Gesprekstechnieken van de hbo lerarenopleiding Frans verschillend is voor mannen en vrouwen. De resultaten laten zien dat er geen significant verschil is tussen de beoordeling van mannen en vrouwen, *W* = `r vW_W`, *p* < 0,0001, *r* = `r Round_and_format(abs(r))`. Het gemiddelde rangnummer is `r Round_and_format(Rangnummer_mannen)` (*n*=`r vN_man`) voor mannen en `r Round_and_format(Rangnummer_vrouwen)` (*n*=`r vN_vrouw`) voor vrouwen. Ondanks het feit dat mannen het vak als moeilijk ervaren, lijken ze niet slechter te presteren dan vrouwen wat betreft gesprekstechnieken.
# 
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
#  
# [^3]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^5]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^8]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^9]: Laerd Statistics (2018). *Mann-Whitney U Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/mann-whitney-u-test-using-spss-statistics.php
# [^10]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^11]: Voor zowel de *Mann-Whitney U toets* als de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html) wordt functie `wilcox.test()` in R gebruikt. Het verschil is dat de *Mann-Whitney U toets* wordt uitgevoerd met het argument `paired = FALSE` en de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html) bij het argument `paired = TRUE`, aangezien de eerste toets ongepaarde groepen en de tweede toets gepaarde groepen vergelijkt.
# [^12]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^13]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
