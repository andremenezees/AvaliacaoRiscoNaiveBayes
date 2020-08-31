from django.shortcuts import render

import pickle
import numpy as np

from app import forms


def index(request):
    formas = {
        'idade': forms.SelecioneIdade(),
        'risco': forms.GrauRisco(),
        'veiculo': forms.ModeloVeiculo(),
    }
    return render(request, "index.html", formas)


def resultado(request):
    if request.method == 'POST':
        # obtem os valores que foram selecionados pelo usuário
        idade = int(request.POST['idade'])
        risco = int(request.POST['risco'])
        veiculo = int(request.POST['veiculo'])

        naive_bayes = pickle.load(open('app/naivebayes/naivebayes_finalizado.sav', 'rb'))
        novo_registro = [[idade, risco, veiculo]]
        novo_registro = np.asarray(novo_registro)
        resposta = naive_bayes.predict_proba(novo_registro)

        # print("Resposta: ", resposta)

        formas = {
            'idade': forms.SelecioneIdade(),
            'risco': forms.GrauRisco(),
            'veiculo': forms.ModeloVeiculo(),
            'Mild': resposta[0][0],
            'None_': resposta[0][1],
            'Moderate': resposta[0][2],
            'Severe': resposta[0][3]
        }

        return render(request, "index.html", formas)
    else:
        index(request)
