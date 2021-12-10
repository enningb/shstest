#!/usr/bin/env python
# coding: utf-8
---
title: "Repeated measures ANOVA"
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
# <!-- ## CLOSEDBLOK: Reticulate.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'library(reticulate)\nknitr::knit_engines$set(python = reticulate::eng_python)')


# <!-- ## /CLOSEDBLOK: Reticulate.py -->
# 
# <!-- ## CLOSEDBLOK: Status.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Status.R -->
# 
# <!-- ## OPENBLOK: Data-aanmaken.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/04.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# Gebruik de *repeated measures ANOVA* om gemiddelden te vergelijken van een groep bij twee of meer herhaalde metingen of om gemiddelden van twee of meer gepaarde groepen te vergelijken.[^1] 
# 
# # Onderwijscasus
# <div id = "casus">
# 
# De opleidingsdirecteur van de bachelor Technische Natuurkunde van een universiteit hoort vanuit de opleidingscommissie dat de eerstejaars studenten de studielast van de eerste onderwijsperiode als erg hoog ervaren. Om te onderzoeken hoe deze ervaren studielast verminderd kan worden, wil hij onderzoeken hoeveel tijd de studenten per week besteden aan hun vakken. Met behulp van een vragenlijst over de studiebelasting in het eerste jaar verzamelt hij gegevens van het aantal uur per week dat eerstejaars studenten besteden aan de vakken in de eerste onderwijsperiode: Lineaire Algebra, Relativiteitstheorie en Kosmologie. Op deze manier kan hij onderzoeken of er verschillen in de tijdsbesteding aan de verschillende vakken zijn en om te bepalen van welke vakken de studielast aangepast moet worden.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het aantal studieuren per week van eerstejaars studenten van de bachelor Technische Natuurkunde is hetzelfde voor de drie vakken in de eerste onderwijsperiode
# 
# *H~A~*: Het aantal studieuren per week van eerstejaars studenten van de bachelor Technsiche Natuurkunde is niet hetzelfde voor de drie vakken in de eerste onderwijsperiode
# 
# </div>
# 
# # Assumpties
# Om een valide toetsresultaat te bereiken met de *repeated measures ANOVA* moet de data aan een aantal voorwaarden voldoen: normaliteit, sphericiteit en onafhankelijkheid.[^1] Onafhankelijkheid houdt in dat de herhaalde metingen van de deelnemers[^12] onafhankelijk van elkaar zijn.
# 
# ## Normaliteit
# <!-- ## TEKSTBLOK: link1.R -->
# De assumptie van normaliteit houdt in dat er een normale
# verdeling van de afhankelijke variabele is in elke groep van metingen. Wanneer er duidelijke afwijkingen van normaliteit zijn,
# is het transformeren van de data een optie.[^2] Een andere optie is het gebruik van de nonparametrische
# [Friedman's ANOVA](09-Friedmans-ANOVA-R.html) waar normaliteit geen assumptie is.[^3] Controleer de assumptie van normaliteit voor elke groep van metingen met de volgende stappen:  
# 1. Controleer de data visueel met een histogram, een boxplot of een Q-Q plot.   
# 2. Toets of de data normaal verdeeld is met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (n < 50) met de *Shapiro-Wilk test*.[^4]<sup>, </sup>[^5]  
# <!-- ## /TEKSTBLOK: link1.R -->
# 
# ## Sphericiteit
# De assumptie van sphericiteit houdt in dat de variantie van de verschilscores tussen groepen van metingen ongeveer aan elkaar gelijk zijn.[^6] In deze casus zijn dat de verschilscores tussen de drie vakken: Lineaire Algebra minus Relativiteitstheorie, Relativiteitstheorie minus Kosmologie en Kosmologie minus Lineaire Algebra. Toets deze assumptie met *Mauchly's test*. Wanneer de data niet aan de assumptie voldoen, geeft de gewone *repeated measures ANOVA* een verkeerd resultaat. Er zijn echter correcties die gebruikt kunnen worden wanneer de data niet aan sphericiteit voldoen. Een voorbeeld van mogelijke output van *Mauchly's test* in R is hieronder weergegeven.
# 
# <!-- ## CLOSEDBLOK: Sphericiteit.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'cat("$`Mauchly\'s Test for Sphericity`\n  Effect         W           p p<.05\n2    Vak 0.8732982 0.005073887     *\n\n$`Sphericity Corrections`\n  Effect       GGe        p[GG] p[GG]<.05       HFe        p[HF] p[HF]<.05\n2    Vak   0.47683     0.05279         *   0.56298      0.04692         ")')


# <!-- ## /CLOSEDBLOK: Sphericiteit.py -->
# 
# <!-- ## TEKSTBLOK: Sphericiteit1.py -->
# Bij een p-waarde < 0,05, toont *Mauchly's test* dat de assumptie van sphericiteit geschonden is. In de output is dit te zien aan de p-waarde van 0,0051 onder ` $Mauchly's Test for Sphericity `. Er zijn twee mogelijke correcties wanneer er geen sphericiteit is: de Greenhouse-Geisser (GG) en Huynh-Feldt (HF) correctie. De Greenhouse-Geisser correctie staat bekend als conservatief, wat betekent dat de correctie een relatief lage kans op een type I fout heeft. In andere woorden, het zal niet vaak gebeuren dat deze correctie een significant effect aantoont wanneer dat er in werkelijkheid niet is. De Huynh-Feldt correctie staat echter bekend als liberaal, wat betekent dat er een relatief hoge kans op een type I fout is. De teststatistiek en p-waarde van beide correcties zijn in de output te vinden onder ` $Sphericity Corrections `.
# <!-- ## TEKSTBLOK: Sphericiteit1.py -->
# 
# Houd de volgende richtlijnen aan bij het interpreteren van de *repeated measures ANOVA* wanneer niet aan sphericiteit is voldaan:
# 
# * Wanneer beide correcties significant zijn, rapporteer de (conservatieve) Greenhouse-Geisser correctie.
# * Wanneer beide correcties niet significant zijn, rapporteer de (liberale) Huynh-Feldt correctie.
# * Wanneer de een significant is en de ander niet, bereken de gemiddelde p-waarde van beide correcties.
#     * Wanneer deze p-waarde significant is, rapporteer dan de significante correctie.
#     * Wanneer deze p-waarde niet significant is, rapporteer dan de niet significante correctie.
# 
# In de voorbeeldoutput is de p-waarde van de Greenhouse-Geisser correctie groter dan 0,05 en de p-waarde van de Huynh-Feldt correctie kleiner dan 0,05. Het gemiddelde van beide p-waarden is 0,049855, wat betekent dat er een significant resultaat is. Rapporteer in dit geval dus de (significante) Huynh-Feldt correctie, i.e. *F* = 0,56, *p* < 0,05.  

# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen van metingen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^6] Voor de *repeated measures ANOVA* wordt de effectmaat eta squared vaak gebruikt.
# 
# ## Eta squared
# De effectmaat eta squared (*η^2^*) berekent de proportie van de variantie in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele. In deze casus berekent het de proportie van de variantie in het aantal uren studeren die verklaard kan worden door het vak in de eerste onderwijsperiode. Een indicatie om *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^7]
# 
# # Post-hoc toetsen
# De *repeated measures ANOVA* toetst of één of meerdere van de gemiddelden anders is dan de andere gemiddelden. Voer een post-hoc toets uit om te bepalen welke groepen van metingen significant verschillen.
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout. Er zijn ook andere opties voor een correctie op de p-waarden.
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.py -->
# Er is een dataset `dfStudieuren_technische_natuurkunde` ingeladen met het aantal studieuren van eerstejaars studenten van de bachelor Technische Natuurkunde voor de drie vakken in de eerste onderwijsperiode.
# <!-- ## /TEKSTBLOK: Dataset-inladen.py -->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken1.py -->

# In[ ]:


import pandas as pd
dfStudieuren_technische_natuurkunde = pd.DataFrame(r.Studieuren_technische_natuurkunde)


# In[ ]:


## Eerste 5 observaties
print(dfStudieuren_technische_natuurkunde.head(5))


# In[ ]:


## Laatste 5 observaties
print(dfStudieuren_technische_natuurkunde.tail(5))


# <!-- ## /OPENBLOK: Data-bekijken1.py -->
# 
# Selecteer de drie groepen van metingen en sla deze op in een vector om deze makkelijker aan te kunnen roepen. 
# <!-- ## OPENBLOK: Data-selecteren.py -->

# In[ ]:


Studieuren_lineaire_algebra = dfStudieuren_technische_natuurkunde[dfStudieuren_technische_natuurkunde['Vak'] == "Lineaire Algebra"]['Studieuren']
Studieuren_relativiteitstheorie = dfStudieuren_technische_natuurkunde[dfStudieuren_technische_natuurkunde['Vak'] == "Relativiteitstheorie"]['Studieuren']
Studieuren_kosmologie = dfStudieuren_technische_natuurkunde[dfStudieuren_technische_natuurkunde['Vak'] == "Kosmologie"]['Studieuren']


# <!-- ## /OPENBLOK: Data-selecteren.py -->

# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# Inspecteer de data met `np.mean()`, `np.std()` en `len()` om meer inzicht te krijgen in de data,, door deze aan te roepen uit het `numpy` package.
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# 
# <!-- ## OPENBLOK: numpy1.py -->

# In[ ]:


import numpy as np


# <!-- ## /OPENBLOK: numpy1.py -->

# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven1.py -->

# In[ ]:


# Gemiddelde
print(np.mean(Studieuren_lineaire_algebra))
# Standaardafwijking
print(np.std(Studieuren_lineaire_algebra))
# Aantal observaties
print(len(Studieuren_lineaire_algebra))


# <!-- ## OPENBLOK: Data-beschrijven1.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Data-beschrijven2.py -->

# In[ ]:


# Gemiddelde
print(np.mean(Studieuren_relativiteitstheorie))
# Standaardafwijking
print(np.std(Studieuren_relativiteitstheorie))
# Aantal observaties
print(len(Studieuren_relativiteitstheorie))


# <!-- ## OPENBLOK: Data-beschrijven2.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Data-beschrijven3.py -->

# In[ ]:


# Gemiddelde
print(np.mean(Studieuren_kosmologie))
# Standaardafwijking
print(np.std(Studieuren_kosmologie))
# Aantal observaties
print(len(Studieuren_kosmologie))


# <!-- ## /OPENBLOK: Data-beschrijven3.py -->
#   </div>
# </div>

# <!-- ## CLOSEDBLOK: Data-beschrijven4.py -->

# In[ ]:


vM_LA = np.mean(Studieuren_lineaire_algebra)
vSD_LA = np.std(Studieuren_lineaire_algebra)
vN_LA = np.size(Studieuren_lineaire_algebra)

vM_RT = np.mean(Studieuren_relativiteitstheorie)
vSD_RT = np.std(Studieuren_relativiteitstheorie)
vN_RT = np.size(Studieuren_relativiteitstheorie)

vM_KL = np.mean(Studieuren_kosmologie)
vSD_KL = np.std(Studieuren_kosmologie)
vN_KL = np.size(Studieuren_kosmologie)


# <!-- ## /CLOSEDBLOK: Data-beschrijven4.py -->
# 
# <!-- ## TEKSTBLOK: Datatekst-beschrijven.py -->
# * Gemiddeld aantal studieuren Lineaire Algebra (standaarddeviatie): `r Round_and_format(py$vM_LA)` (`r Round_and_format(py$vSD_LA)`). *n* = `r py$vN_LA`  
# * Gemiddeld aantal studieuren Relativiteitstheorie (standaarddeviatie): `r Round_and_format(py$vM_RT)` (`r Round_and_format(py$vSD_RT)`). *n* = `r py$vN_RT`.
# * Gemiddeld aantal studieuren Kosmologie (standaarddeviatie): `r Round_and_format(py$vM_KL)` (`r Round_and_format(py$vSD_KL)`). *n* = `r py$vN_KL`.
# 
# <!-- ## /TEKSTBLOK: Datatekst-beschrijven.py -->
# 
# ## Visuele inspectie van normaliteit
# Geef de verdeling van de data visueel weer met een histogram, Q-Q plot en boxplot.
# 
# ### Histogram
# 
# Focus bij het analyseren van een histogram[^18] op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters. Een normale verdeling is symmetrisch, heeft één top en geen uitbijters.[^9]<sup>, </sup>[^10]
# 
# <!-- ## OPENBLOK: Histogram.py -->

# In[ ]:


# Laad seaborn of facets te maken
import seaborn as sb
# Laad matplotlib.pyplot om plots te maken
import matplotlib.pyplot as plt

# Maak een facet plot met een histogram voor elke vooropleiding
g = sb.FacetGrid(dfStudieuren_technische_natuurkunde, col="Vak")
g = (g.map(plt.hist, "Studieuren", edgecolor = "black").set_axis_labels("Aantal studieuren"))
plt.show()


# <!-- ## /OPENBLOK: Histogram.py -->
# 
# Alle drie de verdelingen hebben één top en lijken geen uitbijters te hebben. Tevens zijn de verdelingen redelijk symmetrisch. Deze verdelingen benaderen de normaalverdeling.
# 
# ### Q-Q plot
# <!-- ## TEKSTBLOK: QQplot.py -->
# Importeer `scipy.stats` om een Q-Q plot te maken. Gebruik de functie `scipy.stats.probplot()` om een Q-Q plot te maken.
# <!-- ## TEKSTBLOK: QQplot.py -->
# 
# Als over het algemeen de meeste datapunten op de lijn liggen, neem dan aan dat de data normaal verdeeld zijn.
# <div class = "col-container">
#   <div class="col">
# <!-- ## OPENBLOK: QQplot1.py -->

# In[ ]:


import scipy.stats as stats
qq = stats.probplot(Studieuren_lineaire_algebra, dist="norm", plot=plt)
title = plt.title("Lineaire algebra")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## /OPENBLOK: QQplot1.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot2.py -->

# In[ ]:


import scipy.stats as stats
qq = stats.probplot(Studieuren_relativiteitstheorie, dist="norm", plot=plt)
title = plt.title("Relativiteitstheorie")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## /OPENBLOK: QQplot2.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot3.py -->

# In[ ]:


import scipy.stats as stats
qq = stats.probplot(Studieuren_kosmologie, 
dist="norm", 
plot=plt)
title = plt.title("Kosmologie")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## OPENBLOK: QQplot3.py -->
#   </div>
# </div>
# 
# Bij alle drie de Q-Q plots liggen de punten rond de lijn die normaliteit aangeeft; vermoedelijk zijn deze data normaal verdeeld.
# 
# ### Boxplot
# De box geeft de middelste 50% van het aantal studieuren per week weer. De zwarte lijn binnen de box is de mediaan. In de staarten of snorreharen zitten de eerste 25% en de laatste 25%. Cirkels visualiseren mogelijke uitbijters.[^9]<sup>, </sup>[^10] Hoe meer de boxen overlappen, hoe waarschijnlijker er geen significant verschil is tussen de groepen van metingen. 
# 
# <!-- ## OPENBLOK: Boxplot.py -->

# In[ ]:


fig, ax = plt.subplots()
box = ax.boxplot([Studieuren_lineaire_algebra, Studieuren_relativiteitstheorie, Studieuren_kosmologie], labels = ["Lineaire algebra", "Relativiteitstheorie", "Kosmologie"])
title = plt.title("")
ylab = plt.ylabel("Aantal studieuren")
plt.show()


# <!-- ## /OPENBLOK: Boxplot.py -->
# 
# De boxplotten geven de spreiding weer van het aantal studieuren voor de drie vakken in de eerste onderwijsperiode: Kosmologie, Lineaire Algebra en Relativiteitstheorie. In het algemeen lijken de vakken een symmetrische verdeling te hebben. De medianen van Kosmologie en Lineaire Algebra liggen een stuk lager dan de mediaan van Relativiteitstheorie. Kosmologie en Relativiteitstheorie hebben mogelijke uitbijters. 

# ## Toetsen van normaliteit
# Om te controleren of de verdelingen van de vakken normaal verdeeld zijn, kan de normaliteit getoetst worden. Twee veelgebruikte toetsen zijn: de *Kolmogorov-Smirnov test* en de *Shapiro-Wilk test*.
# 
# ### Kolmogorov-Smirnov
# De *Kolmogorov-Smirnov test* toetst het verschil tussen twee verdelingen. Standaard toetst deze test het verschil tussen een normale verdeling en de verdeling van de steekproef. De Lilliefors correctie is vereist als het gemiddelde en de standaardafwijking niet van tevoren bekend of bepaald zijn, wat meestal het geval is bij een steekproef. Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.
# <!-- ## TEKSTBLOK: Lilliefors-test1.py -->
# De standaard interpretatie van een statitische toets in Python is: `(<teststatistiek>, <p-waarde>)`. Verder toetst Python standaard tweezijdig.
# <!-- ## /TEKSTBLOK: Lilliefors-test1.py -->
# 
# <!-- ## OPENBLOK: Library-nortest.py -->

# In[ ]:


import statsmodels.stats.api


# <!-- ## /OPENBLOK: Library-nortest.py -->
# 
# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Lilliefors-test-1.py -->
# ``` {python Lilliefors Test-1, warning=FALSE}
# print(statsmodels.stats.api.lilliefors(Studieuren_lineaire_algebra, pvalmethod="table"))
# ```
# <!-- ## OPENBLOK: Lilliefors-test-1.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-2.py -->
# ``` {python Lilliefors Test-2, warning=FALSE}
# print(statsmodels.stats.api.lilliefors(Studieuren_relativiteitstheorie, pvalmethod="table"))
# ```
# <!-- ## OPENBLOK: Lilliefors-test-2.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-3.py -->
# ``` {python Lilliefors Test-3, warning=FALSE}
# print(statsmodels.stats.api.lilliefors(Studieuren_kosmologie, pvalmethod="table"))
# ```
# <!-- ## /OPENBLOK: Lilliefors-test-3.py -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor elk vak; er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. [^11] De *repeated measures ANOVA* kan uitgevoerd worden.
# 
# ### Shapiro-Wilk Test
# De *Shapiro-Wilk test* is een soortgelijke toets als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (n < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.
# 
# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.py -->
# ``` {python Shapiro-Wilk Test-3, warning=FALSE}
# import scipy.stats as stats
# print(stats.shapiro(Studieuren_kosmologie))
# ```
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.py -->
#   </div>
#   <div class= "col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-2.py -->
# ``` {python Shapiro-Wilk Test-2, warning=FALSE}
# import scipy.stats as stats
# print(stats.shapiro(Studieuren_relativiteitstheorie))
# 
# ```
# <!-- ## OPENBLOK: Shapiro-Wilk-test-2.py -->
#   </div>
#   <div class= "col"> 
# <!-- ## OPENBLOK: Shapiro-Wilk-test-3.py -->
# ``` {python Shapiro-Wilk Test-1, warning=FALSE}
# import scipy.stats as stats
# print(stats.shapiro(Studieuren_lineaire_algebra))
# 
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-3.py -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor elk vak, dus er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling.[^11] De *repeated measures ANOVA* kan uitgevoerd worden.

# ## Repeated measures ANOVA 
# 
# <!-- ## TEKSTBLOK: repeatedmeasuresANOVA1.py -->
# Voer de *repeated measures ANOVA* uit om de vraag te beantwoorden of er verschillen zijn tussen het aantal studieuren voor de vakken in de eerste onderwijsperiode van het eerste jaar van de bachelor Technische Natuurkunde. Gebruik de functie `rm_anova` van het package `pingouin` met als argumenten de dataset `dfStudieuren_technische_natuurkunde`, de afhankelijke variabele `dv = 'Studieuren'`, de onafhankelijke variabele `within = 'Vak'`, de variabele die de observaties aangeeft `subject = 'Studentnummer'` en `detailed = True` om een uitgebreide tabel met resultaten te verkrijgen.
# <!-- ## /TEKSTBLOK: repeatedmeasuresANOVA1.py -->
# 
# <!-- ## OPENBLOK: repeatedmeasuresANOVA2.py -->

# In[ ]:


# Importeer package pingouin
import pingouin as pg

# Voer de repeated measures ANOVA uit
aov = pg.rm_anova(data = dfStudieuren_technische_natuurkunde, 
dv = 'Studieuren', 
within = 'Vak',
subject = 'Studentnummer')

# Print de resultaten van Mauchly's test
print(aov[['eps','p-GG-corr','W-spher','p-spher','sphericity']])

# Print de resultaten van repeated measures ANOVA
print(aov[['Source','ddof1','ddof2','F','p-unc','np2']])
#aov['p-GG-corr']


# <!-- ## /OPENBLOK: repeatedmeasuresANOVA2.py -->
# 
# <!-- ## CLOSEDBLOK: repeatedmeasuresANOVA3.py -->

# In[ ]:


import pingouin as pg
aov2 = pg.rm_anova(data = dfStudieuren_technische_natuurkunde, 
dv = 'Studieuren', 
within = 'Vak',
subject = 'Studentnummer')

Mauchly_W = aov2['W-spher']
GG_F = aov2['eps']
eta2 = aov2['np2']


# <!-- ## /CLOSEDBLOK: repeatedmeasuresANOVA3.py -->
# 
# <!-- ## TEKSTBLOK: repeatedmeasuresANOVA4.py -->
# 
# * *Mauchly's test* toont aan dat de assumptie van sphericiteit niet standthoudt in deze casus ($\chi^2$ = `r Round_and_format(py$Mauchly_W)`, p < 0,0001); gebruik in dit geval een van de correcties. In Python is alleen de (conservatieve) Greenhouse-Geisser correctie mogelijk, dus rapporteer deze.
# * De data voldoet niet aan de assumptie van sphericiteit, $\chi^2$ = `r Round_and_format(py$Mauchly_W)`, p < 0,0001
# * De resultaten van de Greenhouse-Geisser correctie zijn *F* = `r Round_and_format(py$GG_F)`, p < 0,0001, *η^2^* = `r Round_and_format(py$eta2)`
# * De p-waarde < 0,05, dus de H~0~ wordt verworpen.[^11]
# * Er is een significant verschil tussen het aantal studieuren voor de drie vakken in de eerste onderwijsperiode; het effect van de verschillende vakken op het aantal studieuren is groot
# 
# <!-- ## /TEKSTBLOK: repeatedmeasuresANOVA4.py -->
# 
# ## Post-hoc toets
# <!-- ## TEKSTBLOK: posthoc1.py -->
# Voer post-hoc toetsen uit om te onderzoeken welke vakken uit de eerste onderwijsperiode van elkaar verschillen wat betreft het aantal studieuren dat eerstejaars studenten van de bachelor Technische Natuurkunde hieraan besteden. Bereken eerst de verschillen in gemiddelde tussen de drie vakken. Gebruik daarna voor de post-hoc toetsen de functie `pairwise_ttests` van het `pingouin` package met als argumenten de dataset `data = dfStudieuren_technische_natuurkunde`, de afhankelijke variabele `dv = 'Studieuren'`, de onafhankelijke variabele `within = 'Vak'`, de variabele die de observaties aangeeft `subject = 'Studentnummer'`, de methode om te corrigeren voor meerdere toetsen (Bonferroni) `padjust = 'bonf`' en `parametric = True` om aan te geven dat er een parametrische toets (de t-toets) gebruikt moet worden.
# <!-- ## /TEKSTBLOK: posthoc1.py -->
# 
# <!-- ## OPENBLOK: posthoc2.py -->

# In[ ]:


# Bereken de verschillen in gemiddelde tussen de drie vakken
Verschil_gemiddelde_LA_RT = np.mean(Studieuren_lineaire_algebra) - np.mean(Studieuren_relativiteitstheorie)
Verschil_gemiddelde_RT_KL = np.mean(Studieuren_relativiteitstheorie) - np.mean(Studieuren_kosmologie)
Verschil_gemiddelde_KL_LA = np.mean(Studieuren_kosmologie) - np.mean(Studieuren_lineaire_algebra)

# Voer de post-hoc toetsen uit
post_hoc = pg.pairwise_ttests(data = dfStudieuren_technische_natuurkunde, 
dv = 'Studieuren', 
within = 'Vak',
subject = 'Studentnummer',
padjust = 'bonf',
parametric = True)

# Print de benodigde resultaten
print(post_hoc[['A', 'B', 'T', 'p-corr']])


# <!-- ## /OPENBLOK: posthoc2.py -->
# 
# <!-- ## CLOSEDBLOK: posthoc3.py -->

# In[ ]:


# Bereken de p-waarden van de post-hoc toets
phtest = pg.pairwise_ttests(data = dfStudieuren_technische_natuurkunde, 
dv = 'Studieuren', 
within = 'Vak',
subject = 'Studentnummer',
padjust = 'bonf',
parametric = True)

# Sla de p-waarde van niet significante toets op
pwaardes = phtest['p-corr']
pwaarde_niet_significant = pwaardes[1]


# <!-- ## /CLOSEDBLOK: posthoc3.py -->
# 
# <!-- ## /TEKSTBLOK: posthoc4.py -->
# * Er is een significant verschil tussen Lineaire algebra en Relativiteitstheorie, *MD* = `r Round_and_format(py$Verschil_gemiddelde_LA_RT)`, p < 0,0001
# * Er is een significant verschil tussen Relativiteitstheorie en Kosmologie, *MD* = `r Round_and_format(py$Verschil_gemiddelde_RT_KL)`, p < 0,0001
# * Er is geen significant verschil tussen Kosmologie en Lineaire algebra, *MD* = `r Round_and_format(py$Verschil_gemiddelde_KL_LA)`, p = `r Round_and_format(py$pwaarde_niet_significant)`
# 
# <!-- ## /TEKSTBLOK: posthoc4.py -->

# # Rapportage
# 
# <!-- ## TEKSTBLOK: rapportage.py -->
# Een *repeated measures ANOVA* is uitgevoerd om te onderzoeken of er verschillen zijn tussen het aantal studieuren dat eerstejaars studenten van de bachelor Technische Natuurkunde besteden aan de vakken in de eerste onderwijsperiode. De vakken zijn Lineaire Algebra, Relativiteitstheorie en Kosmologie; beschrijvende statistieken zijn te vinden in Tabel 1. De data voldoen niet aan de assumptie van sphericiteit ($\chi^2$ = `r Round_and_format(py$Mauchly_W)`, p < 0,0001), daarom is de Greenhouse-Geisser correctie gebruikt. Het aantal studieuren voor de drie vakken in de eerste onderwijsperiode verschilt significant van elkaar, *F* = `r Round_and_format(py$GG_F)`, p < 0,0001, *η^2^* = `r Round_and_format(py$eta2)`. De sterkte van het effect van het vak op het aantal studieuren is groot. Post-hoc toetsen - waarbij een Bonferroni correctie is toegepast om te corrigeren voor meerdere toetsen -  tonen aan dat het aantal studieuren voor het vak Relativiteitstheorie significant verschilt van het aantal studieuren voor zowel het vak Lineaire Algebra als Kosmologie (voor beide p < 0,0001), maar dat er geen significant verschil is tussen de vakken Lineaire Algebra en Kosmologie (p = `r Round_and_format(py$pwaarde_niet_significant)`. De resultaten suggereren dat eerstejaars studenten van de bachelor Technische Natuurkunde een hoger aantal uren steken in het vak Relativiteitstheorie dan in de vakken Lineaire Algebra en Kosmologie.
# 
# | Opleiding     | M          | SD          | N          |
# | ------------- | ---------- | ---------- | ----------- |
# | Lineaire Algebra      | `r Round_and_format(py$vM_LA)` | `r Round_and_format(py$vSD_LA)` | `r Round_and_format(py$vN_LA)` |
# | Relativiteitstheorie  | `r Round_and_format(py$vM_RT)` | `r Round_and_format(py$vSD_RT)` | `r Round_and_format(py$vN_RT)` |
# | Kosmologie            | `r Round_and_format(py$vM_KL)` | `r Round_and_format(py$vSD_KL)` | `r Round_and_format(py$vN_KL)` |
# *Tabel 1. Het gemiddelde aantal studieuren, bijbehorende standaarddeviatie en groepsgrootte voor de vakken in de eerste onderwijsperiode van de bachelor Technische Natuurkunde.*
# <!-- ## /TEKSTBLOK: rapportage.py -->
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Universiteit van Amsterdam (26 augustus 2014). *Repeated-Measures ANOVA*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Repeated-Measures_ANOVA).
# [^2]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^3]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^4]: Laerd statistics (2018). *Testing for Normality using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php. 
# [^5]: Universiteit van Amsterdam (14 juli 2014). *Normaliteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).
# [^6]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^7]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^9]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^10]: Uitbijters kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de uitbijters valide uitbijters zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van uitbijters kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde uitbijters te melden in een rapport. 
# [^11]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^12]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
