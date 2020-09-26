from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange

# datetime.strptime(string, formato) -> lê uma string e retorna uma data de acordo com o formato
# datetime.strftime(formato) -> formata a data de acordo com o padrão informado
# datetime.timestamp() -> retorna o timestamp (data em milissegundos desde a Unix Epoch - Jan 1 1970 00:00:00 UTC)
# datetime.fromtimestamp(timestamp) -> retorna a data formatada a partir de um timestamp
# timedelta(days=?...) -> retorna um intervalo de tempo de acordo com os argumentos nomeados (dias, segundos, meses...)
# datas podem ser subtraídas umas das outras para gerar o timedelta entre elas
# datetime.total_seconds() -> retorna os segundos totais de um determinado timedelta
# datetime.time() -> Retorna o horário de uma data
# locale.setlocale(LC_ALL, '') -> Tenta utilizar o locale do ambiente de execução
# calendar.mdays -> retorna a quantidade de dias de um mês
# calendar.monthrange(ano, mês) -> retorna uma tupla contendo o dia da semana no qual o mês inicia e o último dia do mês
# em anos bissextos, mdays pode gerar problemas e, portanto, monthrange é aconselhável

setlocale(LC_ALL, 'pt_BR.utf-8')

data = datetime.now()
mes = int(data.strftime('%m'))

dia_semana, ultimo_dia = monthrange(2020, 9)

print(dia_semana)
