from django import forms
from django.forms import ModelForm
from gestion_patient.models import Demande,Radiologue


class DemandeForm(ModelForm):
    class Meta:
        model = Demande
        fields = ['nom','prenom', 'indication','degre_urgence','type_examen','injection']
        widgets = {
       'degre_urgence':forms.Select,
       'type_examen':forms.Select,
       'injection':forms.Select, 
       'indication': forms.Textarea,    
        }
        
class RadiologueForm(ModelForm):
    class Meta:
        model = Radiologue
        fields = ['prenom','nom','statut','tempsDeTravail','indisponibilites']
        widgets = {
       'statut':forms.Select,
       'tempsDeTravail':forms.Select,    
        }
    