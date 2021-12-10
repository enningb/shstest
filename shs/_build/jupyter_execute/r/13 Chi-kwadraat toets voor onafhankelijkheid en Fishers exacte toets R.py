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


library(here)
if (!exists("Substitute_var")) {
  ## Installeer packages en functies
  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)
}


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





# <!-- ## /CLOSEDBLOK: Header.R -->
# 
# <!-- ## CLOSEDBLOK: Status.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Status.R -->
# 
# <!-- ## CLOSEDBLOK: Reticulate.R -->
# 
# <!-- ## /CLOSEDBLOK: Reticulate.R -->
# 
# <!-- ## OPENBLOK: Data-aanmaken.R -->

# In[ ]:


# TODO: Uitleg extra pagina: nominaal, ordinaal etc., afhankelijk en onafhankelijk  
# TODO: Uitleg transformeren data 


# In[ ]:


source(paste0(here::here(),"/01. Includes/data/13.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
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
# <!-- ## CLOSEDBLOK: Groepsgrootte2.R -->

# In[ ]:


# Sla geobserveerde aantallen op
n11 <- Tabel_uitval_functiebeperking[1,1]
n12 <- Tabel_uitval_functiebeperking[1,2]
n21 <- Tabel_uitval_functiebeperking[2,1]
n22 <- Tabel_uitval_functiebeperking[2,2]
NN <- sum(Tabel_uitval_functiebeperking)

# Bereken verwachte aantallen
En11 <- ((n11 + n12) * (n11 + n21) / NN)
En12 <- ((n11 + n12) * (n12 + n22) / NN)
En21 <- ((n21 + n22) * (n11 + n21) / NN)
En22 <- ((n21 + n22) * (n12 + n22) / NN)


# <!-- ## /CLOSEDBLOK: Groepsgrootte2.R -->

# <!-- ## TEKSTBLOK: Groepsgrootte1.R -->
# 
# |                      | geen uitval   | uitval | totaal | 
# | -------------------- | ---------| ------------| -------------| 
# | **geen leenstelsel** |`r n11`   | `r n12`          | **`r n11 + n12`**|
# | **wel leenstelsel**  |`r n21`   | `r n22`          | **`r n21 + n22`**|
# |**totaal**            |**`r n11 + n21`**   | **`r n12 + n22`**     | **`r NN`** |
# *Tabel 1. Geobserveerde aantallen casus uitval met of zonder leenstelsel*

# De *Chi-kwadraat toets voor onafhankelijkheid* wordt onbetrouwbaar als er in meer dan 20% van de cellen van de kruistabel een verwacht aantal observaties van 5 of lager is. Gebruik in dat geval *Fisher's exacte toets*.[^8] Het verwacht aantal observaties in een cel is het aantal observaties dat zich in een cel op basis van kansrekening zou moeten bevinden wanneer er geen afhankelijkheid tussen de twee variabelen is. Op basis van de nulhypothese van onafhankelijkheid tussen de variabelen kunnen de verwachte aantallen observaties in elke cel berekend worden. Een voorbeeldberekening van het verwacht aantal observaties voor de cel linksboven (geen leenstelsel; geen uitval) werkt als volgt: vermenigvuldig het totaal aantal studenten in de groep geen leenstelsel (`r n11 + n12`) met het totaal aantal studenten dat niet uitvalt (`r n11 + n21`) en deel dit door het totaal aantal studenten (`r NN`).
# 
# * aantal studenten geen leenstelsel: `r n11 + n12`   
# * aantal studenten geen uitval: `r n11 + n21`  
# * totaal aantal studenten: `r NN`
# * verwacht aantal uitgevallen studenten geen leenstelsel: `r n11 + n12` * `r n11 + n21` / `r NN` ≈ `r Round_and_format((n11 + n12) * (n11 + n21) / NN)` 
# 
# Alle verwachte aantallen observaties zijn te vinden in Tabel 2. Merk ook op dat de totalen in de rijen en kolommen gelijk zijn aan de totalen in Tabel 1, de kruistabel met de aantallen observaties. Geen van de verwachte aantallen is kleiner of gelijk aan vijf, dus er is voldaan aan de assumptie van groepsgrootte voor de *Chi-kwadraat toets voor onafhankelijkheid*.

# |                      | geen uitval   | uitval | totaal | 
# | -------------------- | ---------| ------------| -------------| 
# | **geen leenstelsel** |`r Round_and_format(En11)`   | `r Round_and_format(En12)`          | **`r Round_and_format(En11 + En12)`**|
# | **wel leenstelsel**  |`r Round_and_format(En21)`   | `r Round_and_format(En22)`          | **`r Round_and_format(En21 + En22)`**|
# |**totaal**            |**`r Round_and_format(En11 + En21)`**   | **`r Round_and_format(En12 + En22)`**     | **`r NN`** |
# *Tabel 2. Verwachte aantallen casus uitval met of zonder leenstelsel*
# <!-- ## /TEKSTBLOK: Groepsgrootte1.R -->

# # Effectmaat
# 
# De p-waarde geeft aan of een (mogelijk) verschil tussen twee groepen statistisch significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^7] 
# De *Chi-kwadraat toets voor onafhankelijkheid* heeft als effectmaat Cohen's *w*.[^9] Een indicatie om Cohen's *w* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^10]
# 
# De odds ratio is een andere effectmaat die voor zowel de *Chi-kwadraat toets voor onafhankelijkheid* als de *Fisher's exacte toets* kan worden gebruikt. Een voorwaarde is echter dat beide variabelen binair zijn. In andere woorden, er moet een 2x2 kruistabel gevormd kunnen worden. Odds is een Engelse term voor de verhouding van twee kansen, bijvoorbeeld de verhouding tussen het aantal studenten dat uitvalt en niet uitvalt. Een odds ratio is de verhouding tussen twee odds, dus de verhouding van de odds van studentenuitval voor de periode met leenstelsel en de periode zonder leenstelsel. De odds ratio geeft dus een interpretatie van het effect van een leenstelsel op het uitvallen van studenten.[^7]

# # De data bekijken
# 
# <!-- ## TEKSTBLOK: Data-bekijken1.R -->
# Er is een dataset ingeladen genaamd `Uitval_studenten_functiebeperking_leenstelsel`. In deze dataset is voor elke student met een functiebeperking aangegeven of ze studeerden voor of na invoering van het leenstelsel en of ze wel of niet uitgevallen zijn.
# <!-- ## /TEKSTBLOK: Data-bekijken1.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.R -->

# In[ ]:


## Eerste 6 observaties
head(Uitval_studenten_functiebeperking_leenstelsel)

## Laatste 6 observaties
tail(Uitval_studenten_functiebeperking_leenstelsel)


# <!-- ## /OPENBLOK: Data-bekijken2.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Periode` en `Uitval`. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Uitval_studenten_functiebeperking_leenstelsel$Periode` (voor of na invoering leenstelsel) en `Uitval_studenten_functiebeperking_leenstelsel$Uitval` (wel of niet uitgevallen). 
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:



## Maak een kruistabel
Uitval_studenten_kruistabel <- table(Uitval_studenten_functiebeperking_leenstelsel$Periode, Uitval_studenten_functiebeperking_leenstelsel$Uitval)

## Print de kruistabel 
print(Uitval_studenten_kruistabel)

## Print een tabel met proporties, tweede argument 2 zorgt ervoor dat de 
## proporties per rij berekend worden
prop.table(Uitval_studenten_kruistabel, 1)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel3.R -->
# De kruistabel en bijbehorende tabel met proporties laat zien dat het percentage uitgevallen studenten hoger is na invoering van het leenstelsel (`r Round_and_format(100 * prop.table(Uitval_studenten_kruistabel, 1)[2,2])`%) dan voor invoering van het leenstelsel (`r Round_and_format(100 * prop.table(Uitval_studenten_kruistabel, 1)[1,2])`%).
# <!-- ## /TEKSTBLOK: Data-kruistabel3.R -->

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: Assumptie.R -->
# Toets de assumptie dat niet meer dan 20% van de verwachte aantallen observaties gelijk aan of kleiner dan vijf is. Bereken het verwacht aantal observaties met het argument `chisq.test()$expected` van de functie `chisq.test()` met als argumenten de variabelen `Uitval_studenten_functiebeperking_leenstelsel$Periode` (voor of na invoering leenstelsel) en `Uitval_studenten_functiebeperking_leenstelsel$Uitval` (wel of niet uitgevallen). 
# <!-- ## /TEKSTBLOK: Assumptie.R -->
# 
# <!-- ## OPENBLOK: Assumptie1.R -->

# In[ ]:


chisq.test(Uitval_studenten_functiebeperking_leenstelsel$Periode,
           Uitval_studenten_functiebeperking_leenstelsel$Uitval)$expected


# <!-- ## /OPENBLOK: Assumptie1.R -->
# 
# Geen van de verwachte aantallen observaties is gelijk aan of kleiner dan vijf, dus de *Chi-kwadraat toets voor onafhankelijkheid* kan worden uitgevoerd.

# # Chi-kwadraat toets voor onafhankelijkheid
# ## Uitvoering
# <!-- ## TEKSTBLOK: Chi2-toets-1.R -->
# De *Chi-kwadraat toets voor onafhankelijkheid* wordt uitgevoerd om de vraag te beantwoorden of er een afhankelijkheid is tussen het uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel. Gebruik de functie `chisq.test()` met als argumenten de variabelen `Uitval_studenten_functiebeperking_leenstelsel$Periode` (voor of na invoering leenstelsel) en `Uitval_studenten_functiebeperking_leenstelsel$Uitval` (wel of niet uitgevallen). 
# <!-- ## /TEKSTBLOK: Chi2-toets-1.R -->
# 
# <!-- ## OPENBLOK: Chi2-toets-2.R -->

# In[ ]:


chisq.test(Uitval_studenten_functiebeperking_leenstelsel$Periode,
           Uitval_studenten_functiebeperking_leenstelsel$Uitval)


# <!-- ## /OPENBLOK: Chi2-toets-2.R -->
# 
# Bereken de effectmaat Cohen's *w* vervolgens op basis van de &chi;^2^-waarde van de *Chi-kwadraat toets voor onafhankelijkheid*.
# <!-- ## OPENBLOK: Chi2-toets-3.R -->

# In[ ]:


# Sla de teststatistiek op
Chi2_teststatistiek <- chisq.test(Tabel_uitval_functiebeperking)$statistic

# Bereken het totaal aantal observaties als som van de kruistabel
N <- sum(Tabel_uitval_functiebeperking)

# Bereken eta squared
w <- sqrt(Chi2_teststatistiek / N)

# Print de effectgrootte
paste("De effectgrootte is",w)


# <!-- ## /OPENBLOK: Chi2-toets-3.R -->

# <!-- ## CLOSEDBLOK: Chi2-toets-4.R -->

# In[ ]:


Chi2 <- chisq.test(Tabel_uitval_functiebeperking)
vChi2 <- Round_and_format(Chi2$statistic)
vP <- Round_and_format(Chi2$p.value)
vDF <- Chi2$parameter


# <!-- ## /CLOSEDBLOK: Chi2-toets-4.R -->
# 
# <!-- ## TEKSTBLOK: Chi2-toets-5.R-->
# * &chi;^2^ ~1~ = `r vChi2`, *p* = `r vP`, *w* = `r Round_and_format(w)`  
# * Vrijheidsgraden: *df* = (*k*-1)(*r*-1), waar *k* staat voor kolom en *r* voor rij. In dit geval geldt *df* = `r vDF`.  
# * p-waarde < 0,05, dus de H~0~ wordt verworpen.[^11]
# * Effectmaat is `r Round_and_format(w)`, dus een klein effect
# 
# <!-- ## /TEKSTBLOK: Chi2-toets-5.R-->
# 
# ## Rapportage
# 
# <!-- ## CLOSEDBLOK: Rapportage1.R -->

# In[ ]:


## Maak een kruistabel
Uitval_studenten_kruistabel <- table(Uitval_studenten_functiebeperking_leenstelsel$Periode, Uitval_studenten_functiebeperking_leenstelsel$Uitval)

## Print de kruistabel 
print(Uitval_studenten_kruistabel)

## Print een tabel met proporties, tweede argument 2 zorgt ervoor dat de 
## proporties per rij berekend worden
ptable <- prop.table(Uitval_studenten_kruistabel, 1)


# <!-- ## /CLOSEDBLOK: Rapportage1.R -->

# <!-- ## TEKSTBLOK: Rapportage2.R -->
# De *Chi-kwadraat toets voor onafhankelijkheid* is uitgevoerd om te toetsen of er een afhankelijkheid is tussen het uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel. De nulhypothese dat uitval en invoering van het leenstelsel onafhankelijk zijn kan verworpen worden, &chi;^2^ ~`r vDF`~ = `r vChi2`, *p* = `r vP`, *w* = `r Round_and_format(w)`. De propoties per rij in Tabel 3 laten zien dat er relatief meer studenten uitvallen nadat er een leenstelsel is ingevoerd.
# 
# |                      | geen uitval   | uitval | 
# | -------------------- | ---------| ------------| 
# | **geen leenstelsel** |`r Round_and_format(ptable[1,1])`   | `r Round_and_format(ptable[1,2])`          | 
# | **wel leenstelsel**  |`r Round_and_format(ptable[2,1])`   | `r Round_and_format(ptable[2,2])`          |
# *Tabel 3. Proporties wel of niet uitvallen studenten met of zonder leenstelsel berekend per rij.*
# <!-- ## /TEKSTBLOK: Rapportage2.R -->
# 

# # Fisher's exacte toets
# ## Uitvoering 
# <!-- ## TEKSTBLOK: Data-inladen-Fisher.R -->
# *Fisher's exacte toets* wordt uitgevoerd om de vraag te beantwoorden of er een afhankelijkheid is tussen het uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel. Deze toets is ook betrouwbaar bij een laag aantal observaties. Om de toets te illustreren is een subset van de dataset `Uitval_studenten_functiebeperking_leenstelsel` ingeladen; de subset heet `Fisher_Uitval_studenten_functiebeperking_leenstelsel`.
# 
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Periode` en `Uitval`. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Fisher_Uitval_studenten_functiebeperking_leenstelsel$Periode` (voor of na invoering leenstelsel) en `Fisher_Uitval_studenten_functiebeperking_leenstelsel$Uitval` (wel of niet uitgevallen). 
# <!-- ## /TEKSTBLOK: Data-inladen-Fisher.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2Fisher.R -->

# In[ ]:



## Maak een kruistabel
Fisher_Uitval_studenten_kruistabel <- table(Fisher_Uitval_studenten_functiebeperking_leenstelsel$Periode, Fisher_Uitval_studenten_functiebeperking_leenstelsel$Uitval)

## Print de kruistabel 
print(Fisher_Uitval_studenten_kruistabel)

## Print een tabel met proporties, tweede argument 2 zorgt ervoor dat de 
## proporties per rij berekend worden
prop.table(Fisher_Uitval_studenten_kruistabel, 1)


# <!-- ## /OPENBLOK: Data-kruistabel2Fisher.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel3Fisher.R -->
# De kruistabel en bijbehorende tabel met proporties laat zien dat het percentage uitgevallen studenten hoger is na invoering van het leenstelsel (`r Round_and_format(100 * prop.table(Fisher_Uitval_studenten_kruistabel, 1)[2,2])`%) dan voor invoering van het leenstelsel (`r Round_and_format(100 * prop.table(Fisher_Uitval_studenten_kruistabel, 1)[1,2])`%).
# <!-- ## /TEKSTBLOK: Data-kruistabel3Fisher.R -->

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: AssumptieFisher.R -->
# Toets de assumptie dat niet meer dan 20% van de verwachte aantallen observaties gelijk aan of kleiner dan vijf is. Bereken het verwachte aantal observaties met het argument `chisq.test()$expected` van de functie `chisq.test()` met als argumenten de variabelen `Fisher_Uitval_studenten_functiebeperking_leenstelsel$Periode` (voor of na invoering leenstelsel) en `Fisher_Uitval_studenten_functiebeperking_leenstelsel$Uitval` (wel of niet uitgevallen). 
# <!-- ## /TEKSTBLOK: AssumptieFisher.R -->
# 
# <!-- ## OPENBLOK: Assumptie1Fisher.R -->

# In[ ]:


chisq.test(Fisher_Uitval_studenten_functiebeperking_leenstelsel$Periode,
           Fisher_Uitval_studenten_functiebeperking_leenstelsel$Uitval)$expected


# <!-- ## /OPENBLOK: Assumptie1Fisher.R -->
# 
# Een van de verwachte aantallen observaties is kleiner dan vijf, dus de *Chi-kwadraat toets voor onafhankelijkheid* kan niet worden uitgevoerd. *Fisher's exacte toets* moet inderdaad gebruikt worden voor deze dataset.

# ## Fisher's exacte toets
# 
# <!-- ## TEKSTBLOK: Fisher1.R -->
# Voer *Fisher's exacte toets* uit met de functie `fisher.test` met als argumenten de variabelen `Fisher_Uitval_studenten_functiebeperking_leenstelsel$Periode` (voor of na invoering leenstelsel) en `Fisher_Uitval_studenten_functiebeperking_leenstelsel$Uitval` (wel of niet uitgevallen). 
# <!-- ## /TEKSTBLOK: Fisher1.R -->

# <!-- ## OPENBLOK: Fishers-Exact-toets.R -->

# In[ ]:


fisher.test(Fisher_Uitval_studenten_functiebeperking_leenstelsel$Periode,
           Fisher_Uitval_studenten_functiebeperking_leenstelsel$Uitval)


# <!-- ## /OPENBLOK: Fishers-Exact-toets.R -->

# <!-- ## CLOSEDBLOK: Fishers-Exact-toets.R -->

# In[ ]:


fish <- fisher.test(Fisher_Uitval_studenten_functiebeperking_leenstelsel$Periode,
           Fisher_Uitval_studenten_functiebeperking_leenstelsel$Uitval)
vF_p <- Round_and_format(fish$p.value)
vConf.int1 <- Round_and_format(fish$conf.int[1])
vConf.int2 <- Round_and_format(fish$conf.int[2])
vOR <- Round_and_format(fish$estimate)


# <!-- ## /CLOSEDBLOK: Fishers-Exact-toets.R -->
# 
# <!-- ## TEKSTBLOK: Fishers-Exact-toets.R -->
# * *p* = `r vF_p`; p-waarde > 0,05, dus de H~0~ wordt niet verworpen.[^11]  
# * De odds ratio is `r vOR` met een 95%-betrouwbaarheidsinterval van `r vConf.int1` tot `r vConf.int2`. De kans op uitval van studenten met een functiebeperking met leenstelsel is dus `r vOR` keer zo groot is als de kans op uitval van studenten met een functiebeperking zonder het leenstelsel. Deze relatie is echter niet significant.
# 
# <!-- ## /TEKSTBLOK: Fishers-Exact-toets.R -->
# 

# ## Rapportage
# 
# <!-- ## CLOSEDBLOK: Rapportage1Fisher.R -->

# In[ ]:


## Maak een kruistabel
Fisher_Uitval_studenten_kruistabel <- table(Fisher_Uitval_studenten_functiebeperking_leenstelsel$Periode, Fisher_Uitval_studenten_functiebeperking_leenstelsel$Uitval)

## Print de kruistabel 
print(Fisher_Uitval_studenten_kruistabel)

## Print een tabel met proporties, tweede argument 2 zorgt ervoor dat de 
## proporties per rij berekend worden
Fisher_ptable <- prop.table(Fisher_Uitval_studenten_kruistabel, 1)


# <!-- ## /CLOSEDBLOK: Rapportage1Fisher.R -->

# <!-- ## TEKSTBLOK: Rapportage2Fisher.R -->
# *Fisher's exacte toets* is uitgevoerd om te toetsen of er een afhankelijkheid is tussen het uitvallen van studenten met een functiebeperking en het wel of niet invoeren van het leenstelsel. De nulhypothese dat uitval en invoering van het leenstelsel onafhankelijk zijn kan niet verworpen worden, *p* = `r vF_p`. De proporties per rij in Tabel 4 laten zien dat er relatief meer studenten uitvallen nadat er een leenstelsel is ingevoerd, dit verschil is echter niet significant.
# 
# |                      | geen uitval   | uitval | 
# | -------------------- | ---------| ------------| 
# | **geen leenstelsel** |`r Round_and_format(Fisher_ptable[1,1])`   | `r Round_and_format(Fisher_ptable[1,2])`          | 
# | **wel leenstelsel**  |`r Round_and_format(Fisher_ptable[2,1])`   | `r Round_and_format(Fisher_ptable[2,2])`          |
# *Tabel 4. Proporties wel of niet uitvallen studenten met of zonder leenstelsel berekend per rij voor dataset Fisher's exacte toets.*
# <!-- ## /TEKSTBLOK: Rapportage2Fisher.R -->
# 
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





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

# <!-- ## TEKSTBLOK: Extra-Bron.R -->
# 
# <!-- ## /TEKSTBLOK: Extra-Bron.R -->
