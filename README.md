# AvaliacaoRiscoNaiveBayes

Neste projeto foi criado um aplicativo simples através do django, que tem o objetivo de prever o risco de
acidente de trânsito através do algoritimo de aprendizado naive bayes.

A aplicação foi desenvolvida através do pipenv, portanto para executa-la é necessario:

Instalar o pipenv:

    pip install pipenv
   
Executar o pipenv:
    
    pipenv shell
    
Em seguida, instalar as dependencias do projeto:

    pipenv install --dev

Para treinar o modelo foi utilizada a base insurance.csv que está na pasta Algoritimos, junto com um arquivo
com o modelo treinado chamado, naivebayes_finalizados.sav.

O aplicativo criado através do django tem como objetivo final proporcionar ao usuário uma interface que permita
com que o usuário ao especificar alguns atributos tenha como retorno a chance dele se envolver em um acidente.

Forma de utilizar a aplicação:

Para fins de facilitar a utilização da interface foi-se escolhido apenas 3 atributos a serem especificados,
sendo eles idade, gosto de risco e modelo do veículo.

Na idade deve-se ser especificada a idade do condutor.

No gosto de risco deve-se ser especificado a personalidade do condutor com relação a risco,
se o condutor é aventureiro, moderado, psicopata ou normal.

No modelo do veículo deve-se ser especificado o modelo de veículo que o condutor usa.

Ao clicar no botão calcular, o modelo treinado pelo naive bayes ira calcular as probabilidades
de acidente e então retornar. A opção que apresentar maior probabilidade será a que representa
a chance do condutor se envolver em um acidente.
