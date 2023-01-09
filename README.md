#### NUME: Iustina-Andreea Caramida
#### GRUPA: 322CA

## Structura arhivei
    
    ├──graphics/
    │   ├── *.py - fișiere ce generează graficele cu rezultatele testelor
    │   ├── *.png - graficele generate
    │   ├── results.sh - script ce executa fisierele *.py și parsează rezultatele din directorul out într-un fișier .md pentru a putea fi copiate cu ușurință în fișierul latex
    │   ├── results.md - rezultatele parseate gata de a fi copiate într-un tabel din latex
    ├── in/
    │   ├── *.in - fișierele de intrare
    ├── out/
    │   ├── *.out - fișierele de ieșire - la finalul numelui, numărul indică rezultatul unui anumit algoritm :
    │   │   ├── 1 - Brute Force
    │   │   ├── 2 - Greedy
    │   │   ├── 3 - DSatur
    │   │   ├── 4 - RLF
    ├── src/
    │   ├── p1/ - primul algoritm
    │   ├── p2/ - al doilea algoritm
    │   ├── p3/ - al treilea algoritm
    │   ├── p4/ - al patrulea algoritm
    │   ├── statistics-p*.py - fișiere cu statisticile pentru fiecare algoritm (regulă de compilare: make statistics-p*)
    ├── README.md - fișierul curent
    ├── Makefile - fișier de compilare
    ├── 18.pdf - fișierul pdf cu descrierea temei

## Algoritmul cel mai eficient
Am ales algoritmul DSatur ca cel mai bun algoritm deoarece timpul său de execuție este relativ scurt și este cel mai exact algoritm în ceea ce privește rezultatele obținute.

'make run-best' rulează algoritmul cu număul 3 (DSatur)

## Generarea testelor
Generarea testelor am făcut-o cu ajutorul unui generator de grafuri de pe github: https://github.com/ifsmirnov/jngen. Nu am mai adăugat codul sursă al repository-ului deoarece este foarte mare și nu este necesar pentru rularea programului.

## Codul sursă
Fiecare algoritm este într-un director separat. Fiecare fișier ce conține câte un algoritm, la final conține un link către codul sursă de unde m-am inspirat pentru implementarea algoritmului.

## Generarea graficelor
Graficele au fost generate cu Python 3.6.5 și matplotlib 2.2.2.
Timpul de execuție al fiecărui algoritm a fost calculat cu ajutorul utilitarului hyperfine, care rulează un program de mai multe ori și calculează media timpului de execuție. Pentru fiecare algoritm, am rulat de 10 ori fiecare test și am luat media timpului de execuție pentru fiecare test. Aceste date au fost salvate în câte un fișier .md pentru fiecare algoritm și introduse în programele Pyton pentru generarea graficelor.