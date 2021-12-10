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


get_ipython().run_cell_magic('R', '', 'library(here)\nif (!exists("Substitute_var")) {\n  ## Installeer packages en functies\n  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)\n}')


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


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Header.R -->
# 
# <!-- ## CLOSEDBLOK: Status.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Status.R -->
# 
# <!-- ## CLOSEDBLOK: Reticulate.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'library(reticulate)\nknitr::knit_engines$set(python = reticulate::eng_python)')


# <!-- ## /CLOSEDBLOK: Reticulate.py -->
# 
# <!-- ## OPENBLOK: Data-aanmaken.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/07.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# <!-- ## TEKSTBLOK: link1.py -->
# Gebruik de *tekentoets* om te toetsen of de medianen van twee gepaarde groepen van elkaar verschillen.[^1] Deze toets is een alternatief voor de [gepaarde t-toets](02-Gepaarde-t-toets-Python.html) als de verschilscores van de gepaarde groepen niet normaal verdeeld zijn. De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-Python.html) kan ook gebruikt worden om het verschil tussen medianen van gepaarde groepen te toetsen. Deze toets heeft een hoger onderscheidend vermogen[^2], maar vereist dat de verdeling van de verschilscores symmetrisch is.[^3] De *tekentoets* kan ook gebruikt worden als de verdeling niet symmetrisch is. 
# <!-- ## /TEKSTBLOK: link1.py -->
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
# <!-- ## TEKSTBLOK: Dataset-inladen.py-->
# Er is data ingeladen met het bruto jaarinkomen van alumni van de Academie Mens & Maatschappij genaamd `dfAlumni_jaarinkomens`. De directeur wil een vergelijking maken tussen het inkomen één jaar na afstuderen (meetmoment T~1~) en vijf jaar na afstuderen (meetmoment T~2~). 
# <!-- ## /TEKSTBLOK: Dataset-inladen.py-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


# Pandas library importeren
import pandas as pd


# In[ ]:


dfAlumni_jaarinkomens = pd.DataFrame(r.Alumni_jaarinkomens)


# In[ ]:


# Eerste 5 observaties
print(dfAlumni_jaarinkomens.head())


# In[ ]:


# Laatste 5 observaties
print(dfAlumni_jaarinkomens.tail())


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven11.py -->
# Bekijk de grootte en de mediaan  van de data met `len()` en `np.median()` van het package `numpy`. Maak hiervoor twee vectoren met daarin de jaarinkomens op T~1~ en T~2~.
# <!-- ## /TEKSTBLOK: Data-beschrijven11.py -->
# 
# <!-- ## OPENBLOK: Data-selecteren.py-->

# In[ ]:


Alumni_jaarinkomens_T1 = dfAlumni_jaarinkomens[dfAlumni_jaarinkomens["Meetmoment"] == "T1"]["Inkomen"]
Alumni_jaarinkomens_T2 = dfAlumni_jaarinkomens[dfAlumni_jaarinkomens["Meetmoment"] == "T2"]["Inkomen"]


# <!-- ## /OPENBLOK: Data-selecteren.py-->
# 
# <div class="col-container">
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-1.py -->

# In[ ]:


import numpy as np
print(len(Alumni_jaarinkomens_T1))
print(np.median(Alumni_jaarinkomens_T1))


# <!-- ## /OPENBLOK: Data-beschrijven-1.py -->
#   </div>
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-2.py -->

# In[ ]:


import numpy as np
print(len(Alumni_jaarinkomens_T2))
print(np.median(Alumni_jaarinkomens_T2))


# <!-- ## /OPENBLOK: Data-beschrijven-2.py -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven-2.py -->

# In[ ]:


vMed_T1 = np.median(Alumni_jaarinkomens_T1)
vN_T1 = len(Alumni_jaarinkomens_T1)
vMed_T2 = np.median(Alumni_jaarinkomens_T2)
vN_T2 = len(Alumni_jaarinkomens_T2)


# <!-- ## /CLOSEDBLOK: Data-beschrijven-2.py -->
# <!-- ## TEKSTBLOK: Data-beschrijven.py-->
# 
# * Mediaan bruto jaarinkomen op T~1~: `r paste0("€",format(py$vMed_T1, scientific = FALSE))` 
# * Mediaan bruto jaarinkomen op T~2~: `r paste0("€",format(py$vMed_T2, scientific = FALSE))` 
# * Aangezien de gegevens gepaard zijn, zijn de groepsgroottes op beide meetmomenten gelijk: *n~T1~* = `r py$vN_T1` en *n~T2~* = `r py$vN_T2`
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.py-->

# ## De data visualiseren
# 
# Maak een histogram[^18] om de verdeling van de bruto jaarinkomens van de alumni één jaar en vijf jaar na afstuderen visueel weer te geven.
# 
# <!-- ## OPENBLOK: Histogram1.py -->

# In[ ]:


## Histogram met matplotlib
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (15, 10))
sub1 = fig.add_subplot(1, 2, 1)
title1 = plt.title("Een jaar na afstudereren")
hist1 = plt.hist(Alumni_jaarinkomens_T1, density = True, edgecolor = "black", bins = 29)

sub2 = fig.add_subplot(1, 2, 2)
title2 = plt.title("Vijf jaar na afstudereren")
hist2 = plt.hist(Alumni_jaarinkomens_T2, density = True, edgecolor = "black", bins = 31)

main = fig.suptitle('Bruto jaarinkomen alumni Mens & Maatschappij')
plt.show()


# <!-- ## /OPENBLOK: Histogram1.py -->
# 
# Op beide meetmomenten is te zien dat de meeste alumni tussen de 0 en €35.000 euro per jaar verdienen en dat een paar alumni hierboven zit. Beide verdelingen hebben één top, maar zijn niet symmetrisch. Bij de inkomens 1 jaar na afstuderen ligt de meerderheid van de observaties links van de top. Bij de inkomens 5 jaar na afstuderen ligt de meerderheid van de observaties juist rechts van de top. Beide verdeling lijken niet echt op elkaar qua vorm en spreiding.
# 
# Maak vervolgens een histogram[^18] van de verschilscores.
# 
# <!-- ## OPENBLOK: Histogram2.py -->

# In[ ]:


# Maak een variabele met de verschilscores
Alumni_verschilscores = np.array(Alumni_jaarinkomens_T2) - np.array(Alumni_jaarinkomens_T1)

## Histogram met matplotlib
import matplotlib.pyplot as plt
hist = plt.hist(Alumni_verschilscores, density = True, edgecolor = "black", bins = 9)
title = plt.title("Verschilscores bruto jaarinkomen alumni Mens & Maatschappij")
xlab = plt.xlabel("Verschilscores")
ylab = plt.ylabel("Frequentiedichtheid")
plt.show()


# <!-- ## /OPENBLOK: Histogram2.py -->
# 
# De verdeling van de verschilscores bevat voornamelijk positieve waarden en een paar negatieve waarden; de meeste alumni zijn er dus in bruto jaarinkomen op vooruitgegaan. De verdeling lijkt niet geheel symmetrisch te zijn 
# 

# ## Tekentoets
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets.py -->
# Voer een tweezijdige *tekentoets* uit om de vraag te beantwoorden of de mediaan van de bruto jaarinkomens van alumni verschillend is voor de inkomens één jaar en vijf jaar na afstuderen. Gebruik van het `scipy.stats` package de functie `binom_test()` met de argumenten `x = Hoger` dat het aantal alumni aangeeft dat na vijf jaar meer verdient dan na één jaar na afstuderen, `n = Aantal_observaties` dat het totaal aantal alumni aangeeft, `p = 0.5` om de nulhypothese aan te geven en `alternative = 'two-sided'` om een tweezijdige alternatieve hypothese te toetsen. De nulhypothese stelt dat er geen verschil is tussen de medianen van het bruto jaarinkomen één jaar en vijf jaar na afstuderen wat betekent dat (ongeveer) de helft van de verschilscores groter dan nul is en de helft van de verschilscores kleiner dan nul is. Vandaar dat de nulhypothese aangegeven kan worden door de verwachte proportie `p` gelijk te stellen aan `0.5`.
# 
# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets.py -->
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets.py -->

# In[ ]:


import scipy.stats as sps

# Maak een variabele met de verschilscores
Alumni_verschilscores = np.array(Alumni_jaarinkomens_T2) - np.array(Alumni_jaarinkomens_T1)

# Bereken het aantal alumni dat na 5 jaar meer verdient dan na een jaar
Hoger = sum(Alumni_verschilscores > 0)

# Bereken het totaal aantal observaties
Aantal_observaties = len(Alumni_verschilscores)

# Voer de binomiaaltoets uit
Binomiaaltoets = sps.binom_test(x = Hoger, n = Aantal_observaties, p = 0.5, alternative = 'two-sided')

print(Binomiaaltoets)

# Bereken de proportie alumni dat na 5 jaar meer verdient dan na een jaar
Proportie_boven_mediaan = Hoger / Aantal_observaties

print(Proportie_boven_mediaan)


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets.py -->
# 
# <!-- ## CLOSEDBLOK: Wilcoxon-signed-rank-toets.py -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Wilcoxon-signed-rank-toets.py -->
# 
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets2.py -->
# 
# * Er is een significant verschil tussen het mediane inkomen vijf jaar en één jaar na afstuderen, *S* = `r py$Hoger`, *N* = `r py$Aantal_observaties`, *p* < 0.0001 [^4]
# * De toetsstatistiek *S* is het aantal positieve verschillen (inkomen vijf jaar na afstuderen hoger dan één jaar na afstuderen), *N* is het totaal aantal observatie-eenheden (alumni)
# * Van de `r py$Aantal_observaties` alumni verdienen `r py$Hoger` alumni meer vijf jaar na afstuderen dan één jaar na afstuderen
# 
# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets2.py -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# 
# De *tekentoets* is uitgevoerd om te onderzoeken of er een verschil is tussen het mediane bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar en vijf jaar na afstuderen. De resultaten van de toets laten zien dat er een significant verschil is tussen beide medianen, *S* = `r py$Hoger`, *N* = `r py$Aantal_observaties`, *p* < 0.0001. Van de `r py$Aantal_observaties` alumni verdienen `r py$Hoger` alumni meer vijf jaar na afstuderen. Deze resultaten duiden op een verschil in het mediane bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij waarbij de inkomens vijf jaar na afstuderen hoger lijken te liggen.
# 
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Sign Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/sign-test-using-spss-statistics.php
# [^2]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese waar is.
# [^3]: Statistics How To (27 mei 2018). *One Sample Median Test*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/one-sample-median-test/).
# [^4]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^5]: Omdat het betrouwbaarheidsinterval van de mediaan van verschilscores exact berekend wordt, kan het percentage van het betrouwbaarheidsinterval afwijken van 95%. In dit geval is het 96%.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
