# TP THP by **Melzi Mounir** and **Guedda Fatima Zahraa** - 1CS G7

> **Dans ce TP on va transformer un automate d'états finis généralisé vers un automate d'états finis simple en passant par un automate d'états finis partiellement généralisé**

> ## Les types des automates d'états finis:
>
> > ### Généralisé:
> >
> > Un automate d'états finis généralisé est un 5-uplets **$A_{G}$ < $X^{*}$ , $S_{G}$ , $S_{0G}$ , $F_{G}$ , $I_{G}$ >** où:
> >
> > - **$X$** est l’alphabet d’entrée
> > - **$S_{G}$** est un ensemble fini d’états de l’automate
> > - **$S_{0G}$** est l’état initial $S_{0G} \in S_{G}$
> > - **$F_{G}$** est l’ensemble des états finaux $F_{G} \subseteq S_{G}$
> > - **$I_{G}$** est l’ensemble des instructions $I_{G} : S_{G}$ x $X^{*}$ &rarr; $P(S_{G})$
>
> > ### Partiellement Généralisé:
> >
> > Un automate d'états finis partiellement généralisé est un 5-uplets **$A_{PG}$ < $X \cup \{\epsilon\}$ , $S_{PG}$ , $S_{0PG}$ , $F_{PG}$ , $I_{PG}$ >** où:
> >
> > - **$X$** est l’alphabet d’entrée
> > - **$S_{PG}$** est un ensemble fini d’états de l’automate
> > - **$S_{0PG}$** est l’état initial $S_{0PG} \in S_{PG}$
> > - **$F_{PG}$** est l’ensemble des états finaux $F_{PG} \subseteq S_{PG}$
> > - **$I_{PG}$** est l’ensemble des instructions $I_{PG} : S_{PG}$ x $X \cup \{\epsilon\}$ &rarr; $P(S_{PG})$
>
> > ### Simple:
> >
> > Un automate d'états finis simple est un 5-uplets **$A$ < $X$ , $S$ , $S_{0}$ , $F$ , $I$ >** où:
> >
> > - **$X$** est l’alphabet d’entrée
> > - **$S$** est un ensemble fini d’états de l’automate
> > - **$S_{0}$** est l’état initial $S_{0} \in S$
> > - **$F$** est l’ensemble des états finaux $F \subseteq S$
> > - **$I$** est l’ensemble des instructions $I : S$ x $X$ &rarr; $S$

> ## Les étapes de la solution:
>
> 1. Définition de la structure d'un automate d'états finis en `python`.
> 2. Transformation de l'automate généralisé vers un automate partiellement généralisé en éliminant les transitions qui se font par un mot dont la longueur est supérieure ou égale à 2, par l'ajout des états intermédiaires.
> 3. Transformation de l'automate partiellement généralisé vers un automate simple en éliminant les transitions epsilon. Si on a ($S_{i}$, $\epsilon$, $S_{j}$), on applique ces 2 règles:
>    1. On va créer des transitions entre $S_{i}$ et tous les successeurs directes de $S_{j}$
>    2. Si $S_{j}$ est un état final dans $A$ alors $S_{i}$ devient un état final dans le nouvel automate construit
