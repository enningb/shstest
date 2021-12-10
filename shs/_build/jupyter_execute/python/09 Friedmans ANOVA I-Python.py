#!/usr/bin/env python
# coding: utf-8
---
title: "Friedman's ANOVA"
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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/09.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# 
# <!-- ## /TEKSTBLOK: Link1.py -->
# Gebruik *Friedman's ANOVA* om de gemiddelde rangnummers[^13] te vergelijken voor de verdelingen van drie of meer herhaalde metingen van één groep of voor de verdelingen van drie of meer gepaarde groepen.[^1]<sup>, </sup>[^2] *Friedman's ANOVA* is een alternatief voor de [repeated measures ANOVA](04-Repeated-measures-ANOVA-Python.html) wanneer de data niet aan de assumptie van normaliteit voldoet. Daarnaast hebben uitbijters minder invloed op het resultaat van *Friedman's ANOVA* in vergelijking tot de [repeated measures ANOVA](04-Repeated-measures-ANOVA-Python.html). Echter, als de data aan de assumpties van de [repeated measures ANOVA](04-Repeated-measures-ANOVA-Python.html) voldoet, heeft die toets een hoger onderscheidend vermogen dan *Friedman's ANOVA*.[^3]
# <!-- ## /TEKSTBLOK: Link1.py -->

# # Onderwijscasus
# <div id = "casus">
# 
# Uit de Nationale Studenten Enquête (NSE) blijkt dat studenten ontevreden zijn over het horeca-aanbod op de campus van hun hogeschool. De vastgoedmanager van de  Facultaire Dienst (FD) van deze hogeschool is nieuwsgierig hoe de verschillende eetgelegenheden op de campus gewaardeerd worden door studenten om zo te inventarisen op welke manier het horeca-aanbod verbeterd kan worden. Als vervolgonderzoek op de NSE wordt een groep studenten gevraagd om de eetgelegenheden op de campus te beoordelen (met een cijfer tussen 1 en 10). Aan de hand daarvan vergelijkt de vastgoedmanager eetgelegenheden in vier gebouwen: het hoofdgebouw, het bestuursgebouw, het sportcentrum en het cultuurcentrum Rembrandt. Met deze gegevens wil de vastgoedmanager onderzoeken of er verschillen zijn in de waarderingscijfers van de eetgelegenheden in de vier gebouwen. Als deze verschillen aanwezig zijn, is zij benieuwd welke eetgelegenheden van elkaar verschillen.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het gemiddelde rangnummer van de verdelingen van de beoordelingen van studenten is hetzelfde voor de eetgelegenheid in het hoofdgebouw, het bestuursgebouw, het sportcentrum en het cultuurcentrum Rembrandt.
# 
# *H~A~*: Het gemiddelde rangnummer van de verdelingen van de beoordelingen van studenten is niet hetzelfde voor de eetgelegenheid in het hoofdgebouw, het bestuursgebouw, het sportcentrum en het cultuurcentrum Rembrandt.
# 
# </div>
# 
# # Assumpties
# 
# Om een valide toetsresultaat te bereiken, moeten de data aan een aantal assumpties voldoen. Het meetniveau van de afhankelijke variabele is ordinaal[^14] of continu.[^4] In deze toetspagina staat een casus met continue data centraal; een casus met ordinale data met bijbehorende uitwerking is te vinden in [deze toetspagina](24-Friedmans-ANOVA-II-R.html). Bij herhaalde metingen van dezelfde observatie-eenheden, moet de groep observatie-eenheden drie of meer keren gemeten zijn en een willekeurige steekproef van de populatie zijn. Bij gepaarde groepen, moet elk paar bestaan uit drie of meer gepaarde observatie-eenheden en moet de steekproef met alle paren een willekeurige steekproef van de populatie zijn.[^4]

# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^5] Voor *Friedman's ANOVA* wordt de effectmaat *Kendall's W* vaak gebruikt.[^6]<sup>, </sup>[^7]<sup>, </sup>[^8] Een indicatie om *Kendall's W* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^6]

# # Post-hoc toetsen
# 
# <!-- ## TEKSTBLOK: Link2.py -->
# *Friedman's ANOVA* toetst of er verschillen zijn tussen de verdelingen van groepen. Voer een post-hoc toets uit om te bepalen welke groepen van elkaar verschillen. Gebruik de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) als post-hoc toets. De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) toetst of er een verschil tussen de verdelingen is van twee gepaarde groepen (i.e. of een van beide verdelingen hogere waardes heeft dan de andere verdeling). Hoewel het minder gebruikelijk is, is de [tekentoets](27-Tekentoets-II-R.html) ook een optie als post-hoc toets. Deze toets toetst het verschil tussen de medianen van twee gepaarde groepen.
# <!-- ## /TEKSTBLOK: Link2.py -->
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout. Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^5]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.py-->
# Er is een dataset `dfBeoordelingen_eetgelegenheden` ingeladen met de beoordelingen van de eetgelegenheden in het hoofdgebouw, bestuursgebouw, sportcentrum en cultuurcentrum.
# <!-- ## /TEKSTBLOK: Dataset-inladen.py-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


import pandas as pd
dfBeoordelingen_eetgelegenheden = pd.DataFrame(r.Beoordelingen_eetgelegenheden)


# In[ ]:


import pandas as pd
## Eerste 6 observaties
print(dfBeoordelingen_eetgelegenheden.head(6))


# In[ ]:


## Laatste 6 observaties
print(dfBeoordelingen_eetgelegenheden.tail(6))


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken2.py-->
# De dataset bevat beoordelingen van studenten van eetgelegenheden in verschillende gebouwen. Gebruik `<data.frame>.<kolomnaam>.unique()` om te onderzoeken welke gebouwen er in de data aanwezig zijn. 
# <!-- ## /TEKSTBLOK: Data-bekijken2.py-->
# 
# <!-- ## OPENBLOK: Data-bekijken-2.py -->

# In[ ]:


## Unieke opleidingen
print(dfBeoordelingen_eetgelegenheden['Eetgelegenheid'].unique())


# <!-- ## /OPENBLOK: Data-bekijken-2.py -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken3.py-->
# Inspecteer om meer inzicht te krijgen in de data de groepen met `.size()` en `.quantile()`. Selecteer eerst de juiste variabelen met `dfBeoordelingen_eetgelegenheden[['Beoordeling','Eetgelegenheid']]`en groepeer daarna voor de eetgelegenheden met .groupby(['Eetgelegenheid']). De mediaan is gelijk aan kwantiel `0.5`.
# <!-- ## /TEKSTBLOK: Data-bekijken3.py-->
# 
# <!-- ## OPENBLOK: Data-beschrijven.py -->

# In[ ]:


print(dfBeoordelingen_eetgelegenheden[['Beoordeling','Eetgelegenheid']].groupby(['Eetgelegenheid']).size())


# In[ ]:


print(dfBeoordelingen_eetgelegenheden[['Beoordeling','Eetgelegenheid']].groupby(['Eetgelegenheid']).quantile([0.25, 0.5, 0.75]))


# <!-- ## /OPENBLOK: Data-beschrijven.py -->
# <!-- ## CLOSEDBLOK: Data-beschrijven.py -->
# ``` {python data beschrijven als object, include=FALSE, echo=TRUE}
# 
# import numpy as np
# dfHG = np.array(dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Hoofdgebouw"]['Beoordeling'])
# dfBG = np.array(dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Bestuursgebouw"]['Beoordeling'])
# dfSC = np.array(dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Sportcentrum"]['Beoordeling'])
# dfCC = np.array(dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Cultuurcentrum"]['Beoordeling'])
# 
# vN_HG = len(dfHG)
# vN_BG = len(dfBG)
# vN_SC = len(dfSC)
# vN_CC = len(dfCC)
# 
# vQ1_HG = np.quantile(dfHG, 0.25)
# vQ1_BG = np.quantile(dfBG, 0.25)
# vQ1_SC = np.quantile(dfSC, 0.25)
# vQ1_CC = np.quantile(dfCC, 0.25)
# 
# vMed_HG = np.quantile(dfHG, 0.5)
# vMed_BG = np.quantile(dfBG, 0.5)
# vMed_SC = np.quantile(dfSC, 0.5)
# vMed_CC = np.quantile(dfCC, 0.5)
# 
# vQ3_HG = np.quantile(dfHG, 0.75)
# vQ3_BG = np.quantile(dfBG, 0.75)
# vQ3_SC = np.quantile(dfSC, 0.75)
# vQ3_CC = np.quantile(dfCC, 0.75)
# 
# 
# ```
# <!-- ## /CLOSEDBLOK: Data-beschrijven.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# * Hoofdgebouw: *Mdn* =  `r Round_and_format(py$vMed_HG)`, *Q1* = `r Round_and_format(py$vQ1_HG)`, *Q3* = `r Round_and_format(py$vQ3_HG)`, *n* = `r Round_and_format(py$vN_HG)`.
# * Bestuursgebouw: *Mdn* =  `r Round_and_format(py$vMed_BG)`, *Q1* = `r Round_and_format(py$vQ1_BG)`, *Q3* = `r Round_and_format(py$vQ3_BG)`, *n* = `r Round_and_format(py$vN_BG)`.
# * Sportcentrum: *Mdn* =  `r Round_and_format(py$vMed_SC)`, *Q1* = `r Round_and_format(py$vQ1_SC)`, *Q3* = `r Round_and_format(py$vQ3_SC)`, *n* = `r Round_and_format(py$vN_SC)`.
# * Cultuurcentrum: *Mdn* =  `r Round_and_format(py$vMed_CC)`, *Q1* = `r Round_and_format(py$vQ1_CC)`, *Q3* = `r Round_and_format(py$vQ3_CC)`, *n* = `r Round_and_format(py$vN_CC)`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# 

# ## Histogram
# 
# Geef de verdeling van de beoordelingen per gebouw visueel weer met een histogram[^18].[^12]
# 
# <!-- ## OPENBLOK: Histogram.py -->

# In[ ]:


# Laad seaborn of facets te maken
import seaborn as sb
# Laad matplotlib.pyplot om plots te maken
import matplotlib.pyplot as plt

# Maak een facet plot met een histogram voor elke vooropleiding
g = sb.FacetGrid(dfBeoordelingen_eetgelegenheden, col="Eetgelegenheid")
g = (g.map(plt.hist, "Beoordeling", edgecolor = "black").set_axis_labels("Beoordeling"))
plt.show()


# <!-- ## /OPENBLOK: Histogram.py -->
# 
# Bij alle vier de gebouwen lijken er afwijkingen te zijn van de (symmetrische) normale verdeling. De verdeling van het bestuursgebouw heeft een langere staart aan de rechterkant, terwijl de verdelingen van het hoofdgebouw en het sportcentrum juist een langere staart aan de linkerkant hebben. Bij het cultuurcentrum zijn er meer observaties links van het midden dan rechts van het midden, waardoor er ook een vorm van asymmetrie is. Daarom is het een goede optie om *Friedman's ANOVA* uit te voeren, omdat deze toets niet aan de assumptie van normaliteit hoeft te voldoen.
# 

# ## Friedman's ANOVA
# 
# <!-- ## TEKSTBLOK: ANOVA-toets.py -->
# Voer *Friedman's ANOVA* uit om de vraag te beantwoorden of er verschillen zijn tussen de (gemiddelde rangnummers van de) beoordelingen van de eetgelegenheden in de vier gebouwen op de campus van de hogeschool. Gebruik de functie `friedmanchisquare()` van het package `scipy` met als argumenten de vier variabelen met de beoordelingen voor elk van de vier gebouwen. Bij deze functie toetst Python standaard tweezijdig.
# <!-- ## /TEKSTBLOK: ANOVA-toets.py -->
# 
# <!-- ## OPENBLOK: ANOVA-toets.py -->

# In[ ]:


import numpy as np

# Maak een variabele met het aantal studiepunten voor elke vooropleiding
dfHG = np.array(dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Hoofdgebouw"]['Beoordeling'])
dfBG = np.array(dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Bestuursgebouw"]['Beoordeling'])
dfSC = np.array(dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Sportcentrum"]['Beoordeling'])
dfCC = np.array(dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Cultuurcentrum"]['Beoordeling'])

# Voer de Kruskal Wallis toets uit
import scipy.stats as sp
print(sp.friedmanchisquare(dfHG, dfBG, dfSC, dfCC))


# <!-- ## /OPENBLOK: ANOVA-toets.py -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets.py -->
# 
# <!-- ## /CLOSEDBLOK: ANOVA-toets.py -->
# 
# Bereken vervolgens de effectmaat *Kendall's W* op basis van de *&chi;^2^* waarde van *Friedman's ANOVA*.
# <!-- ## OPENBLOK: ANOVA-toets2.py -->

# In[ ]:


# Sla de Chi-kwadraat waarde op
Chi2, pval = sp.friedmanchisquare(dfHG, dfBG, dfSC, dfCC)

# Sla het aantal observatie-eenheden op
N = len(dfBeoordelingen_eetgelegenheden['Studentnummer'].unique())  

# Sla het aantal groepen op
k = len(dfBeoordelingen_eetgelegenheden['Eetgelegenheid'].unique())


# Bereken de effectmaat
W = Chi2 / (N * (k - 1))

# Print de effectmaat
print(W)


# <!-- ## /OPENBLOK: ANOVA-toets2.py -->

# <!-- ## TEKSTBLOK: ANOVA-toets1.py -->
# * *&chi;^2^~3~* = `r Round_and_format(py$Chi2)`, *p* = 0,006, *W* = `r Round_and_format(py$W)`
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^10]
# * Er is een significant verschil tussen de beoordelingen van de eetgelegenheden in de vier gebouwen; het effect van de verschillende gebouwen op de beoordelingen van studenten is klein tot gemiddeld
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets1.py -->
# 
# ## Post-hoc toets
# <!-- ## TEKSTBLOK: posthoc1.py -->
# Voer post-hoc toetsen uit om te onderzoeken tussen welke gebouwen er verschillen zijn in de beoordelingen van studenten. De vier gebouwen zijn het hoofdgebouw, bestuursgebouw, sportcentrum en cultuurcentrum Rembrandt. Gebruik de [Wilcoxon signed-rank toets](07-Wilcoxon-signed-rank-toets-Python.html) als post-hoc toets met bijbehorende functie `posthoc_wilcoxon()` van het package `scikit_posthocs`. De ingevoerde argumenten van de functie zijn 
# de dataset `dfBeoordelingen_eetgelegenheden`, de afhankelijke variabele `val_col = 'Beoordeling'`, de onafhankelijke variabele `group_col = 'Eetgelegenheid'` en de correctie voor meerdere toetsen `p_adjust = 'bonferroni'`. Het significantieniveau is 0,05.[^10]
# <!-- ## /TEKSTBLOK: posthoc1.py -->
# 
# <!-- ## OPENBLOK: post-hoc2.py-->

# In[ ]:


import scikit_posthocs as skph

skph.posthoc_wilcoxon(dfBeoordelingen_eetgelegenheden, val_col = 'Beoordeling', group_col = 'Eetgelegenheid', p_adjust = 'bonferroni')


# <!-- ## /OPENBLOK: post-hoc2.py -->
# 
# Bereken de effectmaat *r* voor elke individuele post-hoc toets.[^11]
# 
# <!-- ## OPENBLOK: post-hoc4.py -->
# ``` {python pairwise wilcox test effectmaat}
# # Sla de p-waarden van de post-hoc toetsen op
# pTabel = skph.posthoc_wilcoxon(dfBeoordelingen_eetgelegenheden, val_col = 'Beoordeling', group_col = 'Eetgelegenheid', p_adjust = 'bonferroni')
# print(pTabel)
# p_HG_BG = pTabel['Hoofdgebouw']['Bestuursgebouw']
# p_HG_SC = pTabel['Hoofdgebouw']['Sportcentrum']
# p_HG_CC = pTabel['Hoofdgebouw']['Cultuurcentrum']
# p_BG_SC = pTabel['Bestuursgebouw']['Sportcentrum']
# p_BG_CC = pTabel['Bestuursgebouw']['Cultuurcentrum']
# p_SC_CC = pTabel['Sportcentrum']['Cultuurcentrum']
# 
# # Sla het aantal observatie-eenheden op
# N = len(dfBeoordelingen_eetgelegenheden['Studentnummer'].unique())  
# 
# # Bereken de effectgrootte voor een tweezijdige toets
# Effectmaat_HG_BG = sp.norm.ppf(p_HG_BG/2) / np.sqrt(N)
# Effectmaat_HG_SC = sp.norm.ppf(p_HG_SC/2) / np.sqrt(N)
# Effectmaat_HG_CC = sp.norm.ppf(p_HG_CC/2) / np.sqrt(N)
# Effectmaat_BG_SC = sp.norm.ppf(p_BG_SC/2) / np.sqrt(N)
# Effectmaat_BG_CC = sp.norm.ppf(p_BG_CC/2) / np.sqrt(N)
# Effectmaat_SC_CC = sp.norm.ppf(p_SC_CC/2) / np.sqrt(N)
# ```
# <!-- ## /OPENBLOK: post-hoc4.py -->
# 
# <!-- ## TEKSTBLOK: Link4.py -->
# De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-Python.html) gebruikt de som van positieve en negatieve rangnummers van de verschilscores om de significantie van de toets te bepalen. Deze sommen beschrijven het verschil tussen twee gepaarde groepen waarbij de groep met een hogere som van rangnummers ook hogere waarden op de afhankelijke variabele heeft. In deze casus heeft het gebouw met hogere rangnummers een hogere beoordeling door studenten. Bereken de som van de positieve en negatieve rangnummers voor alle vergelijkingen.
# <!-- ## /TEKSTBLOK: Link4.py -->
# 
# <!-- ## OPENBLOK: post-hoc5.py -->

# In[ ]:


def Sommen_rangnummers(Gebouw_1, Gebouw_2):
  # Bereken verschilscores
  Verschilscores = np.array(Gebouw_1) - np.array(Gebouw_2)

  # Rangschik de absolute waarden van verschilscores met scipy.rankdata()
  Rangnummers = sp.rankdata(np.abs(Verschilscores))

  # Maak een vector met daarin de tekens (plus of min) van verschilscores) met numpy.sign()
  Tekens = np.sign(Verschilscores)

  # Bereken het aantal en de som van de positieve rangnummers
  N_positief = len(Tekens[Tekens == 1])
  Som_positief = np.sum(Rangnummers[Tekens == 1])

  # Bereken het aantal en de som van de negatieve rangnummers
  N_negatief = len(Tekens[Tekens == -1])
  Som_negatief = np.sum(Rangnummers[Tekens == -1])

  # Print resultaten
  return [N_positief, Som_positief, N_negatief, Som_negatief];

# Definieer variabelen die observaties bevatten voor de verschillende gebouwen
Beoordeling_HG = dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Hoofdgebouw"]["Beoordeling"]
Beoordeling_BG = dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Bestuursgebouw"]["Beoordeling"]
Beoordeling_SC = dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Sportcentrum"]["Beoordeling"]
Beoordeling_CC = dfBeoordelingen_eetgelegenheden[dfBeoordelingen_eetgelegenheden['Eetgelegenheid'] == "Cultuurcentrum"]["Beoordeling"]

# Bereken de gemiddelde rangschikkingen voor elke vergelijking
N_HG_BG_positief, Som_HG_BG_positief, N_HG_BG_negatief, Som_HG_BG_negatief = Sommen_rangnummers(Beoordeling_HG, Beoordeling_BG)

print(N_HG_BG_positief, Som_HG_BG_positief, N_HG_BG_negatief, Som_HG_BG_negatief)

N_HG_SC_positief, Som_HG_SC_positief, N_HG_SC_negatief, Som_HG_SC_negatief = Sommen_rangnummers(Beoordeling_HG, Beoordeling_SC)

N_HG_CC_positief, Som_HG_CC_positief, N_HG_CC_negatief, Som_HG_CC_negatief = Sommen_rangnummers(Beoordeling_HG, Beoordeling_CC)

N_BG_SC_positief, Som_BG_SC_positief, N_BG_SC_negatief, Som_BG_SC_negatief = Sommen_rangnummers(Beoordeling_BG, Beoordeling_SC)

N_BG_CC_positief, Som_BG_CC_positief, N_BG_CC_negatief, Som_BG_CC_negatief = Sommen_rangnummers(Beoordeling_BG, Beoordeling_CC)

N_SC_CC_positief, Som_SC_CC_positief, N_SC_CC_negatief, Som_SC_CC_negatief = Sommen_rangnummers(Beoordeling_SC, Beoordeling_CC)


# <!-- ## /OPENBLOK: post-hoc5.py -->
# 
# <!-- ## TEKSTBLOK: posthoc6.py -->
# 
# | Vergelijking | p-waarde     | Effectmaat        |  Som positieve rangnummers        | Som negatieve rangnummers     |
# | -------------  | ----------  | --------- | ---------- | -------- |
# | HG vs. BG    | 0,878`r #Round_and_format(py$p_HG_BG)` | `r Round_and_format(py$Effectmaat_HG_BG)`| `r Round_and_format(py$Som_HG_BG_positief)` | `r Round_and_format(py$Som_HG_BG_negatief)` |
# | HG vs. SC    | 1,000`r #Round_and_format(py$p_HG_SC)` | `r Round_and_format(py$Effectmaat_HG_SC)`| `r Round_and_format(py$Som_HG_SC_positief)` | `r Round_and_format(py$Som_HG_SC_negatief)` |
# | HG vs. CC    | 0,046`r #Round_and_format(py$p_HG_CC)` | `r Round_and_format(py$Effectmaat_HG_CC)`| `r Round_and_format(py$Som_HG_CC_positief)` | `r Round_and_format(py$Som_HG_CC_negatief)` |
# | BG vs. SC    | 0,108`r #Round_and_format(py$p_BG_SC)` | `r Round_and_format(py$Effectmaat_BG_SC)`| `r Round_and_format(py$Som_BG_SC_positief)` | `r Round_and_format(py$Som_BG_SC_negatief)` |
# | BG vs. CC    | 1,000`r #Round_and_format(py$p_BG_CC)` | `r Round_and_format(py$Effectmaat_BG_CC)`| `r Round_and_format(py$Som_BG_CC_positief)` | `r Round_and_format(py$Som_BG_CC_negatief)` |
# | SC vs. CC    | 0,013`r #Round_and_format(py$p_SC_CC)` | `r Round_and_format(py$Effectmaat_SC_CC)`| `r Round_and_format(py$Som_SC_CC_positief)` | `r Round_and_format(py$Som_SC_CC_negatief)` |
# 
# *Tabel 1. Resultaten post-hoc toetsen voor vergelijking hoofdgebouw (HG), bestuursgebouw (BG), sportcentrum (SC) en cultuurcentrum (CC).*
# <!-- ## /TEKSTBLOK: posthoc6.py -->

# <!-- ## TEKSTBLOK: posthoc7.py -->
# De significante verschillen op de post-hoc toetsen zijn:
# 
# * De beoordelingen van het hoofdgebouw (Som = `r Round_and_format(py$Som_HG_CC_positief)`) verschillen significant van het cultuurcentrum (Som = `r Round_and_format(py$Som_HG_CC_negatief)`), *p* = 0,043`r #Round_and_format(posthoc[2,2])`, *r* = `r Round_and_format(py$Effectmaat_HG_CC)`. De hogere som van rangnummers voor het hoofdgebouw duidt erop dat de beoordelingen van het hoofdgebouw beter zijn dan die van het cultuurcentrum.
# 
# * De beoordelingen van het sportcentrum (Som = `r Round_and_format(py$Som_SC_CC_positief)`) verschillen significant van het cultuurcentrum (Som = `r Round_and_format(py$Som_SC_CC_negatief)`), *p* = 0,012 `r #Round_and_format(posthoc[3,2])`, *r* = `r Round_and_format(py$Effectmaat_SC_CC)`. De hogere som van rangnummers voor het sportcentrum duidt erop dat de beoordelingen van het sportcentrum beter zijn dan die van het cultuurcentrum.
# 
# <!-- ## /TEKSTBLOK: posthoc7.py -->
# 

# # Rapportage
# 
# <!-- ## TEKSTBLOK: rapportage.py -->
# *Friedman's ANOVA* is uitgevoerd om te onderzoeken of de beoordeling van eetgelegenheden door studenten verschilt voor vier gebouwen op de campus van een hogeschool. De vier gebouwen zijn het hoofdgebouw, het bestuursgebouw, het sportcentrum en cultuurcentrum Rembrandt; beschrijvende statistieken zijn te vinden in Tabel 1. De beoordelingen van de vier gebouwen verschillen significant van elkaar (*&chi;^2^~3~* = `r Round_and_format(py$Chi2)`, *p* = 0,006, *W* = `r Round_and_format(py$W)`). De sterkte van het effect van de verschillen in gebouwen op de beoordelingen van studenten is klein tot gemiddeld.
# 
# Post-hoc toetsen met een Bonferroni correctie voor meerdere toetsen zijn uitgevoerd voor alle vergelijkingen tussen twee gebouwen. Hieruit blijkt dat er alleen significante verschillen zijn tussen het hoofdgebouw en cultuurcentrum Rembrandt, en tussen het sportcentrum  en cultuurcentrum Rembrandt. De eetgelegenheid van cultuurcentrum Rembrandt wordt slechter beoordeeld dan de eetgelegenheden in het hoofdgebouw en het sportcentrum; verder zijn er geen significante verschillen tussen de beoordelingen van de eetgelegenheden op de campus.
# <!-- ## /TEKSTBLOK: rapportage.py -->
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Van Geloven, N. (4 oktober 2019). *Friedman toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Friedman_toets). 
# [^2]: Universiteit van Amsterdam (7 juli 2014). *Friedmans ANOVA*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Friedmans_ANOVA). 
# [^3]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^4]: Laerd statistics (2018). *Friedman Test in SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/friedman-test-using-spss-statistics.php. 
# [^5]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^6]: University of Sheffield. *Friedman test in SPSS*. [Mathematics and Statistics Help (MASH)](https://www.sheffield.ac.uk/polopoly_fs/1.714575!/file/stcp-marshall-FriedmanS.pdf). Bezocht op 13 maart 2020.
# [^7]: *Kendall's W* wordt berekend door de teststatistiek van *Friedman's ANOVA* (dit is de *&chi;^2^*) te delen door het aantal observatie-eenheden *N* en het aantal groepen *k* minus één, i.e. $W = \frac{\chi^2}{N(k-1)}$.
# [^8]: Kassambara, A. (2020). *rstatix: Pipe-Friendly Framework for Basic Statistical Tests*. [R package version 0.4.0.](https://CRAN.R-project.org/package=rstatix).
# [^10]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^11]: De effectmaat *r* wordt voor de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) berekend door de
# *z*-waarde behorend bij de *p*-waarde van de toets te delen door de wortel van
# het aantal observatie-eenheden, i.e. $\frac{z}{\sqrt{N}}$.
# [^12]: De breedte van de staven van het histogram worden hier automatisch bepaald, maar kunnen handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^13]: Bij *Friedman's ANOVA* en andere nonparametrische toetsen wordt de data eerst gerangschikt zodat elke observatie een rangnummer toegewezen krijgt. Deze rangnummers worden vervolgens gebruikt om de toets uit te voeren.
# [^14]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
