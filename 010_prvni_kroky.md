Online zdroje
=======================

 * Velice zdařila komunitní stránka je <http://python.cz>. Najdete tu vše, co 
   začátečník potřebuje včetně diskusních skupin a chatu.
 
 * Rozcestník pro začátečníky najdete na <https://python.cz/zacatecnici/>.

 * <http://naucse.python.cz/>
    * [Začátečnický kurz](http://naucse.python.cz/course/pyladies/).
    * [Kurz pro pokročilé](http://naucse.python.cz/course/mi-pyt/).

 * Jako učebnici budeme používat knihu **Ponořme se do Pythonu 3**:
     - [HTML](http://diveintopython3.py.cz/index.html)
     - [... PDF a další formáty](https://knihy.nic.cz/#Python3)

 * Návody vytvořené u nás ve škole:
    - [grafické uživatelské rozhranní s PyQt4](http://spseol.github.io/PyQt4Doc/)
    - [Flask a Jinja2](http://spseol.github.io/CzechFlaskDoc/)
    - [Český manuál k MatPlotLib](http://mamut.spseol.cz/matplotlib/)

 * Komunita:
    - [Pyvec](http://pyvec.org/)
    - [Pyvo](https://pyvo.cz/)


Instalace
=======================

Budeme používat Python 3. Jeho instalátor si stáhnete z oficiálních stránek
<http://python.org/>. Stačí kliknout na [Downloads](https://www.python.org/downloads/).

Při instalaci zadejte **Install Launcher** a **Add Python to PATH**. 
Nainstalujte si i **pip**. Pokud nic nebudete měnit měl by se vám Python 
nainstalovat do *Program Files\Python36*

![](img/1.png)

![](img/2.png)

![](img/3.png)

Uživatelé OS **Linux** už mají nejspíš Python3 nainstalovaný. Pokud ne, stačí 
spustit něco jako 

    apt install pytho3 idle3 python3-tk python3-venv python3-pip 


Knihovny
===================

Pro naši výuku, práci a také pro naše pohodlí budeme potřebovat několik knihoven.
Ty se dají snadno spravovat -- tedy (od/na)instalovat pomocí nástroje 
[pip](https://pip.pypa.io/en/stable/). Takto se dají instalovat nejen knihovny,
ale i programy napsané v Pythonu.

Stačí otevřít příkazovou řádku:

![](img/4.png)

Knihovny pro matematické výpočte a vykreslování grafů jsou 
[NumPy][] a [Matplotlib][]:

    pip3 install numpy matplotlib

Pro interaktivní práci a psaní poznámek budeme potřebovat [IPython][] a
[Jupyter][]: 

    pip3 install ipython jupyter

Pro psaní zdrojového kódu se hodí vývojové prostředí [Spyder][]:

    pip3 install PyQt5
    pip3 install spyder

Pro vytváření webových stránek se hodí [Flask][]:

    pip3 install flask

Pro komunikaci s databázovým serverem [PostgreSQL][] se hodí [psycopg][]:

    pip3 install psycopg2


**Spustitelné soubory všech programů**, které jste si nainstalovali najdete
v adresáři *Program Files\Python 3.6\scripts*. Například

 * spyder3.exe
 * jupyter-notebook.exe
 * ... nebo tak nějak

[NumPy]: http://www.numpy.org/
[Matplotlib]: http://matplotlib.org
[Flask]: http://flask.pocoo.org/
[PostgreSQL]: http://postgres.cz/
[psycopg]: http://initd.org/psycopg/
[IPython]: http://ipython.org/
[Jupyter]: https://jupyter.org/
[Spyder]: https://pythonhosted.org/spyder/

V Linuxu by tento postup měl fungovat také, ale obecně není příliš dobré
přimíchat v ekosystému knihoven obsažených ve vaší distribuci knihovny přímo
staženými z up-streamu. Proto buď knihovny instalujte jen pro daného uživatele
použitím parametru `--user`

    pip3 install --user numpy matplotlib

... nebo se držte balíčků vaší distribuce

    apt install python3-numpy python3-matplotlib spyder3 ipython3 jupyter-qtconsole jupyter-notebook


... nebo tak nějak podobně.

Editory
====================

Základní instalace Pythonu už sama v sobě obsahuje jednoduché vývojové
prostředí a jednoduchou interaktivní konzolu IDLE. Toto prostředí je poměrně
jednoduché, ale rozhodně se nedá říct, že by se v něm nedalo pracovat. Existuje
ale celá řada 
[vývojových prostředí](https://cs.wikipedia.org/wiki/V%C3%BDvojov%C3%A9_prost%C5%99ed%C3%AD),
které nám mohou práci usnadnit a zpříjemnit. 
Z [dlouhého seznamu](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments) 
vybírám dvě.

Spyder
----------------

Jednoduchý, přehledný, dostačující. Obsahuje interaktivní konzolu.

    pip3 install PyQt5
    pip3 install spyder

<https://pythonhosted.org/spyder/>

PyCharm
------------------

[PyCharm]: https://www.jetbrains.com/pycharm/

[PyCharm][] je profesionální vývojové
prostředí. Je dostupný ve placené variantě *Professional* a v open-source
variantě *Community*. Jádro je stejné,
[ale](https://www.jetbrains.com/pycharm/features/editions_comparison_matrix.html)
profesionální verze obsahuje podporu různých technologií (nejen) pro vývoj
webu.

Studenti a učitelé mohou [PyCharm][] používat zdarma, ale jen pro výukové účely.

Notebook
=======================

    pip3 install ipython jupyter

Rád bych zde upozornil ještě na jeden velice užitečný nástroj. Tím je [Jupyter
notebook][Jupyter]. Umožňuje totiž velice efektivně propojit psaní textu,
poznámek a vkládání obrázků se zpravováním dat a  programováním v Pythonu.

Potom to může vypadat třeba takto:
  * [jedna](https://github.com/tlapicka/IPythonNotebooks/blob/master/Matplotlib--zakladni_myslenky_postupy.ipynb)
  * [dva](https://github.com/tlapicka/IPythonNotebooks/blob/master/Harmonicka_analyza--lichobeznik.ipynb)
  * [tři](https://github.com/tlapicka/IPythonNotebooks/blob/master/Aliasing.ipynb)


Git a GitHub
=========================

[Git]: https://cs.wikipedia.org/wiki/Git
[GitHub]: https://cs.wikipedia.org/wiki/GitHub

V naší výuce **budeme používat [Git][] a [GitHub][]**.

Vytvořte si prosím účet na GitHubu
------------------------------------

Tedy na stránkách, na kterých se právě nacházíte.
Stačí kliknout na [Sign up](https://github.com/join).

GitHub můžete používat zdarma. Platíte až za soukromé repositáře. Studenti mají
ale k dipozici celý balíček služeb zdarma. Podívejte se na
<http://education.github.com> a zažádejte si o [Student Developer
Pack](https://education.github.com/pack). Získáte tak soukromé repositáře
(které budeme potřebovat ve výuce) zdarma. 

Stojí také za to podívat se na <https://pages.github.com/>.

Naučte se základy systému Git
--------------------------------

Projděte se [rychlokurs](http://naucse.python.cz/lessons/git/basics/) a můžete
začít git používat.

Existuje volně šiřitelná kniha [Pro Git][] ve které najdete vše potřebné v
češtině. Lze číst i na webu: 
  * [první vydání](https://git-scm.com/book/cs/v1) -- celé v češtině
  * [druhé vydání](https://git-scm.com/book/cs/v2) -- není přeloženo celé;
    můžete se tedy [zapojit do překladu](https://github.com/pepr/progit2-cs).

Pro efektivní používaní tohoto skvělého nástroje vám stačí přečíst si **první tři
kapitoly**. Nenechte se tedy odradit, stojí to jistě za too.


[Pro Git]: https://knihy.nic.cz/#ProGit
