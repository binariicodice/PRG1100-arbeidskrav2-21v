from tkinter import *
import mysql.connector
from datetime import date, datetime
import tkinter.ttk
from tkinter import messagebox

def registrere_student_GUI():
    def generer_studentnr():
        # Kode for å generere studentnr og student e-post:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        generer_snr_markor = mindatabase.cursor()
        generer_snr_markor.execute('SELECT Studentnr FROM Student')
        
        for row in generer_snr_markor:
            maks = max(row)
            nytt_snr = int(maks) + 1
            snr.set(nytt_snr)
            ep.set(str(nytt_snr) + '@usn.no')

        generer_snr_markor.close()
        mindatabase.close()
        
    def registrere_student():
        # Kode for å registrere student:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        registrer_markor = mindatabase.cursor()
        studentnr = int(snr.get())
        fornavn = fnavn.get()
        etternavn = enavn.get()
        epost = ep.get()
        telefon = tlf.get()

        settinn_student = ('INSERT INTO Student'
                        '(Studentnr, Fornavn, Etternavn, Epost, Telefon)'
                        'VALUES(%s, %s, %s, %s, %s)')
        datany_student = (studentnr, fornavn, etternavn, epost, telefon)
        registrer_markor.execute(settinn_student, datany_student)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Studenten er registrert')
        registrer_markor.close()
        mindatabase.close()

        
    # GUI student:
    registrere_student_vindu = Toplevel()
    registrere_student_vindu.title('Student (registrering)')
    registrere_student_vindu.resizable(FALSE, FALSE)
    registrere_student_vindu.geometry('480x350+600+200')

    overskrift = Label(registrere_student_vindu, text='Student registrering', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=4, padx=15, pady=5)
    forklaring_snr = Label(registrere_student_vindu, text='Trykk på lag studentnr for å hente nytt (ubrukt) studentnr (løpende nr)',  font=('Sans-Serif', '11'))
    forklaring_snr.grid(row=1, columnspan=4, padx=15, pady=(10, 30))

    lbl_studentnr = Label(registrere_student_vindu, text='Studentnr:')
    lbl_studentnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    lbl_fornavn = Label(registrere_student_vindu, text='Fornavn:')
    lbl_fornavn.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    lbl_etternavn = Label(registrere_student_vindu, text='Etternavn:')
    lbl_etternavn.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    lbl_epost = Label(registrere_student_vindu, text='Epost:')
    lbl_epost.grid(row=5, column=0, padx=5, pady=5, sticky=E)
    lbl_telefon = Label(registrere_student_vindu, text='Mobil:')
    lbl_telefon.grid(row=6, column=0, padx=5, pady=5, sticky=E)

    snr = StringVar()
    ent_snr = Entry(registrere_student_vindu, state='readonly', width=6, textvariable=snr)
    ent_snr.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    fnavn = StringVar()
    ent_fnavn = Entry(registrere_student_vindu, width=30, textvariable=fnavn)
    ent_fnavn.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    enavn = StringVar()
    ent_enavn = Entry(registrere_student_vindu, width=20, textvariable=enavn)
    ent_enavn.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    ep = StringVar()
    ent_ep = Entry(registrere_student_vindu, state='readonly', width=20, textvariable=ep)
    ent_ep.grid(row=5, column=1, padx=5, pady=5, sticky=W)
    tlf = StringVar()
    ent_tlf = Entry(registrere_student_vindu, width=8, textvariable=tlf)
    ent_tlf.grid(row=6, column=1, padx=5, pady=5, sticky=W)
    
    btn_sok = Button(registrere_student_vindu, text='Lag studentnr', command=generer_studentnr)
    btn_sok.grid(row=2, column=2, padx=5, pady=5, sticky=E)
    btn_lagre = Button(registrere_student_vindu, text='Registrer student', command=registrere_student)
    btn_lagre.grid(row=7, column=2, padx=5, pady=5, sticky=E)
    btn_tilbake2 = Button(registrere_student_vindu, text='Tilbake til meny', command=registrere_student_vindu.destroy)
    btn_tilbake2.grid(row=7, column=0, padx=15, pady=25, sticky=W)

def oppdatere_student_GUI():
    def sok_student():
        # Kode for å søke etter student:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        sok_markor = mindatabase.cursor()
        sok_markor.execute('SELECT * FROM Student')
        for row in sok_markor:
            if studentnr == row[0]:
                fnavn.set(row[1])
                enavn.set(row[2])
                ep.set(row[3])
                tlf.set(row[4])
        sok_markor.close()
        mindatabase.close()

    def oppdatere_student():
        # Kode for å oppdatere student:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        oppdatere_markor = mindatabase.cursor()

        studentnr = int(snr.get())
        fornavn = fnavn.get()
        etternavn = enavn.get()
        epost = ep.get()
        telefon = tlf.get()

        oppdater_student = ('Update Student SET Studentnr = %s, Fornavn = %s, Etternavn = %s, Epost = %s, Telefon = %s WHERE Studentnr = %s')
        data_ny_student = (studentnr, fornavn, etternavn, epost, telefon, studentnr,)
        oppdatere_markor.execute(oppdater_student, data_ny_student)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Studenten er oppdatert')
        oppdatere_markor.close()
        mindatabase.close()

    # GUI student:
    oppdatere_student_vindu = Toplevel()
    oppdatere_student_vindu.title('Student (oppdatering)')
    oppdatere_student_vindu.resizable(FALSE, FALSE)
    oppdatere_student_vindu.geometry('470x350+600+200')

    overskrift = Label(oppdatere_student_vindu, text='Student oppdatering', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=2, padx=15, pady=5)
    forklaring_sok = Label(oppdatere_student_vindu, text='Du kan søke på student ved å skrive inn studentnr og trykke SØK',  font=('Sans-Serif', '11'))
    forklaring_sok.grid(row=1, columnspan=2, padx=15, pady=(10, 30))

    lbl_studentnr = Label(oppdatere_student_vindu, text='Studentnr:')
    lbl_studentnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    lbl_fornavn = Label(oppdatere_student_vindu, text='Fornavn:')
    lbl_fornavn.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    lbl_etternavn = Label(oppdatere_student_vindu, text='Etternavn:')
    lbl_etternavn.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    lbl_epost = Label(oppdatere_student_vindu, text='Epost:')
    lbl_epost.grid(row=5, column=0, padx=5, pady=5, sticky=E)
    lbl_telefon = Label(oppdatere_student_vindu, text='Mobil:')
    lbl_telefon.grid(row=6, column=0, padx=5, pady=5, sticky=E)

    snr = StringVar()
    ent_snr = Entry(oppdatere_student_vindu, width=6, textvariable=snr)
    ent_snr.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    fnavn = StringVar()
    ent_fnavn = Entry(oppdatere_student_vindu, width=30, textvariable=fnavn)
    ent_fnavn.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    enavn = StringVar()
    ent_enavn = Entry(oppdatere_student_vindu, width=20, textvariable=enavn)
    ent_enavn.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    ep = StringVar()
    ent_ep = Entry(oppdatere_student_vindu, state='readonly', width=40, textvariable=ep)
    ent_ep.grid(row=5, column=1, padx=5, pady=5, sticky=W)
    tlf = StringVar()
    ent_tlf = Entry(oppdatere_student_vindu, width=8, textvariable=tlf)
    ent_tlf.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    btn_sok = Button(oppdatere_student_vindu, text='Søk', command=sok_student)
    btn_sok.grid(row=2, column=1, padx=5, pady=5, sticky=E)
    btn_lagre = Button(oppdatere_student_vindu, text='Oppdater student', command=oppdatere_student)
    btn_lagre.grid(row=7, column=1, padx=5, pady=5, sticky=E)
    btn_tilbake2 = Button(oppdatere_student_vindu, text='Tilbake til meny', command=oppdatere_student_vindu.destroy)
    btn_tilbake2.grid(row=7, column=0, padx=15, pady=25, sticky=W)

def slette_student_GUI():
    def sok_student():
        # Kode for å søke etter student:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        sok_markor = mindatabase.cursor()
        sok_markor.execute('SELECT * FROM Student')
        
        for row in sok_markor:
            if studentnr == row[0]:
                fnavn.set(row[1])
                enavn.set(row[2])
                ep.set(row[3])
                tlf.set(row[4])
        sok_markor.close()
        mindatabase.close()

    def slette_student():
        # Kode for å slette student:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        slette_markor = mindatabase.cursor()

        studentnr = snr.get()
        slett_vare = ('DELETE FROM Student WHERE Studentnr = %s AND Studentnr NOT IN (SELECT Studentnr FROM Eksamensresultat)')
        data_ny_student = (studentnr,)
        slette_markor.execute(slett_vare, data_ny_student)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Studenten er slettet')
        slette_markor.close()
        mindatabase.close()

    # GUI student:
    slette_student_vindu = Toplevel()
    slette_student_vindu.title('Student (sletting)')
    slette_student_vindu.resizable(FALSE, FALSE)
    slette_student_vindu.geometry('470x350+600+200')

    overskrift = Label(slette_student_vindu, text='Student sletting', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=3, padx=15, pady=5)
    forklaring_sok = Label(slette_student_vindu, text='Du kan søke på student ved å skrive inn studentnr og trykke SØK',  font=('Sans-Serif', '11'))
    forklaring_sok.grid(row=1, columnspan=2, padx=15, pady=(10, 30))

    lbl_studentnr = Label(slette_student_vindu, text='Studentnr:')
    lbl_studentnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    lbl_fornavn = Label(slette_student_vindu, text='Fornavn:')
    lbl_fornavn.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    lbl_etternavn = Label(slette_student_vindu, text='Etternavn:')
    lbl_etternavn.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    lbl_epost = Label(slette_student_vindu, text='Epost:')
    lbl_epost.grid(row=5, column=0, padx=5, pady=5, sticky=E)
    lbl_telefon = Label(slette_student_vindu, text='Mobil:')
    lbl_telefon.grid(row=6, column=0, padx=5, pady=5, sticky=E)

    snr = StringVar()
    ent_snr = Entry(slette_student_vindu, width=6, textvariable=snr)
    ent_snr.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    fnavn = StringVar()
    ent_fnavn = Entry(slette_student_vindu, state='readonly', width=30, textvariable=fnavn)
    ent_fnavn.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    enavn = StringVar()
    ent_enavn = Entry(slette_student_vindu, state='readonly', width=20, textvariable=enavn)
    ent_enavn.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    ep = StringVar()
    ent_ep = Entry(slette_student_vindu, state='readonly', width=40, textvariable=ep)
    ent_ep.grid(row=5, column=1, padx=5, pady=5, sticky=W)
    tlf = StringVar()
    ent_tlf = Entry(slette_student_vindu, state='readonly', width=8, textvariable=tlf)
    ent_tlf.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    btn_sok = Button(slette_student_vindu, text='Søk', command=sok_student)
    btn_sok.grid(row=2, column=1, padx=5, pady=5, sticky=E)
    btn_lagre = Button(slette_student_vindu, text='Slette student', command=slette_student)
    btn_lagre.grid(row=7, column=1, padx=5, pady=5, sticky=E)
    btn_tilbake2 = Button(slette_student_vindu, text='Tilbake til meny', command=slette_student_vindu.destroy)
    btn_tilbake2.grid(row=7, column=0, padx=15, pady=25, sticky=W)

def utskrift_eksamensresultater_student_GUI():
    def utskrift_alle_resultater():
        # Kode for utskrift alle resultater:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        utskrift_markor = mindatabase.cursor()
        utskrift_markor.execute('SELECT Eksamensresultat.*, Emnenavn, Studiepoeng FROM Eksamensresultat, Emne WHERE Eksamensresultat.Emnekode = Emne.Emnekode ORDER BY Dato ASC')
        
        data = utskrift_markor.fetchall()
        tekst_vindu.delete('1.0', END)
        totalt_snr = 0
        for row in data:
            if studentnr == row[0] and row[3] != None:
                tekst_vindu.insert(END, "Snr:" + str(row[0]) +" | " + "Emnek: " + str(row[1]) + " | " + "Dato: " + str(row[2]) + " | " + "Karakter: " + str(row[3])  + "\n" + "Emnenavn: " + str(row[4]) + " | " + "Studiepoeng: " + str(row[5]) + "\n" +"\n")
                totalt_snr += row[5] 
        totalt.set(totalt_snr)
        utskrift_markor.close()
        mindatabase.close()
    
    def utskrift_vitnemal():
        # Kode for utskrift av vitnemål:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        utskrift_markor = mindatabase.cursor()
        utskrift_markor.execute('SELECT Eksamensresultat.*, Emnenavn, Studiepoeng FROM Eksamensresultat, Emne WHERE Eksamensresultat.Emnekode = Emne.Emnekode AND Eksamensresultat.Karakter IS NOT NULL ORDER BY RIGHT (Eksamensresultat.Emnekode, 4) ASC')

        data = utskrift_markor.fetchall()
        tekst_vindu.delete('1.0', END)
        totalt_snr = 0
        for row in data:
            if studentnr == row[0]:
                tekst_vindu.insert(END, "Snr:" + str(row[0]) +" | " + "Emnek: " + str(row[1]) + " | " + "Dato: " + str(row[2]) + " | " + "Karakter: " + str(row[3])  + "\n" + "Emnenavn: " + str(row[4]) + " | " + "Studiepoeng: " + str(row[5]) + "\n" +"\n")
                totalt_snr += row[5]
        totalt.set(totalt_snr)
        utskrift_markor.close()
        mindatabase.close()

    # GUI utskrift student:
    utskrift_alle_resultater_vindu = Toplevel()
    utskrift_alle_resultater_vindu.title('Student (utskrift)')
    utskrift_alle_resultater_vindu.resizable(FALSE, FALSE)
    utskrift_alle_resultater_vindu.geometry('535x470+600+100')

    overskrift = Label(utskrift_alle_resultater_vindu, text='Eksamensresultater / Vitnemål', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=7, padx=15, pady=5)

    lbl_studentnr = Label(utskrift_alle_resultater_vindu, text='Studentnr:')
    lbl_studentnr.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    lbl_total_student_poeng = Label(utskrift_alle_resultater_vindu, text='Studentpoeng (totalt):')
    lbl_total_student_poeng.grid(row=1, column=3, padx=5, pady=5, sticky=E)
    
    snr = StringVar()
    ent_snr = Entry(utskrift_alle_resultater_vindu, width=6, textvariable=snr)
    ent_snr.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    totalt = StringVar()
    ent_totalt = Entry(utskrift_alle_resultater_vindu, state='readonly', width=5, textvariable=totalt)
    ent_totalt.grid(row=1, column=4, padx=5, pady=5, sticky=W)

    tekst_vindu = Text(utskrift_alle_resultater_vindu, width=65, height=20)
    tekst_vindu.grid(row=2, columnspan=5, padx=5, pady=5)

    btn_hent_data1 = Button(utskrift_alle_resultater_vindu, text='Hent alle resultater', command=utskrift_alle_resultater)
    btn_hent_data1.grid(row=4, column=3, padx=15, pady=5, sticky=SE)

    btn_hent_data2 = Button(utskrift_alle_resultater_vindu, text='Hent vitnemål', command=utskrift_vitnemal)
    btn_hent_data2.grid(row=4, column=4, padx=15, pady=5, sticky=SE)

    btn_tilbake2 = Button(utskrift_alle_resultater_vindu, text='Tilbake til meny', command=utskrift_alle_resultater_vindu.destroy)
    btn_tilbake2.grid(row=4, column=0, padx=15, pady=5, sticky=SW)

def registrere_eksamen_GUI():
    def sok_eksamen():
        # Kode for å søke etter eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        
        dato = date.get()
        sok_markor = mindatabase.cursor()
        sok_markor.execute('SELECT * FROM Eksamen')
        data = sok_markor.fetchall()
        lst_eksamen.delete('1.0', END)
        
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        for row in data:
            if dato_konvertert == row[1]:
                lst_eksamen.insert(END, "Romnr: " + str(row[2]) + " | OPPTATT" + '\n')
        sok_markor.close()
        mindatabase.close()

    def registrere_eksamen():
        # Kode for å registrere eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        
        emnekode = ek.get()
        dato = date.get()
        romnr = romn.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        registrer_eksamen_markor = mindatabase.cursor()
        sql = 'SELECT Eksamen.Dato,Eksamen.Romnr FROM Eksamen WHERE Eksamen.Dato = %s AND Eksamen.Romnr = %s'
        data_ny_eksamen = (dato_konvertert, romnr,)
        registrer_eksamen_markor.execute(sql, data_ny_eksamen)
        data = registrer_eksamen_markor.fetchall()
        if not data:
            settinn_eksamen = ('INSERT INTO Eksamen'
                            '(Emnekode, Dato, Romnr)'
                            'VALUES(%s, %s, %s)')
            datany_eksamen = (emnekode, dato_konvertert, romnr)
            registrer_eksamen_markor.execute(settinn_eksamen, datany_eksamen)
            mindatabase.commit()
            messagebox.showinfo('Info', 'Eksamen er registrert')
        if data:
            messagebox.showinfo('Info', 'Rommet er opptatt')

        registrer_eksamen_markor.close()
        mindatabase.close()
    # GUI registrere eksamen:
    registrere_eksamen_vindu = Toplevel()
    registrere_eksamen_vindu.title('Eksamen (registrering)')
    registrere_eksamen_vindu.resizable(FALSE, FALSE)
    registrere_eksamen_vindu.geometry('580x300+600+200')

    overskrift = Label(registrere_eksamen_vindu, text='Eksamen registrering', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=5, padx=15, pady=5)
    forklaring_sok = Label(registrere_eksamen_vindu, text='Du kan søke på dato for å se hvilke rom som er opptatt på ønsket dato',  font=('Sans-Serif', '11'))
    forklaring_sok.grid(row=1, columnspan=5, padx=15, pady=(10, 30))
    
    lst_eksamen = Text(registrere_eksamen_vindu, width=30, height=5)
    lst_eksamen.grid(row=2, column=2, rowspan=3, padx=5, pady=5, sticky=W)

    lbl_emndekode = Label(registrere_eksamen_vindu, text='Emnekode:')
    lbl_emndekode.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    lbl_dato = Label(registrere_eksamen_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    lbl_romnr = Label(registrere_eksamen_vindu, text='Romnr:')
    lbl_romnr.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    ek = StringVar()
    ent_ek = Entry(registrere_eksamen_vindu, width=8, textvariable=ek)
    ent_ek.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    date = StringVar()
    ent_date = Entry(registrere_eksamen_vindu, width=10, textvariable=date)
    ent_date.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    romn = StringVar()
    ent_romn = Entry(registrere_eksamen_vindu, width=4, textvariable=romn)
    ent_romn.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    
    btn_sok = Button(registrere_eksamen_vindu, text='Søk', command=sok_eksamen)
    btn_sok.grid(row=2, column=4, padx=5, pady=5, sticky=E)
    btn_lagre = Button(registrere_eksamen_vindu, text='Registrer eksamen', command=registrere_eksamen)
    btn_lagre.grid(row=7, column=4, padx=5, pady=25, sticky=E)
    btn_tilbake2 = Button(registrere_eksamen_vindu, text='Tilbake til meny', command=registrere_eksamen_vindu.destroy)
    btn_tilbake2.grid(row=7, column=0, padx=15, pady=25, sticky=W)
    
def oppdatere_eksamen_GUI():
    def sok_eksamen():
        # Kode for å søke etter eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        emnekode = ek.get()
        dato = date.get()
        sok_markor = mindatabase.cursor()
        sok_markor.execute('SELECT * FROM Eksamen')
        data = sok_markor.fetchall()
        if len(emnekode) != 0:
            dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
            for row in data:
                if emnekode == row[0] and dato_konvertert == row[1]:
                    ek.set(row[0])
                    date.set(row[1])
                    romn.set(row[2])
        sok_markor.close()
        mindatabase.close()

    def oppdatere_eksamen():
        # Kode for å oppdatere eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        oppdatere_markor = mindatabase.cursor()

        emnekode = ek.get()
        dato = date.get()
        romnr = romn.get()

        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        registrer_eksamen_markor = mindatabase.cursor()
        sql = 'SELECT Eksamen.Dato,Eksamen.Romnr FROM Eksamen WHERE Eksamen.Dato = %s AND Eksamen.Romnr = %s'
        data_ny_eksamen = (dato_konvertert, romnr,)
        registrer_eksamen_markor.execute(sql, data_ny_eksamen)
        data = registrer_eksamen_markor.fetchall()

        if not data:
            oppdater_eksamen = ('UPDATE Eksamen SET Emnekode = %s, Dato = %s, Romnr = %s WHERE Emnekode = %s AND Dato = %s')
            dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
            data_ny_eksamen = (emnekode, dato_konvertert, romnr, emnekode, dato_konvertert,)
            oppdatere_markor.execute(oppdater_eksamen, data_ny_eksamen)
            mindatabase.commit()
            messagebox.showinfo('Info', 'Eksamen er oppdatert')
        if data:
            messagebox.showinfo('Info', 'Rommet er opptatt')
        oppdatere_markor.close()
        mindatabase.close()

    # GUI oppdatere eksamen:
    oppdatere_eksamen_vindu = Toplevel()
    oppdatere_eksamen_vindu.title('Student (oppdatering)')
    oppdatere_eksamen_vindu.resizable(FALSE, FALSE)
    oppdatere_eksamen_vindu.geometry('540x280+600+200')

    overskrift = Label(oppdatere_eksamen_vindu, text='Eksamens oppdatering', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=3, padx=15, pady=5)
    forklaring_sok = Label(oppdatere_eksamen_vindu, text='Du kan søke på eksamen ved å skrive inn emnekode og dato og trykke SØK',  font=('Sans-Serif', '11'))
    forklaring_sok.grid(row=1, columnspan=3, padx=15, pady=(10, 30))

    lbl_emnekode = Label(oppdatere_eksamen_vindu, text='Emnekode:')
    lbl_emnekode.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    lbl_dato = Label(oppdatere_eksamen_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    lbl_romnr = Label(oppdatere_eksamen_vindu, text='Romnr:')
    lbl_romnr.grid(row=4, column=0, padx=5, pady=5, sticky=E)


    ek = StringVar()
    ent_ek = Entry(oppdatere_eksamen_vindu, width=8, textvariable=ek)
    ent_ek.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    date = StringVar()
    ent_date = Entry(oppdatere_eksamen_vindu, width=10, textvariable=date)
    ent_date.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    romn = StringVar()
    ent_romn = Entry(oppdatere_eksamen_vindu, width=4, textvariable=romn)
    ent_romn.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    btn_sok = Button(oppdatere_eksamen_vindu, text='Søk', command=sok_eksamen)
    btn_sok.grid(row=2, column=2, padx=5, pady=5, sticky=E)
    btn_lagre = Button(oppdatere_eksamen_vindu, text='Oppdater eksamen', command=oppdatere_eksamen)
    btn_lagre.grid(row=5, column=2, padx=5, pady=5, sticky=E)
    btn_tilbake2 = Button(oppdatere_eksamen_vindu, text='Tilbake til meny', command=oppdatere_eksamen_vindu.destroy)
    btn_tilbake2.grid(row=5, column=0, padx=15, pady=25, sticky=W)

def slette_eksamen_GUI():
    def sok_eksamen():
        # Kode for å søke etter eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
    
        emnekode = ek.get()
        dato = date.get()
        sok_markor = mindatabase.cursor()
        sok_markor.execute('SELECT * FROM Eksamen')
        data = sok_markor.fetchall()
        if len(emnekode) != 0:
            dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
            for row in data:
                if emnekode == row[0] and dato_konvertert == row[1]:
                    ek.set(row[0])
                    date.set(row[1])
                    romn.set(row[2])
        sok_markor.close()
        mindatabase.close()  
    def slett_eksamen():
        # Kode for å slette eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        slette_markor = mindatabase.cursor()

        emnekode = ek.get()
        dato = date.get()
        slett_vare = ('DELETE FROM Eksamen WHERE Emnekode = %s AND Dato = %s AND Emnekode NOT IN (SELECT Emnekode FROM Eksamensresultat)')
        data_ny_student = (emnekode, dato,)
        slette_markor.execute(slett_vare, data_ny_student)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Eksamen er slettet')
        slette_markor.close()
        mindatabase.close()

    # GUI slette eksamen:
    oppdatere_eksamen_vindu = Toplevel()
    oppdatere_eksamen_vindu.title('Student (oppdatering)')
    oppdatere_eksamen_vindu.resizable(FALSE, FALSE)
    oppdatere_eksamen_vindu.geometry('540x310+600+200')

    overskrift = Label(oppdatere_eksamen_vindu, text='Eksamens sletting', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=3, padx=15, pady=5)
    forklaring_sok = Label(oppdatere_eksamen_vindu, text='Du kan søke på eksamen ved å skrive inn emnekode og dato og trykke SØK',  font=('Sans-Serif', '11'))
    forklaring_sok.grid(row=1, columnspan=3, padx=15, pady=5)
    forklaring_sok2 = Label(oppdatere_eksamen_vindu, text='Eksamen blir kun slettet hvis det ikke er noen resultater registrert',  font=('Sans-Serif', '11'))
    forklaring_sok2.grid(row=2, columnspan=3, padx=15, pady=(5, 30))

    lbl_emnekode = Label(oppdatere_eksamen_vindu, text='Emnekode:')
    lbl_emnekode.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    lbl_dato = Label(oppdatere_eksamen_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    lbl_romnr = Label(oppdatere_eksamen_vindu, text='Romnr:')
    lbl_romnr.grid(row=5, column=0, padx=5, pady=5, sticky=E)


    ek = StringVar()
    ent_ek = Entry(oppdatere_eksamen_vindu, width=8, textvariable=ek)
    ent_ek.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    date = StringVar()
    ent_date = Entry(oppdatere_eksamen_vindu, width=10, textvariable=date)
    ent_date.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    romn = StringVar()
    ent_romn = Entry(oppdatere_eksamen_vindu, width=4, textvariable=romn)
    ent_romn.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    btn_sok = Button(oppdatere_eksamen_vindu, text='Søk', command=sok_eksamen)
    btn_sok.grid(row=3, column=2, padx=5, pady=5, sticky=E)
    btn_lagre = Button(oppdatere_eksamen_vindu, text='Slett eksamen', command=slett_eksamen)
    btn_lagre.grid(row=6, column=2, padx=5, pady=5, sticky=E)
    btn_tilbake2 = Button(oppdatere_eksamen_vindu, text='Tilbake til meny', command=oppdatere_eksamen_vindu.destroy)
    btn_tilbake2.grid(row=6, column=0, padx=15, pady=25, sticky=W)

def utskrift_eksamen_GUI():
    def alle_eksamen_en_dag():
        # Kode for utskrift av alle eksamner på en dag:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        dato_fra = date_from.get()
        utskrift_markor = mindatabase.cursor()
        utskrift_markor.execute('SELECT * FROM Eksamen')
        dato_konvertert = datetime.strptime(dato_fra, '%Y-%m-%d').date()
        data = utskrift_markor.fetchall()
        tekst_vindu.delete('1.0', END)
        
        for row in data:
            if dato_konvertert == row[1]:
                tekst_vindu.insert(END, "Emnekode: " + str(row[0]) + " | " + "Rom: " + str(row[2]) + "\n")
        utskrift_markor.close()
        mindatabase.close()
    
    def alle_eksamen_periode():
        # Kode for utskrift av alle eksamener innen for en periode, sortert etter dato:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        dato_fra = date_from.get()
        dato_til = date_to.get()
        dato_konvertert = datetime.strptime(dato_fra, '%Y-%m-%d').date()
        dato_konvertert2 = datetime.strptime(dato_til, '%Y-%m-%d').date()
        utskrift_markor = mindatabase.cursor()
        sql = 'SELECT * FROM Eksamen WHERE Dato >= %s AND Dato <= %s ORDER BY Dato'
        data_dato = (dato_konvertert, dato_konvertert2,)
        utskrift_markor.execute(sql, data_dato)
        data = utskrift_markor.fetchall()
        tekst_vindu.delete('1.0', END)
        for row in data:
            tekst_vindu.insert(END, "Emnekode: " + str(row[0]) + " | " + "Dato: " + str(row[1]) + " | " + "Rom: " + str(row[2]) + "\n")

    # GUI utskrift eksamen:
    utskrift_eksamen_vindu = Toplevel()
    utskrift_eksamen_vindu.title('Eksamen (utskrift)')
    utskrift_eksamen_vindu.resizable(FALSE, FALSE)
    utskrift_eksamen_vindu.geometry('535x530+600+100')

    overskrift = Label(utskrift_eksamen_vindu, text='Eksamens utskrift', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=7, padx=15, pady=5)
    forklaring_utskrift = Label(utskrift_eksamen_vindu, text='Hvis du ønsker å søke på kun en dag så fyll inn ønsket dato i dato (fra)',  font=('Sans-Serif', '11'))
    forklaring_utskrift.grid(row=1, columnspan=7, padx=15, pady=(10, 30))

    lbl_studentnr = Label(utskrift_eksamen_vindu, text='Dato (yyyy-mm-dd):')
    lbl_studentnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    lbl_total_student_poeng = Label(utskrift_eksamen_vindu, text='Dato (yyyy-mm-dd):')
    lbl_total_student_poeng.grid(row=2, column=3, padx=5, pady=5, sticky=E)
    
    date_from = StringVar()
    ent_date = Entry(utskrift_eksamen_vindu, width=10, textvariable=date_from)
    ent_date.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    date_to = StringVar()
    ent_totalt = Entry(utskrift_eksamen_vindu, width=10, textvariable=date_to)
    ent_totalt.grid(row=2, column=4, padx=5, pady=5, sticky=W)

    tekst_vindu = Text(utskrift_eksamen_vindu, width=65, height=20)
    tekst_vindu.grid(row=3, columnspan=5, padx=5, pady=5)

    btn_hent_data1 = Button(utskrift_eksamen_vindu, text='Hent data (1 dag)', command=alle_eksamen_en_dag)
    btn_hent_data1.grid(row=4, column=3, padx=15, pady=5, sticky=SE)

    btn_hent_data2 = Button(utskrift_eksamen_vindu, text='Hent data (periode)', command=alle_eksamen_periode)
    btn_hent_data2.grid(row=4, column=4, padx=15, pady=5, sticky=SE)

    btn_tilbake2 = Button(utskrift_eksamen_vindu, text='Tilbake til meny', command=utskrift_eksamen_vindu.destroy)
    btn_tilbake2.grid(row=4, column=0, padx=15, pady=5, sticky=SW) 

def registrere_eksamensresultat_GUI():
    def sok_en_eksamen():
        # Søke etter oppsatt eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        emnekode = sok_ek.get()
        dato = sok_date.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        markor.execute('SELECT * FROM Eksamen')
        data = markor.fetchall()
        for row in data:
            if emnekode == row[0] and dato_konvertert == row[1]:
                ek.set(row[0])
                date.set(row[1])
        markor.close()
        mindatabase.close()

    def registrer_en_karakter():
        # Registrere en enkel karakter:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        emnekode = ek.get()
        dato = date.get()
        karakter = grade.get()
        if karakter == '':
            karakter = None
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        sett_inn_karakter = ('INSERT INTO Eksamensresultat'
                            '(Studentnr, Emnekode, Dato, Karakter)'
                            'VALUES(%s, %s, %s, %s)')
        data_ny_eksamen = (studentnr, emnekode, dato_konvertert, karakter)
        markor.execute(sett_inn_karakter, data_ny_eksamen)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Eksamenskarakteren er registrert')
        markor.close()
        mindatabase.close()


    def sok_eksamensresultat():
        # Hente frem alle studenter for å kunne masse registrere eksamensresultat:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        markor = mindatabase.cursor()
        markor.execute('SELECT * FROM Student')
        data = markor.fetchall()
        eksamen_pa_dato = []
        for row in data:
            eksamen_pa_dato += [row[0]]
        innhold_eksamensresultat.set(tuple(eksamen_pa_dato))
        markor.close()
        mindatabase.close()

    def sok_en_eksamen2():
        # Hente frem ønsket eksamen for å kunne masse registrere eksamensresultat:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        emnekode = sok_ek2.get()
        dato = sok_date2.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        markor.execute('SELECT * FROM Eksamen')
        data = markor.fetchall()
        for row in data:
            if emnekode == row[0] and dato_konvertert == row[1]:
                ek2.set(row[0])
                date2.set(row[1])
        markor.close()
        mindatabase.close()

    def hente_student_eksamensresultat(handling):
        # Koble resultatet fra student listen med set'er til masseregistrering for å gjøre det enklere å masseregistrere:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        valgt = liste_eksamen.get(liste_eksamen.curselection())
        markor = mindatabase.cursor()
        markor.execute('SELECT * FROM Student')
        data = markor.fetchall()
        for row in data:
            if valgt == row[0]:
                snr2.set(row[0])
        markor.close()
        mindatabase.close()

    def registrer_eksamensresultat_mengde():
        # Kode for å registrere hver enkelt student under masseregistrering:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr2.get()
        emnekode = ek2.get()
        dato = date2.get()
        karakter = grade3.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        sett_inn_karakter = ('INSERT INTO Eksamensresultat'
                            '(Studentnr, Emnekode, Dato, Karakter)'
                            'VALUES(%s, %s, %s, %s)')
        data_ny_eksamen = (studentnr, emnekode, dato_konvertert, karakter)
        markor.execute(sett_inn_karakter, data_ny_eksamen)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Eksamenskarakteren er registrert')
        markor.close()
        mindatabase.close()

    # GUI registrere eksamensresultat:
    registrer_eksamensresultat_vindu = Toplevel()
    registrer_eksamensresultat_vindu.title('Eksamensresultat (registrering)')
    registrer_eksamensresultat_vindu.resizable(FALSE, FALSE)
    registrer_eksamensresultat_vindu.geometry('478x755+600+10')

    overskrift = Label(registrer_eksamensresultat_vindu, text='Eksamensresultat registrering', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=5, padx=15, pady=5)
    forklaring_sok = Label(registrer_eksamensresultat_vindu, text='Skriv inn emnekode og dato for å søke på eksamen',  font=('Sans-Serif', '11'))
    forklaring_sok.grid(row=1, columnspan=5, padx=15, pady=(10, 30))

    btn_sok = Button(registrer_eksamensresultat_vindu, text='Søk eksamen', command=sok_en_eksamen)
    btn_sok.grid(row=2, column=4, padx=5, pady=5, sticky=E)

    lbl_sok_emnekode = Label(registrer_eksamensresultat_vindu, text='Emnekode:')
    lbl_sok_emnekode.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    sok_ek = StringVar()
    ent_ek = Entry(registrer_eksamensresultat_vindu, width=8, textvariable=sok_ek)
    ent_ek.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    lbl_sok_dato = Label(registrer_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_sok_dato.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    sok_date = StringVar()
    ent_sok_date = Entry(registrer_eksamensresultat_vindu, width=10, textvariable=sok_date)
    ent_sok_date.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    tkinter.ttk.Separator(registrer_eksamensresultat_vindu, orient=HORIZONTAL).grid(row=4, columnspan=5, pady=10, sticky='WE')

    lbl_studentnr = Label(registrer_eksamensresultat_vindu, text='Studentnr:')
    lbl_studentnr.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    snr = StringVar()
    ent_snr = Entry(registrer_eksamensresultat_vindu, width=6, textvariable=snr)
    ent_snr.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    lbl_emnekode = Label(registrer_eksamensresultat_vindu, text='Emnekode:')
    lbl_emnekode.grid(row=6, column=0, padx=5, pady=5, sticky=E)

    ek = StringVar()
    ent_ek = Entry(registrer_eksamensresultat_vindu, state='readonly', width=8, textvariable=ek)
    ent_ek.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    lbl_dato = Label(registrer_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato.grid(row=7, column=0, padx=5, pady=5, sticky=E)

    date = StringVar()
    ent_date = Entry(registrer_eksamensresultat_vindu, state='readonly', width=10, textvariable=date)
    ent_date.grid(row=7, column=1, padx=5, pady=5, sticky=W)

    lbl_karakter = Label(registrer_eksamensresultat_vindu, text='Karakter:')
    lbl_karakter.grid(row=8, column=0, padx=5, pady=5, sticky=E)

    grade = StringVar()
    ent_grade = Entry(registrer_eksamensresultat_vindu, width=6, textvariable=grade)
    ent_grade.grid(row=8, column=1, padx=5, pady=5, sticky=W)
 
    btn_registrer_eksamen = Button(registrer_eksamensresultat_vindu, text='Registrer eksamensresultat', command=registrer_en_karakter)
    btn_registrer_eksamen.grid(row=9, column=4, padx=5, pady=5, sticky=E)

    tkinter.ttk.Separator(registrer_eksamensresultat_vindu, orient=HORIZONTAL).grid(row=10, columnspan=5, pady=10, sticky='WE')

    forklaring_sok2 = Label(registrer_eksamensresultat_vindu, text='Skriv inn emnekode og dato for å hente eksamens info',  font=('Sans-Serif', '11'))
    forklaring_sok2.grid(row=11, columnspan=5, padx=15, pady=5)

    forklaring_sok3 = Label(registrer_eksamensresultat_vindu, text='Trykk på hent studenter for å hente studentnr',  font=('Sans-Serif', '11'))
    forklaring_sok3.grid(row=12, columnspan=5, padx=15, pady=(0, 30))

    btn_sok2 = Button(registrer_eksamensresultat_vindu, text='Søk eksamen', command=sok_en_eksamen2)
    btn_sok2.grid(row=13, column=4, padx=5, pady=5, sticky=E)

    lbl_sok_emnekode2 = Label(registrer_eksamensresultat_vindu, text='Emnekode:')
    lbl_sok_emnekode2.grid(row=13, column=0, padx=5, pady=5, sticky=E)

    sok_ek2 = StringVar()
    ent_ek2 = Entry(registrer_eksamensresultat_vindu, width=8, textvariable=sok_ek2)
    ent_ek2.grid(row=13, column=1, padx=5, pady=5, sticky=W)

    lbl_sok_dato2 = Label(registrer_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_sok_dato2.grid(row=14, column=0, padx=5, pady=5, sticky=E)

    sok_date2 = StringVar()
    ent_sok_date2 = Entry(registrer_eksamensresultat_vindu, width=10, textvariable=sok_date2)
    ent_sok_date2.grid(row=14, column=1, padx=5, pady=5, sticky=W)

    tkinter.ttk.Separator(registrer_eksamensresultat_vindu, orient=HORIZONTAL).grid(row=15, columnspan=5, pady=10, sticky='WE')

    btn_sok3 = Button(registrer_eksamensresultat_vindu, text='Hent studenter', command=sok_eksamensresultat)
    btn_sok3.grid(row=16, column=4, padx=5, pady=5, sticky=E)

    lbl_studentnr2 = Label(registrer_eksamensresultat_vindu, text='Studentnr:')
    lbl_studentnr2.grid(row=16, column=0, padx=5, pady=5, sticky=E)

    snr2 = StringVar()
    ent_snr2 = Entry(registrer_eksamensresultat_vindu, width=6, textvariable=snr2)
    ent_snr2.grid(row=16, column=1, padx=5, pady=5, sticky=W)

    y_scroll = Scrollbar(registrer_eksamensresultat_vindu, orient=VERTICAL)
    y_scroll.grid(row=16, rowspan=4, column=2,  padx=(100, 0), pady=5, sticky=NS)

    innhold_eksamensresultat = StringVar()
    liste_eksamen = Listbox(registrer_eksamensresultat_vindu, width=15, height=7, listvariable=innhold_eksamensresultat, yscrollcommand=y_scroll.set)
    liste_eksamen.grid(row=16, rowspan=4, column=2, padx=5, pady=5)
    y_scroll['command'] = liste_eksamen.yview 

    lbl_emnekode2 = Label(registrer_eksamensresultat_vindu, text='Emnekode:')
    lbl_emnekode2.grid(row=17, column=0, padx=5, pady=5, sticky=E)

    ek2 = StringVar()
    ent_ek2 = Entry(registrer_eksamensresultat_vindu, width=8, textvariable=ek2)
    ent_ek2.grid(row=17, column=1, padx=5, pady=5, sticky=W)

    lbl_dato2 = Label(registrer_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato2.grid(row=18, column=0, padx=5, pady=5, sticky=E)

    date2 = StringVar()
    ent_date2 = Entry(registrer_eksamensresultat_vindu, width=10, textvariable=date2)
    ent_date2.grid(row=18, column=1, padx=5, pady=5, sticky=W)

    lbl_karakter2 = Label(registrer_eksamensresultat_vindu, text='Karakter:')
    lbl_karakter2.grid(row=19, column=0, padx=5, pady=5, sticky=E)

    grade3 = StringVar()
    ent_grade = Entry(registrer_eksamensresultat_vindu, width=6, textvariable=grade3)
    ent_grade.grid(row=19, column=1, padx=5, pady=5, sticky=W)

    btn_slett2 = Button(registrer_eksamensresultat_vindu, text='Registrer eksamensresultat', command=registrer_eksamensresultat_mengde)
    btn_slett2.grid(row=20, column=4, padx=5, pady=5, sticky=E)

    btn_tilbake = Button(registrer_eksamensresultat_vindu, text='Tilbake til meny', command=registrer_eksamensresultat_vindu.destroy)
    btn_tilbake.grid(row=20, column=0, padx=15, pady=25, sticky=W)

    liste_eksamen.bind('<<ListboxSelect>>', hente_student_eksamensresultat)

def oppdatere_eksamensresultat_GUI():
    def sok_en_karakter():
        # Kode for å søke etter karakter:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        emnekode = ek.get()
        dato = date.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        markor.execute('SELECT * FROM Eksamensresultat')
        data = markor.fetchall()
        for row in data:
            if studentnr == row[0] and emnekode == row[1] and dato_konvertert == row[2]:
                grade.set(row[3])
        markor.close()
        mindatabase.close()
        
    def oppdatere_en_karakter():
        # Kode for å oppdatere karakter:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        emnekode = ek.get()
        dato = date.get()
        karakter = grade2.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        endre_karakter = ('Update Eksamensresultat SET Karakter = %s WHERE Studentnr = %s AND Emnekode = %s AND Dato = %s')
        data_ny_karakter = (karakter, studentnr, emnekode, dato_konvertert,)
        markor.execute(endre_karakter, data_ny_karakter)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Eksamenskarakteren er oppdatert')
        markor.close()
        mindatabase.close()


    def sok_eksamensresultat():
        # Kode for å hente frem studenter med eksamensresultat innenfor en eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        emnekode = ek2.get()
        dato = date2.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        sql = 'SELECT Studentnr, Emnekode, Dato, Karakter FROM Eksamensresultat WHERE Emnekode = %s AND Dato = %s'
        data_eksamen = (emnekode, dato_konvertert,)
        markor.execute(sql, data_eksamen)
        data = markor.fetchall()
        studenter = []
        for row in data:
            studenter += [row[0]]
        innhold_eksamensresultat.set(tuple(studenter))
        markor.close()
        mindatabase.close()
        
    def hente_student_eksamensresultat(handling):
        # Koble valget fra student listen sammen med set'er boksene:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        valgt = liste_eksamen.get(liste_eksamen.curselection())
        emnekode = ek2.get()
        dato = date2.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        markor.execute('SELECT * FROM Eksamensresultat')
        data = markor.fetchall()
        for row in data:
            if valgt == row[0] and emnekode == row[1] and dato_konvertert == row[2]:
                snr2.set(row[0])
                ek2.set(row[1])
                date2.set(row[2])
                grade3.set(row[3])
        markor.close()
        mindatabase.close()

    def oppdater_eksamensresultat_mengde():
        # Utføre oppdatering av karakter:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr2.get()
        emnekode = ek2.get()
        dato = date2.get()
        karakter = grade4.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        endre_karakter = ('Update Eksamensresultat SET Karakter = %s WHERE Studentnr = %s AND Emnekode = %s AND Dato = %s')
        data_ny_karakter = (karakter, studentnr, emnekode, dato_konvertert,)
        markor.execute(endre_karakter, data_ny_karakter)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Eksamenskarakteren er oppdatert')
        markor.close()
        mindatabase.close()

    # GUI oppdatere eksamensresultat:
    oppdater_eksamensresultat_vindu = Toplevel()
    oppdater_eksamensresultat_vindu.title('Eksamensresultat (oppdatering)')
    oppdater_eksamensresultat_vindu.resizable(FALSE, FALSE)
    oppdater_eksamensresultat_vindu.geometry('478x620+600+100')

    overskrift = Label(oppdater_eksamensresultat_vindu, text='Eksamensresultat oppdatering', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=4, padx=15, pady=5)
    forklaring_sok = Label(oppdater_eksamensresultat_vindu, text='Skriv inn studentnr, emnekode og dato for å søke på student',  font=('Sans-Serif', '11'))
    forklaring_sok.grid(row=1, columnspan=4, padx=15, pady=(10, 30))

    btn_sok = Button(oppdater_eksamensresultat_vindu, text='Søk student', command=sok_en_karakter)
    btn_sok.grid(row=2, column=3, padx=5, pady=5, sticky=E)

    lbl_studentnr = Label(oppdater_eksamensresultat_vindu, text='Studentnr:')
    lbl_studentnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    snr = StringVar()
    ent_snr = Entry(oppdater_eksamensresultat_vindu, width=6, textvariable=snr)
    ent_snr.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    lbl_emnekode = Label(oppdater_eksamensresultat_vindu, text='Emnekode:')
    lbl_emnekode.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    ek = StringVar()
    ent_ek = Entry(oppdater_eksamensresultat_vindu, width=8, textvariable=ek)
    ent_ek.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    lbl_dato = Label(oppdater_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    date = StringVar()
    ent_date = Entry(oppdater_eksamensresultat_vindu, width=10, textvariable=date)
    ent_date.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    lbl_karakter = Label(oppdater_eksamensresultat_vindu, text='Karakter:')
    lbl_karakter.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    grade = StringVar()
    ent_grade = Entry(oppdater_eksamensresultat_vindu, state='readonly', width=6, textvariable=grade)
    ent_grade.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    lbl_ny_karakter = Label(oppdater_eksamensresultat_vindu, text='Ny karakter:')
    lbl_ny_karakter.grid(row=6, column=0, padx=5, pady=5, sticky=E)

    grade2 = StringVar()
    ent_grade2 = Entry(oppdater_eksamensresultat_vindu, width=6, textvariable=grade2)
    ent_grade2.grid(row=6, column=1, padx=5, pady=5, sticky=W)
 
    btn_lagre = Button(oppdater_eksamensresultat_vindu, text='Oppdater eksamensresultat', command=oppdatere_en_karakter)
    btn_lagre.grid(row=7, column=3, padx=5, pady=5, sticky=E)

    tkinter.ttk.Separator(oppdater_eksamensresultat_vindu, orient=HORIZONTAL).grid(row=8, columnspan=4, pady=10, sticky='WE')

    forklaring_sok2 = Label(oppdater_eksamensresultat_vindu, text='Skriv inn emnekode og dato for å søke på eksamen',  font=('Sans-Serif', '11'))
    forklaring_sok2.grid(row=9, columnspan=4, padx=15, pady=(10, 30))
    
    btn_sok2 = Button(oppdater_eksamensresultat_vindu, text='Søk eksamen', command=sok_eksamensresultat)
    btn_sok2.grid(row=10, column=3, padx=5, pady=5, sticky=E)

    lbl_studentnr2 = Label(oppdater_eksamensresultat_vindu, text='Studentnr:')
    lbl_studentnr2.grid(row=10, column=0, padx=5, pady=5, sticky=E)

    snr2 = StringVar()
    ent_snr2 = Entry(oppdater_eksamensresultat_vindu, state='readonly', width=6, textvariable=snr2)
    ent_snr2.grid(row=10, column=1, padx=5, pady=5, sticky=W)

    y_scroll = Scrollbar(oppdater_eksamensresultat_vindu, orient=VERTICAL)
    y_scroll.grid(row=10, rowspan=4, column=2,  padx=(100, 0), pady=5, sticky=NS)

    innhold_eksamensresultat = StringVar()
    liste_eksamen = Listbox(oppdater_eksamensresultat_vindu, width=15, height=7, listvariable=innhold_eksamensresultat, yscrollcommand=y_scroll.set)
    liste_eksamen.grid(row=10, rowspan=4, column=2, padx=5, pady=5)
    y_scroll['command'] = liste_eksamen.yview 

    lbl_emnekode2 = Label(oppdater_eksamensresultat_vindu, text='Emnekode:')
    lbl_emnekode2.grid(row=11, column=0, padx=5, pady=5, sticky=E)

    ek2 = StringVar()
    ent_ek2 = Entry(oppdater_eksamensresultat_vindu, width=8, textvariable=ek2)
    ent_ek2.grid(row=11, column=1, padx=5, pady=5, sticky=W)

    lbl_dato2 = Label(oppdater_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato2.grid(row=12, column=0, padx=5, pady=5, sticky=E)

    date2 = StringVar()
    ent_date2 = Entry(oppdater_eksamensresultat_vindu, width=10, textvariable=date2)
    ent_date2.grid(row=12, column=1, padx=5, pady=5, sticky=W)

    lbl_karakter2 = Label(oppdater_eksamensresultat_vindu, text='Karakter:')
    lbl_karakter2.grid(row=13, column=0, padx=5, pady=5, sticky=E)

    grade3 = StringVar()
    ent_grade2 = Entry(oppdater_eksamensresultat_vindu, state='readonly', width=6, textvariable=grade3)
    ent_grade2.grid(row=13, column=1, padx=5, pady=5, sticky=W)

    lbl_ny_karakter2 = Label(oppdater_eksamensresultat_vindu, text='Ny karakter:')
    lbl_ny_karakter2.grid(row=14, column=0, padx=5, pady=5, sticky=E)

    grade4 = StringVar()
    ent_grade3 = Entry(oppdater_eksamensresultat_vindu, width=6, textvariable=grade4)
    ent_grade3.grid(row=14, column=1, padx=5, pady=5, sticky=W)

    btn_lagre2 = Button(oppdater_eksamensresultat_vindu, text='Oppdater eksamensresultat', command=oppdater_eksamensresultat_mengde)
    btn_lagre2.grid(row=15, column=3, padx=5, pady=5, sticky=E)

    btn_tilbake = Button(oppdater_eksamensresultat_vindu, text='Tilbake til meny', command=oppdater_eksamensresultat_vindu.destroy)
    btn_tilbake.grid(row=15, column=0, padx=15, pady=25, sticky=W)

    liste_eksamen.bind('<<ListboxSelect>>', hente_student_eksamensresultat)

def slette_eksamensresultat_GUI():
    def sok_en_karakter():
        # Kode for å søke på karakter:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        emnekode = ek.get()
        dato = date.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        markor.execute('SELECT * FROM Eksamensresultat')
        data = markor.fetchall()
        for row in data:
            if studentnr == row[0] and emnekode == row[1] and dato_konvertert == row[2]:
                grade.set(row[3])
        markor.close()
        mindatabase.close()
    
    def slette_en_karakter():
        # Kode for å slette karakter:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr.get()
        emnekode = ek.get()
        dato = date.get()
        karakter = grade.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        endre_karakter = ('DELETE FROM Eksamensresultat WHERE Studentnr = %s AND Emnekode = %s AND Dato = %s AND Karakter = %s')
        data_ny_karakter = (studentnr, emnekode, dato_konvertert, karakter,)
        markor.execute(endre_karakter, data_ny_karakter)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Eksamenskarakteren er slettet')
        markor.close()
        mindatabase.close()

    def sok_eksamensresultat():
        # Kode for å hente frem studenter med eksamensresultat innenfor en eksamen:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        emnekode = ek2.get()
        dato = date2.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        sql = 'SELECT Studentnr, Emnekode, Dato, Karakter FROM Eksamensresultat WHERE Emnekode = %s AND Dato = %s'
        data_eksamen = (emnekode, dato_konvertert,)
        markor.execute(sql, data_eksamen)
        data = markor.fetchall()
        studenter = []
        for row in data:
            studenter += [row[0]]
        innhold_eksamensresultat.set(tuple(studenter))
        markor.close()
        mindatabase.close()

    def hente_student_eksamensresultat(handling):
        # Koble valget fra student listen sammen med set'er boksene:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        valgt = liste_eksamen.get(liste_eksamen.curselection())
        emnekode = ek2.get()
        dato = date2.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        markor.execute('SELECT * FROM Eksamensresultat')
        data = markor.fetchall()
        for row in data:
            if valgt == row[0] and emnekode == row[1] and dato_konvertert == row[2]:
                snr2.set(row[0])
                ek2.set(row[1])
                date2.set(row[2])
                grade3.set(row[3])
        markor.close()
        mindatabase.close()

    def slett_eksamensresultat_mengde():
        # Utføre sletting av karakter:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        studentnr = snr2.get()
        emnekode = ek2.get()
        dato = date2.get()
        karakter = grade3.get()
        dato_konvertert = datetime.strptime(dato, '%Y-%m-%d').date()
        markor = mindatabase.cursor()
        endre_karakter = ('DELETE FROM Eksamensresultat WHERE Studentnr = %s AND Emnekode = %s AND Dato = %s AND Karakter = %s')
        data_ny_karakter = (studentnr, emnekode, dato_konvertert, karakter,)
        markor.execute(endre_karakter, data_ny_karakter)
        mindatabase.commit()
        messagebox.showinfo('Info', 'Eksamenskarakteren er slettet')
        markor.close()
        mindatabase.close()

    # GUI slette eksamensresultat:
    slett_eksamensresultat_vindu = Toplevel()
    slett_eksamensresultat_vindu.title('Eksamensresultat (sletting)')
    slett_eksamensresultat_vindu.resizable(FALSE, FALSE)
    slett_eksamensresultat_vindu.geometry('478x560+600+100')

    overskrift = Label(slett_eksamensresultat_vindu, text='Eksamensresultat sletting', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=4, padx=15, pady=5)
    forklaring_sok = Label(slett_eksamensresultat_vindu, text='Skriv inn studentnr, emnekode og dato for å søke på student',  font=('Sans-Serif', '11'))
    forklaring_sok.grid(row=1, columnspan=4, padx=15, pady=(10, 30))

    btn_sok = Button(slett_eksamensresultat_vindu, text='Søk student', command=sok_en_karakter)
    btn_sok.grid(row=2, column=3, padx=5, pady=5, sticky=E)

    lbl_studentnr = Label(slett_eksamensresultat_vindu, text='Studentnr:')
    lbl_studentnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    snr = StringVar()
    ent_snr = Entry(slett_eksamensresultat_vindu, width=6, textvariable=snr)
    ent_snr.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    lbl_emnekode = Label(slett_eksamensresultat_vindu, text='Emnekode:')
    lbl_emnekode.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    ek = StringVar()
    ent_ek = Entry(slett_eksamensresultat_vindu, width=8, textvariable=ek)
    ent_ek.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    lbl_dato = Label(slett_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    date = StringVar()
    ent_date = Entry(slett_eksamensresultat_vindu, width=10, textvariable=date)
    ent_date.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    lbl_karakter = Label(slett_eksamensresultat_vindu, text='Karakter:')
    lbl_karakter.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    grade = StringVar()
    ent_grade = Entry(slett_eksamensresultat_vindu, width=6, textvariable=grade)
    ent_grade.grid(row=5, column=1, padx=5, pady=5, sticky=W)
 
    btn_slett = Button(slett_eksamensresultat_vindu, text='Slett eksamensresultat', command=slette_en_karakter)
    btn_slett.grid(row=6, column=3, padx=5, pady=5, sticky=E)

    tkinter.ttk.Separator(slett_eksamensresultat_vindu, orient=HORIZONTAL).grid(row=7, columnspan=4, pady=10, sticky='WE')

    forklaring_sok2 = Label(slett_eksamensresultat_vindu, text='Skriv inn emnekode og dato for å søke på eksamen',  font=('Sans-Serif', '11'))
    forklaring_sok2.grid(row=8, columnspan=4, padx=15, pady=(10, 30))

    btn_sok2 = Button(slett_eksamensresultat_vindu, text='Søk eksamen', command=sok_eksamensresultat)
    btn_sok2.grid(row=9, column=3, padx=5, pady=5, sticky=E)

    lbl_studentnr2 = Label(slett_eksamensresultat_vindu, text='Studentnr:')
    lbl_studentnr2.grid(row=9, column=0, padx=5, pady=5, sticky=E)

    snr2 = StringVar()
    ent_snr2 = Entry(slett_eksamensresultat_vindu, state='readonly', width=6, textvariable=snr2)
    ent_snr2.grid(row=9, column=1, padx=5, pady=5, sticky=W)

    y_scroll = Scrollbar(slett_eksamensresultat_vindu, orient=VERTICAL)
    y_scroll.grid(row=9, rowspan=4, column=2,  padx=(100, 0), pady=5, sticky=NS)

    innhold_eksamensresultat = StringVar()
    liste_eksamen = Listbox(slett_eksamensresultat_vindu, width=15, height=7, listvariable=innhold_eksamensresultat, yscrollcommand=y_scroll.set)
    liste_eksamen.grid(row=9, rowspan=4, column=2, padx=5, pady=5)
    y_scroll['command'] = liste_eksamen.yview 

    lbl_emnekode2 = Label(slett_eksamensresultat_vindu, text='Emnekode:')
    lbl_emnekode2.grid(row=10, column=0, padx=5, pady=5, sticky=E)

    ek2 = StringVar()
    ent_ek2 = Entry(slett_eksamensresultat_vindu, width=8, textvariable=ek2)
    ent_ek2.grid(row=10, column=1, padx=5, pady=5, sticky=W)

    lbl_dato2 = Label(slett_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato2.grid(row=11, column=0, padx=5, pady=5, sticky=E)

    date2 = StringVar()
    ent_date2 = Entry(slett_eksamensresultat_vindu, width=10, textvariable=date2)
    ent_date2.grid(row=11, column=1, padx=5, pady=5, sticky=W)

    lbl_karakter2 = Label(slett_eksamensresultat_vindu, text='Karakter:')
    lbl_karakter2.grid(row=12, column=0, padx=5, pady=5, sticky=E)

    grade3 = StringVar()
    ent_grade = Entry(slett_eksamensresultat_vindu, state='readonly', width=6, textvariable=grade3)
    ent_grade.grid(row=12, column=1, padx=5, pady=5, sticky=W)

    btn_slett2 = Button(slett_eksamensresultat_vindu, text='Slett eksamensresultat', command=slett_eksamensresultat_mengde)
    btn_slett2.grid(row=14, column=3, padx=5, pady=5, sticky=E)

    btn_tilbake = Button(slett_eksamensresultat_vindu, text='Tilbake til meny', command=slett_eksamensresultat_vindu.destroy)
    btn_tilbake.grid(row=14, column=0, padx=15, pady=25, sticky=W)

    liste_eksamen.bind('<<ListboxSelect>>', hente_student_eksamensresultat)

def utskrift_eksamensresultat_GUI():
    def utskrift_karakterliste():
        # Kode for utskrift av karakterliste:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        emnekode = ek.get()
        utskrift_markor = mindatabase.cursor()        
        sql = 'SELECT * FROM Eksamensresultat WHERE Emnekode = %s ORDER BY Studentnr'
        data_utskrift = (emnekode,)
        utskrift_markor.execute(sql, data_utskrift)
        data = utskrift_markor.fetchall()
        tekst_vindu.delete('1.0', END)
        for row in data:
            if row[3] != None:
                tekst_vindu.insert(END, "Snr:" + str(row[0]) + " | " + "Emnek: " + str(row[1]) + " | " + "Dato: " + str(row[2]) + " | " + "Karakter: " + str(row[3])  + "\n")
        utskrift_markor.close()
        mindatabase.close()
    
    def utskrift_karakterstatistikk():
        # Kode for utskrift av karakterstatistikk utifra valgt dato:
        mindatabase = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef', password='oblig2021', db='oblig2021')
        emnekode = ek.get()
        dato_tastet = dato.get()
        dato_konvertert = datetime.strptime(dato_tastet, '%Y-%m-%d').date()
        utskrift_markor = mindatabase.cursor()      
        sql = 'SELECT * FROM Eksamensresultat WHERE Emnekode = %s AND Dato = %s ORDER BY Studentnr'
        data_utskrift = (emnekode, dato_konvertert,)
        utskrift_markor.execute(sql, data_utskrift)
        data = utskrift_markor.fetchall()
        karakter_A = 0
        karakter_B = 0
        karakter_C = 0
        karakter_D = 0
        karakter_E = 0
        karakter_F = 0
        tekst_vindu.delete('1.0', END)
        for row in data:
            if row[3] != None:
                tekst_vindu.insert(END, "Snr:" + str(row[0]) + " | " + "Emnek: " + str(row[1]) + " | " + "Dato: " + str(row[2]) + " | " + "Karakter: " + str(row[3])  + "\n")
                if row[3] == 'A':
                    karakter_A += 1
                elif row[3] == 'B':
                    karakter_B += 1
                elif row[3] == 'C':
                    karakter_C += 1
                elif row[3] == 'D':
                    karakter_D += 1
                elif row[3] == 'E':
                    karakter_E += 1
                elif row[3] == 'F':
                    karakter_F += 1
        karaktera.set(karakter_A)
        karakterb.set(karakter_B)
        karakterc.set(karakter_C)
        karakterd.set(karakter_D)
        karaktere.set(karakter_E)
        karakterf.set(karakter_F)
        utskrift_markor.close()
        mindatabase.close()  

    # GUI utskrift eksamensresultat:
    utskrift_eksamensresultat_vindu = Toplevel()
    utskrift_eksamensresultat_vindu.title('Eksamensresultater (utskrift)')
    utskrift_eksamensresultat_vindu.resizable(FALSE, FALSE)
    utskrift_eksamensresultat_vindu.geometry('535x570+600+100')

    overskrift = Label(utskrift_eksamensresultat_vindu, text='Eksamensresultat utskrift', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=7, padx=15, pady=5)
    forklaring_utskrift = Label(utskrift_eksamensresultat_vindu, text='Velg utskrift av "karakterliste" eller karakterstatistikk nederst',  font=('Sans-Serif', '11'))
    forklaring_utskrift.grid(row=1, columnspan=7, padx=15, pady=(10, 30))

    lbl_dato = Label(utskrift_eksamensresultat_vindu, text='Dato (yyyy-mm-dd):')
    lbl_dato.grid(row=2, column=1, padx=5, pady=5, stick=E)

    dato = StringVar()
    ent_dato = Entry(utskrift_eksamensresultat_vindu, width=10, textvariable=dato)
    ent_dato.grid(row=2, column=2, padx=5, pady=5, sticky=W)
    
    lbl_ek = Label(utskrift_eksamensresultat_vindu, text='Emnekode:')
    lbl_ek.grid(row=3, column=1, padx=5, pady=5, sticky=E)

    ek = StringVar()
    ent_ek = Entry(utskrift_eksamensresultat_vindu, width=10, textvariable=ek)
    ent_ek.grid(row=3, column=2, padx=5, pady=5, sticky=W)

    lbl_karaktera = Label(utskrift_eksamensresultat_vindu, text='A:')
    lbl_karaktera.grid(row=3, column=3, padx=(0, 0), pady=5, sticky=W)

    karaktera = StringVar()
    ent_karaktera = Entry(utskrift_eksamensresultat_vindu, state='readonly', width=2, textvariable=karaktera)
    ent_karaktera.grid(row=3, column=3, padx=(20, 0), pady=5, sticky=W)

    lbl_karakterb = Label(utskrift_eksamensresultat_vindu, text='B:')
    lbl_karakterb.grid(row=3, column=3, padx=(40, 0), pady=5, sticky=W)

    karakterb = StringVar()
    ent_karakterb = Entry(utskrift_eksamensresultat_vindu, state='readonly', width=2, textvariable=karakterb)
    ent_karakterb.grid(row=3, column=3, padx=(60, 0), pady=5, sticky=W)

    lbl_karakterc = Label(utskrift_eksamensresultat_vindu, text='C:')
    lbl_karakterc.grid(row=3, column=3, padx=(80, 0), pady=5, sticky=W)

    karakterc = StringVar()
    ent_karakterc = Entry(utskrift_eksamensresultat_vindu, state='readonly', width=2, textvariable=karakterc)
    ent_karakterc.grid(row=3, column=3, padx=(100, 0), pady=5, sticky=W)

    lbl_karakterd = Label(utskrift_eksamensresultat_vindu, text='D:')
    lbl_karakterd.grid(row=3, column=3, padx=(120, 0), pady=5, sticky=W)

    karakterd = StringVar()
    ent_karakterd = Entry(utskrift_eksamensresultat_vindu, state='readonly', width=2, textvariable=karakterd)
    ent_karakterd.grid(row=3, column=3, padx=(140, 0), pady=5, sticky=W)

    lbl_karaktere = Label(utskrift_eksamensresultat_vindu, text='E:')
    lbl_karaktere.grid(row=3, column=3, padx=(160, 0), pady=5, sticky=W)

    karaktere = StringVar()
    ent_karaktere = Entry(utskrift_eksamensresultat_vindu, state='readonly', width=2, textvariable=karaktere)
    ent_karaktere.grid(row=3, column=3, padx=(180, 0), pady=5, sticky=W)

    lbl_karakterf = Label(utskrift_eksamensresultat_vindu, text='F:')
    lbl_karakterf.grid(row=3, column=3, padx=(200, 0), pady=5, sticky=W)

    karakterf = StringVar()
    ent_karakterf = Entry(utskrift_eksamensresultat_vindu, state='readonly', width=2, textvariable=karakterf)
    ent_karakterf.grid(row=3, column=3, padx=(220, 0), pady=5, sticky=W)

    tekst_vindu = Text(utskrift_eksamensresultat_vindu, width=65, height=20)
    tekst_vindu.grid(row=4, columnspan=5, padx=5, pady=5)

    btn_hent_data1 = Button(utskrift_eksamensresultat_vindu, text='Utskrift av "karakterliste"', command=utskrift_karakterliste)
    btn_hent_data1.grid(row=5, column=2, padx=5, pady=5, sticky=SE)

    btn_hent_data2 = Button(utskrift_eksamensresultat_vindu, text='Utskrift av karakterstatistikk', command=utskrift_karakterstatistikk)
    btn_hent_data2.grid(row=5, column=3, padx=15, pady=5, sticky=SE)

    btn_tilbake2 = Button(utskrift_eksamensresultat_vindu, text='Tilbake til meny', command=utskrift_eksamensresultat_vindu.destroy)
    btn_tilbake2.grid(row=5, column=1, padx=15, pady=5, sticky=SW) 
    
def main():
    # GUI meny:
    hovedvindu = Tk()
    hovedvindu.title('Meny')
    hovedvindu.resizable(FALSE, FALSE)
    hovedvindu.geometry('500x300+600+200')

    overskrift = Label(hovedvindu, text='USN Student og eksamens program', font=('Sans-Serif', '22'))
    overskrift.grid(row=0, columnspan=5, padx=15, pady=15)

    text_student = Label(hovedvindu, text='Student:', font=('Sans-Serif', '10'))
    text_student.grid(row=1, column=0, padx=15, pady=5)
    btn_registrere_student = Button(hovedvindu, text="Registrere", command=registrere_student_GUI)
    btn_registrere_student.grid(row=1, column=1, padx=5, pady=20, sticky=W)
    btn_oppdatere_student = Button(hovedvindu, text='Oppdatere', command=oppdatere_student_GUI)
    btn_oppdatere_student.grid(row=1, column=2, padx=5, pady=20, sticky=W)
    btn_slette_student = Button(hovedvindu, text='Slette', command=slette_student_GUI)
    btn_slette_student.grid(row=1, column=3, padx=5, pady=20, sticky=W)
    btn_utskrift_student = Button(hovedvindu, text='Utskrift', command=utskrift_eksamensresultater_student_GUI)
    btn_utskrift_student.grid(row=1, column=4, padx=5, pady=20, sticky=W)

    text_eksamen = Label(hovedvindu, text='Eksamen:', font=('Sans-Serif', '10'))
    text_eksamen.grid(row=2, column=0, padx=15, pady=5)
    btn_registrere_eksamen = Button(hovedvindu, text="Registrere", command=registrere_eksamen_GUI)
    btn_registrere_eksamen.grid(row=2, column=1, padx=5, pady=20, sticky=W)
    btn_oppdatere_eksamen = Button(hovedvindu, text='Oppdatere', command=oppdatere_eksamen_GUI)
    btn_oppdatere_eksamen.grid(row=2, column=2, padx=5, pady=20, sticky=W)
    btn_slette_eksamen = Button(hovedvindu, text='Slette', command=slette_eksamen_GUI)
    btn_slette_eksamen.grid(row=2, column=3, padx=5, pady=20, sticky=W)
    btn_utskrift_eksamen = Button(hovedvindu, text='Utskrift', command=utskrift_eksamen_GUI)
    btn_utskrift_eksamen.grid(row=2, column=4, padx=5, pady=20, sticky=W)

    text_eksamensresultat = Label(hovedvindu, text='Eksamensresultat:', font=('Sans-Serif', '10'))
    text_eksamensresultat.grid(row=3, column=0, padx=15, pady=5)
    btn_registrere_eksamensresultat = Button(hovedvindu, text="Registrere", command=registrere_eksamensresultat_GUI)
    btn_registrere_eksamensresultat.grid(row=3, column=1, padx=5, pady=20, sticky=W)
    btn_oppdatere_eksamensresultat = Button(hovedvindu, text='Oppdatere', command=oppdatere_eksamensresultat_GUI)
    btn_oppdatere_eksamensresultat.grid(row=3, column=2, padx=5, pady=20, sticky=W)
    btn_slette_eksamenresultat = Button(hovedvindu, text='Slette', command=slette_eksamensresultat_GUI)
    btn_slette_eksamenresultat.grid(row=3, column=3, padx=5, pady=20, sticky=W)
    btn_utskrift_eksamensresultat = Button(hovedvindu, text='Utskrift', command=utskrift_eksamensresultat_GUI)
    btn_utskrift_eksamensresultat.grid(row=3, column=4, padx=5, pady=20, sticky=W)

    hovedvindu.mainloop()
main()