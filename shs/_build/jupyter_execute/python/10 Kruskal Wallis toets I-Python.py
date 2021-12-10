#!/usr/bin/env python
# coding: utf-8
---
title: "Kruskal Wallis toets"
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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/10.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# <!-- ## TEKSTBLOK: link1.py -->
# Gebruik de *Kruskal Wallis toets* om te toetsen of de gemiddelde rangnummers van de verdelingen van twee of meer groepen van elkaar verschillen.[^1]<sup>, </sup>[&17] De *Kruskal Wallis toets* kan een alternatief zijn voor de [one-way ANOVA](05-One-way-ANOVA-Python.html).[^2] De *Kruskal Wallis toets* hoeft niet te voldoen aan de assumptie van normaliteit van de verdelingen van elke groep. Daarnaast hebben uitbijters bij de *Kruskal Wallis toets*  minder invloed op het eindresultaat dan bij de [one-way ANOVA](05-One-way-ANOVA-Python.html). Daarentegen, als de data wel normaal verdeeld is, heeft de *Kruskal Wallis toets* minder onderscheidend vermogen[^4] dan de [one-way ANOVA](05-One-way-ANOVA-Python.html).[^3] Vandaar dat ondanks de voordelen van de grotere robuustheid er toch minder vaak voor de *Kruskal Wallis toets* gekozen wordt. 
# <!-- ## /TEKSTBLOK: link1.py -->
# 
# # Onderwijscasus
# <div id="casus">
# De opleidingsdirecteur van de tweejarige Masteropleiding Arbeidsrecht is geïnteresseerd in de afstudeersnelheid van haar studenten. Zij vraagt zich af of er een verschil zit in het type vooropleiding dat de studenten hebben gehaald en de hoeveel studiepunten die de studenten behalen in het eerste jaar. Zij kijkt naar de vier meest gangbare vooropleidingen die de studenten doorlopen voordat ze met de Master Arbeidsrecht beginnen: de Bachelors Fiscaal Recht, Notarieel Recht en Rechtsgeleerdheid en de Premaster. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het gemiddelde rangnummer van de verdeling van het aantal behaalde studiepunten in het eerste jaar van de master Arbeidsrecht is gelijk voor de studenten met als vooropleidingen Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster.
# 
# *H~A~*: Het gemiddelde rangnummer van de verdeling van het aantal behaalde studiepunten in het eerste jaar van de master Arbeidsrecht is niet gelijk voor de studenten met als vooropleiding Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster.
# 
# </div>
# 
# # Assumpties
# <!-- ## TEKSTBLOK: link2.py -->
# Het meetniveau van de afhankelijke variabele is ordinaal[^16] of continu.[^6] In deze toetspagina staat een casus met continue data centraal; een casus met ordinale data met bijbehorende uitwerking is te vinden in de [Kruskal Wallis toets II](25-Kruskall-Wallis-toets-II-Python.html). 
# <!-- ## /TEKSTBLOK: link2.py -->
# 
# # Post-hoc toets 
# <!-- ## TEKSTBLOK: link3.py -->
# De *Kruskal Wallis toets* toetst of twee of meerdere groepen van elkaar verschillen. Een post-hoc toets specificeert of groep significant van een andere groep verschilt. Gebruik de [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-Python.html) als post-hoc toets. Hoewel het minder gebruikelijk is, is *Moods'mediaan toets* ook een optie als post-hoc toets. Deze toets toetst het verschil tussen de medianen van twee ongepaarde groepen. De [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-Python.html) toetst het verschil tussen de verdelingen van twee ongepaarde groepen.
# <!-- ## /TEKSTBLOK: link3.py -->
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout.[^9] Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^5]
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^2] 
# 
# Bij de *Kruskal Wallis toets* wordt eta-squared (*η^2^*) als effectmaat gebruikt.[^10] De effectmaat eta squared (*η^2^*) berekent de proportie van de variantie in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele. In deze casus berekent het de proportie van de variantie in het aantal studiepunten wat verklaard kan worden door de vooropleiding. Een indicatie om *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^11]
# 

# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.py-->
# Er is een dataset `dfResultaten_Arbeidsrecht` ingeladen met studieresultaten van het eerste jaar van de master Arbeidsrecht per vooropleiding: Fiscaal Recht, Notarieel Recht, Rechtsgeleerdheid en de Premaster.
# <!-- ## /TEKSTBLOK: Dataset-inladen.py-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


import pandas as pd
dfResultaten_Arbeidsrecht = pd.DataFrame(r.Resultaten_Arbeidsrecht)


# In[ ]:


import pandas as pd
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
print(dfResultaten_Arbeidsrecht['Vooropleiding'].unique())


# <!-- ## /OPENBLOK: Data-bekijken-2.py -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken3.py -->
# Inspecteer om meer inzicht te krijgen in de data de groepen met `.size()` en `.quantile()`. Groepeer hiervoor eerst met `<dataframe>.groupby([<column>])`. De mediaan is gelijk aan kwantiel `0.5`.
# <!-- ## /TEKSTBLOK: Data-bekijken3.py -->
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
# * Mediaan Fiscaal Recht is `r Round_and_format(py$vMed_FIS)`, *n* = `r py$vN_FIS`.
# * Mediaan Notarieel Recht is `r Round_and_format(py$vMed_NOT)`, *n* = `r py$vN_NOT`.
# * Mediaan Premaster is `r Round_and_format(py$vMed_PM)`, *n* = `r py$vN_PM`.
# * Mediaan Rechtsgeleerdheid is `r Round_and_format(py$vMed_RCH)`, *n* = `r py$vN_RCH`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# 
# ## De data visualiseren
# 
# Geef de verdeling van de verschillende vooropleidingen visueel weer met een histogram.[^18]
# 
# <!-- ## OPENBLOK: Histogram.py -->

# In[ ]:


# Laad seaborn of facets te maken
import seaborn as sb
# Laad matplotlib.pyplot om plots te maken
import matplotlib.pyplot as plt

# Maak een facet plot met een histogram voor elke vooropleiding
g = sb.FacetGrid(dfResultaten_Arbeidsrecht, col="Vooropleiding")
g = (g.map(plt.hist, "EC_Jaar1", edgecolor = "black").set_axis_labels("Aantal studiepunten jaar 1"))
plt.show()


# <!-- ## /OPENBLOK: Histogram.py -->
# 
# Allereerst valt op dat de verdeling enigszins discreet is. Aangezien er in deze casus zes studiepunten per vak te verdienen zijn met een totaal van 60 in het eerste jaar, bestaan de histogrammen uit staven waartussen de verschillen zes studiepunten zijn. De verdeling van alle vier de vooropleidingen zijn niet normaal maar scheef verdeeld. Met uitzondering van de vooropleiding Rechtsgeleerdheid ligt de top op 60 studiepunten en is er een staart links daarvan.
# 
# ## Kruskal Wallis toets
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-1.py -->
# Voer de *Kruskal Wallis toets* uit om te onderzoeken of er verschillen zijn in het aantal studiepunten in het eerste jaar tussen de studenten van de master Arbeidsrecht met vier verschillende vooropleidingen   Gebruik de functie `kruskal()` van het package `scipy` met als argumenten vier variabelen met het aantal studiepunten `EC_Jaar1` voor elk van de vier vooropleidingen. Bij deze functie toetst Python standaard tweezijdig.
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-1.py -->
# 
# <!-- ## OPENBLOK: Kruskal-Wallis-test-2.py -->

# In[ ]:


# Maak een variabele met het aantal studiepunten voor elke vooropleiding
EC_FSC = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Fiscaal Recht"]["EC_Jaar1"]
EC_NTR = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Notarieel Recht"]["EC_Jaar1"]
EC_PRE = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Premaster"]["EC_Jaar1"]
EC_REC = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Rechtsgeleerdheid"]["EC_Jaar1"]


# In[ ]:


# Voer de Kruskal Wallis toets uit
import scipy.stats as sp
print(sp.kruskal(EC_FSC, EC_NTR, EC_PRE, EC_REC))


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-2.py -->
# 
# Bereken de effectmaat *&eta;^2^* vervolgens op basis van de *&chi;^2^*-waarde van de *Kruskal-Wallis toets*.
# <!-- ## OPENBLOK: Kruskal-Wallis-test-3.py -->

# In[ ]:


# Sla de teststatistiek op
stat, pval = sp.kruskal(EC_FSC, EC_NTR, EC_PRE, EC_REC)

# Bereken eta squared
Eta_squared = stat / (len(dfResultaten_Arbeidsrecht['EC_Jaar1']) - 1)

# Print de effectgrootte
print(Eta_squared)


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-3.py -->

# <!-- ## CLOSEDBLOK: Kruskal-Wallis-test-4.py -->

# In[ ]:


stat, pval = sp.kruskal(EC_FSC, EC_NTR, EC_PRE, EC_REC)
df = 3


# <!-- ## /CLOSEDBLOK: Kruskal-Wallis-test-4.py -->
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-5.py -->
# * *df*: het aantal groepen - 1 = `r py$df`  
# * *H* = `r Round_and_format(py$stat)`, *df* = `r py$df`, *p* < 0,0001, *&eta;^2^* = `r Round_and_format(py$Eta_squared)`  [^13]  
# * p-waarde < 0,05, dus de H~0~ wordt verworpen[^14]
# * Eta squared is `r Round_and_format(py$Eta_squared)` wat duidt op een gemiddeld tot groot effect 
# 
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-5.py -->

# ## Post-hoc toets: Mann-Whitney U toets
# <!-- ## TEKSTBLOK: Mann-Whitney-U-test.py -->
# Gebruik de *Mann-Whitney U toets* als post-hoc toets om te bepalen wélke groepen significant verschillen. De *Mann-Whitney U toets* wordt ook wel de *Wilcoxon rank-sum toets* genoemd.[^10] Gebruik de functie `pg.mwu()`. 
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-test.py -->
# <!-- ## OPENBLOK: Mann-Whitney-U-test.py -->

# In[ ]:


import scikit_posthocs as skph

skph.posthoc_mannwhitney(dfResultaten_Arbeidsrecht, val_col = 'EC_Jaar1', group_col = 'Vooropleiding', p_adjust = 'bonferroni')


# <!-- ## /OPENBLOK: Mann-Whitney-U-test.py-->
# 
# <!-- ## CLOSEDBLOK: Mann-Whitney-U-test1.py -->

# In[ ]:


import scikit_posthocs as skph

pTabel = skph.posthoc_mannwhitney(dfResultaten_Arbeidsrecht, val_col = 'EC_Jaar1', group_col = 'Vooropleiding', p_adjust = 'bonferroni')

p_FR_NR = pTabel['Fiscaal Recht']['Notarieel Recht']
p_FR_PM = pTabel['Fiscaal Recht']['Premaster']
p_FR_RG = pTabel['Fiscaal Recht']['Rechtsgeleerdheid']
p_NR_PM = pTabel['Notarieel Recht']['Premaster']
p_NR_RG = pTabel['Notarieel Recht']['Rechtsgeleerdheid']
p_PM_RG = pTabel['Premaster']['Rechtsgeleerdheid']


# <!-- ## /CLOSEDBLOK: Mann-Whitney-U-test1.py -->
# 
# <!-- ## TEKSTBLOK: link4.py -->
# De [Mann-Whitney U toets](08-Mann-Whitney-U-toets-I-Python.html) gebruikt het gemiddelde rangnummer van twee ongepaarde groepen om de significantie van de toets te bepalen. Met behulp van het gemiddelde rangnummer kan bepaald worden welke groep hogere rangnummers heeft wat een benadering is voor het verschil tussen twee verdelingen.[^15] In deze casus heeft de vooropleiding met een hoger rangnummer dus over het algemeen studenten met een hoger aantal studiepunten. Bereken en rapporteer daarom het gemiddelde rangnummer.
# <!-- ## /TEKSTBLOK: link4.py -->
# 
# <!-- ## OPENBLOK: Mann-Whitney-U-test2.py -->

# In[ ]:


def Gemiddelde_rangschikking(Vooropleiding_1, Vooropleiding_2):
  # Bind alle observaties in een variabele
  Aantal_studiepunten = np.concatenate((np.array(Vooropleiding_1), np.array(Vooropleiding_2)))
  
  # Maak een variabele die aangeeft in welke groep de observatie zit
  Groepsindicator = np.concatenate([[1]*len(Vooropleiding_1),[2]*len(Vooropleiding_2)])

  # Bereken de rangschikkingen van alle observaties
  Rangschikkingen = sp.rankdata(Aantal_studiepunten)

  # Bereken de gemiddelde rangschikking voor beide vooropleidingen
  Gemiddelde_rangschikking_Vooropleiding_1 = np.mean(Rangschikkingen[Groepsindicator == 1])
  Gemiddelde_rangschikking_Vooropleiding_2 = np.mean(Rangschikkingen[Groepsindicator == 2])
  # Print resultaten
  return [Gemiddelde_rangschikking_Vooropleiding_1, Gemiddelde_rangschikking_Vooropleiding_2];

# Definieer variabelen die observaties bevatten voor de verschillende vooropleidingen
Studiepunten_Fiscaal_Recht = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Fiscaal Recht"]["EC_Jaar1"]
Studiepunten_Notarieel_Recht = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Notarieel Recht"]["EC_Jaar1"]
Studiepunten_Premaster = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Premaster"]["EC_Jaar1"]
Studiepunten_Rechtsgeleerdheid = dfResultaten_Arbeidsrecht[dfResultaten_Arbeidsrecht['Vooropleiding'] == "Rechtsgeleerdheid"]["EC_Jaar1"]


# Bereken de gemiddelde rangschikkingen voor elke vergelijking
Gem_FR_NR_1, Gem_FR_NR_2 = Gemiddelde_rangschikking(Studiepunten_Fiscaal_Recht, Studiepunten_Notarieel_Recht)

Gem_FR_PM_1, Gem_FR_PM_2 = Gemiddelde_rangschikking(Studiepunten_Fiscaal_Recht, Studiepunten_Premaster)

Gem_FR_RG_1, Gem_FR_RG_2 = Gemiddelde_rangschikking(Studiepunten_Fiscaal_Recht, Studiepunten_Rechtsgeleerdheid)

Gem_NR_PM_1, Gem_NR_PM_2 = Gemiddelde_rangschikking(Studiepunten_Notarieel_Recht, Studiepunten_Premaster)

Gem_NR_RG_1, Gem_NR_RG_2 = Gemiddelde_rangschikking(Studiepunten_Notarieel_Recht, Studiepunten_Rechtsgeleerdheid)

Gem_PM_RG_1, Gem_PM_RG_2 = Gemiddelde_rangschikking(Studiepunten_Premaster, Studiepunten_Rechtsgeleerdheid)


# <!-- ## /OPENBLOK: Mann-Whitney-U-test2.py -->
# 
# <!-- ## TEKSTBLOK: Mann-Whitney-U-test3.py -->
# | Vergelijking | p-waarde     | Gemiddelde rangschikking (links)  | Gemiddelde rangschikking (rechts)     |
# | -------------  | ----------  | ---------- | -------- |
# | FR vs. NR    | 1,00 `r #Round_and_format(abs(py$p_FR_NR))` |  `r Round_and_format(py$Gem_FR_NR_1)` | `r Round_and_format(py$Gem_FR_NR_2)` |
# | FR vs. PM    | 0,10 `r #Round_and_format(abs(py$p_FR_PM))` |  `r Round_and_format(py$Gem_FR_PM_1)` | `r Round_and_format(py$Gem_FR_PM_2)` |
# | FR vs. RG    | < 0,0001 `r #Round_and_format(abs(py$p_FR_RG))` |  `r Round_and_format(py$Gem_FR_RG_1)` | `r Round_and_format(py$Gem_FR_RG_2)` |
# | NR vs. PM    | 0,02 `r #Round_and_format(abs(py$p_NR_PM))` |  `r Round_and_format(py$Gem_NR_PM_1)` | `r Round_and_format(py$Gem_NR_PM_2)` |
# | NR vs. RG    | < 0,0001 `r #Round_and_format(abs(py$p_NR_RG))` |  `r Round_and_format(py$Gem_NR_RG_1)` | `r Round_and_format(py$Gem_NR_RG_2)` |
# | PM vs. RG    | 0,03 `r #Round_and_format(abs(py$p_PM_RG))` |  `r Round_and_format(py$Gem_PM_RG_1)` | `r Round_and_format(py$Gem_PM_RG_2)` |
# *Tabel 1. Resultaten post-hoc toetsen voor vergelijking Fiscaal Recht (FR), Notarieel Recht (NR), Premaster (PM) en Rechtsgeleerdheid (RG).*
# 
# Als voorbeeld wordt de bovenste rij van Tabel 1 in woorden uitgelegd. Er is geen  significant verschil gevonden tussen Fiscaal (Gemiddelde rangschikking = `r Round_and_format(py$Gem_FR_NR_1)`,  *n*=`r py$vN_FIS`) Recht en Notarieel Recht (Gemiddelde rangschikking = `r Round_and_format(py$Gem_FR_NR_2)`,  *n*=`r py$vN_NOT`), *p*=1,00.
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-test3.py -->

# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# De *Kruskal Wallis toets* is uitgevoerd om te toetsen of er verschillen zijn tussen de studenten van de Master Arbeidsrecht met als vooropleiding Bachelor Fiscaal Recht, Notarieel Recht of Rechtsgeleerdheid of de Premaster wat betreft de verdeling van het aantal studiepunten dat de studenten in het eerste jaar behalen. Uit de resultaten kan afgelezen worden dat er een significant verschil is tussen de verdelingen van het aantal studiepunten voor de verschillende vooropleidingen, *H* = `r Round_and_format(py$stat)`, *df* = `r py$df`, *p* < 0,0001, *&eta;^2^* = `r Round_and_format(py$Eta_squared)`. De resultaten ondersteunen de conclusie dat er een verschil is tussen studenten van de vier verschillende vooropleidingen wat betreft de verdeling van de hoeveelheid studiepunten die studenten behalen tijdens het eerste jaar van de master Arbeidsrecht.  
# 
# De [Mann-Whitney U toets](08-Mann-Whitney-U-toets-Python.html) is uitgevoerd als post-hoc toets om te onderzoeken welke vooropleidingen van elkaar verschillen qua aantal studiepunten dat studenten behalen.  De studenten met Rechtsgeleerdheid als vooropleiding behalen significant minder punten bij de Master Arbeidsrecht, dan de studenten met een andere vooropleiding. Er is ook een significant verschil gevonden tussen de behaalde studiepunten van studenten met de vooropleiding Notarieel Recht en de Premaster, waarbij de studenten van de Premaster minder punten behaalden dan de studenten van Notarieel Recht. Er zijn geen significante verschillen gevonden tussen de vooropleidingen Fiscaal Recht en Notarieel Recht, en Fiscaal Recht en Premaster. De *Bonferroni correctie* is gebruikt om de Type I fout te voorkomen die gepaard gaat met het veelvuldig toetsen. De gemiddelde rangschikkingen en p-waarden van de post-hoc toetsen zijn te vinden in Tabel 1. 
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: De toets rangschikt de datapunten van laag naar hoog en geeft elke datapunt een rangnummer. Vervolgens wordt per groep het gemiddelde berekend van de rangnummers. Deze gemiddelden wordt met elkaar vergeleken. Voor meer informatie lees: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^2]: Van Geloven, N. (21 maart 2018). *Kruskal Wallis*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Kruskal_Wallis). 
# [^3]: Universiteit van Amsterdam (7 juli 2014). *Kruskal-Wallis Test*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Kruskal-Wallis_Test). 
# [^4]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.
# [^5]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^6]: Van Geloven, N. (21 November 2017). *KEUZE TOETS*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/KEUZE_TOETS).
# [^9]: Universiteit van Amsterdam (7 juli 2014). *Kruskal-Wallis Test*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Kruskal-Wallis_Test).
# [^10]: De effectmaat *&eta;^2^* wordt voor de *Kruskal-Wallis toets* berekend door de *&chi;^2^*-waarde te delen door het totaal aantal observaties minus één, i.e. $\frac{\chi^2}{N-1} $.
# [^11]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^13]: De test-statistiek *H* volgt bij benadering de chi-kwadraat verdeling. Onder deze hypothese is *H* chi-kwadraat, vandaar dat dit in de output uitgedrukt wordt in chi-kwadraat.
# [^14]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met Type I en Type II fouten. 
# [^15]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^16]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^17]:  Laerd statistics (2018). *Kruskal-Wallis H Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/kruskal-wallis-h-test-using-spss-statistics.php.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^19]: Bij de *Kruskal Wallis toets* en andere nonparametrische toetsen wordt de data eerst gerangschikt zodat elke observatie een rangnummer toegewezen krijgt. Deze rangnummers worden vervolgens gebruikt om de toets uit te voeren.
# 
