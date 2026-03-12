tempo_execucao = float(input("informe a tempo de execucao de uma tarefa: "))
qtd_tarefas_executadas = int(input("informe a quantidade de tarefas executadas: "))
tempo_total = (tempo_execucao * qtd_tarefas_executadas) /60
print(f"O tempo de execução total é de {tempo_total:.0f} minutos")