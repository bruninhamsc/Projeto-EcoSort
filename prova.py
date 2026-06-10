"""
Projeto EcoSort - Express-Cargo
Autor: Inteligência Artificial
Descrição: Motor de cálculo logístico e automação de frete contra falhas operacionais.
"""

def main() -> None:
    # 1. Inicialização da Memória de Processamento (Vetores/Listas estáticas)
    TOTAL_PACOTES = 10
    pesos: list[float] = [0.0] * TOTAL_PACOTES
    fretes: list[float] = [0.0] * TOTAL_PACOTES
    
    # Variáveis de consolidação
    carga_total: float = 0.0
    faturamento_bruto: float = 0.0
    
    print("====================================================")
    print("      Express-Cargo - SISTEMA ECO SORT v4.0         ")
    print("====================================================\n")
    
    # 2. Estrutura de Repetição Controlada (Lote de 10 Pacotes)
    for i in range(TOTAL_PACOTES):
        print(f"--- Processando Pacote {i + 1}/{TOTAL_PACOTES} ---")
        
        # Validação de Dados Defensiva: Peso do Pacote
        while True:
            try:
                peso_atual = float(input("Digite o peso do pacote (em kg): "))
                if peso_atual > 0:
                    break  # Dado válido, sai do loop
                print("[ERRO] O peso deve ser estritamente maior que zero.")
            except ValueError:
                print("[ERRO] Entrada inválida! Digite um valor numérico real (ex: 4.5).")
        
        # Armazenamento no vetor de pesos
        pesos[i] = peso_atual
        
        # Validação de Dados Defensiva: Destino (Uso de operadores lógicos)
        while True:
            try:
                destino = int(input("Digite o destino (1 - Nacional | 2 - Internacional): "))
                if destino == 1 or destino == 2:
                    break  # Dado válido, sai do loop
                print("[ERRO] Opção inválida. Digite apenas 1 ou 2.")
            except ValueError:
                print("[ERRO] Entrada inválida! Digite um número inteiro (1 ou 2).")
        
        # 3. Estrutura de Decisão Encadeada: Categorização Automática de Preços
        if peso_atual <= 2.0:
            custo_base = 10.00
        else:
            if peso_atual <= 10.0:
                custo_base = 20.00
            else:
                custo_base = 30.00
        
        # 4. Condicional Simples: Logística Internacional (+20%)
        if destino == 2:
            custo_base = custo_base * 1.20
            
        # 5. Memorização e Acumulação de Dados
        fretes[i] = custo_base
        carga_total += peso_atual
        faturamento_bruto += custo_base
        
        print(f"-> Sucesso: Frete calculado em R$ {custo_base:.2f}\n")
        
    # 6. Consolidação e Fechamento do Lote
    ticket_medio = faturamento_bruto / TOTAL_PACOTES
    
    # 7. Relatório Final de Saída (Output idêntico ao exigido)
    print("========== RESULTADO FINAL ==========")
    print(f"Total de pacotes: {TOTAL_PACOTES}")
    print(f"Carga total acumulada: {carga_total:.1f} kg")
    print(f"Faturamento bruto do lote: R$ {faturamento_bruto:.2f}")
    print(f"Ticket médio por pacote: R$ {ticket_medio:.2f}")
    print("=====================================")

if __name__ == "__main__":
    main()