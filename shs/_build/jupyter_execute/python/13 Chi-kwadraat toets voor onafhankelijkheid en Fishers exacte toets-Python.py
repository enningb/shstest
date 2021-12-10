#!/usr/bin/env python
# coding: utf-8
---
title: "Chi-kwadraat toets voor onafhankelijkheid en Fisher's exacte toets"
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


get_ipython().run_cell_magic('R', '', '# TODO: Uitleg extra pagina: nominaal, ordinaal etc., afhanjeklijk en onafhankelijk  \n# TODO: Uitleg transformeren data ')


# In[ ]:


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/13.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# Gebruik de *Chi-kwadraat toets voor onafhankelijkheid* of de *Fisher's exacte toets* om te toetsen of er een afhankelijkheid bestaat tussen twee ongepaarde, binaire variabelen.[^1]<sup>, </sup>[^2] In tegenstelling tot de *Chi-kwadraat toets voor onafhankelijkheid* kan de *Fisher's exacte toets* ook bij een laag aantal observaties gebruikt worden, dit wordt bij de assumpties toegelicht.[^4] De *Chi-kwadraat toets voor onafhankelijkheid* kan ook gebruikt worden wanneer de twee categorische variabelen meer dan twee categorieën bevatten, maar *Fisher's exacte toets* vereist wel dat beide variabelen binair zijn. Deze toetspagina illustreert de toets echter voor twee ongepaarde binaire variabelen.

# # Onderwijscasus
# <div id = "casus">
# De studentendecaan van een hogeschool vraagt zich af of het invoeren van het leenstelsel van invloed is op het uitvallen van studenten met een functiebeperking. Daarom onderzoekt hij of er een afhankelijkheid is tussen het wel of niet uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen afhankelijkheid tussen het wel of niet uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel.
# 
# *H~A~*: Er is een afhankelijkheid tussen het wel of niet uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel.
# </div>
# 
# # Assumpties
# Voor een valide resultaat moeten de data aan een aantal voorwaarden voldoen voordat de toets uitgevoerd kan worden. De variabelen zijn categorisch (nominaal[^6] of ordinaal[^5]) en de observaties zijn onafhankelijk van elkaar. 
# 
# ## Groepsgrootte
# De *Chi-kwadraat toets voor onafhankelijkheid* heeft een assumptie wat betreft het aantal observaties in een kruistabel. Een kruistabel is een tabel waarin de aantallen observaties worden weergegeven per combinatie van de categorieën van beide variabelen. De kruistabel van de data in de huidige casus is te vinden in Tabel 1.   
# 
# <!-- ## CLOSEDBLOK: Groepsgrootte2.py -->

# In[ ]:


import numpy as np
import pandas as pd

dfUitval_studenten_functiebeperking_leenstelsel = pd.DataFrame(r.Uitval_studenten_functiebeperking_leenstelsel)
dfFisher_Uitval_studenten_functiebeperking_leenstelsel = pd.DataFrame(r.Fisher_Uitval_studenten_functiebeperking_leenstelsel)

dfTabel_uitval_functiebeperking = np.array(r.Tabel_uitval_functiebeperking)
dfFisher_Tabel_uitval_functiebeperking = np.array(r.Fisher_Tabel_uitval_functiebeperking)

#print(dfTabel_uitval_functiebeperking)

# Sla geobserveerde aantallen op
n11 = dfTabel_uitval_functiebeperking[0,0]
n12 = dfTabel_uitval_functiebeperking[0,1]
n21 = dfTabel_uitval_functiebeperking[1,0]
n22 = dfTabel_uitval_functiebeperking[1,1]
NN = np.sum(dfTabel_uitval_functiebeperking)

# Bereken verwachte aantallen
En11 = ((n11 + n12) * (n11 + n21) / NN)
En12 = ((n11 + n12) * (n12 + n22) / NN)
En21 = ((n21 + n22) * (n11 + n21) / NN)
En22 = ((n21 + n22) * (n12 + n22) / NN)
#print(En11)


# <!-- ## /CLOSEDBLOK: Groepsgrootte2.py -->

# <!-- ## TEKSTBLOK: Groepsgrootte1.py -->
# 
# |                      | geen uitval   | uitval | totaal | 
# | -------------------- | ---------| ------------| -------------| 
# | **geen leenstelsel** |`r py$n11`   | `r py$n12`          | **`r py$n11 + py$n12`**|
# | **wel leenstelsel**  |`r py$n21`   | `r py$n22`          | **`r py$n21 + py$n22`**|
# |**totaal**            |**`r py$n11 + py$n21`**   | **`r py$n12 + py$n22`**     | **`r py$NN`** |
# *Tabel 1. Geobserveerde aantallen casus uitval met of zonder leenstelsel*

# De *Chi-kwadraat toets voor onafhankelijkheid* wordt onbetrouwbaar als er in meer dan 20% van de cellen van de kruistabel een verwacht aantal observaties van 5 of lager is. Gebruik in dat geval *Fisher's exact toets*.[^8] Het verwacht aantal observaties in een cel is het aantal observaties dat zich in een cel op basis van kansrekening zou moeten bevinden wanneer er geen afhankelijkheid tussen de twee variabelen is. Op basis van de nulhypothese van onafhankelijkheid tussen de variabelen kunnen de verwachte aantallen observaties in elke cel berekend worden. Een voorbeeldberekening van het verwacht aantal observaties voor de cel linksboven (geen leenstelsel; geen uitval) werkt als volgt: vermenigvuldig het totaal aantal studenten in de groep geen leenstelsel (`r py$n11 + py$n12`) met het totaal aantal studenten dat uitvalt (`r py$n11 + py$n21`) en deel dit door het totaal aantal studenten (`r py$NN`).
# 
# * aantal studenten geen leenstelsel: `r py$n11 + py$n12`   
# * aantal studenten uitval: `r py$n11 + py$n21`  
# * totaal aantal studenten: `r py$NN`
# * verwacht aantal uitgevallen studenten geen leenstelsel: `r py$n11 + py$n12` * `r py$n11 + py$n21` / `r py$NN` ≈ `r Round_and_format((py$n11 + py$n12) * (py$n11 + py$n21) / py$NN)` 
# 
# Alle verwachte aantallen observaties zijn te vinden in Tabel 2. Merk ook op dat de totalen in de rijen en kolommen gelijk zijn aan de totalen in Tabel 1, de kruistabel met de aantallen observaties. Geen van de verwachte aantallen is kleiner of gelijk aan vijf, dus er is voldaan aan de assumptie van groepsgrootte voor de *Chi-kwadraat toets voor onafhankelijkheid*.

# |                      | geen uitval   | uitval | totaal | 
# | -------------------- | ---------| ------------| -------------| 
# | **geen leenstelsel** |`r Round_and_format(py$En11)`   | `r Round_and_format(py$En12)`          | **`r Round_and_format(py$En11 + py$En12)`**|
# | **wel leenstelsel**  |`r Round_and_format(py$En21)`   | `r Round_and_format(py$En22)`          | **`r Round_and_format(py$En21 + py$En22)`**|
# |**totaal**            |**`r Round_and_format(py$En11 + py$En21)`**   | **`r Round_and_format(py$En12 + py$En22)`**     | **`r py$NN`** |
# *Tabel 2. Verwachte aantallen casus uitval met of zonder leenstelsel*
# <!-- ## /TEKSTBLOK: Groepsgrootte1.py -->

# # Effectmaat
# 
# De p-waarde geeft aan of een (mogelijk) verschil tussen twee groepen statistisch significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^7] 
# De *Chi-kwadraat toets voor onafhankelijkheid* heeft als effectmaat Cohen's *w*.[^9] Een indicatie om Cohen's *w* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^10]
# 
# De odds ratio is een andere effectmaat die voor zowel de *Chi-kwadraat toets voor onafhankelijkheid* als de *Fisher's exacte toets* kan worden gebruikt. Een voorwaarde is echter dat beide variabelen binair zijn. In andere woorden, er moet een 2x2 kruistabel gevormd kunnen worden. Odds is een Engelse term voor de verhouding van twee kansen, bijvoorbeeld de verhouding tussen het aantal studenten dat uitvalt en niet uitvalt. Een odds ratio is de verhouding tussen twee odds, dus de verhouding van de odds van studentenuitval voor de periode met leenstelsel en de periode zonder leenstelsel. De odds ratio geeft dus een interpretatie van het effect van een leenstelsel op het uitvallen van studenten.[^7]

# # De data bekijken
# 
# <!-- ## TEKSTBLOK: Data-bekijken1.py -->
# Er is een dataset ingeladen genaamd `dfUitval_studenten_functiebeperking_leenstelsel`. In deze dataset is voor elke student met een functiebeperking aangegeven of ze studeerden voor of na invoering van het leenstelsel en of ze wel of niet uitgevallen zijn.
# <!-- ## /TEKSTBLOK: Data-bekijken1.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.py -->

# In[ ]:


## Importeer nuttige packages
import numpy as np
import pandas as pd
## Eerste 5 observaties
print(dfUitval_studenten_functiebeperking_leenstelsel.head(5))


# In[ ]:


## Laatste 5 observaties
print(dfUitval_studenten_functiebeperking_leenstelsel.tail(5))


# <!-- ## /OPENBLOK: Data-bekijken2.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.py -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Periode` en `Uitval`. Maak de kruistabel met de functie `.crosstab()` van het package `pandas` met als argumenten de variabele `dfUitval_studenten_functiebeperking_leenstelsel['Periode']` (voor of na invoering leenstelsel) en `dfUitval_studenten_functiebeperking_leenstelsel['Uitval']` (wel of niet uitgevallen).
# <!-- ## /TEKSTBLOK: Data-kruistabel1.py -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.py -->

# In[ ]:


# Maak een kruistabel
Uitval_studenten_kruistabel =  pd.crosstab(dfUitval_studenten_functiebeperking_leenstelsel['Periode'], dfUitval_studenten_functiebeperking_leenstelsel['Uitval'])

# Print de kruistabel
print(Uitval_studenten_kruistabel)

# Maak een tabel met proporties, argument 'normalize = index' zorgt ervoor dat de proporties
# per rij berekend worden
Prop_Uitval_studenten_kruistabel = pd.crosstab(dfUitval_studenten_functiebeperking_leenstelsel['Periode'], dfUitval_studenten_functiebeperking_leenstelsel['Uitval'], normalize = 'index')

# Print de tabel met proporties
print(Prop_Uitval_studenten_kruistabel)


# In[ ]:


voor = np.array(Prop_Uitval_studenten_kruistabel)[0,1]
na = np.array(Prop_Uitval_studenten_kruistabel)[1,1]


# <!-- ## /OPENBLOK: Data-kruistabel2.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel3.py -->
# De kruistabel en bijbehorende tabel met proporties laat zien dat het percentage uitgevallen studenten hoger is na invoering van het leenstelsel (`r Round_and_format(100 *py$voor)`%) dan voor invoering van het leenstelsel (`r Round_and_format(100 * py$na)`%).
# <!-- ## /TEKSTBLOK: Data-kruistabel3.py -->

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: Assumptie.py -->
# Toets de assumptie dat niet meer dan 20% van de verwachte aantallen observaties gelijk of kleiner dan vijf is. Bereken het verwacht aantal observaties met de functie `.contingency.expected_freq()` van het `scipy.stats` package met als argument de kruistabel `Uitval_studenten_kruistabel`.
# <!-- ## /TEKSTBLOK: Assumptie.py -->
# 
# <!-- ## OPENBLOK: Assumptie1.py -->

# In[ ]:


import scipy.stats as sps 
# Maak een kruistabel
Uitval_studenten_kruistabel = pd.crosstab(dfUitval_studenten_functiebeperking_leenstelsel['Periode'], dfUitval_studenten_functiebeperking_leenstelsel['Uitval'])

# Bereken verwachte aantallen observaties
sps.contingency.expected_freq(Uitval_studenten_kruistabel)


# <!-- ## /OPENBLOK: Assumptie1.py -->
# 
# Geen van de verwachte aantallen observaties is gelijk aan of kleiner dan vijf, dus de *Chi-kwadraat toets voor onafhankelijkheid* kan worden uitgevoerd.

# # Chi-kwadraat toets voor onafhankelijkheid
# ## Uitvoering
# <!-- ## TEKSTBLOK: Chi2-toets-1.py -->
# De *Chi-kwadraat toets voor onafhankelijkheid* wordt uitgevoerd om de vraag te beantwoorden of er een afhankelijkheid is tussen het uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel. Gebruik de functie `.stats.chi2_contingency()` van het `scipy` package met als argument de kruistabel `Uitval_studenten_kruistabel`. De weergegeven output bevat de teststatistiek, de p-waarde, het aantal vrijheidsgraden en een aantal met de verwachte aantallen observaties (in deze volgorde).
# <!-- ## /TEKSTBLOK: Chi2-toets-1.py -->
# 
# <!-- ## OPENBLOK: Chi2-toets-2.py -->

# In[ ]:


import scipy.stats as sps
sps.chi2_contingency(Uitval_studenten_kruistabel)


# <!-- ## /OPENBLOK: Chi2-toets-2.py -->
# 
# Bereken de effectmaat Cohen's *w* vervolgens op basis van de &chi;^2^-waarde van de *Chi-kwadraat toets voor onafhankelijkheid*.
# <!-- ## OPENBLOK: Chi2-toets-3.py -->

# In[ ]:


# Sla de teststatistiek op
chi2, pval, df, tab = sps.chi2_contingency(Uitval_studenten_kruistabel)

# Bereken het totaal aantal observaties als som van de kruistabel
N = np.sum(np.array(Uitval_studenten_kruistabel))

# Bereken eta squared
Eta2 = np.sqrt(chi2 / N)

# Print de effectgrootte
print(Eta2)


# <!-- ## /OPENBLOK: Chi2-toets-3.py -->

# <!-- ## CLOSEDBLOK: Chi2-toets-4.py -->
# <!-- ## /CLOSEDBLOK: Chi2-toets-4.py -->
# 
# <!-- ## TEKSTBLOK: Chi2-toets-5.py-->
# * &chi;^2^ ~1~ = `r Round_and_format(py$chi2)`, *p* = `r Round_and_format(py$pval)`, *w* = `r Round_and_format(py$Eta2)`  
# * Vrijheidsgraden: *df* = (*k*-1)(*r*-1), waar *k* staat voor kolom en *r* voor rij. In dit geval geldt *df* = `r Round_and_format(py$df)`.  
# * p-waarde < 0,05, dus de H~0~ wordt verworpen.[^11]
# * Effectmaat is `r Round_and_format(py$Eta2)`, dus een klein effect
# 
# <!-- ## /TEKSTBLOK: Chi2-toets-5.py-->
# 
# ## Rapportage
# 
# <!-- ## CLOSEDBLOK: Rapportage1.py -->

# In[ ]:



# Maak een tabel met proporties, argument 'normalize = index' zorgt ervoor dat de proporties
# per rij berekend worden
Prop_Uitval_studenten_kruistabel = pd.crosstab(dfUitval_studenten_functiebeperking_leenstelsel['Periode'], dfUitval_studenten_functiebeperking_leenstelsel['Uitval'], normalize = 'index')

# Sla vier waarden apart op
gg = np.array(Prop_Uitval_studenten_kruistabel)[0,0]
gu = np.array(Prop_Uitval_studenten_kruistabel)[0,1]
wg = np.array(Prop_Uitval_studenten_kruistabel)[1,0]
wu = np.array(Prop_Uitval_studenten_kruistabel)[1,1]


# <!-- ## /CLOSEDBLOK: Rapportage1.py -->

# <!-- ## TEKSTBLOK: Rapportage2.py -->
# De *Chi-kwadraat toets voor onafhankelijkheid* is uitgevoerd om te toetsen of er een afhankelijkheid is tussen het uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel. De nulhypothese dat uitval en invoering van het leenstelsel onafhankelijk zijn kan verworpen worden, &chi;^2^ ~1~ = `r Round_and_format(py$chi2)`, *p* = `r Round_and_format(py$pval)`, *w* = `r Round_and_format(py$Eta2)`. De propoties per rij in Tabel 3 laten zien dat er relatief meer studenten uitvallen wanneer er een leenstelsel is ingevoerd.
# 
# |                      | geen uitval   | uitval | 
# | -------------------- | ---------| ------------| 
# | **geen leenstelsel** |`r Round_and_format(py$gg)`   | `r Round_and_format(py$gu)`          | 
# | **wel leenstelsel**  |`r Round_and_format(py$wg)`   | `r Round_and_format(py$wu)`          |
# *Tabel 3. Proporties wel of niet uitvallen studenten met of zonder leenstelsel berekend per rij.*
# <!-- ## /TEKSTBLOK: Rapportage2.py -->
# 

# # Fisher's exacte toets
# ## Uitvoering 
# <!-- ## TEKSTBLOK: Data-inladen-Fisher.py -->
# *Fisher's exact toets* wordt uitgevoerd om de vraag te beantwoorden of er een afhankelijkheid is tussen het uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel. Deze toets is ook betrouwbaar bij een laag aantal observaties. Om de toets te illustreren is een subset van de dataset `dfUitval_studenten_functiebeperking_leenstelsel` ingeladen; de subset heet `dfFisher_Uitval_studenten_functiebeperking_leenstelsel`.
# 
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Periode` en `Uitval`. Maak de kruistabel met de functie `.crosstable()` van het package `pandas` met als argumenten de variabele `dfUitval_studenten_functiebeperking_leenstelsel['Periode']` (voor of na invoering leenstelsel) en `dfUitval_studenten_functiebeperking_leenstelsel['Uitval']` (wel of niet uitgevallen).
# <!-- ## /TEKSTBLOK: Data-inladen-Fisher.py -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2Fisher.py -->

# In[ ]:


import pandas as pd

# Maak een kruistabel
Fisher_Uitval_studenten_kruistabel =  pd.crosstab(dfFisher_Uitval_studenten_functiebeperking_leenstelsel['Periode'], dfFisher_Uitval_studenten_functiebeperking_leenstelsel['Uitval'])

# Print de kruistabel
print(Fisher_Uitval_studenten_kruistabel)

# Maak een tabel met proporties, argument 'normalize = index' zorgt ervoor dat de proporties
# per rij berekend worden
Fisher_Prop_Uitval_studenten_kruistabel = pd.crosstab(dfFisher_Uitval_studenten_functiebeperking_leenstelsel['Periode'], dfFisher_Uitval_studenten_functiebeperking_leenstelsel['Uitval'], normalize = 'index')

# Print de tabel met proporties
print(Fisher_Prop_Uitval_studenten_kruistabel)


# In[ ]:


voor = np.array(Fisher_Prop_Uitval_studenten_kruistabel)[0,1]
na = np.array(Fisher_Prop_Uitval_studenten_kruistabel)[1,1]


# <!-- ## /OPENBLOK: Data-kruistabel2Fisher.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel3Fisher.py -->
# De kruistabel en bijbehorende tabel met proporties laat zien dat het percentage uitgevallen studenten lager is na invoering van het leenstelsel (`r Round_and_format(100 * py$na)`%) dan voor invoering van het leenstelsel (`r Round_and_format(100 * py$voor)`%).
# <!-- ## /TEKSTBLOK: Data-kruistabel3Fisher.py -->

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: AssumptieFisher.py -->
# Toets de assumptie dat niet meer dan 20% van de verwachte aantallen observaties gelijk of kleiner dan vijf is. Bereken het verwachte aantal observaties met de functie `.contingency.expected_freq()` van het `scipy.stats` package met als argument de kruistabel `Fisher_Uitval_studenten_kruistabel`.
# <!-- ## /TEKSTBLOK: AssumptieFisher.py -->
# 
# <!-- ## OPENBLOK: Assumptie1Fisher.py -->

# In[ ]:


import scipy.stats as sps 
# Maak een kruistabel
Fisher_Uitval_studenten_kruistabel = pd.crosstab(dfFisher_Uitval_studenten_functiebeperking_leenstelsel['Periode'], dfFisher_Uitval_studenten_functiebeperking_leenstelsel['Uitval'])

# Bereken verwachte aantallen observaties
sps.contingency.expected_freq(Fisher_Uitval_studenten_kruistabel)


# <!-- ## /OPENBLOK: Assumptie1Fisher.py -->
# 
# Een van de verwachte aantallen observaties is kleiner dan vijf, dus de *Chi-kwadraat toets voor onafhankelijkheid* kan niet worden uitgevoerd. *Fisher's exacte toets* moet inderdaad gebruikt worden voor deze dataset.

# ## Fisher's exacte toets
# 
# <!-- ## TEKSTBLOK: Fisher1.py -->
# Voer *Fisher's exact toets* uit met de functie `.fisher_exact()` van het package `scipy.stats` met als argumenten de kruistabel `Fisher_Uitval_studenten_kruistabel` en `alternative = 'two-sided'` om tweezijdig te toetsen. De output geeft de odds ratio en de p-waarde weer.
# <!-- ## /TEKSTBLOK: Fisher1.py -->

# <!-- ## OPENBLOK: Fishers-Exact-toets.py -->

# In[ ]:


import scipy.stats as sps
sps.fisher_exact(Fisher_Uitval_studenten_kruistabel, alternative = 'two-sided')


# <!-- ## /OPENBLOK: Fishers-Exact-toets.py -->

# <!-- ## CLOSEDBLOK: Fishers-Exact-toets.py -->

# In[ ]:


OR, pval = sps.fisher_exact(Fisher_Uitval_studenten_kruistabel, alternative = 'two-sided')


# <!-- ## /CLOSEDBLOK: Fishers-Exact-toets.py -->
# 
# <!-- ## TEKSTBLOK: Fishers-Exact-toets.py -->
# * *p* = `r Round_and_format(py$pval)`; p-waarde > 0,05, dus de H~0~ wordt niet verworpen.[^11]  
# * De odds ratio is `r Round_and_format(py$OR)`. De kans op uitval van studenten met een functiebeperking met leenstelsel is dus `r Round_and_format(py$OR)` keer zo groot is als de kans op uitval van studenten met een functiebeperking zonder het leenstelsel. Deze relatie is echter niet significant.
# 
# <!-- ## /TEKSTBLOK: Fishers-Exact-toets.py -->
# 

# ## Rapportage
# 
# <!-- ## CLOSEDBLOK: Rapportage1Fisher.py -->

# In[ ]:


# Maak een tabel met proporties, argument 'normalize = index' zorgt ervoor dat de proporties
# per rij berekend worden
Fisher_Prop_Uitval_studenten_kruistabel = pd.crosstab(dfFisher_Uitval_studenten_functiebeperking_leenstelsel['Periode'], dfFisher_Uitval_studenten_functiebeperking_leenstelsel['Uitval'], normalize = 'index')

# Sla vier waarden apart op
fgg = np.array(Fisher_Prop_Uitval_studenten_kruistabel)[0,0]
fgu = np.array(Fisher_Prop_Uitval_studenten_kruistabel)[0,1]
fwg = np.array(Fisher_Prop_Uitval_studenten_kruistabel)[1,0]
fwu = np.array(Fisher_Prop_Uitval_studenten_kruistabel)[1,1]


# <!-- ## /CLOSEDBLOK: Rapportage1Fisher.py -->

# <!-- ## TEKSTBLOK: Rapportage2Fisher.py -->
# *Fisher's exact toets* is uitgevoerd om te toetsen of er een afhankelijkheid is tussen het uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel. De nulhypothese dat uitval en invoering van het leenstelsel onafhankelijk zijn kan niet verworpen worden, *p* = `r py$pval`. De proporties per rij in Tabel 4 laten zien dat er relatief meer studenten uitvallen wanneer er een leenstelsel is ingevoerd, dit verschil is echter niet significant.
# 
# |                      | geen uitval   | uitval | 
# | -------------------- | ---------| ------------| 
# | **geen leenstelsel** |`r Round_and_format(py$fgg)`   | `r Round_and_format(py$fgu)`          | 
# | **wel leenstelsel**  |`r Round_and_format(py$fwg)`   | `r Round_and_format(py$fwu)`          |
# *Tabel 4. Proporties wel of niet uitvallen studenten met of zonder leenstelsel berekend per rij voor dataset Fisher's exact toets.*
# <!-- ## /TEKSTBLOK: Rapportage2Fisher.py -->
# 
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Binaire variabelen: twee elkaar uitsluitende waarden, zoals ja of nee, 0 of 1, aan of uit. 
# [^2]: Prabhakaran, S. (2016-2017). *Statistical Tests*. http://r-statistics.co/Statistical-Tests-in-R.html.
# [^4]: Van Geloven, N., & Holman, R., (6 mei 2016). *Fisher's exact toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Fisher's_exact_toets).
# [^5]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^6]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# [^7]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^8]: Van Geloven, N. (20 augustus 2015). *Chi-kwadraat toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Chi-kwadraat_toets).
# [^9]: De effectmaat Cohen's *w* wordt voor de *Chi-kwadraat toets* berekend door de wortel te nemen van de
# &chi;^2^-waarde gedeeld door het totaal aantal observaties, i.e. $\sqrt{ \frac{\chi^2}{N} }$.
# [^10]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^11]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.

# <!-- ## TEKSTBLOK: Extra-Bron.py -->
# [^12]: Het 95%-betrouwbaarheidsinterval van de odds ratio wordt bij deze Python functie niet weergegeven. Bij de uitvoering van *Fisher's exact toets* in R zit het betrouwbaarheidsinterval wel in de output.
# <!-- ## /TEKSTBLOK: Extra-Bron.py -->
# NA
# <!-- ## /TEKSTBLOK: Extra-Bron.R -->
