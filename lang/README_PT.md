## Gerenciador de Tarefas CLI em Python

🌐 **Languages**

[![English](https://img.shields.io/badge/English-blue?style=for-the-badge)](/README.md)
[![Español](https://img.shields.io/badge/Español-red?style=for-the-badge)](README_ES.md)
[![한국어](https://img.shields.io/badge/한국어-purple?style=for-the-badge)](README_KO.md)

Um simples gerenciador de tarefas em linha de comando feito com Python. Este projeto permite que os usuários gerenciem suas tarefas diárias diretamente pelo terminal de forma rápida e prática.

### Funcionalidades

* Adicionar novas tarefas
* Listar todas as tarefas
* Marcar tarefas como concluídas
* Deletar tarefas
* Armazenamento persistente de dados usando arquivos JSON
* Interface de linha de comando simples e intuitiva

### Como funciona

As tarefas são armazenadas em um arquivo local `taks.json`. Cada tarefa contém:

* **ID** – identificador único
* **Descrição da tarefa**
* **Status** – "Em andamento" ou "Concluído"

O programa carrega o arquivo JSON quando é iniciado e o atualiza sempre que uma tarefa é criada, concluída ou deletada.

### Tecnologias Utilizadas

* **Python 3**
* **JSON** para persistência de dados
* **Módulo OS** para utilidades no terminal

### Como Usar

1. Clone o repositório:

```
git clone https://github.com/Hallow303/cli-task-manager.git
```

2. Navegue até a pasta do projeto:

```
cd cli-task-manager
```

3. Execute o programa:

```
python main.py
```

4. Use o menu no terminal para gerenciar suas tarefas:

* Adicionar uma tarefa
* Ver tarefas
* Marcar uma tarefa como concluída
* Deletar uma tarefa

### Objetivo

Este projeto foi criado como um exercício de aprendizado para praticar:

* Manipulação de arquivos em Python
* Trabalho com dados em JSON
* Construção de aplicações simples em CLI
* Organização de código usando funções

