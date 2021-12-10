#!/usr/bin/env python
# coding: utf-8
---
title: "Tekentoets"
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
# <!-- ## /CLOSEDBLOK: Reticulate.R -->
# 
# <!-- ## OPENBLOK: Data-aanmaken.R -->

# In[ ]:


source(paste0(here::here(),"/01. Includes/data/06.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# <!-- ## TEKSTBLOK: Link1.R -->
# Gebruik de *tekentoets* om de mediaan van een steekproef te vergelijken met een bekende mediaan of norm in een populatie.[^1] Deze toets wordt gebruikt als er niet aan de assumpties is voldaan bij sterkere toetsen zoals de [one sample t-toets](01-One-sample-t-toets-R.html) en de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html). Als de verdeling van de steekproef bij benadering normaal verdeeld is, dan kan de [one sample t-toets](01-One-sample-t-toets-R.html) gebruikt worden om het gemiddelde van een steekproef te vergelijken met een bekend gemiddelde of norm in een populatie. Als de verdeling symmetrisch is, kan de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html) gebruikt worden om de mediaan van een steekproef te vergelijken met een bekende mediaan of norm in een populatie. De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html) heeft in dat geval een hoger onderscheidend vermogen[^9].
# 
# <!-- ## /TEKSTBLOK: Link1.R -->
# 
# # Onderwijscasus
# <div id ="casus">
# De opleidingsdirecteur van de school voor Journalistiek is benieuwd wat alumni verdienen ten opzichte van de gemiddelde Nederlander. Daarom wil zij de jaarinkomens van oud-studenten vergelijken met het mediane jaarinkomen van werknemers in Nederland van €35.200.[^2] Op deze manier vergaart zij meer informatie over het succes op de arbeidsmarkt na de opleiding Journalistiek.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: De mediaan van het jaarinkomen van alumni Journalistiek is gelijk aan €35.200, het mediane jaarinkomen in Nederland.
# 
# *H~A~*: De mediaan van het jaarinkomen van alumni Journalistiek is niet gelijk aan €35.200, het mediane jaarinkomen in Nederland.
# </div>
# 
# # Assumpties
# 
# Het meetniveau van de variabele is continu.[^10]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Data-inladen.R -->
# Er is data ingeladen met jaarlijkse bruto inkomens van alumni van de school voor Journalistiek genaamd `Jaarlijks_inkomen`. De directeur wil kijken hoe haar oud-studenten scoren ten opzichte van het mediane jaarinkomen in Nederland.
# <!-- ## /TEKSTBLOK: Data-inladen.R -->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Jaarlijks_inkomen)

## Laatste 6 observaties
tail(Jaarlijks_inkomen)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# Inspecteer de data met `mean()`, `sd()`, `median()` en `length()` om meer inzicht te krijgen in de data.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# 
# <!-- ## OPENBLOK: Data-beschrijven.R -->

# In[ ]:


mean(Jaarlijks_inkomen$Inkomen)
sd(Jaarlijks_inkomen$Inkomen)
median(Jaarlijks_inkomen$Inkomen)
length(Jaarlijks_inkomen$Inkomen)


# <!-- ## /OPENBLOK: Data-beschrijven.R -->
# <!-- ## CLOSEDBLOK: Data-beschrijven2.R -->

# In[ ]:


vMean <- Round_and_format(mean(Jaarlijks_inkomen$Inkomen))
vSD   <- Round_and_format(sd(Jaarlijks_inkomen$Inkomen))
vN    <- Round_and_format(length(Jaarlijks_inkomen$Inkomen))
vMed  <- Round_and_format(median(Jaarlijks_inkomen$Inkomen))


# <!-- ## /CLOSEDBLOK: Data-beschrijven2.R -->
# 
# <!-- ## TEKSTBLOK: Datatekst-beschrijven2.R -->
# Het gemiddelde jaarinkomen van de alumni is `r paste("€", vMean, sep="")` met een standaardafwijking van `r paste("€", vSD, sep="")` (*n* = `r vN`). De mediaan van het inkomen is `r paste("€", vMed, sep="")`.
# <!-- ## /TEKSTBLOK: Datatekst-beschrijven2.R -->
# 
# ## De data visualiseren
# 
# Visualiseer de data om een goed beeld van de jaarinkomens van de alumni te krijgen. Geef de verdeling van de data weer in een histogram[^18]. Focus bij het analyseren van een histogram op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters.[^6]<sup>, </sup>[^7]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot2
library(ggplot2)

ggplot(Jaarlijks_inkomen, 
       aes(x = Inkomen)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 10000, 
                 color = "white", 
                 fill = "#158CBA") +
  #geom_density(alpha = .2, adjust = 1) +
  ylab("Frequentiedichtheid") +
  xlab("Jaarlijks inkomen") +
scale_x_continuous(labels = as.character(seq(20000, 100000, 20000)), 
                   breaks = seq(20000, 100000, 20000)) +
labs(title = "Jaarinkomen alumni Journalistiek", 
     subtitle = "")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# <!-- ## TEKSTBLOK: Link3.R -->
# De verdeling heeft één top en geen uitbijters. De histogram laat echter ook zien dat de verdeling een langere staart aan de rechterkant heeft en dus enigszins afwijkt van de (symmetrische) normaalverdeling. Aangezien de verdeling niet symmetrisch is, kan de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html) niet gebruikt worden om een hypothese over de mediaan te toetsen.
# <!-- ## /TEKSTBLOK: Link3.R -->
# 
# # Tekentoets 
# 
# <!-- ## TEKSTBLOK: Tekentoets0.R -->
# Voer een tweezijdige *tekentoets* uit om te bepalen of het mediane jaarinkomen van de alumni Journalistiek hoger ligt dan het mediane jaarinkomen in Nederland van €35.200. Gebruik van het `DescTools` package de `SignTest()` functie met de argumenten `x = Jaarlijks_inkomen` voor de data van de steekproef, `mu = 35200` voor de waarde van de mediaan die getoetst wordt en `alternative = "two.sided"` om een tweezijdige alternatieve hypothese te toetsen.
# <!-- ## /TEKSTBLOK: Tekentoets0.R -->
# 
# <!-- ## OPENBLOK: Tekentoets.R -->

# In[ ]:


library(DescTools)
SignTest(x = Jaarlijks_inkomen$Inkomen, mu = 35200, alternative = "two.sided")


# <!-- ## /OPENBLOK: Tekentoets.R -->
# 
# <!-- ## CLOSEDBLOK: Tekentoets.R -->

# In[ ]:


b <- SignTest(x = Jaarlijks_inkomen$Inkomen, mu = 35200, alternative = "two.sided")

vS <- b$statistic
vN <- b$parameter
vconf.int1 <- Round_and_format(b$conf.int[1])
vconf.int2 <- Round_and_format(b$conf.int[2])
vMed <- Round_and_format(b$estimate)


# <!-- ## /CLOSEDBLOK: Tekentoets.R -->
# 
# <!-- ## TEKSTBLOK: Tekentoets.R -->
# * De mediaan van de steekproef is significant verschillend van €35.200, *S* = `r vS`, *N* = `r vN`, *p* < 0,001. De H~0~ wordt verworpen. [^5]
# * De toetsstatistiek *S* is het aantal positieve verschillen (inkomen hoger dan het mediane jaarinkomen in Nederland), *N* is het totaal aantal verschillen
# * Van de `r vN` alumni verdienen `r vS` alumni boven het mediane jaarinkomen in Nederland
# * De geschatte mediaan van de steekproef is `r vMed` met bijbehorend 95%-betrouwbaarheidsinterval van `r vconf.int1` tot `r vconf.int2`.
# 
# <!-- ## /TEKSTBLOK: Tekentoets.R -->

# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *tekentoets* is uitgevoerd om te toetsen of het mediane inkomen van alumni van de opleiding Journalistiek veschilt van het mediane jaarinkomen van werknemers in Nederland van €35.200. Het mediane inkomen van alumni verschilt significant van €35.200 (*S* = `r vS`, *N* = `r vN`, *p* < 0,001). De geschatte mediaan is `r paste("€", vMed, sep="")` met bijbehorend 95%-betrouwbaarheidsinterval van `r paste("€", vconf.int1, sep="")` tot `r paste("€", vconf.int2, sep="")`. Van de `r vN` alumni verdienen `r vS` alumni boven het mediane jaarinkomen in Nederland. Deze resultaten duiden op een verschil tussen het mediane jaarinkomen van alumni van de opleiding Journalistiek en het mediane jaarinkomen van de gemiddelde Nederlander waarbij de inkomens van de alumni hoger lijken te liggen.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Van Geloven, N. (25 mei 2016). *Tekentoets* [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Tekentoets). 
# [^2]: Doorsnee inkomen werkenden al 10 jaar vrijwel constant (22 maart 2019). [Centraal Bureau voor de Statistiek](https://www.cbs.nl/nl-nl/nieuws/2019/12/doorsnee-inkomen-werkenden-al-10-jaar-vrijwel-constant)
# [^5]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^6]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^7]: Uitbijters kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de uitbijters valide uitbijters zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van uitbijters kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde uitbijters te melden in een rapport.
# [^8]: Statistics How To (27 mei 2018). *One Sample Median Test*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/one-sample-median-test/).
# [^9]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese waar is.
# [^10]: Miller, I. & Miller, C. (2012). *John E. Freund's Mathematical Statistics with Applications*. Pearson: eighth edition.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
