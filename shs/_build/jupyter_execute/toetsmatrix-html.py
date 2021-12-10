#!/usr/bin/env python
# coding: utf-8

# # toetsmatrix html

# <table class="toetsmatrix">
#     <tbody>
#         <tr>
#             <td colspan="3" rowspan="3"></td>
#             <td colspan="5" class="header1 innercell">Onafhankelijke variabele</td>
#         </tr>
#         <tr>
#             <td class="header2 innercell">1 groep</td>
#             <td colspan="2" class="header2 innercell">2 groepen</td>
#             <td colspan="2" class="header2 innercell">&gt;2 groepen</td>
#         </tr>
#         <tr>
#             <td class="header3 innercell">met referentie</td>
#             <td class="header3 innercell">gepaard</td>
#             <td class="header3 innercell">ongepaard</td>
#             <td class="header3 innercell">gepaard</td>
#             <td class="header3 innercell">ongepaard</td>
#         </tr>
#  <tr>
# <td rowspan="5" class="header1 innercell">Afhankelijke variabele</td>
# <td rowspan="2" class="header2 innercell">
# continu
# <br/>
# (interval en ratio)
# </td>
# <td class="header3 innercell">
# normaal
# <br/>
# verdeeld
# </td>
# <td class="innercell published">
# <a href="01-One-sample-t-toets-R.html" title="One sample t-toets">One sample t-toets</a>
# </td>
# <td class="innercell published">
# <a href="02-Gepaarde-t-toets-R.html" title="Gepaarde t-toets">Gepaarde t-toets</a>
# </td>
# <td class="innercell published">
# <a href="03-Ongepaarde-t-toets-R.html" title="Ongepaarde t-toets">Ongepaarde t-toets</a>
# </td>
# <td class="innercell published">
# <a href="04-Repeated-measures-ANOVA-R.html" title="Repeated measures ANOVA">Repeated measures ANOVA</a>
# </td>
# <td class="innercell published">
# <a href="05-One-way-ANOVA-R.html" title="One-way ANOVA">One-way ANOVA</a>
# </td>
# </tr><tr>
# <td class="header3 innercell">
# niet normaal
# <br/>
# verdeeld
# </td>
# <td class="innercell published">
# <a href="06-Tekentoets-I-R.html" title="Tekentoets I">Tekentoets I</a>
# </td>
# <td class="innercell">
# <a href="07-Wilcoxon-signed-rank-toets-I-R.html" title="Wilcoxon signed rank toets I" class="published">Wilcoxon signed rank toets I</a>
# /
# <a href="26-Tekentoets-II-R.html" title="Tekentoets II" class="published">Tekentoets II</a>
# </td>
# <td class="innercell">
# <a href="08-Mann-Whitney-U-toets-I-R.html" title="Mann-Whitney U toets I" class="published">Mann-Whitney U toets I</a>
# /
# <a href="27-Moods-mediaan-toets-R.html" title="Mood&#39;s mediaan toets" class="published">Mood's mediaan toets</a>
# </td>
# <td class="innercell published">
# <a href="09-Friedmans-ANOVA-I-R.html" title="Friedman&#39;s ANOVA I">Friedman's ANOVA I</a>
# </td>
# <td class="innercell published">
# <a href="10-Kruskal-Wallis-toets-I-R.html" title="Kruskal Wallis toets I">Kruskal Wallis toets I</a>
# </td>
# </tr><tr>
# <td rowspan="3" class="header2 innercell">
# categorisch
# <br/>
# 
# </td>
# <td class="header3 innercell">
# binair
# <br/>
# (2 waarden)
# </td>
# <td class="innercell published">
# <a href="11-Chi-kwadraat-toets-voor-goodness-of-fit-en-binomiaaltoets-R.html" title="Chi-kwadraat toets voor goodness of fit en binomiaaltoets">Chi-kwadraat toets voor goodness of fit en binomiaaltoets</a>
# </td>
# <td class="innercell published">
# <a href="12-McNemar-toets-R.html" title="McNemar toets">McNemar toets</a>
# </td>
# <td class="innercell published">
# <a href="13-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fishers-exacte-toets-R.html" title="Chi-kwadraat toets voor onafhankelijkheid en Fisher&#39;s exacte toets">Chi-kwadraat toets voor onafhankelijkheid en Fisher's exacte toets</a>
# </td>
# <td class="innercell published">
# <a href="15-Cochrans-Q-toets-R.html" title="Cochran&#39;s Q toets">Cochran's Q toets</a>
# </td>
# <td class="innercell published">
# <a href="16-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fisher-Freeman-Halton-exacte-toets-I-R.html" title="Chi-kwadraat toets voor onafhankelijkheid en Fisher-Freeman-Halton exacte toets I">Chi-kwadraat toets voor onafhankelijkheid en Fisher-Freeman-Halton exacte toets I</a>
# </td>
# </tr><tr>
# <td class="header3 innercell">
# nominaal 
# <br/>
# (&gt;2 waarden)
# </td>
# <td class="innercell published">
# <a href="21-Chi-kwadraat-toets-voor-goodness-of-fit-en-multinomiaaltoets-R.html" title="Chi-kwadraat toets voor goodness of fit en multinomiaaltoets">Chi-kwadraat toets voor goodness of fit en multinomiaaltoets</a>
# </td>
# <td class="innercell published">
# <a href="18-Bhapkar-toets-R.html" title="Bhapkar toets">Bhapkar toets</a>
# </td>
# <td class="innercell published">
# <a href="16-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fisher-Freeman-Halton-exacte-toets-I-R.html" title="Chi-kwadraat toets voor onafhankelijkheid en Fisher-Freeman-Halton exacte toets I">Chi-kwadraat toets voor onafhankelijkheid en Fisher-Freeman-Halton exacte toets I</a>
# </td>
# <td class="innercell published">
# <a href="20-Multilevel-multinomiale-logistische-regressie-R.html" title="Multilevel multinomiale logistische regressie">Multilevel multinomiale logistische regressie</a>
# </td>
# <td class="innercell published">
# <a href="16-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fisher-Freeman-Halton-exacte-toets-I-R.html" title="Chi-kwadraat toets voor onafhankelijkheid en Fisher-Freeman-Halton exacte toets I">Chi-kwadraat toets voor onafhankelijkheid en Fisher-Freeman-Halton exacte toets I</a>
# </td>
# </tr><tr>
# <td class="header3 innercell">ordinaal</td>
# <td class="innercell published">
# <a href="21-Chi-kwadraat-toets-voor-goodness-of-fit-en-multinomiaaltoets-R.html" title="Chi-kwadraat toets voor goodness of fit en multinomiaaltoets">Chi-kwadraat toets voor goodness of fit en multinomiaaltoets</a>
# </td>
# <td class="innercell published">
# <a href="22-Wilcoxon-signed-rank-toets-II-R.html" title="Wilcoxon signed rank toets II">Wilcoxon signed rank toets II</a>
# </td>
# <td class="innercell published">
# <a href="23-Mann-Whitney-U-toets-II-R.html" title="Mann-Whitney U toets II">Mann-Whitney U toets II</a>
# </td>
# <td class="innercell published">
# <a href="24-Friedmans-ANOVA-II-R.html" title="Friedman&#39;s ANOVA II">Friedman's ANOVA II</a>
# </td>
# <td class="innercell published">
# <a href="25-Kruskal-Wallis-toets-II-R.html" title="Kruskal Wallis toets II">Kruskal Wallis toets II</a>
# </td>
# </tr> <!-- Toestmatrix footer -->
#         <tr>
#             <td colspan=8>&nbsp;</td>
#         </tr>
#         <tr>
#             <td colspan=6>&nbsp;</td>
#             <td class="innercell published">Gereed</td>
#             <td class="innercell unpublished">Onder handen</td>
#         </tr>
#     </tbody>
# </table>
