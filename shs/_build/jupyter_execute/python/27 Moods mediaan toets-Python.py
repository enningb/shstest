#!/usr/bin/env python
# coding: utf-8
---
title: "Mood's mediaan toets"
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
# <!-- ## CLOSEDBLOK: Functies.py -->

# In[1]:


get_ipython().run_cell_magic('R', '', 'library(here)\nif (!exists("Substitute_var")) {\n  ## Installeer packages en functies\n  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)\n}')


# <!-- ## /CLOSEDBLOK: Functies.py -->
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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/08.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# # Toepassing
# <!-- ## TEKSTBLOK: link1.py-->
# Gebruik *Mood's mediaan toets* om te toetsen of de medianen van twee ongepaarde groepen van elkaar verschillen.[^1]<sup>,</sup>[^2] Deze toets is een alternatief voor de [ongepaarde t-toets](03-Ongepaarde-t-toets-Python.html) als een van de of beide ongepaarde groepen niet normaal verdeeld zijn. *Mood's mediaan toets* kan ook gebruikt worden om medianen van meer dan twee ongepaarde groepen te vergelijken. Deze toetspagina illustreert de toets echter voor twee ongepaarde groepen.
# 
# Naast *Mood's mediaan toets* kan de [Mann-Whitney U toets](08-Mann-Whitney-U-toetsI-Python.html) ook gebruikt worden om het verschil tussen medianen van twee ongepaarde groepen te toetsen. Deze toets heeft een hoger onderscheidend vermogen[^3]<sup>,</sup>[^1], maar vereist dat de verdelingen van beide ongepaarde groepen dezelfde vorm hebben.[^4] *Mood's mediaan toets* kan ook gebruikt worden als de verdelingen niet dezelfde vorm hebben. 
# <!-- ## /TEKSTBLOK: link1.py-->

# # Onderwijscasus
# <div id ="casus">
# De onderwijsdirecteur van de opleiding Business Administration van een hogeschool vraagt zich af of er verschil is in de studieresultaten van studenten met een Nederlandse vooropleiding en een buitenlandse vooropleiding. Met name in het tweede studiejaar lijken er verschillen op te treden die hij wil begrijpen om mogelijke interventies met zijn docenten te bespreken. Hij vraagt zich af: ‘Verschilt het aantal studiepunten in het tweede studiejaar van studenten met een Nederlandse vooropleiding van het aantal studiepunten in het tweede studiejaar van studenten met een buitenlandse vooropleiding?
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: De verdeling van het behaalde aantal studiepunten in het tweede jaar van studenten met een buitenlandse vooropleiding is hetzelfde als de verdeling van studenten met een Nederlandse vooropleiding. 
# 
# *H~A~*: De verdeling van het behaalde aantal studiepunten in het tweede jaar van studenten met een buitenlandse vooropleiding is anders dan de verdeling van studenten met een Nederlandse vooropleiding.
# </div>
# 
# # Assumpties
# 
# Het meetniveau van de afhankelijke variabele is continu.[^5]<sup>,</sup>[^6] 
# 
# ## Groepsgroottes
# 
# <!-- ## TEKSTBLOK: link2.py-->
# *Mood's mediaan toets* toetst het verschil tussen de medianen van twee ongepaarde groepen. Eerst wordt de mediaan berekend van de samengevoegde observaties van beide groepen. Daarna worden voor beide ongepaarde groepen het aantal observaties groter dan en kleiner dan of gelijk aan de mediaan geteld. Dit levert een kruistabel op die vervolgens getoetst kan worden met de [Chi-kwadraat toets voor onafhankelijkheid](13-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fishers-exact-toets-Python.html). Een voorbeeld van zo'n kruistabel is te zien in Tabel 1.
# <!-- ## /TEKSTBLOK: link2.py-->
# 
# |                      | Groep 1    | Groep 2 | 
# | -------------------- | ---------- | ------------| 
# | Aantal observaties groter dan mediaan  | 20   | 25          | 
# | Aantal observaties kleiner dan of gelijk aan mediaan  | 30   | 40          |
# *Tabel 1. Kruistabel met aantal observaties groter dan en kleiner dan of gelijk aan mediaan voor twee ongepaarde groepen.*
# 
# <!-- ## TEKSTBLOK: link3.py-->
# Een assumptie van de *Chi-kwadraat toets voor onafhankelijk* is dat niet meer dan 20% van de cellen van de kruistabel een verwacht aantal observaties van vijf of minder heeft. Als dit niet het geval is, is *Fisher's exact toets* een beter alternatief. Zie de toetspagina van de [Chi-kwadraat toets voor onafhankelijkheid](13-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fishers-exact-toets-Python.html) voor een uitgebreide uitleg over deze assumptie. 
# <!-- ## /TEKSTBLOK: link3.py-->
# 
# # Uitvoering 
# <!-- ## TEKSTBLOK: Dataset-inladen.py-->
# Er is een dataset `dfStudiepunten_studiejaar2` ingeladen met het aantal punten dat studenten in het tweede jaar halen.
# <!-- ## /TEKSTBLOK: Dataset-inladen.py-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


# Pandas library importeren
import pandas as pd


# In[ ]:


import pandas as pd
dfStudiepunten_studiejaar2 = pd.DataFrame(r.Studiepunten_studiejaar2)


# In[ ]:


## Eerste 6 observaties
print(dfStudiepunten_studiejaar2.head(6))


# In[ ]:


## Laatste 6 observaties
print(dfStudiepunten_studiejaar2.tail(6))


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# Bekijk de grootte, de mediaan en de kwantielen van de data met `np.size()` en `np.quantile()`. De mediaan en kwantielen worden vaak gebruikt als maat wanneer een verdeling niet symmetrisch is.
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# <!-- ## OPENBLOK: Data-selecteren.py -->

# In[ ]:


Studiepunten_Nederlands = dfStudiepunten_studiejaar2[dfStudiepunten_studiejaar2["Vooropleiding"] == "Nederlands"]["Studiepunten"]
Studiepunten_buitenlands = dfStudiepunten_studiejaar2[dfStudiepunten_studiejaar2["Vooropleiding"] == "buitenlands"]["Studiepunten"]


# <!-- ## /OPENBLOK: Data-selecteren.py -->
# 
# <!-- ## OPENBLOK: Numpy-inladen.py -->

# In[ ]:


import numpy as np


# <!-- ## /OPENBLOK: Numpy-inladen.py -->
# 
# <div class="col-container">
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-1.py -->

# In[ ]:


print(np.size(Studiepunten_Nederlands))
print(np.quantile(Studiepunten_Nederlands, [0, 0.25, 0.5, 0.75, 1]))


# <!-- ## /OPENBLOK: Data-beschrijven-1.py -->
#   </div>
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-2.py -->

# In[ ]:


print(np.size(Studiepunten_buitenlands))
print(np.quantile(Studiepunten_buitenlands, [0, 0.25, 0.5, 0.75, 1]))


# <!-- ## /OPENBLOK: Data-beschrijven-2.py -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven-3.py -->
# ``` {python data beschrijven als object, include=FALSE, echo=TRUE}
# ## Onderstaand zijn de dynamische variabelen te vinden
# q_NL = np.quantile(Studiepunten_Nederlands, [0, 0.25, 0.5, 0.75, 1])
# q_Inter = np.quantile(Studiepunten_buitenlands, [0, 0.25, 0.5, 0.75, 1])
# 
# vN_NL = len(Studiepunten_Nederlands)
# vN_Inter = len(Studiepunten_buitenlands)
# 
# vQ1_NL = q_NL[1]
# vQ1_Inter = q_Inter[1]
# 
# vQ2_NL = q_NL[2]
# vQ2_Inter = q_Inter[2]
# 
# vQ3_NL = q_NL[3]
# vQ3_Inter = q_Inter[3]
# ```
# <!-- ## /CLOSEDBLOK: Data-beschrijven-3.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven2.py -->
# * Mediaan studenten Nederlandse vooropleiding: `r Round_and_format(py$vQ2_NL)`, *n* = `r py$vN_NL`.
# * Mediaan studenten buitenlandse vooropleiding: `r Round_and_format(py$vQ2_Inter)`, *n* = `r py$vN_Inter`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven2.py -->

# ## De data visualiseren
# 
# Maak een histogram[^18] om de verdeling van het aantal studiepunten in het tweede jaar voor studenten met een Nederlandse en buitenlandse vooropleiding visueel weer te geven.
# 
# <!-- ## OPENBLOK: Histogram1.py -->

# In[ ]:


## Histogram met matplotlib
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (15, 10))
sub1 = fig.add_subplot(1, 2, 1)
title1 = plt.title("Nederlandse vooropleiding")
hist1 = plt.hist(Studiepunten_Nederlands, density = True, edgecolor = "black", bins = 29)

sub2 = fig.add_subplot(1, 2, 2)
title2 = plt.title("Buitenlandse vooropleiding")
hist2 = plt.hist(Studiepunten_buitenlands, density = True, edgecolor = "black", bins = 31)

main = fig.suptitle('Studiepunten van studenten Business Administration in het tweede jaar')
plt.show()


# <!-- ## /OPENBLOK: Histogram1.py -->
# 
# Beide histogrammen bevatten een grote groep studenten met een laag aantal studiepunten (twaalf of minder). De overige studenten volgen een ietwat scheve verdeling met de top rond de vijftig studiepunten. De verdelingen van beide groepen studenten hebben echter niet dezelfde vorm. De frequentiedichtheid van het aantal studenten rond de vijftig studiepunten is veel hoger voor de studenten met Nederlandse vooropleiding, terwijl de frequentiedichtheid van het aantal studenten met twaalf of minder studiepunten juist hoger is voor de studenten met een buitenlandse vooropleiding.

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: groepsgrootte1.py -->
# Maak een kruistabel met het aantal observaties hoger en lager dan de mediaan voor beide ongepaarde groepen. Bereken vervolgens de verwachte aantallen observaties met de functie `sps.contingency.expected_freq()` van het package `scipy` met als argument de kruistabel `Kruistabel`.
# <!-- ## /TEKSTBLOK: groepsgrootte1.py -->
# 
# <!-- ## OPENBLOK: groepsgrootte2.py -->

# In[ ]:


import scipy.stats as sps 

# Bereken de mediaan van alle observaties samengevoegd
Mediaan = np.median(dfStudiepunten_studiejaar2["Studiepunten"])

# Bepaal voor elke observatie of deze hoger of lager/gelijk aan de mediaan is
Index_hoger_lager = dfStudiepunten_studiejaar2["Studiepunten"] > Mediaan 

# Maak een kruistabel
Kruistabel = pd.crosstab(Index_hoger_lager, dfStudiepunten_studiejaar2["Vooropleiding"])

# Bereken verwachte aantallen observaties
sps.contingency.expected_freq(Kruistabel)


# <!-- ## /OPENBLOK: groepsgrootte2.py -->

# Geen van de verwachte aantallen observaties is kleiner dan vijf, dus er is voldaan aan de assumptie over de groepsgroottes. Voer *Mood's mediaan toets* uit met behulp van de *Chi-kwadraat toets*.

# ## Mood's mediaan toets

# <!-- ## TEKSTBLOK: Moods-mediaan-toets-1.py -->
# Gebruik de functie `median_test()` van het package `scipy.stats` om *Mood's mediaan toets* uit te voeren. De eerste twee argumenten zijn vectoren met het aantal studiepunten van studenten met een Nederlandse (`Studiepunten_Nederlands`) en buitenlandse (`Studiepunten_buitenlands`) vooropleiding. Het derde argument `ties = "below"` geeft aan dat de observaties die gelijk zijn aan de mediaan opgeteld worden bij de observaties die kleiner dan de mediaan zijn.
# <!-- ## /TEKSTBLOK: Moods-mediaan-toets-1.py -->
# 
# <!-- ## OPENBLOK: Moods-mediaan-toets-2.py -->

# In[ ]:


# Sla de studiepunten van beide groepen apart op in een vector
Studiepunten_Nederlands = dfStudiepunten_studiejaar2[dfStudiepunten_studiejaar2["Vooropleiding"] == "Nederlands"]["Studiepunten"]
Studiepunten_buitenlands = dfStudiepunten_studiejaar2[dfStudiepunten_studiejaar2["Vooropleiding"] == "buitenlands"]["Studiepunten"]

# Voer Mood's mediaan toets uit
Toetsstatistiek, p_waarde, Mediaan, Kruistabel = sps.median_test(Studiepunten_Nederlands, Studiepunten_buitenlands, ties = "below")

Toetsstatistiek

p_waarde

Mediaan


# <!-- ## /OPENBLOK: Moods-mediaan-toets-2.py -->
# <!-- ## CLOSEDBLOK: Moods-mediaan-toets-3.py -->
# 
# <!-- ## /CLOSEDBLOK: Moods-mediaan-toets-3.py -->
# 
# <!-- ## TEKSTBLOK: Moods-mediaan-toets-3.py -->
# <!-- ## /TEKSTBLOK: Moods-mediaan-toets-3.py -->
# 
# <!-- ## OPENBLOK: Moods-mediaan-toets-4.py -->
# 
# <!-- ## /OPENBLOK: Moods-mediaan-toets-4.py -->

# <!-- ## TEKSTBLOK: Moods-mediaan-toets-4.py -->
# * &chi;^2^ ~ 1 ~ = `r Round_and_format(py$Toetsstatistiek)`, *p* = < 0,0001
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^9]
# * De mediaan van de variabele studiepunten is `r Round_and_format_0decimals(py$Mediaan)`  
# 
# <!-- ## /TEKSTBLOK: Moods-mediaan-toets-4.py -->

# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# *Mood's mediaan toets* is uitgevoerd om te toetsen of de mediaan van het behaald aantal studiepunten in het tweede jaar van de bachelor Business Administration hetzelfde is voor studenten met buitenlandse vooropleiding als voor studenten met Nederlandse vooropleiding. De resultaten van de toets laten zien dat er een significant verschil is tussen beide medianen, &chi;^2^ ~1~ = `r Round_and_format(py$Toetsstatistiek)`, *p* = < 0,0001. Studenten met een Nederlandse vooropleiding lijken dus meer studiepunten te behalen in het tweede jaar dan studenten met een buitenlandse vooropleiding.
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->

# [^1]: Statistics How To (28 februari 2016). *Mood’s Median Test: Definition, Run the Test and Interpret Results*. [Statistics How to](https://www.statisticshowto.com/moods-median-test/).
# [^2]: Brown, G. W., & Mood, A. M. (1951). *On median tests for linear hypotheses*. In *Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability*. The Regents of the University of California.
# [^3]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.
# [^4]: Divine, G. W., Norton, H. J., Barón, A. E., & Juarez-Colunga, E. (2018). *The Wilcoxon–Mann–Whitney procedure fails as a test of medians*. The American Statistician, 72(3), 278-286.
# [^5]: SPSS Tutorials. *SPSS Median Test for 2 Independent Medians*. Bezocht op 22 april 2020. [Statistics How to](https://www.statisticshowto.com/moods-median-test/).
# [^6]: *Mood's mediaan toets* kan ook uitgevoerd worden om de medianen te vergelijken van twee of meer ordinale variabelen. Echter, de [Mann-Whitney U toets](08-Mann-Whitney-U-toetsiI-R.html) of de [Kruskal Wallis toets](10-Kruskal-Wallis-toets-I-R.html) zijn dan alternatieven met een hoger onderscheidend vermogen.
# [^7]: De mediaan van de verschilscores kan bij twee ongepaarde steekproeven bijvoorbeeld geschat worden door alle *m x n* verschilscores te berekenen tussen *m* observaties uit de ene steekproef en *n* observaties uit de andere steekproef. De mediaan van deze *m x n* verschilscores is dan de schatting.
# [^8]: Wikipedia (10 maart 2020). *Hogdes-Lehmann estimator. *[https://en.wikipedia.org/wiki/Hodges%E2%80%93Lehmann_estimator](https://en.wikipedia.org/wiki/Hodges%E2%80%93Lehmann_estimator) 
# [^9]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
