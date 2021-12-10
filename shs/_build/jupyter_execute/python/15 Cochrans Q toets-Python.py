#!/usr/bin/env python
# coding: utf-8
---
title: "Cochran's Q toets"
output:
  html_document:
    theme: lumen
    toc: yes
    toc_depth: 2
    toc_float: 
      collapsed: FALSE 
    number_sections: true
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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/15.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# 
# Gebruik *Cochran's Q toets* om te toetsen of er verschillen zijn op een binaire variabele[^1] tussen drie of meer herhaalde metingen van één groep of tussen drie of meer gepaarde groepen.[^2] 

# # Onderwijscasus
# <div id = "casus">
# De opleidingsdirecteur van de bacheloropleiding Kunstmatige Intelligentie van een universiteit merkt dat er tijdens het eerste studiejaar veel studenten zijn die niet alle vakken voldoende afsluiten. Hij wil uitvinden in welke onderwijsperiode dit vooral plaatsvindt om te onderzoeken waardoor de studievertraging veroorzaakt wordt. Op deze universiteit bestaat het eerste jaar uit vier onderwijsperiodes. Daarom vraagt hij studieresultaten op van eerstejaars studenten uit het vorige collegejaar die niet zijn uitgevallen gedurende dat jaar. Met deze resultaten wil hij onderzoeken of er een effect is van de onderwijsperiodes op het wel of niet hebben van herkansingen voor de eerstejaars studenten.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen effect van de onderwijsperiode op het wel of niet hebben van herkansingen voor eerstejaars studenten.
# 
# *H~A~*: Er is een effect van de onderwijsperiode op het wel of niet hebben van herkansingen voor eerstejaars studenten.
# </div>
# 
# # Assumpties
# 
# Om *Cochran's Q toets* uit te voeren, moeten de data aan een aantal voorwaarden voldoen. Er dient een categorische afhankelijke variabele te zijn met twee categorieën zonder overlap: elke observatie past slechts in een van beide categorieën. Daarnaast zijn er drie of meer herhaalde metingen van één groep of zijn er drie of meer gepaarde groepen. In beide gevallen zijn de deelnemers[^11] een willekeurige steekproef van de populatie.[^3]
# 
# *Cochran's Q toets* is te gebruiken wanneer het product van het aantal deelnemers en het aantal herhaalde metingen groter dan of gelijk aan 24 is.[^4] Gebruik de exacte versie van *Cochran's Q toets* wanneer dit niet het geval is.[^5]
# 
# # Post-hoc toetsen
# 
# <!-- ## TEKSTBLOK: PH1.py -->
# *Cochran's Q toets* toetst of er verschillen zijn tussen een percentage op drie of meer herhaalde metingen. Voer een post-hoc toets uit om te bepalen welke metingen van elkaar verschillen. Gebruik de [McNemar toets](12-McNemar-toets-Python.html) of de exacte [McNemar toets](12-McNemar-toets-Python.html) als post-hoc toets.[^6]
# <!-- ## /TEKSTBLOK: PH1.py -->
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout.[^9] Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^9]

# # De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken1.py -->
# Er is een dataset ingeladen genaamd `dfHerkansingen_kunstmatige_intelligentie`. In deze dataset is per onderwijsperiode aangegeven of een student wel of geen herkansingen heeft gemaakt.
# <!-- ## /TEKSTBLOK: Data-bekijken1.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.py -->

# In[ ]:


import pandas as pd

dfHerkansingen_kunstmatige_intelligentie = pd.DataFrame(r.Herkansingen_kunstmatige_intelligentie)


# In[ ]:


## Importeer nuttige packages
import numpy as np
import pandas as pd

## Eerste 5 observaties
print(dfHerkansingen_kunstmatige_intelligentie.head(5))


# In[ ]:


## Laatste 5 observaties
print(dfHerkansingen_kunstmatige_intelligentie.tail(5))


# <!-- ## /OPENBLOK: Data-bekijken2.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.py -->
# Een kruistabel geeft weer hoeveel eerstejaars studenten wel of geen herkansingen hebben in de vier onderwijsperiodes. Maak de kruistabel met de functie `.crosstab()` van het package `pandas` met als argumenten de variabele `dfHerkansingen_kunstmatige_intelligentie['Herkansingen']` die aangeeft of eerstejaars studenten wel of geen herkansing hebben en de variabele `dfHerkansingen_kunstmatige_intelligentie['Onderwijsperiode']` die aangeeft in welke onderwijsperiode een observatie is gedaan.
# 
# <!-- ## /TEKSTBLOK: Data-kruistabel1.py -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.py -->

# In[ ]:


## Maak een kruistabel
Herkansingen_kruistabel = pd.crosstab(dfHerkansingen_kunstmatige_intelligentie['Herkansingen'], dfHerkansingen_kunstmatige_intelligentie['Onderwijsperiode'])

## Print de kruistabel 
print(Herkansingen_kruistabel)

## Print een tabel met proporties, tweede argument 'columns' zorgt ervoor dat de 
## proporties per kolom berekend worden
Prop_Herkansingen_kruistabel =  pd.crosstab(dfHerkansingen_kunstmatige_intelligentie['Herkansingen'], dfHerkansingen_kunstmatige_intelligentie['Onderwijsperiode'], normalize = 'columns')

## Print de tabel met proporties
print(Prop_Herkansingen_kruistabel)


# <!-- ## /OPENBLOK: Data-kruistabel2.py -->
# 
# <!-- ## CLOSEDBLOK: Data-kruistabel3.py -->
# 
# <!-- ## /CLOSEDBLOK: Data-kruistabel3.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel4.py -->
# De kruistabel en bijbehorende tabel met proporties laten zien dat het aantal eerstejaars studenten dat een herkansing doet in onderwijsperiode 1 (`r py$Herkansingen_kruistabel[1,1]`) relatief laag is en relatief hoog is in onderwijsperiode 2 (`r py$Herkansingen_kruistabel[1,2]`). Onderwijsperiode 3 en 4 (`r py$Herkansingen_kruistabel[1,3]` en `r py$Herkansingen_kruistabel[1,4]`) zitten qua aantal herkansende eerstejaars studenten ertussenin.
# <!-- ## /TEKSTBLOK: Data-kruistabel4.py -->
# 
# # Uitvoering
# 
# ## Assumptie steekproefgrootte
# 
# Een assumptie van *Cochran's Q toets* is dat het product van het aantal deelnemers en het aantal herhaalde metingen groter dan of gelijk is aan 24. In deze casus gaat het om het product van het aantal eerstejaars studenten en het aantal onderwijsperiodes. Toets deze assumpties door dit product te berekenen.
# 
# <!-- ## OPENBLOK: steekproefgrootte1.py -->

# In[ ]:


# Bereken het aantal eerstejaars studenten
N = len(set(dfHerkansingen_kunstmatige_intelligentie['Studentnummer']))

# Bereken het aantal onderwijsperiodes
k = len(set(dfHerkansingen_kunstmatige_intelligentie['Onderwijsperiode']))

# Bereken het product van beide
Product = N * k

# Print het resultaat
print(Product)


# <!-- ## /OPENBLOK: steekproefgrootte1.py -->
# 
# <!-- ## TEKSTBLOK: steekproefgrootte2.py -->
# Het product van het aantal eerstejaars studenten en het aantal onderwijsperiodes is `r py$Product`. Aangezien dit aantal groter dan 24 is, is aan de assumptie wat betreft de steekproefgrootte voldaan.
# <!-- ## /TEKSTBLOK: steekproefgrootte2.py -->

# ## Cochran's Q toets
# <!-- ## TEKSTBLOK: Cochran1.py -->
# Voer *Cochran's Q toets* uit om te onderzoeken of er effect is van de onderwijsperiodes op het wel of niet hebben van herkansingen van eerstejaars studenten van de bachelor Kunstmatige Intelligentie. Maak eerst een numerieke variabele voor de variabele Herkansingen met de functie `np.where()` van het package `numpy`. Zet daarna de dataset om in een wijd formaat met behulp van de functie `pd.pivot_table()` van het package `pandas`. Op deze manier ontstaat een nieuwe dataset `dfHerkansingen_kunstmatige_intelligentie_wijd` met in de eerste kolom de studentnummers en in de tweede kolom een numerieke indicator die aangeeft of de student wel of geen herkansing heeft in onderwijsperiode 1 waarbij de variabele de waarde 1 heeft als de student wel een herkansing heeft en de waarde 0 heeft als de student geen herkansing heeft. De kolommen 3, 4 en 5 zijn hetzelfde als kolom 2, maar dan voor onderwijsperiode 2, 3 en 4.
# 
# Voer ten slotte *Cochran's Q toets* uit met behulp van de functie `sms.contingency_tables.cochrans_q()` van het package `statsmodels.stats` met als argumenten de wijde dataset `dfHerkansingen_kunstmatige_intelligentie_wijd` en `return_object = True` om de output overzichtelijk weer te geven.
# <!-- ## /TEKSTBLOK: Cochran1.py -->
# 
# <!-- ## OPENBLOK: Cochran2.py -->

# In[ ]:


import statsmodels.stats as sms

## Maak numeriek
dfHerkansingen_kunstmatige_intelligentie['Herkansingen_dummy'] = np.where(dfHerkansingen_kunstmatige_intelligentie['Herkansingen'] == 'ja', 1, 0)

## Maak dataset wijd
dfHerkansingen_kunstmatige_intelligentie_wijd = pd.pivot_table(data = dfHerkansingen_kunstmatige_intelligentie, index='Studentnummer', columns='Onderwijsperiode', values='Herkansingen_dummy')

# Voer Cochran's Q toets uit
Cochrans_Q  = sms.contingency_tables.cochrans_q(dfHerkansingen_kunstmatige_intelligentie_wijd, return_object = True)
print(Cochrans_Q)


# <!-- ## /OPENBLOK: Cochran2.py -->
# 
# <!-- ## CLOSEDBLOK: Cochran3.py -->

# In[ ]:


## Maak numeriek
dfHerkansingen_kunstmatige_intelligentie['Herkansingen_dummy'] = np.where(dfHerkansingen_kunstmatige_intelligentie['Herkansingen'] == 'ja', 1, 0)

## Maak dataset wijd
dfHerkansingen_kunstmatige_intelligentie_wijd = pd.pivot_table(data = dfHerkansingen_kunstmatige_intelligentie, index='Studentnummer', columns='Onderwijsperiode', values='Herkansingen_dummy')

# Voer Cochran's Q toets uit
stat, pval, df  = sms.contingency_tables.cochrans_q(dfHerkansingen_kunstmatige_intelligentie_wijd, return_object = False)


# <!-- ## /CLOSEDBLOK: Cochran3.py -->
# 
# <!-- ## TEKSTBLOK: Cochran4.py -->
# * Q (`r py$df`, *N* = `r py$N`) = `r Round_and_format(py$stat)`, *p* = `r Round_and_format(py$pval, 3)`
# * Aantal vrijheidsgraden is gelijk aan aantal herhaalde metingen minus één, in deze casus `r py$k` - 1 = `r py$df`
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^10]
# * Er is een significant effect van de vier onderwijsperiodes op het wel of niet hebben van herkansingen van eerstejaars studenten van de bachelor Kunstmatige Intelligentie
# 
# <!-- ## /TEKSTBLOK: Cochran4.py -->

# ## Post-hoc toets
# 
# <!-- ## TEKSTBLOK: posthoc1.py -->
# Voer post-hoc toetsen uit om te onderzoeken tussen welke onderwijsperiodes er verschillen zijn in de verdeling van de eerstejaars studenten die wel of geen herkansingen hebben. Gebruik de [McNemar toets](12-McNemar-toets-Python.html) als post-hoc toets. Maak eerst een aparte variabele aan voor iedere onderwijsperiode waarin is aangegeven of een student wel of geen herkansing heeft gehad in die periode. Gebruik daarna om een [McNemar toets](12-McNemar-toets-Python.html) uit te voeren de zelfgeschreven[^12] functie `McNemar_toets()` met als argumenten de te vergelijken onderwijsperiodes (bijvoorbeeld `P1` en `P2`) en het argument `'mid'` om aan te geven dat de *mid p-value* methode gebruikt moet worden. 
# 
# Voer de [McNemar toets](12-McNemar-toets-Python.html) uit voor alle zes de combinaties van onderwijsperiodes. Hiervoor is het nodig om handmatig een correctie uit te voeren voor meerdere toetsen. Voer de Bonferroni correctie uit door het significantieniveau te delen door het aantal uitgevoerde toetsen. Het significatieniveau voor deze post-hoc toetsen wordt dan 0,05 / 6 ≈ 0,008. Vergelijk de p-waarden van de [McNemar toetsen](12-McNemar-toets-Python.html) daarna met dit significantieniveau.
# <!-- ## /TEKSTBLOK: posthoc1.py -->
# 
# <!-- ## OPENBLOK: posthoc2.py -->

# In[ ]:


## Importeer het package scipy.stats
import scipy.stats as sps
import numpy as np
import pandas as pd

## Maak voor elke onderwijsperiode een variabele
P1 = np.array(dfHerkansingen_kunstmatige_intelligentie_wijd['1'])
P2 = np.array(dfHerkansingen_kunstmatige_intelligentie_wijd['2'])
P3 = np.array(dfHerkansingen_kunstmatige_intelligentie_wijd['3'])
P4 = np.array(dfHerkansingen_kunstmatige_intelligentie_wijd['4'])

## Maak een frequentiematrix

## Definieer een functie om de mid p-waarde of de exacte p-waarde voor de McNemar toets te berekenen
def McNemar_toets(Variabele_1, Variabele_2, p_waarde):
  
  ## Maak een frequentiematrix
  Frequentiematrix =  np.array(pd.crosstab(Variabele_1, Variabele_2))

  ## Sla de niet-diagonale elementen op
  n12 = Frequentiematrix[0,1]
  n21 = Frequentiematrix[1,0]
  
  ## Bereken de som van de niet-diagonale elementen
  n = n12 + n21
  
  ## Bepaal het minimum van beide niet-diagonale elementen 
  n_min = min(n12,n21)
  
  ## Bereken de p-waarde als beide elementen gelijk zijn
  if n12 == n21:
    exact_p_value
    mid_p_value = 1 - sps.binom.pmf(n_min, n, 0.5)

  ## Bereken de p-waarde als beide elementen niet gelijk zijn
  else:
    exact_p_value = 2 * sps.binom.cdf(n_min, n, 0.5)
    mid_p_value = exact_p_value - sps.binom.pmf(n_min, n, 0.5)
  
  ## Retourneer de juiste p-waarde op basis van de gekozen methode
  if p_waarde == 'exact':
    return exact_p_value
  if p_waarde == 'mid':
    return mid_p_value

## Voer de McNemar toets uit voor elke combinatie van onderwijsperiodes
print(McNemar_toets(P1, P2, 'mid'))
print(McNemar_toets(P1, P3, 'mid'))
print(McNemar_toets(P1, P4, 'mid'))
print(McNemar_toets(P2, P3, 'mid'))
print(McNemar_toets(P2, P4, 'mid'))
print(McNemar_toets(P3, P4, 'mid'))


# <!-- ## /OPENBLOK: posthoc2.py -->
# 
# <!-- ## CLOSEDBLOK: posthoc3.py -->

# In[ ]:


## Importeer het package scipy.stats
import scipy.stats as sps
import numpy as np
import pandas as pd

P1 = np.array(dfHerkansingen_kunstmatige_intelligentie_wijd['1'])
P2 = np.array(dfHerkansingen_kunstmatige_intelligentie_wijd['2'])
P3 = np.array(dfHerkansingen_kunstmatige_intelligentie_wijd['3'])
P4 = np.array(dfHerkansingen_kunstmatige_intelligentie_wijd['4'])

## Maak een frequentiematrix

## Definieer een functie om de mid p-waarde of de exacte p-waarde voor de McNemar toets te berekenen
def McNemar_toets(Variabele_1, Variabele_2, p_waarde):
  
  ## Maak een frequentiematrix
  Frequentiematrix =  np.array(pd.crosstab(Variabele_1, Variabele_2))

  ## Sla de niet-diagonale elementen op
  n12 = Frequentiematrix[0,1]
  n21 = Frequentiematrix[1,0]
  
  ## Bereken de som van de niet-diagonale elementen
  n = n12 + n21
  
  ## Bepaal het minimum van beide niet-diagonale elementen 
  n_min = min(n12,n21)
  
  ## Bereken de p-waarde als beide elementen gelijk zijn
  if n12 == n21:
    exact_p_value
    mid_p_value = 1 - sps.binom.pmf(n_min, n, 0.5)

  ## Bereken de p-waarde als beide elementen niet gelijk zijn
  else:
    exact_p_value = 2 * sps.binom.cdf(n_min, n, 0.5)
    mid_p_value = exact_p_value - sps.binom.pmf(n_min, n, 0.5)
  
  ## Retourneer de juiste p-waarde op basis van de gekozen methode
  if p_waarde == 'exact':
    return exact_p_value
  if p_waarde == 'mid':
    return mid_p_value

## Voer de McNemar toets uit voor elke combinatie van onderwijsperiodes
Pval_P1_P2 = McNemar_toets(P1, P2, 'mid')


# <!-- ## /CLOSEDBLOK: posthoc3.py -->
# 
# <!-- ## TEKSTBLOK: posthoc4.py -->
# * Er is een significant verschil gevonden in de verdeling van eerstejaars studenten wat betreft herkansingen  tussen onderwijsperiode 1 en onderwijsperiode 2 (*p* = `r Round_and_format(py$Pval_P1_P2, 3)`)
# * Er zijn geen significante verschillen gevonden bij de overige vergelijkingen tussen onderwijsperiodes
# 
# <!-- ## /TEKSTBLOK: posthoc4.py -->
# 

# # Rapportage
# <!-- ## CLOSEDBLOK: rapportage1.py -->
# <!-- ## /CLOSEDBLOK: rapportage1.py -->
# 
# <!-- ## TEKSTBLOK: rapportage2.py -->
# *Cochran's Q toets* is uitgevoerd om te onderzoeken of er een effect is van de vier onderwijsperiodes op het wel of niet hebben van herkansingen van eerstejaars studenten van de bachelor Kunstmatige Intelligentie. Het percentage eerstejaars studenten dat een of meerdere herkansingen heeft is per onderwijsperiode weergegeven in Tabel 1. *Cochran's Q toets* toont aan dat er een significant effect is van de onderwijsperiodes op het wel of niet hebben van herkansingen, Q (`r py$df`, *N* = `r py$N`) = `r Round_and_format(py$stat)`, *p* = `r Round_and_format(py$pval, 3)`. 
# 
# Om te bepalen tussen welke onderwijsperiodes er verschillen zijn, is de [McNemar toets](12-McNemar-toets-Python.html) als post-hoc toets uitgevoerd met een Bonferroni correctie voor meerdere toetsen. Uit de post-hoc toetsen blijkt dat er alleen een significant verschil is tussen onderwijsperiode 1 (`r Round_and_format(100*py$Prop_Herkansingen_kruistabel[1,1], 1)`% eerstejaars studenten met herkansingen) en onderwijsperiode 2 (`r Round_and_format(100*py$Prop_Herkansingen_kruistabel[1,2], 1)`% eerstejaars studenten met herkansingen) met als p-waarde `r Round_and_format(py$Pval_P1_P2, 3)`. Er zijn dus significant meer eerstejaars studenten met een of meerdere herkansingen in periode 2 in vergelijking tot periode 1, maar verder zijn er geen verschillen tussen de onderwijsperiodes.
# <!-- ## /TEKSTBLOK: rapportage2.py -->
# 

# <!-- ## TEKSTBLOK: rapportage3.py -->
# |                      | Periode 1          | Periode 2          | Periode 3          | Periode 4 |
# |-------------| -------------------- | -------------| ------------|-------------| ------------| 
# |Herkansingen (%) | `r Round_and_format(100*py$Prop_Herkansingen_kruistabel[1,1], 1)` | `r Round_and_format(100*py$Prop_Herkansingen_kruistabel[1,2], 1)` | `r Round_and_format(100*py$Prop_Herkansingen_kruistabel[1,3], 1)` | `r Round_and_format(100*py$Prop_Herkansingen_kruistabel[1,4], 1)` |
# |Geen herkansingen (%) | `r Round_and_format(100*py$Prop_Herkansingen_kruistabel[2,1], 1)` | `r Round_and_format(100*py$Prop_Herkansingen_kruistabel[2,2], 1)` | `r Round_and_format(100*py$Prop_Herkansingen_kruistabel[2,3], 1)` | `r Round_and_format(100*py$Prop_Herkansingen_kruistabel[2,4], 1)` |
# 
# *Tabel 1. Het percentage eerstejaars studenten van de bachelor Kunstmatige Intelligentie dat wel of geen herkansingen heeft voor de vakken in de vier onderwijsperiodes.*
# <!-- ## /TEKSTBLOK: rapportage3.py -->
# 
# 
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Binaire variabelen: twee elkaar uitsluitende waarden, zoals ja of nee, 0 of 1, aan of uit.
# [^2]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^3]: Laerd statistics (2018). *Cochran's Q test using SPSS Statistics*. [Laerd statistics](https://statistics.laerd.com/spss-tutorials/cochrans-q-test-in-spss-statistics.php#assumption4) 
# [^4]: Statistics How To (18 juli 2016). *Cochran’s Q Test*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/cochrans-q-test/).
# [^5]: Er is geen package gevonden om de exacte versie van *Cochran's Q toets* uit te voeren in R. De exacte versie is echter wel uit te voeren in SPSS.
# [^9]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^10]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten. 
# [^11]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^12]: Additional file 1 van Fagerland, M.W., Lydersen, S., & Laake, P. (2013). *The McNemar test for binary matched-pairs data: mid-p and asymptotic are better than exact conditional*. BMC medical research methodology, 13, 91. https://doi.org/10.1186/1471-2288-13-91 . Te vinden op https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3716987/#S1
