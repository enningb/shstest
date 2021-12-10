#!/usr/bin/env python
# coding: utf-8
---
title: "Mann-Whitney U toets"
output:
  html_document:
    theme: lumen
    toc: yes
    toc_float: 
      collapsed: FALSE 
    number_sections: true
  keywords: [statistisch handboek, studiedata]
---
# <!-- ## CLOSEDBLOK: Functies.py -->

# In[1]:


get_ipython().run_cell_magic('R', '', 'library(here)\nif (!exists("Substitute_var")) {\n  ## Installeer packages en functies\n  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)\n}')


# <!-- ## /CLOSEDBLOK: Functies.py -->
# 
# <style>
# `r htmltools::includeHTML(paste0(here::here(),"/01. Includes/css/Stylesheet_SHHO.css"))`
# </style>
# 
# <!-- ## CLOSEDBLOK: Header.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Header.py -->
# 
# <!-- ## CLOSEDBLOK: Status.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Status.py -->
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
# Gebruik de *Mann-Whitney U toets* om te toetsen of twee onafhankelijke groepen significant van elkaar verschillen. 
# 
# Deze toets wordt ook *Mann–Whitney–Wilcoxon*, *Wilcoxon rank-sum toets*, of *Wilcoxon–Mann–Whitney toets* genoemd.[^1] Niet te verwarren met de *Wilcoxon Signed Rank Test* die toets of twee afhankelijke groepen significant van elkaar verschillen. 
# 
# De *Mann-Whitney U toets* kan een alternatief zijn voor de *ongepaarde t-toets*. De *Mann-Whitney U toets* stelt minder eisen aan de data en hoeft onder andere niet te voldoen aan de assumptie van normaliteit. Bij de *Mann-Whitney U toets* hebben uitbijters minder invloed op het eindresultaat dan bij de *ongepaarde t-toets*. Daarentegen, als de data wel normaal verdeeld zijn heeft de *Mann-Whitney U toets* minder onderscheidend vermogen dan de *ongepaarde t-toets*.[^2] Vandaar dat ondanks de voordelen er toch minder vaak voor de *Mann-Whitney U toets* test gekozen wordt. 
# 
# # Onderwijscasus
# <div id ="casus">
# De directeur van een hogeschool vraagt zich af wat de invloed is van internationalisering op zijn instelling. Om uitval een minder grote rol te laten spelen, gebruikt hij hiervoor het totaal aantal punten behaald in het tweedejaar. Hij vraagt af: ‘Is het behaald aantal EC in het tweede jaar van internationale studenten anders is dan dat van de Nederlandse studenten?’ 
# 
# *H~0~*: De verdeling van het behaalde aantal EC in het tweede jaar van internationale studenten is hetzelfde als de verdeling van Nederlandse studenten. 
# 
# *H~A~*: De verdeling van het behaalde aantal EC in het tweede jaar van internationale studenten is anders dan de verdeling van Nederlandse studenten.
# </div>
# 
# # Assumpties
# Voor een valide resultaat moeten de data aan een aantal voorwaarden voldoen voordat de toets uitgevoerd kan worden: de data zijn nomimaal, ordinaal of numeriek. De groepen zijn onafhankelijk van elkaar [^3] en het aantal groepen is 2. Gebruik bij meer dan 2 groepen de *Kruskal Wallis toets*.
# 
# # Uitvoering 
# <!-- ## TEKSTBLOK: Dataset-inladen.py -->
# Er is data ingeladen met het aantal punten dat studenten in het tweede jaar halen. `dfPunten_jaar2_NL` bevat Nederlandse studenten, `dfPunten_jaar2_inter` bevat internationale studenten. 
# <!-- ## /TEKSTBLOK: Dataset-inladen.py -->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


import pandas as pd
dfPunten_jaar2 = pd.DataFrame(r.Punten_jaar2)


# In[ ]:


## Eerste 6 observaties
print(dfPunten_jaar2.head(6))


# In[ ]:


## Laatste 6 observaties
print(dfPunten_jaar2.tail(6))


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# Bekijk de grootte, de mediaan en de kwantielen van de data met `np.size()` en `np.quantile()`.
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# <!-- ## OPENBLOK: Data-selecteren.py -->

# In[ ]:


Nederlands = dfPunten_jaar2[dfPunten_jaar2["Nederlands"] == "ja"]["EC_Jaar2"]
Niet_Nederlands = dfPunten_jaar2[dfPunten_jaar2["Nederlands"] != "ja"]["EC_Jaar2"]


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


print(np.size(Nederlands))
print(np.quantile(Nederlands, [0, 0.25, 0.5, 0.75, 1]))


# <!-- ## /OPENBLOK: Data-beschrijven-1.py -->
#   </div>
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-2.py -->

# In[ ]:


print(np.size(Niet_Nederlands))
print(np.quantile(Niet_Nederlands, [0, 0.25, 0.5, 0.75, 1]))


# <!-- ## /OPENBLOK: Data-beschrijven-2.py -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven-3.py -->
# ``` {python data beschrijven als object, include=FALSE, echo=TRUE}
# ## Onderstaand zijn de dynamische variabelen te vinden
# q_NL = np.quantile(Nederlands, [0, 0.25, 0.5, 0.75, 1])
# q_Inter = np.quantile(Niet_Nederlands, [0, 0.25, 0.5, 0.75, 1])
# 
# vN_NL = len(Nederlands)
# vN_Inter = len(Niet_Nederlands)
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
# * Mediaan Nederlandse studenten: `r Round_and_format(py$vQ2_NL)`. *n* = `r py$vN_NL`.
# * Mediaan internationale studenten: `r Round_and_format(py$vQ2_Inter)`. *n* = `r py$vN_Inter`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven2.py -->
# 
# ## Mann-Whitney U toets
# <!-- ## TEKSTBLOK: Mann-Whitney-U-toets-1.py -->
# Gebruik `pg.mwu()` met twee argumenten om een Mann-Whitney U toets te doen in Python. De standaard interpretatie van een statitische toets in Python is als: `(<teststatistiek>, <p-waarde>)`. Verder toetst Python standaard tweezijdig.
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-toets-1.py -->
# 
# <!-- ## OPENBLOK: Mann-Whitney-U-toets-2.py -->

# In[ ]:


import pingouin as pg


# In[ ]:


print(pg.mwu(Nederlands, Niet_Nederlands))


# <!-- ## /OPENBLOK: Mann-Whitney-U-toets-2.py -->
# <!-- ## CLOSEDBLOK: Mann-Whitney-U-toets-3.py -->

# In[ ]:


stat = pg.mwu(Nederlands, Niet_Nederlands)['U-val']
pval = pg.mwu(Nederlands, Niet_Nederlands)['p-val']


# <!-- ## /CLOSEDBLOK: Mann-Whitney-U-toets-3.py -->
# <!-- ## TEKSTBLOK: Mann-Whitney-U-toets-4.py -->
# * *W* = `r Round_and_format(py$stat)`, *p* = `r Round_and_format(py$pval)`
# * p-waarde > 0,05, dus de H~0~ wordt niet verworpen.[^4]
# 
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-toets-4.py -->

# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# De *Mann-Whitney U toets* is uitgevoerd om te toetsen of het behaalde aantal EC in het tweede jaar hetzelfde is van internationale studenten als van Nederlandse studenten. Uit de resultaten kan afgelezen worden dat er geen statistisch significant verschil is tussen het aantal studiepunten van internationale studenten als van Nederlandse studenten. *W* = `r Round_and_format(py$stat)`, p-waarde > 0,05. 
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
#  
# [^1]: Van Geloven, N. (13 maart 2018). *Mann-Whitney U toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Mann-Whitney_U_toets).
# [^2]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.  
# [^3]: Elke groep heeft geen overlap met één van de andere groepen en de groepen kunnen elkaars deelname niet beïnvloeden. Deze stap wordt beredeneerd en wordt niet getoetst.  
# [^4]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
