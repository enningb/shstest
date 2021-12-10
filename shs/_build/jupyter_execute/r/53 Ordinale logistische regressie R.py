#!/usr/bin/env python
# coding: utf-8
---
title: "Ordinale logistische regressie"
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


source(paste0(here::here(),"/01. Includes/data/53.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# Gebruik *ordinale logistische regressie* om te toetsen of een ordinale[^13] afhankelijke variabele voorspeld kan worden met twee of meer onafhankelijke variabelen (predictors) en om te toetsen of er een relatie is tussen een predictor en de afhankelijke variabele in aanwezigheid van andere predictors.[^1]

# # Onderwijscasus
# <div id = "casus">
# 
# De bacheloropleiding Industrieel Ontwerpen van een technische universiteit wordt afgesloten met een eindproject waarin studenten opgedane kennis gebruiken voor een praktijkopdracht. Deze praktijkopdracht wordt beoordeeld als onvoldoende, voldoende, goed of uitstekend. De coördinator van het eindproject is benieuwd of er verschillen zijn tussen studenten die voor de bachelor zijn toegelaten op basis van een vwo-vooropleiding of een propedeuse in het hbo. Zij wil tegelijkertijd rekening houden met de leeftijd en het gemiddelde cijfer in het eerste jaar, omdat ze verwacht dat deze factoren ook invloed hebben op de beoordeling van het eindproject. Als er een verschil tussen studenten met een hbo-p en vwo-vooropleiding blijkt te zijn, wil de coördinator uitzoeken wat dit verschil veroorzaakt en indien nodig het eindproject aanpassen.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is. Bij *ordinale logistische regressie* wordt er een hypothese opgesteld voor het complete model en hypotheses voor de individuele predictors.
# 
# Hypotheses regressiemodel:
# 
# *H~0~*: Geen enkele predictor van de predictors Gemiddeld_cijfer, Leeftijd en Vooropleiding is gerelateerd aan de afhankelijke variabele Beoordeling ($\beta_{1} = \beta_{2} = \beta_{3} = 0$).
# 
# *H~A~*: Ten minste een van de predictors Gemiddeld_cijfer, Leeftijd en Vooropleiding is gerelateerd aan de afhankelijke variabele Beoordeling (Ten minste één $\beta_{i} \neq 0, i = 1, 2, 3$).
# 
# Hypotheses individuele predictors (met als voorbeeld de predictor Gemiddeld_cijfer ):
# 
# *H~0~*: De predictor Gemiddeld_cijfer heeft geen voorspellende waarde voor de beoordeling van het eindproject in aanwezigheid van de andere predictors Leeftijd en Vooropleiding ($\beta = 0$).
# 
# *H~A~*: De predictor Gemiddeld_cijfer heeft voorspellende waarde voor de beoordeling van het eindproject in aanwezigheid van de andere predictors Leeftijd en Vooropleiding ($\beta \neq 0$).
# 
# </div>
# 
# # Ordinale logistische regressie
# 
# Het doel van *ordinale logistische regressie* is het voorspellen van een ordinale afhankelijke variabele (met meer dan twee categorieën) op basis van meerdere onafhankelijke variabelen, ook wel predictors genoemd.[^1] Bij [multipele lineaire regressie](28-Multipele-lineaire-regressie-R.html) wordt het voorspellen van een afhankelijke variabele gedaan met behulp van een regressievergelijking waarin de afhankelijke variabele een lineaire combinatie is van de predictors, i.e. 
# 
# $$ y_i = \beta_0 + \beta_1 * x_{1i} + \beta_2 * x_{2i} + e_i$$
# 
# met $y_i$ als afhankelijke variabele, $\beta_0$ als intercept, $x_{1i}$ en $x_{2i}$ als predictors, $\beta_{1}$ en $\beta_{2}$ als regressiecoefficiënten van predictors, $e_i$ als residu of error en $i$ als indicator van de deelnemer[^19] uit de steekproef. De intercept $\beta_0$ geeft de waarde van de afhankelijke variabele weer als alle predictors gelijk aan nul zijn. De regressiecoefficiënten $\beta_1$ en $\beta_2$ geven de relatie tussen de afhankelijke variabele en de predictor weer. De residu of error $e_i$ is het verschil tussen de geobserveerde waarde van de afhankelijke variabele en de voorspelde waarde op basis van het regressiemodel.[^21] 
# 
# Bij [multipele lineaire regressie](28-Multipele-lineaire-regressie-R.html) wordt een continue afhankelijke variabele voorspeld op basis van een aantal predictors. Daarnaast is er [logistische regressie](41-Logistische-regressie-R.html) waarbij de afhankelijke variabele binair is. Bij [logistische regressie](41-Logistische-regressie-R.html) wordt de kans op een van beide mogelijkheden van de binaire variabele voorspeld. Als de afhankelijke variabele Uitval in het eerste studiejaar bestaat uit de mogelijkheden Uitval en Geen Uitval, dan kan met [logistische regressie](41-Logistische-regressie-R.html) de kans op het uitvallen van de student voorspeld worden. Voor meer informatie, zie de bijbehorende [toetspagina](41-Logistische-regressie-R.html).
# 
# Ook als de afhankelijke variabele categorisch is en meer dan twee mogelijkheden bevat, is het mogelijk een vorm van regressie uit te voeren. De gebruikte techniek hangt dan echter af van het meetniveau van de afhankelijke variabele. Als het meetniveau nominaal[^14] is, is [multinomiale logistische regressie](47-Multinomiale-logistische-regressie-R.html) de juiste techniek. Een voorbeeld van een nominale afhankelijke variabele is het vervolg na een hbo bachelor met als mogelijkheden een hbo master, een wo master en direct aan het werk gaan. Als het meetniveau ordinaal[^13] is, dan is *ordinale logistische regressie* de juiste techniek. Bij *ordinale logistische regressie* wordt een ordinale afhankelijke variabele voorspeld op basis van een aantal predictors. Bij *ordinale logistische regressie* wordt er rekening gehouden met de volgorde in de mogelijkheden van de afhankelijke variabele. Technisch gezien wordt er voor elke mogelijkheid de kans voorspeld dat de deelnemer in in die mogelijkheid valt of in een mogelijkheid lager in de rangorde. Voor de huidige casus is er dus een regressievergelijking om de kans te voorspellen op een onvoldoende, een voldoende of lager (voldoende + onvoldoende) en een goed of lager (goed + voldoende + onvoldoende). Voor de hoogste mogelijkheid is er geen regressievergelijking, want de kans dat iemand in de hoogste mogelijkheid of lager valt is gelijk aan 1. Immers, een deelnemer valt altijd in één van de mogelijkheden en alle mogelijkheden zijn dan beschikbaar. In de huidige casus zou het gaan om de kans dat een student een uitstekend of lager, dus een uitstekend, goed, voldoende of onvoldoende behaald. Dit zijn alle mogelijke resultaten van het eindproject, dus is de kans altijd gelijk aan 1.[^20]
# 
# Voor de huidige casus worden de volgende drie regressievergelijkingen opgesteld:
# 
# $$ \log(\frac{P(B_i \leq Onvoldoende)}{P(B_i > Onvoldoende)})  = \beta_{0,1} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i} + e_{i,1}$$
# $$ \log(\frac{P(B_i \leq Voldoende)}{P(B_i > Voldoende)})  = \beta_{0,2} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i} + e_{i,2}$$
# 
# $$ \log(\frac{P(B_i \leq Goed)}{P(B_i > Goed)})  = \beta_{0,3} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i} + e_{i,3}$$
# 
# waarbij $P(B_i \leq Onvoldoende)$ de kans is dat de beoordeling $B_i$ van deelnemer $i$ gelijk of lager is dan een onvoelde (en waarbij de andere kansen op vergelijkbare wijze zijn weergegeven),  $\beta_{0,1}$ als intercept van de eerste vergelijking, $Vooropleiding_{i}$, $GemiddeldCijfer_{i}$ en $Leeftijd_{i}$ als predictors, $\beta_{1}$, $\beta_{2}$ en $\beta_{3}$ als regressiecoefficiënten van de predictors, $e_{i,1}$ als residu of error van de eerste vergelijking en $i$ als indicator van de deelnemer uit de steekproef. Dezelfde notatie geldt ook voor de tweede en derde vergelijking. Bij *ordinale logistische regressie* is het aantal vergelijkingen gelijk aan het aantal mogelijkheden van de ordinale afhankelijke variabele minus één (de hoogste mogelijkheid).[^20]
# 
# Bij *ordinale logistische regressie* wordt eerst getoetst of alle vergelijkingen met de predictors toegevoegd samen voor een betere voorspelling zorgen dan alle vergelijkingen met alleen een intercept. Als dit het geval is, dan worden de individuele predictors getoetst op hun significantie. Elke vergelijking heeft een eigen intercept, deze verschilt dus per vergelijking. De regressiecoëfficiënten van de predictors zijn echter aan elkaar gelijk. In elke vergelijking heeft de predictor dus hetzelfde effect op de afhankelijke variabele. Dit wordt de *proportional odds assumptie* genoemd en is specifiek voor deze techniek van *ordinale logistische regressie*. Er zijn ook andere manieren om een *ordinale logistische regressie* uit te voeren, maar deze techniek is de meest gangbare.
# 
# In onderstaande sectie wordt in meer details aan de hand van een aantal wiskundige formules uitgelegd hoe *ordinale logistische regressie* werkt. Zonder deze paragraaf te lezen is de toetspagina ook goed te begrijpen. De geïnteresseerde lezer kan hier wat meer begrip op doen over de achtergrond van *ordinale logistische regressie*.
# 
# ## De achtergrond van ordinale logistische regressie
# 
# Bij *ordinale logistische regressie* wordt een voorspelling gemaakt van de logaritme van de kans dat een deelnemer een observatie heeft die gelijk aan of lager dan een bepaalde mogelijkheid is gedeeld door de kans dat een deelnemer een observatie heeft die hoger dan een bepaalde mogelijkheid is. Wiskundig gezien is dit op te schrijven als
# 
# $$ \log(\frac{P(y_i \leq j)}{P(y_i > j)}) = \beta_{0,j} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i} + e_{i,j} $$
# 
# waarbij $y_i$ de observatie op de afhankelijke variabele $y$ voor deelnemer $i$ is, $j$ de mogelijkheid van de afhankelijke variabele is en $P()$ de kans aangeeft. De breuk van twee kansen wordt ook wel een odds genoemd, deze term wordt verderop in de toetspagina uitgewerkt in de sectie Individuele predictors toetsen en interpreteren met de Wald toets. Daarnaast wordt de kans dat een observatie gelijk aan kleiner is dan een bepaalde mogelijkheid een cumulatieve kans genoemd. Bij *ordinale logistische regressie* wordt dus de log-odds van de cumulatieve kans voorspeld met een regressievergelijking.[^20]
# 
# Voor elke mogelijkheid van de afhankelijke variabele behalve de hoogste mogelijkheid is er een regressievergelijking opgesteld. In de huidige casus zijn de regressievergelijkingen
# 
# $$ \log(\frac{P(B_i \leq Onvoldoende)}{P(B_i > Onvoldoende)})  = \beta_{0,1} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i} + e_{i,1}$$
# $$ \log(\frac{P(B_i \leq Voldoende)}{P(B_i > Voldoende)})  = \beta_{0,2} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i} + e_{i,2}$$
# 
# $$ \log(\frac{P(B_i \leq Goed)}{P(B_i > Goed)})  = \beta_{0,3} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i} + e_{i,3}$$
# 
# waarbij $P(B_i \leq Onvoldoende)$ de kans is dat de beoordeling $B_i$ van deelnemer $i$ gelijk of lager is dan een onvoelde (en waarbij de andere kansen op vergelijkbare wijze zijn weergegeven),  $\beta_{0,1}$ als intercept van de eerste vergelijking, $Vooropleiding_{i}$, $GemiddeldCijfer_{i}$ en $Leeftijd_{i}$ als predictors, $\beta_{1}$, $\beta_{2}$ en $\beta_{3}$ als regressiecoefficiënten van de predictors, $e_{i,1}$ als residu of error van de eerste vergelijking en $i$ als indicator van de deelnemer uit de steekproef. Dezelfde notatie geldt ook voor de tweede en derde vergelijking. In feite is er dus een [logistische regressie](41-Logistische-regressie-R.html)-vergelijking voor elke log-odds van de cumulatieve kans. De hoogste mogelijkheid heeft geen vergelijking omdat de cumulatieve kans daar gelijk is aan 1. Immers, de deelnemer heeft altijd een observatie die gelijk aan of lager is dan de hoogste mogelijkheid. Zoals eerder genoemd schrijft de *proportional odds assumptie* voor dat de regressiecoëfficiënten van de predictors voor elke vergelijking hetzelfde zijn. Bij elke cumulatieve kans heeft de predictor dus hetzelfde effect.
# 
# De regressievergelijking geeft niet direct een voorspelling van de cumulatievenkans op de mogelijkheid van de ordinale afhankelijke variabele, maar een voorspelling van de logaritme van de odds op de cumulatieve kans. De cumulatieve kans is getransformeerd met behulp van een logit-transformatie. Bij [multipele lineaire regressie](28-Multipele-lineaire-regressie-R.html) is er een directe lineaire relatie tussen de afhankelijke variabele en de predictors. Bij *ordinale logistische regressie* is er een lineaire relatie tussen de logit van de cumulatieve kans op de mogelijkheid en de predictors. De interesse gaat echter uit naar de kans op een bepaalde mogelijkheid van de ordinale afhankelijke variabele en niet naar de logit. Er is dus geen directe lineaire relatie tussen de kans op een mogelijkheid en de predictors. De logit transformatie is als het ware de intermediair die zorgt voor de lineaire relatie en wordt daarom ook wel een link-functie genoemd.[^20]
# 
# Op basis van de logits is het wel mogelijk om de cumulatieve kansen op de verschillende mogelijkheden en de 'gewone' kansen op de mogelijkheden van de ordinale afhankelijke variabele uit te rekenen. Voor een algemene *ordinale logistische regressie* met twee predictoren is de formule voor de cumulatieve kansen
# 
# $$ P(Y_i \leq j) = \frac{\exp( \beta_{0,j} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i})}{1 +  \exp( \beta_{0,j} + \beta_{1} * Vooropleiding_{i} + \beta_{2} * Gemiddeld Cijfer_{i} + \beta_{3} * Leeftijd_{i})} .$$
# 
# De kans op een bepaalde mogelijkheid kan berekend worden door twee cumulatieve kansen van elkaar af te trekken. De kans op de beoordeling goed is te vinden door de cumulatieve kans op een beoordeling voldoende af te trekken van de cumulatieve kans op de beoordeling goed, i.e.
# 
# $$ P(B_i = Goed) = P(B_i \leq Goed) - P(B_i \leq Voldoende) .$$
# Voor de laagste mogelijkheid is de cumulatieve kans gelijk aan de 'gewone' kans zelf. Immers, er is niets lager dan de laagste mogelijkheid. De kans op een onvoldoende of lager is dus gelijk aan de kans op een onvoldoende, omdat er niets lager is dan een onvoldoende.
# 
# Hoewel de techniek van *ordinale logistische regressie* bedoeld is om de significantie van het model en de individuele regressiecoëfficiënten te toetsen, kunnen de berekende kansen ook gebruikt worden om een voorspelling of classificatie te maken van de mogelijkheid van de ordinale afhankelijke variabele die voor de deelnemer geobserveerd zal worden. De classificatie kan bijvoorbeeld de categorie met de hoogste voorspelde kans zijn. Op deze manier kan *ordinale logistische regressie* gebruikt worden om studenten te classificeren.
# 
# ## Maximum likelihood
# 
# Bij *multipele lineaire regressie* worden de regressiecoëfficiënten bepaald door de som van de gekwadrateerde residuën zo klein mogelijk te maken. Deze methode heet *ordinary least squares* (OLS) en zorgt ervoor dat de voorspellingen van het regressiemodel zo dichtbij als mogelijk zitten bij de echte observaties. Voor meer informatie, zie de [toetspagina](28-Multipele-lineaire-regressie-R.html). Bij *ordinale logistische regressie* wordt ook geprobeerd om de voorspellingen van het regressiemodel zo dichtbij de observaties te krijgen als mogelijk, maar er wordt een andere methode gebruikt. Deze methode heet *maximum likelihood* schatting en heeft als gevolg dat er ook andere statistische toetsen gebruikt worden. Om modellen te vergelijken wordt bij *ordinale logistische regressie* de *likelihood ratio toets* gebruikt in plaats van de F-toets. Om regressiecoëfficiënten te toetsen, wordt de *Wald toets* gebruikt in plaats van de t-toets.[^2]<sup>,</sup>[^20]

# ## Likelihood ratio toets voor significantie regressiemodel
# 
# Bij *maximum likelihood* schatting laat de likelihood van het model zien hoe dichtbij de voorspellingen van het model bij de observaties zitten. De likelihood is hoger voor een model waarin de voorspellingen dichterbij de observaties zitten. Op basis van de likelihood wordt het gehele regressiemodel statistisch getoetst en kunnen (geneste) modellen onderling vergeleken worden.
# 
# De eerste vraag bij *ordinale logistische regressie* is of het model betere voorspellingen geeft dan een model zonder predictors. Daarom wordt het voorgestelde model vergeleken met een interceptmodel, een model waarin er geen predictors zijn en dus alleen de intercept gebruikt wordt om voorspellingen te maken. De verwachting is dat het voorgestelde model betere voorspellingen genereert en dus een hogere likelihood heeft. De significantie van dit verschil wordt getoetst met een *likelihood ratio* toets. De getoetste nulhypothese is dat de regressiecoëfficiënten van alle predictors gelijk aan nul zijn, wat wil zeggen dat de predictors niet zorgen voor betere voorspellingen. De getoetste alternatieve hypothese is dat minimaal een van de regressiecoëfficiënten van de predictors niet gelijk aan nul is, wat wil zeggen dat het model betere voorspellingen genereert. Als het verschil tussen beide modellen significant is, kunnen de individuele predictors getoetst worden. Als de toename niet significant is, is de analyse afgelopen en is de conclusie dat het voorgestelde model niet in staat is om de afhankelijke variabele beter te voorspellen dan een model zonder predictors.[^2]<sup>,</sup>[^20]
# 
# De *likelihood ratio* toets kan ook gebruikt worden om verschillende regressiemodellen onderling te vergelijken. Hierbij wordt getoetst of er een verschil is tussen de likelihood (de kwaliteit van het model) van beide modellen. Er kan bijvoorbeeld in eerste instantie een model met twee predictors getoetst worden om vervolgens te toetsen of de voorspellingen van het regressiemodel nog beter worden met twee extra predictors. Het verschil in likelihood tussen het model met twee en vier predictors wordt dan getoetst met een chi-kwadraat toets. Hierbij is de nulhypothese dat de extra toegevoegde predictors een regressiecoëfficiënt van nul hebben en de alternatieve hypothese dat minimaal een van de regressiecoëfficiënten van de extra predictors niet gelijk aan nul is. Een eis voor deze toets is dat beide modellen genest zijn. Bij geneste modellen is het ene model te schrijven als een versie van het andere model na het verwijderen van een aantal predictors. In deze casus zou er een model opgesteld kunnen worden waarin alleen de variabele Vooropleiding een predictor is van Beoordeling en een model waarin de de variabelen Vooropleiding, Gemiddeld_cijfer en Leeftijd predictors zijn van Beoordeling. Dit zijn geneste modellen, omdat het eerste model (alleen Vooropleiding als predictor) een versie is van het tweede model na het verwijderen van de predictors Gemiddeld_cijfer en Leeftijd. Het model waarbij de predictors verwijderd zijn, wordt als het ware gereduceerd. Daarom wordt dit het gereduceerde model genoemd. Het model waar de predictors niet verwijderd zijn, wordt het uitgebreide model genoemd. Om modellen met een *likelihood ratio* te vergelijken, moeten ze dus genest zijn. In andere woorden, het verschil tussen beide regressiemodellen moet dus toe te wijzen zijn aan het toevoegen of verwijderen van een of meerdere predictors.[^2]<sup>,</sup>[^20]
# 
# Bij *ordinale logistische regressie* is de effectmaat gebaseerd op een vergelijking van de likelihood van het voorgestelde model ten opzichte van de likelihood van het interceptmodel. Een veelgebruikte versie hiervan is Nagelkerke's $R^2$ ($R_N^2$) welke waardes aanneemt tussen 0 en 1. Let op dat Nagelkerke's $R^2$ niet geïnterpreteerd kan worden als verklaarde variantie (zoals $R^2$ bij *multipele lineaire regressie*). Er kan dus niet gezegd worden dat een bepaald percentage van de variantie verklaard wordt door het model. Daarom wordt er een algemenere term gebruikt om Nagelkerke's $R^2$ te duiden. De juiste term hiervoor is de verklaarde variatie of model fit.[^2]
# 
# ## Individuele predictors toetsen en interpreteren met de Wald toets
# 
# Als de *likelihood ratio* toets aantoont dat het regressiemodel betere voorspellingen geeft dan het interceptmodel, kunnen de predictors getoetst worden. De regressiecoefficiënten van de predictors en de intercept worden getoetst met een *Wald toets* waarbij de nulhypothese is dat de coefficiënt gelijk aan nul is ($\beta = 0$) en de (tweezijdige) alternatieve hypothese dat de coefficiënt niet gelijk aan nul is ($\beta \neq 0$). Er kan ook een eenzijdige alternatieve hypothese opgesteld worden, bijvoorbeeld als er de verwachting is dat de coefficiënt positief of negatief is. De *Wald-toets* toont in feite aan of er wel of geen relatie is tussen de predictor en afhankelijke variabele in de aanwezigheid van de andere predictoren van het regressiemodel. Bij de *Wald-toets* is de gebruikte toetsstatistiek de z-score.[^2]
# 
# De regressiecoëfficiënten bij *ordinale logistische regressie* worden geïnterpreteerd in termen van odds ratios. Odds is een Engelse term en is een variant van kans, namelijk de kans op een gebeurtenis gedeeld door 1 minus de kans op een gebeurtenis ($\frac{\pi}{1 - \pi}$). Bij een kans van  2/3 is de odds $\frac{2/3}{1 - 2/3} = \frac{2/3}{1/3} = 2$. Bij het opgooien van een muntje is de kans op zowel kop als munt 0,5. De odds van zowel kop of munt zijn dus $\frac{1/2}{1 - 1/2} = \frac{1/2}{1/2} = 1$. De odds kan echter ook uitgedrukt worden als een ratio van de kansen van twee gebeurtenissen, namelijk de kans op de ene gebeurtenis gedeeld door de kans op de andere gebeurtenis. In de huidige casus is er bijvoorbeeld de odds van de het behalen van een voldoende of lager ten, wat een ratio is van de kans op het behalen van een voldoende of lager en de kans op het behalen van een beoordeling die hoger is dan voldoende.
# 
# Een odds ratio is een ratio van twee odds. In de huidige casus wordt bijvoorbeeld onderzocht of de vooropleiding gerelateerd is aan de beoordeling van het eindproject. Stel dat de odds op een voldoende of lager 3 is voor de vooropleiding hbo-p en 2 voor de vooropleiding vwo. Dan is de odds ratio voor de variabele Vooropleiding 3/2 = 1,5. De odds op een voldoende of lager zijn dus 1,5 keer zo hoog voor een hbo-p vooropleiding ten opzichte van een vwo vooropleiding. Dit is de manier om de odds ratio te interpreteren.[^2] Bij *ordinale logistische regressie* is het van belang op te letten hoe de afhankelijke variabele geordend is, omdat dit de interpretatie van de odds bepaald. In de huidige casus is de afhankelijke variabele geordend als onvoldoende, voldoende, goed en uitstekend. Een odds ratio groter dan 1 betekent in dat geval dat de eindbeoordeling minder goed zal zijn. De odds ratio voor de predictor Vooropleiding van 1,5 houdt bijvoorbeeld in dat studenten met een hbo-p vooropleiding een 1,5 keer zo hoge odds op een voldoende of lager hebben dan studenten met een vwo vooropleiding. Een hogere odds voor een voldoende of lager betekent een hogere kans op een voldoende of lager en dus een lagere kans op een beoordeling die hoger dan een voldoende is. De eindbeoordeling is dus waarschijnlijk minder hoog voor studenten met een hbo-p vooropleidingop basis van de gevonden odds ratio.
# 
# Regressiecoëfficiënten zijn gelijk aan de logaritme van de odds ratio van de bijbehorende predictor. De odds ratio zelf wordt berekend door de exponent te nemen van de regressiecoëfficiënt. Let bij het interpreteren van odds ratios op dat de betekenis verschillend is voor continue en categorische predictors. In beide gevallen geldt echter dat een toename van één eenheid van de predictor resulteert in een odds die vermenigvuldigd wordt met de exponent van de regressiecoëfficiënt $\exp(\beta)$. De odds zijn dus $\exp(\beta)$ keer zo hoog na een toename van één eenheid van de predictor. Een voorbeeld van de interpretatie van regressiecoëfficiënten is handig voor de huidige casus. Voor elke predictor is een fictieve waarde van de regressiecoëfficiënt gemaakt die geïnterpreteerd wordt. De intercept wordt bij *ordinale logistische regressie* meestal niet geïnterpreteerd.[^2]
# 
# * Vooropleiding ($\beta_{1,1} = 0,405$): De regressiecoefficiënt van de variabele Vooropleiding is gelijk aan 0,405. De odds ratio van deze predictor is dus $exp(0,405) = 1,5$. De variabele Vooropleiding is zo opgesteld dat het een hbo-p vooropleiding vergelijkt ten opzichte van de vwo vooropleiding als referentiecategorie. Als de overige predictors gelijkblijven is de odds van het behalen van een bepaalde beoordeling of een beoordeling die lager is 1,5 keer zo hoog voor studenten met een hbo-p vooropleiding ten opzichte van studenten met een vwo vooropleiding. Studenten met een hbo-p vooropleiding hebben dus relatief gezien lagere beoordelingen dan studenten met een vwo vooropleiding. In een regressiemodel worden categorische variabelen omgezet in binaire variabelen met de waarden 0 en 1, omdat dat nodig is om het model te fitten. De variabele Vooropleiding zou bijvoorbeeld gecodeerd kunnen worden met een 1 voor een hbo-p vooropleiding en een 0 voor een vwo vooropleiding. Let goed op hoe de categorieën gecodeerd zijn, i.e. welke categorie de waarde 1 en 0 hebben. Dit bepaalt namelijk de interpretatie.
# * Gemiddeld_cijfer ($\beta = -0,105$): De coëfficient van de variabele Gemiddeld_cijfer is gelijk aan -0,105. De odds ratio van deze predictor is dus $exp(-0,105) = 0,9$. Als de overige predictors gelijkblijven is de odds van het behalen van een bepaalde beoordeling of een beoordeling die lager is 0,9 keer zo hoog bij een toename van het gemiddeld cijfer met één punt. De odds het behalen van een bepaalde beoordeling of een beoordeling die lager is, is dus eigenlijk 1.11 (1 / 0,9) keer zo laag bij een toename van één punt in het gemiddelde cijfer. Dit betekent dus dat studenten met een hoger gemiddeld cijfer relatief gezien een hogere beoordeling voor hun eindproject ontvangen.
# * Leeftijd ($\beta = 0,182$): De coëfficient van de variabele Leeftijd is gelijk aan 0,182. De odds ratio van deze predictor is dus $exp(0,182) = 1,2$. Als de overige predictors gelijkblijven is de odds van het behalen van een bepaalde beoordeling of een beoordeling die lager is 1,2 keer zo hoog bij een toename van Leeftijd met één jaar. Dit betekent dus dat oudere studenten relatief gezien een lagere beoordeling voor hun eindproject ontvangen.
# 
# ## Predictors vergelijkingen door standaardisatie
# 
# Op basis van de regressievergelijking en de Wald-toetsen kan bepaald worden of predictors gerelateerd zijn aan de afhankelijke variabele en wat de invloed van een verandering van de predictor is op de afhankelijke variabele. Een andere relevante vraag is welke predictor het sterkst gerelateerd is aan de afhankelijke variabele. Op basis van de regressiecoëfficienten kan dit niet bepaald worden, omdat de schaal van de predictors verschilt. Het gemiddelde cijfer varieert tussen de 1 en 10 (waarschijnlijk zijn de meeste waarden hoger dan 5,5), de leeftijd van studenten zal waarschijnlijk tussen de 18 en 24 liggen met wat uitschieters daaromheen en de variabele Vooropleiding is gelijk aan een 1 of een 0. 
# 
# Standaardiseer de predictors om de predictors onderling te kunnen vergelijken. Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$. Als het regressiemodel opnieuw geschat wordt met gestandaardiseerde variabelen, kunnen de coëfficiënten onderling vergeleken worden op basis van hun grootte. Een grotere (absolute waarde van de) coëfficient betekent een sterkere relatie met de afhankelijke variabele. De coëfficiënt is nu te interpreteren in termen van standaardafwijkingen. Een toename van één eenheid van de predictor staat voor een toename van een standaardafwijking van deze predictor. Deze toename van één standaardafwijking resulteert in een verandering van de odds die gelijk is aan de exponent van de bijbehorende (gestandaardiseerde) regressiecoëfficiënt.[^2]<sup>,</sup>[^11] De predictor met de hoogste absolute waarde van de regressiecoëfficiënt is het sterkst gerelateerd aan de afhankelijke variabele.
# 
# ## Voorspellen op basis van het regressiemodel
# 
# Een regressiemodel maakt het mogelijk om een afhankelijke variabele te voorspellen op basis van een aantal predictors. Als van een student bekend is wat zijn gemiddelde cijfer en zijn leeftijd is en of hij een hbo-p of vwo vooropleiding heeft, kan een voorspelling gemaakt worden van de kans op elke beoordeling van het eindproject (onvoldoende, voldoende, goed en uitstekend). Voor alle deelnemers in de steekproef kunnen deze voorspellingen gemaakt worden. De regressievergelijking maakt het echter ook mogelijk om voor nieuwe deelnemers voorspellingen te maken, waar bijvoorbeeld ook *machine learning* technieken voor gebruikt kunnen worden. Dit wordt een out-of-sample voorspelling genoemd omdat de nieuwe deelnemer niet in de steekproef zit waarop het regressiemodel wordt geschat. Als de coördinator van het eindproject een jaar later de beoordelingen van de nieuwe studenten van de opleiding Industrieel Ontwerpen wilt voorspellen, kan hij de regressievergelijking van het jaar ervoor gebruiken. Een out-of-sample voorspelling geeft vaak een goede indicatie van de kwaliteit van het regressiemodel, omdat de nieuwe deelnemer niet gebruikt zijn om het model te schatten. Als het doel is om het regressiemodel te gebruiken voor het voorspellen van nieuwe deelnemers, dan is de kwaliteit van de out-of-sample voorspellingen van belang.[^2]
# 
# Bij *ordinale logistische regressie* wordt de logaritme van de odds dat de observatie van een deelnemer gelijk aan of kleiner is dan een bepaalde mogelijkheid van de afhankelijke variabele. In de huidige casus gaat het om de odds op een beoordeling die gelijk is aan of lager is dan een onvoldoende, voldoende of goed. Deze odds kunnen echter ook omgezet worden in de kans op een bepaalde gebeurtenis. In de huidige casus gaat het dan om de kans op de beoordeling onvoldoende, voldoende, goed of uitstekend. Een kans kan waarden aannemen tussen 0 en 1. De geobserveerde waarde is echter een mogelijkheid, in de huidige casus de gegeven beoordeling. Het voorspellen van een categorische variabele wordt classificatie genoemd en is ook mogelijk met *ordinale logistische regressie*. Voor elke mogelijkheid van de afhankelijke variabele is een kans voorspeld en de mogelijkheid met de hoogste voorspelde kans is dan het meest waarschijnlijk. Met het regressiemodel kan er geclassificeerd worden door de categorie met de hoogste voorspelde kans toe te wijzen aan die deelnemer. Als een deelnemer een kans van 0,2 heeft op een onvoldoende, een kans van 0,4 op een voldoende, een kans van 0,3 op een goed en een kans van 0,1 op uitstekend, dan is de juiste classificatie dat de deelnemer een voldoende krijgt.[^12]
# 
# Op basis van de classificaties en de geobserveerde waarden kan een classificatietabel gemaakt worden. Hierin worden de geobserveerde waarden voor de variabele uitval uitgezet tegenover de geclassificeerde waarden. Een voorbeeld van een classificatietabel voor de huidige casus is te zien in Tabel 1. In de cel linksboven is te zien dat er 70 studenten zijn waarvoor voorspeld is dat ze een onvoldoende beoordeling ontvangen en die dat ook daadwerkelijk als beoordeling hebben gekregen. Deze studenten zijn dus correct geclassificeerd. Daarnaast zijn er 60 studenten met een voldoende, 100 studenten met een goed en 80 studenten met een uitstekend correct geclassificeerd. Deze cellen vormen samen een schuine lijn van linksboven naar rechtsonder in de tabel, deze lijn wordt de diagonaal genoemd. Alle cellen op de diagonaal bevatten de deelnemers die correct geclassificeerd zijn. De overige cellen liggen niet op de diagonaal en bevatten de deelnemers die incorrect geclassificeerd zijn. Zo bevat de cel linksonder 20 studenten waarvoor voorspeld is dat ze een onvoldoende beoordeling ontvangen, maar die in werkelijkheid de beoordeling uitstekend gekregen hebben. 
# 
# Op basis van de classificatietabel kan berekend worden welk percentage van de deelnemers correct geclassificeerd is. Dit wordt de accuraatheid genoemd en is te berekenen door het aantal correct geclassificeerde deelnemers te delen door het totaal aantal deelnemers. In de huidige casus is de accuraatheid $\frac{70 + 60 + 100 + 80}{680} = 0,456$, dus 45,6% van de deelnemers is correct geclassificeerd.[^12]
# 
# ||                      | Voorspelling    | | | |
# |-------------| -------------------- | -------------| ------------| ------------| ------------| 
# ||                            | Onvoldoende | Voldoende | Goed | Uitstekend |
# |**Observaties**| Onvoldoende  | **70**         | 40        | 20  | 30 |
# |               | Voldoende    | 10         | **60**        | 20  | 80 |
# |               | Goed         | 10         | 30        | **100** | 60 |
# |               | Uitstekend   | 20         | 40        | 10 | **80** |
# 
# *Tabel 1. Classificatietabel van de observaties en classificaties van de beoordelingen van het eindproject van de bacheloropleiding Industrieel Ontwerpen.*
# 
# # Uitleg assumpties
# 
# Om een valide resultaat te vinden met *ordinale logistische regressie*, dient er aan een aantal assumpties voldaan te worden.[^1]<sup>,</sup>[^2] In deze sectie worden de assumpties allen toegelicht en worden de opties bij het niet voldoen aan de assumptie weergegeven. Verderop in de toetspagina worden de assumpties getoetst met de dataset van de onderwijscasus.
# 
# ## Outliers
# 
# Voordat gestart kan worden met *ordinale logistische regressie*, moet de data gescreend worden op de aanwezigheid van outliers. Outliers (uitbijters) zijn observaties die sterk afwijken van de overige observaties. Univariate outliers zijn observaties die afwijken voor één specifieke variabele, zoals een student die twintig jaar over zijn studie heeft gedaan. Multivariate outliers zijn observaties die afwijken door de combinatie van meerdere variabelen, zoals een persoon van 18 jaar met een inkomen van €100.000,-. De leeftijd van 18 jaar is geen outlier op zichzelf en een inkomen van €100.000,- is dat ook niet. Echter, de combinatie van beide zorgt ervoor dat de observatie vrij onwaarschijnlijk is.[^9]
# 
# Na het vinden van een outlier is de volgende stap om een goede oplossing voor te outlier te bedenken. Het is van belang hier goed over na te denken en niet zomaar een outlier te verwijderen met als enige argument dat het een outlier is. In het algemeen kan er onderscheid gemaakt worden tussen onmogelijke en onwaarschijnlijke outliers.[^3] Een onmogelijke outlier is een observatie die technisch gezien niet kan kloppen, bijvoorbeeld een leeftijd van 1000 jaar, een negatief salaris of een man die zwanger is. Bij deze outliers is het een optie om de waarde te vervangen als er een overduidelijke fout bij het invoeren van de data is gemaakt. Een andere optie is de waarde te verwijderen. Een onwaarschijnlijke outlier is een observatie die technisch gezien wel kan, maar heel erg afwijkt van de overige observaties. De rijksten der aarde zijn in de stad of het dorp waar zij wonen qua vermogen waarschijnlijk een outlier. Maar het zijn bestaande personen dus het verwijderen van de observatie zou hier foutief zijn. Opties in deze situatie zijn om te overwegen de variabele(n) te transformeren, de outlier gewoon mee te nemen in de analyse of de analyse met en zonder de outlier uit te voeren en beide te rapporteren. Ook is het niet verboden om de outlier toch te verwijderen, maar het is in dat geval wel van belang dit transparant te rapporteren en op een goede wijze te beargumenteren.[^3]
# 
# Bij *ordinale logistische regressie* zijn er vier nuttige methoden om outliers te vinden.[^9]
# 
# ### Boxplots en standaardiseren
# 
# Begin voor de analyse met het screenen van de variabelen in de dataset op de aanwezigheid van univariate outliers. Voor continue variabelen bestaat deze screening uit het visualiseren van de variabele met een boxplot en het standaardiseren[^4] van de variabele. Als een observatie een gestandaardiseerde score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. In dat geval wijkt de observatie namelijk meer dan drie standaardafwijkingen af van het gemiddelde van de variabele. Gebruik zowel de boxplot als de standaardisering om outliers te vinden voor continue variabelen.[^3]
# 
# Bij categorische variabelen hebben boxplots en standaardisatie geen zin, omdat het geen variabelen met een continue schaal zijn. Bij categorische variabelen is het nuttig om een overzicht te maken van de bestaande categorieën en bijbehorende aantallen observaties en is het nuttig om te onderzoeken of elke observatie slechts in één categorie past. Doe dit met behulp van tabellen.
# 
# ### Gestandaardiseerde residuën
# 
# De residuën van een logistisch regressiemodel zijn de verschillen tussen de observaties van de afhankelijke variabele en de voorspelde kans. Bij *ordinale logistische regressie* zijn er echter meer dan twee mogelijkheden voor de afhankelijke variabele en worden er meerdere kansen berekend. Er wordt daarom gebruik gemaakt van de odds van cumulatieve kansen. Het is daarom ingewikkeld om de residuën te berekenen en vervolgens de gestandaardiseerde residuën te onderzoeken.
# 
# Een oplossing hiervoor is het uitvoeren van een [logistische regressie](41-Logistische-regressie-R.html) voor elke cumulatieve kans en voor elke cumulatieve kans de gestandaardiseerde residuën te onderzoeken. In de huidige casus zijn er drie cumulatieve kansen: kleiner dan of gelijk aan onvoldoende, kleiner dan of gelijk aan voldoende en kleiner dan of gelijk aan goed. Voer voor elke combinatie een logistisch regressiemodel uit en onderzoek de gestandaardiseerde residuën. Als er een groot verschil is tussen observatie en voorspelling, zou dat kunnen wijzen op een univariate outlier. Bekijk met een grafiek of er outliers zijn. Als het gestandaardiseerde residu een score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. Op deze manier kunnen outliers bij het regressiemodel kunnen worden geïdentificeerd.[^9]
# 
# ### Mahalanobis afstand
# 
# Multivariate outliers zijn deelnemers met een combinatie van observaties op verschillende variabelen die erg afwijken van de overige deelnemers. Deze multivariate outliers kunnen geïdentificeerd worden met de Mahalanobis afstand. De Mahalanobis afstand is een maat die aangeeft in hoeverre de observaties van een deelnemer voor alle predictors afwijken van de gemiddeldes van de predictors. Het is een maat voor een afstand tussen twee punten als meerdere variabelen worden gebruikt. Bereken de Mahalanobis afstand voor elke deelnemer en vergelijk deze met de criteriumwaarde. De criteriumwaarde wordt bepaald op basis van de chi-kwadraat score bij een aantal vrijheidsgraden dat gelijk is aan het aantal predictors en een significantieniveau van 0,001 (of een zelf gekozen significantieniveau). In de code wordt toegelicht hoe de criteriumwaarde bepaald kan worden.[^9]
# 
# ### Cook's afstand
# 
# De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van de andere deelnemers wat betreft de waardes van de predictorvariabelen. Een andere manier om multivariate outliers te vinden is te bepalen hoeveel invloed een deelnemer heeft op de schattingen van het regressiemodel. Als de uitkomsten van het regressiemodel sterk veranderen als een bepaalde deelnemer weggelaten wordt uit de dataset, dan is deze deelnemer invloedrijk. Met behulp van Cook's afstand worden invloedrijke deelnemers ontdekt. Als Cook's afstand groter dan 1 is, wordt de deelnemer beschouwd als invloedrijk.
# 
# Hoewel de Mahalanobis afstand en Cook's afstand beide multivariate outliers identificeren, verschillen ze in het soort outlier waarop de focus ligt. Bij de Mahalanobis afstand worden afwijkende datapunten gevonden en bij Cook's distance invloedrijke datapunten. Het is echter niet zo dat een afwijkend datapunt ook tegelijkertijd invloedrijk is en dat een invloedrijk datapunt ook afwijkt. Een afwijkend datapunt kan ondanks zijn afwijking van de de overige datapunten toch op een juiste manier voorspeld worden. En een invloedrijk datapunt hoeft niet per se sterk af te wijken van de overige datapunten wat betreft de waardes voor de predictorvariabelen. Houdt hier rekening mee bij het bepalen hoe om te gaan met de gevonden outlier(s).[^9]
# 
# Cook's afstand wordt berekend op basis van de residuën van het regressiemodel. Bij *ordinale logistische regressie* zijn er meer dan twee mogelijkheden voor de afhankelijke variabele en worden er meerdere kansen berekend. Er wordt daarom gebruik gemaakt van de odds van cumulatieve kansen. Het is daarom ingewikkeld om de residuën te berekenen en vervolgens de gestandaardiseerde residuën te onderzoeken. Een oplossing hiervoor is het uitvoeren van een [logistische regressie](41-Logistische-regressie-R.html) voor elke cumulatieve kans en voor elke cumulatieve kans de gestandaardiseerde residuën te onderzoeken. In de huidige casus zijn er drie cumulatieve kansen: kleiner dan of gelijk aan onvoldoende, kleiner dan of gelijk aan voldoende en kleiner dan of gelijk aan goed. Voer voor elke combinatie een logistisch regressiemodel uit en onderzoek de Cook's afstanden. Als Cook's afstand groter dan 1 is, wordt de deelnemer beschouwd als invloedrijk en zou er een outlier kunnen zijn.
# 
# ## Lineariteit: Box-Tidwell
# 
# Bij *ordinale logistische regressie* is de regressievergelijking zo opgesteld dat er een lineaire relatie is tussen elke predictor en de logit van de cumulatieve kans op een mogelijkheid van de afhankelijke variabele. Een lineaire relatie houdt in dat de toename of afname van de (logit van de) cumulatieve kans als gevolg van de toename van de predictor constant is. In tegenstelling tot [multipele lineaire regressie](28-Multipele-lineaire-regressie-R.html) kan bij *ordinale logistische regressie* geen grafiek gemaakt worden om een lineaire relatie te onderzoeken. In plaats daarvan is er een statistische toets om te onderzoeken of er een lineaire relatie is tussen de predictor en de logit van de cumulatieve kans. Bij deze *Box-Tidwell test* wordt er voor elke continue predictor een extra term toegevoegd die bestaat uit het product van de predictor en de logaritme van de predictor. Voor de predictor Gemiddeld_cijfer zou dit dus betekenen dat er een extra variabele wordt (Gemiddeld_cijfer * ln[Gemiddeld_cijfer]). Voeg deze interactietermen voor alle continue predictors toe en toets of de regressiecoëfficiënten van deze interactietermen significant zijn. Als dit zo is, dan is er voor die predictor niet voldaan aan de assumptie van lineariteit. Een oplossing hiervoor is het transformeren[^5] van de variabele.[^6]
# 
# ## Multicollineariteit
# 
# Multicollineariteit houdt in dat er een hoge correlatie tussen twee of meerdere predictors is. Er is perfecte multicollineariteit als één predictor een lineaire combinatie is van een of meerdere andere predictors. In andere woorden, de predictor is precies te berekenen op basis van andere predictor(s). In dat geval kan de regressievergelijking niet wiskundig bepaald worden en werkt *ordinale logistische regressie* niet. Dit komt zeer weinig voor en is vaak makkelijk op te lossen door goed naar de variabelen die het veroorzaken te kijken en een variabele te transformeren of te verwijderen.[^9]
# 
# Bij een hoog niveau van multicollineariteit kan de regressievergelijking wel geschat worden, maar zijn de uitkomsten minder betrouwbaar. De standaardfouten van de regressiecoëfficiënten worden groter bij meer multicollineariteit en dit levert bij hoge multicollineariteit problemen op. Ook is het lastig om te ontdekken wat per predictor de bijdrage is aan de voorspellingen van de afhankelijke variabele, omdat bepaalde predictors sterk gecorreleerd zijn en overlappen in het deel van de variantie dat ze verklaren.[^9] 
# 
# Multicollineariteit wordt getoetst met de Variance Inflation Factor (VIF) die meet hoe sterk elke predictor gecorreleerd is met de andere predictors. Als de VIF van een predictor hoger dan 10 is, is er multicollineariteit voor die predictor.[^9]<sup>,</sup>[^7] Multicollineariteit kan opgelost worden door een van de predictors die het veroorzaakt te verwijderen uit het model. Een andere optie is een principale componenten analyse (PCA) uitvoeren op de predictoren zodat er een onderliggende variabele gecreëerd wordt (zie Field[^9] voor meer informatie).
# 
# ## Observaties per variabele
# 
# Bij *ordinale logistische regressie* is de afhankelijke variabele ordinaal wat betekent dat de variabele meer dan twee mogelijkheden heeft. Dit kan een probleem opleveren als er categorische predictors zijn. Voor elke categorie van een categorische predictor moeten er observaties zijn voor alle mogelijkheden van de afhankelijke variabele. Deze assumptie kan onderzocht worden door een kruistabel te maken voor de combinatie van elke categorische predictor en de afhankelijke variabele. Een voorbeeld van een dergelijke kruistabel is te zien in Tabel 2 voor de afhankelijke variabele Beoordeling en predictor Vooropleiding. In deze kruistabel is te zien dat er binnen de categorie hbo van de predictor Vooropleiding nul deelnemers zijn die een onvoldoende behalen. Deze categorie bevat dus een lege cel en voldoet niet aan de assumptie.[^2]<sup>,</sup>[^6]
# 
# ||                      | Nominaal    | |
# |-------------| -------------------- | -------------| ------------| 
# |                |             | hbo      | wo |
# |**Beoordeling** | Onvoldoende | 0        | 10        |
# |                | Voldoende   | 60       | 80        |
# |                | Goed        | 80       | 50        |
# |                | Uitstekend  | 20       | 40        |
# 
# *Tabel 2. Kruistabel van de observaties voor de afhankelijke variabele Beoordeling en predictor Vooropleiding waarbij voor de categorie hbo niet alle waarden van de afhankelijke variabele aanwezig zijn.*
# 
# Daarnaast is het met een ordinale afhankelijke variabele mogelijk dat er een categorische predictor is die perfect de waarde van de afhankelijke variabele voorspelt. Een voorbeeld hiervan is te zien in Tabel 3, opnieuw voor de afhankelijke variabele Beoordeling en predictor Vooropleiding. De categorie Uitstekend bevat alleen studenten met een wo vooropleiding en de andere categorieën alleen studenten met een hbo vooropleiding. De predictor Vooropleiding voorspelt dus perfect of een student wel of niet een uitstekend als beoordeling krijgt. Dit fenomeen wordt *complete separation* genoemd en komt af en toe voor als er heel veel predictors aanwezig zijn en weinig observaties. Als dit gebeurt, dan werkt de *maximum likelihood* methode niet.[^6]
# 
# ||                      | Nominaal    | |
# |-------------| -------------------- | -------------| ------------| 
# |                |             | hbo      | wo |
# |**Beoordeling** | Onvoldoende | 20       | 0        |
# |                | Voldoende   | 50       | 0        |
# |                | Goed        | 70       | 0        |
# |                | Uitstekend  | 0        | 90        |
# 
# *Tabel 3. Kruistabel van de observaties voor de afhankelijke variabele Beoordeling en predictor Vooropleiding waarbij er sprake is van complete separation.*
# 
# Het gevolg van de assumptie voor observaties per variabele zijn dat er extreem hoge regressiecoëfficiënten en standaardfouten worden gevonden of dat de *maximum likelihood* methode niet werkt. Toets daarom deze assumptie door voor elke categorische predictor een kruistabel te maken met de afhankelijke variabele en onderzoek of er lege cellen zijn en of er *complete separation* plaatsvindt. Als er niet aan deze assumptie voldaan is, dan zijn er meerdere oplossingen mogelijk. De categorie die problemen geeft bij de categorische predictor kan verwijderd worden of worden samengevoegd met een andere categorie. Daarnaast kan de hele predictor verwijderd worden. Ten slotte is meer data verzamelen ook een optie als dit mogelijk is.[^6]
# 
# ## Overdispersie
# 
# Bij *ordinale logistische regressie* wordt aangenomen dat de residuën niet gecorreleerd zijn. Dit is in principe het geval als alle deelnemers willekeurig in de steekproef zijn opgenomen. Als deelnemers meerdere keren gemeten zijn of gematcht zijn met andere deelnemers, dan is hier geen sprake van en zijn er waarschijnlijk gecorreleerde residuën. *Ordinale logistische regressie* is dan niet de juiste analysemethode, maar *multilevel ordinale logistische regressie* kan hiervoor wel gebruikt worden. Bij *ordinale logistische regressie* wordt daarom getoetst of er overdispersie is. Overdispersie betekent dat de variantie in de voorspelde kansen groter is dan op basis van het model wordt verwacht. Het gevolg is dat de standaardfouten te laag zijn en er een hogere kans is op type I fouten (onterecht verwerpen van de nulhypothese) bij het toetsen van de significantie van regressiecoëfficiënten, de significantie van het hele model en de significantie van het vergelijken van verschillende modellen onderling met de *likelihood ratio toets*.[^6]<sup>,</sup>[^22]
# 
# De dispersieparameter geeft aan of er sprake is van overdispersie. De dispersieparameter hoort in de buurt van 1 te zitten. Als de parameter hoger dan 2 is, is er sprake van overdispersie. De gevolgen van overdispersie voor het toetsen van regressiecoëfficiënten kunnen verholpen worden door de standaardfouten van de regressiecoëfficiënten te herschalen op basis van de overdispersie. Bij het toetsen van het gehele model of het vergelijken van modellen onderling worden de waarden van de chi-kwadraat toetsstatistiek gedeeld door de dispersieparameter en wordt de p-waarde berekend op basis van de herschaalde toetsstatistiek. Het onderzoeken van de dispersieparameter en het corrigeren in het geval van overdispersie worden toegelicht bij het toetsen van de assumpties in deze toetspagina.[^6]<sup>,</sup>[^22]
# 
# Er kan ook sprake zijn van onderdispersie: de situatie waarin de variantie in voorspelde kansen kleiner is dan op basis van het model wordt verwacht. Dit leidt tot meer conservatieve toetsen en een erg lage kans op type I fouten. Deze situatie is minder erg dan overdispersie en er wordt in dit geval meestal geen correctie uitgevoerd. Dezelfde correctie als bij overdispersie kan echter wel uitgevoerd worden en zorgt er in dit geval voor dat de significantietoetsen minder conservatief worden.[^6]<sup>,</sup>[^22]
# 
# ## Proportional odds
# 
# Bij *ordinale logistische regressie* is er voor elke cumulatieve kans een regressievergelijking. Voor elke regressievergelijking wordt een intercept en een regressiecoëfficiënt voor elke predictor geschat. De intercepten zijn verschillend voor elke regressievergelijking. De regressiecoëfficiënten kunnen echter hetzelfde zijn voor elke regressievergelijking. Dit betekent dat de predictor hetzelfde effect heeft op elke cumulatieve kans. Voor de huidige casus zou dit betekenen dat de predictors Vooropleiding, Leeftijd en Gemiddeld_cijfer hetzelfde effect hebben op de cumulatieve kans op een onvoldoende, een voldoende of een goed. Dit wordt de assumptie van proportional odds genoemd. Immers, elke predictor heeft hetzelfde effect op de odds (gebaseerd op de cumulatieve kans) voor elke mogelijkheid van de afhankelijke variabele.[^20]<sup>,</sup>[^23]
# 
# Het alternatief voor de proportional odds assumptie is dat elke regressievergelijking een individuele regressiecoëfficiënt heeft voor een (of meerdere) predictor(s). Dit wordt het *partial proportional odds* model genoemd. De relatie tussen de predictor op de afhankelijke variabele hangt dan af van de mogelijkheid van de afhankelijke variabele, waardoor de relatie lastiger te interpreteren is.
# 
# De assumptie van proportional odds wordt getoetst door een model dat voldoet aan de assumptie van proportional odds te vergelijken met een model waarin er voor alle predictors niet voldaan is aan de assumptie. Oftewel, het is te toetsen door een model met per vergelijking dezelfde regressiecoëfficiënten voor elke predictor te vergelijken met een model met per vergelijking individuele regressiecoëfficiënten voor elke predictor. De toetsing wordt gedaan met behulp van een *likelihood ratio toets*. Als deze significant is, betekent het dat het model met individuele regressiecoëfficiënten significant beter is. Als deze niet significant is, is er geen verschil tussen beide modellen en is er voldaan aan de assumptie van proportional odds.
# 
# Bij een significante *likelihood ratio toets* zijn er een aantal vervolgstappen om de assumptie verder te onderzoeken. Voer eerst voor elke predictor een *likelihood ratio toets* uit waarin een model dat voldoet aan de assumptie van proportional odds vergeleken wordt met een model waarin alleen voor die specifieke predictor individuele regressiecoëfficiënten zijn voor elke vergelijking. Op deze manier kan onderzocht worden voor welke specifieke predictor(s) er niet voldaan is aan de assumptie van proportional odds. De predictors waarbij er een significante uitkomst van de *likelihood ratio toets* is, moeten nader onderzocht worden. Fit een model met individuele regressiecoëfficiënten voor alle predictors met een significante *likelihood ratio toets* en onderzoek de grootte van de regressiecoëfficiënten voor deze predictors. In het algemeen wordt aangenomen dat kleine verschillen tussen de waarden van de regressiecoëfficiënten geen reden zijn om van het *proportional odds* model af te wijken. De *likelihood ratio toets* kan namelijk ook voor kleine verschillen een significant resultaat geven, terwijl dat niet per se betekent dat het *proportional odds* model echt verkeerd is. Er zijn geen criteria voor wat een klein of groot verschil is, dit wordt overgelaten aan de beoordeling van de onderzoeker.
# 
# # Toetsing assumpties
# 
# Voer een *ordinale logistische regressie* uit om te onderzoeken of de beoordeling van het eindproject van de bachelor Industrieel Ontwerpen te voorspellen is op basis van het gemiddelde cijfer, de leeftijd en de vooropleiding van de studenten. Start met het toetsen van de assumpties en voer vervolgens de *ordinale logistische regressie* uit als hieraan voldaan is.
# 
# ## Outliers
# 
# ### Boxplots en standaardiseren
# 
# <!-- ## TEKSTBLOK: Outlier1.R -->
# Onderzoek of er univariate outliers zijn met behulp van boxplots en gestandaardiseerde scores voor continue variabelen en tabellen voor categorische variabelen. Begin met de boxplot voor de variabelen `Gemiddeld_cijfer` en `Leeftijd`.
# <!-- ## /TEKSTBLOK: Outlier1.R -->
# 
# <!-- ## OPENBLOK: Outlier2.R -->

# In[ ]:


# Maak een boxplot van de continue variabelen in de dataset
boxplot(Beoordelingen_eindproject[,c("Gemiddeld_cijfer","Leeftijd")])


# <!-- ## /OPENBLOK: Outlier2.R -->
# 
# Voor beide variabelen zijn er geen onmogelijke scores en zijn er geen grote afwijkingen. Op basis van de gestandaardiseerde scores kan onderzocht worden of er toch nog een outlier is. Onderzoek de gestandaardiseerde scores door een functie te schrijven die het aantal observaties per variabele telt met een gestandaardiseerde score hoger dan 3 of lager dan -3. Pas deze functie vervolgens toe op de gemiddelde cijfers en de leeftijden.
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
Outlier_standaardiseren(Beoordelingen_eindproject$Gemiddeld_cijfer)
Outlier_standaardiseren(Beoordelingen_eindproject$Leeftijd)


# <!-- ## /OPENBLOK: Outlier3.R -->

# Er zijn nul observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3 voor beide variabelen. Er zijn in deze stap voor de continue variabelen geen outliers gevonden.
# 
# Beoordeling en Vooropleiding zijn de categorische variabele in deze dataset. Maak een tabel met de frequenties voor alle categoriëen van deze variabelen om te onderzoeken of hier afwijkende waardes zijn.
# 
# <!-- ## OPENBLOK: Outlier4.R -->

# In[ ]:


table(Beoordelingen_eindproject$Vooropleiding)
table(Beoordelingen_eindproject$Beoordeling)


# <!-- ## /OPENBLOK: Outlier4.R -->
# 
# Voor beide categorische variabelen zijn er geen categorieën met opmerkelijke waarden. Er zijn hier dus ook geen outliers.
# 
# ### Gestandaardiseerde residuën
# 
# <!-- ## TEKSTBLOK: Outlier5.R -->
# Onderzoek of er outliers zijn met behulp van de gestandaardiseerde residuën. Voer een [logistische regressie](41-Logistische-regressie-R.html) uit voor de cumulatieve kansen van de beoordeling onvoldoende, voldoende en goed en onderzoek voor elke cumulatieve kans de gestandaardiseerde residuën. Maak eerst aparte variabelen voor elke cumulatieve kans. Gebruik daarna om de logistische regressie uit te voeren de functie `glm()` met als eerste argument de regressievergelijking `Onvoldoende_en_lager ~ Vooropleiding + Gemiddeld_cijfer + Leeftijd` met links van de tilde de afhankelijke variabele `Onvoldoende_en_lager` (voor deze cumulatieve kans) en rechts de twee onafhankelijke variabelen `Vooropleiding`, `Gemiddeld_cijfer` en `Leeftijd`. Het tweede argument is de dataset `Beoordelingen_eindproject` en het derde argument `family = "binomial"` geeft aan dat er een *logistische regressie* uitgevoerd moet worden. Bereken vervolgens de gestandaardiseerde residuën met de functie `rstandard()`, maak een plot en tel het aantal gestandaardiseerde residuën met een waarde hoger dan 3 of lager dan -3.
# <!-- ## /TEKSTBLOK: Outlier5.R -->
# 
# <!-- ## OPENBLOK: Outlier6.R -->

# In[ ]:


## Maak datasets voor de logistische regressievergelijkingen
Beoordelingen_eindproject$Onvoldoende_en_lager <- Beoordelingen_eindproject$Beoordeling == "Onvoldoende"
Beoordelingen_eindproject$Voldoende_en_lager <- Beoordelingen_eindproject$Beoordeling == "Onvoldoende" | Beoordelingen_eindproject$Beoordeling == "Voldoende"
Beoordelingen_eindproject$Goed_en_lager <- Beoordelingen_eindproject$Beoordeling == "Onvoldoende" | Beoordelingen_eindproject$Beoordeling == "Voldoende" | Beoordelingen_eindproject$Beoordeling == "Goed"

## Voer de logistische regressiemodellen uit
Regressiemodel_Onvoldoende_en_lager <- glm(Onvoldoende_en_lager ~ Vooropleiding + Gemiddeld_cijfer + Leeftijd,
                                           data = Beoordelingen_eindproject,
                                           family = "binomial")
Regressiemodel_Voldoende_en_lager <- glm(Voldoende_en_lager ~ Vooropleiding + Gemiddeld_cijfer + Leeftijd,
                                           data = Beoordelingen_eindproject,
                                           family = "binomial")
Regressiemodel_Goed_en_lager <- glm(Goed_en_lager ~ Vooropleiding + Gemiddeld_cijfer + Leeftijd,
                                           data = Beoordelingen_eindproject,
                                           family = "binomial")

# Sla de gestandaardiseerde residuën op
Residu_gestandaardiseerd_Onvoldoende_en_lager <- rstandard(Regressiemodel_Onvoldoende_en_lager)
Residu_gestandaardiseerd_Voldoende_en_lager <- rstandard(Regressiemodel_Voldoende_en_lager)
Residu_gestandaardiseerd_Goed_en_lager <- rstandard(Regressiemodel_Goed_en_lager)

# Plot de gestandaardiseerde residuën
plot(Residu_gestandaardiseerd_Onvoldoende_en_lager, 
     xlab = "Volgorde", ylab = "Gestandaardiseerde residuën")
plot(Residu_gestandaardiseerd_Voldoende_en_lager, 
     xlab = "Volgorde", ylab = "Gestandaardiseerde residuën")
plot(Residu_gestandaardiseerd_Goed_en_lager, 
     xlab = "Volgorde", ylab = "Gestandaardiseerde residuën")

# Tel het aantal gestandaardiseerde residuën met een absolute waarde groter dan 3
sum(abs(Residu_gestandaardiseerd_Onvoldoende_en_lager > 3))
sum(abs(Residu_gestandaardiseerd_Voldoende_en_lager > 3))
sum(abs(Residu_gestandaardiseerd_Goed_en_lager > 3))


# <!-- ## /OPENBLOK: Outlier6.R -->
# 
# Er zijn geen gestandaardiseerde residuën met een score hoger dan 3 of lager dan -3 wat er op wijst dat er geen outliers in de data zijn.
# 
# ### Mahalanobis distance
# 
# <!-- ## TEKSTBLOK: Outlier7.R -->
# Onderzoek of er multivariate outliers zijn met behulp van de Mahalanobis distance met behulp van de functie `mahalanobis()`. De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van het gemiddelde van alle deelnemers voor alle predictors samen. Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Zet daarom eerst de variabele Vooropleiding om in een numerieke variabele met de waarde 1 voor vwo en 0 voor hbo-p. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd.
# 
# Neem vervolgens een subset van de dataset met alleen de predictors en gebruik deze voor de Mahalanobis afstand. Gebruik de functie `mahalanobis()` met als argumenten de dataset `Subset`, de gemiddeldes van elke kolom berekend met `colMeans(Subset)` en de covariantiematrix van de dataset berekend met `cov(Subset)`.
# 
# Bereken daarna de criteriumwaarde op basis van het gewenste significantieniveau en het aantal predictors. Plot de Mahalanobis afstanden en tel het aantal deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde. Het gehanteerde significantieniveau is 0,001.
# <!-- ## /TEKSTBLOK: Outlier7.R -->
# 
# <!-- ## OPENBLOK: Outlier8.R -->

# In[ ]:


# Zet Vooropleiding om in een numerieke variabele met een 1 voor een vwo en 0 voor hbo-p
Beoordelingen_eindproject$Vooropleiding_dummy <- as.numeric(Beoordelingen_eindproject$Vooropleiding == "vwo")

# Maak een subset van de dataset met alle predictors
Subset <- Beoordelingen_eindproject[,c("Vooropleiding_dummy",
                                    "Gemiddeld_cijfer",
                                    "Leeftijd"
                                    )]

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
# Onderzoek of er outliers zijn met behulp van de gestandaardiseerde residuën. Voer een [logistische regressie](41-Logistische-regressie-R.html) uit voor de cumulatieve kansen van de beoordeling onvoldoende, voldoende en goed en onderzoek voor elke cumulatieve kans de Cook's afstanden. Maak eerst aparte variabelen voor elke cumulatieve kans. Gebruik daarna om de logistische regressie uit te voeren de functie `glm()` met als eerste argument de regressievergelijking `Onvoldoende_en_lager ~ Vooropleiding + Gemiddeld_cijfer + Leeftijd` met links van de tilde de afhankelijke variabele `Onvoldoende_en_lager` (voor deze cumulatieve kans) en rechts de twee onafhankelijke variabelen `Vooropleiding`, `Gemiddeld_cijfer` en `Leeftijd`. Het tweede argument is de dataset `Beoordelingen_eindproject` en het derde argument `family = "binomial"` geeft aan dat er een *logistische regressie* uitgevoerd moet worden. Bereken vervolgens de Cook's afstanden met de functie `cooks.distance()`, maak een plot en tel het aantal Cook's afstanden dat groter is dan de criteriumwaarde van 1.
# 
# <!-- ## /TEKSTBLOK: Outlier10.R -->
# 
# <!-- ## OPENBLOK: Outlier11.R -->

# In[ ]:


## Maak datasets voor beide logistische regressievergelijkingen
Beoordelingen_eindproject$Onvoldoende_en_lager <- Beoordelingen_eindproject$Beoordeling == "Onvoldoende"
Beoordelingen_eindproject$Voldoende_en_lager <- Beoordelingen_eindproject$Beoordeling == "Onvoldoende" | Beoordelingen_eindproject$Beoordeling == "Voldoende"
Beoordelingen_eindproject$Goed_en_lager <- Beoordelingen_eindproject$Beoordeling == "Onvoldoende" | Beoordelingen_eindproject$Beoordeling == "Voldoende" | Beoordelingen_eindproject$Beoordeling == "Goed"

## Voer de logistische regressiemodellen uit
Regressiemodel_Onvoldoende_en_lager <- glm(Onvoldoende_en_lager ~ Vooropleiding + Gemiddeld_cijfer + Leeftijd,
                                           data = Beoordelingen_eindproject,
                                           family = "binomial")
Regressiemodel_Voldoende_en_lager <- glm(Voldoende_en_lager ~ Vooropleiding + Gemiddeld_cijfer + Leeftijd,
                                           data = Beoordelingen_eindproject,
                                           family = "binomial")
Regressiemodel_Goed_en_lager <- glm(Goed_en_lager ~ Vooropleiding + Gemiddeld_cijfer + Leeftijd,
                                           data = Beoordelingen_eindproject,
                                           family = "binomial")

# Bepaal Cook's afstand voor elke deelnemer
Cooks_afstand_Onvoldoende_en_lager <- cooks.distance(Regressiemodel_Onvoldoende_en_lager)
Cooks_afstand_Voldoende_en_lager <- cooks.distance(Regressiemodel_Voldoende_en_lager)
Cooks_afstand_Goed_en_lager <- cooks.distance(Regressiemodel_Goed_en_lager)

# Plot Cook's afstanden
plot(Cooks_afstand_Onvoldoende_en_lager, 
     xlab = "Volgorde", ylab = "Cook's afstanden")
plot(Cooks_afstand_Voldoende_en_lager, 
     xlab = "Volgorde", ylab = "Cook's afstanden")
plot(Cooks_afstand_Goed_en_lager, 
     xlab = "Volgorde", ylab = "Cook's afstanden")

# Tel het aantal Cook's afstanden groter dan de criteriumwaarde van 1
sum(abs(Cooks_afstand_Onvoldoende_en_lager > 1))
sum(abs(Cooks_afstand_Voldoende_en_lager > 1))
sum(abs(Cooks_afstand_Goed_en_lager > 1))


# <!-- ## /OPENBLOK: Outlier11.R -->
# 
# Er zijn geen deelnemers met een Cook's afstand groter dan de criteriumwaarde van 1. Er lijken dus geen invloedrijke datapunten of multivariate outliers te zijn.
# 
# ## Lineariteit: Box-Tidwell
# 
# Voer de *Box-Tidwell test* uit om te onderzoeken of er een lineaire relatie is tussen de continue predictors en de logit van de afhankelijke variabele. Maak eerst voor elke continue predictor een nieuwe variabele aan die bestaat uit het product van de predictor met de logaritme (`log()`) van de predictor. Voeg daarna deze nieuwe interactietermen toe aan de regressievergelijking en voer de *ordinale logistische regressie* uit. 
# 
# Gebruik de functie `vglm()` van het package `VGAM` met als eerste argument de regressievergelijking `Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer + Leeftijd_log + Gemiddeld_cijfer_log` met links van de tilde de afhankelijke variabele `Beoordeling` en rechts de drie onafhankelijke variabelen `Vooropleiding`, `Leeftijd` en `Gemiddeld_cijfer` en de interactietermen `Leeftijd_log` en `Gemiddeld_cijfer_log`. Het tweede argument is `family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE)` met daarin `cumulative()` om aan te geven dat de cumulatieve kansen gebruikt worden in het model, `link = "logitlink"` om aan te geven dat er een logistische (logit) link-functie gebruikt wordt, `parallel = TRUE` om aan te geven dat de assumptie van *proportional odds* wordt toegepast op de regressiecoëfficiënten en `reverse = FALSE` om aan te geven dat de volgorde van de ordinale afhankelijke variabele van laag naar hoog gaat. Het derde argument is de dataset `Beoordelingen_eindproject`.
# 
# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


# Maak de interactievariabelen aan voor de continue predictors Gemiddeld_cijfer en Leeftijd
Beoordelingen_eindproject$Gemiddeld_cijfer_log <- Beoordelingen_eindproject$Gemiddeld_cijfer * log(Beoordelingen_eindproject$Gemiddeld_cijfer)
Beoordelingen_eindproject$Leeftijd_log <- Beoordelingen_eindproject$Leeftijd * log(Beoordelingen_eindproject$Leeftijd)

library(VGAM)

# Voeg deze interactievariabelen toe aan het regressiemodel en toets het regressiemodel
Regressiemodel_Box_Tidwell <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer + Leeftijd_log + Gemiddeld_cijfer_log, 
                                   family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE), 
                                   data = Beoordelingen_eindproject)

# Bekijk de significantie van de regressiecoëfficiënten
summary(Regressiemodel_Box_Tidwell)


# <!-- ## /OPENBLOK: AssLineariteit1.R -->
# 
# <!-- ## CLOSEDBLOK: AssLineariteit2.R -->

# In[ ]:


# Maak de interactievariabelen aan voor de continue predictors Gemiddeld_cijfer en Leeftijd
Beoordelingen_eindproject$Gemiddeld_cijfer_log <- Beoordelingen_eindproject$Gemiddeld_cijfer * log(Beoordelingen_eindproject$Gemiddeld_cijfer)
Beoordelingen_eindproject$Leeftijd_log <- Beoordelingen_eindproject$Leeftijd * log(Beoordelingen_eindproject$Leeftijd)

library(VGAM)

# Voeg deze interactievariabelen toe aan het regressiemodel en toets het regressiemodel
Regressiemodel_Box_Tidwell <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer + Leeftijd_log + Gemiddeld_cijfer_log, 
                                   family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE), 
                                   data = Beoordelingen_eindproject)

# Bekijk de significantie van de regressiecoëfficiënten
BT_z <- wald.stat.vlm(Regressiemodel_Box_Tidwell)


# <!-- ## /CLOSEDBLOK: AssLineariteit2.R -->
# 
# De interactieterm van de predictor Leeftijd (*z* = `r Round_and_format(BT_z[4])`, *p* = 0,663) en de predictor Gemiddeld_cijfer (*z* = `r Round_and_format(BT_z[5])`, *p* = 0,212) zijn niet significant.[^8] Er is dus voldaan aan de assumptie van lineariteit.
# 
# ## Multicollineariteit
# 
# <!-- ## TEKSTBLOK: AssMulticollineariteit1.R -->
# Onderzoek of er sprake is van multicollineariteit met behulp van Variance Inflation Factors (VIFs). Bereken de VIFs voor elke predictor met de functie `VIF()` van het package `DescTools` waarbij de functie als argument `Multicollineariteit` (het object van het regressiemodel) heeft. De functie `VIF()` werkt niet op het object van de *ordinale logistische regressie* van het package `VGAM`. Voer daarom een regressiemodel uit met een zelfverzonnen afhankelijke variabele en de predictors van de *ordinale logistische regressie*. Gebruik de functie `lm()` met als eerste argument de vergelijking `log(Gemiddeld_cijfer) ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer` met links van het tilde de zelfverzonnen afhankelijke variabele `log(Gemiddeld_cijfer)` en rechts de predictors `Vooropleiding`, `Leeftijd` en `Gemiddeld_cijfer`. Het tweede argument is de dataset `Beoordelingen_eindproject`. De afhankelijke variabele is hier zelfverzonnen omdat de VIF niet afhankelijk is van deze variabele. De afhankelijke variabele kan dus ook op een andere manier gemaakt worden.
# <!-- ## /TEKSTBLOK: AssMulticollineariteit1.R -->
# 
# <!-- ## OPENBLOK: AssMulticollineariteit2.R -->

# In[ ]:


library(DescTools)

# Voer een lineaire regressie uit
Multicollineariteit <- lm(log(Gemiddeld_cijfer) ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                           Beoordelingen_eindproject)

# Bereken de VIF voor de predictors Cijfers_P1, Cijfers_P2 en Cijfers_P3
VIF(Multicollineariteit)


# <!-- ## /OPENBLOK: AssMulticollineariteit2.R -->
# 
# Geen enkele van de VIFs is hoger dan 10, dus er is voldaan aan de assumptie van multicollineariteit.
# 
# ## Observaties per variabele
# 
# Onderzoek met behulp van kruistabellen de assumptie over observaties per variabele. Maak voor elke categorische predictor een kruistabel met de afhankelijke variabele en onderzoek of voor elk niveau van de categorische predictors beide waarden van de afhankelijke variabele aanwezig zijn.
# 
# <!-- ## OPENBLOK: ObsperVar1.R -->

# In[ ]:


# Maak de kruistabel voor de predictor Vooropleiding
with(Beoordelingen_eindproject,
     table(Vooropleiding,
           Beoordeling))


# <!-- ## /OPENBLOK: ObsperVar1.R -->
# 
# Voor beide categorieën van de predictor Vooropleiding zijn alle vier de beoordelingen geobserveerd. Dus alle waarden van de afhankelijke variabele zijn aanwezig in alle categorieën. Er is dus ook geen sprake van *complete separation* dus er is aan deze assumptie voldaan.
# 
# ## Overdispersie
# 
# <!-- ## TEKSTBLOK: Dispersie1.R -->
# Bereken de dispersieparameter om te bepalen of er sprake is van overdispersie. Voer eerst de *ordinale logistische regressie* uit omdat deze nodig is voor het toetsen van assumpties en sla het resultaat op. Interpreteer de resultaten pas na het toetsen van de assumpties.
# 
# Fit eerst het model om vervolgens de dispersieparameter te kunnen berekenen. Gebruik de functie `vglm()` van het package `VGAM` met als eerste argument de regressievergelijking `Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer` met links van de tilde de afhankelijke variabele `Beoordeling` en rechts de drie onafhankelijke variabelen `Vooropleiding`, `Leeftijd` en `Gemiddeld_cijfer`. Het tweede argument is `family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE)` met daarin `cumulative()` om aan te geven dat de cumulatieve kansen gebruikt worden in het model, `link = "logitlink"` om aan te geven dat er een logistische (logit) link-functie gebruikt wordt, `parallel = TRUE` om aan te geven dat de assumptie van *proportional odds* wordt toegepast op de regressiecoëfficiënten en `reverse = FALSE` om aan te geven dat de volgorde van de ordinale afhankelijke variabele van laag naar hoog gaat. Het derde argument is de dataset `Beoordelingen_eindproject`.
# 
# Bereken vervolgens de dispersieparameter door de deviance te delen door de vrijheidsgraden van de residuën.
# <!-- ## /TEKSTBLOK: Dispersie1.R -->
# 
# <!-- ## OPENBLOK: Dispersie2.R -->

# In[ ]:


library(VGAM)

# Fit het model
Dispersie <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                  family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                  data = Beoordelingen_eindproject)

# Bereken de dispersieparameter
Dispersie_parameter <- deviance(Dispersie) / Dispersie@df.residual

# Print de dispersieparameter
Dispersie_parameter

# Indien nodig, verkrijg de significantie van de regressiecoëfficiënten na een correctie voor de dispersie
summary(Dispersie, dispersion = Dispersie_parameter)


# <!-- ## /OPENBLOK: Dispersie2.R -->

# <!-- ## TEKSTBLOK: Dispersie3.R -->
# Er is sprake van een onderdispersie, aangezien de dispersieparameter (`r Round_and_format(Dispersie_parameter)`) kleiner dan 1 is. Het verschil met 1 is echter niet zeer klein en bij onderdispersie wordt er in het algemeen geen correctie uitgevoerd. Voor de *ordinale logistische regressie* in deze casus wordt daarom geen correctie uitgevoerd vanwege onderdispersie.
# <!-- ## /TEKSTBLOK: Dispersie3.R -->
# 
# ## Proportional odds
# 
# <!-- ## TEKSTBLOK: ProportionalOdds1.R -->
# Toets de assumptie van *proportional odds* door een model dat wel rekening houdt met deze assumptie te vergelijken met een model dat er geen rekening mee houdt. Fit eerst het model dat er wel rekening mee houdt . Gebruik de functie `vglm()` van het package `VGAM` met als eerste argument de regressievergelijking `Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer` met links van de tilde de afhankelijke variabele `Beoordeling` en rechts de drie onafhankelijke variabelen `Vooropleiding`, `Leeftijd` en `Gemiddeld_cijfer`. Het tweede argument is `family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE)` met daarin `cumulative()` om aan te geven dat de cumulatieve kansen gebruikt worden in het model, `link = "logitlink"` om aan te geven dat er een logistische (logit) link-functie gebruikt wordt, `parallel = TRUE` om aan te geven dat de assumptie van *proportional odds* wordt toegepast op de regressiecoëfficiënten en `reverse = FALSE` om aan te geven dat de volgorde van de ordinale afhankelijke variabele van laag naar hoog gaat. Het derde argument is de dataset `Beoordelingen_eindproject`.
# 
# Fit daarna het model dat er geen rekening mee houdt. De procedure hiervoor is precies hetzelfde, behalve dat er nu in de functie `cumulative()` het argument `parallel = FALSE` in plaats van `parallel = TRUE` gebruikt wordt. Toets daarna het verschil tussen beide modellen met een *likelihood ratio toets* met behulp van de functie `VGAM::lrtest()` van het package `VGAM` met als argumenten het model dat wel (`Proportional_odds`) en geen (`Geen_proportional_odds`) rekening houdt met *proportional odds*.
# <!-- ## /TEKSTBLOK: ProportionalOdds1.R -->
# 
# <!-- ## OPENBLOK: ProportionalOdds2.R -->

# In[ ]:


library(VGAM)

# Fit het model met en zonder de assumptie van proportional odds voor alle predictors
Proportional_odds <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                  family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                  data = Beoordelingen_eindproject)

Geen_proportional_odds <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                  family = cumulative(link = "logitlink", parallel = FALSE, reverse = FALSE),
                  data = Beoordelingen_eindproject)

# Toets de significantie van het verschil tussen beide modellen
VGAM::lrtest(Proportional_odds, Geen_proportional_odds)


# <!-- ## /OPENBLOK: ProportionalOdds2.R -->
# 
# <!-- ## CLOSEDBLOK: Dispersie3.R -->

# In[ ]:


library(VGAM)

# Fit het model met en zonder de assumptie van proportional odds voor alle predictors
Proportional_odds <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                  family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                  data = Beoordelingen_eindproject)

Geen_proportional_odds <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                  family = cumulative(link = "logitlink", parallel = FALSE, reverse = FALSE),
                  data = Beoordelingen_eindproject)

# Toets de significantie van het verschil tussen beide modellen
PO_toets <- VGAM::lrtest(Proportional_odds, Geen_proportional_odds)@Body
PO_toets_chi <- PO_toets$Chisq[2]
PO_toets_df <- -1 * PO_toets$Df[2]
PO_toets_p <- PO_toets$`Pr(>Chisq)`[2]


# <!-- ## /CLOSEDBLOK: Dispersie3.R -->
# 
# <!-- ## TEKSTBLOK: ProportionalOdds4.R -->
# Uit de *likelihood ratio toets* blijkt dat er geen significant verschil is tussen beide modellen, *&chi;^2^* = `r Round_and_format(PO_toets$Chisq[2])`, *df* = `r PO_toets_df`, *p* = `r Round_and_format(PO_toets_p,3)`. Er is dus voldaan aan de assumptie van *proportional odds*.
# 
# Hoewel het in de huidige casus dus niet nodig is, wordt nu geïllustreerd wat de vervolgstappen zijn als er niet voldaan is aan de assumptie van *proportional odds*. Onderzoek eerst voor welke predictor(s) er niet voldaan is aan de assumptie van *proportional odds* door het model met *proportional odds* voor alle predictors te vergelijken met de modellen waarbij steeds voor één predictor geen *proportional odds* zijn. Fit deze modellen op vergelijkbare manier als hierboven en vergelijk de modellen ook op de manier die hierboven is omschreven. Bij een significant resultaat is er sprake van een schending van de assumptie van *proportional odds* voor die assumptie.
# <!-- ## /TEKSTBLOK: ProportionalOdds4.R -->
# 
# <!-- ## OPENBLOK: ProportionalOdds5.R -->

# In[ ]:


# Fit het model met en zonder de assumptie van proportional odds voor alle predictors
Proportional_odds <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                  family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                  data = Beoordelingen_eindproject)

Geen_proportional_odds_vooropleiding <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                                             family = cumulative(link = "logitlink", parallel = FALSE ~ 1 + Vooropleiding, reverse = FALSE),
                                             data = Beoordelingen_eindproject)

Geen_proportional_odds_leeftijd <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                                             family = cumulative(link = "logitlink", parallel = FALSE ~ 1 + Leeftijd, reverse = FALSE),
                                             data = Beoordelingen_eindproject)

Geen_proportional_odds_gemiddeld_cijfer <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                                             family = cumulative(link = "logitlink", parallel = FALSE ~ 1 + Gemiddeld_cijfer, reverse = FALSE),
                                             data = Beoordelingen_eindproject)

# Toets de significantie van het verschil tussen beide modellen
VGAM::lrtest(Proportional_odds, Geen_proportional_odds_vooropleiding)
VGAM::lrtest(Proportional_odds, Geen_proportional_odds_leeftijd)
VGAM::lrtest(Proportional_odds, Geen_proportional_odds_gemiddeld_cijfer)

# Bekijk de regressiecoëfficiënten van het model om te onderzoeken hoe groot de verschillen zijn
summary(Geen_proportional_odds_gemiddeld_cijfer)


# <!-- ## OPENBLOK: ProportionalOdds5.R -->
# 
# Voor alle drie de predictors geeft de *likelihood ratio toets* geen significant resultaat. Dit betekent dat alle drie de predictors voldoen aan de assumptie van *proportional odds*. Stel dat een van de predictors voor een significante *likelihood ratio toets* zorgt, onderzoek dan (met behulp van de functie `summary()`) de verschillen tussen de regressiecoëfficiënten van de predictors voor de verschillende vergelijkingen met behulp van de functie `summary()` door de regressiecoëfficiënten te vergelijken qua grootte.
# 
# # Uitvoering
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Als alle assumpties zijn getoetst en aan alle assumpties is voldaan, kan de *ordinale logistische regressie* uitgevoerd worden. Gebruik de functie `vglm()` van het package `VGAM` met als eerste argument de regressievergelijking `Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer` met links van de tilde de afhankelijke variabele `Beoordeling` en rechts de drie onafhankelijke variabelen `Vooropleiding`, `Leeftijd` en `Gemiddeld_cijfer`. Het tweede argument is `family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE)` met daarin `cumulative()` om aan te geven dat de cumulatieve kansen gebruikt worden in het model, `link = "logitlink"` om aan te geven dat er een logistische (logit) link-functie gebruikt wordt, `parallel = TRUE` om aan te geven dat de assumptie van *proportional odds* wordt toegepast op de regressiecoëfficiënten en `reverse = FALSE` om aan te geven dat de volgorde van de ordinale afhankelijke variabele van laag naar hoog gaat. Het derde argument is de dataset `Beoordelingen_eindproject`. 
# 
# Voer daarna de *likelihood ratio toets* uit met behulp van de functie `VGAM::lrtest()` van het package `VGAM` met als argument het object van het regressiemodel (`Regressiemodel`). Sla het model op en presenteer vervolgens een overzicht van de resultaten met de functie `summary()`. Bepaal de 95%-betrouwbaarheidsintervallen van de regressiecoëfficiënten met de functie `confint()`. Bereken ten slotte de Nagelkerke $R^2$ met behulp van een zelfgeschreven functie[^15].
# 
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


library(VGAM)

# Stel het regressiemodel op
Regressiemodel <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                  family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                  data = Beoordelingen_eindproject)

# Voer de likelihood ratio toets uit
VGAM::lrtest(Regressiemodel)

# Presenteer de resultaten
summary(Regressiemodel)

# Presenteer de 95%-betrouwbaarheidsintervallen
confint(Regressiemodel)

# Bereken de odds ratio van alle regressiecoëfficiënten door de exponent te nemen
exp(coef(Regressiemodel))

# Bepaal de Nagelkerke R2

# Sla het resultaat van de likelihood ratio toets op
LR_toets <- VGAM::lrtest(Regressiemodel)@Body
# Bereken de deviance for het regressiemodel en voor een interceptmodel
Deviance_interceptmodel <- -2*LR_toets$LogLik[2]
Deviance_regressiemodel <- -2*LR_toets$LogLik[1]
# Sla het aantal deelnemers op
Aantal_deelnemers <- nrow(Beoordelingen_eindproject)
# Vul de formule in voor de Nagelkerke R2
Nagelkerke_R2 <- (1 - exp( (Deviance_regressiemodel - Deviance_interceptmodel) / Aantal_deelnemers) ) / (1 - exp( -Deviance_interceptmodel / Aantal_deelnemers) )
# Print de Nagelkerke R2
Nagelkerke_R2


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# <!-- ## CLOSEDBLOK: Uitvoering3.R -->

# In[ ]:


Reg <- summary(Regressiemodel)@coef3
CI <- confint(Regressiemodel)


# <!-- ## /CLOSEDBLOK: Uitvoering3.R -->
# 
# ## Significantie regressiemodel
# 
# <!-- ## TEKSTBLOK: Ftoets1.R -->
# Bepaal als eerste stap de significantie van het regressiemodel met behulp van de *likelihood ratio toets*. De *likelihood ratio toets* voor het regressiemodel laat een significant verschil zien tussen het voorgestelde model en een model met alleen een intercept, *&chi;^2^* = `r Round_and_format(LR_toets$Chisq[2])`, *df* = `r LR_toets$Df[2]`, *p* < 0,0001, $R^2_N$ = `r Round_and_format(100 * Nagelkerke_R2)`.[^8] De nulhypothese dat geen enkele predictor van de predictors Vooropleiding, Leeftijd en  Gemiddeld_cijfer gerelateerd is aan de afhankelijke variabele Beoordeling kan verworpen worden. De Nagelkerke $R^2$ is `r Round_and_format(100*Nagelkerke_R2)`. Omdat de *likelihood ratio toets* voor het gehele model significant is, kunnen de coëfficiënten geinterpreteerd worden.
# <!-- ## TEKSTBLOK: Ftoets1.R -->
# 
# ## Significantie en interpretatie coëfficiënten
# 
# <!-- ## TEKSTBLOK: Coefficienten1.R -->
# Voor de intercept en de regressiecoëfficiënten van de predictors zijn de geschatte coëfficiënt (`Estimate`), de standaardfout van de geschatte coëfficiënt (`Std. Error`) en de z-statistiek (`z value`) en p-waarde (`Pr(>|z|)`) van de *Wald toets* voor de regressiecoëfficiënt weergegeven:
# 
# * Vooropleiding: De geschatte waarde voor de regressiecoëfficiënt van de variabele Vooropleiding is `r Round_and_format(Reg[4,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg[4,3])`, *p* = `r Round_and_format(Reg[4,4], 3)`).[^8] De hoofdcategorie van de variabele Vooropleiding is `vwo`, aangezien de variabele in de resultaten weergegeven is als `Vooropleidingvwo`. Dit betekent dat de referentiecategorie `hbo-p` is. Als de overige predictors gelijkblijven is de odds van het behalen van een bepaalde beoordeling of een beoordeling die lager is `r Round_and_format(exp(Reg[4,1]))` keer zo hoog voor studenten met een hbo-p vooropleiding ten opzichte van studenten met een vwo vooropleiding. Studenten met een hbo-p vooropleiding hebben dus relatief gezien lagere beoordelingen dan studenten met een vwo vooropleiding.
# * Leeftijd: De geschatte waarde voor de regressiecoëfficiënt van de variabele Leeftijd is `r Round_and_format(Reg[5,1])` en is niet significant verschillend van 0 (*z* = `r Round_and_format(Reg[5,3])`, *p* = `r Round_and_format(Reg[5,4], 3)`).[^8] De odds ratio hoeft niet geïnterpreteerd te worden, omdat de regressiecoëfficiënt niet significant verschillend van nul is. Er is dus geen relatie tussen de leeftijd en de beoordeling van de student.
# * Gemiddeld_cijfer: De geschatte waarde voor de regressiecoëfficiënt van de variabele Gemiddeld_cijfer is `r Round_and_format(Reg[6,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg[6,3])`, *p* < 0,0001).[^8] Als de overige predictors gelijkblijven is de odds van het behalen van een bepaalde beoordeling of een beoordeling die lager is `r Round_and_format(exp(Reg[6,1]))` keer zo hoog bij een toename van het gemiddeld cijfer met één punt. De odds het behalen van een bepaalde beoordeling of een beoordeling die lager is, is dus eigenlijk `r Round_and_format(1/exp(Reg[6,1]))` (1 / `r Round_and_format(exp(Reg[6,1]))`) keer zo laag bij een toename van één punt in het gemiddelde cijfer. Dit betekent dus dat studenten met een hoger gemiddeld cijfer relatief gezien een hogere beoordeling voor hun eindproject ontvangen.

# <!-- ## /TEKSTBLOK: Coefficienten1.R -->
# 
# ## Sterkte van de relatie tussen de predictor en afhankelijke variabele
# 
# <!-- ## TEKSTBLOK: CoefficientenStd1.R -->
# De regressiecoëfficiënten van de predictors Vooropleiding en Gemiddeld_cijfer zijn significant verschillend van nul. Met behulp van de gestandaardiseerde regressiecoëfficiënten kan bepaald worden welke predictor het sterkst gerelateerd is aan de afhankelijke variabele Beoordeling. 
# 
# Standaardiseer alle predictors met de functie `scale()` met als argument de predictor. Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Zet daarom eerst de variabele `Vooropleiding` om in een numerieke variabele met de waarde 1 voor vwo en 0 voor hbo-p. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd. Voer nu de *ordinale logistische regressie* uit met de gestandaardiseerde predictors en bekijk de regressiecoëfficiënten. Deze regressiecoëfficiënten zijn nu gestandaardiseerd.
# <!-- ## /TEKSTBLOK: CoefficientenStd1.R -->
# 
# <!-- ## OPENBLOK: CoefficientenStd2.R -->

# In[ ]:


# Zet de variabele Vooropleiding om in een numerieke variabele met een 1 voor vwo en 0 voor hbo-p
Beoordelingen_eindproject$Vooropleiding_dummy <- as.numeric(Beoordelingen_eindproject$Vooropleiding == "vwo")

# Standaardiseer de predictors
Beoordelingen_eindproject$Vooropleiding_dummy_stand <- scale(Beoordelingen_eindproject$Vooropleiding_dummy)
Beoordelingen_eindproject$Leeftijd_stand <- scale(Beoordelingen_eindproject$Leeftijd)
Beoordelingen_eindproject$Gemiddeld_cijfer_stand <- scale(Beoordelingen_eindproject$Gemiddeld_cijfer)

# Stel het regressiemodel op
Regressiemodel_gestandaardiseerd <- vglm(Beoordeling ~ Vooropleiding_dummy_stand + Leeftijd_stand + Gemiddeld_cijfer_stand,
                                         family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                                         data = Beoordelingen_eindproject)

# Laat de gestandaardiseerde coefficienten zien
coef(Regressiemodel_gestandaardiseerd)

# Laat de gestandaardiseerde odds ratios zien
exp(coef(Regressiemodel_gestandaardiseerd))


# <!-- ## /OPENBLOK: CoefficientenStd2.R -->
# 
# <!-- ## CLOSEDBLOK: CoefficientenStd3.R -->

# In[ ]:


Coefficienten_std <- coef(Regressiemodel_gestandaardiseerd)


# <!-- ## /CLOSEDBLOK: CoefficientenStd3.R -->
# 
# <!-- ## TEKSTBLOK: CoefficientenStd4.R -->
# De gestandaardiseerde regressiecoëfficiënt is `r Round_and_format(Coefficienten_std[4])` voor de predictor Vooropleiding, `r Round_and_format(Coefficienten_std[5])` voor de predictor Leeftijd en `r Round_and_format(Coefficienten_std[6])` voor de predictor Gemiddeld_cijfer. Het gemiddelde cijfer van een student heeft dus de meeste invloed op de beoordeling van het eindproject. De gestandaardiseerde odds ratio van de predictor Gemiddeld_cijfer laat zien dat een toename van één standaardafwijking in de leeftijd van een student resulteert in een `r Round_and_format(exp(Coefficienten_std[6]))` zo hoge odds van het behalen van een bepaalde beoordeling of een beoordeling die lager is, oftewel een `r Round_and_format(1/exp(Coefficienten_std[6]))` zo lage odds van het behalen van een bepaalde beoordeling of een beoordeling die lager is, als de overige predictors gelijk blijven.
# <!-- ## /TEKSTBLOK: CoefficientenStd4.R -->
# 
# # Uitvoering likelihood ratio toets voor vergelijking twee regressiemodellen
# 
# De *likelihood ratio toets* wordt bij *ordinale logistische regressie* gebruikt om de significantie van het gehele regressiemodel te toetsen ten opzichte van het interceptmodel. Deze *likelihood ratio toets* kan ook gebruikt worden om te toetsen of twee geneste regressiemodellen onderling verschillen qua model fit. Hoewel deze vergelijking in de casus niet voorbijkomt, wordt deze toch geïllustreerd. Vergelijk hiervoor een model met de predictor Vooropleiding met een model met de predictors Vooropleiding, Leeftijd en Gemiddeld_cijfer.
# 
# <!-- ## TEKSTBLOK: ModellenVergelijken1.R -->
# Voer de *likelihood ratio toets* uit met de functie `VGAM::lrtest()` van het package `VGAM` met als argumenten de modelobjecten van de resultaten van de twee regressiemodellen die worden vergeleken (`Model_1` en `Model_2`). Voer eerst de *ordinale logistische regressie* uit voor beide modellen en vergelijk ze daarna. Bereken ten slotte de Nagelkerke $R^2$ met een zelfgeschreven functie.
# <!-- ## /TEKSTBLOK: ModellenVergelijken1.R -->
# 
# <!-- ## OPENBLOK: ModellenVergelijken2.R -->

# In[ ]:


library(VGAM)

# Stel het regressiemodel op
Model_1 <- vglm(Beoordeling ~ Vooropleiding,
                family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                data = Beoordelingen_eindproject)

Model_2 <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                data = Beoordelingen_eindproject)

# Voer de likelihood ratio toets uit
VGAM::lrtest(Model_1, Model_2)

# Bereken de Nagelkerke R2 (%) van model 1
LR_toets_model_1 <- VGAM::lrtest(Model_1)@Body
Deviance_interceptmodel <- -2*LR_toets_model_1$LogLik[2]
Deviance_model_1 <- -2*LR_toets_model_1$LogLik[1]
Aantal_deelnemers <- nrow(Beoordelingen_eindproject)

Nagelkerke_R2_model_1 <- (1 - exp( (Deviance_model_1 - Deviance_interceptmodel) / Aantal_deelnemers) ) / (1 - exp( -Deviance_interceptmodel / Aantal_deelnemers) )

Nagelkerke_R2_model_1

# Bereken de Nagelkerke R2 (%) van model 2
LR_toets_model_2 <- VGAM::lrtest(Model_2)@Body
Deviance_interceptmodel <- -2*LR_toets_model_2$LogLik[2]
Deviance_model_2 <- -2*LR_toets_model_2$LogLik[1]
Aantal_deelnemers <- nrow(Beoordelingen_eindproject)

Nagelkerke_R2_model_2 <- (1 - exp( (Deviance_model_2 - Deviance_interceptmodel) / Aantal_deelnemers) ) / (1 - exp( -Deviance_interceptmodel / Aantal_deelnemers) )

Nagelkerke_R2_model_2


# <!-- ## /OPENBLOK: ModellenVergelijken2.R -->
# 
# <!-- ## CLOSEDBLOK: ModellenVergelijken3.R -->

# In[ ]:


library(VGAM)

# Stel het regressiemodel op
Model_1 <- vglm(Beoordeling ~ Vooropleiding,
                family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                data = Beoordelingen_eindproject)

Model_2 <- vglm(Beoordeling ~ Vooropleiding + Leeftijd + Gemiddeld_cijfer,
                family = cumulative(link = "logitlink", parallel = TRUE, reverse = FALSE),
                data = Beoordelingen_eindproject)

# Voer de likelihood ratio toets uit
library(lmtest)
Vergelijking <- VGAM::lrtest(Model_1, Model_2)@Body
Vergelijking_chi <- Vergelijking$Chisq[2]
Vergelijking_df <- -1 * Vergelijking$Df[2]


# <!-- ## /CLOSEDBLOK: ModellenVergelijken3.R -->
# 
# <!-- ## TEKSTBLOK: ModellenVergelijken4.R -->
# De *likelihood ratio toets* toont aan dat er een significant verschil is in de model fit tussen beide modellen, *&chi;^2^* = `r Round_and_format(Vergelijking_chi)`, *df* = `r Vergelijking_df[2]`, *p* < 0,0001.[^8] Het regressiemodel met predictor Vooropleiding verklaart slechts `r Round_and_format(100*Nagelkerke_R2_model_1)`% van de variatie in Beoordeling en het regressiemodel met predictoren Vooropleiding, Leeftijd en Gemiddeld_cijfer verklaart `r Round_and_format(100*Nagelkerke_R2_model_2)`% van de variatie. Het verschil in verklaarde variatie is `r Round_and_format(100*Nagelkerke_R2_model_2 - 100*Nagelkerke_R2_model_1)`%. Het model met Vooropleiding, Leeftijd en Gemiddeld_cijfer als predictors heeft dus een significant betere model fit dan het model met alleen Vooropleiding als predictor.
# <!-- ## /TEKSTBLOK: ModellenVergelijken4.R -->
# 
# # Voorspellen en classificeren
# 
# Op basis van het regressiemodel kan voor iedere student de kans op een bepaalde beoordeling voorspeld worden. De voorspelde kans kan direct vergeleken worden met de observaties om te onderzoeken hoe goed het model voorspeld. Daarnaast is het ook mogelijk om de studenten te classificeren op een bepaalde beoordeling op basis van de voorspelde kans. Met behulp van de classificaties kan een classificatietabel gemaakt worden waarmee de kwaliteit van de voorspelkracht van het model beoordeeld kan worden.
# 
# Bepaal eerst de voorspelde kansen met de functie `predict()` met als argumenten het object van het regressie model `Regressiemodel` en `type = response` om aan te geven dat de voorspelde kans bepaald moet worden. Classificeer daarna de studenten op basis van de mogelijkheid met de hoogste voorspelde kans. Maak daarna een tabel met de frequenties per mogelijkheid van de classificaties en maak een classificatietabel voor de classificaties en observaties van de studenten Fysiotherapie. Bereken op basis van de classificatietabel de accuraatheid van de classificaties.

# In[ ]:


# Bepaal de voorspelde kansen
Voorspelde_kans <- predict(Regressiemodel,
                           type = "response")

# Classificeer de studenten op basis van de hoogste voorspelde kans
Classificaties <- c()
for (i in 1:nrow(Voorspelde_kans)) {
  Vervolg_opties <- colnames(Voorspelde_kans)
  Classificaties[i] <- Vervolg_opties[Voorspelde_kans[i,] == max(Voorspelde_kans[i,])]
}

# Tabelleer de frequenties per categorie van de classificaties
table(Classificaties)

# Maak een classificatietabel, gebruik de functie factor en het argument levels om aan te geven
# welke categorieën er moeten worden weergegeven
Tabel <- table(Classificaties = factor(Classificaties, levels = c("Onvoldoende", "Voldoende", "Goed","Uitstekend")),
               Observaties = Beoordelingen_eindproject$Beoordeling)
print(Tabel)

# Bereken de accuraatheid
Accuraatheid <- (Tabel["Onvoldoende","Onvoldoende"] + Tabel["Voldoende","Voldoende"] +  Tabel["Goed","Goed"] + Tabel["Uitstekend","Uitstekend"]) / sum(Tabel)

Accuraatheid


# De classificatietabel laat zien dat de meerderheid van de studenten correct geclassificeerd is, maar ook dat er veel verkeerde classificaties zijn. Ook valt het op dat er heel weinig studenten geclassificeerd zijn met de mogelijkheden Onvoldoende en Uitstekend. De accuraatheid van de classificaties van het regressiemodel is `r Round_and_format(100*Accuraatheid)`%.

# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage1.R -->
# Een *ordinale logistische regressie* is uitgevoerd om te onderzoeken of de beoordeling van het eindproject van studenten van de bachelor Industrieel Ontwerpen gerelateerd is aan de vooropleiding (vwo of hbo-p), de leeftijd en het gemiddelde cijfer in het eerste jaar van de bachlor. Uit het toetsen van de assumpties van *ordinale logistische regressie* bleek dat er aan alle assumpties is voldaan. De resultaten van de *ordinale logistische regressie* zijn te vinden in Tabel 4. 
# 
# De *likelihood ratio toets* voor het regressiemodel laat zien dat het opgestelde regressiemodel minimaal één coëfficiënt heeft die significant verschilt van nul, *&chi;^2^* = `r Round_and_format(LR_toets$Chisq[2])`, *df* = `r LR_toets$Df[2]`, *p* < 0,0001, $R^2_N$ = `r Round_and_format(100 * Nagelkerke_R2)`. De vooropleiding (*&beta;* = `r Round_and_format(Reg[4,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg[4,3])`, *p* = `r Round_and_format(Reg[4,4], 3)`) en het gemiddeld eindexamencijfer (*&beta;* = `r Round_and_format(Reg[6,1])`, *z* = `r Round_and_format(Reg[6,3])`, *p* < 0,0001), maar de leeftijd van de student is dit niet (*&beta;* = `r Round_and_format(Reg[5,1])`, *z* = `r Round_and_format(Reg[5,3])`, *p* = `r Round_and_format(Reg[5,4], 3)`). De 
# 
# De gestandaardiseerde coëfficiënten laten zien dat het gemiddelde cijfer van de student het sterkst gerelateerd is aan de kans op uitval. Om in te schatten of een student extra ondersteuning kan krijgen omdat de kans op uitval hoger is, kan de studieloopbaanbegeleider dus rekening houden met het geslacht, de leeftijd en het gemiddeld eindexamencijfer van studenten, maar hoeft hij geen rekening te houden met de vooropleiding.
# 
# `r Round_and_format(Reg[4,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg[4,3])`, *p* = `r Round_and_format(Reg[4,4], 3)`)

# Voor de vergelijking tussen de mogelijkheden hbo master en direct aan het werk gaan zijn zowel het gemiddelde cijfer (*&beta;* = `r Round_and_format(Reg[5,1])`, *z* = `r Round_and_format(Reg[5,3])`, *p* < 0,0001) als (*&beta;* = `r Round_and_format(Reg[3,1])`, *z* = `r Round_and_format(Reg[3,3])`, *p* = 0,007) significante predictors. Voor de vergelijking tussen de mogelijkheden wo master en direct aan het werk gaan is het gemiddelde cijfer (*&beta;* = `r Round_and_format(Reg[6,1])`, *z* = `r Round_and_format(Reg[6,3])`, *p* < 0,0001) wel een significante predictor, maar het wel of niet nominaal afstuderen (*&beta;* = `r Round_and_format(Reg[4,1])`, *z* = `r Round_and_format(Reg[4,3])`, *p* = `r Round_and_format(Reg[4,4])`) geen significante predictor. De gestandaardiseerde coëfficiënten laten zien dat het gemiddelde cijfer tijdens de bachelor het sterkst gerelateerd is aan het vervolg na de opleiding Fysiotherapie. Om in te schatten welke studenten in aanmerking komen voor een hbo master zijn het wel of niet nominaal afstuderen en het gemiddelde cijfer relevant, maar voor een wo master is alleen het gemiddelde cijfer in de bachelor relevant.
# <!-- ## /TEKSTBLOK: Rapportage1.R -->
# 
# <!-- ## TEKSTBLOK: Rapportage2.R -->
# |                           | Coëfficiënt   | Standaard- fout | z | p-waarde | 95%-betrouwbaar- heidsinterval | Gestandaardiseerde coëfficiënt  | Odds ratio |
# | ------------------------- | ---------| ---------| ---------| ---------| ---------| ---------| ---------| 
# | Intercept (Beoordeling <= Onvoldoende)                | `r Round_and_format(Reg[1,1])` |  `r Round_and_format(Reg[1,2])` |  `r Round_and_format(Reg[1,3])` |  < 0,0001*  |  `r Round_and_format(CI[1,1])` - `r Round_and_format(CI[1,2])`  | - | - |
# | Intercept (Beoordeling <= Voldoende)                 | `r Round_and_format(Reg[2,1])` |  `r Round_and_format(Reg[2,2])` |  `r Round_and_format(Reg[2,3])` |  < 0,0001*  |  `r Round_and_format(CI[2,1])` - `r Round_and_format(CI[2,2])`  | - | - |
# | Intercept (Beoordeling <= Goed)                | `r Round_and_format(Reg[3,1])` |  `r Round_and_format(Reg[3,2])` |  `r Round_and_format(Reg[3,3])` |  < 0,0001*  |  `r Round_and_format(CI[3,1])` - `r Round_and_format(CI[3,2])`  | - | - |
# | Vooropleiding (vwo)       | `r Round_and_format(Reg[4,1])` |  `r Round_and_format(Reg[4,2])` |  `r Round_and_format(Reg[4,3])` |  `r Round_and_format(Reg[4,4],3)`* |  `r Round_and_format(CI[4,1])` - `r Round_and_format(CI[4,2])` | `r Round_and_format(Coefficienten_std[4])`| `r Round_and_format(exp(Reg[4,1]))` |
# | Leeftijd          | `r Round_and_format(Reg[5,1])` |  `r Round_and_format(Reg[5,2])` |  `r Round_and_format(Reg[5,3])` |  `r Round_and_format(Reg[5,4],3)` |  `r Round_and_format(CI[5,1])` - `r Round_and_format(CI[5,2])`  | `r Round_and_format(Coefficienten_std[5])`| `r Round_and_format(exp(Reg[5,1]))` |
# | Gemiddeld cijfer       | `r Round_and_format(Reg[6,1])` |  `r Round_and_format(Reg[6,2])` |  `r Round_and_format(Reg[6,3])` |  < 0,0001* |  `r Round_and_format(CI[6,1])` - `r Round_and_format(CI[6,2])` | `r Round_and_format(Coefficienten_std[6])`| `r Round_and_format(exp(Reg[6,1]))` |
# 
# *Tabel 4. Regressiecoëfficiënten en bijbehorende standaardfouten, z-statistieken, p-waardes, 95%-betrouwbaarheidsintervallen, gestandaardiseerde coëfficiënten en odds ratios.*
# <!-- ## /TEKSTBLOK: Rapportage2.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Ordinal Regression using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/ordinal-regression-using-spss-statistics.php
# [^2]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 760-813.
# [^3]: Universiteit van Amsterdam (13 augustus 2016). *Outliers*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).  
# [^4]: Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$.
# [^5]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^6]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 443-446.
# [^7]: Stat 501. *12.4 - Detecting Multicollinearity Using Variance Inflation Factors*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat501/lesson/12/12.4).
# [^8]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^9]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 293-356.
# [^11]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 338-341.
# [^12]: James, G., Witten, D., Hastie, T. & Tibshirani, R. (2013). *Introduction to Statistical Learning with applications in R*. Springer. Pagina 127-174.
# [^13]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^14]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# [^15]: De Nagelkerke $R^2$ is te berekenen met de formule $R^2_N = \frac{1 + exp([Dev_{model} - Dev_{null}]/N)}{1 + exp([- Dev_{null}]/N)}$ waarbij $Dev_{model}$ de deviance van het getoetste model is, $Dev_{null}$ de deviance van een interceptmodel (verschillend per vergelijking) is en $N$ het aantal deelnemers is. Voor meer informatie zie Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 764-766. 
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^20]: Stat 504. *8.4 - The Proportional-Odds Cumulative Logit Model*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat504/lesson/8/8.4).
# [^21]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 293-356.
# [^22]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 772.
# [^23]: ReStore. *Module 5 - Ordinal Regression*. [National Centre for Research Methods - University of Southampton](https://www.restore.ac.uk/srme/www/fac/soc/wie/research-new/srme/modules/mod5/index.html)
