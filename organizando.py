import datetime as dt
import datetime
# Data atual
data_atual = datetime.date.today()

# Data do empréstimo
data_emprestimo_str = input("Informe a data que você retirou o(s) livro(s) - (DIA/MES/ANO): ")
data_emprestimo_str = dt.datetime.strptime(data_emprestimo_str, '%d/%m/%Y')
print(data_emprestimo_str.date())
ano, mes, dia = data_emprestimo_str.year, data_emprestimo_str.month, data_emprestimo_str.day
dia_emprestimo = dt.date(ano, mes, dia)

# Verifica se já se passaram 14 dias desde a data do empréstimo
dias_passados = (data_atual - dia_emprestimo).days
print(dias_passados)