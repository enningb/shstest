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


source(paste0(here::here(),"/01. Includes/data/07.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# <!-- ## TEKSTBLOK: link1.R-->
# Gebruik de *Wilcoxon signed rank toets* om te toetsen of de som van de rangnummers[^12] van de verdelingen van twee gepaarde groepen van elkaar verschillen.[^1] Deze toets is een alternatief voor de [gepaarde t-toets](02-Gepaarde-t-toets-R.html) als de verschilscores van de gepaarde groepen niet normaal verdeeld zijn. Alleen als de verdeling van de verschilscores symmetrisch is, kan de *Wilcoxon signed rank toets* gebruikt worden om een verschil tussen de medianen van gepaarde groepen te toetsen.[^3] Als de verdeling van verschilscores niet symmetrisch is, gebruik dan de gepaarde [tekentoets](27-Tekentoets-II-R.html) om medianen te toetsen.
# <!-- ## /TEKSTBLOK: link1.R-->
# 
# # Onderwijscasus
# <div id ="casus">
# 
# De directeur van de Academie Mens & Maatschappij wil bekijken hoe het inkomen van zijn alumni zich ontwikkelt nadat zij zijn afgestudeerd. Hij is nieuwsgierig of het inkomen gedurende deze jaren groeit of juist stagneert voor deze alumni. Deze informatie is interessant om te gebruiken bij voorlichtingsactiviteiten van de Academie. Hij bekijkt het bruto jaarinkomen van de alumni één jaar na afstuderen en vergelijkt het met het bruto jaarinkomen vijf jaar na afstuderen. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil in de som van rangnummers van de verdeling tussen het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar na afstuderen en vijf jaar na afstuderen.
# 
# *H~A~*: Er is een verschil in de som van rangnummers van de verdeling tussen het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar na afstuderen en vijf jaar na afstuderen. Een van beide verdelingen bevat hogere waarden wat betreft het bruto jaarinkomen.
#  
# </div>
# 
# # Assumpties
# <!-- ## TEKSTBLOK: link2.R-->
# Het meetniveau van de afhankelijke variabele is ordinaal[^10] of continu.[^1] In deze toetspagina staat een casus met continue data centraal; een casus met ordinale data met bijbehorende uitwerking is te vinden in de [Wilcoxon signed rank toets II](22-Wilcoxon-signed-rank-toets-II-R.html).
# 
# De *Wilcoxon signed rank toets* is een alternatief voor de [gepaarde t-toets](02-Gepaarde-t-toets-R.html). Een voordeel van de *Wilcoxon signed rank toets* is dat de data niet aan de assumptie van normaliteit hoeven te voldoen. Maar als de data wel normaal verdeeld is, heeft de *Wilcoxon signed rank toets* minder onderscheidend vermogen[^4] dan de [gepaarde t-toets](02-Gepaarde-t-toets-R.html).[^5] Vandaar dat ondanks het voordeel van de grotere robuustheid minder vaak voor de *Wilcoxon signed rank toets* gekozen wordt. 
# <!-- ## /TEKSTBLOK: link2.R-->
# 
# ## Verdeling steekproef
# 
# De *Wilcoxon signed rank toets* schrijft geen assumpties voor over de verdeling van de verschilscores (verschillen tussen beide meetmomenten voor alle deelnemers[^19]).[^5] In principe toetst de *Wilcoxon signed rank toets* een hypothese over het verschil tussen de verdelingen van twee gepaarde groepen. De *Wilcoxon signed rank toets* maakt een rangschikking van de absolute waarden van de verschilscores en telt vervolgens de rangnummers op voor de positieve en negatieve verschilscores. Het verschil tussen de som van de positieve en negatieve rangnummers bepaalt de significantie van de toets. 
# 
# Als er geen symmetrische verdeling van verschilscores is, doet de *Wilcoxon signed rank toets* een uitspraak over het verschil tussen verdelingen. Een verschil tussen verdelingen kan meerdere oorzaken hebben. De top of toppen van de verdelingen kunnen verschillend zijn, maar ook de spreiding van de verdeling kan verschillen. In alle gevallen is er echter een verschil tussen de som van de rangnummers van de verdelingen. In andere woorden, de ene verdeling bevat hogere waarden dan de andere verdeling. Benoem daarom de sommen van positieve en negatieve rangnummers in de rapportage en visualiseer de verdeling van beide gepaarde groepen om duidelijk te maken op welke manier de verdelingen van elkaar verschillen.
# 
# <!-- ## TEKSTBLOK: link3.R-->
# Als de verschilscores echter symmetrisch zijn, toetst de *Wilcoxon signed rank toets* ook een hypothese over het verschil tussen de medianen van twee gepaarde groepen. In dat geval heeft de *Wilcoxon signed rank toets* een hoger onderscheidend vermogen[^4] dan de [tekentoets](06-Tekentoets-R.html) om medianen te toetsen.[^5] De [tekentoets](06-Tekentoets-R.html) vereist niet dat de verschilscores symmetrisch zijn en toetst alleen een hypothese over het verschil tussen medianen van gepaarde groepen.
# <!-- ## /TEKSTBLOK: link3.R-->
# 
# # Effectmaat
# 
# De p-waarde geeft aan of een (mogelijk) verschil tussen twee groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^6] 
# 
# De *Wilcoxon signed rank toets* heeft als effectmaat *r*. Een indicatie om *r* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^8] De effectmaat *r* wordt voor de *Wilcoxon signed rank toets* berekend door de *z*-waarde behorend bij de p-waarde van de toets te delen door de wortel van het aantal deelnemers, i.e. $\frac{z}{\sqrt{N}}$.[^8] Een correlatie tussen twee variabelen wordt vaak ook aangeduid met het symbool *r*. Beide zijn effectmaten, maar er is verder geen verband tussen de correlatie en de effectmaat van de *Wilcoxon signed rank toets*.

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
# <!-- ## TEKSTBLOK: Data-beschrijven.R-->
# Bekijk de groepsgrootte en de mediaan  van de data met `length()` en `median()`. Omdat inkomens vaak een scheve verdeling hebben, is de mediaan informatiever dan het gemiddelde.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R-->
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
# 
# <!-- ## TEKSTBLOK: Data-beschrijven3.R-->
# * Mediaan bruto jaarinkomen op T~1~: `r paste0("€",format(vMed_T1, scientific = FALSE))` 
# * Mediaan bruto jaarinkomen op T~2~: `r paste0("€",format(vMed_T2, scientific = FALSE))` 
# * Aangezien de gegevens gepaard zijn, zijn de groepsgroottes op beide meetmomenten gelijk: *n~T1~* = `r vN_T1` en *n~T2~* = `r vN_T2`
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven3.R-->
# 
# ## De data visualiseren
# 
# Maak een histogram[^18] om de verdeling van de bruto jaarinkomens van de alumni één jaar en vijf jaar na afstuderen visueel weer te geven.[^11]
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
  facet_wrap(~ Meetmoment, labeller = labeller(Meetmoment = c(T1 = "Een jaar na afstuderen", T2 = "Vijf jaar na afstuderen"))) +
  ylab("Frequentie") +
  labs(title = "Bruto jaarinkomen alumni Mens & Maatschappij")


# <!-- ## /OPENBLOK: Histogram1.R -->
# 
# Op beide meetmomenten is te zien dat de meeste alumni tussen de 0 en €35.000 euro per jaar verdienen en dat een paar alumni hierboven zit. Beide verdelingen hebben één top, maar zijn niet symmetrisch omdat de meerderheid van de observaties links van de top ligt. Beide verdeling lijken niet echt op elkaar qua vorm en spreiding.
# 
# Maak vervolgens een histogram van de verschilscores om te onderzoeken of deze verdeling symmetrisch is.
# 
# <!-- ## OPENBLOK: Histogram2.R -->

# In[ ]:


# Maak een dataset met de verschilscores
Alumni_verschilscores <- data.frame(Verschilscores = Alumni_jaarinkomens$Inkomen[Alumni_jaarinkomens$Meetmoment == "T2"] - Alumni_jaarinkomens$Inkomen[Alumni_jaarinkomens$Meetmoment == "T1"])

## Histogram met ggplot2
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
# De verdeling van de verschilscores bevat voornamelijk positieve waarden en een paar negatieve waarden; de meeste alumni zijn er dus in bruto jaarinkomen op vooruitgegaan. De verdeling is niet symmetrisch. Gebruik de *Wilcoxon signed rank toets* dus niet om een uitspraak te doen over het verschil in medianen.
# 
# ## Wilcoxon signed rank toets
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets.R -->
# Voer de *Wilcoxon signed rank toets* uit om de vraag te beantwoorden of de verdeling van de bruto jaarinkomens van alumni verschillend is voor de inkomens één jaar en vijf jaar na afstuderen. Gebruik de functie `wilcox.test()` met als eerste argument `Inkomen ~ Meetmoment` waarin `Inkomen` de afhankelijke variabele is en `Meetmoment` de onafhankelijke variabele is die twee meetmomenten aangeeft. Gebruik het argument `paired = TRUE` om aan te geven dat de twee meetmomenten aan elkaar gepaard zijn. Toets tweezijdig door het argument `alternative = "two.sided"` te gebruiken.
# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets.R -->

# In[ ]:


wilcox.test(Inkomen ~ Meetmoment, Alumni_jaarinkomens,
            paired = TRUE, 
            alternative = "two.sided")


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets2.R -->
# Bereken de effectmaat *r* vervolgens op basis van de p-waarde van de *Wilcoxon signed rank toets*.

# In[ ]:


# Sla de p-waarde op
pwaarde <- wilcox.test(Inkomen ~ Meetmoment, 
                       Alumni_jaarinkomens, 
                       paired = TRUE, 
                       alternative = "two.sided")$p.value

# Bereken de effectgrootte voor een tweezijdige toets
r <- abs(qnorm(pwaarde/2)) / sqrt(length(Alumni_jaarinkomens_T1))
# Bereken de effectgrootte voor een eenzijdige toets
#r <- abs(qnorm(pwaarde)) / sqrt(length(Alumni_jaarinkomens_T1))

# Print de effectgrootte
paste("De effectmaat is", r)


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets2.R -->
# 
# Bereken de aantallen en de sommen van positieve en negatieve rangnummers op basis van de verschilscores.
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets3.R -->

# In[ ]:


# Bereken verschilscores
Verschilscores <- Alumni_jaarinkomens$Inkomen[Alumni_jaarinkomens$Meetmoment == "T2"] - Alumni_jaarinkomens$Inkomen[Alumni_jaarinkomens$Meetmoment == "T1"]

# Rangschik de absolute waarden van verschilscores
Rangnummers <- rank(abs(Verschilscores))

# Maak een vector met daarin de tekens (plus of min) van verschilscores)
Tekens <- sign(Verschilscores)

# Bereken het aantal en de som van de positieve rangnummers
N_positief <- length(Tekens[Tekens == 1])
Som_positief <- sum(Rangnummers[Tekens == 1])

# Bereken het aantal en de som van de negatieve rangnummers
N_negatief <- length(Tekens[Tekens == -1])
Som_negatief <- sum(Rangnummers[Tekens == -1])

# Print de resultaten
N_positief
Som_positief
N_negatief
Som_negatief


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets3.R -->

# <!-- ## CLOSEDBLOK: Wilcoxon-signed-rank-toets.R -->

# In[ ]:


wilcox <- wilcox.test(Inkomen ~ Meetmoment, Alumni_jaarinkomens, paired = TRUE, alternative = "two.sided")
vVstatistic <- Round_and_format(wilcox$statistic)


# <!-- ## /CLOSEDBLOK: Wilcoxon-signed-rank-toets.R -->
# 
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets4.R -->
# * *V* = `r vVstatistic`, *p* < 0,0001 , *r* = `r Round_and_format(r)`
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen[^9]
# * De toetsstatistiek *V* is in deze casus gelijk aan de som van de negatieve rangnummers
# * Het aantal positieve rangnummers is `r N_positief`; de som is `r format(round(Som_positief), scientific = FALSE)`
# * Het aantal negatieve rangnummers is `r N_negatief`; de som is `r round(Som_negatief)`
# * De som van de positieve rangnummers is hoger dan de som van de negatieve rangnummers De verdeling van de bruto jaarinkomens bevat dus hogere waarden vijf jaar na afstuderen.
# * Effectmaat is `r Round_and_format(r)`, dus een groot effect

# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets4.R -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *Wilcoxon signed rank toets* is uitgevoerd om de vraag te beantwoorden of de verdeling van het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij verschillend is voor de inkomens één jaar na afstuderen en vijf jaar na afstuderen. De resultaten van de toets laten zien dat er een significant verschil is tussen het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar en vijf jaar na afstuderen, *V* = `r vVstatistic`, *p* < 0,0001, *r* = `r Round_and_format(r)`. Er zijn `r N_positief` alumni die vijf jaar na afstuderen meer verdienen dan één jaar na afstuderen (som van rangnummers is `r format(round(Som_positief), scientific = FALSE)`) en er zijn `r N_negatief` alumni die vijf jaar na afstuderen minder verdienen dan één jaar na afstuderen (som van rangnummers is `r Som_negatief`). Alumni lijken dus meer te verdienen wanneer ze vijf jaar afgestudeerd zijn.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Wilcoxon Signed-Rank Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/wilcoxon-signed-rank-test-using-spss-statistics.php
# [^3]: Statistics How To (27 mei 2018). *One Sample Median Test*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/one-sample-median-test/).
# [^4]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese waar is.  
# [^5]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^6]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^8]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^9]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^10]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^11]: De breedte van de staven van het histogram worden hier automatisch bepaald, maar kunnen handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^12]: Bij de *Wilcoxon signed rank toets* en andere nonparametrische toetsen wordt de data eerst gerangschikt zodat elke observatie een rangnummer toegewezen krijgt. Deze rangnummers worden vervolgens gebruikt om de toets uit te voeren.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
