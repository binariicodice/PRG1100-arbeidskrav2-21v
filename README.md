<h1>PRG1100 Grunnleggende Programmering 2 - Arbeidskrav 2 - 2021 - USN Ringerike</h1>
  
<h2>Oppgave: system for håndtering av eksamen ved USN</h2>
Det skal programmeres et grafisk basert grensesnitt for applikasjonen og applikasjonen skal kjøre
mot en database i MySQL. Det skal lages en applikasjon for eksamenskontoret ved USN. Applikasjonen skal brukes til planlegging av eksamener og ajourhold av eksamensresultater for studentene. Det skal være mulig med ajourhold av studenter, eksamen og eksamensresultater. 

Det er følgende krav til den nye applikasjonen:
- kunne ajourholde framtidige eksamener og kontrollere at et rom bare settes opp med en eksamen pr dag
- utskrift/visning av alle eksamener på en dag, med informasjon om emne og rom
- utskrift/visning av alle eksamener i en periode, ordnet etter dato med informasjon om emne og rom
- registrere karakterer for en avholdt eksamen samlet
- utskrift/visning av alle eksamensresultater i et emne («karakterliste»), dvs alle studenter med oppnådd karakter ordnet etter studentnr
- utskrift/visning av karakterstatistikk for en gjennomført eksamen i et emne med emneopplysninger og en opptelling av antall kandidater på hver karakter («karakterfordeling»)
- utskrift av alle eksamensresultater med emnenavn og antall studiepoeng for en student (hvor en kan ha ett eller flere eksamensresultater i samme emne), ordnet etter eksamensdato
- utskrift av vitnemål for en student. Ved flere avlagte eksamener i samme emne skal kun ett/beste resultat komme på vitnemålet. Emnene sorteres på fagnivå og emnekode, dvs alle emnekoder i 1000-serien sorteres og kommer før alle emnekodene i 2000-serien osv. Vitnemålet må ha en summering av antall oppnådde studiepoeng for beståtte emner

<h2>Preview:</h2>

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/mainMenu.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/studentRegistrering.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/studentOppdatering.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/studentSletting.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/studentUtskrift.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/mysqlEksamensresultat.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/eksamenRegistrering.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/eksamenOppdatering.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/eksamenSletting.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/eksamenUtskrift.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/eksamenResultatRegistrering.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/eksamenResultatOppdatering.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/eksamenResultatSletting.png?raw=true)

![alt text](https://github.com/binariicodice/PRG1100-arbeidskrav2-21v/blob/main/eksamenResultatUtskrift.png?raw=true)
