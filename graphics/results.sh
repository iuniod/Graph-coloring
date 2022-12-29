#!/bin/bash

# Generarea graficelor
for i in $(seq 1 6)
do
	python3 fig"$i".py
done

# Generarea tabelului cu raspunsuri in functie de algoritm
touch results.md
header="| nr set | nr noduri + nr muchii | Brute Force | Greedy | DSatur | RLF |\n"
for i in $(seq 1 34)
do
	nm=$(head -n 1 ../in/test"$i".in)
	b=$(head -n 1 ../out/test"$i".out1)
	g=$(head -n 1 ../out/test"$i".out2)
	d=$(head -n 1 ../out/test"$i".out3)
	r=$(head -n 1 ../out/test"$i".out4)
	header+="textbf{$i} & $nm & - & $b & $g & $d & $r \ \hline \n"
done

printf "$header" > results.md
