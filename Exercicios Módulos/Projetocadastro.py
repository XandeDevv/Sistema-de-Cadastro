import re

class Testando:
    def __init__(self,lista):
        self.estado=self.nome=self.user=self.senha=self.email= ''
        self.idade=0
        self.lista=lista

    def menu(self):
        print(f'\033[35m-\033[m'*42)
        print(f'\033[35mRadiante\033[m'.center(47))
        print(f'\033[35m-\033[m' * 42)
        print('\033[34m[1]- Para fazer um cadastro\n'
              '[2]- Para fazer login\n'
              '[3]- Para ver as pessoas cadastrados\n'
              '[4]- Sair\033[m')
        op=input('Qual a sua opção?')
        if op=='4':
            print(f'\033[35m-\033[m' * 42)
            print(f'\033[35mFechando o programa...\033[m'.center(49))
            print(f'\033[35m-\033[m' * 42)
            exit()
        elif op=='1':
            self.cadastrar()
        elif op=='2':
            self.login()
        elif op=='3':
            self.ver_inf()
        else:
            print('\033[31mOpção Inválida!\033[m')
            self.menu()

    def cadastrar(self):
        self.perg_nome_estado()
        if __name__ == '__main__':
            self.email_válido()
        self.perg_idade()
        self.perg_user()
        self.senha_válida()
        self.registro = {'Nome': self.nome, 'Estado': self.estado, 'Idade': self.idade, 'Email': self.email,
                         'User': self.user,'Senha': self.senha}
        self.adicionar_lista()
        print(f'\033[35m-\033[m' * 42)
        print(f'\033[35mCadastrado com sucesso!\033[m'.center(49))
        print(f'\033[35m-\033[m' * 42)
        self.registro={}
        self.menu()

    def perg_nome_estado(self):
        self.nome=input('Nome:').title()
        self.estado=input('Em que Estado você mora:').title()
        if not self.nome.isalpha() or not self.estado.isalpha():
            print('\033[31mDigite apenas letras\033[m')
            self.perg_nome_estado()

    def perg_idade(self):
        try:
            self.idade=int(input('Idade:'))
            if self.idade<0:
                print('\033[31mDigite números maiores que zero\033[m')
                self.perg_idade()
        except:
            print('\033[31mDigite apenas números maiores que zero\033[m')
            self.perg_idade()

    def perg_user(self):
        print('\033[32mO nome de Usuário deve conter apenas letras e números\033[m')
        self.user=input('Nome de Usuário:')
        if not self.user.isalnum():
            self.perg_user()

    def senha_válida(self):
        flag = 0
        while flag<=0:
            print('\033[32mA senha deve conter o minímo de 8 caracteres\n'
                  'No minímo uma letra maíuscula e uma minuscula\n'
                  'No mínimo um número\n'
                  'No mínimo um desses _@$%#&*\033[m ')
            self.senha = input('Digite sua senha:')
            if (len(self.senha) < 8):
                flag = -1
            elif not re.search("[a-z]", self.senha):
                flag = -1
            elif not re.search("[A-Z]", self.senha):
                flag = -1
            elif not re.search("[0-9]", self.senha):
                flag = -1
            elif not re.search("[_@$%#&*]", self.senha):
                flag = -1
            elif re.search("\s", self.senha):
                flag = -1
            else:
                flag = 1
                print(f'\033[34mA senha é Válida\033[m')
                break
            if flag == -1:
                print(f'\033[31mA senha é inválida\033[m')
        while flag==1:
            self.senhadnv=input('Digite a senha novamente:')
            if self.senhadnv!=self.senha:
                print('\033[31mVocê digitou uma senha diferente!\033[m')
                self.senha_válida()
            break

    def email_válido(self):
        regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
        if __name__ == '__main__':
            self.email=input('Email:')
            if (re.search(regex, self.email)):
                print(f'\033[34mO Email é Válido\033[m')
            else:
                print(f'\033[31mO Email é Inválido\033[m')
                self.email_válido()

    def login(self):
        self.digtuser=input('User:')
        self.digtsenha=input('Senha:')
        with open('pessoas_cadastradas.txt','r') as arquivo:
            for c in arquivo:
                if self.digtuser in c and self.digtsenha in c:
                    print(f'\033[35m-\033[m' * 42)
                    print(f'\033[35mLogando...\033[m'.center(49))
                    print(f'\033[35m-\033[m' * 42)
                    print(c.replace(',','\n'))
                    self.menu()
            else:
                print(f'\033[31mOs dados obtidos estão incorretos!\033[m')
                self.login()

    def adicionar_lista(self):
        with open("pessoas_cadastradas.txt",'a') as arquivo:
            arquivo.write(str(self.registro) + '\n')

    def ver_inf(self):
        with open("pessoas_cadastradas.txt",'rt') as arquivo:
            for c in arquivo:
                print(c)
        self.menu()


pessoas_cadastradas=[{}]
p1=Testando(pessoas_cadastradas)
p1.menu()
