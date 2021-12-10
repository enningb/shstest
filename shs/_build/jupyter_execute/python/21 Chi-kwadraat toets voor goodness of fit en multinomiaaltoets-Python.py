#!/usr/bin/env python
# coding: utf-8
---
title: "Chi-kwadraat toets voor goodness of fit en multinomiaaltoets"
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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/21.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# 
# <!-- ## TEKSTBLOK: Link1.py -->
# Gebruik de *Chi-kwadraat toets voor goodness of fit* om te onderzoeken of de geobserveerde frequenties van de categorieën van één categorische variabele met meer dan twee categorieën overeenkomt met de verwachte frequenties van de categorische variabele.[^6]<sup>,</sup>[^7] Met deze toets kunnen geobserveerde percentages met bekende of verwachte percentages vergeleken worden. Gebruik de exacte *multinomiaaltoets* bij een laag aantal observaties, dit wordt bij de assumpties toegelicht.[^1] De *Chi-kwadraat toets voor goodness of fit* kan ook gebruikt worden voor een categorische variabele met twee categorieën. Voor de exacte *multinomiaaltoets* geldt dit ook, maar in dat geval is de toets gelijk aan de exacte *binomiaaltoets* die te vinden is in bijbehorende [toetspagina](11-Chi-kwadraat-toets-voor-goodness-of-fit-en-binomiaaltoets-Python.html). De *Chi-kwadraat toets voor goodness of fit* en de exacte *multinomiaaltoets* zijn voor zowel nominale[^9] als ordinale[^8] variabelen te gebruiken.
# <!-- ## /TEKSTBLOK: Link1.py -->
# 
# # Onderwijscasus
# <div id = "casus">
# 
# De opleidingsdirecteur van de bacheloropleiding Maritieme Techniek van een universiteit is geïnteresseerd in de resultaten van het Bindend Studie Advies (BSA) van de studenten die deze opleiding volgen. Zij is met name geïnteresseerd in de mate waarin de resultaten van het BSA overeenkomen met de resultaten van de universiteit. Bij deze universiteit ontvangt 70% van de studenten een positief BSA, 20% een negatief BSA en 10% een uitgesteld BSA aan het einde van het eerste jaar. Als blijkt dat de resultaten van het BSA voor de opleiding Maritieme Techniek afwijken van de resultaten van de gehele universiteit, dan kan dit een signaal voor de opleidingsdirecteur zijn om het eerste jaar van de opleiding anders in te richten.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# H~0~: De verdeling van het BSA van de studenten Maritieme Techniek is gelijk aan de verdeling van de gehele universiteit (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA). 
# 
# H~A~: De verdeling van het BSA van de studenten Maritieme Techniek is niet gelijk aan de verdeling van de gehele universiteit (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA).
# 
# </div>
# 
# # Assumpties
# 
# Om de *Chi-kwadraat toets voor goodness of fit* en de exacte *multinomiaaltoets*uit te voeren, moet de variabele nominaal[^9] of ordinaal[^8] zijn.[^6] In deze casus is de categorische variabele nominaal, bij een ordinale categorische variabele worden de toetsen op dezelfde manier uitgevoerd. 
# 
# De categorieën van de variabele mogen niet overlappen, wat wil zeggen dat elke observatie slechts in een van de categorieën past. Voor de *Chi-kwadraat toets voor goodness of fit* mag in niet meer dan 20% van de categorieën van de variabele de verwachte frequentie minder dan vijf zijn. Als dit wel het geval is, gebruik dan de *multinomiaaltoets*.[^7]
# 
# # Post-hoc toetsen
# 
# De *Chi-kwadraat toets voor goodness of fit* en de exacte *multinomiaaltoets* worden gebruikt om te onderzoeken of de verdeling van een categorische variabele met meer dan twee categorieën overeenkomt met een verwachte verdeling. Als de verdelingen niet overeenkomen, is de volgende stap om te bepalen voor welke specifieke categorieën er een verschil is. Met behulp van post-hoc toetsen wordt vervolgens bepaald in welke categorieën de verschillen te vinden zijn.
# 
# Als post-hoc toets voor de *Chi-kwadraat toets voor goodness of fit* wordt het gestandaardiseerde residu gebruikt. Dit is het gestandaardiseerde verschil tussen het (geobserveerde) aantal observaties en het verwachte aantal observaties, waarbij gestandaardiseerd betekent dat het een gemiddelde van 0 en standaardafwijking van 1 heeft. Op deze manier kunnen de verschillende residuen met elkaar vergeleken worden, omdat ze dezelfde schaal hebben. Voor elke cel in de kruistabel kan het gestandaardiseerde residu bepaald worden. Vergelijkbaar met z-scores[^11] zijn deze residuen significant bij een waarde groter dan ± 1,96 wanneer een significantieniveau (α) van 0,05 wordt gehanteerd. Op deze manier kan bepaald worden in welke cellen er afwijkingen van de verwachte frequenties zijn.[^12]
# 
# Voor de *multinomiaaltoets* zijn er geen voorgeschreven post-hoc toetsen. Vergelijk hiervoor de geobserveerde percentages met de percentages die verwacht worden om te onderzoeken in welke categorieën er afwijkingen zijn tussen het geobserveerde en verwachte percentage.
# 
# # De data bekijken
# 
# <!-- ## TEKSTBLOK: Data-bekijken1.py -->
# Er is een dataset ingeladen genaamd `dfBSA_Maritieme_techniek`. Dit is een dataframe met studentnummers en een nominale variabele die laat zien wat voor BSA de student heeft ontvangen.
# <!-- ## /TEKSTBLOK: Data-bekijken1.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.py -->

# In[ ]:


## Importeer nuttige packages
import numpy as np
import pandas as pd
import scipy.stats as sps


# In[ ]:


dfBSA_Maritieme_techniek = pd.DataFrame(r.BSA_Maritieme_techniek)
dfBSA_Maritieme_techniek_steekproef = pd.DataFrame(r.BSA_Maritieme_techniek_steekproef)


# In[ ]:


## Eerste 5 observaties
print(dfBSA_Maritieme_techniek.head(5))


# In[ ]:


## Laatste 5 observaties
print(dfBSA_Maritieme_techniek.tail(5))


# <!-- ## /OPENBLOK: Data-bekijken2.py -->
# 
# Het is informatief om de frequenties en de percentages van de drie mogelijkheden van het BSA te bepalen voor de studenten Maritieme Techniek.
# 
# <!-- ## OPENBLOK: Data-bekijken3.py -->

# In[ ]:


## Bepaal de frequenties
pd.crosstab(dfBSA_Maritieme_techniek['BSA_advies'], columns = 'Frequentie')


# In[ ]:


## Bepaal de percentages
100 * pd.crosstab(dfBSA_Maritieme_techniek['BSA_advies'], columns = 'Percentage', normalize = 'columns')


# In[ ]:


Tab = pd.crosstab(dfBSA_Maritieme_techniek['BSA_advies'], columns = 'Frequentie')

Proptab = 100 * pd.crosstab(dfBSA_Maritieme_techniek['BSA_advies'], columns = 'Percentage', normalize = 'columns')


# <!-- ## /OPENBLOK: Data-bekijken3.py -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken4.py -->
# Het aantal studenten met een positief BSA is `r Round_and_format(py$Tab[2, 1])` (`r Round_and_format(py$Proptab[2, 1])`%), met een negatief BSA is `r Round_and_format(py$Tab[1, 1])` (`r Round_and_format(py$Proptab[1, 1])`%) en met een uitgesteld BSA is `r Round_and_format(py$Tab[3, 1])` (`r Round_and_format(py$Proptab[3, 1])`%). Het lijkt erop dat het percentage studenten met een positief BSA lager is dan het percentage van de gehele universiteit (70%) en dat het percentage studenten met een negatief BSA juist hoger is dan dat van de gehele universiteit (20%). De *Chi-kwadraat toets voor goodness of fit* of de *multinomiaaltoets* toetst of dit verschil significant is.
# <!-- ## /TEKSTBLOK: Data-bekijken4.py -->
# 
# # Chi-kwadraat toets voor goodness of fit
# 
# ## Asssumptie verwachte frequenties
# 
# <!-- ## TEKSTBLOK: Assumptie.py -->
# De verwachte frequentie mag niet kleiner dan vijf zijn in 20% van de categorieën van de categorische variabele. Aangezien er een variabele met drie categorieën getoetst wordt, mag geen van de drie categorieën dus minder dan vijf als verwachte frequentie hebben. Bereken de verwachte frequentie door de verwachte proporties te vermenigvuldigen met het aantal observaties in de dataset. Sla eerst de verwachte proporties op met `np.array([0.7,0.2, 0.1])` van het package `numpy` en vermenigvuldig deze met het totaal aantal observaties `len(dfBSA_Maritieme_techniek)`.
# <!-- ## /TEKSTBLOK: Assumptie.py -->
# 
# <!-- ## OPENBLOK: Assumptie1.py -->

# In[ ]:


# Sla de verwachte proporties op in een vector
Verwachte_proporties = np.array([0.7,0.2, 0.1])

# Bereken het verwachte aantal observaties door de verwachte proporties met het totaal aantal observaties te vermenigvuldigen
Verwacht_aantal_observaties = Verwachte_proporties * len(dfBSA_Maritieme_techniek)

# Print het verwachte aantal observaties
print(Verwacht_aantal_observaties)


# <!-- ## /OPENBLOK: Assumptie1.py -->
# 
# Geen van de verwachte frequenties is kleiner dan vijf, dus de *Chi-kwadraat toets voor goodness of fit* kan worden uitgevoerd.
# 
# ## Uitvoering
# 
# Voer de *Chi-kwadraat toets voor goodness of fit*  uit om te onderzoeken of de verdeling van de BSA mogelijkheden van de studenten Maritieme Techniek overeenkomt met de verdeling van de gehele universiteit (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA).
# 
# <!-- ## TEKSTBLOK: Chi-kwadraat1.py -->
# Bereken eerst de aantallen observaties en verwachte aantallen observaties. Gebruik daarna de functie `chisquare()` van het `scipy.stats` package met als argumenten de aantallen observaties `Aantal_observaties`, de verwachte aantallen observaties `Verwacht_aantal_observaties` en `axis = None` om aan te geven dat alle waarden in de twee vorige argumenten van dezelfde dataset afkomstig zijn. Let goed op dat de volgorde van de aantallen observaties en de verwachte aantallen observaties dezelfde volgorde hebben zodat de toets de goede vergelijking maakt.
# <!-- ## /TEKSTBLOK: Chi-kwadraat1.py -->

# <!-- ## OPENBLOK: Chi-kwadraat2.py-->

# In[ ]:


## Bereken de aantallen observaties
Aantal_observaties = pd.crosstab(dfBSA_Maritieme_techniek['BSA_advies'], columns = 'Frequentie')

## Zet het aantal observaties om in een numpy array. Gebruik de toevoeging .T om de array om te zetten in een rij
Aantal_observaties = np.array(Aantal_observaties).T

## Sla de verwachte proporties op in een vector
Verwachte_proporties = np.array([0.2,0.7, 0.1])

## Bereken het verwachte aantal observaties door de verwachte proporties met het totaal aantal observaties te vermenigvuldigen
Verwacht_aantal_observaties = Verwachte_proporties * len(dfBSA_Maritieme_techniek)

## Voer de chi-kwadraat toets voor goodness of fit uit
sps.chisquare(Aantal_observaties, Verwacht_aantal_observaties, axis = None)


# <!-- ## /OPENBLOK: Chi-kwadraat2.py-->
# 
# <!-- ## CLOSEDBLOK: Chi-kwadraat3.py-->

# In[ ]:


## Bereken de aantallen observaties
Aantal_observaties = pd.crosstab(dfBSA_Maritieme_techniek['BSA_advies'], columns = 'Frequentie')

## Zet het aantal observaties om in een numpy array. Gebruik de toevoeging .T om de array om te zetten in een rij
Aantal_observaties = np.array(Aantal_observaties).T

## Sla de verwachte proporties op in een vector
Verwachte_proporties = np.array([0.2,0.7, 0.1])

## Bereken het verwachte aantal observaties door de verwachte proporties met het totaal aantal observaties te vermenigvuldigen
Verwacht_aantal_observaties = Verwachte_proporties * len(dfBSA_Maritieme_techniek)

## Voer de chi-kwadraat toets voor goodness of fit uit
chi2, pval = sps.chisquare(Aantal_observaties, Verwacht_aantal_observaties, axis = None)

vdf = len(Verwacht_aantal_observaties) -1


# <!-- ## /CLOSEDBLOK: Chi-kwadraat3.py-->
# 
# <!-- ## TEKSTBLOK: Chi-kwadraat4.py-->
# * &chi;^2^~`r Round_and_format(py$vdf)`~ = `r Round_and_format(py$chi2)`, *p* < 0,001
# * De p-waarde is kleiner dan 0,05, dus de nulhypothese wordt verworpen.[^5]
# 
# <!-- ## /TEKSTBLOK: Chi-kwadraat4.py-->

# ## Post-hoc toets: gestandaardiseerde residuën
# 
# Voer post-hoc toetsen uit om te bepalen voor welke BSA mogelijkheden er verschillen zijn tussen de verdeling van de studenten Maritieme Techniek en de verdeling van de gehele universiteit. Inspecteer hiervoor de Pearson residuen van de *Chi-kwadraat toets voor onafhankelijkheid* op waarden groter dan 1,96 en kleiner dan -1,96. Let op dat hier nog geen correctie voor meerdere toetsen plaatsvindt.[^10]
# 
# <!-- ## TEKSTBLOK: Chi2-toets post-hoc0.py -->
# Bereken de gestandaardiseerde residuën door het verschil tussen het aantal observaties en verwacht aantal observaties te delen door de wortel van het verwacht aantal observaties, i.e. $\frac{Geobserveerd - Verwacht}{\sqrt(Verwacht)}$.
# <!-- ## /TEKSTBLOK: Chi2-toets post-hoc0.py -->
# 
# <!-- ## OPENBLOK: Chi2-toets post-hoc1.py -->

# In[ ]:


## Bereken de aantallen observaties
Aantal_observaties = pd.crosstab(dfBSA_Maritieme_techniek['BSA_advies'], columns = 'Frequentie')

## Zet het aantal observaties om in een numpy array. Gebruik de toevoeging .T om de array om te zetten in een rij
Aantal_observaties = np.array(Aantal_observaties).T

## Sla de verwachte proporties op in een vector
Verwachte_proporties = np.array([0.2,0.7, 0.1])

## Bereken het verwachte aantal observaties door de verwachte proporties met het totaal aantal observaties te vermenigvuldigen
Verwacht_aantal_observaties = Verwachte_proporties * len(dfBSA_Maritieme_techniek)

## Bereken de gestandaardiseerde residuen
(Aantal_observaties - Verwacht_aantal_observaties)/ np.sqrt(Verwacht_aantal_observaties)


# <!-- ## /OPENBLOK: Chi2-toets post-hoc1.py -->
# 
# <!-- ## CLOSEDBLOK: Chi2-toets post-hoc1_1.py -->

# In[ ]:


## Bereken de aantallen observaties
Aantal_observaties = pd.crosstab(dfBSA_Maritieme_techniek['BSA_advies'], columns = 'Frequentie')

## Zet het aantal observaties om in een numpy array. Gebruik de toevoeging .T om de array om te zetten in een rij
Aantal_observaties = np.array(Aantal_observaties).T

## Sla de verwachte proporties op in een vector
Verwachte_proporties = np.array([0.2,0.7, 0.1])

## Bereken het verwachte aantal observaties door de verwachte proporties met het totaal aantal observaties te vermenigvuldigen
Verwacht_aantal_observaties = Verwachte_proporties * len(dfBSA_Maritieme_techniek)

## Bereken de gestandaardiseerde residuen
PH_res = (Aantal_observaties - Verwacht_aantal_observaties)/ np.sqrt(Verwacht_aantal_observaties)


# <!-- ## /CLOSEDBLOK: Chi2-toets post-hoc1_1.py -->
# 
# De post-hoc toetsing op basis van de gestandaardiseerde residuën kan als volgt geïnterpreteerd worden:
# <!-- ## TEKSTBLOK: Chi2-toets post-hoc2.py-->
# * Significant hoger aantal observaties bij een negatief BSA , *z* = `r Round_and_format(py$PH_res[1,1])`
# * Geen significant lager aantal observaties bij een positief BSA , *z* = `r Round_and_format(py$PH_res[1,2])`
# * Geen significant verschillend aantal observaties bij een uitgesteld BSA , *z* = `r Round_and_format(py$PH_res[1,3])`
# 
# <!-- ## /TEKSTBLOK: Chi2-toets post-hoc2.py-->
# 
# ## Rapportage
# <!-- ## TEKSTBLOK: Chi-kwadraat5.py-->
# De *Chi-kwadraat toets voor goodness of fit* is uitgevoerd om te onderzoeken of de verdeling van het BSA van studenten Maritieme Techniek overeenkomt met de verdeling van de gehele universiteit waar deze opleiding onder valt (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA). De verdeling van het BSA van de instromende studenten Maritieme Techniek is significant verschillend van de verdeling van de gehele universiteit, &chi;^2^~`r Round_and_format(py$vdf)`~ = `r Round_and_format(py$chi2)`, *p* < 0,001. 
# 
# Uit de post-hoc toetsen blijkt dat het aantal studenten met een negatief BSA significant hoger is dan het percentage van de gehele universiteit (`r Round_and_format(py$Proptab[1, 1])`%, *z* = `r Round_and_format(py$PH_res[1,1])`). Het aantal studenten met een positief BSA (`r Round_and_format(py$Proptab[2, 1])`%, *z* = `r Round_and_format(py$PH_res[1,2])`) en een uitgesteld BSA (`r Round_and_format(py$Proptab[3, 1])`%, *z* = `r Round_and_format(py$PH_res[1,3])`) is niet significant verschillend is van het percentage van de gehele universiteit. De resultaten suggereren dat de opleiding Maritieme Technieken qua BSA dus iets afwijkt van de gehele universiteit waarbij het aantal negatieve BSA's hoger is in vergelijking tot de gehele universiteit.
# <!-- ## /TEKSTBLOK: Chi-kwadraat5.py-->

# # Multinomiaaltoets
# 
# ## Uitvoering
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets1.py -->
# Voer de *multinomiaaltoets*  uit te onderzoeken of de verdeling van de BSA mogelijkheden van de studenten Maritieme Techniek overeenkomt met de verdeling van de gehele universiteit (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA). Deze toets is een alternatief voor de *Chi-kwadraat toets voor goodness of fit* bij een laag aantal observaties. Er is een subset `dfBSA_Maritieme_techniek_steekproef` van de dataset `dfBSA_Maritieme_techniek` ingeladen met daarin een lager aantal observaties.
# <!-- ## /TEKSTBLOK: Binomiaaltoets1.py -->
# 
# Het is informatief om de frequenties en de percentages van de drie mogelijkheden van het BSA te bepalen voor de studenten Maritieme Techniek.
# 
# <!-- ## OPENBLOK: Binomiaaltoets3.py -->

# In[ ]:


## Bepaal de frequenties
pd.crosstab(dfBSA_Maritieme_techniek_steekproef['BSA_advies'], columns = 'Frequentie')


# In[ ]:


## Bepaal de percentages
100 * pd.crosstab(dfBSA_Maritieme_techniek_steekproef['BSA_advies'], columns = 'Percentage', normalize = 'columns')


# <!-- ## /OPENBLOK: Binomiaaltoets3.py -->
# 
# <!-- ## CLOSEDBLOK: Binomiaaltoets3_3.py -->

# In[ ]:


Tab2 = pd.crosstab(dfBSA_Maritieme_techniek_steekproef['BSA_advies'], columns = 'Frequentie')

Proptab2 = 100 * pd.crosstab(dfBSA_Maritieme_techniek_steekproef['BSA_advies'], columns = 'Percentage', normalize = 'columns')


# <!-- ## /CLOSEDBLOK: Binomiaaltoets3_3.py -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets4.py -->
# Het aantal studenten met een positief BSA is `r Round_and_format(py$Tab2[2, 1])` (`r Round_and_format(py$Proptab2[2, 1])`%), met een negatief BSA is `r Round_and_format(py$Tab2[1, 1])` (`r Round_and_format(py$Proptab2[1, 1])`%) en met een uitgesteld BSA is `r Round_and_format(py$Tab2[3, 1])` (`r Round_and_format(py$Proptab2[3, 1])`%). Het lijkt erop dat het percentage studenten met een positief BSA lager is dan het percentage van de gehele universiteit (70%) en dat het percentage studenten met een negatief BSA juist hoger is dan dat van de gehele universiteit (20%). De *multinomiaaltoets* toetst of dit verschil significant is.
# <!-- ## /TEKSTBLOK: Binomiaaltoets4.py -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets5.py -->
# Bereken de verwachte frequentie door de verwachte proporties te vermenigvuldigen met het aantal observaties in de dataset. Sla eerst de verwachte proporties op met `np.array([0.7,0.2, 0.1])` van het package `numpy` en vermenigvuldig deze met het totaal aantal observaties `len(dfBSA_Maritieme_techniek_steekproef)`.
# <!-- ## /TEKSTBLOK: Binomiaaltoets5.py -->
# 
# <!-- ## OPENBLOK: Binomiaaltoets6.py -->

# In[ ]:


# Sla de verwachte proporties op in een vector
Verwachte_proporties = np.array([0.7,0.2, 0.1])

# Bereken het verwachte aantal observaties door de verwachte proporties met het totaal aantal observaties te vermenigvuldigen
Verwacht_aantal_observaties = Verwachte_proporties * len(dfBSA_Maritieme_techniek_steekproef)

# Print het verwachte aantal observaties
print(Verwacht_aantal_observaties)


# <!-- ## /OPENBLOK: Binomiaaltoets6.py -->
# 
# <!-- ## CLOSEDBLOK: Binomiaaltoets6_1.py -->
# <!-- ## /CLOSEDBLOK: Binomiaaltoets6_1.py -->
# 
# De verwachte frequentie voor studenten met een uitgesteld BSA is kleiner dan 5. Dit betekent dat er in meer dan 20% van de categorieën een verwachte frequentie van minder dan 5 is en dat er dus niet voldaan is aan de assumptie van verwachte frequenties. Voer daarom de *multinomiaaltoets* uit.
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets7.py -->
# Voor zover bekend is er geen package om de *multinomiaaltoets* uit te voeren in Python. De *multinomiaaltoets* kan in Python alleen uitgevoerd worden voor een nominale variabele met twee categorieën, dan is de *multinomiaaltoets* gelijk aan de *binomiaaltoets*. Deze stap kan dus in deze toetspagina niet weergegeven worden. Bekijk de [toetspagina van de multinomiaaltoets in R](21-Chi-kwadraat-toets-voor-goodness-of-fit-en-multinomiaaltoets-R.html) om deze met de programmeertaal R uit te voeren. Voor het vervolg van deze toetspagina wordt aangenomen dat de *multinomiaaltoets* geen significant resultaat laat zien.
# <!-- ## /TEKSTBLOK: Binomiaaltoets7.py -->
# 
# <!-- ## OPENBLOK: Binomiaaltoets8.py-->
# <!-- ## /OPENBLOK: Binomiaaltoets8.py-->
# 
# <!-- ## CLOSEDBLOK: Binomiaaltoets9.py -->
# <!-- ## /CLOSEDBLOK: Binomiaaltoets9.py -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets10.py-->
# <!-- ## /TEKSTBLOK: Binomiaaltoets10.py-->

# ## Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage2.py-->
# 
# De *multinomiaaltoets* is uitgevoerd om te onderzoeken of de verdeling van het BSA van studenten Maritieme Techniek overeenkomt met de verdeling van de gehele universiteit waar deze opleiding onder valt (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA) voor een dataset met een laag aantal observaties. De verdeling van het BSA van de instromende studenten van de universiteit verschilt niet significant van de landelijke verdeling (*p* > 0,05). Het aantal studenten met een positief BSA is `r Round_and_format(py$Tab2[2, 1])` (`r Round_and_format(py$Proptab2[2, 1])`%), met een negatief BSA is `r Round_and_format(py$Tab2[1, 1])` (`r Round_and_format(py$Proptab2[1, 1])`%) en met een uitgesteld BSA is `r Round_and_format(py$Tab2[3, 1])` (`r Round_and_format(py$Proptab2[3, 1])`%). De resultaten suggereren dat de opleiding Maritieme Technieken qua BSA niet afwijkt van de gehele universiteit.
# 
# <!-- ## /TEKSTBLOK: Rapportage2.py-->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Agresti, A. (2003). *Categorical data analysis*. Vol. 482, John Wiley & Sons.
# [^4]: Een proportie van een bepaalde categorie is de frequentie van de categorie gedeeld door het totaal aantal observaties. Het kan gezien worden als de kans van een bepaalde categorie en bevat een waarde tussen 0 en 1.
# [^5]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^6]: Laerd Statistics (2018). *Chi-Square Goodness-of-Fit Test in SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/chi-square-goodness-of-fit-test-in-spss-statistics.php
# [^7]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^8]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^9]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# [^10]: De waarde 1,96 is een z-score en correspondeert met het significantieniveau 0,05 voor een tweezijdige toets. Om te corrigeren voor meerdere testen kan een ander significantieniveau gekozen worden wat resulteert in een andere z-score om mee te vergelijken. Bij een significantieniveau van 0,01 is de z-score bijvoorbeeld 2,58. De z-score per significantieniveau is te berekenen met `abs(qnorm(alfa/2))` waarbij `alfa` het gewenste significantieniveau is.
# [^11]: Een z-score is een maat om aan te geven hoeveel een observatie afwijkt van het gemiddelde. De z-score wordt berekend door het gemiddelde van de observatie af te halen en dit daarna te delen door de standaarddeviatie, i.e. $\frac{X - \mu}{\sigma}$. In feite geeft een z-score aan hoeveel standaarddeviaties de observatie van het gemiddelde afwijkt.
# [^12]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# 
# <!-- ## TEKSTBLOK: Extra-Bron.py -->
# 
# <!-- ## /TEKSTBLOK: Extra-Bron.py -->
# 
