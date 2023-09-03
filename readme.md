                    Registro de Infomações Empresa de Transportes


Descricão:
	Este é um CRUD (Create, Read, Update, Delete) desenvolvido para registrar informacões relacionadas às entregas de produtos por uma empresa de transportes. Ele permite o registro de detalhes como nome do cliente, email, endereco, pedido, data prevista de entrega do produto e anotações.

Funcionalidades :
    O CRUD possui as seguintes operações: 
    Criar (Create): Adicionar novos registros de pedidos com informações completas, incluindo nome, email, data prevista de entrega e reclamação, se houver. 
    Ler  (Read): Visualizar informações detalhadas sobre entregas existentes, incluindo todos os campos registrados .
    Atualizar  (Update): Modificar informações de entregas existentes, permitindo a edição de qualquer campo. 
    Excluir (Delete): Remover registros de entregas existentes, se necessário.

Requisitos:
    •	Python
    •	Django
    •	Django Rest Framework
    •	Postegresql 
    •	Ambiente Virtual

Instalação:
		Para executar este CRUD em sua máquina local, siga estas etapas:

        1.	Crie um ambiente virtual (opcional, mas recomendado) para isolar as dependências do projeto:
        python -m venv venv

        2.	Ative o ambiente virtual:

            •	No windowns
            venv\Scripts\activate
            •	No mac/linux:
            source venv/bin/activate

        3.	Instale as dependências do projeto usando o pip:
            pip install -r requirements.txt

        4.	Configure o banco de dados de acordo com as configurações do seu projeto no arquivo settings.py. Isso pode envolver a criação do banco de dados, aplicação de migrações, etc.

        5.	Inicie o servidor de desenvolvimento Django:
                python manage.py runserver

        6.	Abra o aplicativo em seu navegador em:
                http://localhost:8000/.                    

        7.	Agora, o CRUD estará em execução em seu ambiente local, e você poderá começar a usar e testar as funcionalidades relacionadas ao registro de reclamações da empresa de transportes. Certifique-se de personalizar as etapas de acordo com as configurações específicas do seu projeto e inclua quaisquer informações adicionais necessárias para os usuários que desejam configurar e executar o CRUD em seus próprios ambientes.

