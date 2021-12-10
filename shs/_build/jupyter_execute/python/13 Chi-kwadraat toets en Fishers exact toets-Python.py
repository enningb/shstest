#!/usr/bin/env python
# coding: utf-8
---
title: "Chi-kwadraat toets en Fisher's exact toets"
output:
  html_document:
    theme: lumen
    toc: yes
    toc_float: 
      collapsed: FALSE 
    number_sections: true
  keywords: [statistisch handboek, studiedata]
---
# <!-- ## CLOSEDBLOK: Functies.R -->

# In[1]:


library(here)
if (!exists("Substitute_var")) {
  ## Installeer packages en functies
  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)
}


# <!-- ## /CLOSEDBLOK: Functies.R -->
# 
# <style>
# `r htmltools::includeHTML(paste0(here::here(),"/01. Includes/css/Stylesheet_SHHO.css"))`
# </style>
# 
# <!-- ## CLOSEDBLOK: Header.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Header.R -->
# 
# <!-- ## CLOSEDBLOK: Status.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Status.R -->
# 
# <!-- ## CLOSEDBLOK: Reticulate.py -->

# In[ ]:


library(reticulate)
knitr::knit_engines$set(python = reticulate::eng_python)


# <!-- ## /CLOSEDBLOK: Reticulate.py -->
# 
# <!-- ## OPENBLOK: Data-aanmaken.py -->

# In[ ]:


# TODO: Uitleg extra pagina: nominaal, ordinaal etc., afhanjeklijk en onafhankelijk  
# TODO: Uitleg transformeren data 


# In[ ]:


source(paste0(here::here(),"/01. Includes/data/13.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# Gebruik de *Chi-kwadraat toets* of de *Fisher's exact toets* om te toetsen of er een afhankelijkheid bestaat tussen twee ongepaarde, binaire variabelen.[^1]<sup>, </sup>[^2] In tegenstelling tot de *Chi-kwadraat toets* kan de *Fisher's exact toets* ook bij lage aantallen gebruikt worden.[^3] De *Fisher's exact toets* is terughoudender in het benoemen of er een significant verschil is in percentage tussen beide groepen dan de *Chi-kwadraat toets*.[^4]   
# 
# # Onderwijscasus
# <div id = "casus">
# De studentendecaan van een hogeschool vraagt zich af of studenten met een functiebeperking sinds het invoeren van het leenstelsel meer of minder uitvallen.
# 
# *H~0~*: Onder de studenten met een functiebeperking is het percentage uitval na de invoering van het leenstelsel gelijk gebleven.
# 
# *H~A~*: Onder de studenten met een functiebeperking is het percentage uitval na de invoering van het leenstelsel veranderd.
# </div>
# 
# # Assumpties
# Voor een valide resultaat moeten de data aan een aantal voorwaarden voldoen voordat de toets uitgevoerd kan worden. De groepen zijn op nominaal of ordinaal niveau gemeten[^5] en daarmee onafhankelijk van elkaar. 
# 
# ## Groepsgrootte
# Beide testen maken gebruik van een kruistabel; zie tabel 1 voor de geoberveerde waarden van de casus.De *Chi-kwadraat toets* wordt onbetrouwbaar als er een geobserveerde waarde van 10 of lager is.[^6]  

# |                      | uitval   | geen uitval | totaal | 
# | -------------------- | ---------| ------------| -------------| 
# | **geen leenstelsel** |`r Uitval_functiebeperking[1,1]`   | `r Uitval_functiebeperking[1,2]`          | **`r sum(Uitval_functiebeperking[1,1:2])`**|
# | **wel leenstelsel**  |`r Uitval_functiebeperking[2,1]`   | `r Uitval_functiebeperking[2,2]`         | **`r sum(Uitval_functiebeperking[2,1:2])`**|
# |**totaal**            |**`r sum(Uitval_functiebeperking[1:2,1])`**   | **`r sum(Uitval_functiebeperking[1:2,2])`**     | **`r sum(Uitval_functiebeperking)`** |
# *Tabel 1. Geobserveerde waarden casus uitval met of zonder leenstelsel*
# 
# Op basis van geobserveerde waarden kunnen de verwachte waarden berekend worden. In deze casus kan de verwachte waarde van de groep uitgevallen studenten zonder leenstelsel berekend worden door het aantal studenten zonder leenstelsel te vermenigvuldigen met het aantal studenten dat is uitgevallen en de uitkomst te delen door het totaal aantal studenten:
# 
# * aantal studenten zonder leenstelsel: 871   
# * aantal studenten die uitgevallen zijn: 744  
# * totaal aantal studenten: 1634  
# * verwacht aantal uitgevallen studenten zonder leenstelsel: 871*744/1634 ≈ 397, zie tabel 2. 
# 
# |                      | uitval | geen uitval |
# | -------------------- | -------------| ------------| 
# | **geen leenstelsel** | 397      | 474     |
# | **wel leenstelsel**  | 347      | 416     |
# *Tabel 2. Verwachte waarden casus uitval met of zonder leenstelsel*
# 
# Naast onbetrouwbaarheid bij geobserveerde waarden lager dan 10, wordt de *chi-kwadraat toets* ook onbetrouwbaar als één van de verwachte waarden lager dan 5 is. Gebruik in die gevallen de *Fisher’s exact toets*.[^7]  
# 
# # De data bekijken
# <!-- ## TEKSTBLOK: Dataset-inladen.py -->
# Er is een kruistabel `Uitval_functiebeperking` ingeladen over de uitval van studenten met een functiebeperking voor en na de invoering van het leenstelsel. Zowel de variabele voor uitval (wel of geen uitval) als voor functiebeperking (wel of geen functiebeperking) zijn binair. Deze tabel is gebaseerd op een dataset waarin uitval en functiebeperking voor studenten wordt bijgehouden.
# <!-- ## /TEKSTBLOK: Dataset-inladen.py -->
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


get_ipython().run_cell_magic('python', '', 'import pandas as pd\nUitval_functiebeperking = r.Uitval_functiebeperking\nUitval_functiebeperking_n43 = r.Uitval_functiebeperking_n43')


# In[ ]:


get_ipython().run_cell_magic('python', '', 'print(Uitval_functiebeperking)')


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# 
# # Chi-kwadraat toets
# ## Uitvoering
# <!-- ## TEKSTBLOK: Chi2-toets-1.py -->
# De *chi-kwadraat toets* wordt uitgevoerd om de vraag te beantwoorden of het percentage studenten met een functiebeperking dat is uitgevallen voor en na de invoering van het leenstelsel veranderd is. Gebruik `stats.chi2_contingency()` op een kruistabel. De interpretatie van de statitische toets in Python is: `<teststatistiek>, <p-waarde>, <vrijheidsgraad>`.
# <!-- ## /TEKSTBLOK: Chi2-toets-1.py -->
# 
# <!-- ## OPENBLOK: Chi2-toets-2.py -->

# In[ ]:


get_ipython().run_cell_magic('python', '', 'import scipy.stats as stats\ntstat, pval, df, tab = stats.chi2_contingency(Uitval_functiebeperking, correction=True)\nprint(tstat, df, pval)')


# <!-- ## /OPENBLOK: Chi2-toets-2.py -->
# 
# <!-- ## CLOSEDBLOK: Chi2-toets-3.py -->
# 
# <!-- ## /CLOSEDBLOK: Chi2-toets-3.py -->
# 
# <!-- ## TEKSTBLOK: Chi2-toets-4.py -->
# * *χ^2^* ~1~ ≈ `r Round_and_format(py$tstat)`, *p* ≈ `r Round_and_format(py$pval)`  
# * Vrijheidsgraden: *df* = (*k*-1)(*r*-1), waar k staat voor kolom en r voor rij. In dit geval geldt *df* = `r py$df`. De continuïteitscorrectie van Yates wordt automatisch toegepast wanneer het aantal vrijheidsgraden 1 is.[^6]   
# * p-waarde < 0,05, dus de H~0~ wordt verworpen.[^8]  
# 
# <!-- ## /TEKSTBLOK: Chi2-toets-4.py -->
# 
# ## Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# De *Chi-kwadraat toets* is uitgevoerd om te toetsen of studenten met een functiebeperking meer of minder uitvallen sinds de invoering van het leenstelsel. De resultaten ondersteunen de alternatieve hypothese: het percentage uitval van het aantal studenten met een functiebeperking is na de invoering van het leenstelsel veranderd, *χ^2^* ~`r py$df`~ ≈ `r py$pval`, *p* < 0,05.
# 
# <!-- ## /TEKSTBLOK: Rapportage.py -->

# # Fisher's exact toets
# ## Uitvoering 
# <!-- ## TEKSTBLOK: Data-inladen-n43.R -->
# De *Fisher's exact toets* wordt uitgevoerd om de vraag te beantwoorden of het percentage studenten met een functiebeperking dat is uitgevallen voor en na de invoering van het leenstelsel gelijk is gebleven. Deze toets is ook betrouwbaar bij een lage waarde; hierbij een voorbeeld met lage aantallen. Er is een steekproef van `Uitval_functiebeperking` ingeladen genaamd `Uitval_functiebeperking_n43`. 
# <!-- ## /TEKSTBLOK: Data-inladen-n43.R -->
# 
# <!-- ## OPENBLOK: data-bekijken-n43.py -->

# In[ ]:


get_ipython().run_cell_magic('python', '', 'print(Uitval_functiebeperking_n43)')


# <!-- ## /OPENBLOK: data-bekijken-n43.py -->
# 
# De groepen hebben een laag aantal geobserveerde waarden variërend van 5 tot 16. Voer de *Fisher's exact toets* uit.
# 
# <!-- ## OPENBLOK: Fishers-Exact-toets.py -->

# In[ ]:


get_ipython().run_cell_magic('python', '', 'print(stats.fisher_exact(Uitval_functiebeperking_n43))')


# <!-- ## /OPENBLOK: Fishers-Exact-toets.py -->
# 
# <!-- ## CLOSEDBLOK: Fishers-Exact-toets.py -->

# In[ ]:


get_ipython().run_cell_magic('python', '', 'stat, pval = stats.fisher_exact(Uitval_functiebeperking_n43)')


# <!-- ## /CLOSEDBLOK: Fishers-Exact-toets.py -->
# <!-- ## TEKSTBLOK: Fishers-Exact-toets.py -->
# * *p* = `r Round_and_format(py$pval)`; p-waarde > 0,05, dus de H~0~ wordt niet verworpen.[^8]  
# * De odds ratio is 1,8. Dat wil zeggen dat de kans op uitval van studenten met een functiebeperking met leenstelsel 1,8 keer zo groot is als de kans op uitval van studenten met een functiebeperking zonder het leenstelsel. Deze relatie is niet significant, daarom wordt het in het rapport ook niet benoemd.  
# 
# <!-- ## /TEKSTBLOK: Fishers-Exact-toets.py -->
# 
# ## Rapportage 
# De *Fisher's exact toets* is uitgevoerd om te toetsen of studenten met een functiebeperking meer of minder uitvallen sinds de invoering van het leenstelsel. De resultaten ondersteunen de nulhypothese: het percentage uitval van het aantal studenten met een functiebeperking is na de invoering van het leenstelsel gelijk gebleven, *p* > 0,05. 
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Binaire variabelen: twee elkaar uitsluitende waarden, zoals ja of nee, 0 of 1, aan of uit. 
# [^2]: Prabhakaran, S. (2016-2017). *Statistical Tests*. http://r-statistics.co/Statistical-Tests-in-R.html.
# [^3]: Van Geloven, N., & Holman, R., (6 mei 2016). *Fisher's exact toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Fisher's_exact_toets).
# [^4]: Universiteit van Amsterdam (13 november 2017). *Chi-square test*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Chi-square_test#Assumpties). 
# [^5]: Nominaal: variabelen die niet afhankelijk van elkaar zijn en niet op inhoudelijke basis geordend kunnen worden. Voorbeelden hiervan zijn geslacht of achternamen. Een binaire variabele is een voorbeeld van een nominale variabele. Binaire variabelen hebben twee mogelijkheden, ja of nee, terwijl nominale variabelen meerdere mogelijkheden kunnen hebben. 
# [^6]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^7]: Van Geloven, N. (20 augustus 2015). *Chi-kwadraat toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Chi-kwadraat_toets).
# [^8]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
