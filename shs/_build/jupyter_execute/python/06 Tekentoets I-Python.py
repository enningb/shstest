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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/06.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# 
# <!-- ## TEKSTBLOK: Link1.py -->
# Gebruik de *tekentoets* om de mediaan van een steekproef te vergelijken met een bekende mediaan of norm in een populatie.[^1] Deze toets is een alternatief voor de [one sample t-toets](01-One-sample-t-toets-Python.html) wanneer de data niet normaal verdeeld is. De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-Python.html) kan ook gebruikt worden om de mediaan van een steekproef te vergelijken met een bekende mediaan. Deze toets heeft een hoger onderscheidend vermogen[^9], maar vereist dat de verdeling van de data symmetrisch is.[^8] De *tekentoets* kan ook gebruikt worden als de verdeling van de data niet symmetrisch is.
# <!-- ## /TEKSTBLOK: Link1.py -->
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
# <!-- ## TEKSTBLOK: Data-inladen.py -->
# Er is data ingeladen met jaarlijkse bruto inkomens van alumni van de school voor Journalistiek genaamd `dfJaarlijks_inkomen`. De directeur wil kijken hoe haar oud-studenten scoren ten opzichte van het modale inkomen in Nederland.
# <!-- ## /TEKSTBLOK: Data-inladen.py -->
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


dfJaarlijks_inkomen = pd.DataFrame(r.Jaarlijks_inkomen)


# In[ ]:


# Eerste 6 observaties
print(dfJaarlijks_inkomen.head(6))


# In[ ]:


# Laatste 6 observaties
print(dfJaarlijks_inkomen.tail(6))


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# Inspecteer de data met `np.mean()`, `np.std()`, `np.median()` en `len()` van het package `numpy` om meer inzicht te krijgen in de data.
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# 
# <!-- ## OPENBLOK: Data-beschrijven.py -->

# In[ ]:


import numpy as np

np.mean(dfJaarlijks_inkomen['Inkomen'])
np.std(dfJaarlijks_inkomen['Inkomen'])
np.median(dfJaarlijks_inkomen['Inkomen'])
len(dfJaarlijks_inkomen['Inkomen'])


# <!-- ## /OPENBLOK: Data-beschrijven.py -->
# <!-- ## CLOSEDBLOK: Data-beschrijven2.py -->

# In[ ]:


vMean = np.mean(dfJaarlijks_inkomen['Inkomen'])
vSD = np.std(dfJaarlijks_inkomen['Inkomen'])
vMed = np.median(dfJaarlijks_inkomen['Inkomen'])
vN = len(dfJaarlijks_inkomen['Inkomen'])


# <!-- ## /CLOSEDBLOK: Data-beschrijven2.py -->
# 
# <!-- ## TEKSTBLOK: Datatekst-beschrijven2.py -->
# Het gemiddelde jaarinkomen van de alumni is `r paste("€", Round_and_format_0decimals(py$vMean), sep="")` met een standaardafwijking van `r paste("€", Round_and_format(py$vSD), sep="")` (*n* = `r py$vN`). De mediaan van het inkomen is `r paste("€", Round_and_format_0decimals(py$vMed), sep="")`.
# <!-- ## /TEKSTBLOK: Datatekst-beschrijven2.py -->
# 
# ## De data visualiseren
# 
# Visualiseer de data om een goed beeld van de jaarinkomens van de alumni te krijgen. Geef de verdeling van de data weer in een histogram[^18]. Focus bij het analyseren van een histogram op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters.[^6]<sup>, </sup>[^7]
# 
# <!-- ## OPENBLOK: Histogram.py -->

# In[ ]:


## Histogram met matplotlib
import matplotlib.pyplot as plt
hist = plt.hist(dfJaarlijks_inkomen['Inkomen'], density = True, edgecolor = "black", bins = 9)
title = plt.title("Jaarinkomen alumni Journalistiek")
xlab = plt.xlabel("Jaarlijks inkomen")
ylab = plt.ylabel("Frequentiedichtheid")
plt.show()


# <!-- ## /OPENBLOK: Histogram.py -->
# 
# <!-- ## TEKSTBLOK: Link3.py -->
# De verdeling heeft één top en geen uitbijters. De histogram laat echter ook zien dat de verdeling een langere staart aan de rechterkant heeft en dus enigszins afwijkt van de (symmetrische) normaalverdeling. Aangezien de verdeling niet symmetrisch is, kan de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-I-Python.html) niet gebruikt worden om een hypothese over de mediaan te toetsen.
# <!-- ## /TEKSTBLOK: Link3.py -->
# 
# # Tekentoets 
# 
# <!-- ## TEKSTBLOK: Tekentoets0.py -->
# Voer een tweezijdige *tekentoets* uit om te bepalen of het mediane jaarinkomen van de alumni Journalistiek hoger ligt dan het modale inkomen van €36.000. Gebruik van het `scipy.stats` package de functie `binom_test()` met de argumenten `x = Boven_mediaan` dat het aantal alumni aangeeft dat meer dan normaal verdient, `n = Aantal_observaties` dat het totaal aantal alumni aangeeft, `p = 0.5` om de nulhypothese aan te geven en `alternative = 'two-sided'` om een tweezijdige alternatieve hypothese te toetsen. De nulhypothese stelt dat er geen verschil is met de opgestelde mediaan van €36.000 wat betekent dat (ongeveer) de helft van de alumni meer dan dit bedrag en de helft van de alumni minder dan dit bedrag verdienen. Vandaar dat de nulhypothese aangegeven kan worden door de verwachte proportie `p` gelijk te stellen aan `0.5`.
# <!-- ## /TEKSTBLOK: Tekentoets0.py -->
# 
# <!-- ## OPENBLOK: Tekentoets.py -->

# In[ ]:


import scipy.stats as sps

# Bereken het aantal observaties met hbo vooropleiding
Boven_mediaan = sum(dfJaarlijks_inkomen['Inkomen'] > 36000)

# Bereken het totaal aantal observaties
Aantal_observaties = len(dfJaarlijks_inkomen['Inkomen'])

# Voer de binomiaaltoets uit
sps.binom_test(x = Boven_mediaan, n = Aantal_observaties, p = 0.5, alternative = 'two-sided')

# Bereken de proportie studenten met een hbo vooropleiding
Proportie_boven_mediaan = Boven_mediaan / Aantal_observaties

print(Proportie_boven_mediaan)


# <!-- ## /OPENBLOK: Tekentoets.py -->
# 
# <!-- ## CLOSEDBLOK: Tekentoets.py -->
# <!-- ## /CLOSEDBLOK: Tekentoets.py -->
# 
# <!-- ## TEKSTBLOK: Tekentoets.py -->
# * De mediaan van de steekproef is significant verschillend van €36.000, *p* < 0,0001. De nulhypothese kan worden verworpen. [^5]
# * Van de `r py$Aantal_observaties` alumni verdienen `r py$Boven_mediaan` alumni boven modaal
# * De geschatte mediaan van de steekproef is `r paste("€", Round_and_format_0decimals(py$vMed), sep="")` 
# 
# <!-- ## /TEKSTBLOK: Tekentoets.py -->

# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.py -->
# De *tekentoets* is uitgevoerd om te toetsen of het mediane inkomen van alumni van de opleiding Journalistiek veschilt van het modale inkomen in Nederland van €36.000. Het mediane inkomen van alumni verschilt significant van €36.000 (*p* < 0,0001). De geschatte mediaan van de alumni-inkomens is `r paste("€", Round_and_format_0decimals(py$vMed), sep="")`. Van de `r py$Aantal_observaties` alumni verdienen `r py$Boven_mediaan` alumni boven modaal. Deze resultaten duiden op een verschil tussen het mediane jaarinkomen van alumni van de opleiding Journalistiek en het mediane jaarinkomen van de gemiddelde Nederlander waarbij de inkomens van de alumni hoger lijken te liggen.
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


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
