#!/usr/bin/env python
# coding: utf-8
---
title: "Gepaarde t-toets"
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

# In[ ]:


# doorlinken naar de Wilcoxon Signed Rank Test
# linken naar blz transformeren data 


# <!-- ## OPENBLOK: Data-aanmaken.R -->

# In[ ]:


source(paste0(here::here(),"/01. Includes/data/02.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik de *gepaarde t-toets* om te toetsen of de gemiddelden van twee (herhaalde) metingen van een groep verschillen en om te toetsen of de gemiddelden van twee gepaarde groepen van elkaar verschillen.[^1] 
# 
# # Onderwijscasus
# <div id ="casus">
# Voor het verminderen van de studielast van studenten biedt het Centrum voor Studentbegeleiding van een universiteit een cursus Plannen aan. De cursus is bedoeld om studenten beter inzicht te geven in de gevolgen van de planning van hun studielast. De cursus wordt tussen twee onderwijsperiodes in gegeven. Voor en na de cursus moeten de studenten gedurende een onderwijsperiode een logboek bijhouden over hun studiegedrag. De cursuscoördinator vraagt zich af of er een verandering in het aantal studieuren is na deelname aan de cursus.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het gemiddeld aantal uren studeren per onderwijsperiode verandert niet na de cursus, µ~T0~ = µ~T1~  
# 
# *H~A~*: Het gemiddeld aantal uren studeren per onderwijsperiode verandert na de cursus, µ~T0~ ≠ µ~T1~ 
# </div>
# 
# # Assumpties
# Om een valide resultaat te bereiken moet er, voordat de toets kan worden uitgevoerd, aan een aantal voorwaarden voldaan worden.
# 
# ## Normaliteit
# De *gepaarde t-toets* gaat ervan uit dat de verschillen tussen de gepaarde observaties (verschilscores) normaal verdeeld zijn. Ga er bij een aantal deelnemers[^13] *n* groter dan 100 vanuit dat de *gepaarde t-toets* robuust genoeg is om uit te voeren zonder dat er voldaan is aan de assumptie van normaliteit.   
# 
# Controleer de assumptie van normaliteit met de volgende stappen:  
# 1. Controleer de verschilscores visueel met een histogram, een Q-Q plot en een boxplot.  
# 2. Toets of de verschilscores normaal verdeeld is met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (*n* < 50) met de *Shapiro-Wilk test*.[^3]<sup>, </sup>[^4]  
# 
# De eerste stap heeft als doel een goede indruk te krijgen van de verdeling van de steekproef. In de tweede stap wordt de assumptie van normaliteit getoetst. De statistische toets laat zien of de verdeling van de steekproef voldoet aan de assumptie van normaliteit.
# 
# <!-- ## TEKSTBLOK: Link1.R-->
# Als blijkt dat de verschilscores niet normaal verdeeld is, transformeer dan de afhankelijke variabele eventueel en bepaal daarna of de verschilscores wel normaal verdeeld is [^5] of gebruik de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html).[^6]<sup>, </sup>[^7]
# <!-- ## /TEKSTBLOK: Link1.R-->
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset ingeladen met het gemiddeld aantal uren studeren voor (T~0~) en na (T~1~) de cursus. De gemiddeldes per onderwijsperiode zijn afgerond op 1 decimaal in de dataset `Studielogboek`. 
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Studielogboek)

## Laatste 6 observaties
tail(Studielogboek)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# Selecteer beide groepen, sla deze op in een vector en bereken het verschil in de afhankelijke variabelen (het aantal studieuren) voor alle deelnemers (de studenten).
# <!-- ## OPENBLOK: Data-selecteren.R -->

# In[ ]:


Uren_studeren_T0 <- Studielogboek[Studielogboek$Meetmoment == "T0", 2]
Uren_studeren_T1 <- Studielogboek[Studielogboek$Meetmoment == "T1", 2]
Uren_studeren_verschil <- Uren_studeren_T1 - Uren_studeren_T0


# <!-- ## /OPENBLOK: Data-selecteren.R -->
# 
# <!-- ## TEKSTBLOK: Data-inspectie.R-->
# Inspecteer de data met `length()`, `mean()`en `sd()` om meer inzicht te krijgen in de data.
# <!-- ## /TEKSTBLOK: Data-inspectie.R-->

# <!-- ## OPENBLOK: numpy-inladen.R -->
# 
# <!-- ## /OPENBLOK: numpy-inladen.R -->
# 

# <div class = "col-container">
#   <div class ="col">
# <!-- ## OPENBLOK: Data-beschrijven-1.R -->

# In[ ]:


## aantallen, gemiddelde en standaarddeviatie voor cursus
length(Uren_studeren_T0)
mean(Uren_studeren_T0)
sd(Uren_studeren_T0)


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Data-beschrijven-2.R -->

# In[ ]:


## aantallen, gemiddelde en standaarddeviatie na cursus
length(Uren_studeren_T1)
mean(Uren_studeren_T1)
sd(Uren_studeren_T1)


# <!-- ## /OPENBLOK: Data-beschrijven-2.R -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven.R -->

# In[ ]:


vMean_t0 <- Round_and_format(mean(Uren_studeren_T0))
vSD_t0   <- Round_and_format(sd(Uren_studeren_T0))
vN_t0    <- Round_and_format(length(Uren_studeren_T0))
vMean_t1 <- Round_and_format(mean(Uren_studeren_T1))
vSD_t1   <- Round_and_format(sd(Uren_studeren_T1))
vN_t1    <- Round_and_format(length(Uren_studeren_T1))


# <!-- ## /CLOSEDBLOK: Data-beschrijven.R -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# * Gemiddeld uren studeren T~0~ (standaardafwijking): `r vMean_t0` (`r vSD_t0`). *n* = `r vN_t0`.
# * Gemiddeld uren studeren T~1~ (standaardafwijking): `r vMean_t1` (`r vSD_t1`). *n* = `r vN_t1`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# 
# ## Visuele inspectie van normaliteit
# Geef de verdeling van de verschilscores van het aantal uur studeren voor en na het volgen van de cursus visueel weer met een histogram, Q-Q plot en boxplot.
# 
# ### Histogram
# 
# Focus bij het analyseren van een histogram[^18] op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters. Een normale verdeling is symmetrisch, heeft één top en geen uitbijters.[^8]<sup>, </sup>[^9]
# 
# <!-- ## OPENBLOK: Histogram.R -->

# In[ ]:


## Histogram met ggplot2
library(ggplot2)

# Zet de variable om in een dataframe zodat het met ggplot gevisualiseerd kan worden
Uren_studeren_verschil_dataframe <- as.data.frame(Uren_studeren_verschil)

ggplot(Uren_studeren_verschil_dataframe,
  aes(x = Uren_studeren_verschil)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 1,
                 color = "grey30",
                 fill = "#0089CF") +
  geom_density(alpha = .2, adjust = 1) +
  xlab("Verschilscores uren studeren") +
  ylab("Frequentiedichtheid") +
  scale_x_continuous(
    labels = as.character(seq(-12, 16, 4)),
    breaks = seq(-12, 16, 4)) + 
     labs(title = "Verschilscores uren studeren voor en na cursus")


# <!-- ## /OPENBLOK: Histogram.R -->
# 
# De histogram lijkt niet geheel symmetrisch, maar heeft één top en geen outliers. Er lijken geen grote afwijkingen van de normaalverdeling te zijn.

# ### Q-Q plot
# <!-- ## TEKSTBLOK: QQplot.R-->
# Gebruik `qqnorm()` en `qqline()` met `pch = 1`om een Q-Q plot te maken, met als datapunten kleine cirkels.
# <!-- ## /TEKSTBLOK: QQplot.R-->
# 
# <!-- ## OPENBLOK: QQplot-inladen.R -->
# 
# <!-- ## /OPENBLOK: QQplot-inladen.R -->
# 
# Als over het algemeen de meeste datapunten op de lijn liggen, kan aangenomen worden dat de data bij benadering normaal verdeeld is.
# 
# <!-- ## OPENBLOK: QQplot-1.R -->

# In[ ]:


qqnorm(Uren_studeren_verschil, 
       pch = 1,
       main = "Normaal Q-Q plot verschilscores uren studeren voor en na cursus",
       ylab = "kwantielen in data",
       xlab = "Theoretische kwantielen")
qqline(Uren_studeren_verschil)


# <!-- ## /OPENBLOK: QQplot-1.R -->
# 
# In deze casus liggen de meeste datapunten op of vlakbij de lijn. Hoewel er bij de uiteinden van de verdeling wat afwijkingen zijn, duidt deze grafiek op een goede benadering van de normaalverdeling.
# 
# ### Boxplot
# 
# De doos van de boxplot geeft de middelste 50% van de verschilscores in studieuren uit het studielogboek weer. De zwarte lijn binnen de box is de mediaan. In de staarten of snorreharen zitten de eerste 25% en de laatste 25%. Cirkels visualiseren mogelijke uitbijters.[^8]<sup>, </sup>[^9]
# 
# <!-- ## OPENBLOK: Boxplot.R -->
# ``` {r Boxplot}
# ## Boxplot
# boxplot(Uren_studeren_verschil,
#         main = "Boxplot van verschilscore uren studeren voor en na cursus")
# ```
# <!-- ## /OPENBLOK: Boxplot.R -->
# 
# De boxplotten geven de spreiding weer in de verschilscores van het aantal uur studeren voor en na het volgen van de cursus voor deelnemers aan de cursus. De boxplot is niet helemaal symmetrisch, maar beide snorreharen zijn ongeveer even lang en de mediaan ligt ongeveer in het midden. Daarom zijn de verschilscores bij benadering normaal verdeeld.
# 
# Op basis van de grafieken lijken er geen grote afwijkingen van de normaalverdeling voor de verschillen in studieuren te zijn, maar normaliteit kan ook getoetst worden met statistische toetsen.
# 
# ## Toetsen van normaliteit
# Om te controleren of de verschilscores normaal verdeeld zijn, kan de normaliteit getoetst worden. Twee veelgebruikte toetsen zijn: de *Kolmogorov-Smirnov test* en de *Shapiro-Wilk test*.
# 
# ### Kolmogorov-Smirnov 
# De *Kolmogorov-Smirnov test* toetst het verschil tussen twee verdelingen. Standaard toetst deze test het verschil tussen een normale verdeling en de verdeling van de steekproef. De Lilliefors correctie is vereist als het gemiddelde en de standaardafwijking niet van tevoren bekend of bepaald zijn, wat meestal het geval is bij een steekproef. Als de p-waarde kleiner dan 0,05 is, is de verdeling van de steekproef significant verschillend van de normale verdeling.
# 
# <!-- ## TEKSTBLOK: Lilliefors-test1.R -->
# 
# <!-- ## /TEKSTBLOK: Lilliefors-test1.R -->
# 
# <!-- ## OPENBLOK: Library-nortest.R -->

# In[ ]:


library(nortest)


# <!-- ## /OPENBLOK: Library-nortest.R -->
# 
# <!-- ## OPENBLOK: Lilliefors-test-1.R -->
# ``` {r Lilliefors Test-1, warning=FALSE}
# lillie.test(Uren_studeren_verschil)
# ```
# <!-- ## /OPENBLOK: Lilliefors-test-1.R -->
# 
# <!-- ## TEKSTBLOK: Lilliefors-test-2.R -->
# De test heeft een p-waarde van `r Round_and_format(lillie.test(Uren_studeren_verschil)$p.value)`, dus er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. De *gepaarde t-toets* kan uitgevoerd worden. 
# <!-- ## /TEKSTBLOK: Lilliefors-test-2.R -->
# 
# ### Shapiro-Wilk Test
# De *Shapiro-Wilk test* is een soortgelijke test als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (*n* < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de steekproef significant verschillend van de normale verdeling.
# 
# <!-- ## CLOSEDBLOK: data inladen-2.R -->
# 
# <!-- ## /CLOSEDBLOK: data inladen-2.R -->
# 
# <!-- ## TEKSTBLOK: Shapiro-Wilk-test.R -->
# Er is een subset van de verschillen tussen het aantal studieuren op T~0~ en T~1~ ingeladen, `Uren_studeren_verschil_n30`, met daarin `r length(Uren_studeren_verschil_n30)` observaties. Voor een relatief kleine steekproef als deze is de *Shapiro-Wilk Test* geschikt.
# 
# <!-- ## /TEKSTBLOK: Shapiro-Wilk-test.R -->
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.R -->
# ``` {r Shapiro-Wilk Test-1, warning=FALSE}
# shapiro.test(Uren_studeren_verschil_n30)
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-1.R -->
# 
# <!-- ## TEKSTBLOK: Shapiro-Wilk-test-2.R -->
# Voor deze subset is de p-waarde `r Round_and_format(shapiro.test(Uren_studeren_verschil_n30)$p.value)`, dus er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. De *gepaarde t-toets* kan uitgevoerd worden.  
# <!-- ## /TEKSTBLOK: Shapiro-Wilk-test-2.R -->
# 
# ## Gepaarde t-toets
# <!-- ## TEKSTBLOK: T-test.R -->
# Gebruik de functie `t.test()` met het argument `paired = TRUE` om een *gepaarde t-toets* uit te voeren. Gebruik hier weer het hele dataframe `Studielogboek`. Het eerste argument bestaat uit de afhankelijke variabele `Uren_studeren` en de groepvariabele `Meetmoment`. Het argument `alternative = two.sided"` geeft aan dat er tweezijdig getoetst wordt.
# <!-- ## /TEKSTBLOK: T-test.R -->

# <!-- ## OPENBLOK: T-toets.R -->

# In[ ]:


t.test(Uren_studeren ~ Meetmoment, Studielogboek, 
       paired = TRUE,
       alternative = "two.sided")


# <!-- ## /OPENBLOK: T-toets.R -->
# <!-- ## CLOSEDBLOK: T-test.R -->

# In[ ]:


t <- t.test(Uren_studeren ~ Meetmoment, Studielogboek, paired = TRUE)
vT_waarde <- Round_and_format(t$statistic)
vN <- t$parameter + 1
vDF <- t$parameter
vconf.int1 <- Round_and_format(-t$conf.int[1])
vconf.int2 <- Round_and_format(-t$conf.int[2])
vDiffMean <- Round_and_format(t$estimate*-1)


# <!-- ## /CLOSEDBLOK: T-test.R -->
# <!-- ## TEKSTBLOK: T-test2.R -->
# * *t*~`r vDF`~ = `r vT_waarde`, *p* < 0,0001
# * Vrijheidsgraden, *df* = *n* -1 = `r vN`-1 = `r vDF`  
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen [^10]
# * De output van deze functie berekend het verschil in gemiddelde als µ~verschil~ = µ~T0~ - µ~T1~. Om het duidelijker te maken wordt in deze toetspagina het verschil andersom berekend, dus µ~verschil~ = µ~T1~ - µ~T0~.
# * 95%-betrouwbaarheidsinterval: bij het herhalen van het experiment met verschillende steekproeven van de populatie zal 95% van de betrouwbaarheidsintervallen de daadwerkelijke parameter bevatten, het verschil tussen het aantal studieuren voor en na de cursus,  µ~verschil~ = µ~T1~ - µ~T0~. In deze casus is het interval tussen `r vconf.int1` en `r vconf.int2`. Aangezien 0 niet in dit interval zit, is er een significant verschil tussen µ~T1~ en µ~T0~.
# * Het absolute gemiddelde verschil tussen de twee groepen is `r vDiffMean`.
# 
# <!-- ## /TEKSTBLOK: T-test2.R -->
# 
# De p-waarde geeft aan of het verschil tussen twee groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^11] Een veel gebruikte effectmaat is Cohen's *d*. Cohen's *d* geeft een gestandaardiseerd verschil weer: het verschil in gemiddelden tussen twee groepen gecorrigeerd voor de standaardafwijking van de eerste meting (T~0~). Een indicatie om *d* te interpreteren is: rond 0,3 is een klein effect, rond 0,5 is een gemiddeld effect en rond 0,8 is een groot effect.[^12]  
# 
# <!-- ## TEKSTBLOK: Cohen-d.R -->
# Gebruik de functie `cohensD()` van het package `lsr` om de effectmaat te berekenen. Het eerste argument bestaat uit de afhankelijke variabele `Uren_studeren` en de groepvariabele `Meetmoment` en het tweede argument is de dataset `Studielogboek`. Gebruik het argument `method = x.sd` om de effectmaat te berekenen op basis van de standaardafwijking van de observaties voor de cursus (T~0~).
# <!-- ## /TEKSTBLOK: Cohen-d.R  -->
# 
# <!-- ## OPENBLOK: Cohens-d-test.R -->

# In[ ]:


library(lsr)
cohensD(Uren_studeren ~ Meetmoment, Studielogboek, method = "x.sd")


# <!-- ## /OPENBLOK: Cohens-d-test.R -->
# 
# <!-- ## CLOSEDBLOK: Cohens-d-test.R -->

# In[ ]:


vD_waarde <- cohensD(Uren_studeren ~ Meetmoment, Studielogboek, method = "x.sd")


# <!-- ## CLOSEDBLOK: Cohens-d-test.R -->
# 
# <!-- ## TEKSTBLOK: Cohens-d-test.R -->
# *d* = `r vD_waarde`. De sterkte van het effect van de tutor op het cijfer is groot. 
# <!-- ## /TEKSTBLOK: Cohens-d-test.R -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# Een *gepaarde t-toets* is uitgevoerd om te toetsen of het gemiddeld aantal uur studeren van de studenten is veranderd na deelname aan de cursus Plannen. Het verschil tussen het gemiddelde van T~0~ (*M~T0~* = `r vMean_t0`, *SD~T0~* = `r vSD_t0`) en het gemiddelde van T~1~ (*M~T1~* =`r vMean_t1`, *SD~T1~* = `r vSD_t1`) is significant, *t* ~`r vDF`~ = `r vT_waarde`, *p* < 0,0001. Gemiddeld studeren de studenten `r vDiffMean` uur meer na deelname aan de cursus, dit is een groot effect. Het 95%-betrouwbaarheidsinterval voor het verschil tussen het gemiddelde van beide groepen (T~1~ - T~0~) loopt van `r vconf.int1` tot `r vconf.int2`. Aan de hand van de resultaten kan geconcludeerd worden dat de studenten, na deelname aan de cursus Plannen, meer tijd besteden aan hun studie dan daarvoor.

# | Meting     | N         | M            | SD         |
# | --------   | --------- | ------------ | ---------- |
# | T~0~       | `r vN_t0` | `r vMean_t0` | `r vSD_t0` |
# | T~1~       | `r vN_t1` | `r vMean_t1` | `r vSD_t1` |
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# *Tabel 1. Groepsgrootte, gemiddeld tentamencijfer en standaarddeviatie van het aantal uren door studenten besteed aan hun studie per meetmoment*

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Wikipedia (21 augustus 2019). *Student's t-test*. [Wikipedia](https://en.wikipedia.org/wiki/student%27s_t-test).
# [^2]: Lumley, T., Diehr, P., Emerson, S., & Chen, L. (2002). The importance of the normality assumption in large public health data sets. *Annu Rev Public Health, 23*, 151-69. doi: 10.1146/annurev.publheath.23.100901.140546 http://rctdesign.org/techreports/arphnonnormality.pdf 
# [^3]: Van Geloven, N. (25 september2013). *Wilcoxon signed rank toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Wilcoxon_signed_rank_toets).
# [^4]: Laerd statistics (2018). *Testing for Normality using SPSS Statistics*. [Testing for Normality using SPSS Statistics](https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php).  
# [^5]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^6]: Universiteit van Amsterdam (14 juli 2014). *Normaliteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).  
# [^7]: De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) maakt een rangschikking van de data. Hierdoor is de test verdelingsvrij en is normaliteit geen assumptie. Ook zijn uitbijters minder van invloed op het eindresultaat. Toch wordt er voor deze test minder vaak gekozen, doordat bij het maken van een rankschikking de data informatie verliest. Als de data wel normaal verdeeld is, heeft de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) minder onderscheidend vermogen dan wanneer de *gepaarde t-toets* uitgevoerd zou worden.  
# [^8]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^9]: Uitbijters kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de uitbijters valide uitbijters zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van uitbijters kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde uitbijters te melden in een rapport.
# [^10]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen, houd hierbij rekening met type I en type II fouten.
# [^11]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^12]: Marshall, E., & Boggis, E. (2016). *The statistics tutor’s quick guide to commonly used statistical tests*. http://www.statstutor.ac.uk/resources/uploaded/tutorsquickguidetostatistics.pdf 
# [^13]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
# <!-- ## TEKSTBLOK: Extra-Bron.R -->
# 
# <!-- ## /TEKSTBLOK: Extra-Bron.R -->
