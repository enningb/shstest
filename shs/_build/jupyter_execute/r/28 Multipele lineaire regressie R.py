#!/usr/bin/env python
# coding: utf-8
---
title: "Multipele lineaire regressie"
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


source(paste0(here::here(),"/01. Includes/data/28.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# Gebruik *multipele lineaire regressie* om te toetsen of een continue afhankelijke variabele voorspeld kan worden met twee of meer onafhankelijke variabelen (predictors) en om te toetsen of er een relatie is tussen een predictor en de afhankelijke variabele in aanwezigheid van andere predictors.[^1]

# # Onderwijscasus
# <div id = "casus">
# 
# De docent van het vak Methoden & Statistiek van de bachelor Onderwijskunde wil zijn studenten ervan overtuigen dat het nuttig is om naar zijn colleges te komen. Hij wil daarom onderzoeken of er een relatie is tussen het aantal colleges dat studenten volgen en het eindcijfer voor zijn vak. Daarnaast vermoedt hij dat het eindexamencijfer voor Wiskunde ook gerelateerd is aan het eindcijfer voor het vak en dat er man-vrouw verschillen zouden kunnen zijn. Op basis van de data van vorig jaar onderzoekt hij of er een relatie is tussen het aantal hoorcolleges dat studenten volgen, waarbij hij rekening houdt met het eindexamencijfer Wiskunde en man-vrouw verschillen. Met de resultaten hiervan hoopt hij zijn studenten ervan te overtuigen om de hoorcolleges van het vak bij te wonen.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is. Bij *multipele lineaire regressie* wordt er een hypothese opgesteld voor het complete model en hypotheses voor de individuele predictors.
# 
# Hypotheses regressiemodel:
# 
# *H~0~*: Geen enkele predictor van de predictors geslacht, eindexamencijfer Wiskunde en aantal gevolgde hoorcolleges is gerelateerd aan de afhankelijke variabele eindcijfer Methoden & Statistiek ($\beta_1 = \beta_2 = \beta_3 = 0$).
# 
# *H~A~*: Ten minste een van de predictors geslacht, eindexamencijfer Wiskunde en aantal gevolgde hoorcolleges is gerelateerd aan de afhankelijke variabele eindcijfer Methoden & Statistiek (Ten minste één $\beta_i \neq 0, i = 1, 2, 3$).
# 
# Hypotheses individuele predictors (met als voorbeeld de predictor aantal hoorcolleges):
# 
# *H~0~*: Het aantal hoorcolleges heeft geen voorspellende waarde voor het eindcijfer Methoden & Statistiek in aanwezigheid van de andere predictoren geslacht en eindexamencijfer Wiskunde ($\beta = 0$).
# 
# *H~A~*: Het aantal hoorcolleges heeft voorspellende waarde voor het eindcijfer Methoden & Statistiek in aanwezigheid van de andere predictoren geslacht en eindexamencijfer Wiskunde ($\beta \neq 0$).
# 
# </div>
# 
# # Multipele lineaire regressie
# 
# Het doel van *multipele lineaire regressie* is het voorspellen van een afhankelijke variabele op basis van meerdere onafhankelijke variabelen, ook wel predictors genoemd.[^1] Het voorspellen van een afhankelijke variabele wordt gedaan met behulp van een regressievergelijking waarin de afhankelijke variabele een lineaire combinatie is van de predictors, i.e. 
# 
# $$ y_i = \beta_0 + \beta_1 * x_{1i} + \beta_2 * x_{2i} + e_i$$
# 
# met $y_i$ als afhankelijke variabele, $\beta_0$ als intercept, $x_{1i}$ en $x_{2i}$ als predictors, $\beta_{1}$ en $\beta_{2}$ als regressiecoefficiënten van predictors, $e_i$ als residu of error en $i$ als indicator van de deelnemer[^19] uit de steekproef. De intercept $\beta_0$ geeft de waarde van de afhankelijke variabele weer als alle predictors gelijk aan nul zijn. De regressiecoefficiënten $\beta_1$ en $\beta_2$ geven de relatie tussen de afhankelijke variabele en de predictor weer. De residu of error $e_i$ is het verschil tussen de geobserveerde waarde van de afhankelijke variabele en de voorspelde waarde op basis van het regressiemodel. Voor de huidige casus is de volgende regressievergelijking op te stellen:
# 
# $$ EindcijferM\&S_i = \beta_0 + \beta_1 * Geslacht_i + \beta_2 * EindexamencijferWiskunde_i + \beta_3 * Aantal Hoorcolleges_i + e_i$$
# 
# De regressiecoefficiënten ($\beta_0$, $\beta_1$, $\beta_2$ en $\beta_3$) worden geschat door de waardes voor deze coefficiënten te vinden waarbij de som van de kwadraten van de residu $e_i$ zo klein mogelijk is. Multipele regressie wordt daarom ook wel ordinary least squares (OLS) regressie genoemd, omdat het de oplossing vind met de kleinste kwadraten van de residuën.[^2] De reden dat het kwadraat van de residuën gebruikt wordt is dat dit ervoor zorgt dat ook een negatief residu positief gemaakt kan worden. De methode kan als volgt visueel weergegeven worden:
# 
# <div class = "col-container">
#   <div class="col">
# <!-- ## CLOSEDBLOK: Regressie1.R -->

# In[ ]:


set.seed(12345)
x <- rnorm(100,5,2)
y <- 3 + 1.2 * x + rnorm(100,0,1)
dataset <- data.frame(Afhankelijke_variabele = y, Predictor = x)

model <- lm(Afhankelijke_variabele ~ 1, data = dataset)
dataset$Fit <- fitted(model)

ggplot(dataset, aes(x = Predictor, y = Afhankelijke_variabele)) +
    geom_point() + ylab("Afhankelijke variabele") + 
    geom_smooth(method = "lm", se = FALSE, formula = "y ~1") + 
    geom_segment(aes(x = Predictor, y = Afhankelijke_variabele,
                   xend = Predictor, yend = Fit)) +
  ggtitle("Interceptmodel")


# <!-- ## /CLOSEDBLOK: Regressie1.R -->
#   </div>
#   <div class = "col">
# <!-- ## CLOSEDBLOK: Regressie2.R -->

# In[ ]:


set.seed(12345)
x <- rnorm(100,5,2)
y <- 3 + 1.2 * x + rnorm(100,0,1)
dataset <- data.frame(Afhankelijke_variabele = y, Predictor = x)

model <- lm(Afhankelijke_variabele ~ Predictor, data = dataset)
dataset$Fit <- fitted(model)

ggplot(dataset, aes(x = Predictor, y = Afhankelijke_variabele)) +
    geom_point() + geom_smooth(method = "lm", se = FALSE) + ylab("Afhankelijke variabele") +
    geom_segment(aes(x = Predictor, y = Afhankelijke_variabele,
                   xend = Predictor, yend = Fit)) + 
  ggtitle("Regressiemodel")


# <!-- ## /CLOSEDBLOK: Regressie2.R -->
#   </div>
# </div>
# 
# *Figuur 1.  Illustratie van multipele lineaire regressie met behulp van een interceptmodel (links) en een regressiemodel (rechts) waarbij de punten de observaties zijn, de blauwe lijn de voorspelling van het model en de zwarte lijn het residu.*
# 
# Beide figuren laten een manier zien om een goede voorspelling te maken. De punten zijn de observaties, de blauwe lijn is de voorspelling en de zwarte lijnen zijn het verschil tussen observatie en voorspelling oftewel het residu. In de linkerfiguur wordt de voorspelling gemaakt met behulp van alleen een intercept (horizontale lijn), dit heet een interceptmodel. Echter, in de rechterfiguur wordt de voorspelling gemaakt door een lijn te trekken waarbij de kwadraten van de residuën zo klein mogelijk zijn. Het trekken van de best passende lijn is in feite wat er gedaan wordt bij *multipele lineaire regressie*.
# 
# ## F-toets voor significantie regressiemodel
# 
# Een maat om de kwaliteit van de voorspellingen van het regressiemodel te kwantificeren is de verklaarde variantie van de afhankelijke variabele. De verklaarde variantie - ook wel $R^2$ genoemd - wordt berekend als 1 minus de onverklaarde variantie. De onverklaarde variantie wordt berekend door de som van gekwadrateerde residuën van het regressiemodel te delen door de som van gekwadrateerde residuën van het interceptmodel. De kwaliteit van het regressiemodel wordt dus altijd vergeleken ten opzichte van het interceptmodel. Een goed regressiemodel heeft kleine residuën, wat leidt tot een lage onverklaarde variantie en dus een hoge verklaarde variantie.[^2]
# 
# De eerste vraag bij *multipele lineaire regressie* is of het model betere voorspellingen geeft dan een model zonder predictors. Daarom wordt het voorgestelde model vergeleken met een interceptmodel. Er is de verwachting van een toename in verklaarde variantie als beide modellen vergeleken worden. De significantie van deze toename wordt getoetst met een F-toets. De getoetste nulhypothese is dat de verklaarde variantie nul is ($R^2 = 0$) en de getoetste alternatieve hypothese is dat de verklaarde variantie groter dan nul is ($R^2 > 0$). Als de toename in verklaarde variantie significant is, kunnen de individuele predictors getoetst worden. Als de toename niet significant is, is de analyse afgelopen en is de conclusie dat het voorgestelde model niet in staat is om de afhankelijke variabele beter te voorspellen dan een model zonder predictors. De verklaarde variantie $R^2$ wordt ook gebruikt als effectmaat bij *multipele lineaire regressie*. Een verklaarde variantie rond 0,02 kan geïnterpreteerd worden als een klein effect, rond 0,13 als een gemiddeld effect en rond 0,26 als een groot effect.[^2]
# 
# De F-toets kan ook gebruikt worden om verschillende regressiemodellen onderling te vergelijken. Hierbij wordt getoetst of er een verschil is tussen de verklaarde variantie van beide modellen. Er kan bijvoorbeeld in eerste instantie een model met twee predictors getoetst worden en daarna toetsen of de voorspellingen van het regressiemodel nog beter worden met twee extra predictors. Het verschil in verklaarde variantie tussen het model met twee en vier predictors wordt dan getoetst met een F-toets. Hierbij is de nulhypothese dat het verschil in verklaarde variantie nul is ($\Delta R^2 = 0$) en de alternatieve hypothese dat het verschil in verklaarde variantie groter dan nul is ($\Delta R^2 > 0$). 
# 
# Een eis voor deze toets is dat beide modellen genest zijn. Bij geneste modellen is het ene model te schrijven als een versie van het andere model na het verwijderen van een aantal predictors. 
# In deze casus zou er een model opgesteld kunnen worden waarin alleen de variabele eindexamencijfer Wiskunde een predictor is van het eindcijfer Methoden & Statistiek en een model waarin de de variabelen geslacht, aantal gevolgde hoorcolleges en eindexamencijfer Wiskunde predictors zijn van statistiek. Dit zijn geneste modellen, omdat het eerste model (alleen eindexamencijfer Wiskunde als predictor) een versie is van het tweede model na het verwijderen van de predictors geslacht en aantal gevolgde hoorcolleges. Het model waarbij de predictors verwijderd zijn, wordt als het ware gereduceerd. Daarom wordt dit het gereduceerde model genoemd. Het model waar de predictors niet verwijderd zijn, wordt het uitgebreide model genoemd. Om modellen met een F-toets te vergelijken, moeten ze dus genest zijn. In andere woorden, het verschil tussen beide regressiemodellen moet dus toe te wijzen zijn aan het toevoegen of verwijderen van een of meerdere predictors.[^2]

# ## Individuele predictors toetsen en interpreteren
# 
# Als de F-toets aantoont dat het regressiemodel betere voorspellingen geeft dan het interceptmodel, kunnen de predictors getoetst worden. De regressiecoefficiënten van de predictors en de intercept worden getoetst met een t-toets waarbij de nulhypothese is dat de coefficiënt gelijk aan nul is ($\beta = 0$) en de (tweezijdige) alternatieve hypothese dat de coefficiënt niet gelijk aan nul is ($\beta \neq 0$). Er kan ook een eenzijdige alternatieve hypothese opgesteld worden, bijvoorbeeld als er verwacht wordt dat de coefficiënt positief of negatief is. De t-toets toont in feite aan of er wel of geen relatie is tussen de predictor en afhankelijke variabele in de aanwezigheid van de andere predictoren van het regressiemodel.[^2]
# 
# Op basis van de geschatte regressiecoefficiënten kan de regressievergelijking ingevuld worden. Op basis van de data zou bijvoorbeeld de volgende regressievergelijking gemaakt kunnen worden
# 
# $$ EindcijferM\&S_i = 3 + 0,5 * Geslacht_i + 0,4 * EindexamencijferWiskunde_i + 0,3 * AantalHoorcolleges_i  +  e_i$$
# waarbij alle regressiecoefficiënten significant zijn. Neem aan dat de variabele Geslacht de waarde 1 heeft voor vrouwen en 0 voor mannen. De regressiecoefficiënten geven informatie over de relatie van predictoren met de afhankelijke variabele:
# 
# * Intercept ($\beta_0$): De intercept geeft de waarde van de afhankelijke variabele weer als alle predictors gelijk aan nul zijn. Als een deelnemer dus de waarde 0 voor Geslacht heeft (dus een man is) en een 0 voor Eindexamencijfer_Wiskunde heeft, dan is het voorspelde eindcijfer Methoden & Statistiek een 3. De intercept geeft soms geen realistische waarde voor de afhankelijke variabele omdat het onwaarschijnlijk is dat de predictor gelijk is aan nul. Met een eindexamencijfer Wiskunde dat gelijk is aan een nul zou iemand nooit bij de bachelor Onderwijskunde terecht kunnen komen. An sich is dit geen groot probleem, omdat het niet altijd nodig is de intercept te kunnen interpreteren. Een oplossing is het centeren van de predictors wat inhoudt dat per predictor het gemiddelde van die predictor van alle waarden wordt afgehaald. Op die manier ontstaat een predictor met een gemiddelde van nul. In die situatie is de intercept gelijk aan de voorspelde waarde van de afhankelijke variabele voor een deelnemer die voor alle predictors gelijk is aan het gemiddelde. Het is in feite de voorspelde waarde voor een gemiddelde deelnemer en daarom erg interessant.
# * Geslacht ($\beta_1$): De coefficiënt van de variabele Geslacht is gelijk aan 0,5. Als de overige predictors gelijkblijven is het eindcijfer Methoden & Statistiek 0,5 punten hoger voor vrouwen dan voor mannen. Immers, het product van predictor en coëfficient is $0,5 * 0 = 0$ voor mannen en $0,5 * 1 = 0,5$ voor vrouwen. In een regressiemodel worden categorische variabelen omgezet in binaire variabelen met de waarden 0 en 1, omdat dat nodig is om het model te fitten. De variabele Geslacht zou bijvoorbeeld gecodeerd kunnen worden met een 1 voor mannen en een 0 voor vrouwen. Let goed op hoe de categorieën gecodeerd zijn, i.e. welke categorie de waarde 1 en 0 hebben. Dit bepaalt namelijk de interpretatie.
# * Eindexamencijfer_Wiskunde: De coëfficient van de variabele Eindexamencijfer_Wiskunde is gelijk aan 0,4. Dit betekent dat een toename van 1 van de variabele Eindexamencijfer_Wiskunde zorgt voor een toename van 0,4 op de afhankelijke variabele Eindcijfer Methoden & Statistiek als de andere predictors gelijkblijven. Er is dus een positieve relatie tussen het eindexamencijfer Wiskunde en het eindcijfer Methoden & Statistiek. Een deelnemer met een eindexamencijfer Wiskunde dat één punt hoger is dan een andere deelnemer zal dus een voorspelde waarde voor het eindcijfer Methoden & Statistiek hebben van 0,4 punt hoger als de overige predictors gelijkblijven.
# * Aantal_Hoorcolleges: De coëfficient van de variabele Aantal_Hoorcolleges is gelijk aan 0,3. Dit betekent dat een toename van 1 van de variabele Aantal_Hoorcolleges zorgt voor een toename van 0,3 op de afhankelijke variabele Eindcijfer Methoden & Statistiek als de andere predictors gelijkblijven. Er is dus een positieve relatie tussen het aantal gevolgde hoorcolleges en het eindcijfer Methoden & Statistiek. Een deelnemer met een extra gevolgd hoorcollege dan een andere deelnemer zal dus een voorspelde waarde voor het eindcijfer Methoden & Statistiek hebben van 0,3 punt hoger als de overige predictors gelijkblijven.
# 
# ## Predictors vergelijkingen door standaardisatie
# 
# Op basis van de regressievergelijking en de t-toetsen kan bepaald worden of predictors gerelateerd zijn aan de afhankelijke variabele en wat de invloed van een verandering van de predictor is op de afhankelijke variabele. Een andere relevante vraag is welke predictor het sterkst gerelateerd is aan de afhankelijke variabele. Op basis van de regressiecoëfficienten kan dit niet bepaald worden, omdat de schaal van de predictors verschilt. Het eindexamencijfer Wiskunde varieert tussen de 1 en 10 terwijl de variabele Geslacht gelijk is aan een 1 of een 0. 
# 
# Standaardiseer de afhankelijke variabele en de predictors om de predictors onderling te kunnen vergelijken. Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$. Als het regressiemodel opnieuw geschat wordt met gestandaardiseerde variabelen, kunnen de coëfficiënten onderling vergeleken worden op basis van hun grootte. Een grotere (absolute waarde van de) coëfficient betekent een sterkere relatie met de afhankelijke variabele. De coëfficiënt is nu te interpreteren in termen van standaardafwijkingen. Een toename van één eenheid van de predictor staat voor een toename van een standaardafwijking van deze predictor. Deze toename van één standaardafwijking zorgt ervoor dat de afhankelijke variabele $b$ standaardafwijkingen toeneemt waarbij $b$ de coëfficiënt van de regressievergelijking met gestandaardiseerde variabelen is.[^2] De predictor met de hoogste absolute waarde van de regressiecoëfficiënt is het sterkst gerelateerd aan de afhankelijke variabele.
# 
# ## Voorspellen op basis van het regressiemodel
# 
# Een regressiemodel maakt het mogelijk om een afhankelijke variabele te voorspellen op basis van een aantal predictors. Als van een student bekend is wat zijn geslacht, eindexamencijfer Wiskunde en aantal gevolgde hoorcolleges is, kan een voorspelling gemaakt worden van het eindcijfer Methoden & Statistiek voor die student. Voor alle deelnemers in de steekproef is er een voorspelling. De regressievergelijking maakt het echter ook mogelijk om voor nieuwe deelnemers een voorspelling te maken. Dit wordt een out-of-sample voorspelling genoemd omdat de nieuwe deelnemer niet in de steekproef zit waarop het regressiemodel wordt geschat. Als de docent een jaar later de eindcijfers wilt voorspellen van de studenten die zijn vak volgen, kan hij de regressievergelijking van het jaar ervoor gebruiken. Een mannelijke student met een 7 als eindexamencijfer Wiskunde die 8 hoorcolleges volgt, heeft een voorspeld eindcijfer voor het vak Methoden & Statistiek 
# 
# $$ EindcijferM\&S_i = 3 + 0,5 * 0 + 0,4 * 7 + 0,3 * 8 = 8,2$$
# een 8,2. Een out-of-sample voorspelling geeft vaak een goede indicatie van de kwaliteit van het regressiemodel, omdat de nieuwe deelnemer niet gebruikt zijn om het model te schatten. Als het doel is om het regressiemodel te gebruiken voor het voorspellen van nieuwe deelnemers, dan is de kwaliteit van de out-of-sample voorspellingen van belang.[^2]
# 
# # Uitleg assumpties
# 
# Om een valide resultaat te vinden met *multipele lineaire regressie*, dient er aan een aantal assumpties voldaan te worden.[^1]<sup>,</sup>[^2] In deze sectie worden de assumpties allen toegelicht en worden de opties bij het niet voldoen aan de assumptie weergegeven. Verderop in de toetspagina worden de assumpties getoetst met de dataset van de onderwijscasus.
# 
# ## Outliers
# 
# Voordat gestart kan worden met *multipele lineaire regressie*, moet de data gescreend worden op de aanwezigheid van outliers. Outliers (uitbijters) zijn observaties die sterk afwijken van de overige observaties. Univariate outliers zijn observaties die afwijken voor één specifieke variabele, zoals een student die twintig jaar over zijn studie heeft gedaan. Multivariate outliers zijn observaties die afwijken door de combinatie van meerdere variabelen, zoals een persoon van 18 jaar met een inkomen van €100.000,-. De leeftijd van 18 jaar is geen outlier op zichzelf en een inkomen van €100.000,- is dat ook niet. Echter, de combinatie van beide zorgt ervoor dat de observatie vrij onwaarschijnlijk is.[^2]
# 
# Na het vinden van een outlier is de volgende stap om een goede oplossing voor te outlier te bedenken. Het is van belang hier goed over na te denken en niet zomaar een outlier te verwijderen met als enige argument dat het een outlier is. In het algemeen kan er onderscheid gemaakt worden tussen onmogelijke en onwaarschijnlijke outliers.[^3] Een onmogelijke outlier is een observatie die technisch gezien niet kan kloppen, bijvoorbeeld een leeftijd van 1000 jaar, een negatief salaris of een man die zwanger is. Bij deze outliers is het een optie om de waarde te vervangen als er een overduidelijke fout bij het invoeren van de data is gemaakt. Een andere optie is de waarde te verwijderen. Een onwaarschijnlijke outlier is een observatie die technisch gezien wel kan, maar heel erg afwijkt van de overige observaties. De rijksten der aarde zijn in de stad of het dorp waar zij wonen qua vermogen waarschijnlijk een outlier. Maar het zijn bestaande personen dus het verwijderen van de observatie zou hier foutief zijn. Opties in deze situatie zijn de variabele(n) te transformeren, de outlier gewoon mee te nemen in de analyse of de analyse met en zonder de outlier uit te voeren en beide te rapporteren. Ook is het niet verboden om de outlier toch te verwijderen, maar het is in dat geval wel van belang dit transparant te rapporteren en op een goede wijze te beargumenteren.[^3]
# 
# Bij *multipele lineaire regressie* zijn er vier nuttige methoden om outliers te vinden.[^2]
# 
# ### Boxplots en standaardiseren
# 
# Begin voor de analyse met het screenen van de variabelen in de dataset op de aanwezigheid van univariate outliers. Voor continue variabelen bestaat deze screening uit het visualiseren van de variabele met een boxplot en het standaardiseren[^4] van de variabele. Als een observatie een gestandaardiseerde score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. In dat geval wijkt de observatie namelijk meer dan drie standaardafwijkingen af van het gemiddelde van de variabele. Gebruik zowel de boxplot als de standaardisering om outliers te vinden voor continue variabelen.[^3]
# 
# Bij categorische variabelen hebben boxplots en standaardisatie geen zin, omdat het geen variabelen met een continue schaal zijn. Bij categorische variabelen is het nuttig om een overzicht te maken van de bestaande categorieën en bijbehorende aantallen observaties en is het nuttig om te onderzoeken of elke observatie slechts in één categorie past. Doe dit met behulp van tabellen.
# 
# ### Gestandaardiseerde residuën
# 
# De residuën van een regressiemodel zijn de verschillen tussen de observaties van de afhankelijke variabele en de voorspellingen. Als er een groot verschil is tussen observatie en voorspelling, zou dat kunnen wijzen op een univariate outlier. Standaardiseer daarom de residuën en onderzoek met een histogram of er outliers zijn. Als een observatie een gestandaardiseerde score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. Op deze manier kunnen outliers bij het regressiemodel kunnen worden geïdentificeerd.[^2]
# 
# ### Mahalanobis afstand
# 
# Multivariate outliers zijn deelnemers met een combinatie van observaties op verschillende variabelen die erg afwijken van de overige deelnemers. Deze multivariate outliers kunnen geïdentificeerd worden met de Mahalanobis afstand. De Mahalanobis afstand is een maat die aangeeft in hoeverre de observaties van een deelnemer voor alle predictors afwijken van de gemiddeldes van de predictors. Het is een maat voor een afstand tussen twee punten als meerdere variabelen worden gebruikt. Bereken de Mahalanobis afstand voor elke deelnemer en vergelijk deze met de criteriumwaarde. De criteriumwaarde wordt bepaald op basis van de chi-kwadraat score bij een aantal vrijheidsgraden dat gelijk is aan het aantal predictors en een significantieniveau van 0,001 (of een zelf gekozen significantieniveau). In de code wordt toegelicht hoe de criteriumwaarde bepaald kan worden.[^2]
# 
# ### Cook's afstand
# 
# De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van de andere deelnemers wat betreft de waardes van de predictorvariabelen. Een andere manier om multivariate outliers te vinden is te bepalen hoeveel invloed een deelnemer heeft op de schattingen van het regressiemodel. Als de uitkomsten van het regressiemodel sterk veranderen als een bepaalde deelnemer weggelaten wordt uit de dataset, dan is deze deelnemer invloedrijk. Met behulp van Cook's afstand worden invloedrijke deelnemers ontdekt. Als Cook's afstand groter dan 1 is, wordt de deelnemer beschouwd als invloedrijk.
# 
# Hoewel de Mahalanobis afstand en Cook's afstand beide multivariate outliers identificeren, verschillen ze in het soort outlier waarop de focus ligt. Bij de Mahalanobis afstand worden afwijkende datapunten gevonden en bij Cook's distance invloedrijke datapunten. Het is echter niet zo dat een afwijkend datapunt ook tegelijkertijd invloedrijk is en dat een invloedrijk datapunt ook afwijkt. Een afwijkend datapunt kan ondanks zijn afwijking van de de overige datapunten toch op een juiste manier voorspeld worden. En een invloedrijk datapunt hoeft niet per se sterk af te wijken van de overige datapunten wat betreft de waardes voor de predictorvariabelen. Houdt hier rekening mee bij het bepalen hoe om te gaan met de gevonden outlier(s).[^2]
# 
# ## Lineariteit
# 
# De regressievergelijking is zo opgesteld dat er een lineaire relatie is tussen elke predictor en de afhankelijke variabele. Een lineaire relatie houdt in dat de toename of afname van de afhankelijke variabele als gevolg van de toename van de predictor constant is: er is een rechte lijn door de data heen te trekken. Een voorbeeld van een lineaire en niet-lineaire relatie is weergegeven in onderstaande figuren. Bij de linkerfiguur kan er duidelijk een rechte lijn door de punten getrokken worden en is er dus sprake van een lineaire relatie. Bij de rechterfiguur is dit niet het geval, daar is er sprake van een curve in de relatie tussen predictor en afhankelijke variabele. De regressiecoëfficiënt van een niet-lineair verband is dan niet informatief, omdat er dan niet aan lineariteit voldaan is.[^2]<sup>,</sup>[^6] 
# 
# De assumptie van lineariteit wordt onderzocht met behulp van scatter plots, zoals in onderstaande figuren. Deze assumptie hoeft alleen onderzocht te worden voor continue variabelen. Categorische variabelen worden in het regressiemodel omgezet naar variabelen met twee categorieën en met slechts twee categorieën kan niet onderzocht worden of er een lineaire relatie is. Als er geen lineaire relatie is, zijn er verschillende opties. De variabele kan op verschillende manieren getransformeerd[^5] worden zodat er alsnog een lineaire relatie ontstaat. Als er geen geschikte transformatie gevonden kan worden, dan is het verwijderen van de variabele ook een optie, maar dit heeft logischerwijs niet de voorkeur.
# 
# <div class = "col-container">
#   <div class="col">
# <!-- ## CLOSEDBLOK: Lineariteit1.R -->

# In[ ]:


set.seed(12345)
x <- rnorm(100,0,2)
y <- 3 + 1.2 * x + rnorm(100,0,1)
dataset <- data.frame(Afhankelijke_variabele = y, Predictor = x)

ggplot(dataset, aes(x = Predictor, y = Afhankelijke_variabele)) +
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
dataset <- data.frame(Afhankelijke_variabele = y, Predictor = x)

ggplot(dataset, aes(x = Predictor, y = Afhankelijke_variabele)) +
    geom_point()  + ylab("Afhankelijke variabele") +
  ggtitle("Niet-lineaire relatie")


# <!-- ## /CLOSEDBLOK: Lineariteit2.R -->
#   </div>
# </div>
# 
# *Figuur 2.  Voorbeeld van een lineaire (links) en niet-lineaire (rechts) relatie tussen een afhankelijke variabele en een predictor.*
# 
# ## Normaliteit van residuën
# 
# De residuën van het regressiemodel moeten normaal verdeeld zijn met een gemiddelde van ongeveer 0. Als er niet aan deze assumptie is voldaan, zijn de standaardfouten, betrouwbaarheidsintervallen en significantietoetsen van de regressiecoëfficiënten incorrect. De regressiecoëfficiënten zelf zijn echter wel betrouwbaar als deze assumptie wordt geschonden. De assumptie wordt getoetst door een histogram te maken van de gestandaardiseerde residuën. Als de verdeling van de gestandaardiseerde residuën sterk afwijkt van de normale verdeling, is de assumptie geschonden. Een oplossing hiervoor is het bootstrappen van de standaardfouten, betrouwbaarheidsintervallen en significantietoetsen. Een uitleg over bootstrappen volgt later in deze toetspagina.[^2]
# 
# ## Homoskedasticiteit
# 
# Homoskedasticiteit houdt in dat de variantie van de residuën niet afhangt van de waarden van de predictors. Als er niet voldaan is aan deze assumptie (dit heet heteroskedasticiteit), zijn de coëfficiënten nog steeds correct, maar de standaardfouten, betrouwbaarheidsintervallen en significantietoetsen van de coëfficiënten niet meer. Deze assumptie wordt getoetst door een scatter plot te maken van de voorspellingen van het regressiemodel versus de gestandaardiseerde residuën. Onderstaande figuur geeft een voorbeeld weer van homoskedasticiteit en heteroskedasticiteit. Bij heteroskedasticiteit is zichtbaar dat de variantie in de residuën toeneemt als de waarde van de voorspellingen toeneemt. Als deze assumptie geschonden is, is het bootstrappen van de standaardfouten, betrouwbaarheidsintervallen en significantietoetsen een oplossing. Een andere oplossing is het uitvoeren van weighted least squares regressie waarbij rekening wordt gehouden met de verschillen in variantie.[^2]
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
# *Figuur 3.  Voorbeeld van homoskedasticiteit (links) en heteroskedasticiteit (rechts) van residuën van een regressiemodel.*
# 
# ## Multicollineariteit
# 
# Multicollineariteit houdt in dat er een hoge correlatie tussen twee of meerdere predictors is. Er is perfecte multicollineariteit als één predictor een lineaire combinatie is van een of meerdere andere predictors. In andere woorden, de predictor is precies te berekenen op basis van andere predictor(s). In dat geval kan de regressievergelijking niet wiskundig bepaald worden en werkt *multipele lineaire regressie* niet. Dit komt zeer weinig voor en is vaak makkelijk op te lossen door goed naar de variabelen die het veroorzaken te kijken en een variabele te transformeren of te verwijderen.[^2]
# 
# Bij een hoog niveau van multicollineariteit kan de regressievergelijking wel geschat worden, maar zijn de uitkomsten minder betrouwbaar. De standaardfouten van de regressiecoëfficiënten worden groter bij meer multicollineariteit en dit levert bij hoge multicollineariteit problemen op. Ook is het lastig om te ontdekken wat per predictor de bijdrage is aan de voorspellingen van de afhankelijke variabele, omdat bepaalde predictors sterk gecorreleerd zijn en overlappen in het deel van de variantie dat ze verklaren.[^2] 
# 
# Multicollineariteit wordt getoetst met de Variance Inflation Factor (VIF) die meet hoe sterk elke predictor gecorreleerd is met de andere predictors. Als de VIF van een predictor hoger dan 10 is, is er multicollineariteit voor die predictor.[^2]<sup>,</sup>[^7] Multicollineariteit kan opgelost worden door een van de predictors die het veroorzaakt te verwijderen uit het model. Een andere optie is een principale componenten analyse (PCA) uitvoeren op de predictoren zodat er een onderliggende variabele gecreëerd wordt (zie Field[^2] voor meer informatie).
# 
# # Bootstrappen
# 
# Als er niet voldaan is aan de assumpties van normaliteit of  homoskedasticiteit, dan zijn de standaardfouten, betrouwbaarheidsintervallen en significantietoetsen van het regressiemodel incorrect. Bootstrappen is hier een oplossing voor. Bij bootstrappen wordt de verdelingen van de parameters van het regressiemodel nagebootst. Als eerste stap wordt de steekproef gezien als een populatie waaruit een nieuwe steekproef getrokken kan worden. Deze steekproef is even groot als de echte steekproef, maar toch verschillend omdat het mogelijk is dezelfde deelnemer meerdere keren in de steekproef te hebben. Op basis van de nieuwe steekproef wordt het regressiemodel opnieuw geschat en is er een schatting van de regressiecoëfficiënten. Deze procedure wordt een groot aantal keer (10000) herhaald, waardoor er 10000 keer regressiecoëfficiënten worden bepaald. Met behulp van deze 10000 waarden van de regressiecoëfficiënten is er een verdeling gemaakt voor elke regressiecoëfficiënt waaruit de standaardfout en de betrouwbaarheidsintervallen kunnen worden berekend. Op basis van de betrouwbaarheidsintervallen kunnen er ook significantietoetsen worden uitgevoerd. Op deze manier is bootstrappen de oplossing voor *multipele lineaire regressie* als er niet voldaan is aan normaliteit of homoskedasticiteit.[^2]
# 
# # Toetsing assumpties
# 
# Voer *multipele lineaire regressie* uit om te onderzoeken of het eindcijfer voor het vak Methoden & Statistiek van de bachelor Onderwijskunde te voorspellen is op basis van het geslacht, eindexamencijfer Wiskunde en aantal gevolgde hoorcolleges. Start met het toetsen van de assumpties en voer vervolgens de *multipele lineaire regressie* uit als hieraan voldaan is.
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Voer eerst de *multipele lineaire regressie* uit omdat deze nodig is voor het toetsen van assumpties en sla het resultaat op. Interpreteer de resultaten pas na het toetsen van de assumpties. Gebruik de functie `lm()` met als eerste argument de regressievergelijking `Eindcijfer_MS ~ Geslacht + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges` met links van het golfteken de afhankelijke variabele `Eindcijfer_MS` en rechts de drie onafhankelijke variabelen `Eindexamencijfer_Wiskunde`, `Aantal_Hoorcolleges` en `Eindcijfer_MS`. Het tweede argument is de dataset `Studenten_Methoden_Statistiek`.
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


Regressiemodel <- lm(Eindcijfer_MS ~ Geslacht + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges, Studenten_Methoden_Statistiek)


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# ## Outliers
# 
# ### Boxplots en standaardiseren
# 
# <!-- ## TEKSTBLOK: Outlier1.R -->
# Onderzoek of er univariate outliers zijn met behulp van boxplots en gestandaardiseerde scores voor continue variabelen en tabellen voor categorische variabelen. Begin met de boxplot voor de variabelen `Eindexamencijfer_Wiskunde`, `Aantal_Hoorcolleges` en `Eindcijfer_MS`.
# <!-- ## /TEKSTBLOK: Outlier1.R -->
# 
# <!-- ## OPENBLOK: Outlier2.R -->

# In[ ]:


# Maak een boxplot van de continue variabelen in de dataset
boxplot(Studenten_Methoden_Statistiek[,c("Eindexamencijfer_Wiskunde",
                                         "Aantal_Hoorcolleges",
                                         "Eindcijfer_MS")],
        names = c("Cijfer Wiskunde",
                                         "Hoorcolleges",
                                         "Cijfer M&S"))


# <!-- ## /OPENBLOK: Outlier2.R -->
# 
# Voor alle drie de variabelen zijn er geen onmogelijke scores en zijn er geen grote afwijkingen.  
# 
# Onderzoek de gestandaardiseerde scores door een functie te schrijven die het aantal observaties per variabele telt met een gestandaardiseerde score hoger dan 3 of lager dan -3. Pas deze functie vervolgens toe op de drie continue variabelen in de dataset.
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
Outlier_standaardiseren(Studenten_Methoden_Statistiek$Eindexamencijfer_Wiskunde)
Outlier_standaardiseren(Studenten_Methoden_Statistiek$Aantal_Hoorcolleges)
Outlier_standaardiseren(Studenten_Methoden_Statistiek$Eindcijfer_MS)


# <!-- ## /OPENBLOK: Outlier3.R -->
# 
# Alle drie de variabelen hebben nul observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3. Er zijn in de stap voor de continue variabelen geen outliers gevonden.
# 
# Geslacht is de enige categorische variabele in deze dataset. Maak een tabel met de frequenties voor alle categoriëen van deze variabele om te onderzoeken of hier afwijkende waardes zijn.
# 
# <!-- ## OPENBLOK: Outlier4.R -->

# In[ ]:


table(Studenten_Methoden_Statistiek$Geslacht)


# <!-- ## /OPENBLOK: Outlier4.R -->
# 
# De categorieën van de variabele Geslacht zijn `Man` en `Vrouw`; beide komen redelijk veel voor. Er zijn dus geen opmerkelijke waarden bij de variabele Geslacht.
# 
# ### Gestandaardiseerde residuën
# 
# <!-- ## TEKSTBLOK: Outlier5.R -->
# Onderzoek of er outliers zijn met behulp van de gestandaardiseerde residuën van het regressiemodel. Vind eerst de residuën met de functie `rstandard` met als argument `Regressiemodel` (het object van het regressiemodel). Maak vervolgens een plot en tel het aantal gestandaardiseerde residuën met een waarde hoger dan 3 of lager dan -3.
# <!-- ## /TEKSTBLOK: Outlier5.R -->
# 
# <!-- ## OPENBLOK: Outlier6.R -->

# In[ ]:


# Sla de gestandaardiseerde residuën op
Residu_gestandaardiseerd <- rstandard(Regressiemodel)

# Maak een plot
plot(Residu_gestandaardiseerd, xlab = "Volgorde", ylab = "Gestandaardiseerde residuën")

# Tel het aantal gestandaardiseerde residuën met een absolute waarde groter dan 3
sum(abs(Residu_gestandaardiseerd > 3))


# <!-- ## /OPENBLOK: Outlier6.R -->
# 
# Er zijn geen gestandaardiseerde residuën met een score hoger dan 3 of lager dan -3 wat er op wijst dat er geen outliers in de data zijn.
# 
# ### Mahalanobis distance
# 
# <!-- ## TEKSTBLOK: Outlier7.R -->
# Onderzoek of er multivariate outliers zijn met behulp van de Mahalanobis distance met behulp van de functie `mahalanobis()`. De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van het gemiddelde van alle deelnemers voor alle predictors samen. Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Zet daarom eerst de variabele `Geslacht` om in een numerieke variabele met de waarde 1 voor vrouwen en 0 voor mannen. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd.
# 
# Neem vervolgens een subset van de dataset met alleen de predictors en gebruik deze voor de mahalanobis afstand. Gebruik de functie `mahalanobis()` met als argumenten de dataset `Subset`, de gemiddeldes van elke kolom berekend met `colMeans(Subset)` en de covariantiematrix van de dataset berekend met `cov(Subset)`.
# 
# Bereken daarna de criteriumwaarde op basis van het gewenste significantieniveau en het aantal predictors. Plot de Mahalanobis afstanden en tel het aantal deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde. Het gehanteerde significantieniveau is 0,001.
# <!-- ## /TEKSTBLOK: Outlier7.R -->
# 
# <!-- ## OPENBLOK: Outlier8.R -->

# In[ ]:


# Zet Geslacht om in een numerieke variabele met een 1 voor een vrouw en 0 voor een man
Studenten_Methoden_Statistiek$Geslacht_numeriek <- as.numeric(Studenten_Methoden_Statistiek$Geslacht == "Vrouw")

# Maak een subset van de dataset met alle predictors
Subset <- Studenten_Methoden_Statistiek[,c("Eindexamencijfer_Wiskunde",
                                           "Aantal_Hoorcolleges",
                                           "Eindcijfer_MS",
                                           "Geslacht_numeriek")]

# Bereken de Mahalanobis afstand voor elke deelnemer 
Mahalanobis_afstanden <- mahalanobis(Subset,
            colMeans(Subset),
            cov(Subset))

# Bepaal de criteriumwaarde voor de Mahalanobis afstand met de functie qchisq() met als eerste argument 1 - het significantieniveau en als tweede argument het aantal predictors. In deze casus is het significantieniveau voor de Mahalanobis afstand 0.001 en het aantal predictors berekend met ncol(Subset).
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
# Onderzoek of er multivariate outliers zijn met behulp van Cook's afstand. Cook's afstand geeft aan hoeveel invloed het weglaten van een deelnemer heeft op de uitkomsten van het regressiemodel. Gebruik hiervoor de functie `cooks.distance` met als argument  `Regressiemodel` (het object van het regressiemodel). Plot de Cook's afstanden daarna en tel het aantal Cook's afstanden dat groter is dan de criteriumwaarde van 1.
# <!-- ## /TEKSTBLOK: Outlier10.R -->
# 
# <!-- ## OPENBLOK: Outlier11.R -->

# In[ ]:


# Bepaal Cook's afstand voor elke deelnemer
Cooks_afstand <-  cooks.distance(Regressiemodel)

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
# Onderzoek of er een lineaire relatie is tussen de continue predictoren en de afhankelijke variabele met behulp van scatter plots. 
# 
# <div class = "col-container">
#   <div class="col">
# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


plot(Eindcijfer_MS ~ Eindexamencijfer_Wiskunde, data = Studenten_Methoden_Statistiek,
     xlab = "Eindexamencijfer Wiskunde", ylab = "Eindcijfer Methoden & Statistiek")


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
# Bij beide predictors lijkt er een lineaire relatie te zijn met de afhankelijke variabele. Er is dus aan de assumptie van lineariteit voldaan.
# 
# ## Normaliteit
# 
# <!-- ## TEKSTBLOK: AssNormaliteit1.R -->
# Onderzoek of de gestandaardiseerde residuën van het regressiemodel een normale verdeling volgen. Sla eerst de gestandaardiseerde residuën op met behulp van de functie `rstandard()` met als argument `Regressiemodel` (het object van het regressiemodel) en maak vervolgens een histogram[^18] om de verdeling te inspecteren. Het is ook mogelijk om normaliteit te onderzoeken met behulp van een QQ-plot.
# <!-- ## /TEKSTBLOK: AssNormaliteit1.R -->
# 
# <!-- ## OPENBLOK: AssNormaliteit2.R -->

# In[ ]:


# Sla de gestandaardiseerde residuën op
Residu_gestandaardiseerd <- rstandard(Regressiemodel)

# Maak een histogram
hist(Residu_gestandaardiseerd, xlab = "Gestandaardiseerde residuën", ylab = "Frequentie", main = "")


# <!-- ## /OPENBLOK: AssNormaliteit2.R -->
# 
# De verdeling van de gestandaardiseerde residuën lijkt een normaalverdeling te benaderen. Er is dus voldaan aan de assumptie van normaliteit.
# 
# ## Homoskedasticiteit
# 
# <!-- ## TEKSTBLOK: AssHomoskedasticiteit1.R -->
# Toets de assumptie van homoskedasticiteit door te onderzoeken of de variantie ongeveer gelijk is voor alle waarden van de voorspellingen van de afhankelijke variabele. Maak hiervoor een plot van de gestandaardiseerde residuën versus de voorspellingen. De gestandaardiseerde residuën zijn te vinden met de functie `rstandard()` met als argument `Regressiemodel` (het object van het regressiemodel) en de voorspellingen met de functie `fitted()` met wederom als argument `Regressiemodel`.
# <!-- ## /TEKSTBLOK: AssHomoskedasticiteit1.R -->
# 
# <!-- ## OPENBLOK: AssHomoskedasticiteit2.R -->

# In[ ]:


# Sla de gestandaardiseerde residuën op
Residu_gestandaardiseerd <- rstandard(Regressiemodel)

# Sla de voorspellingen op
Voorspellingen <- fitted(Regressiemodel)

# Maak een scatter plot
plot(Voorspellingen, Residu_gestandaardiseerd, ylab = "Gestandaardiseerde residuën", xlab = "Voorspellingen", main = "")


# <!-- ## /OPENBLOK: AssHomoskedasticiteit2.R -->
# 
# De spreiding van de gestandaardiseerde residuën lijkt redelijk constant te zijn voor de verschillende waarden van de voorspellingen. Er is dus voldaan aan de assumptie van homoskedasticiteit.
# 
# ## Multicollineariteit
# 
# <!-- ## TEKSTBLOK: AssMulticollineariteit1.R -->
# Onderzoek of er sprake is van multicollineariteit met behulp van Variance Inflation Factors (VIFs). Bereken de VIFs voor elke predictor met de functie `VIF()` van het package `DescTools` waarbij de functie als argument `Regressiemodel` (het object van het regressiemodel) heeft.
# <!-- ## /TEKSTBLOK: AssMulticollineariteit1.R -->
# 
# <!-- ## OPENBLOK: AssMulticollineariteit2.R -->

# In[ ]:


library(DescTools)

# Bereken de VIF voor elke predictor
VIF(Regressiemodel)


# <!-- ## /OPENBLOK: AssMulticollineariteit2.R -->
# 
# Geen enkele van de VIFs is hoger dan 10, dus er is voldaan aan de assumptie van multicollineariteit.
# 
# # Uitvoering
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Als alle assumpties zijn getoetst en aan alle assumpties is voldaan, kan de *multipele lineaire regressie* uitgevoerd worden. Gebruik de functie `lm()` met als eerste argument de regressievergelijking `Eindcijfer_MS ~ Geslacht + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges` met links van het golfteken de afhankelijke variabele `Eindcijfer_MS` en rechts de drie onafhankelijke variabelen `Eindexamencijfer_Wiskunde`, `Aantal_Hoorcolleges` en `Eindcijfer_MS`. Het tweede argument is de dataset `Studenten_Methoden_Statistiek`. Sla het model op en presenteer vervolgens een overzicht van de resultaten met de functie `summary`. Bepaal de 95%-betrouwbaarheidsintervallen van de regressiecoëfficiënten met de functie `confint`.
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


# Voer de multipele lineaire regressie uit
Regressiemodel <- lm(Eindcijfer_MS ~ Geslacht + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges,
                     Studenten_Methoden_Statistiek)

# Presenteer de resultaten
summary(Regressiemodel)

# Presenteer de 95%-betrouwbaarheidsintervallen
confint(Regressiemodel)


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# <!-- ## CLOSEDBLOK: Uitvoering3.R -->

# In[ ]:


# Voer de multipele lineaire regressie uit
Regressiemodel <- lm(Eindcijfer_MS ~ Geslacht + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges,
                     Studenten_Methoden_Statistiek)

# Presenteer de resultaten
Reg <- summary(Regressiemodel)
F_toets <- Reg$fstatistic
R2 <- Reg$r.squared
CI <- confint(Regressiemodel)


# <!-- ## /CLOSEDBLOK: Uitvoering3.R -->
# 
# ### Significantie regressiemodel
# 
# <!-- ## TEKSTBLOK: Ftoets1.R -->
# Bepaal als eerste stap de significantie van het regressiemodel met behulp van de F-toets. De F-toets voor het regressiemodel laat zien dat het opgestelde regressiemodel een significant hogere verklaarde variantie heeft dan het model met alleen een intercept, *F*(`r Round_and_format_0decimals(F_toets[2])`,`r Round_and_format_0decimals(F_toets[3])`) = `r Round_and_format(F_toets[1])`, *p* < 0,0001.[^8] De nulhypothese dat geen enkele predictor van de predictors geslacht, eindexamencijfer Wiskunde en aantal gevolgde hoorcolleges is gerelateerd aan de afhankelijke variabele eindcijfer Methoden & Statistiek kan verworpen worden. De verklaarde variantie $R^2$ is `r Round_and_format(100*R2)`. Omdat de F-toets voor het gehele model significant is, kunnen de coëfficiënten geinterpreteerd worden.
# <!-- ## TEKSTBLOK: Ftoets1.R -->
# 
# ### Significantie en interpretatie coëfficiënten.
# 
# <!-- ## TEKSTBLOK: Coefficienten1.R -->
# Voor de intercept en de regressiecoëfficiënten van de predictors zijn de geschatte coëfficiënt (`Estimate`), de standaardfout van de geschatte coëfficiënt (`Std. Error`) en de t-statistiek (`t value`) en p-waarde (`Pr(>|t|)`) van de t-toets voor de regressiecoëfficiënt weergegeven:
# 
# * Intercept: de geschatte waarde voor de intercept is `r Round_and_format(Reg$coefficients[1,1])` en is significant verschillend van 0 (*t* = `r Round_and_format(Reg$coefficients[1,3])`, *p* = `r Round_and_format(Reg$coefficients[1,4])`)[^8]. De intercept staat voor het voorspelde eindcijfer Methoden & Statistiek als alle predictors een waarde van nul hebben. Een man met een 0 als eindexamencijfer Wiskunde die nul hoorcolleges volgt zal naar verwachting een `r Round_and_format(Reg$coefficients[1,1])` behalen als eindcijfer voor het vak Methoden & Statistiek.
# * Geslacht: de geschatte waarde voor de regressiecoëfficiënt van de variabele Geslacht is `r Round_and_format(Reg$coefficients[2,1])` en is niet significant verschillend van 0 (*t* = `r Round_and_format(Reg$coefficients[2,3])`, *p* = `r Round_and_format(Reg$coefficients[2,4])`)[^8]. De coëfficiënt hoeft dus niet geïnterpreteerd te worden.
# * Eindexamencijfer_Wiskunde: de geschatte waarde voor de regressiecoëfficiënt van de variabele Eindexamencijfer_Wiskunde is `r Round_and_format(Reg$coefficients[3,1])` en is significant verschillend van 0 (*t* = `r Round_and_format(Reg$coefficients[3,3])`, *p* < 0,01)[^8]. Als het eindexamencijfer Wiskunde met één punt toeneemt, neemt de voorspelling voor het eindcijfer Methoden & Statistiek met `r Round_and_format(Reg$coefficients[3,1])` toe.
# * Aantal_Hoorcolleges: de geschatte waarde voor de regressiecoëfficiënt van de variabele Aantal_Hoorcolleges is `r Round_and_format(Reg$coefficients[4,1])` en is significant verschillend van 0 (*t* = `r Round_and_format(Reg$coefficients[4,3])`, *p* < 0,0001)[^8]. Als een student een extra hoorcollege volgt, neemt de voorspelling voor het eindcijfer Methoden & Statistiek met `r Round_and_format(Reg$coefficients[4,1])` toe.
# 
# <!-- ## /TEKSTBLOK: Coefficienten1.R -->
# 
# ### Sterkte van de relatie tussen de predictor en afhankelijke variabele
# 
# <!-- ## TEKSTBLOK: CoefficientenStd1.R -->
# De regressiecoëfficiënten van de predictors Eindexamencijfer_Wiskunde en Aantal_Hoorcolleges zijn significant verschillend van nul en dragen dus bij aan het voorspellen van het eindcijfer Methoden & Statistiek. Met behulp van de gestandaardiseerde regressiecoëfficiënten kan bepaald worden welke predictor het sterkst gerelateerd is aan de afhankelijke variabele. Gebruik hiervoor de functie `lm.beta()` van het package `QuantPsyc` met als argument `Regressiemodel_numeriek` (het object van het regressiemodel). Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Zet daarom eerst de variabele `Geslacht` om in een numerieke variabele met de waarde 1 voor vrouwen en 0 voor mannen. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd. Gebruik de numerieke variabele `Geslacht_numeriek` vervolgens om de *multipele lineaire regressie* uit te voeren met de functie `lm()` op dezelfde manier als eerder is gedaan.
# <!-- ## /TEKSTBLOK: CoefficientenStd1.R -->
# 
# <!-- ## OPENBLOK: CoefficientenStd2.R -->

# In[ ]:


# Laad het package QuantPsyc in
library(QuantPsyc)

# Zet Geslacht om in een numerieke variabele met een 1 voor een vrouw en 0 voor een man
Studenten_Methoden_Statistiek$Geslacht_numeriek <- as.numeric(Studenten_Methoden_Statistiek$Geslacht == "Vrouw")

# Stel het regressiemodel op met Geslacht als numerieke variabele
Regressiemodel_numeriek <- lm(Eindcijfer_MS ~ Geslacht_numeriek + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges, Studenten_Methoden_Statistiek)

# Bereken de gestandaardiseerde coefficienten
lm.beta(Regressiemodel_numeriek)


# <!-- ## /OPENBLOK: CoefficientenStd2.R -->
# 
# <!-- ## CLOSEDBLOK: CoefficientenStd3.R -->

# In[ ]:


Coefficienten_std <- lm.beta(Regressiemodel_numeriek)


# <!-- ## /CLOSEDBLOK: CoefficientenStd3.R -->
# 
# <!-- ## TEKSTBLOK: CoefficientenStd4.R -->
# De gestandaardiseerde regressiecoëfficiënt is `r Round_and_format(Coefficienten_std[2])` voor de predictor Eindexamen_Wiskunde en `r Round_and_format(Coefficienten_std[3])` voor de predictor Aantal_Hoorcolleges. Het aantal hoorcolleges heeft dus meer invloed op het eindcijfer Methoden & Statistiek dan het eindexamencijfer Wiskunde. Een toename van één standaardafwijking in het aantal hoorcolleges resulteert in een toename van `r Round_and_format(Coefficienten_std[3])` standaardafwijkingen in het eindcijfer Methoden & Statistiek. De gestandaardiseerde regressiecoëfficiënt van de variabele Geslacht_numeriek hoeft niet geïnterpreteerd te worden omdat deze niet significant is (de significatietoetsen veranderen niet door standaardisatie).
# <!-- ## /TEKSTBLOK: CoefficientenStd4.R -->
# 
# # Uitvoering F-toets voor vergelijking twee regressiemodellen
# 
# De F-toets wordt bij *multipele lineaire regressie* gebruikt om de significantie van het gehele regressiemodel te toetsen ten opzichte van het interceptmodel. Deze F-toets kan ook gebruikt worden om te toetsen of twee geneste regressiemodellen onderling verschillen qua verklaarde variantie. Hoewel deze vergelijking in de casus niet voorbijkomt, wordt deze toch geïllustreerd. Vergelijk hierbij een model met als enige predictor het geslacht van de student met een model met de predictors Geslacht, Eindexamencijfer_Wiskunde en Aantal_Hoorcolleges.
# 
# <!-- ## TEKSTBLOK: ModellenVergelijken1.R -->
# Voer de F-toets uit met de functie `anova()` met als argumenten de modelobjecten van de resultaten van de twee regressiemodellen die worden vergeleken (`Model_1` en `Model_2`). Voer eerst de *multipele lineaire regressie* uit voor beide modellen en vergelijk ze daarna. Bereken ten slotte de verklaarde variantie met de functie `summary()$r.squared` met als argument het modelobject waarvan de verklaarde variantie berekend moet worden.
# <!-- ## /TEKSTBLOK: ModellenVergelijken1.R -->
# 
# <!-- ## OPENBLOK: ModellenVergelijken2.R -->

# In[ ]:


# Stel het regressiemodel op met alleen Geslacht als predictor
Model_1 <- lm(Eindcijfer_MS ~ Geslacht, 
              Studenten_Methoden_Statistiek)

# Stel het regressiemodel op met Geslacht, Eindexamencijfer_Wiskunde en Aantal_Hoorcolleges als predictors
Model_2 <- lm(Eindcijfer_MS ~ Geslacht + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges,
              Studenten_Methoden_Statistiek)

# Voer de F-toets uit om beide modellen te vergelijken
anova(Model_1, Model_2)

# Bereken verklaarde variantie (%) van model 1
100*summary(Model_1)$r.squared

# Bereken verklaarde variantie (%) van model 2
100*summary(Model_2)$r.squared


# <!-- ## /OPENBLOK: ModellenVergelijken2.R -->
# 
# <!-- ## CLOSEDBLOK: ModellenVergelijken3.R -->

# In[ ]:


# Stel het regressiemodel op met alleen Geslacht als predictor
Model_1 <- lm(Eindcijfer_MS ~ Geslacht, 
              Studenten_Methoden_Statistiek)

# Stel het regressiemodel op met Geslacht, Eindexamencijfer_Wiskunde en Aantal_Hoorcolleges als predictors
Model_2 <- lm(Eindcijfer_MS ~ Geslacht + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges,
              Studenten_Methoden_Statistiek)

# Voer de F-toets uit om beide modellen te vergelijken
Vergelijking <- anova(Model_1, Model_2)

# Verklaarde variantie model 1
R2_model1 <- 100*summary(Model_1)$r.squared

# Verklaarde variantie model 2
R2_model2 <- 100*summary(Model_2)$r.squared


# <!-- ## /CLOSEDBLOK: ModellenVergelijken3.R -->
# 
# <!-- ## TEKSTBLOK: ModellenVergelijken4.R -->
# De F-toets toont aan dat er een significant verschil is in verklaarde variantie tussen beide modellen, *F*(`r Round_and_format_0decimals(Vergelijking[2,1])`,`r Round_and_format_0decimals(Vergelijking[2,3])`) = `r Round_and_format(Vergelijking[2,5])`, *p* < 0,0001. Het regressiemodel met alleen Geslacht als predictor verklaart slechts `r Round_and_format(R2_model1)`% van de variantie in het eindcijfer Methoden & Statistiek en het regressiemodel met drie predictoren verklaart `r Round_and_format(R2_model2)`% van de variantie. Het verschil in verklaarde variantie is `r Round_and_format(R2_model2 - R2_model1)`%. Het model met het geslacht, eindexamencijfer Wiskunde en aantal gevolgde hoorcolleges van een student als predictors verklaart dus significant meer variantie dan het model met alleen het geslacht van een student als predictor.
# <!-- ## /TEKSTBLOK: ModellenVergelijken4.R -->
# 
# # Uitvoering bootstrappen
# 
# Aangezien aan de assumpties van normaliteit en homoskedasticiteit is voldaan, hoeft er geen bootstrapping plaats te vinden. De methode wordt echter toch geïllustreerd voor de onderzoeksvraag in deze casus. 
# 
# <!-- ## OPENBLOK: Bootstrap1.R -->

# In[ ]:


# Laad het package car in
library(car)

# Zet een seed zodat bij herhaling dezelfde resultaten uit de bootstrap komen
set.seed(12345)

# Voer de multipele lineaire regressie uit
Regressiemodel <- lm(Eindcijfer_MS ~ Geslacht + Eindexamencijfer_Wiskunde + Aantal_Hoorcolleges,
                     Studenten_Methoden_Statistiek)

# Voer de bootstrap uit voor het regressiemodel
Bootstrap_resultaat <- Boot(Regressiemodel, R = 10000)

# Presenteer de gebootstrapte standaardfouten van de regressiecoëfficiënten
summary(Bootstrap_resultaat)

# Presenteer de 95%-betrouwbaarheidsintervallen van de regressiecoëfficiënten
confint(Bootstrap_resultaat, type = "bca")


# <!-- ## /OPENBLOK: Bootstrap1.R -->
# 
# <!-- ## TEKSTBLOK: Bootstrap2.R -->
# De resultaten van de bootstrap bevatten de originale waarde van de regressiecoëfficiënten (`original`), het verschil met de schatting van de regressiecoëfficiënt op basis van het gemiddelde van alle bootstrapwaarden (`bootBias`), de standaardfout van de regressiecoëfficiënt op basis van de bootstrap (`bootSE`) en de mediaan van alle bootstrapwaarden voor de regressiecoëfficiënt (`bootMed`). Van deze resultaten is de standaardfout het meest relevant omdat die incorrect is als de assumptie van normaliteit of homoskedasticiteit is geschonden.
# <!-- ## /TEKSTBLOK: Bootstrap2.R -->
# 
# De 95%-betrouwbaarheidsintervallen van de regressiecoëfficiënten op basis van de bootstrap zijn ook weergegeven. Op basis van de 95%-betrouwbaarheidsintervallen kan de significantie van de regressiecoëfficiënten bepaald worden[^8]. Als 0 in het interval zit, is de regressiecoëfficiënt niet significant verschillend van 0. Als 0 niet in het interval zit, is de regressiecoëfficiënt wel significant verschillend van 0 en kan de nulhypothese voor die regressiecoëfficiënt verworpen worden. De resultaten van de significantietoetsen op basis van de bootstrap komen overeen met de t-toetsen van het regressiemodel: de regressiecoëfficiënt van de variabele Geslacht is niet significant en de overige regressiecoëfficiënten wel.
# 
# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage1.R -->
# Een *multipele lineaire regressie* is uitgevoerd om de vraag te beantwoorden of er een relatie is tussen het aantal gevolgde hoorcolleges en het eindcijfer van het vak Methoden & Statistiek van de bachelor Onderwijskunde rekening houdend met het eindexamencijfer Wiskunde van studenten en man-vrouw verschillen. Uit het toetsen van de assumpties van *multipele lineaire regressie* bleek dat er aan alle assumpties is voldaan. De resultaten van de *multipele lineaire regressie* zijn te vinden in Tabel 1. De F-toets voor het regressiemodel laat zien dat het opgestelde regressiemodel minimaal één coëfficiënt heeft die significant verschilt van nul, *F*(`r Round_and_format_0decimals(F_toets[2])`,`r Round_and_format_0decimals(F_toets[3])`) = `r Round_and_format(F_toets[1])`, *p* < 0,0001. Het eindexamencijfer Wiskunde (*&beta;* = `r Round_and_format(Reg$coefficients[3,1])`, *t* = `r Round_and_format(Reg$coefficients[3,3])`, *p* < 0,01) en het aantal gevolgde hoorcolleges (*&beta;* = `r Round_and_format(Reg$coefficients[4,1])`, *t* = `r Round_and_format(Reg$coefficients[4,3])`, *p* < 0,0001) zijn significante predictors van het eindcijfer voor het vak, maar het geslacht van de student is dit niet (*&beta;* = `r Round_and_format(Reg$coefficients[2,1])`, *t* = `r Round_and_format(Reg$coefficients[2,3])`, *p* = `r Round_and_format(Reg$coefficients[2,4])`). Een toename van het eindexamencijfer Wiskunde leidt tot een toename van het voorspelde eindcijfer voor het vak van `r Round_and_format(Reg$coefficients[3,1])` en het volgen van één extra hoorcollege tot een toename in het voorspelde eindcijfer van `r Round_and_format(Reg$coefficients[4,1])`. De gestandaardiseerde coëfficiënten laten zien dat het aantal gevolgde hoorcolleges het sterkst gerelateerd is aan het eindcijfer. De docent van het vak Methoden & Statistiek kan hieruit concluderen dat er geen man-vrouw verschillen zijn, dat studenten met een hoger eindexamencijfer Wiskunde beter presteren voor zijn vak, maar bovenal dat het volgen van het hoorcolleges de grootste invloed heeft op het eindcijfer.
# <!-- ## /TEKSTBLOK: Rapportage1.R -->
# 
# <!-- ## TEKSTBLOK: Rapportage2.R -->
# |                           | Coëfficiënt   | Standaard- fout | t | p-waarde | 95%-betrouwbaarheids- interval | Gestandaardiseerde coëfficiënt  | 
# | ------------------------- | ---------| ---------| ---------| ---------| ---------| ---------| 
# | Intercept                 | `r Round_and_format(Reg$coefficients[1,1])` |  `r Round_and_format(Reg$coefficients[1,2])` |  `r Round_and_format(Reg$coefficients[1,3])` |  `r Round_and_format(Reg$coefficients[1,4])`  |  `r Round_and_format(CI[1,1])` - `r Round_and_format(CI[1,2])`  | - |
# | Geslacht (vrouw)          | `r Round_and_format(Reg$coefficients[2,1])`0 |  `r Round_and_format(Reg$coefficients[2,2])` |  `r Round_and_format(Reg$coefficients[2,3])` |  `r Round_and_format(Reg$coefficients[2,4])` |  `r Round_and_format(CI[2,1])` - `r Round_and_format(CI[2,2])`  | `r Round_and_format(Coefficienten_std[1])`|
# | Eindexamencijfer_Wiskunde | `r Round_and_format(Reg$coefficients[3,1])` |  `r Round_and_format(Reg$coefficients[3,2])` |  `r Round_and_format(Reg$coefficients[3,3])` |  < 0,01* |  `r Round_and_format(CI[3,1])` - `r Round_and_format(CI[3,2])` | `r Round_and_format(Coefficienten_std[2])`|
# | Aantal_Hoorcolleges       | `r Round_and_format(Reg$coefficients[4,1])` |  `r Round_and_format(Reg$coefficients[4,2])` |  `r Round_and_format(Reg$coefficients[4,3])` |  < 0,0001* |  `r Round_and_format(CI[4,1])` - `r Round_and_format(CI[4,2])` | `r Round_and_format(Coefficienten_std[3])`|
# *Tabel 1. Regressiecoëfficiënten en bijbehorende standaardfouten, t-statistieken, p-waardes,  95%-betrouwbaarheidsintervallen en gestandaardiseerde coëfficiënten.*
# <!-- ## /TEKSTBLOK: Rapportage2.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Multiple Regression Analysis using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/multiple-regression-using-spss-statistics.php
# [^2]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 293-356.
# [^3]: Universiteit van Amsterdam (13 augustus 2016). *Outliers*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).  
# [^4]: Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$.
# [^5]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^6]: Universiteit van Amsterdam (7 juli 2014). *Lineariteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Lineariteit).  
# [^7]: Stat 501. *12.4 - Detecting Multicollinearity Using Variance Inflation Factors*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat501/lesson/12/12.4).
# [^8]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
