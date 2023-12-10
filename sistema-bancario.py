import tkinter as tk

class ContaBancaria:
    def __init__(self, saldo_inicial=5000):
        self.saldo = saldo_inicial
        self.transacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.transacoes.append(f'Depósito: +{valor}, Saldo: {self.saldo}')

    def saque(self, valor):
        if valor > self.saldo:
            return 'Saldo insuficiente.'
        else:
            self.saldo -= valor
            self.transacoes.append(f'Saque: -{valor}, Saldo: {self.saldo}')
            return None

    def extrato(self):
        extrato = '\nExtrato:'
        for transacao in self.transacoes:
            extrato += '\n' + transacao
        extrato += f'\nSaldo atual: {self.saldo}'
        return extrato

class BancoApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Sistema Bancário')
        
        self.conta = ContaBancaria()
        
        self.label_saldo = tk.Label(master, text=f'Saldo atual: {self.conta.saldo}')
        self.label_saldo.pack()

        self.label_resultado = tk.Label(master, text='')
        self.label_resultado.pack()

        self.entry_valor = tk.Entry(master)
        self.entry_valor.pack()

        self.botao_deposito = tk.Button(master, text='Depósito', command=self.realizar_deposito)
        self.botao_deposito.pack()

        self.botao_saque = tk.Button(master, text='Saque', command=self.realizar_saque)
        self.botao_saque.pack()

        self.botao_extrato = tk.Button(master, text='Extrato', command=self.exibir_extrato)
        self.botao_extrato.pack()

        self.botao_sair = tk.Button(master, text='Sair', command=master.destroy)
        self.botao_sair.pack()

    def realizar_deposito(self):
        valor = float(self.entry_valor.get())
        self.conta.deposito(valor)
        self.atualizar_interface()

    def realizar_saque(self):
        valor = float(self.entry_valor.get())
        resultado = self.conta.saque(valor)
        if resultado:
            self.label_resultado['text'] = resultado
        else:
            self.atualizar_interface()

    def exibir_extrato(self):
        resultado = self.conta.extrato()
        self.label_resultado['text'] = resultado

    def atualizar_interface(self):
        self.label_saldo['text'] = f'Saldo atual: {self.conta.saldo}'
        self.label_resultado['text'] = ''

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
