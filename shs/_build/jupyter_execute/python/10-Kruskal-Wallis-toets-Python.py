#!/usr/bin/env python
# coding: utf-8
---
title: "Kruskal Wallis toets"
output: 
  html_document:
    toc: TRUE
    toc_float:
      collapsed: FALSE
    number_sections: TRUE
    theme: lumen
---
# <!-- ## CLOSEDBLOK: Functies.R -->

# In[1]:


get_ipython().run_cell_magic('R', '', 'library(here)\nif (!exists("Substitute_var")) {\n  ## Installeer packages en functies\n  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)\n}')


# <!-- ## /CLOSEDBLOK: Functies.R -->
# 
# <style>
# `r htmltools::includeHTML(paste0(here::here(),"/01. Includes/css/Stylesheet_SHHO.css"))`
# </style>
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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/10.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# Gebruik de *Kruskal Wallis toets* om te toetsen of 2 of meer groepen significant van elkaar verschillen.[^1] De *Kruskal Wallis toets* kan een alternatief zijn voor de *one-way ANOVA*.[^2] De *Kruskal Wallis toets* stelt minder eisen aan de data en hoeft onder andere niet te voldoen aan de assumptie normaliteit. Bij de *Kruskal Wallis toets* hebben uitbijters minder invloed op het eindresultaat dan bij de *one-way ANOVA*. Daarentegen, als de data wel normaal verdeeld zijn, heeft de *Kruskal Wallis toets* minder onderscheidend vermogen dan de *one way ANOVA*.[^3]<sup>, </sup>[^4] Vandaar dat ondanks de voordelen er toch minder vaak voor de *Kruskal Wallis toets* test gekozen wordt. 
# 
# # Onderwijscasus
# <div id="casus">
# De opleidingsdirecteur van de tweejarige Masteropleiding Arbeidsrecht is geïnteresseerd in de afstudeersnelheid van zijn studenten. Zij vraagt zich af of er een verschil zit in het type vooropleiding die de studenten hebben gehaald en de hoeveel studiepunten die de studenten behalen in het eerste jaar. Zij kijkt naar de vier meest gangbare vooropleidingen die de studenten doorlopen voordat ze met de Master Arbeidsrecht beginnen: de Bachelors Fiscaal Recht, Notarieel Recht en Rechtsgeleerdheid en de Premaster.  
# 
# *H~0~*: De verdeling van het aantal behaalde studiepunten in het eerste jaar van de master Arbeidsrecht is gelijk voor studenten met als vooropleiding Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster.
# 
# *H~A~*: De verdeling van het aantal behaalde studiepunten in het eerste jaar van de master Arbeidsrecht is niet gelijk voor studenten met als vooropleiding Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster.
# 
# </div>
# 
# # Assumpties
# Voor een valide resultaat moeten de data aan een aantal voorwaarden voldoen voordat de toets uitgevoerd kan worden: de data zijn (semi-)continu,[^5] de groepen zijn onafhankelijk van elkaar [^6] en het aantal groepen is groter dan 2. Gebruik bij 2 groepen de *Mann-Whitney U toets*.
# 
# # Post-hoc toets 
# De *Kruskal Wallis toets* toetst of twee of meerdere groepen van elkaar verschillen. Een post-hoc toets specificeert welke groep significant van andere groepen verschillen. Gebruik de *Mann-Whitney U toets* als post-hoc toets. 
# 
# Gebruik de *Bonferroni correctie* om Type I fouten te voorkomen. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans dat er bij toeval een verband wordt ontdekt dat er niet is.[^7]<sup>, </sup>[^8]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset ingeladen met studieresultaten van de master Arbeidsrecht per vooropleiding: Fiscaal Recht, Notarieel Recht, Rechtsgeleerdheid en de Premaster.
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


import pandas as pd
dfResultaten_Arbeidsrecht = pd.DataFrame(r.Resultaten_Arbeidsrecht)


# In[ ]:


## Eerste 6 observaties
print(dfResultaten_Arbeidsrecht.head(6))


# In[ ]:


## Laatste 6 observaties
print(dfResultaten_Arbeidsrecht.tail(6))


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken2.py -->
# De dataset bevat data van studenten van verschillende vooropleidingen. Gebruik `<data.frame>.<kolomnaam>.unique()` om te onderzoeken welke opleidingen er in de data aanwezig zijn. 
# <!-- ## /TEKSTBLOK: Data-bekijken2.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken-2.py -->

# In[ ]:


## Opleidingen in de data aanwezig
print(dfResultaten_Arbeidsrecht.Vooropleiding.unique())


# <!-- ## /OPENBLOK: Data-bekijken-2.py -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken.R-->
# Inspecteer om meer inzicht te krijgen in de data de groepen met `length()`, `median()` en `quantile()`. Groepeer hiervoor eerst met `group_by()`.
# <!-- ## /TEKSTBLOK: Data-bekijken.R-->
# 
# <!-- ## OPENBLOK: Data-beschrijven.py -->

# In[ ]:


print(dfResultaten_Arbeidsrecht.groupby(['Vooropleiding']).size())


# In[ ]:


print(dfResultaten_Arbeidsrecht.groupby(['Vooropleiding']).quantile([0.25, 0.5, 0.75]))


# <!-- ## /OPENBLOK: Data-beschrijven.py -->
# <!-- ## CLOSEDBLOK: Data-beschrijven.py -->
# ``` {python data beschrijven als object, include=FALSE, echo=TRUE}
# import numpy as np
# EC_FSC = np.array(dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Fiscaal Recht"]["EC_Jaar1"])
# EC_NTR = np.array(dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Notarieel Recht"]["EC_Jaar1"])
# EC_PRE = np.array(dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Premaster"]["EC_Jaar1"])
# EC_REC = np.array(dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Rechtsgeleerdheid"]["EC_Jaar1"])
# 
# vN_FIS = len(EC_FSC)
# vN_NOT = len(EC_NTR)
# vN_RCH = len(EC_PRE)
# vN_PM = len(EC_REC)
# 
# vQ1_FIS = np.quantile(EC_FSC, 0.25)
# vQ1_NOT = np.quantile(EC_NTR, 0.25)
# vQ1_PM = np.quantile(EC_PRE, 0.25)
# vQ1_RCH = np.quantile(EC_REC, 0.25)
# 
# vMed_FIS = np.quantile(EC_FSC, 0.5)
# vMed_NOT = np.quantile(EC_NTR, 0.5)
# vMed_RCH = np.quantile(EC_REC, 0.5)
# vMed_PM = np.quantile(EC_PRE, 0.5)
# 
# vQ3_FIS = np.quantile(EC_FSC, 0.75)
# vQ3_NOT = np.quantile(EC_NTR, 0.75)
# vQ3_RCH = np.quantile(EC_REC, 0.75)
# vQ3_PM = np.quantile(EC_PRE, 0.75)
# ```
# <!-- ## /CLOSEDBLOK: Data-beschrijven.py -->
# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# * Mediaan Fiscaal Recht: `r Round_and_format(py$vMed_FIS)`. *n* = `r py$vN_FIS`.
# * Mediaan Notarieel Recht: `r Round_and_format(py$vMed_NOT)`. *n* = `r py$vN_NOT`.
# * Mediaan Premaster: `r Round_and_format(py$vMed_PM)`. *n* = `r py$vN_PM`.
# * Mediaan Rechtsgeleerdheid: `r Round_and_format(py$vMed_RCH)`. *n* = `r py$vN_RCH`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# 
# ### Boxplot
# De box geeft de middelste 50% van het aantal studiepunten weer. De zwarte lijn binnen de box is de mediaan. De staarten bevatten de eerste 25% en de laatste 25%. Cirkels visualiseren mogelijke uitbijters. Hoe meer de boxen overlappen, hoe waarschijnlijker er geen significant verschil is tussen de groepen. 
# 
# <!-- ## OPENBLOK: Boxplot.py -->

# In[ ]:


import matplotlib.pyplot as plt
box = dfResultaten_Arbeidsrecht.boxplot(column='EC_Jaar1', by='Vooropleiding')
no_suptitle = plt.suptitle("")
title = plt.title("Aantal EC per vooropleiding van de Master Arbeidsrecht")
ylab = plt.ylabel("Aantal EC in jaar 1")
no_grid = plt.grid(b = False)
plt.show()


# <!-- ## /OPENBLOK: Boxplot.py -->
# 
# De mediaan van studenten met een vooropleiding Rechtsgeleerdheid heeft duidelijk minder studiepunten dan studenten met een vooropleiding Fiscaal Recht en Notarieel Recht. De mediaan van de studenten met de Premaster als vooropleiding ligt er tussen in.[^9]
# 
# ## Kruskal Wallis toets
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-1.py -->
# Gebruik `stats.kruskal()` om de Kruskal-Wallis toets uit te voeren. Eerst moet de data worden gesplitst per opleiding. De standaard interpretatie van een statitische toets in Python is: `(<teststatistiek>, <p-waarde>)`. Verder toetst Python standaard tweezijdig.
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-1.py -->
# 
# <!-- ## OPENBLOK: Kruskal-Wallis-test-2.py -->

# In[ ]:


# We splitsen de dataset per opleiding
EC_FSC = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Fiscaal Recht"]["EC_Jaar1"]
EC_NTR = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Notarieel Recht"]["EC_Jaar1"]
EC_PRE = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Premaster"]["EC_Jaar1"]
EC_REC = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Rechtsgeleerdheid"]["EC_Jaar1"]


# In[ ]:


import scipy.stats as stats
print(stats.kruskal(EC_FSC, EC_NTR, EC_PRE, EC_REC))


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-2.py -->
# 
# <!-- ## CLOSEDBLOK: Kruskal-Wallis-test-3.py -->

# In[ ]:


stat, pval = stats.kruskal(EC_FSC, EC_NTR, EC_PRE, EC_REC)
df = 3


# <!-- ## /CLOSEDBLOK: Kruskal-Wallis-test-3.py -->
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-4.py -->
# * *df*: het aantal groepen - 1 = `r py$df`  
# * *H*~3~ = `r Round_and_format(py$stat)`, p < 0,05  
# * De test-statistiek *H* volgt bij benadering de chi-kwadraat verdeling. Onder deze hypothese is *H* chi-kwadraat, vandaar dat dit in de output uitgedrukt wordt in chi-kwadraat    
# * p-waarde < 0,05, dus de H~0~ wordt verworpen[^10]
# 
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-4.py -->

# ## Post-hoc toets: Mann-Whitney U toets
# <!-- ## TEKSTBLOK: Mann-Whitney-U-test.py -->
# Gebruik de *Mann-Whitney U toets* als post-hoc toets om te bepalen wélke groepen significant verschillen. De *Mann-Whitney U toets* wordt ook wel de *Wilcoxon rank-sum toets* genoemd.[^10] Gebruik de functie `pg.mwu()`. 
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-test.py -->
# <!-- ## OPENBLOK: Mann-Whitney-U-test.py -->

# In[ ]:


import pingouin as pg


# In[ ]:


# Correctie kan gedaan worden door p-value x aantal Hypotheses te doen (= 6)
pg.mwu(EC_PRE, EC_NTR)


# <!-- ## /OPENBLOK: Mann-Whitney-U-test.py-->
# * Er is geen statistisch significant verschil gevonden tussen Fiscaal Recht en Notarieel Recht.
# * Er is ook geen statistisch significant verschil gevonden tussen Fiscaal Recht en de Premaster.
# * Er is een statistisch significant verschil gevonden tussen de Premaster en Notarieel Recht.   
# * Er zijn statistisch significante verschillen gevonden tussen Rechtsgeleerdheid en de overige vooropleidingen.
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# De *Kruskal Wallis toets* is uitgevoerd om te toetsen of significante verschillen zijn tussen de studenten van de Master Arbeidsrecht met als vooropleiding Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster en het aantal studiepunten dat de studenten in het eerste jaar behalen. Uit de resultaten kan afgelezen worden dat er een statistisch significant verschil is tussen het aantal studiepunten en het type vooropleiding dat de student heeft afgerond. *H*~`r py$df`~ ≈ `r Round_and_format(py$stat)` < 0,05.   
# 
# | Vooropleiding     | N          | Q1         | M           | Q3          |
# | ------------- | ---------- | ---------- | ----------- | ----------- |
# | Fiscaal Recht      | `r py$vN_FIS` | `r Round_and_format(py$vQ1_FIS)` | `r Round_and_format(py$vMed_FIS)` | `r Round_and_format(py$vQ3_FIS)` |
# | Notarieel Recht     | `r py$vN_NOT` | `r Round_and_format(py$vQ1_NOT)` | `r Round_and_format(py$vMed_NOT)` | `r Round_and_format(py$vQ3_NOT)` |
# | Rechtsgeleerdheid  | `r py$vN_RCH` | `r Round_and_format(py$vQ1_RCH)` | `r Round_and_format(py$vMed_RCH)` | `r Round_and_format(py$vQ3_RCH)` |
# | Premaster          | `r py$vN_PM`| `r Round_and_format(py$vQ1_PM)` | `r Round_and_format(py$vMed_PM)` | `r Round_and_format(py$vQ3_PM)` |
# *Tabel 1. Groepsgrootte, 1e kwantiel, mediaan en 3e kwantiel per vooropleiding*
# 
# Met een post-hoc toets is het verschil tussen de vooropleidingen getoetst. De studenten met Rechtsgeleerdheid als vooropleiding behalen statistisch significant minder punten bij de Master Arbeidsrecht, dan de studenten met een andere vooropleiding. Er is een statistisch significant verschil gevonden tussen de behaalde studiepunten van studenten met de vooropleiding Notarieel Recht en de Premaster, waarbij de studenten van de Premaster minder punten behaalden dan de studenten van Notarieel Recht. Er zijn geen statistisch significante verschillen gevonden tussen de vooropleidingen Fiscaal Recht en Notarieel Recht, en Fiscaal Recht en Premaster. De *Bonferroni correctie* is gebruikt om de Type I fout te voorkomen die gepaard gaat met het veelvuldig toetsen.  
# 
# Kortom, de resultaten ondersteunen de conclusie dat er een verschil is tussen de vooropleidingen die de studenten hebben afgerond en de hoeveelheid studiepunten die een student behaalt tijdens het eerste jaar van de master Arbeidsrecht. De studenten met Rechtsgeleerdheid als vooropleiding behalen statistisch significant minder studiepunten dan de drie andere vooropleidingen. 
# Studenten met de vooropleiding Fiscaal Recht (mediaan = `r Round_and_format(py$vMed_FIS)`) en Notarieel Recht (mediaan = `r Round_and_format(py$vMed_NOT)`) behalen naar verhouding de meeste studiepunten.
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: De toets rangschikt de datapunten van laag naar hoog en geeft elke datapunt een rangnummer. Vervolgens wordt per groep het gemiddelde berekend van de rangnummers. Dit gemiddelde wordt met elkaar vergeleken. Voor meer informatie lees: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^2]: Van Geloven, N. (21 maart 2018). *Kruskal Wallis*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Kruskal_Wallis). 
# [^3]: Universiteit van Amsterdam (7 juli 2014). *Kruskal-Wallis Test*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Kruskal-Wallis_Test). 
# [^4]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.  
# [^5]: Semi-continue data: de data zijn discreet, bijvoorbeeld gehele getallen, met zoveel mogelijkheden dat de data geanalyseerd kunnen worden alsof ze continu zijn. Van Geloven, N. (21 November 2017). *KEUZE TOETS*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/KEUZE_TOETS).
# [^6]: Elke groep heeft geen overlap met één van de andere groepen en de groepen kunnen elkaars deelname niet beïnvloeden. Deze stap wordt beredeneerd en wordt niet getoetst.  
# [^7]: Type I fout: Ten onrechte H~0~ verwerpen.
# [^8]: Universiteit van Amsterdam (7 juli 2014). *Kruskal-Wallis Test*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Kruskal-Wallis_Test).
# [^9]: Bij niet normaal verdeelde data wordt de mediaan berekend in plaats van een gemiddelde om het midden van de data aan te geven. 
# [^10]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met Type I en Type II fouten. 
# [^11]: Van Geloven, N. (13 maart 2018).  *Mann-Whitney U toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Mann-Whitney_U_toets).
# 
