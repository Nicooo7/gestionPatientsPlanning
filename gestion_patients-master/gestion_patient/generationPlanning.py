#coding:utf_8
from random import *
import time
from openpyxl import Workbook
from openpyxl.styles import Font, Color
from openpyxl.styles import colors
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment





class Personne:

	liste=[]

	def __init__(self, nom, prenom, statut, tempsDeTravailMax, joursIndisponibles, joursSansTravail):
		self.nom = nom
		self.prenom = prenom
		self.statut = statut
		self.tempsDeTravailMax = tempsDeTravailMax
		self.tempsDeTravailCumule = 0
		self.joursIndisponibles = joursIndisponibles
		self.listeDesVacations = []
		self.joursSansTravail = joursSansTravail
		Personne.liste.append(self)

	def __repr__ (self):
		return self.prenom	
	


class Vacation:

	liste=[]

	def __init__(self, intitule, duree, moment):
		self.intitule=intitule
		self.duree=duree
		self.moment=moment
		self.responsable ="non attribue"
		Vacation.liste.append(self)

	def __repr__ (self):
		return self.intitule	

def reinitialiserLesObjects():
	Vacation.liste=[]
	Personne.liste= []
	LigneVacation.liste= []
	LigneStatistiquePersonne.liste= []

def creerLesPersonnes(radiologues):
	pleinTemps = 48
	for radiologue in radiologues:
		if radiologue.tempsDeTravail == "1/2 temps":
			tps = 0.5
		elif radiologue.tempsDeTravail == "3/4 temps":
			tps = 0.75
		elif radiologue.tempsDeTravail == "temps complet":
			tps = 1	

		Personne(nom=radiologue.nom, 
				prenom=radiologue.prenom, 
				statut=radiologue.statut, 
				joursIndisponibles=radiologue.indisponibilites,
				tempsDeTravailMax= tps * pleinTemps,
				joursSansTravail= radiologue.jourSansTravail,
				)


#afficher le planning
def afficherLePlanning(listeMoment):
	for moment in listeMoment:
		print ("\n _____________",moment,"\n")
		for vacation in Vacation.liste:
			if vacation.moment == moment:
				print(vacation, vacation.responsable)

def afficherLesStatistiques():
	for personne in Personne.liste:
		print (personne, ":    nombre de vacation:", len(personne.listeDesVacations), "   temps cumulé:", personne.tempsDeTravailCumule, "ecart par rapport au temps prévu", personne.ecart,"homogénéité: ", personne.scoreHomogeneiteVacation)
				






#bloquer une vacation
def bloquerUneVacation(intitule, moment, prenom):
	for personne in Personne.liste:
		if personne.prenom == prenom:
			p = personne
			for vacation in Vacation.liste:
				if vacation.intitule == intitule:
					if vacation.moment == moment:
						vacation.responsable = p
						p.listeDesVacations.append(vacation)

def bloquerLesVacations():
	bloquerUneVacation("IRM", "mardi matin", "Nicolas")
	bloquerUneVacation("scanner", "vendredi aprem", "Paul")
	bloquerUneVacation("echographie", "vendredi matin", "Paul")




def genererUnPlanning(listeMoment):

	#reinitialiser le planning
	def reinitialiser():
		#reenintialiser les vacations:
		for vacation in Vacation.liste:
			vacation.responsable = "non attribue"

		

		#reeinitialiser les personnes:
		for personne in Personne.liste:
			personne.listeDesVacations = []
			personne.tempsDeTravailCumule  = 0

		#bloquer les vacations	
		bloquerLesVacations()

	#implémenter le planning:
	def implementerLePlanning():
		for vacation in Vacation.liste:

			#tester si la vacation est bloquée:
			if vacation.responsable != "non attribue":

				for personne in Personne.liste:
					if personne.prenom == vacation.responsable.prenom:
						personne.tempsDeTravailCumule = personne.tempsDeTravailCumule + vacation.duree 
						personne.listeDesVacations.append(vacation)
					
				
			else:

				#affecter une personne à une vacation
				etape = 0
				tps1 = time.clock()
				compteur = 0
				while etape == 0:
					compteur = compteur + 1
					if compteur > 50 : 
						break
					x =  randint(0, len(Personne.liste)- 1)
					personne = Personne.liste[x]
					#print("personne affectée à la vaction:  _________", personne)
					tempsCumule = personne.tempsDeTravailCumule + vacation.duree 
					etape = 1
					#tester si le temps de travail cumulé de la personne n'exede pas son temps pax
					if tempsCumule > personne.tempsDeTravailMax:
						etape = 0
						#print("1")
					#tester si la personne n'est pas vaqué deux fois au même moment
					if len(personne.listeDesVacations) > 0:
						#print("liste des vacations de ", personne, "___________", personne.listeDesVacations)
						#input()
						for v in personne.listeDesVacations:
							if v.moment == vacation.moment:
								etape = 0
							#	print("2")

					jour = vacation.moment.split(" ")[0]		
					#tester si la personne n'est pas absente
					if jour in personne.joursIndisponibles:
						etape = 0
					
					#tester si la personne travaille bien le jour prévu
					if jour in personne.joursSansTravail:
						etape = 0	

					#tester si les personnes travaillant l'aprem travaillent aussi le matin: 
					if compteur < len(personne.liste):
						if "aprem" in vacation.moment:
							identifiant = vacation.moment[0:2]
							posteLeMatin = "non"
							for v in personne.listeDesVacations:
								if v.moment[0:2]==identifiant:
									posteLeMatin = "oui"
							if posteLeMatin == "non":
								etape = 0
					#tester si une personne n'est pas vaqué deux fois à la meme vacation le même jour:
					identifiant = vacation.moment[0:2]
					for v in personne.listeDesVacations:
						if v.moment[0:2]==identifiant:
							if v.intitule == vacation.intitule:
								etape = 0
								#print("3")

					if etape == 1:
						#concrétiser l'affectation						
						vacation.responsable = personne
						personne.listeDesVacations.append(vacation)
						personne.tempsDeTravailCumule = tempsCumule
	

	reinitialiser()
	implementerLePlanning()

	
def testerLePlanning():
	#tester l'écart de répartition par rapport au temps de travail théorique 
	
	ecartTotal = 0
	#calculer le l'écart pour chaque personne.
	for personne in Personne.liste:
		personne.ecart = personne.tempsDeTravailCumule/personne.tempsDeTravailMax
	
	#definir le score d'homogénéité des vacations 
	scoreTotal = 0
	for personne in Personne.liste:
		score = 0
		liste = []
		chaine = ""
		for vacation in personne.listeDesVacations:
			chaine = chaine + vacation.intitule
		if "scanner" in chaine:
			score +=1
		if "echographie" in chaine:
			score +=1
		if "IRM" in chaine:
			score += 1
		personne.scoreHomogeneiteVacation = score
			
			

	"""#faire la moyenne des écarts et obtenir la distance de la répartition par rapport à l'idéal (1)	
	for personne in Personne.liste:
		ecartTotal = ecartTotal + personne.ecart
	moyenne = ecartTotal/len(Personne.liste)
	distance = abs(1 - moyenne)
	return distance"""


#preparer la liste des lignes pour l'affichage

class LigneVacation:

		liste= []

		def __init__(self, vacation):
			self.titre= vacation.intitule + " " + vacation.moment
			self.intitule = vacation.intitule
			self.moment = vacation.moment
			self.responsable = vacation.responsable
			LigneVacation.liste.append(self)
	
class LigneStatistiquePersonne:	

	liste= []

	def __init__(self, personne):
		self.nom= personne
		self.nombreDeVacation = len(personne.listeDesVacations)
		self.tempsCumule = personne.tempsDeTravailCumule
		self.ecart = personne.ecart
		self.homogeneite = personne.scoreHomogeneiteVacation

		LigneStatistiquePersonne.liste.append(self)



def creerAffichageTableauPlanning():
	
					
	for vacation in Vacation.liste:
		LigneVacation(vacation)
	for personne in Personne.liste:
		LigneStatistiquePersonne(personne)
	


def genererFichierExcel():
	listeLigne= ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
	listeLettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
	listeDesColonnes= ["scanner matin", "scanner aprem", "IRM matin", "IRM aprem", "echographie matin", "echographie aprem"]

	rouge = Font(color=colors.RED)
	bleu = Font(color=colors.BLUE)



	book = Workbook()
	D = book.active
	i=1

	for colonne in listeDesColonnes:
		D['A'+ str(i + 1)] = colonne 
		D['A'+ str(i + 1)].font = bleu

		i +=1
	
	i = 0
	for ligne in listeLigne:
		lettre = listeLettres[i+1]		
		D[lettre + "1"] = ligne
		D[lettre + "1"].font = rouge
		i += 1

	for i in range(2,8):
		for j in range(1,6):
			jour = D['A'+ str(i)].value
			vac = D[listeLettres[j] + '1'].value
			ensemble = jour + vac
			for vacation in Vacation.liste:
				intitule = vacation.intitule
				moment = vacation.moment
				general = (intitule + " "+ moment).split(" ")
				
				#print(general[0], general[1], general[2])
				#print("ensemble:", ensemble)
				if general[0] in ensemble:
					if general[1] in ensemble:
						if general[2] in ensemble:
							if vacation.responsable == "non attribue":
								D[listeLettres[j]+ str(i)] = "XXX"
							else:
								D[listeLettres[j]+ str(i)] = vacation.responsable.prenom

								


				



	path = "/Users/nicolas/Desktop/apprentissage/"
	book.save( path + "planning.xlsx")				


def BouclePrincipale(listeMoment):
	v = True
	while v==True:
		v=False
		print("génération du planning")
		message = genererUnPlanning(listeMoment)
		testerLePlanning()
		print(message)
		if message=="echec":
			v=True
		for personne in Personne.liste:
			if personne.ecart<0.7:
				print("nouvelle génération car éart trop grand")
				v= True
			if personne.scoreHomogeneiteVacation < 3:
				v = True
	

def generationDuPlanning(radiologues):

	reinitialiserLesObjects()
	creerLesPersonnes(radiologues)
	listeMoment = ["lundi matin", "lundi aprem", "mardi matin", "mardi aprem", "mercredi matin", "mercredi aprem", "jeudi matin", "jeudi aprem", "vendredi matin", "vendredi aprem"]
	for moment in listeMoment:
		Vacation(
			intitule="scanner",
			duree= 5,
			moment = moment
			)
		Vacation(
		intitule="IRM",
		duree= 6,
		moment = moment
		)
		Vacation(
		intitule="echographie",
		duree= 4,
		moment = moment
		)
		Vacation(
		intitule="radiographies",
		duree= 4,
		moment = moment
		)
	BouclePrincipale(listeMoment)
	creerAffichageTableauPlanning()
	resultat = (LigneVacation.liste, LigneStatistiquePersonne.liste)
	return resultat







