```markdown
# Aula_17_bootcamp

Exemplo simples usando SQLAlchemy e SQLite.

Como configurar o ambiente e executar:

# Aula_17_bootcamp

Exemplo simples usando SQLAlchemy e SQLite.

O script `exemplo01.py` cria o arquivo `meubanco.db` e uma tabela `usuarios`.

Requisitos
- Python 3.12+

PowerShell (Windows)

1. Criar e ativar um virtualenv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Atualizar pip e instalar dependências:

```powershell
python -m pip install --upgrade pip
python -m pip install SQLAlchemy==2.0.44
```

3. Executar:

```powershell
python exemplo01.py
```

Bash (Git Bash ou terminal que não seja PowerShell)

Em alguns terminais Bash no Windows (ex.: Git Bash) o comando `python` pode apontar para a instalação global (ex.: pyenv) e não para o `.venv` do projeto. Para garantir que o script use as dependências do projeto, active o venv ou chame o executável do venv diretamente.

1. Criar o virtualenv (se ainda não criado):

```bash
python -m venv .venv
```

2. Ativar o venv no Bash (Git Bash):

```bash
source .venv/Scripts/activate
# ou
. .venv/Scripts/activate
```

> Observação: em WSL ou Linux o caminho de ativação normalmente é `.venv/bin/activate`.

3. Instalar dependências:

```bash
python -m pip install --upgrade pip
python -m pip install SQLAlchemy==2.0.44
```

4. Executar:

```bash
python exemplo01.py
```

Alternativa (sem ativar o venv): chame diretamente o Python do venv:

```bash
.venv/Scripts/python.exe exemplo01.py
```

Dica rápida de diagnóstico
- Se `python` no Bash aponta para algo como `C:\Users\ppjon\.pyenv\...`, isso indica que o Python global está sendo usado. Nesse caso active o venv ou use o executável do venv.

Se quiser, eu posso testar executar `exemplo01.py` para você no terminal Bash usando o Python do venv.
