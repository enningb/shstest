#!/usr/bin/env python
# coding: utf-8
---
title: "Multilevel multinomiale logistische regressie"
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


source(paste0(here::here(),"/01. Includes/data/20.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# Gebruik *multilevel multinomiale logistische regressie* om te toetsen of er verschillen zijn op een nominale variabele tussen drie of meer herhaalde metingen van één groep of tussen drie of meer gepaarde groepen.[^1] 

# # Onderwijscasus
# <div id = "casus">
# 
# In de bachelor Psychologie kiezen studenten aan het einde van het eerste jaar een specialisatie voor jaar 2 en 3. Hierbij kunnen studenten kiezen uit de richtingen Klinische Neuropsychologie (KNP), Sociale Psychologie (SP), en Arbeids- en Organisatiepsychologie (AOP). De opleidingsdirecteur wil onderzoeken op welk moment in het eerste studiejaar studenten ontdekken welke specialisatie zij willen doen. Daarom start zij een experiment waarin ze aan een groep eerstejaars studenten vraagt om na elke onderwijsperiode aan te geven welke specialisatie ze op dat moment zouden kiezen. Met dit experiment kan zij ontdekken op welk moment in het eerste studiejaar studenten de keuze maken, maar ook in welke periode studenten van voorkeur veranderen. Op basis van deze analyse kan de opleidingsdirecteur onderzoeken op welk moment in het jaar er behoefte is aan voorlichting over de verschillende specialisaties in de bachelor Psychologie. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen afhankelijkheid tussen de verschillende periodes en de keuze voor een specialisatie.
# 
# *H~A~*: Er is een afhankelijkheid tussen de verschillende periodes en de keuze voor een specialisatie.
# </div>
# 
# # Multilevel multinomiale logistische regressie
# 
# *Multilevel multinomiale logistische regressie* is een techniek waarbij een nominale afhankelijke variabele wordt voorspeld met behulp van één of meerdere onafhankelijke variabelen.[^1] De term *multilevel* houdt in dat rekening wordt gehouden met de hiërarchische structuur in de data. Elke student wordt gemeten in vijf onderwijsperiodes, wat betekent dat de observaties gekoppeld zijn aan een bepaalde student. Om met deze hiërarchie rekening te houden, wordt de multilevel variant van *multinomiale logistische regressie* uitgevoerd.[^1]<sup>,</sup>[^12]<sup>,</sup>[^13]
# 
# Om de hypothese te toetsen dat er geen afhankelijkheid bestaat tussen de keuze voor een specialisatie en de onderwijsperiodes worden twee regressiemodellen geschat. In het eerste model wordt de afhankelijke variabele specialisatie voorspeld met behulp van een student specifieke intercept. In het tweede model wordt worden de onderwijsperiodes als onafhankelijke variabele toegevoegd waardoor de afhankelijke variabele specialisatie wordt voorspeld met een student specifieke intercept en de onderwijsperiodes. Daarna worden beide modellen vergeleken waarbij in feite wordt getoetst of de toevoeging van de onderwijsperiodes zorgt voor een significante verbetering van het model. Bij een significant resultaat is er een afhankelijkheid tussen de onderwijsperiodes en de specialisatie. Bij een niet significant verschil resultaat is er geen afhankelijkheid.
# 
# ## Modellen
# 
# In de eerste vergelijking wordt de afhankelijke variabele specialisatie voorspeld met behulp van een student specifieke intercept. Reden hiervoor is dat er op deze manier gecontroleerd wordt voor het feit dat de observaties gekoppeld zijn aan een bepaalde student, i.e. de hiërarchische structuur van de data. Het eerste model noemt men het *intercept-only model* en is als volgt geformuleerd[^2]:
# 
# $$ Specialisatie_{it} = \beta_{0i} + e_{it}$$
# 
# met $t$ als indicator van de onderwijsperiode, $i$ als indicator van de student, de afhankelijke variabele $Specialisatie_{it}$ die aangeeft welke specialisatie gekozen is, $\beta_{0i}$ als student specifiek intercept (vanwege de index $i$) en $e_{it}$ als residu. 
# 
# In het tweede regressiemodel wordt de specialisatie voorspeld met behulp van een student specifiek intercept en variabelen voor de onderwijsperiodes. In dit model wordt de keuze voor een specialisatie voorspeld op basis van de onderwijsperiodes en een student specifiek intercept. Het model is als volgt geformuleerd[^2]:
# 
# $$ Specialisatie_{it} = \beta_{0i} + \beta_1*P_2 + \beta_2*P_3 + \beta_3*P_4 + \beta_4*P_5 + e_{it}$$
# met $t$ als indicator van de onderwijsperiode, $i$ als indicator van de student, de afhankelijke variabele $Specialisatie_{it}$ die aangeeft welke specialisatie gekozen is, $\beta_{0i}$ als student specifiek intercept (vanwege de index $i$), $P_2$ als variabele voor onderwijsperiode 2 met bijbehorende regressiecoefficient $\beta_1$, $P_3$, $P_4$ en $P_5$ als variabelen voor respectievelijk onderwijsperiodes 3, 4 en 5  en $e_{it}$ als residu. 
# 
# Model 1 en model 2 zijn geneste modellen. Bij geneste modellen is het ene model te schrijven als een versie van het andere model na het verwijderen van een aantal predictors. In deze casus zijn beide modellen genest, omdat model 1 te schrijven is als een versie van model 2 na het verwijderen van alle onderwijsperiodes uit de regressie-vergelijking van model 2. Het model waarbij de predictors verwijderd zijn, wordt als het ware gereduceerd. Daarom wordt dit het gereduceerde model genoemd. Het model waar de predictors niet verwijderd zijn, wordt het uitgebreide model genoemd. Model 1 is dus het gereduceerde model; model 2 het uitgebreide model.[^11]
# 
# ## Likelihood ratio toets
# 
# De hypothese van afhankelijkheid tussen de keuze voor een specialisatie en de onderwijsperiodes wordt getoetst door beide modellen met elkaar te vergelijken met een *likelihood ratio toets*. Een *likelihood ratio toets* toetst of het verschil tussen twee geneste modellen significant is op basis van de log-likelihood van de modellen. De log-likelihood van een model is een maat voor de kwaliteit van het model en wordt berekend door voorspellingen en observaties te vergelijken. Deze toets wordt bij regressie-analyses gebruikt als meerdere predictors tegelijkertijd toegevoegd worden. Een niet significant resultaat bij de *likelihood ratio toets* betekent dat er geen significante verschil is tussen het gereduceerde en uitgebreide model. In andere woorden, het uitbreiden van het model is geen significante toevoeging en het gereduceerde model volstaat. Een significant resultaat bij de *likelihood ratio toets* betekent dat er wel een significant verschil is tussen het gereduceerde en uitgebreide model. In dat geval is het uitgebreide model een betere representatie van de werkelijkheid en heeft de toevoeging van predictors waarde.[^11]
# 
# De toetsstatistiek van de *likelihood ratio toets* is te berekenen als $- 2 * (LL_r - LL_u)$ waarin $LL_r$ de loglikelihood van het gereduceerde model is en $LL_u$ de loglikelihood van het uitgebreide model is. De toetsstatistiek volgt een chi-kwadraat verdeling met als aantal vrijheidsgraden het aantal predictors dat is verwijderd in het gereduceerde model.[^11] In dit geval zijn er vier predictors verwijderd. Echter, bij multinomiale logistische regressie moet dit getal vermenigvuldigd worden met het aantal categorieën van de afhankelijke variabele minus één.[^3] In deze casus zijn er drie categorieën (de drie specialisaties), dus wordt het aantal verwijderde predictors (vier) vermenigvuldigd met twee. Het aantal vrijheidsgraden bij de *likelihood ratio toets* is dus acht.
# 
# Om de afhankelijkheid tussen de keuze voor een specialisatie en de onderwijsperiodes te toetsen, worden model 1 en model 2 met een *likelihood ratio toets* vergeleken. Een significant resultaat betekent dat de toevoeging van de onderwijsperiodes als predictors waarde heeft. Dit betekent dat de onderwijsperiodes gerelateerd zijn aan de keuze van de specialisatie en er dus een afhankelijkheid is tussen beide. In dat geval wordt de nulhypothese dat er geen afhankelijkheid is tussen de keuze van de specialisatie en de onderwijsperiodes verworpen. Een niet significant resultaat bij de *likelihood ratio toets* betekent dat toevoeging van de onderwijsperiodes als predictors geen waarde heeft. In dat geval kan de nulhypothese dat er geen afhankelijkheid is niet worden verworpen.
# 
# # Assumpties
# 
# Om een *multilevel multinomiale logistische regressie* uit te voeren, moeten de data aan een aantal voorwaarden voldoen. Er dient een categorische afhankelijke variabele te zijn met meer dan twee categorieën zonder overlap: elke observatie past slechts in een van beide categorieën. Daarnaast zijn er drie of meer herhaalde metingen van één groep of zijn er drie of meer gepaarde groepen. In beide gevallen zijn de observationele eenheden een willekeurige steekproef van de populatie.[^4]
# 
# ## Complete informatie
# Bij *multilevel multinomiale logistische regressie* is de keuze voor de specialisatie de afhankelijke variabele en de onderwijsperiode de onafhankelijke variabele. Om *multilevel multinomiale logistische regressie* uit te voeren, moet er voor elke combinatie van de afhankelijke variabele en onafhankelijke variabele minimaal één observatie zijn.[^13] Met betrekking tot deze casus betekent dat dat er minimaal één observatie is voor elke specialisatie in elke periode. Toets deze assumptie met behulp van een kruistabel: een tabel waarin de aantallen observaties worden weergegeven per combinatie van de categorieën van beide variabelen. Een voorbeeld van een kruistabel voor de huidige casus is te vinden in Tabel 1.   
# 
# |          | Periode 1   | Periode 2 | Periode 3 | Periode 4 | Periode 5 | 
# | -------- | ---------| ------------| -------------| -------------| -------------| 
# | Arbeids- en organisatiepsychologie  | 20 |  10 |  10 |  5  |  5  |
# | Klinische neuropsychologie          | 20 |  30 |  40 |  40 |  45 |
# | Sociale psychologie                 | 20 |  20 |  10 |  15 |  10 |
# *Tabel 1. Geobserveerde aantallen per specialisatie in elke onderwijsperiode.*
# 
# In Tabel 1 is te zien dat er voor elke combinatie van onderwijsperiode en specialisatie meer dan één observatie is. Dit betekent dat er aan de assumptie van complete informatie is voldaan.
# 
# # Post-hoc toetsen
# 
# Met *multilevel multinomiale logistische regressie* wordt getoetst of er een afhankelijkheid is tussen de keuze voor een specialisatie en de verschillende onderwijsperiodes. Voer een post-hoc toets uit om daarna te bepalen welke onderwijsperiodes van elkaar verschillen wat betreft de keuze voor specialisaties. Gebruik hiervoor de [Bhapkar toets](18-Bhapkar-toets-R.html) als post-hoc toets.[^6] 
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout.[^8] Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook nog andere opties voor een correctie op de p-waarden.[^9] 
# 
# # De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken1.R -->
# Er is een dataset ingeladen genaamd `Data_Specialisatie`. In deze dataset is per onderwijsperiode aangegeven welke specialisatie de student kiest.
# <!-- ## /TEKSTBLOK: Data-bekijken1.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.R -->

# In[ ]:


## Eerste 6 observaties
head(Data_Specialisatie)

## Laatste 6 observaties
tail(Data_Specialisatie)


# <!-- ## /OPENBLOK: Data-bekijken2.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft weer hoeveel eerstejaars studenten er kiezen voor een bepaalde specialisatie in elke onderwijsperiode. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Data_Specialisatie$Specialisatie` die aangeeft welke specialisatie de student kiest en de variabele `Data_Specialisatie$Onderwijsperiode` die aangeeft in welke onderwijsperiode de observatie is gedaan. 
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:


## Maak een kruistabel
Specialisatie_kruistabel <- table(Data_Specialisatie$Specialisatie, Data_Specialisatie$Onderwijsperiode)

## Print de kruistabel 
print(Specialisatie_kruistabel)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# <!-- ## CLOSEDBLOK: Data-kruistabel3.R -->

# In[ ]:


## Maak een kruistabel
Specialisatie_kruistabel <- table(Data_Specialisatie$Specialisatie, Data_Specialisatie$Onderwijsperiode)


# <!-- ## /CLOSEDBLOK: Data-kruistabel3.R -->
# 
# De kruistabel laat zien dat alle drie de specialisaties even vaak door studenten zijn gekozen, maar dat dat daarna veranderd. In onderwijsperiode 5 kiezen de meeste studenten voor de specialisatie Klinische neuropsychologie.

# # Uitvoering
# 
# ## Assumptie complete informatie
# 
# Een assumptie bij *multilevel multinomiale logistische regressie* is dat er minimaal één observatie is voor elke combinatie van afhankelijke en onafhankelijke variabele. Toets deze assumptie door de kruistabel te controleren op het aantal observaties per cel. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Data_Specialisatie$Specialisatie` die aangeeft welke specialisatie de student kiest en de variabele `Data_Specialisatie$Onderwijsperiode` die aangeeft in welke onderwijsperiode de observatie is gedaan.
# 
# <!-- ## OPENBLOK: steekproefgrootte1.R -->

# In[ ]:


## Maak een kruistabel
Specialisatie_kruistabel <- table(Data_Specialisatie$Specialisatie, Data_Specialisatie$Onderwijsperiode)

## Print de kruistabel 
print(Specialisatie_kruistabel)


# <!-- ## /OPENBLOK: steekproefgrootte1.R -->
# 
# Elke cel van de kruistabel heeft meerdere observaties. Dit betekent dat er voor elke combinatie van de afhankelijke en onafhankelijke variabele minimaal één observatie is. Er is dus aan de assumptie van complete informatie voldaan.
# 
# ## Multilevel multinomiale logistische regressie
# <!-- ## TEKSTBLOK: MMLR1.R -->
# Voer een *multilevel multinomiale logistische regressie* uit om te onderzoeken of er een afhankelijkheid is tussen de keuze voor de specialisatie en de onderwijsperiodes bij eerstejaars studenten van de bachelor Psychologie. Fit eerst het gereduceerde en uitgebreide model met behulp van de functie `brm()` van het `brms` package. Bereken daarna van beide modellen de log-likelihood. Voer tenslotte de *likelihood ratio toets* uit.
# 
# Fit het gereduceerde model met de functie `brm()` met als argument `formula = Specialisatie ~ (1 | Studentnummer)` met daarin de afhankelijke variabele `specialisatie` en `(1 | Studentnummer)` om een student specifiek intercept in te stellen, `data = Data_Specialisatie` voor de gebruikte dataset, `family = "categorical"` om aan te geven dat de afhankelijke variabele nominaal is, een seed `seed = 12345` zodat de uitkomsten bij opnieuw runnen van de code hetzelfde zijn en `save_all_pars = TRUE` om de loglikelihood te berekenen. Voor de seed kan elk willekeurig getal gekozen worden, in deze casus is het getal 12345 gekozen.
# 
# Fit het uitgebreide model met de functie `brm()` met als argument `formula = Specialisatie ~ Onderwijsperiode + (1 | Studentnummer)` met daarin de afhankelijke variabele `Specialisatie`, als onafhankelijke variabele `Onderwijsperiode` en `(1 | Studentnummer)` om een student specifiek intercept in te stellen, `data = Data_Specialisatie` voor de gebruikte dataset, `family = "categorical"` om aan te geven dat de afhankelijke variabele nominaal is, een seed `seed = 12345` zodat de uitkomsten bij opnieuw runnen van de code hetzelfde zijn en `save_all_pars = TRUE` om de loglikelihood te berekenen.Voor de seed kan elk willekeurig getal gekozen worden, in deze casus is het getal 12345 gekozen.
# 
# Bereken daarna de loglikelihood voor beide modellen met de zelfgemaakte functie `Loglikelihood_Functie` en voer de *likelihood ratio toets* uit. 
# 
# <!-- ## /TEKSTBLOK: MMLR1.R -->
# 
# <!-- ## OPENBLOK: MMLR2.R -->

# In[ ]:


library(brms)


# In[ ]:


# Stel model 1 op: student specifiek intercept
Model_1 <- "Specialisatie ~ (1 | Studentnummer)"

# Stel model 2 op: student specifiek intercept plus onderwijsperiodes
Model_2 <- "Specialisatie ~ Onderwijsperiode + (1 | Studentnummer)"

# Fit het gereduceerde model: student specifiek intercept
Fit_1 <- brm(formula = Model_1,
           data = Data_Specialisatie, 
           family = "categorical",
           seed = 12345, save_all_pars = TRUE)

# Fit het uitgebeide model: student specifiek intercept plus onderwijsperiodes
Fit_2 <- brm(formula = Model_2, 
           data = Data_Specialisatie, 
           family = "categorical",
           seed = 12345, save_all_pars = TRUE)


# In[ ]:


# Maak een functie om de loglikelihood voor een model te berekenen
LogLikelihood_Functie <- function(fit){
  # Sla de matrix met loglikelihood samples op
  LL1 <- log_lik(fit)
  # Neem de exponent om de likelihood in plaats van de loglikelihood te krijgen
  LL2 <- exp(LL1)
  # Bereken de gemiddelde likelihood per kolom (per student) met colMeans
  LL3 <- colMeans(LL2)
  # Neem logaritme om terug te gaan naar de log-likelihood
  LL4 <- log(LL3)
  # Neem de som zodat je de loglikelihood voor alle studenten krijgt
  LL5 <- sum(LL4)
  # Retourneer de loglikelihood
  return(LL5)
}

# Bereken de loglikelihood voor beide modellen
Loglikelihood_Model_1 <- LogLikelihood_Functie(Fit_1)
Loglikelihood_Model_2 <- LogLikelihood_Functie(Fit_2)

# Bereken de toetsstatistiek van de likelihood ratio toets
Toetsstatistiek <- -2 * (Loglikelihood_Model_1 - Loglikelihood_Model_2)

# Stel het aantal predictors in dat is verwijderd bij het gereduceerde model
Vrijheidsgraden <- 8

# Bereken de p-waarde
p_waarde <- 1 - pchisq(Toetsstatistiek, df = Vrijheidsgraden)

# Print de toetsstatistiek en de p-waarde
Toetsstatistiek
p_waarde


# <!-- ## /OPENBLOK: MMLR2.R -->
# 

# <!-- ## TEKSTBLOK: MMLR4.R -->
# * &chi;^2^ ~8~ = `r Round_and_format(Toetsstatistiek)`, *df* = 8, *p* < 0,0001
# * Vrijheidsgraden: *df* = *p*(*c*-1), waar *p* staat voor het aantal verwijderde predictors en *c* voor het aantal categorieën van de afhankelijke variabele. In dit geval is *df* = 4(3 - 1) = 8.  
# * p-waarde < 0,05, dus de H~0~ wordt verworpen.[^10]
# * Er is een afhankelijkheid tussen de onderwijsperiodes en de keuze voor de specialisatie.
# 
# <!-- ## /TEKSTBLOK: MMLR4.R -->

# ## Post-hoc toets
# 
# <!-- ## TEKSTBLOK: posthoc1.R -->
# Voer post-hoc toetsen uit om te onderzoeken tussen welke onderwijsperiodes er verschillen zijn in de verdeling van de keuzes voor de specialisaties van de eerstejaars studenten Psychologie. Gebruik de [Bhapkar toets](18-Bhapkar-toets-R.html) als post-hoc toets. 
# 
# Voer de post-hoc toetsen uit met de functie `bhapkar()` van het package `irr` met als argument `cbind(P1, P2)` waarin `P1` de vector met de gekozen specialisaties in onderwijsperiode 1 is en `P2` de vector met de gekozen specialisaties in onderwijsperiode 2 is. Maak hiervoor eerst een vector aan met de gekozen specialisaties in elke onderwijsperiode en voer daarna voor elke combinatie van onderwijsperiodes een post-hoc toets uit. Voer de Bonferroni correctie uit door het significantieniveau te delen door het aantal uitgevoerde toetsen. Het significatieniveau voor deze post-hoc toetsen wordt dan 0,05 / 10 ≈ 0,005. Vergelijk de p-waarden van de [Bhapkar toets](18-Bhapkar-toets-R.html) daarna met dit significantieniveau. 
# 
# <!-- ## /TEKSTBLOK: posthoc1.R -->

# <!-- ## OPENBLOK: posthoc2.R -->

# In[ ]:


## Laad het package van de Bhapkar toets in
library(irr)

## Sla de voorlopige en definitieve BSA-adviezen op in een vector
P1 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P1"]
P2 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P2"]
P3 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P3"]
P4 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P4"]
P5 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P5"]

## Voer de Bhapkar toets uit voor alle combinaties van onderwijsperiodes
bhapkar(cbind(P1, P2))
bhapkar(cbind(P1, P3))
bhapkar(cbind(P1, P4))
bhapkar(cbind(P1, P5))
bhapkar(cbind(P2, P3))
bhapkar(cbind(P2, P4))
bhapkar(cbind(P2, P5))
bhapkar(cbind(P3, P4))
bhapkar(cbind(P3, P5))
bhapkar(cbind(P4, P5))


# <!-- ## /OPENBLOK: posthoc2.R -->
# 
# <!-- ## CLOSEDBLOK: posthoc3.R -->

# In[ ]:


## Laad het package van de Bhapkar toets in
library(irr)

## Sla de voorlopige en definitieve BSA-adviezen op in een vector
P1 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P1"]
P2 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P2"]
P3 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P3"]
P4 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P4"]
P5 <- Data_Specialisatie$Specialisatie[Data_Specialisatie$Onderwijsperiode == "P5"]

## Voer de Bhapkar toets uit voor alle combinaties van onderwijsperiodes
PH_P1_P3 <-  bhapkar(cbind(P1, P3))
PH_P1_P4 <-  bhapkar(cbind(P1, P4))
PH_P1_P5 <-  bhapkar(cbind(P1, P5))


# <!-- ## /CLOSEDBLOK: posthoc3.R -->
# 
# <!-- ## TEKSTBLOK: posthoc4.R -->
# * Er zijn significante verschillen gevonden tussen de verdeling van de keuzes voor specialisaties tussen onderwijsperiode 1 en 3 (*&chi;^2^ ~2~* = `r Round_and_format(PH_P1_P3$statistic)`, *p* < 0,001), onderwijsperiode 1 en 4 (*&chi;^2^ ~2~* = `r Round_and_format(PH_P1_P4$statistic)`, *p* < 0,001) en onderwijsperiode 1 en 5 (*&chi;^2^ ~2~* = `r Round_and_format(PH_P1_P5$statistic)`, *p* < 0,0001). 
# * Tussen de overige onderwijsperiodes is geen significant verschil gevonden wat betreft de verdeling van keuzes voor specialisaties.
# 
# <!-- ## TEKSTBLOK: posthoc4.R -->
# 

# # Rapportage
# 
# <!-- ## TEKSTBLOK: rapportage2.R -->
# 
# Een *multilevel multinomiale logistische regressie* is uitgevoerd om te onderzoeken of er een afhankelijkheid is tussen de onderwijsperiode en de keuze voor een specialisatie van eerstejaars studenten van de bachelor psychologie. De verdeling van de keuzes voor de specialisaties in de verschillende onderwijsperiodes is weergegeven in Tabel 2. De nulhypothese dat er geen afhankelijkheid tussen onderwijsperiode en keuze voor specialisatie is kan verworpen worden, &chi;^2^ ~8~ = `r Round_and_format(Toetsstatistiek)`, *df* = 8, *p* < 0,0001. Er zijn dus verschillen in de verdeling van de keuze voor specialisaties tussen de verschillende onderwijsperiodes.
# 
# Om te bepalen tussen welke onderwijsperiodes deze percentages verschillen, is de [Bhapkar toets](18-Bhapkar-toets-R.html) als post-hoc toets uitgevoerd met een Bonferroni correctie voor meerdere toetsen. Uit de post-hoc toetsen blijkt dat er alleen significante verschillen zijn gevonden tussen de verdeling van de keuzes voor specialisaties tussen onderwijsperiode 1 en 3 (*&chi;^2^ ~2~* = `r Round_and_format(PH_P1_P3$statistic)`, *p* < 0,001), onderwijsperiode 1 en 4 (*&chi;^2^ ~2~* = `r Round_and_format(PH_P1_P4$statistic)`, *p* < 0,001) en onderwijsperiode 1 en 5 (*&chi;^2^ ~2~* = `r Round_and_format(PH_P1_P5$statistic)`, *p* < 0,0001). De frequenties in Tabel 2 lijken te suggereren dat in onderwijsperiode 1 alle specialisaties even vaak gekozen worden en dat er vanaf onderwijsperiode 3 afwijkingen hiervan ontstaan waarbij Klinische neuropsychologie het populairst is.
# <!-- ## /TEKSTBLOK: rapportage2.R -->
# 

# |          | Periode 1   | Periode 2 | Periode 3 | Periode 4 | Periode 5 | 
# | -------- | ---------| ------------| -------------| -------------| -------------| 
# | Arbeids- en organisatiepsychologie  | 20 |  10 |  10 |  5  |  5  |
# | Klinische neuropsychologie          | 20 |  30 |  40 |  40 |  45 |
# | Sociale psychologie                 | 20 |  20 |  10 |  15 |  10 |
# *Tabel 2. Geobserveerde aantallen per specialisatie in elke onderwijsperiode.*
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Hox, J. J., Moerbeek, M., & Van de Schoot, R. (2010). Multilevel analysis: Techniques and applications. Routledge.
# [^2]: Om precies te zijn wordt de logaritme van de kans dat de observatie in categorie $i$ valt gedeeld door de kans dat de observatie in de referentiecategorie $ref$ valt, i.e. $\log(\frac{\pi_i}{\pi_{ref}})$. Er wordt een aparte vergelijking voor alle categorieën ten opzichte van de referentiecategorie geschat. Dus er zijn in feite meerdere regressievergelijkingen die geschat worden. 
# [^3]: Bij multinomiale logistische regressie bestaat de afhankelijke variabele uit meer dan twee categorieën. Daarom wordt de kans voorspeld dat een observatie in een categorie valt ten opzichte van een referentiecategorie. De referentiecategorie is voor alle andere categorieën hetzelfde. Er worden dus meerdere regressievergelijkingen geschat, om precies te zijn het aantal categorieën minus één (dat is de referentiecategorie). Daarom wordt het aantal verwijderde predictors vermenigvuldigd met dit aantal.
# [^4]: Laerd Statistics (2018). *Multinomial Logistic Regression using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/multinomial-logistic-regression-using-spss-statistics.php
# [^8]: Statistics How To (12 oktober 2015). *Benjamini-Hochberg Procedure*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/benjamini-hochberg-procedure/). 
# [^9]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^10]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten. 
# [^11]: Stat 504. *6.2.3 - More on Goodness-of-Fit and Likelihood ratio tests*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat504/node/220/).
# [^12]: Stat 504. *8.1 - Polytomous (Multinomial) Logistic Regression*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat504/node/172/).
# [^13]: Stat 504. *8.2 - Baseline-Category Logit Model*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat504/node/173/).
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
