
✅ 1. README.md 

📦 Controle de Produtos - Sistema de Gestão de Estoque

Este projeto é um sistema completo de gestão de estoque desenvolvido com Django, oferecendo funcionalidades robustas para controle de produtos, autenticação de usuários, relatórios detalhados e exportação de dados para Excel.

🚀 Funcionalidades Principais
Autenticação de Usuários: Cadastro, login e logout seguros.
Gestão Completa de Produtos (CRUD): Cadastro, visualização, edição e exclusão de produtos.
Controle de Estoque: Registro automático de entradas e saídas, mantendo o saldo atualizado.
Relatórios Detalhados: Visualização clara e organizada dos produtos cadastrados.
Exportação para Excel: Exporte facilmente seus dados para planilhas Excel.
🛠️ Tecnologias Utilizadas
Python 3.11
Django 4.x
Bootstrap 5
SQLite (desenvolvimento) / PostgreSQL (produção)
Openpyxl (para exportação Excel)
Gunicorn (servidor HTTP para produção)
📂 Estrutura do Projeto
controle-produtos/
├── gestao_estoque/          # Configurações principais do projeto Django
├── estoque/                 # Aplicação principal para gestão de produtos
├── templates/               # Templates HTML com Bootstrap 5
├── staticfiles/             # Arquivos estáticos (CSS, JS, imagens)
├── Procfile                 # Arquivo para deploy no Railway
├── runtime.txt              # Versão do Python para deploy
└── requirements.txt         # Dependências do projeto

⚙️ Como Executar Localmente
1. Clone o repositório:
git clone https://github.com/rdralves/controle-produtos.git
cd controle-produtos

2. Crie e ative um ambiente virtual:
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Rode as migrações e crie um superusuário:
python manage.py migrate
python manage.py createsuperuser

5. Execute o servidor local:
python manage.py runserver


Acesse em: http://localhost:8000

🚀 Deploy em Produção (Railway)

Este projeto está preparado para deploy rápido e fácil no Railway:

Crie uma conta gratuita no Railway.
Conecte seu repositório GitHub.
Configure as variáveis de ambiente (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL).
Execute as migrações e crie um superusuário diretamente no terminal remoto do Railway.
📊 Relatórios e Exportação Excel
Acesse relatórios detalhados dos produtos cadastrados.
Exporte facilmente os dados para Excel com um clique.
🔐 Segurança e Autenticação
Sistema seguro com autenticação obrigatória.
Logout protegido contra ataques CSRF.




📌 Próximos Passos (Roadmap)
 Implementar filtros avançados nos relatórios.
 Exportação para PDF.
 Dashboard com gráficos e indicadores.
 Melhorias na interface e experiência do usuário.
🤝 Contribuições

Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do projeto.
Crie uma branch com sua feature (git checkout -b feature/nova-feature).
Faça commit das suas alterações (git commit -m 'Adicionando nova feature').
Faça push para a branch (git push origin feature/nova-feature).
Abra um Pull Request.
📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

📞 Contato

Criado por rdralves. Sinta-se à vontade para entrar em contato!

🌟 Gostou do projeto?

Deixe uma ⭐️ para apoiar o projeto e ajudar a alcançar mais pessoas!

