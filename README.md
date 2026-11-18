## 🔗 Links Úteis
* **Acesse o projeto rodando:** [Ver Aplicação To-Do List](http://127.0.0.1:5000) *(ou cole aqui o link do seu vídeo no YouTube/Drive se preferir)*

## 📋 Modelagem e Especificação do Sistema (UML)

### 1. Diagrama de Classes
O sistema da *To-Do List* é estruturado com base em uma única entidade principal de persistência (Model), contendo os seguintes atributos e tipos de dados:

* **Classe:** `Tarefa`
  * `id` (INTEGER, Primary Key, Auto-increment)
  * `titulo` (TEXT, Not Null)
  * `status` (TEXT, Default: 'Pendente')

### 2. Dicionário de Dados (Projeto Físico - SQLite)
* **Tabela:** `tarefas`
  * **id:** Identificador único e sequencial de cada registro.
  * **titulo:** Descrição textual da tarefa a ser executada.
  * **status:** Indicador do estado atual da tarefa (ex: Pendente / Concluída).

### 3. Interface Humano-Computador (IHC)
* **Protótipo de Telas:** O sistema conta com uma interface web limpa e minimalista baseada em formulários de entrada de dados (`<input type="text">` e botões de ação) e uma listagem dinâmica com rota de exclusão rápida.
* **Experiência do Usuário (UX):** Focada em clareza, simplicidade e feedback visual imediato após a inclusão ou remoção de registros.
