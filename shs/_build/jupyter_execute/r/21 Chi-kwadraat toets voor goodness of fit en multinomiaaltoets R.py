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


source(paste0(here::here(),"/01. Includes/data/21.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# <!-- ## TEKSTBLOK: Link1.R -->
# Gebruik de *Chi-kwadraat toets voor goodness of fit* om te onderzoeken of de geobserveerde frequenties van de categorieën van één categorische variabele met meer dan twee categorieën overeenkomt met de verwachte frequenties van de categorische variabele.[^6]<sup>,</sup>[^7] Met deze toets kunnen geobserveerde percentages met bekende of verwachte percentages vergeleken worden. Gebruik de exacte *multinomiaaltoets* bij een laag aantal observaties, dit wordt bij de assumpties toegelicht.[^1] De *Chi-kwadraat toets voor goodness of fit* kan ook gebruikt worden voor een categorische variabele met twee categorieën. Voor de exacte *multinomiaaltoets* geldt dit ook, maar in dat geval is de toets gelijk aan de exacte *binomiaaltoets* die te vinden is in bijbehorende [toetspagina](11-Chi-kwadraat-toets-voor-goodness-of-fit-en-binomiaaltoets-R.html). De *Chi-kwadraat toets voor goodness of fit* en de exacte *multinomiaaltoets* zijn voor zowel nominale[^9] als ordinale[^8] variabelen te gebruiken.
# <!-- ## /TEKSTBLOK: Link1.R -->
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
# <!-- ## TEKSTBLOK: Data-bekijken1.R -->
# Er is een dataset ingeladen genaamd `BSA_Maritieme_techniek`. Dit is een dataframe met studentnummers en een nominale variabele die laat zien wat voor BSA de student heeft ontvangen.
# <!-- ## /TEKSTBLOK: Data-bekijken1.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.R -->

# In[ ]:


## Eerste 6 observaties
head(BSA_Maritieme_techniek)
## Laatste 6 observaties
tail(BSA_Maritieme_techniek)


# <!-- ## /OPENBLOK: Data-bekijken2.R -->
# 
# Het is informatief om de frequenties en de percentages van de drie mogelijkheden van het BSA te bepalen voor de studenten Maritieme Techniek.
# 
# <!-- ## OPENBLOK: Data-bekijken3.R -->

# In[ ]:


## Bepaal de frequenties
table(BSA_Maritieme_techniek$BSA_advies)


# In[ ]:


## Bepaal de percentages
100*prop.table(table(BSA_Maritieme_techniek$BSA_advies))


# In[ ]:


Tab <- table(BSA_Maritieme_techniek$BSA_advies)
Proptab <- 100*prop.table(table(BSA_Maritieme_techniek$BSA_advies))


# <!-- ## /OPENBLOK: Data-bekijken3.R -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken4.R -->
# Het aantal studenten met een positief BSA is `r Round_and_format(Tab[2])` (`r Round_and_format(Proptab[2])`%), met een negatief BSA is `r Round_and_format(Tab[1])` (`r Round_and_format(Proptab[1])`%) en met een uitgesteld BSA is `r Round_and_format(Tab[3])` (`r Round_and_format(Proptab[3])`%). Het lijkt erop dat het percentage studenten met een positief BSA lager is dan het percentage van de gehele universiteit (70%) en dat het percentage studenten met een negatief BSA juist hoger is dan dat van de gehele universiteit (20%). De *Chi-kwadraat toets voor goodness of fit* of de *multinomiaaltoets* toetst of dit verschil significant is.
# <!-- ## /TEKSTBLOK: Data-bekijken4.R -->
# 
# # Chi-kwadraat toets voor goodness of fit
# 
# ## Asssumptie verwachte frequenties
# 
# <!-- ## TEKSTBLOK: Assumptie.R -->
# De verwachte frequentie mag niet kleiner dan vijf zijn in 20% van de categorieën van de categorische variabele. Aangezien er een variabele met drie categorieën getoetst wordt, mag geen van de drie categorieën dus minder dan vijf als verwachte frequentie hebben. Bereken de verwachte frequentie met het argument `chisq.test()$expected` van de functie `chisq.test()`. De argumenten van de functie zijn de tabel met daarin de hoeveelheid studenten voor de drie mogelijkheden van het BSA `Tabel_volgorde` en een vector die aangeeft wat de verwachte proporties[^4] zijn voor het aantal studenten met respectievelijk een positief, negatief of uitgesteld BSA `p = c(0.7, 0.2, 0.1)`. Let hierbij goed op dat de volgorde van de BSA mogelijkheden in de tabel overeenkomt met de volgorde van de proporties.
# <!-- ## /TEKSTBLOK: Assumptie.R -->
# 
# <!-- ## OPENBLOK: Assumptie1.R -->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten per BSA mogelijkheid
Tabel <- table(BSA_Maritieme_techniek$BSA_advies)

# Zet de tabel op volgorde Positief, Negatief, Uitgesteld
Tabel_volgorde <- Tabel[c("Positief", "Negatief", "Uitgesteld")]

# Bereken de verwachte frequenties
chisq.test(Tabel_volgorde, p = c(0.7, 0.2, 0.1))$expected


# <!-- ## /OPENBLOK: Assumptie1.R -->
# 
# Geen van de verwachte frequenties is kleiner dan vijf, dus de *Chi-kwadraat toets voor goodness of fit* kan worden uitgevoerd.
# 
# ## Uitvoering
# 
# Voer de *Chi-kwadraat toets voor goodness of fit*  uit om te onderzoeken of de verdeling van de BSA mogelijkheden van de studenten Maritieme Techniek overeenkomt met de verdeling van de gehele universiteit (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA).
# 
# <!-- ## TEKSTBLOK: Chi-kwadraat1.R -->
# Gebruik de functie `chisq.test()` met als argumenten de tabel met daarin de hoeveelheid studenten voor de drie mogelijkheden van het BSA `Tabel_volgorde` en een vector die aangeeft wat de verwachte proporties[^4] zijn voor het aantal studenten met respectievelijk een positief, negatief of uitgesteld BSA `p = c(0.7, 0.2, 0.1)`. Let hierbij goed op dat de volgorde van de BSA mogelijkheden in de tabel overeenkomt met de volgorde van de proporties.
# <!-- ## /TEKSTBLOK: Chi-kwadraat1.R -->

# <!-- ## OPENBLOK: Chi-kwadraat2.R-->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten per BSA mogelijkheid
Tabel <- table(BSA_Maritieme_techniek$BSA_advies)

# Zet de tabel op volgorde Positief, Negatief, Uitgesteld
Tabel_volgorde <- Tabel[c("Positief", "Negatief", "Uitgesteld")]

# Voer de toets uit
chisq.test(Tabel_volgorde, p = c(0.7, 0.2, 0.1))


# <!-- ## /OPENBLOK: Chi-kwadraat2.R-->
# 
# <!-- ## CLOSEDBLOK: Chi-kwadraat3.R-->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten per BSA mogelijkheid
Tabel <- table(BSA_Maritieme_techniek$BSA_advies)

# Zet de tabel op volgorde Positief, Negatief, Uitgesteld
Tabel_volgorde <- Tabel[c("Positief", "Negatief", "Uitgesteld")]

# Voer de toets uit
chi2 <- chisq.test(Tabel_volgorde, p = c(0.7, 0.2, 0.1))

vchi2 <- Round_and_format(chi2$statistic)
vp <- Round_and_format(chi2$p.value)
vdf <- chi2$parameter


# <!-- ## /CLOSEDBLOK: Chi-kwadraat3.R-->
# 
# <!-- ## TEKSTBLOK: Chi-kwadraat4.R-->
# * &chi;^2^~`r vdf`~ = `r vchi2`, *p* < 0,001
# * De p-waarde is kleiner dan 0,05, dus de nulhypothese wordt verworpen.[^5]
# 
# <!-- ## /TEKSTBLOK: Chi-kwadraat4.R-->

# ## Post-hoc toets: gestandaardiseerde residuën
# 
# Voer post-hoc toetsen uit om te bepalen voor welke BSA mogelijkheden er verschillen zijn tussen de verdeling van de studenten Maritieme Techniek en de verdeling van de gehele universiteit. Inspecteer hiervoor de Pearson residuen van de *Chi-kwadraat toets voor onafhankelijkheid* op waarden groter dan 1,96 en kleiner dan -1,96. Let op dat hier nog geen correctie voor meerdere toetsen plaatsvindt.[^10]
# 
# <!-- ## TEKSTBLOK: Chi2-toets post-hoc0.R -->
# <!-- ## /TEKSTBLOK: Chi2-toets post-hoc0.R -->
# 
# <!-- ## OPENBLOK: Chi2-toets post-hoc1.R -->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten per BSA mogelijkheid
Tabel <- table(BSA_Maritieme_techniek$BSA_advies)

# Zet de tabel op volgorde Positief, Negatief, Uitgesteld
Tabel_volgorde <- Tabel[c("Positief", "Negatief", "Uitgesteld")]

# Voer de toets uit
Resultaat <- chisq.test(Tabel_volgorde, p = c(0.7, 0.2, 0.1))

# Bekijk de gestandaardiseerde residuën
Resultaat$residuals


# <!-- ## /OPENBLOK: Chi2-toets post-hoc1.R -->
# 
# <!-- ## CLOSEDBLOK: Chi2-toets post-hoc1_1.R -->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten per BSA mogelijkheid
Tabel <- table(BSA_Maritieme_techniek$BSA_advies)

# Zet de tabel op volgorde Positief, Negatief, Uitgesteld
Tabel_volgorde <- Tabel[c("Positief", "Negatief", "Uitgesteld")]

# Voer de toets uit
Resultaat <- chisq.test(Tabel_volgorde, p = c(0.7, 0.2, 0.1))

# Bekijk de gestandaardiseerde residuën
PH_res <- Resultaat$residuals


# <!-- ## /CLOSEDBLOK: Chi2-toets post-hoc1_1.R -->
# 
# De post-hoc toetsing op basis van de gestandaardiseerde residuën kan als volgt geïnterpreteerd worden:
# <!-- ## TEKSTBLOK: Chi2-toets post-hoc2.R-->
# 
# * Significant lager aantal observaties bij een positief BSA , *z* = `r Round_and_format(PH_res[1])`
# * Significant hoger aantal observaties bij een negatief BSA , *z* = `r Round_and_format(PH_res[2])`
# * Geen significant verschillend aantal observaties bij een uitgesteld BSA , *z* = `r Round_and_format(PH_res[3])`
# 
# <!-- ## /TEKSTBLOK: Chi2-toets post-hoc2.R-->
# 
# ## Rapportage
# <!-- ## TEKSTBLOK: Chi-kwadraat5.R-->
# De *Chi-kwadraat toets voor goodness of fit* is uitgevoerd om te onderzoeken of de verdeling van het BSA van studenten Maritieme Techniek overeenkomt met de verdeling van de gehele universiteit waar deze opleiding onder valt (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA). De verdeling van het BSA van de instromende studenten Maritieme Techniek is significant verschillend van de verdeling van de gehele universiteit, &chi;^2^~`r vdf`~ = `r vchi2`, *p* < 0,001. 
# 
# Uit de post-hoc toetsen blijkt dat het aantal studenten met een positief BSA significant lager is dan het percentage van de gehele universiteit (`r Round_and_format(Proptab[2])`%, *z* = `r Round_and_format(PH_res[1])`), het aantal studenten met een negatief BSA significant hoger is dan het percentage van de gehele universiteit (`r Round_and_format(Proptab[1])`%, *z* = `r Round_and_format(PH_res[2])`) en het percentage studenten met een uitgesteld BSA niet significant verschillend is van de gehele universiteit (`r Round_and_format(Proptab[3])`%, *z* = `r Round_and_format(PH_res[3])`). De resultaten suggereren dat de opleiding Maritieme Technieken qua BSA dus afwijkt van de gehele universiteit waarbij het aantal positieve BSA's lager en het aantal negatieve BSA's hoger in vergelijking tot de gehele universiteit.
# <!-- ## /TEKSTBLOK: Chi-kwadraat5.R-->

# # Multinomiaaltoets
# 
# ## Uitvoering
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets1.R -->
# Voer de *multinomiaaltoets*  uit te onderzoeken of de verdeling van de BSA mogelijkheden van de studenten Maritieme Techniek overeenkomt met de verdeling van de gehele universiteit (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA). Deze toets is een alternatief voor de *Chi-kwadraat toets voor goodness of fit* bij een laag aantal observaties. Er is een subset `BSA_Maritieme_techniek_steekproef` van de dataset `BSA_Maritieme_techniek` ingeladen met daarin een lager aantal observaties.
# <!-- ## /TEKSTBLOK: Binomiaaltoets1.R -->
# 
# Het is informatief om de frequenties en de percentages van de drie mogelijkheden van het BSA te bepalen voor de studenten Maritieme Techniek.
# 
# <!-- ## OPENBLOK: Binomiaaltoets3.R -->

# In[ ]:


table(BSA_Maritieme_techniek_steekproef$BSA_advies)


# In[ ]:


100*prop.table(table(BSA_Maritieme_techniek_steekproef$BSA_advies))


# <!-- ## /OPENBLOK: Binomiaaltoets3.R -->
# 
# <!-- ## CLOSEDBLOK: Binomiaaltoets3_3.R -->

# In[ ]:


Tab2 <- table(BSA_Maritieme_techniek_steekproef$BSA_advies)
Proptab2 <- 100*prop.table(table(BSA_Maritieme_techniek_steekproef$BSA_advies))


# <!-- ## /CLOSEDBLOK: Binomiaaltoets3_3.R -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets4.R -->
# Het aantal studenten met een positief BSA is `r Round_and_format(Tab2[2])` (`r Round_and_format(Proptab2[2])`%), met een negatief BSA is `r Round_and_format(Tab2[1])` (`r Round_and_format(Proptab2[1])`%) en met een uitgesteld BSA is `r Round_and_format(Tab2[3])` (`r Round_and_format(Proptab2[3])`%). Het lijkt erop dat het percentage studenten met een positief BSA hoger is dan het percentage van de gehele universiteit (70%) en dat het percentage studenten met een negatief BSA juist lager is dan dat van de gehele universiteit (20%). De *multinomiaaltoets* toetst of dit verschil significant is.
# <!-- ## /TEKSTBLOK: Binomiaaltoets4.R -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets5.R -->
# Bereken de verwachte frequentie met het argument `chisq.test()$expected` van de functie `chisq.test()`. De argumenten van de functie zijn de tabel met daarin de hoeveelheid studenten voor de drie mogelijkheden van het BSA `Tabel_volgorde` en een vector die aangeeft wat de verwachte proporties[^4] zijn voor het aantal studenten met respectievelijk een positief, negatief of uitgesteld BSA `p = c(0.7, 0.2, 0.1)`. Let hierbij goed op dat de volgorde van de BSA mogelijkheden in de tabel overeenkomt met de volgorde van de proporties.
# <!-- ## /TEKSTBLOK: Binomiaaltoets5.R -->
# 
# <!-- ## OPENBLOK: Binomiaaltoets6.R -->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten per BSA mogelijkheid
Tabel <- table(BSA_Maritieme_techniek_steekproef$BSA_advies)

# Zet de tabel op volgorde Positief, Negatief, Uitgesteld
(Tabel_volgorde <- Tabel[c("Positief", "Negatief", "Uitgesteld")])

# Voer de toets uit
chisq.test(Tabel_volgorde, p = c(0.7, 0.2, 0.1))$expected


# <!-- ## /OPENBLOK: Binomiaaltoets6.R -->
# 
# <!-- ## CLOSEDBLOK: Binomiaaltoets6_1.R -->

# In[ ]:


exp <- chisq.test(Tabel_volgorde, p = c(0.7, 0.2, 0.1))$expected


# <!-- ## /CLOSEDBLOK: Binomiaaltoets6_1.R -->
# 
# De verwachte frequentie voor studenten met een uitgesteld BSA is kleiner dan 5. Dit betekent dat er in meer dan 20% van de categorieën een verwachte frequentie van minder dan 5 is en dat er dus niet voldaan is aan de assumptie van verwachte frequenties. Voer daarom de *multinomiaaltoets* uit.
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets7.R -->
# Voer de *multinomiaaltoets* uit met de functie `multinomial.test()` van het package `RVAideMemoire` met als argument een vector met daarin de hoeveelheid studenten voor de drie mogelijkheden van het BSA `Vector_volgorde` en een vector die aangeeft wat de verwachte proporties[^4] zijn voor het aantal studenten met respectievelijk een positief, negatief of uitgesteld BSA `p = c(0.7, 0.2, 0.1)`. Deze functie vereist een vector wat de reden is dat de tabel met de aantallen observaties per categorie omgezet wordt in een vector. Let hierbij goed op dat de volgorde van de BSA mogelijkheden in de tabel overeenkomt met de volgorde van de proporties.
# <!-- ## /TEKSTBLOK: Binomiaaltoets7.R -->
# 
# <!-- ## OPENBLOK: Binomiaaltoets8.R-->

# In[ ]:


# Laad het package in
library(RVAideMemoire)

# Maak een tabel met daarin de aantallen studenten per BSA mogelijkheid
Tabel <- table(BSA_Maritieme_techniek_steekproef$BSA_advies)

# Zet de tabel op volgorde Positief, Negatief, Uitgesteld
Tabel_volgorde <- Tabel[c("Positief", "Negatief", "Uitgesteld")]

# Zet de tabel om in een vector voor de functie multinomial.test
Vector_volgorde <- as.numeric(Tabel_volgorde)

# Voer de toets uit
multinomial.test(Vector_volgorde, p = c(0.7, 0.2, 0.1))


# <!-- ## /OPENBLOK: Binomiaaltoets8.R-->
# 
# <!-- ## CLOSEDBLOK: Binomiaaltoets9.R -->

# In[ ]:


# Laad het package in
library(RVAideMemoire)

# Maak een tabel met daarin de aantallen studenten per BSA mogelijkheid
Tabel <- table(BSA_Maritieme_techniek_steekproef$BSA_advies)

# Zet de tabel op volgorde Positief, Negatief, Uitgesteld
Tabel_volgorde <- Tabel[c("Positief", "Negatief", "Uitgesteld")]

# Zet de tabel om in een vector voor de functie multinomial.test
Vector_volgorde <- as.numeric(Tabel_volgorde)

# Voer de toets uit
multitoets <- multinomial.test(Vector_volgorde, p = c(0.7, 0.2, 0.1))

# Sla p-waarde op
mp <- Round_and_format(multitoets$p.value)


# <!-- ## /CLOSEDBLOK: Binomiaaltoets9.R -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets10.R-->
# * p-waarde = `r mp`, dus de nulhypothese kan niet worden verworpen.[^5]  
# 
# <!-- ## /TEKSTBLOK: Binomiaaltoets10.R-->

# ## Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage2.R-->
# 
# De *multinomiaaltoets* is uitgevoerd om te onderzoeken of de verdeling van het BSA van studenten Maritieme Techniek overeenkomt met de verdeling van de gehele universiteit waar deze opleiding onder valt (70% positief BSA, 20% negatief BSA en 10% uitgesteld BSA) voor een dataset met een laag aantal observaties. De verdeling van het BSA van de instromende studenten van de universiteit verschilt niet significant van de landelijke verdeling (*p* = `r mp`). Het aantal studenten met een positief BSA is `r Round_and_format(Tab2[2])` (`r Round_and_format(Proptab2[2])`%), met een negatief BSA is `r Round_and_format(Tab2[1])` (`r Round_and_format(Proptab2[1])`%) en met een uitgesteld BSA is `r Round_and_format(Tab2[3])` (`r Round_and_format(Proptab2[3])`%). De resultaten suggereren dat de opleiding Maritieme Technieken qua BSA niet afwijkt van de gehele universiteit.
# 
# <!-- ## /TEKSTBLOK: Rapportage2.R-->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





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
# <!-- ## TEKSTBLOK: Extra-Bron.R -->
# 
# <!-- ## /TEKSTBLOK: Extra-Bron.R -->
# 
