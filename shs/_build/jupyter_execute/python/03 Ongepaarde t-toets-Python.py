#!/usr/bin/env python
# coding: utf-8
---
title: "Ongepaarde t-toets"
output:
  html_document:
    includes:
      in_header:
      - ../01. Includes/html/nocache.html
      - ../01. Includes/html/favicon.html
      - ../01. Includes/html/analytics.html
    number_sections: yes
    theme: lumen
    toc: yes
    toc_depth: 2
    toc_float:
      collapsed: no
  keywords:
  - statistisch handboek
  - studiedata
  word_document:
    toc: yes
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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/03.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# Gebruik de *ongepaarde t-toets* om de gemiddelden van twee onafhankelijke groepen te vergelijken.[^1]
# 
# # Onderwijscasus
# <div id = "casus">
# Vanaf 2011 heeft de opleiding Taalwetenschap een Bindend Studieadvies (BSA) die de selectiviteit van het eerste jaar moet vergroten. De studieadviseur vraagt zich af of het gemiddelde cijfer van de opleiding Taalwetenschap op 1 februari, na invoering van het BSA, veranderd is. De data is beschikbaar voor het cohort gestart in 2010 en voor het cohort gestart in 2011.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het gemiddelde tentamencijfer dat de studenten halen aan de opleiding Taalwetenschap is niet veranderd na de invoer van het BSA, µ~0~ = µ~1~  
# 
# *H~A~*: Het gemiddelde tentamencijfer dat de studenten halen aan de opleiding Taalwetenschap is veranderd na de invoer van het BSA, µ~0~ ≠ µ~1~
# </div>
# 
# # Assumpties
# Voor een valide resultaat moet de data aan een aantal voorwaarden voldoen voordat de toets uitgevoerd kan worden.
# 
# ## Normaliteit 
# De *ongepaarde t-toets* gaat ervan uit dat de afhankelijke variabele normaal verdeeld is voor alle groepen. Als elke groep een aantal observaties (*n*) heeft dat groter dan 100 is,  ga er dan vanuit dat de *ongepaarde t-toets* robuust genoeg is om uit te voeren zonder dat de afhankelijke variabele een normale verdeling volgt.
# 
# Controleer de assumptie van normaliteit met de volgende stappen:  
# 1. Controleer de afhankelijke variabele per groep visueel met een histogram, een boxplot en een Q-Q plot.   
# 2. Toets of de afhankelijke variabele voor beide groepen normaal verdeeld is met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (*n* < 50) met de *Shapiro-Wilk test*.[^3]<sup>, </sup>[^4]  
# 
# De eerste stap heeft als doel een goede indruk te krijgen van de verdeling van de steekproef. In de tweede stap wordt de assumptie van normaliteit getoetst. De statistische toets laat zien of de verdeling van de observaties van een groep voldoet aan de assumptie van normaliteit. Voor beide groepen moet er voldaan zijn aan de assumptie van normaliteit.
# 
# <!-- ## TEKSTBLOK: Link1.py -->
# Als blijkt dat de afhankelijke variabele niet normaal verdeeld is voor één van of allebei de groepen, transformeer[^5] dan de afhankelijke variabele en bepaal daarna of deze wel normaal verdeeld is of gebruik de [Mann-Whitney U toets](08-Mann-Whitney-U-toets-Python.html).[^6]<sup>, </sup>[^7]  
# <!-- ## /TEKSTBLOK: Link1.py -->
# 
# ## Wel of geen gepoolde variantie
# De *ongepaarde t-toets* kan met en zonder gepoolde variantie uitgevoerd worden. Bij een gepoolde variantie is de berekening van de variantie van het verschil in gemiddelden anders en wordt aangenomen dat de varianties van beide steekproeven even groot zijn. Deze aanname is te toetsen met de *Levene's test*, waarbij een significant resultaat aangeeft dat er een verschil is in de varianties van beide groepen. De hedendaagse consensus is echter om altijd deze aanname niet te toetsen en de *ongepaarde t-toets* zonder gepoolde variantie uit te voeren.[^8] Een gepoolde variantie zorgt ervoor dat het onderscheidend vermogen[^14] van de *ongepaarde t-toets* iets hoger is als de varianties van beide groepen ongeveer gelijk zijn, maar geeft verkeerde resultaten als de varianties van elkaar afwijken. Daarnaast heeft *Levene's test* een laag onderscheidend vermogen, wat betekent dat het lastig is om ongelijke varianties goed te toetsen. Gebruik daarom de *ongepaarde t-toets* zonder gepoolde variantie; deze staat ook wel bekend als *Welch's t-toets*.[^8]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.py -->
# Er is een dataset ingeladen met gemiddelde cijfers van tweedejaarsstudenten bij de opleiding Taalwetenschap: `dfCijfers_gemiddeld`. De data bevatten cijfers van 180 studenten begonnen in 2010 en cijfers van 160 studenten begonnen in 2011.
# <!-- ## /TEKSTBLOK: Dataset-inladen.py -->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


import pandas as pd
dfCijfers_gemiddeld = pd.DataFrame(r.Cijfers_gemiddeld)


# In[ ]:


## Eerste 6 observaties
print(dfCijfers_gemiddeld.head())


# In[ ]:


## Laatste 6 observaties
print(dfCijfers_gemiddeld.tail())


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# 
# Selecteer beide groepen en sla deze op in een vector om deze makkelijker aan te kunnen roepen. 
# <!-- ## OPENBLOK: Data-selecteren.py -->

# In[ ]:


Cijfers_2010 = dfCijfers_gemiddeld[dfCijfers_gemiddeld['Cohort'] == "2010"]['Cijfers']
Cijfers_2011 = dfCijfers_gemiddeld[dfCijfers_gemiddeld['Cohort'] == "2011"]['Cijfers']


# <!-- ## /OPENBLOK: Data-selecteren.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# Inspecteer de data met `np.size()`, `np.mean()` en `np.std())`, door deze aan te roepen uit het package `numpy`.
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-inladen.py -->

# In[ ]:


# Om het gemiddelde en de standaard deviatie te berekenen, hebben we de library 'numpy' nodig
import numpy as np


# <!-- ## /OPENBLOK: Data-beschrijven-inladen.py -->
# 
# <div class="col-container">
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-1.py -->

# In[ ]:


## Aantallen, gemiddelde en standaarddeviatie 2010
print(np.size(Cijfers_2010))
print(np.mean(Cijfers_2010))
print(np.std(Cijfers_2010))


# <!-- ## /OPENBLOK: Data-beschrijven-1.py -->
#   </div>
#   <div class ="col">
# <!-- ## OPENBLOK: Data-beschrijven-2.py -->

# In[ ]:


## Aantallen, gemiddelde en standaarddeviatie 2011
print(np.size(Cijfers_2011))
print(np.mean(Cijfers_2011))
print(np.std(Cijfers_2011))


# <!-- ## /OPENBLOK: Data-beschrijven-2.py -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven-3.py -->

# In[ ]:


vN_t0 = np.size(Cijfers_2010)
vMean_t0 = np.mean(Cijfers_2010)
vSD_t0 = np.std(Cijfers_2010)
vN_t1 = np.size(Cijfers_2011)
vMean_t1 = np.mean(Cijfers_2011)
vSD_t1 = np.std(Cijfers_2011)


# <!-- ## /CLOSEDBLOK: Data-beschrijven-3.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven-4.py -->
# * Gemiddeld tentamencijfer 2010 (standaarddeviatie): `r Round_and_format(py$vMean_t0)` (`r Round_and_format(py$vSD_t0)`). *n* = `r py$vN_t0`.
# * Gemiddeld tentamencijfer 2011 (standaarddeviatie): `r Round_and_format(py$vMean_t1)` (`r Round_and_format(py$vSD_t1)`). *n* = `r py$vN_t1`.
# <!-- ## /TEKSTBLOK: Data-beschrijven-4.py -->
# 
# ## Visuele inspectie van normaliteit
# Geef de verdeling van de tentamencijfers van beide groepen visueel weer met een histogram, Q-Q plot en boxplot.
# 
# ### Histogram
# 
# Focus bij het analyseren van een histogram[^18] op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters. Een normale verdeling is symmetrisch, heeft één top en geen uitbijters.[^9]<sup>, </sup>[^10]
# 
# <!-- ## OPENBLOK: Histogram.py -->

# In[ ]:


## Histogram met matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
sub1 = fig.add_subplot(1, 2, 1)
title1 = plt.title("2010")
xlab = plt.xlabel("Cijfers")
ylab = plt.ylabel("Frequentiedichtheid")
hist1 = plt.hist(Cijfers_2010, density = True, edgecolor = "black", bins = 9)

sub2 = fig.add_subplot(1, 2, 2)
title2 = plt.title("2011")
xlab = plt.xlabel("Cijfers")
hist2 = plt.hist(Cijfers_2011, density = True, edgecolor = "black", bins = 9)

main = fig.suptitle('Taalwetenschap gemiddelde cijfers voor en na de BSA')
plt.show()


# <!-- ## /OPENBLOK: Histogram.py -->
# 
# Beide histogrammen laten een verdeling zien die redelijk symmetrisch is, één top heeft en geen uitbijters. Daarom zijn beide verdelingen bij benadering normaal verdeeld.
# 
# ### Q-Q plot
# <!-- ## TEKSTBLOK: QQplot.py -->
# Gebruik de functie `probplot` van het `scipy` package om een Q-Q plot te maken, met als datapunten kleine cirkels. 
# <!-- ## TEKSTBLOK: QQplot.py -->
# 
# Als over het algemeen de meeste datapunten op de lijn liggen, kan aangenomen worden dat de data normaal verdeeld is.
# <div class ="col-container">
#   <div class = "col"> 
# <!-- ## OPENBLOK: QQplot-t1.py -->

# In[ ]:


import scipy.stats as stats
qq = stats.probplot(Cijfers_2010, dist="norm", plot=plt)
title = plt.title("Normaal Q-Q plot van tentamencijfers 2010")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## /OPENBLOK: QQplot-t1.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot-t2.py -->

# In[ ]:


import scipy.stats as stats
qq = stats.probplot(Cijfers_2011, dist="norm", plot=plt)
title = plt.title("Normaal Q-Q plot van tentamencijfers 2011")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## /OPENBLOK: QQplot-t2.py -->
#   </div>
# </div>
# 
# Voor beide Q-Q plots liggen de meeste datapunten op of vlakbij de lijn. Hoewel er bij de uiteinden van de verdeling wat afwijkingen zijn, duidt deze grafiek op een goede benadering van de normaalverdeling voor beide cohorten.
# 
# ### Boxplot
# De box geeft de middelste 50% van de tentamencijfers weer. De zwarte lijn binnen de box is de mediaan. In de staarten of snorreharen zitten de eerste 25% en de laatste 25%. Cirkels visualiseren mogelijke uitbijters.[^9] Hoe meer de boxen overlappen, hoe waarschijnlijker er geen significant verschil is tussen de groepen. 
# 
# <!-- ## OPENBLOK: Boxplot.py -->

# In[ ]:


fig, ax = plt.subplots()
box = ax.boxplot([Cijfers_2010, Cijfers_2011], labels = ["2010", "2011"])
title = plt.title("Tentamencijfers Taalwetenschap voor en na de BSA")
plt.show()


# <!-- ## /OPENBLOK: Boxplot.py -->
# 
# De boxplotten geven de spreiding weer van het gemiddelde tentamencijfer voor de BSA en na de BSA. De boxplotten en de staarten lijken symmetrisch, wat een teken is van een bij benadering normale verdeling. Het cohort van 2011 heeft een aantal mogelijke uitbijters.[^10] 
# 
# ## Toetsen van normaliteit
# Om te controleren of de afhankelijke variabele voor beide groepen normaal verdeeld is, kan de normaliteit getoetst worden. Twee veelgebruikte toetsen zijn: de *Kolmogorov-Smirnov test* en de *Shapiro-Wilk test*.
# 
# ### Kolmogorov-Smirnov
# De *Kolmogorov-Smirnov test* toetst het verschil tussen twee verdelingen. Standaard toetst deze test het verschil tussen een normale verdeling en de verdeling van de steekproef. De Lilliefors correctie is vereist als het gemiddelde en de standaardafwijking niet van tevoren bekend of bepaald zijn, wat meestal het geval is bij een steekproef. Als de p-waarde kleiner dan 0,05 is, is de verdeling van de steekproef significant verschillend van de normale verdeling.
# 
# <!-- ## TEKSTBLOK: Lilliefors-test1.py -->
# De standaard interpretatie van de statistische toetsen van normaliteit in Python is: `(<teststatistiek>, <p-waarde>)`. Verder toetst Python hierbij tweezijdig. Gebruik bij deze toets het argument `pvalmethod = "table"` om een betrouwbare p-waarde te krijgen.
# <!-- ## /TEKSTBLOK: Lilliefors-test1.py -->
# 
# <!-- ## OPENBLOK: Library-nortest.py -->

# In[ ]:


import statsmodels.stats.api as smod


# <!-- ## OPENBLOK: Library-nortest.py -->
# 
# <div class="col-container">
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-1.py -->
# ``` {python Lilliefors Test-1, warning=FALSE}
# print(smod.lilliefors(Cijfers_2010, pvalmethod="table"))
# ```
# ``` {python Lilliefors Test-1 closed, warning=FALSE, include = FALSE}
# lilliefors2010 = smod.lilliefors(Cijfers_2010, pvalmethod="table")
# ```
# <!-- ## /OPENBLOK: Lilliefors-test-1.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-2.py -->
# ``` {python Lilliefors Test-2, warning=FALSE}
# print(smod.lilliefors(Cijfers_2011, pvalmethod="table"))
# ```
# ``` {python Lilliefors Test-2 closed, warning=FALSE, include = FALSE}
# lilliefors2011 = smod.lilliefors(Cijfers_2011, pvalmethod="table")
# ```

# In[ ]:


Cijfers_2010_n30 = r.Cijfers_2010_n30
Cijfers_2011_n30 = r.Cijfers_2011_n30
n = len(Cijfers_2010_n30)


# <!-- ## /OPENBLOK: Lilliefors-test-2.py -->
#   </div>
# </div>
# 
# Bij deze casus is van beide groepen de p-waarde groter dan 0,05, dus er zijn geen significante verschillen gevonden tussen de verdeling van de steekproef en de normale verdeling. De *ongepaarde t-toets* kan uitgevoerd worden.
# 
# ### Shapiro-Wilk Test
# De *Shapiro-Wilk test* is een soortgelijke test als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (*n* < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de steekproef significant verschillend van de normale verdeling. 
# <!-- ## TEKSTBLOK: Shapiro-Wilk-test.py -->
# Er zijn twee subsets van `Cijfers_gemiddeld` ingeladen: `Cijfers_2010_n30` en `Cijfers_2011_n30`. Beide subsets bevatten `r py$n` studenten. Voor relatief kleine steekproeven als deze is de *Shapiro-Wilk Test* geschikt.
# <!-- ## TEKSTBLOK: Shapiro-Wilk-test.py -->
# <div class = "col-container">
#   <div class="col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.py -->
# ``` {python Shapiro-Wilk Test-1, warning=FALSE}
# print(stats.shapiro(Cijfers_2010_n30))
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-1.py -->
#   </div>
#   <div class="col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-2.py -->
# ``` {python Shapiro-Wilk Test-2, warning=FALSE}
# print(stats.shapiro(Cijfers_2011_n30))
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-2.py -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor beide groepen, dus er zijn geen significante verschillen gevonden tussen de verdeling van de steekproef en de normale verdeling. De *ongepaarde t-toets* kan uitgevoerd worden.
# 
# ## Ongepaarde t-toets
# <!-- ## TEKSTBLOK: T-test.py -->
# Voer een ongepaarde t-toets uit in twee stappen. Definieer eerst de vergelijking van de twee groepen met `CompareMeans()` met als argumenten de observaties uit 2010 `DescrStatsW(Cijfers_2010)` en de observaties uit 2011 `DescrStatsW(Cijfers_2011)`. Voer daarna de t-toets uit met `ttest_ind()` met de argumenten `alternative='two-sided'` vanwege de tweezijdige alternatieve hypothese en `usevar = 'unequal'` omdat er geen gepoolde variantie wordt gebruikt. Bereken daarna het 95%-betrouwbaarheidsinterval met `tconfint_diff()` met als nieuw argument `alpha = 0.05` om het significantieniveau aan te geven. Deze functies zijn afkomstig van het package `statsmodels.stats.api`.
# <!-- ## /TEKSTBLOK: T-test.py -->
# 
# <!-- ## OPENBLOK: T-test.py -->

# In[ ]:


# Importeer library voor statistische toets
import statsmodels.stats.api as stat
# Maak een object voor de groepen die vergeleken worden
Groepen = stat.CompareMeans(stat.DescrStatsW(Cijfers_2010), stat.DescrStatsW(Cijfers_2011))
# Print de resultaten van de ongepaarde t-toets
print(Groepen.ttest_ind(alternative = 'two-sided', usevar = 'unequal'))
# Print het 95%-betrouwbaarheidsinterval
print(Groepen.tconfint_diff(alpha = 0.05, alternative = 'two-sided', usevar = 'pooled'))


# <!-- ## /OPENBLOK: T-test.py -->
# <!-- ## CLOSEDBLOK: T-test.py -->

# In[ ]:


stat, pval, df = Groepen.ttest_ind(alternative='two-sided', usevar = 'unequal')
lb, ub = Groepen.tconfint_diff(alpha=0.05, alternative='two-sided', usevar='pooled')
mean1 = np.mean(Cijfers_2010)
mean2 = np.mean(Cijfers_2011)


# <!-- ## /CLOSEDBLOK: T-test.py -->
# 
# <!-- ## TEKSTBLOK: T-test2.py -->
# * *t* = `r Round_and_format(py$stat)`, *p* = `r Round_and_format(py$pval)`
# * Vrijheidsgraden, *df* = *n* -1 = `r py$n`-1 = `r py$df`  
# * De p-waarde is groter dan 0,05, dus de H~0~ wordt niet verworpen [^11]
# * Vrijheidsgraden: *df* = `r Round_and_format(py$df)`, niet gelijk aan aantal observaties min één bij een ongepaarde t-toets zonder gepoolde varianties
# * 95%-betrouwbaarheidsinterval: bij het herhalen van het experiment met verschillende steekproeven van de populatie zal 95% van de betrouwbaarheidsintervallen de daadwerkelijke parameter bevatten, het verschil tussen de hoogte van de cijfers voor en na de BSA  cursus, µ~verschil~ = µ~T2011~ - µ~T2010~. In deze casus is het interval tussen `r Round_and_format(py$lb)` en `r Round_and_format(py$ub)`. Aangezien 0 in dit interval zit, is er geen significant verschil tussen beide gemiddelden in 2010 en 2011.
# * Het gemiddelde van de steekproef is in 2010 `r Round_and_format(py$mean1)`
# * Het gemiddelde van de steekproef is in 2011 `r Round_and_format(py$mean2)`
# <!-- ## /TEKSTBLOK: T-test2.py -->
# 
# ### Effectmaat: Cohen's d 
# De p-waarde geeft aan of het verschil tussen twee groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^12] Een veel gebruikte effectmaat is Cohen's *d*. Cohen's *d* geeft een gestandaardiseerd verschil weer: het verschil in gemiddelden tussen twee groepen gecorrigeerd voor de gecombineerde standaardafwijking van de twee groepen. Een indicatie om *d* te interpreteren is: rond 0,3 is het een klein effect, rond 0,5 is het een gemiddeld effect en rond 0,8 is het een groot effect.[^13]
# 
# In dit voorbeeld is de p-waarde groter dan 0,05, dus is een effectmaat uitrekenen onnodig. Pas de volgende stappen toe bij een p-waarde kleiner dan 0,05.
# 
# <!-- ## TEKSTBLOK: Cohen-d.py -->
# Er is geen Python functie voor Cohen's d. Bereken daarom de effectmaat zelf door het verschil tussen de gemiddelden van beide groepen te delen door de ongepoolde standaardafwijking.[^15] Neem de absolute waarde omdat het gebruikelijk is om een effectmaat als positief getal weer te geven.
# <!-- ## /TEKSTBLOK: Cohen-d.py -->
# 
# <!-- ## OPENBLOK: Cohens-d-test.py -->

# In[ ]:


# Bereken verschil in gemiddelden beide groepen
Verschil = np.mean(Cijfers_2011) - np.mean(Cijfers_2010)

# Bereken ongepoolde standaardafwijking
SD = np.sqrt((np.var(Cijfers_2010, ddof = 1) + np.var(Cijfers_2010, ddof = 1)) / 2)

# Bereken Cohen's d
d = abs(Verschil / SD)

# Print effectmaat
print(d)


# <!-- ## /OPENBLOK: Cohens-d-test.py -->
# <!-- ## CLOSEDBLOK: Cohens-d-test.py -->
# <!-- ## /CLOSEDBLOK: Cohens-d-test.py -->
# <!-- ## TEKSTBLOK: Cohens-d-test.py -->
# *d* = `r Round_and_format(py$d)`. De sterkte van het effect van de tutor op het cijfer is verwaarloosbaar. 
# <!-- ## /TEKSTBLOK: Cohens-d-test.py -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# Een *ongepaarde t-toets* is uitgevoerd om te toetsen of het gemiddelde tentamencijfer is veranderd na de invoer van het BSA. Het verschil tussen het gemiddelde tentamencijfer van cohort 2010 (*M~2010~* = `r Round_and_format(py$vMean_t0)`, *SD~2010~* = `r Round_and_format(py$vSD_t0)`) en het gemiddelde tentamencijfer van cohort 2011 (*M~2011~* = `r Round_and_format(py$vMean_t1)`, *SD~2011~* = `r Round_and_format(py$vSD_t1)`) is  niet significant, *t* ~`r py$df`~ = `r Round_and_format(py$stat)`, *p* = `r Round_and_format(py$pval)`. Het 95% betrouwbaarheidsinterval voor het verschil tussen het gemiddelde van beide groepen loopt van `r Round_and_format(py$lb)` tot `r Round_and_format(py$ub)`. Het gemiddelde tentamencijfer lijkt niet veranderd te zijn na de invoer van het BSA. 
# 
# | Cohort   | N         | M            | SD         |
# | -------- | --------- | ------------ | ---------- |
# | 2010     | `r py$vN_t0` | `r Round_and_format(py$vMean_t0)` | `r Round_and_format(py$vSD_t0)` |
# | 2011     | `r py$vN_t1` | `r Round_and_format(py$vMean_t1)` | `r Round_and_format(py$vSD_t1)` |
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# *Tabel 1. Groepsgrootte, gemiddeld tentamencijfer en standaarddeviatie per cohort*
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Van Geloven, N. (25 mei 2016). *T-toets* [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/T-toets#ongepaarde_t-toets).
# [^2]: Lumley, T., Diehr, P., Emerson, S., & Chen, L. (2002). The importance of the normality assumption in large public health data sets. *Annu Rev Public Health, 23*, 151-69. doi: 10.1146/annurev.publheath.23.100901.140546 http://rctdesign.org/techreports/arphnonnormality.pdf 
# [^3]: Laerd statistics. (2018). [Testing for Normality using SPSS Statistics](https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php).
# [^4]: Normaliteit. (14 juli 2014). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).
# [^5]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^6]: Van Geloven, N. (13 maart 2018). *Mann-Whitney U toets* [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Mann-Whitney_U_toets).
# [^7]: De [Mann-Whitney U toets](08-Mann-Whitney-U-toets-R.html) maakt een rangschikking van de data. Hierdoor is de test verdelingsvrij en is normaliteit geen assumptie. Ook zijn uitbijters minder van invloed op het eindresultaat. Toch wordt er voor deze test minder vaak gekozen, doordat bij het maken van een rankschikking de data informatie verliest. Als de data wel normaal verdeeld is, heeft de [Mann-Whitney U toets](08-Mann-Whitney-U-toets-R.html) minder onderscheidend vermogen dan wanneer de *ongepaarde t-toets* uitgevoerd zou worden. 
# [^8]: Lakens, D. (26 januari 2015). *Always use Welch's t-test instead of Student's t-test*. [The 20% Statistician](http://daniellakens.blogspot.com/2015/01/always-use-welchs-t-test-instead-of.html).
# [^9]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^10]: Uitbijters kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de uitbijters valide uitbijters zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van uitbijters kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde uitbijters te melden in een rapport. 
# [^11]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^12]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^13]: Marshall, E., & Boggis, E. (2016). *The statistics tutor’s quick guide to commonly used statistical tests*. http://www.statstutor.ac.uk/resources/uploaded/tutorsquickguidetostatistics.pdf.
# [^14]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.  
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
# <!-- ## TEKSTBLOK: Extra-Bron.py -->
# [^15]: Navarro, D. J. (2015). *Learning statistics with R: A tutorial for psychology students
#   and other beginners. (Version 0.5)* University of Adelaide. Adelaide, Australia. 
# [Link](http://www.fon.hum.uva.nl/paul/lot2015/Navarro2014.pdf)
# <!-- ## /TEKSTBLOK: Extra-Bron.py -->
# 
