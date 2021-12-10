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
# 
# <!-- ## /CLOSEDBLOK: Reticulate.R -->
# 
# <!-- ## OPENBLOK: Data-aanmaken.R -->

# In[ ]:


source(paste0(here::here(),"/01. Includes/data/07.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# <!-- ## TEKSTBLOK: link1.R -->
# Gebruik de *tekentoets* om de medianen van twee gepaarde groepen te vergelijken.[^1] Deze toets wordt gebruikt als er niet aan de assumpties is voldaan bij sterkere toetsen zoals de [gepaarde t-toets](02-Gepaarde-t-toets-R.html) en de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html). Als de verdeling van de steekproef bij benadering normaal verdeeld is, dan kan de [gepaarde t-toets](02-Gepaarde-t-toets-R.html) gebruikt worden om de gemiddelden te vergelijken. Als de verdeling symmetrisch is, kan de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html) gebruikt worden om de medianen te vergelijken.[^3] De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-R.html) heeft in dat geval een hoger onderscheidend vermogen[^2].
# <!-- ## /TEKSTBLOK: link1.R -->
# 

# # Onderwijscasus
# <div id ="casus">
# De directeur van de Academie Mens & Maatschappij wil bekijken hoe het inkomen van zijn alumni zich ontwikkelt nadat zij zijn afgestudeerd. Hij is nieuwsgierig of het inkomen gedurende deze jaren groeit of juist stagneert voor deze alumni. Deze informatie is interessant om te gebruiken bij voorlichtingsactiviteiten van de Academie. Hij bekijkt het bruto jaarinkomen van de alumni één jaar na afstuderen en vergelijkt het met het bruto jaarinkomen vijf jaar na afstuderen. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil in de medianen van het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar na afstuderen en vijf jaar na afstuderen.
# 
# *H~A~*: Er is een verschil in de medianen van het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar na afstuderen en vijf jaar na afstuderen.
#  
# </div>
# 
# # Assumpties
# 
# Het meetniveau van de variabelen is continu.[^1]

# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is data ingeladen met het bruto jaarinkomen van alumni van de Academie Mens & Maatschappij genaamd `Alumni_jaarinkomen`. De directeur wil een vergelijking maken tussen het inkomen één jaar na afstuderen (meetmoment T~1~) en vijf jaar na afstuderen (meetmoment T~2~). 
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
head(Alumni_jaarinkomens)

## Laatste 6 observaties
tail(Alumni_jaarinkomens)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven11.R-->
# Bekijk de grootte en de mediaan  van de data met `length()` en `median()`. Maak hiervoor twee vectoren met daarin de jaarinkomens op T~1~ en T~2~.
# <!-- ## /TEKSTBLOK: Data-beschrijven11.R-->
# 
# <!-- ## OPENBLOK: Data-selecteren.R-->

# In[ ]:


Alumni_jaarinkomens_T1 <- Alumni_jaarinkomens$Inkomen[Alumni_jaarinkomens$Meetmoment == "T1"]
Alumni_jaarinkomens_T2 <- Alumni_jaarinkomens$Inkomen[Alumni_jaarinkomens$Meetmoment == "T2"]


# <!-- ## /OPENBLOK: Data-selecteren.R-->
# 
# <div class="col-container">
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-1.R -->

# In[ ]:


length(Alumni_jaarinkomens_T1)
median(Alumni_jaarinkomens_T1)


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
#   </div>
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-2.R -->

# In[ ]:


length(Alumni_jaarinkomens_T2)
median(Alumni_jaarinkomens_T2)


# <!-- ## /OPENBLOK: Data-beschrijven-2.R -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven-2.R -->

# In[ ]:


vMed_T1 <- median(Alumni_jaarinkomens_T1)
vN_T1 <- length(Alumni_jaarinkomens_T1)
vMed_T2 <- median(Alumni_jaarinkomens_T2)
vN_T2 <- length(Alumni_jaarinkomens_T2)


# <!-- ## /CLOSEDBLOK: Data-beschrijven-2.R -->
# <!-- ## TEKSTBLOK: Data-beschrijven.R-->
# * Mediaan bruto jaarinkomen op T~1~: `r paste0("€",format(vMed_T1, scientific = FALSE))` 
# * Mediaan bruto jaarinkomen op T~2~: `r paste0("€",format(vMed_T2, scientific = FALSE))` 
# * Aangezien de gegevens gepaard zijn, zijn de groepsgroottes op beide meetmomenten gelijk: *n~T1~* = `r vN_T1` en *n~T2~* = `r vN_T2`
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.R-->

# ## De data visualiseren
# 
# Maak een histogram[^18] om de verdeling van de bruto jaarinkomens van de alumni één jaar en vijf jaar na afstuderen visueel weer te geven.
# 
# <!-- ## OPENBLOK: Histogram1.R -->

# In[ ]:


## Histogram met ggplot2
library(ggplot2)

ggplot(Alumni_jaarinkomens,
  aes(x = Inkomen)) +
  geom_histogram(color = "grey30",
                 fill = "#0089CF",
                 binwidth = 2000) +
  facet_wrap(~ Meetmoment, labeller = labeller(Meetmoment = c(T1 = "Een jaar na afstudereren", T2 = "Vijf jaar na afstuderen"))) +
  geom_density(alpha = .2, adjust = 1) +
  ylab("Frequentiedichtheid") +
  labs(title = "Bruto jaarinkomen alumni Mens & Maatschappij")


# <!-- ## /OPENBLOK: Histogram1.R -->
# 
# Op beide meetmomenten is te zien dat de meeste alumni tussen de 0 en €35.000 euro per jaar verdienen en dat een paar alumni hierboven zit. Beide verdelingen hebben één top, maar zijn niet symmetrisch. Bij de inkomens 1 jaar na afstuderen ligt de meerderheid van de observaties links van de top. Bij de inkomens 5 jaar na afstuderen ligt de meerderheid van de observaties juist rechts van de top. Beide verdeling lijken niet echt op elkaar qua vorm en spreiding.
# 
# Maak vervolgens een histogram[^18] van de verschilscores.
# 
# <!-- ## OPENBLOK: Histogram2.R -->

# In[ ]:


# Maak een dataset met de verschilscores
Alumni_verschilscores <- data.frame(Verschilscores = Alumni_jaarinkomens$Inkomen[Alumni_jaarinkomens$Meetmoment == "T2"] - Alumni_jaarinkomens$Inkomen[Alumni_jaarinkomens$Meetmoment == "T1"])

## Maak een histogram met ggplot2
library(ggplot2)

ggplot(Alumni_verschilscores,
  aes(x = Verschilscores)) +
  geom_histogram(color = "grey30",
                 fill = "#0089CF",
                 binwidth = 250) +
  geom_density(alpha = .2, adjust = 1) +
  ylab("Frequentiedichtheid") +
  labs(title = "Verschilscores bruto jaarinkomen alumni Mens & Maatschappij")


# <!-- ## /OPENBLOK: Histogram2.R -->
# 
# De verdeling van de verschilscores bevat voornamelijk positieve waarden en een paar negatieve waarden; de meeste alumni zijn er dus in bruto jaarinkomen op vooruitgegaan. De verdeling lijkt niet geheel symmetrisch te zijn 
# 

# ## Tekentoets
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets.R -->
# Voer de *tekentoets* uit om de vraag te beantwoorden of de mediaan van de bruto jaarinkomens van alumni verschillend is voor de inkomens één jaar en vijf jaar na afstuderen. Gebruik om aan te geven dat de twee meetmomenten aan elkaar gepaard zijn het argument `paired = TRUE`.  Toets tweezijdig door het argument `alternative = "two.sided"` te gebruiken. Gebruik een tweezijdige toets om ook de optie open te houden dat de inkomens 5 jaar na afstuderen lager zijn dan 1 jaar na afstuderen.
# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets.R -->

# In[ ]:


library(DescTools)
SignTest(Alumni_jaarinkomens_T2, Alumni_jaarinkomens_T1, alternative = "two.sided")


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## CLOSEDBLOK: Wilcoxon-signed-rank-toets.R -->

# In[ ]:


b <- SignTest(Alumni_jaarinkomens_T2, Alumni_jaarinkomens_T1, 
              alternative = "two.sided")

vS <- b$statistic
vN <- b$parameter
vconf.int1 <- Round_and_format(b$conf.int[1])
vconf.int2 <- Round_and_format(b$conf.int[2])
vMed <- Round_and_format(b$estimate)


# <!-- ## /CLOSEDBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets2.R -->
# * Er is een significant verschil tussen het mediane inkomen vijf jaar en één jaar na afstuderen, *S* = `r vS`, *N* = `r vN`, *p* < 0,0001 [^4]
# * De toetsstatistiek *S* is het aantal positieve verschillen (inkomen vijf jaar na afstuderen hoger dan één jaar na afstuderen), *N* is het totaal aantal deelnemers[^19] (alumni)
# * Van de `r vN` alumni verdienen `r vS` alumni meer vijf jaar na afstuderen dan één jaar na afstuderen
# * De geschatte mediaan van de verschilscores is `r vMed` met bijbehorend 96%-betrouwbaarheidsinterval[^5] van `r vconf.int1` tot `r vconf.int2`.
# 
# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets2.R -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# 
# De *tekentoets* is uitgevoerd om te onderzoeken of er een verschil is tussen het mediane bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar en vijf jaar na afstuderen. De resultaten van de toets laten zien dat er een significant verschil is tussen beide medianen, *S* = `r vS`, *N* = `r vN`, *p* < 0,0001. De geschatte mediaan van de verschilscores is €`r vMed` met bijbehorend 96%-betrouwbaarheidsinterval van €`r vconf.int1` tot €`r vconf.int2`. Van de `r vN` alumni verdienen `r vS` alumni meer vijf jaar na afstuderen. Deze resultaten duiden op een verschil in het mediane bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij waarbij de inkomens vijf jaar na afstuderen hoger lijken te liggen.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Sign Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/sign-test-using-spss-statistics.php
# [^2]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese waar is.
# [^3]: Statistics How To (27 mei 2018). *One Sample Median Test*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/one-sample-median-test/).
# [^4]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^5]: Omdat het betrouwbaarheidsinterval van de mediaan van verschilscores exact berekend wordt, kan het percentage van het betrouwbaarheidsinterval afwijken van 95%. In dit geval is het 96%.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
