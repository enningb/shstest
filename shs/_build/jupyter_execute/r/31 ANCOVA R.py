#!/usr/bin/env python
# coding: utf-8
---
title: "ANCOVA"
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


set.seed(12345)
source(paste0(here::here(),"/01. Includes/data/31.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# Gebruik de *ANCOVA* bij het toetsen of de gemiddelden van groepen op basis van één of meer onafhankelijke categorische variabelen van elkaar verschillen na het corrigeren voor één of meerdere achtergrondvariabelen. In de casus behorend bij deze toetspagina is er één onafhankelijke variabele die de groepen definieert. Er wordt dus een *one-way ANCOVA* uitgevoerd.[^1] 
# 
# # Onderwijscasus
# <div id = "casus">
# 
# De docent van het vak Methoden & Statistiek van de faculteit Sociale Wetenschappen wil ontdekken of er verschillen zijn tussen studenten van verschillende opleidingen in het eindcijfer van zijn vak. Het vak wordt gevolgd door studenten Psychologie, Onderwijskunde en Sociologie. Uit ervaring blijkt dat het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer van de middelbare school ook van invloed is op het eindcijfer en dat dit nogal eens verschilt tussen studenten. Om een eerlijke vergelijking te maken, wilt hij daarom corrigeren voor het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer van de middelbare school. Op basis van de data van vorig jaar onderzoekt hij of er een verschil is tussen de drie opleidingen wat betreft het eindcijfer van het vak Methoden & Statistiek rekening houdend met het aantal gevolgde hoorcolleges.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil tussen de gemiddelde eindcijfers voor het vak Methoden & Statistiek voor studenten van de opleidingen Psychologie, Onderwijskunde en Sociologie na corrigeren voor het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer van de middelbare school.
# 
# *H~A~*: Er is een verschil tussen de gemiddelde eindcijfers voor het vak Methoden & Statistiek voor studenten van de opleidingen Psychologie, Onderwijskunde en Sociologie na corrigeren voor het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer van de middelbare school.
# 
# </div>

# # ANCOVA
# 
# Het doel van de *ANCOVA* is om de gemiddelde scores van groepen op een afhankelijke variabele te vergelijken rekening houdend met andere variabelen (covariaten) die ook invloed hebben op de afhankelijke variabele. In de huidige casus is het doel om de gemiddelde eindcijfers voor het vak Methoden & Statistiek te vergelijken voor studenten afkomstig van de opleidingen Psychologie, Onderwijskunde en Sociologie. Het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer van de middelbare school is echter ook van invloed op het eindcijfer. Als het aantal gevolgde hoorcolleges of het gemiddeld eindexamencijfer verschillend is voor studenten van de drie opleidingen, dan heeft dit gevolgen voor de gemiddelde eindcijfers per opleiding. Daarom is het nuttig om covariaten mee te nemen bij het vergelijken van gemiddelden van groepen.[^3]
# 
# De *ANCOVA* verschilt van de *one-way ANOVA* en *factoriële ANOVA* door het gebruik van covariaten. Het gebruik van covariaten heeft twee voordelen. Het eerste voordeel is dat het ruis in de data wegneemt waardoor er meer onderscheidend vermogen[^2] is om een verschil tussen groepen te kunnen vinden. Als eindcijfers bepaald worden door zowel de opleiding als het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer van de student, dan kan het effect van de opleiding preciezer gevonden worden na het rekening houden met beide variabelen. Het tweede voordeel is dat er rekening gehouden wordt met verschillen in de achtergrondvariabelen voor de verschillende groepen. Als studenten van een bepaalde opleiding structureel minder hoorcolleges volgen, zal dat kunnen leiden tot lagere eindcijfers. De reden voor de lagere cijfers is dan dat de studenten minder hoorcolleges volgen en niet dat ze van een bepaalde opleiding afkomstig zijn. Als de studenten van die opleiding meer hoorcolleges zouden volgen, zou er misschien geen verschil met studenten van andere opleidingen zijn. Op deze manier kan opnieuw het effect van de opleiding preciezer gevonden worden. Het is alsof de opleidingen vergeleken worden voor studenten die hetzelfde aantal hoorcolleges volgen en hetzelfde gemiddeld eindexamencijfer op de middelbare school hebben behaald.[^3]
# 
# # Experimenteel vs. cross-sectioneel
# 
# Voor de interpretatie en het gebruik van de *ANCOVA* is het van belang om rekening te houden met de opzet van een onderzoek. Een onderzoek kan worden geplaatst binnen experimenteel en cross-sectioneel onderzoek. Bij experimenteel onderzoek worden deelnemers[^19] willekeurig aan verschillende groepen toegewezen en worden groepen vergeleken. Een voorbeeld is dat studenten Methoden & Statistiek willekeurig in twee groepen worden verdeeld, waarbij beide groepen een andere onderwijsmethode gebruiken. Bij cross-sectioneel onderzoek worden deelnemers niet aan groepen toegewezen, maar wordt er data verzameld van de deelnemers op basis waarvan groepen kunnen worden bepaald. De huidige casus is een voorbeeld van cross-sectioneel onderzoek. De studenten worden in groepen ingedeeld op basis van de opleiding die zij volgen. De opleiding is echter niet willekeurig toegewezen, want studenten hebben hun opleiding zelf gekozen. Cross-sectioneel onderzoek wordt vaak uitgevoerd omdat een experiment niet mogelijk is. Bepaalde variabelen kunnen niet willekeurig worden toegewezen, denk hierbij aan geslacht, opleiding en land van hoogste vooropleiding.[^3]
# 
# Bij experimenteel onderzoek verschillen de groepen alleen wat betreft hun groepslidmaatschap. Omdat de deelnemers willekeurig zijn toegewezen, zouden de achtergrondvariabelen gelijk verdeeld moeten zijn voor de verschillende groepen. Het doel van de *ANCOVA* is in dat geval om ruis weg te nemen zodat er meer onderscheidend vermogen is om een verschil tussen groepen te vinden. Bij cross-sectioneel onderzoek verschillen de groepen mogelijk meer van elkaar dan alleen in hun groepslidmaatschap. Bepaalde achtergrondvariabelen kunnen ook verschillend zijn voor de verschillende groepen. Als deze variabelen gerelateerd zijn aan de afhankelijke variabele, dan heeft dit invloed op de groepsgemiddelden. In dat geval is het nuttig om te corrigeren voor deze variabelen, bijvoorbeeld met een *ANCOVA*. Bij cross-sectioneel onderzoek is het doel van de *ANCOVA* dus om ruis weg te nemen en rekening te houden met verschillen in achtergrondvariabelen. Let goed op bij de interpretatie van de *ANCOVA* bij cross-sectioneel onderzoek. Na het corrigeren voor achtergrondvariabelen is er nog steeds geen sprake van een experimenteel onderzoek. Een verschil in gemiddelde tussen de groepen wordt dus niet veroorzaakt door de groepen. In de huidige casus kan er een verschil tussen de opleidingen gevonden worden na het corrigeren voor het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer. Dit betekent echter niet dat het lidmaatschap van een bepaalde opleiding ook de oorzaak is van verschillen in de eindcijfers Methoden & Statistiek. Let dus goed op dat de resultaten niet op deze manier geïnterpreteerd en gerapporteerd worden.[^3]
# 
# # Uitleg assumpties
# 
# Om een valide resultaat te vinden met de *ANCOVA*, dient er aan een aantal assumpties voldaan te worden.[^1]<sup>,</sup>[^3] In deze sectie worden de assumpties allen toegelicht en worden de opties bij het niet voldoen aan de assumptie weergegeven. Verderop in de toetspagina worden de assumpties getoetst met de dataset van de onderwijscasus.
# 
# ## Outliers
# 
# Voordat gestart kan worden met de *ANCOVA*, moet de data gescreend worden op de aanwezigheid van outliers. Outliers (uitbijters) zijn observaties die sterk afwijken van de overige observaties. Univariate outliers zijn observaties die afwijken voor één specifieke variabele, zoals een student die twintig jaar over zijn studie heeft gedaan. Multivariate outliers zijn observaties die afwijken door de combinatie van meerdere variabelen, zoals een persoon van 18 jaar met een inkomen van €100.000,-. De leeftijd van 18 jaar is geen outlier op zichzelf en een inkomen van €100.000,- is dat ook niet. Echter, de combinatie van beide zorgt ervoor dat de observatie vrij onwaarschijnlijk is.[^4]
# 
# Na het vinden van een outlier is de volgende stap om een goede oplossing voor de outlier te bedenken. Het is van belang hier goed over na te denken en niet zomaar een outlier te verwijderen met als enige argument dat het een outlier is. In het algemeen kan er onderscheid gemaakt worden tussen onmogelijke en onwaarschijnlijke outliers.[^5] Een onmogelijke outlier is een observatie die technisch gezien niet kan kloppen, bijvoorbeeld een leeftijd van 1000 jaar, een negatief salaris of een man die zwanger is. Bij deze outliers is het een optie om de waarde te vervangen als er een overduidelijke fout bij het invoeren van de data is gemaakt. Een andere optie is de waarde te verwijderen. Een onwaarschijnlijke outlier is een observatie die technisch gezien wel kan, maar heel erg afwijkt van de overige observaties. De rijksten der aarde zijn in de stad of het dorp waar zij wonen qua vermogen waarschijnlijk een outlier. Maar het zijn bestaande personen dus het verwijderen van de observatie zou hier foutief zijn. Opties in deze situatie zijn de variabele(n) te transformeren, de outlier gewoon mee te nemen in de analyse of de analyse met en zonder de outlier uit te voeren en beide te rapporteren. Ook is het niet verboden om de outlier toch te verwijderen, maar het is in dat geval wel van belang dit transparant te rapporteren en op een goede wijze te beargumenteren.[^5]
# 
# Bij de *ANCOVA* zijn er drie nuttige methoden om outliers te vinden.[^3]
# 
# ### Boxplots en standaardiseren
# 
# Begin voor de analyse met het screenen van de variabelen in de dataset op de aanwezigheid van univariate outliers. Voor continue variabelen bestaat deze screening uit het visualiseren van de variabele met een boxplot en het standaardiseren[^6] van de variabele. Als een observatie een gestandaardiseerde score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. In dat geval wijkt de observatie namelijk meer dan drie standaardafwijkingen af van het gemiddelde van de variabele. Gebruik zowel de boxplot als de standaardisering om outliers te vinden voor continue variabelen.[^5]
# 
# ### Mahalanobis afstand
# 
# Multivariate outliers zijn deelnemers met een combinatie van observaties op verschillende variabelen die erg afwijken van de overige deelnemers. Deze multivariate outliers kunnen geïdentificeerd worden met de Mahalanobis afstand. De Mahalanobis afstand is een maat die aangeeft in hoeverre de observaties van een deelnemer voor alle covariaten afwijken van de gemiddeldes van de covariaten. Het is een maat voor een afstand tussen twee punten als meerdere covariaten worden gebruikt. Gebruik de Mahalanaobis afstand als er meerdere covariaten zijn om te onderzoeken of er multivariate outliers zijn bij de covariaten.[^3] Als er slechts één covariaat is, dan hoeft de Mahalanobis afstand niet gebruikt te worden. Bereken de Mahalanobis afstand voor elke deelnemer en vergelijk deze met de criteriumwaarde. De criteriumwaarde wordt bepaald op basis van de chi-kwadraat score bij een aantal vrijheidsgraden dat gelijk is aan het aantal variabelen en een significantieniveau van 0,001 (of een zelf gekozen significantieniveau). In de code wordt toegelicht hoe de criteriumwaarde bepaald kan worden.[^4]
# 
# ### Cook's afstand
# 
# De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van de andere deelnemers wat betreft de waardes van de covariaten. Een andere manier om multivariate outliers te vinden is te bepalen hoeveel invloed een deelnemer heeft op de resultaten van de *ANCOVA*. Als de uitkomsten van de *ANCOVA* sterk veranderen als een bepaalde deelnemer weggelaten wordt uit de dataset, dan is deze deelnemer invloedrijk. Met behulp van Cook's afstand worden invloedrijke deelnemers ontdekt. Als Cook's afstand groter dan 1 is, wordt de deelnemer beschouwd als invloedrijk.
# 
# Hoewel de Mahalanobis afstand en Cook's afstand beide multivariate outliers identificeren, verschillen ze in het soort outlier waarop de focus ligt. Bij de Mahalanobis afstand worden afwijkende datapunten gevonden en bij Cook's distance invloedrijke datapunten. Het is echter niet zo dat een afwijkend datapunt ook tegelijkertijd invloedrijk is en dat een invloedrijk datapunt ook afwijkt. Een afwijkend datapunt kan ondanks zijn afwijking van de overige datapunten toch op een juiste manier voorspeld worden. En een invloedrijk datapunt hoeft niet per se sterk af te wijken van de overige datapunten wat betreft de waardes voor de covariaten. Houdt hier rekening mee bij het bepalen hoe om te gaan met de gevonden outlier(s).[^4]
# 
# ## Lineariteit
# 
# In de *ANCOVA* wordt aangenomen dat er een lineaire relatie is tussen elke covariaat en de afhankelijke variabele. Een lineaire relatie houdt in dat de toename of afname van de afhankelijke variabele als gevolg van de toename van de covariaat constant is: er is een rechte lijn door de data heen te trekken. Een voorbeeld van een lineaire en niet-lineaire relatie is weergegeven in Figuur 1. Bij de linkerfiguur kan er duidelijk een rechte lijn door de punten getrokken worden en is er dus sprake van een lineaire relatie. Bij de rechterfiguur is dit niet het geval, daar is er sprake van een curve in de relatie tussen de covariaat en afhankelijke variabele. Als er geen lineair verband is tussen de covariaat en de afhankelijke variabele, dan wordt er niet op de juiste manier gecorrigeerd voor de covariaat wat gevolgen heeft voor de validiteit van de *ANCOVA*.[^4]<sup>,</sup>[^8] 
# 
# De assumptie van lineariteit wordt onderzocht met behulp van scatter plots, zoals in onderstaande figuren. Deze assumptie hoeft alleen onderzocht te worden voor continue variabelen. Bij categorische variabelen krijgt elke categorie een aparte waarde waardoor er geen lineariteit kan zijn. Als er geen lineaire relatie is, is het transformeren van de afwijkende variabele een optie. De variabele kan op verschillende manieren getransformeerd[^7] worden zodat er alsnog een lineaire relatie ontstaat.
# 
# <div class = "col-container">
#   <div class="col">
# <!-- ## CLOSEDBLOK: Lineariteit1.R -->

# In[ ]:


set.seed(12345)
x <- rnorm(100,0,2)
y <- 3 + 1.2 * x + rnorm(100,0,1)
dataset <- data.frame(Afhankelijke_variabele = y, Covariaat = x)

ggplot(dataset, aes(x = Covariaat, y = Afhankelijke_variabele)) +
    geom_point() + ylab("Afhankelijke variabele") + 
  ggtitle("Lineare relatie")


# <!-- ## /CLOSEDBLOK: Lineariteit1.R -->
#   </div>
#   <div class = "col">
# <!-- ## CLOSEDBLOK: Lineariteit2.R -->

# In[ ]:


set.seed(12345)
x <- rnorm(100,0,2)
y <- 3 + 1.2 * x^2 + rnorm(100,0,1)
dataset <- data.frame(Afhankelijke_variabele = y, Covariaat = x)

ggplot(dataset, aes(x = Covariaat, y = Afhankelijke_variabele)) +
    geom_point()  + ylab("Afhankelijke variabele") +
  ggtitle("Niet-lineaire relatie")


# <!-- ## /CLOSEDBLOK: Lineariteit2.R -->
#   </div>
# </div>
# 
# *Figuur 1.  Voorbeeld van een lineaire (links) en niet-lineaire (rechts) relatie tussen een afhankelijke variabele en een covariaat.*
# 
# ## Normaliteit van residuën
# 
# Op basis van de groep van de deelnemer en de waarden van de covariaten kan voor elke deelnemer een voorspelling gemaakt worden voor de afhankelijke variabele. Het verschil tussen de voorspelling en de geobserveerde waarde heet het residu. De residuën van de *ANCOVA* moeten normaal verdeeld zijn met een gemiddelde van ongeveer 0. De assumptie wordt getoetst door een histogram te maken van de gestandaardiseerde residuën. Als de verdeling van de gestandaardiseerde residuën sterk afwijkt van de normale verdeling, is de assumptie geschonden. De *ANCOVA* is redelijk robuust ten opzichte van een schending van de assumptie van normaliteit. Als er kleine afwijkingen zijn, heeft dat relatief kleine gevolgen voor de validiteit van de toets. Bij grotere afwijkingen is het transformeren van de afhankelijke variabele een optie.[^2] Als dit niet werkt, dan is het een optie om de *ANCOVA* uit te voeren als *multipele lineaire regressie* en te bootstrappen; zie bijbehorende [toetspagina](28-Multipele-lineaire-regressie-R.html).

# ## Homoskedasticiteit
# 
# Homoskedasticiteit houdt in dat de variantie van de residuën niet afhangt van de waarden van de covariaten. Deze assumptie wordt getoetst door een scatter plot te maken van de voorspellingen van de *ANCOVA* versus de gestandaardiseerde residuën. Figuur 2 geeft een voorbeeld weer van homoskedasticiteit en heteroskedasticiteit. Bij heteroskedasticiteit is zichtbaar dat de variantie in de residuën toeneemt als de waarde van de voorspellingen toeneemt. Als deze assumptie geschonden is, is het een optie om de *ANCOVA* uit te voeren als *multipele lineaire regressie* en te bootstrappen; zie bijbehorende [toetspagina](28-Multipele-lineaire-regressie-R.html).[^4]
# 
# <div class = "col-container">
#   <div class="col">
# <!-- ## CLOSEDBLOK: Homoskedasticiteit1.R -->

# In[ ]:


set.seed(12345)
x <- rnorm(1000,10,2)
y <- rnorm(1000,0,1)
dataset <- data.frame(Residu = y, Voorspelling = x)

ggplot(dataset, aes(x = Voorspelling, y = Residu)) +
    geom_point() + ylab("Gestandaardiseerd residu") + 
  ggtitle("Homoskedasticiteit")


# <!-- ## /CLOSEDBLOK: Homoskedasticiteit1.R -->
#   </div>
#   <div class = "col">
# <!-- ## CLOSEDBLOK: Homoskedasticiteit2.R -->

# In[ ]:


set.seed(12345)
x <- seq(from = 4.01,to = 16.5, length.out = 1000)
y <- c(rnorm(200,0,0.5),
       rnorm(200,0,1),
       rnorm(200,0,2),
       rnorm(200,0,4),
       rnorm(200,0,8)) / 10

dataset <- data.frame(Residu = y, Voorspelling = x)

ggplot(dataset, aes(x = Voorspelling, y = Residu)) +
    geom_point()  + ylab("Gestandaardiseerd residu") +
  ggtitle("Heteroskedasticiteit")


# <!-- ## /CLOSEDBLOK: Homoskedasticiteit2.R -->
#   </div>
# </div>
# *Figuur 2.  Voorbeeld van homoskedasticiteit (links) en heteroskedasticiteit (rechts) van residuën.*
# 
# ## Multicollineariteit
# 
# Multicollineariteit houdt in dat er een hoge correlatie tussen twee of meerdere covariaten is. Er is perfecte multicollineariteit als één covariaat een lineaire combinatie is van een of meerdere andere covariaten. In andere woorden, de covariaat is precies te berekenen op basis van andere covariaten. In dat geval kan de *ANCOVA* niet wiskundig bepaald worden en werkt de *ANCOVA* niet. Dit komt zeer weinig voor en is vaak makkelijk op te lossen door goed naar de variabelen die het veroorzaken te kijken en een variabele te transformeren of te verwijderen.[^4]
# 
# Bij een hoog niveau van multicollineariteit kan de *ANCOVA* wel uitgevoerd worden, maar zijn de uitkomsten minder betrouwbaar. Het is dan lastig om te ontdekken wat per covariaat de bijdrage is aan de voorspellingen van de afhankelijke variabele, omdat bepaalde covariaten sterk gecorreleerd zijn en overlappen in het deel van de variantie dat ze verklaren. Hierdoor is het moeilijker om goed te corrigeren voor de covariaten.[^4] 
# 
# Multicollineariteit wordt getoetst met de Variance Inflation Factor (VIF) die meet hoe sterk elke covariaat gecorreleerd is met de andere covariaten. Als de VIF van een covariaat hoger dan 10 is, is er multicollineariteit voor die covariaat.[^4]<sup>,</sup>[^9] Multicollineariteit kan opgelost worden door een van de covariaten die het veroorzaakt te verwijderen. Een andere optie is een principale componenten analyse (PCA) uitvoeren op de covariaten zodat er een onderliggende variabele gecreëerd wordt (zie Field[^4] voor meer informatie).
# 
# ## Homogeniteit van Varianties
# 
# <!-- ## TEKSTBLOK: Link2.R -->
# Homogeniteit van varianties houdt in dat de variantie in alle groepen ongeveer hetzelfde is. Toets deze assumptie met de *Levene's Test*. Bij een p-waarde kleiner dan 0,05 is de variantie van de groepen significant verschillend.[^10]<sup>,</sup>[^11] De *ANCOVA* is redelijk robuust ten opzichte van een schending van de assumptie van homogeniteit van varianties als de steekproefgroottes groot zijn en niet veel van elkaar verschillen. Als de ratio van de grootste en kleinste steekproefgrootte van alle groepen kleiner dan 10 is en de ratio van de grootste en kleinste variantie van alle groepen kleiner dan 4 is, dan kan de *ANCOVA* gewoon uitgevoerd worden.[^12]  Als dit niet het geval is, dan is  het een optie om de *ANCOVA* uit te voeren als *multipele lineaire regressie* en te bootstrappen; zie bijbehorende [toetspagina](28-Multipele-lineaire-regressie-R.html).
# <!-- ## /TEKSTBLOK: Link2.R -->

# ## Homogeniteit van regressielijnen
# 
# Bij de *ANCOVA* worden groepen vergeleken na het corrigeren voor covariaten. Een vereiste is dan wel dat de relatie tussen de covariaat hetzelfde is voor elke groep. Deze voorwaarde is de assumptie van homogeniteit van regressielijnen. In de huidige casus wordt voor de *ANCOVA* aangenomen dat de relatie tussen het aantal hoorcolleges en het eindcijfer Methoden & Statistiek en tussen het gemiddeld eindexamencijfer en het eindcijfer Methoden & Statistiek hetzelfde is voor studenten van de opleidingen Psychologie, Onderwijskunde en Sociologie. Als dit niet het geval is, dan kan het verschil tussen groepen niet goed geanalyseerd worden. Het verschil tussen de groepen hangt dan namelijk ook af van de waarde van de covariaat. 
# 
# Een voorbeeld van homogeniteit en heterogeniteit van regressielijnen is weergegeven in Figuur 3. Bij de linkerfiguur lopen de regressielijnen parallel voor de drie groepen. Er is in dit geval aan de assumptie voldaan. Op basis van de regressielijnen kan al ingeschat worden op welke manier de groepen van elkaar verschillen. Bij de rechterfiguur is er sprake van heterogeniteit van regressielijnen. Hier lopen de regressielijnen niet parallel voor de drie groepen. De verschillen tussen  de groepen hangen dus af van de waarde van de covariaat. Een *ANCOVA* is dan geen goede manier om verschillen tussen groepen te onderzoeken.
# 
# <div class = "col-container">
#   <div class="col">
# <!-- ## CLOSEDBLOK: Homoskedasticiteit1.R -->

# In[ ]:


set.seed(12345)
library(ggplot2)
## ANCOVA
HC_Psychologie <- rnorm(50, 6, 1)
HC_Onderwijskunde <- rnorm(50, 18, 1)
HC_Sociologie <- rnorm(50, 29, 2)
HC <- round(c(HC_Psychologie, HC_Onderwijskunde, HC_Sociologie))

HC <- rnorm(50, 2, 1)

Opleiding <- c(rep("Groep_1", 50),
             rep("Groep_2", 50),
             rep("Groep_3", 50))

Cijfer_gemiddeld_P <-  6 + 1 * HC + rnorm(50,0,1)
Cijfer_gemiddeld_O <-  10 + 1 * HC + rnorm(50,0,1)
Cijfer_gemiddeld_S <-  15 + 1 * HC + rnorm(50,0,1)
Cijfer_gemiddeld <- c(Cijfer_gemiddeld_P, Cijfer_gemiddeld_O, Cijfer_gemiddeld_S)
#Cijfer_gemiddeld[Cijfer_gemiddeld > 10] <- 10

dataset <- data.frame(Covariaat = HC,
                   Onafhankelijke_variabele = Opleiding,
                    Afhankelijke_variabele = Cijfer_gemiddeld)

ggplot(dataset, aes(x = Covariaat, y = Afhankelijke_variabele, color = Onafhankelijke_variabele)) +
    geom_point() +
    scale_color_manual(values = c("darkorange", "deepskyblue", "darkgreen")) +
    geom_abline(intercept = 6, slope = 1, color = "darkorange ") +
    geom_abline(intercept = 10, slope = 1, color = "deepskyblue") +
    geom_abline(intercept = 15, slope = 1, color = "darkgreen")


# <!-- ## /CLOSEDBLOK: Homoskedasticiteit1.R -->
#   </div>
#   <div class = "col">
# <!-- ## CLOSEDBLOK: Homoskedasticiteit2.R -->

# In[ ]:


set.seed(12345)
library(ggplot2)
## ANCOVA
HC_Psychologie <- rnorm(50, 6, 1)
HC_Onderwijskunde <- rnorm(50, 12, 1)
HC_Sociologie <- rnorm(50, 20, 2)
HC <- round(c(HC_Psychologie, HC_Onderwijskunde, HC_Sociologie))

HC <- rnorm(50, 2, 1)

Opleiding <- c(rep("Groep_1", 50),
             rep("Groep_2", 50),
             rep("Groep_3", 50))

Cijfer_gemiddeld_P <-  6 + 2 * HC + rnorm(50,0,1)
Cijfer_gemiddeld_O <-  8 + 0 * HC + rnorm(50,0,1)
Cijfer_gemiddeld_S <-  10 + -1 * HC + rnorm(50,0,1)
Cijfer_gemiddeld <- c(Cijfer_gemiddeld_P, Cijfer_gemiddeld_O, Cijfer_gemiddeld_S)
#Cijfer_gemiddeld[Cijfer_gemiddeld > 10] <- 10

dataset <- data.frame(Covariaat = HC,
                   Onafhankelijke_variabele = Opleiding,
                    Afhankelijke_variabele = Cijfer_gemiddeld)

ggplot(dataset, aes(x = Covariaat, y = Afhankelijke_variabele, color = Onafhankelijke_variabele)) +
    geom_point() +
    scale_color_manual(values = c("darkorange", "deepskyblue", "darkgreen")) +
    geom_abline(intercept = 6, slope = 2, color = "darkorange") +
    geom_abline(intercept = 8, slope = 0, color = " deepskyblue") +
    geom_abline(intercept = 10, slope = -1, color = "darkgreen")


# <!-- ## /CLOSEDBLOK: Homoskedasticiteit2.R -->
#   </div>
# </div>
# *Figuur 3.  Voorbeeld van homogeniteit (links) en heterogeniteit (rechts) van regressielijnen.*
# 
# Toets deze assumptie door een *ANCOVA* uit te voeren waarbij er een interactieterm van de onafhankelijke variabele en de covariaat is meegenomen. Als deze interactieterm significant is, is er niet voldaan aan de assumptie. Het effect van de onafhankelijke variabele hangt dan af van de covariaat, dus er zijn geen parallelle regressielijnen. Als deze assumptie geschonden is, kan de *ANCOVA* niet uitgevoerd worden. Het betekent namelijk dat de afhankelijke variabele bepaald wordt door een interactie tussen de onafhankelijke variabele en de covariaat. Dit is op zichzelf al nuttige informatie, maar dit kan ook gemodelleerd worden met behulp van *multipele lineaire regressie*, zie bijbehorende [toetspagina](28-Multipele-lineaire-regressie-R.html).
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^13] Voor de *ANCOVA* wordt de effectmaat *partial eta squared* vaak gebruikt.[^14]
# 
# De effectmaat *partial eta squared* (partial *η^2^*) berekent de proportie van de onverklaarde variantie (variantie die niet door de andere variabelen wordt verklaard) in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele.[^14] Voor de variabele Opleiding geeft de partial eta squared dus de proportie verklaarde variantie weer van de variantie die niet verklaard is door de variabelen Aantal Hoorcolleges en Eindexamencijfer. De partial eta squared van alle termen van het model tellen dus niet per se op tot 1.[^14] Een indicatie om partial *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^15]
# 
# # Post-hoc toetsen en marginale gemiddelden
# 
# De *ANCOVA* toetst of er verschillen zijn tussen de gemiddelden van de verschillende groepen na het corrigeren voor covariaten. Voer een post-hoc toets uit om te bepalen welke specifieke groepen van elkaar verschillen. Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Benjamini-Hochberg correctie* gebruikt. Deze correctie zorgt ervoor dat de proportie type I fouten (*false discovery rate*) in het aantal significante toetsen gereduceerd wordt. Deze correctie is minder strict dan de *Bonferroni correctie* die ervoor zorgt dat de kans op ten minste één type I fout in alle toetsen gereduceerd wordt.[^16]<sup>,</sup>[^17] Er zijn ook andere opties voor een correctie op de p-waarden.[^13]
# 
# Naast de post-hoc toetsen, zijn de marginale gemiddelden van belang bij de *ANCOVA*. Het marginale gemiddelde van een groep is de voorspelde waarde op de afhankelijke variabele voor een bepaalde groep als de covariaten gelijk zijn aan het gemiddelde in de steekproef. In de huidige casus zou dit betekenen dat voor studenten Psychologie, Onderwijskunde en Sociologie het eindcijfer Methoden & Statistiek wordt berekend als het aantal gevolgde hoorcolleges en het gemiddelde eindexamencijfer van de middelbare school precies gelijk zijn aan de gemiddelden van alle studenten samen. In feite worden de groepen gelijk getrokken wat betreft de covariaten. Als er namelijk een verschil is in het aantal gevolgde hoorcolleges tussen de opleidingen, dan vertekent dat de waarde van het (echte) gemiddelde. Met het marginale gemiddelde kan er dus een eerlijke vergelijking tussen groepen gemaakt worden als er covariaten aanwezig zijn die invloed hebben op de afhankelijke variabele. De post-hoc toetsen toetsen in feite de marginale gemiddelden. Rapporteer daarom de post-hoc toetsen in combinatie met de marginale gemiddelden.
# 
# # Uitvoering
# 
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset ingeladen met daarin de eindcijfers voor het vak Methoden & Statistiek, het aantal gevolgde hoorcolleges, het gemiddeld eindexamencijfer, de opleiding en het studentnummers van de studenten die het vak Methoden & Statistiek hebben gevolgd. De dataset heet `Studenten_Methoden_Statistiek`. 
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 5 observaties
head(Studenten_Methoden_Statistiek)

## Laatste 5 observaties
tail(Studenten_Methoden_Statistiek)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 

# <!-- ## TEKSTBLOK: Data-beschrijven.R -->
# Inspecteer voor alle groepen het gemiddelde, de standaardafwijking, de mediaan en het aantal observaties voor de variabelen Eindcijfer Methoden & Statistiek, Eindexamencijfer en Aantal Hoorcolleges om meer inzicht te krijgen. Gebruik hiervoor de functie `descr` en `stby` van het package `summarytools` om de beschrijvende statistieken per groep weer te geven. Voer de gewenste statistieken in met het argument `stats = c("mean","sd","med","n.valid")`.
# <!-- ## /TEKSTBLOK: Data-beschrijven.R -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-1.R -->

# In[ ]:


# Gemiddelde, standaardafwijking, mediaan en aantal observaties
library(summarytools)

with(Studenten_Methoden_Statistiek, 
     stby(data = cbind(Aantal_Hoorcolleges, Eindexamencijfer, Eindcijfer_MS), 
          list(Opleiding), 
          descr, 
          stats = c("mean", "sd", "med", "n.valid")))


# <!-- ## /OPENBLOK: Data-beschrijven-1.R -->
# 
# Uit de beschrijvende statistieken blijkt dat het gemiddelde eindcijfer Methoden & Statistiek ongeveer gelijk is voor de opleidingen Psychologie en Sociologie en iets hoger is voor Onderwijskunde. Het aantal gevolgde hoorcolleges verschilt echter per opleiding waarbij opvalt dat het voor de opleiding Psychologie een stuk lager is. Het gemiddeld eindexamencijfer op de middelbare school is echter redelijk gelijk voor studenten van de drie opleidingen.
# 
# # Toetsing assumpties
# 
# Gebruik de *ANCOVA* om te onderzoeken of het eindcijfer voor het vak Methoden & Statistiek van de faculteit Sociale Wetenschappen verschilt voor studenten afkomstig van de opleidingen Psychologie, Onderwijskunde en Sociologie na corrigeren voor het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer. Start met het toetsen van de assumpties en voer vervolgens de *ANCOVA* uit als hieraan voldaan is.
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Voer eerst de *ANCOVA* uit omdat deze nodig is voor het toetsen van assumpties en sla het resultaat op. Interpreteer de resultaten pas na het toetsen van de assumpties. Gebruik de functie `aov()` met als eerste argument de vergelijking `Eindcijfer_MS ~ Opleiding + Aantal_Hoorcolleges + Eindexamencijfer` met links van de tilde de afhankelijke variabele `Eindcijfer_MS` en rechts de onafhankelijke variabele `Opleiding` en de covariaten `Aantal_Hoorcolleges` en `Eindexamencijfer`. Het tweede argument is de dataset `Studenten_Methoden_Statistiek`.
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


ANCOVA <- aov(Eindcijfer_MS ~ Opleiding + Aantal_Hoorcolleges + Eindexamencijfer,
              Studenten_Methoden_Statistiek)


# <!-- ## /OPENBLOK: Uitvoering2.R -->

# ## Outliers
# 
# ### Boxplots en standaardiseren
# 
# <!-- ## TEKSTBLOK: Outlier1.R -->
# Onderzoek of er univariate outliers zijn met behulp van boxplots en gestandaardiseerde scores voor continue variabelen en tabellen voor categorische variabelen. Begin met de boxplot voor de variabelen `Eindexamencijfer`, `Aantal_Hoorcolleges` en `Eindcijfer_MS`.
# <!-- ## /TEKSTBLOK: Outlier1.R -->
# 
# <!-- ## OPENBLOK: Outlier2.R -->

# In[ ]:


# Maak een boxplot van de continue variabelen in de dataset
boxplot(Studenten_Methoden_Statistiek[,c("Aantal_Hoorcolleges",
                                         "Eindexamencijfer",
                                         "Eindcijfer_MS")])


# <!-- ## /OPENBLOK: Outlier2.R -->
# 
# Voor de drie variabelen zijn er geen onmogelijke scores en zijn er geen grote afwijkingen op basis van de boxplot. Onderzoek de gestandaardiseerde scores door een functie te schrijven die het aantal observaties per variabele telt met een gestandaardiseerde score hoger dan 3 of lager dan -3. Pas deze functie vervolgens toe op de drie continue variabelen in de dataset.
# 
# <!-- ## OPENBLOK: Outlier3.R -->

# In[ ]:


# Maak een functie om het aantal observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3 te tellen
Outlier_standaardiseren <- function(variabele){
  # Standaardiseer de variabele met de scale functie
  Z_score <- scale(variabele)
  # Tel het aantal observaties met een absolute score hoger dan 3
  Aantal_outliers <- sum(abs(Z_score) > 3)
  # Retourneer dit aantal
  return(Aantal_outliers)
}

# Tel voor de continue variabelen het aantal observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3
Outlier_standaardiseren(Studenten_Methoden_Statistiek$Aantal_Hoorcolleges)
Outlier_standaardiseren(Studenten_Methoden_Statistiek$Eindcijfer_MS)


# <!-- ## /OPENBLOK: Outlier3.R -->

# Beide variabelen hebben nul observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3. Er zijn in de stap voor de continue variabelen geen outliers gevonden.
# 
# Opleiding is de enige categorische variabele in deze dataset. Maak een tabel met de frequenties voor alle categoriëen van deze variabele om te onderzoeken of hier afwijkende waardes zijn.
# 
# <!-- ## OPENBLOK: Outlier4.R -->

# In[ ]:


table(Studenten_Methoden_Statistiek$Opleiding)


# <!-- ## /OPENBLOK: Outlier4.R -->
# 
# De categorieën van de variabele Opleiding zijn `Onderwijskunde`, `Psychologie` en `Sociologie`. Er zijn dus geen opmerkelijke waarden bij de variabele Opleiding.
# 
# ### Mahalanobis distance
# 
# <!-- ## TEKSTBLOK: Outlier7.R -->
# Onderzoek of er multivariate outliers zijn met behulp van de Mahalanobis distance met behulp van de functie `mahalanobis()`. De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van het gemiddelde van alle deelnemers voor alle covariaten samen. Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Bij een categorische covariaat moet deze dus omgezet worden. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd.
# 
# Neem vervolgens een subset van de dataset met alleen de covariaten en gebruik deze voor de Mahalanobis afstand. Gebruik de functie `mahalanobis()` met als argumenten de dataset `Subset`, de gemiddeldes van elke kolom berekend met `colMeans(Subset)` en de covariantiematrix van de dataset berekend met `cov(Subset)`.
# 
# Bereken daarna de criteriumwaarde op basis van het gewenste significantieniveau en het aantal covariaten. Plot de Mahalanobis afstanden en tel het aantal deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde. Het gehanteerde significantieniveau is 0,001.
# <!-- ## /TEKSTBLOK: Outlier7.R -->
# 
# <!-- ## OPENBLOK: Outlier8.R -->

# In[ ]:


# Maak een subset van de dataset met alle cvoariaten
Subset <- Studenten_Methoden_Statistiek[,c("Eindexamencijfer",
                                         "Aantal_Hoorcolleges")]

# Bereken de Mahalanobis afstand voor elke deelnemer 
Mahalanobis_afstanden <- mahalanobis(Subset,
                                     colMeans(Subset),
                                     cov(Subset))

# Bepaal de criteriumwaarde voor de Mahalanobis afstand met de functie qchisq() met als eerste argument 1 - het significantieniveau en als tweede argument het aantal covariaten. In deze casus is het significantieniveau voor de Mahalanobis afstand 0.001 en het aantal covariaten berekend met ncol(Subset).
(Criteriumwaarde <- qchisq(1 - 0.001, ncol(Subset)))

# Plot de Mahalanobis afstanden
plot(Mahalanobis_afstanden, xlab = "Volgorde", ylab = "Mahalanobis afstanden")

# Tel het aantal Mahalanobis afstanden groter dan de criteriumwaarde
sum(Mahalanobis_afstanden > Criteriumwaarde)


# <!-- ## /OPENBLOK: Outlier8.R -->
# 
# <!-- ## TEKSTBLOK: Outlier9.R -->
# Er zijn geen deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde van `r Round_and_format(Criteriumwaarde)`, dus er lijken geen multivariate outliers te zijn op basis van de Mahalanobis afstand.
# <!-- ## /TEKSTBLOK: Outlier9.R -->
# 
# ### Cook's afstand
# 
# <!-- ## TEKSTBLOK: Outlier10.R -->
# Onderzoek of er multivariate outliers zijn met behulp van Cook's afstand. Cook's afstand geeft aan hoeveel invloed het weglaten van een deelnemer heeft op de uitkomsten van de *ANCOVA*. Gebruik hiervoor de functie `cooks.distance` met als argument  `ANCOVA` (het object van de *ANCOVA*). Plot de Cook's afstanden daarna en tel het aantal Cook's afstanden dat groter is dan de criteriumwaarde van 1.
# <!-- ## /TEKSTBLOK: Outlier10.R -->
# 
# <!-- ## OPENBLOK: Outlier11.R -->

# In[ ]:


# Bepaal Cook's afstand voor elke deelnemer
Cooks_afstand <-  cooks.distance(ANCOVA)

# Plot Cook's afstanden
plot(Cooks_afstand, xlab = "Volgorde", ylab = "Cook's afstanden")

# Tel het aantal Cook's afstanden groter dan de criteriumwaarde van 1
sum(Cooks_afstand > 1)


# <!-- ## /OPENBLOK: Outlier11.R -->
# 
# Er zijn geen deelnemers met een Cook's afstand groter dan de criteriumwaarde van 1. Er lijken dus geen invloedrijke datapunten of multivariate outliers te zijn.
# 
# ## Lineariteit
# 
# Onderzoek of er een lineaire relatie is tussen de covariaten en de afhankelijke variabele met behulp van scatter plots. 
# 
# <div class = "col-container">
#   <div class="col">
# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


plot(Eindcijfer_MS ~ Eindexamencijfer, data = Studenten_Methoden_Statistiek,
     xlab = "Eindexamencijfer", ylab = "Eindcijfer Methoden & Statistiek")


# <!-- ## /OPENBLOK: AssLineariteit1.R -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: AssLineariteit2.R -->

# In[ ]:


plot(Eindcijfer_MS ~ Aantal_Hoorcolleges, data = Studenten_Methoden_Statistiek,
     xlab = "Aantal hoorcolleges", ylab = "Eindcijfer Methoden & Statistiek")


# <!-- ## /OPENBLOK: AssLineariteit2.R -->
#   </div>
# </div>
# 
# Bij beide covariaten lijkt er een lineaire relatie te zijn met de afhankelijke variabele. Er is dus aan de assumptie van lineariteit voldaan.
# 
# ## Normaliteit
# 
# <!-- ## TEKSTBLOK: AssNormaliteit1.R -->
# Onderzoek of de gestandaardiseerde residuën van de *ANCOVA* een normale verdeling volgen. Sla eerst de gestandaardiseerde residuën op met behulp van de functie `rstandard()` met als argument `ANCOVA` (het object van de *ANCOVA*) en maak vervolgens een histogram[^18] om de verdeling te inspecteren. Het is ook mogelijk om normaliteit te onderzoeken met behulp van een QQ-plot.
# <!-- ## /TEKSTBLOK: AssNormaliteit1.R -->
# 
# <!-- ## OPENBLOK: AssNormaliteit2.R -->

# In[ ]:


# Sla de gestandaardiseerde residuën op
Residu_gestandaardiseerd <- rstandard(ANCOVA)

# Maak een histogram
hist(Residu_gestandaardiseerd, xlab = "Gestandaardiseerde residuën", ylab = "Frequentie", main = "")


# <!-- ## /OPENBLOK: AssNormaliteit2.R -->
# 
# De verdeling van de gestandaardiseerde residuën lijkt een normaalverdeling te benaderen. Er is dus voldaan aan de assumptie van normaliteit.
# 
# ## Homoskedasticiteit
# 
# <!-- ## TEKSTBLOK: AssHomoskedasticiteit1.R -->
# Toets de assumptie van homoskedasticiteit door te onderzoeken of de variantie ongeveer gelijk is voor alle waarden van de voorspellingen van de afhankelijke variabele. Maak hiervoor een plot van de gestandaardiseerde residuën versus de voorspellingen. De gestandaardiseerde residuën zijn te vinden met de functie `rstandard()` met als argument `ANCOVA` (het object van de *ANCOVA*) en de voorspellingen met de functie `fitted()` met opnieuw als argument `ANCOVA`.
# <!-- ## /TEKSTBLOK: AssHomoskedasticiteit1.R -->
# 
# <!-- ## OPENBLOK: AssHomoskedasticiteit2.R -->

# In[ ]:


# Sla de gestandaardiseerde residuën op
Residu_gestandaardiseerd <- rstandard(ANCOVA)

# Sla de voorspellingen op
Voorspellingen <- fitted(ANCOVA)

# Maak een scatter plot
plot(Voorspellingen, Residu_gestandaardiseerd, ylab = "Gestandaardiseerde residuën", xlab = "Voorspellingen", main = "")


# <!-- ## /OPENBLOK: AssHomoskedasticiteit2.R -->
# 
# De spreiding van de gestandaardiseerde residuën lijkt redelijk constant te zijn voor de verschillende waarden van de voorspellingen. Er is dus voldaan aan de assumptie van homoskedasticiteit.
# 
# ## Multicollineariteit
# 
# <!-- ## TEKSTBLOK: AssMulticollineariteit1.R -->
# Onderzoek of er sprake is van multicollineariteit bij de covariaten met behulp van Variance Inflation Factors (VIFs). Bereken de VIFs voor elke covariaat met de functie `VIF()` van het package `DescTools` waarbij de functie als argument `ANCOVA_multicollineariteit` heeft. Voer hiervoor eerst een *ANCOVA* uit met alleen de covariaten zonder de onafhankelijke variabele en sla deze op als `ANCOVA_multicollineariteit`. Gebruik de functie `aov()` met als eerste argument de vergelijking `Eindcijfer_MS ~ Aantal_Hoorcolleges + Eindexamencijfer` met links van de tilde de afhankelijke variabele `Eindcijfer_MS` en rechts de covariaten `Aantal_Hoorcolleges` en `Eindexamencijfer`. Het tweede argument is de dataset `Studenten_Methoden_Statistiek`.
# <!-- ## /TEKSTBLOK: AssMulticollineariteit1.R -->

# <!-- ## OPENBLOK: AssMulticollineariteit2.R -->

# In[ ]:


library(DescTools)

# Voer de ANCOVA uit en sla het op in een object
ANCOVA_multicollineariteit <- aov(Eindcijfer_MS ~ Aantal_Hoorcolleges + Eindexamencijfer,
                                  Studenten_Methoden_Statistiek)

# Bereken de VIF voor elke covariaat
VIF(ANCOVA_multicollineariteit)


# <!-- ## /OPENBLOK: AssMulticollineariteit2.R -->
# 
# Geen enkele van de VIFs is hoger dan 10, dus er is voldaan aan de assumptie van multicollineariteit.
# 
# ## Homogeniteit van varianties
# 
# <!-- ## TEKSTBLOK: LeveneTest1.R -->
# Toets met de *Levene's test* de assumptie homogeniteit van varianties voor de onafhankelijke variabele Opleiding. Gebruik hiervoor de functie `leveneTest` van het package `car` met het argument `Eindcijfer_MS ~ Opleiding` met daarin de afhankelijke variabele `Eindcijfer_MS` en de onafhankelijke variabelen `Opleiding` en het argument `data = Studenten_Methoden_Statistiek`.
# <!-- ## /TEKSTBLOK: LeveneTest1.R -->
# 
# <!-- ## OPENBLOK: Levenes-test.R -->

# In[ ]:


library(car)

leveneTest(Eindcijfer_MS ~ Opleiding, 
           data = Studenten_Methoden_Statistiek)


# <!-- ## /OPENBLOK: Levenes-test.R -->
# 
# <!-- ## CLOSEDBLOK: Levenes-test.R -->

# In[ ]:


L <- leveneTest(Eindcijfer_MS ~ Opleiding, 
           data = Studenten_Methoden_Statistiek)

vF_waarde <- Round_and_format(L$`F value`[1])
vF_p <- Round_and_format(L$`Pr(>F)`[1])
vDF1 <- Round_and_format(L$`Df`[1])
vDF2 <- Round_and_format(L$`Df`[2])


# <!-- ## /CLOSEDBLOK: Levenes-test.R -->
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->
# * *F*(`r vDF1`,`r vDF2`) = `r vF_waarde`, p-waarde = `r vF_p`, 
# * De p-waarde is groter dan 0,05, dus er is geen significant verschil gevonden tussen de groepen in variantie.[^11] Er is dus aan de assumptie van homogeniteit van varianties voldaan.
# 
# <!-- ## TEKSTBLOK: Levenes-test.R -->

# ## Homogeniteit van regressielijnen
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Toets de assumptie van homogeniteit van regressielijnen voor elke covariaat door een interactieterm van de covariaat met de onafhankelijke variabele toe te voegen aan de *ANCOVA*. Gebruik hiervoor de functie `aov()` met als eerste argument de vergelijking `Eindcijfer_MS ~ Opleiding + Aantal_Hoorcolleges + Eindexamencijfer + `
# `Opleiding:Aantal_Hoorcolleges + Opleiding:Eindexamencijfer` met links van de tilde de afhankelijke variabele `Eindcijfer_MS` en rechts de onafhankelijke variabele `Opleiding`, de covariaten `Aantal_Hoorcolleges` en `Eindexamencijfer` en de interactietermen `Opleiding:Aantal_Hoorcolleges` en `Opleiding:Eindexamencijfer`. Het tweede argument is de dataset `Studenten_Methoden_Statistiek`.
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


ANCOVA_interacties <- aov(Eindcijfer_MS ~ Opleiding + Aantal_Hoorcolleges + 
                            Eindexamencijfer + Opleiding:Aantal_Hoorcolleges +
                            Opleiding:Eindexamencijfer,
                          Studenten_Methoden_Statistiek)

summary(ANCOVA_interacties)


# In[ ]:


AI <- summary(ANCOVA_interacties)[[1]]

AHvF_waarde <- Round_and_format(AI$`F value`[4])
AHvDF1 <- Round_and_format(AI$Df[4])
AHvDF2 <- Round_and_format(AI$Df[6])
AHvp <- Round_and_format(AI$`Pr(>F)`[4])

ECvF_waarde <- Round_and_format(AI$`F value`[5])
ECvDF1 <- Round_and_format(AI$Df[5])
ECvDF2 <- Round_and_format(AI$Df[6])
ECvp <- Round_and_format(AI$`Pr(>F)`[5])


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# Zowel de interactie tussen Opleiding en Aantal_Hoorcolleges (*F* (`r AHvDF1`,`r AHvDF2`) = `r AHvF_waarde`, *p* = `r AHvp`) als de interactie tussen Opleiding en Eindexamencijfer (*F* (`r ECvDF1`,`r ECvDF2`) = `r ECvF_waarde`, *p* = `r ECvp`) is niet significant.[^11] Dit betekent dat er geen interactie is tussen de covariaat en onafhankelijke variabele wat betekent dat er voldaan is aan de assumptie van homogeniteit van regressielijnen.

# # ANCOVA
# 
# Voer de *ANCOVA* uit om te onderzoeken of het eindcijfer voor het vak Methoden & Statistiek van de faculteit Sociale Wetenschappen verschilt voor studenten afkomstig van de opleidingen Psychologie, Onderwijskunde en Sociologie na corrigeren voor het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer.
# 
# Gebruik de functie `aov()` met als eerste argument de vergelijking `Eindcijfer_MS ~ Opleiding + Aantal_Hoorcolleges + Eindexamencijfer` met links van de tilde de afhankelijke variabele `Eindcijfer_MS` en rechts de onafhankelijke variabele `Opleiding` en de covariaten `Aantal_Hoorcolleges` en `Eindexamencijfer`. Het tweede argument is de dataset `Studenten_Methoden_Statistiek`. Sla het resultaat op als een object met de naam `ANCOVA` en laat de resultaten vervolgens zien met de functie `summary()`.
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


ANCOVA <- aov(Eindcijfer_MS ~ Opleiding + Aantal_Hoorcolleges + Eindexamencijfer,
              Studenten_Methoden_Statistiek)

summary(ANCOVA)


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# <!-- ## CLOSEDBLOK: Uitvoering3.R -->

# In[ ]:


AC <- summary(ANCOVA)[[1]]

OLvF_waarde <- Round_and_format(AC$`F value`[1])
OLvDF1 <- Round_and_format(AC$Df[1])
OLvDF2 <- Round_and_format(AC$Df[4])
OLvp <- Round_and_format(AC$`Pr(>F)`[1])

AHvF_waarde <- Round_and_format(AC$`F value`[2])
AHvDF1 <- Round_and_format(AC$Df[2])
AHvDF2 <- Round_and_format(AC$Df[4])
AHvp <- Round_and_format(AC$`Pr(>F)`[2])

ECvF_waarde <- Round_and_format(AC$`F value`[3])
ECvDF1 <- Round_and_format(AC$Df[3])
ECvDF2 <- Round_and_format(AC$Df[4])
ECvp <- Round_and_format(AC$`Pr(>F)`[3])


# <!-- ## /CLOSEDBLOK: Uitvoering3.R -->

# <!-- ## TEKSTBLOK: ANOVA-toets2.R -->
# Bereken vervolgens de effectmaat partial eta squared met behulp van de functie `EtaSq` van het package `DescTools` met als argument het ANOVA-object `ANOVA_object`.
# <!-- ## /TEKSTBLOK: ANOVA-toets2.R -->
# 
# <!-- ## OPENBLOK: ANOVA-toets3.R -->

# In[ ]:


library(DescTools)

EtaSq(ANCOVA)


# <!-- ## /OPENBLOK: ANOVA-toets3.R -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets4.R -->

# In[ ]:


pes <- EtaSq(ANCOVA)
EsqOL <- Round_and_format(pes[1,2])
EsqAH <- Round_and_format(pes[2,2])
EsqEC <- Round_and_format(pes[3,2])


# <!-- ## /CLOSEDBLOK: ANOVA-toets4.R -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets5.R -->
# 
# * Er is een significant[^11] effect van Opleiding op Eindcijfer Methoden & Statistiek na corrigeren voor het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer, *F* (`r OLvDF1`,`r OLvDF2`) = `r OLvF_waarde`, *p* < 0,0001, *η^2^* = `r EsqOL`
# * De covariaat Aantal_Hoorcolleges heeft een significant[^11] effect op het Eindcijfer Methoden & Statistiek, *F* (`r AHvDF1`,`r AHvDF2`) = `r AHvF_waarde`, *p* < 0,0001, *η^2^* = `r EsqAH`
# * De covariaat Eindexamencijfer heeft een significant[^11] effect op het Eindcijfer Methoden & Statistiek, *F* (`r ECvDF1`,`r ECvDF2`) = `r ECvF_waarde`, *p* < 0,0001, *η^2^* = `r EsqEC`
# * Het effect van Opleiding op Eindcijfer Methoden & Statistiek is klein tot gemiddeld
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets5.R -->

# # Post-hoc toetsen en marginale gemiddelden
# 
# <!-- ## TEKSTBLOK: PHtest1.R -->
# Omdat er significante verschillen tussen de gemiddelde eindcijfers Methoden & Statistiek zijn voor studenten afkomstig van de opleidingen Psychologie, Onderwijskunde en Sociologie na corrigeren voor het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer van de middelbare school, kunnen er post-hoc toetsen uitgevoerd worden om te onderzoeken tussen welke opleidingen er significante verschillen zijn.  Gebruik hiervoor de functie `emmeans_test` van het package `rstatix` met als argumenten de dataset `Studenten_Methoden_Statistiek`, de formule `Eindcijfer_MS ~ Opleiding` met als afhankelijke variabele `Eindcijfer_MS` en onafhankelijke variabele `Opleiding`, de covariaten `covariate = c(Aantal_Hoorcolleges, Eindexamencijfer)` en de correctie voor meerdere toetsen `p.adjust.method = "fdr"`. Hier staat `fdr` voor de *false discovery rate* oftewel de Benjamini-Hochberg correctie.
# <!-- ## /TEKSTBLOK: PHtest1.R -->
# 
# <!-- ## OPENBLOK: PHtest2.R -->

# In[ ]:


library(rstatix)
#install.packages("emmeans")
#install.packages("rstatix")
emmeans_test(Studenten_Methoden_Statistiek,
             Eindcijfer_MS ~ Opleiding, 
             covariate = c(Aantal_Hoorcolleges, 
                           Eindexamencijfer),
             p.adjust.method = "fdr"
    )


# Bereken vervolgens de marginale gemiddelden voor elke opleiding. Het marginale gemiddelde is een gemiddelde dat gecorrigeerd is voor de covariaten. Gebruik de functie `get_emmeans()` van het package `rstatix` met als argument een object dat gemaakt wordt door de post-hoc toetsen uit te voeren.
# 

# In[ ]:


library(rstatix)

# Voer de post-hoc toetsen uit en sla het resultaat op in een object
Marginale_gemiddelden <- emmeans_test(Studenten_Methoden_Statistiek,
    Eindcijfer_MS ~ Opleiding, covariate = c(Aantal_Hoorcolleges, Eindexamencijfer),
    p.adjust.method = "fdr"
    )

# Bepaal de marginale gemiddelden
get_emmeans(Marginale_gemiddelden)


# <!-- ## /OPENBLOK: PHtest2.R -->
# 
# <!-- ## CLOSEDBLOK: PHtest3.R -->

# In[ ]:


posthoc <- emmeans_test(Studenten_Methoden_Statistiek,
             Eindcijfer_MS ~ Opleiding, 
             covariate = c(Aantal_Hoorcolleges, 
                           Eindexamencijfer),
             p.adjust.method = "fdr"
    )

marmeans <- get_emmeans(Marginale_gemiddelden)


# <!-- ## /CLOSEDBLOK: PHtest3.R -->

# <!-- ## TEKSTBLOK: PHtest7.R -->
# De verschillen voor de groepen van de onafhankelijke variabele Opleiding zijn[^11]:
# 
# * Onderwijskunde versus Psychologie: de marginale gemiddelden van de studenten Onderwijskunde (`r Round_and_format(marmeans$emmean[1])`) en de studenten Psychologie (`r Round_and_format(marmeans$emmean[2])`) zijn niet significant verschillend van elkaar (*p* = 1,00)
# * Onderwijskunde versus Sociologie: de marginale gemiddelden van de studenten Onderwijskunde (`r Round_and_format(marmeans$emmean[1])`) en de studenten Psychologie (`r Round_and_format(marmeans$emmean[3])`) zijn niet significant verschillend van elkaar (*p* < 0,0001)
# * Psychologie versus Sociologie: de marginale gemiddelden van de studenten Onderwijskunde (`r Round_and_format(marmeans$emmean[2])`) en de studenten Psychologie (`r Round_and_format(marmeans$emmean[3])`) zijn niet significant verschillend van elkaar (*p* < 0,0001)
# 
# De marginale gemiddelden zijn hier gelijk aan de op basis van de *ANCOVA* voorspelde waarde van het eindcijfer Methoden & Statistiek bij een waarde van het aantal gevolgde hoorcolleges en gemiddeld eindexamencijfer dat gelijk is aan het steekproefgemiddelde van beide variabelen. Het gemiddelde aantal hoorcolleges in de steekproef is `r Round_and_format(marmeans$Aantal_Hoorcolleges[1])` en het gemiddelde van het gemiddelde eindexamencijfer is `r Round_and_format(marmeans$Eindexamencijfer[1])`.
# <!-- ## /TEKSTBLOK: PHtest7.R -->
# 
# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *ANCOVA* is uitgevoerd om te toetsen of er verschillen zijn tussen studenten afkomstig van de opleidingen Psychologie, Onderwijskunde en Sociologie wat betreft het gemiddelde eindcijfer voor het vak Methoden & Statistiek corrigerend voor het aantal gevolgde hoorcolleges en het gemiddelde eindexamencijfer van de middelbare school. De resultaten laten zien dat er significante verschillen zijn tussen de gemiddelde eindcijfers van de drie opleidingen na corrigeren voor beide covariaten,  *F* (`r OLvDF1`,`r OLvDF2`) = `r OLvF_waarde`, *p* < 0,0001, *η^2^* = `r EsqOL`.
# 
# Om te onderzoeken welke opleidingen van elkaar verschillen in het gemiddeld eindcijfer Methoden & Statistiek, zijn post-hoc toetsen uitgevoerd met een Benjamini-Hochberg correctie voor meerdere toetsen. De marginale gemiddelden van de opleidingen Psychologie (`r Round_and_format(marmeans$emmean[2])`) en Onderwijskunde (`r Round_and_format(marmeans$emmean[1])`) zijn beide significant hoger dan het marginale gemiddelde van de opleiding Sociologie (`r Round_and_format(marmeans$emmean[3])`), maar verschillen niet significant van elkaar. De resultaten suggereren dat Sociologie studenten minder hoge cijfers halen dan studenten Psychologie en Onderwijskunde als er rekening gehouden wordt met het aantal gevolgde hoorcolleges en het gemiddeld eindexamencijfer van de middelbare school.
# 
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *One-way ANCOVA in SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/ancova-using-spss-statistics.php
# [^2]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.  
# [^3]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 86.
# [^4]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 293-356.
# [^5]: Universiteit van Amsterdam (13 augustus 2016). *Outliers*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).  
# [^6]: Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$.
# [^7]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^8]: Universiteit van Amsterdam (7 juli 2014). *Lineariteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Lineariteit).  
# [^9]: Stat 501. *12.4 - Detecting Multicollinearity Using Variance Inflation Factors*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat501/lesson/12/12.4).
# [^10]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. 
# Sage. Pagina 507-542.
# [^11]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^12]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 86.
# [^13]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^14]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 54 - 55.
# [^15]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited. Pagina 84.
# [^16]: Statistics How To (29 oktober 2017). *False Discovery Rate: Simple Definition, Adjusting for FDR*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/false-discovery-rate/). 
# [^17]: Statistics How To (12 oktober 2015). *Benjamini-Hochberg Procedure*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/benjamini-hochberg-procedure/). 
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
