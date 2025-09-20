# Sabor Express | Formação Python e Orientação a Objetos

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=yellow)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Projeto Sabor Express, desenvolvido e aprimorado ao longo da formação **"Python e Orientação a Objetos"** da [Alura](https://www.alura.com.br). A aplicação, inicialmente procedural, foi refatorada e evoluída utilizando os pilares da Programação Orientada a Objetos (POO). O projeto final aplica desde conceitos fundamentais, como classes e encapsulamento, até tópicos avançados como herança, polimorfismo e a integração com APIs externas.

## 🚀 Sobre o Projeto

O Sabor Express é uma aplicação de console para gerenciamento de restaurantes. Sua arquitetura foi construída de forma incremental:

1.  **Fase 1 (Introdução à POO):** A base do projeto foi convertida de um modelo procedural (com dicionários e funções isoladas) para uma arquitetura orientada a objetos. Cada restaurante passou a ser modelado como um **objeto** da classe `Restaurante`, com seus próprios atributos e métodos, tornando o código mais organizado e reutilizável.

2.  **Fase 2 (Avançando na POO e API):** O projeto evoluiu para uma aplicação híbrida. Além do gerenciamento local, o sistema agora se conecta a uma **API externa** para buscar e listar restaurantes dinamicamente. Conceitos como **herança** e **classes abstratas** foram introduzidos para criar uma estrutura de código ainda mais robusta e flexível.

### ✨ Funcionalidades

* **[Curso 1]** Cadastro de novos restaurantes como objetos.
* **[Curso 1]** Listagem formatada de todos os restaurantes cadastrados.
* **[Curso 1]** Alternância do estado de ativação de um restaurante de forma encapsulada.
* **[Curso 1]** Atribuição de notas a um restaurante específico.
* **[Curso 2]** Atribuição de Pratos, Bebidas e Sobremesas para restaurantes específicos.
* **[Curso 2]** Exibir listagem do cardápio por restaurante com itens específicos.
* **[Curso 2]** Consumo de uma API externa para buscar e exibir restaurantes dinamicamente. (main.py)
* **[Curso 2]** Tratamento de exceções para lidar com falhas de conexão com a API. (main.py)

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Requests:** Biblioteca para realizar requisições HTTP e consumir a API de restaurantes.
* **Fast-API:** API utilizada para gerenciar os recursos 

## 🧠 Principais Aprendizados e Conceitos Aplicados

Este projeto foi fundamental para construir uma base sólida em Programação Orientada a Objetos, desde os fundamentos até a aplicação em cenários práticos de integração. A lista abaixo detalha a jornada de aprendizado:

#### 1. **Classes e Objetos**
   - Criação da classe `Restaurante` como um molde para definir a estrutura e o comportamento de todos os restaurantes no sistema.
   - Instanciação de objetos únicos a partir da classe, cada um representando um restaurante específico.

#### 2. **Abstração e Encapsulamento**
   - Modelagem da entidade "Restaurante" focando em seus atributos e comportamentos essenciais (abstração).
   - Proteção dos dados com atributos "privados" (usando `_`) e controle de acesso através de métodos e propriedades (encapsulamento).

#### 3. **Properties e Métodos Mágicos**
   - Uso do decorator `@property` para criar getters, permitindo acesso controlado a atributos.
   - Implementação do método `__str__` para fornecer uma representação textual e legível dos objetos.

#### 4. **Herança e Polimorfismo**
   - Criação de uma hierarquia de classes, com uma classe pai `Restaurante` definindo uma base comum e classes filhas especializando comportamentos.
   - Aplicação de polimorfismo para tratar objetos de diferentes classes de maneira uniforme, tornando o código mais flexível.

#### 5. **Classes e Métodos Abstratos (ABC)**
   - Uso do módulo `abc` para criar uma Classe Base Abstrata, definindo um "contrato" que força as classes filhas a implementarem métodos essenciais, garantindo a robustez do sistema.

#### 6. **Consumo de API e Manipulação de JSON**
   - Utilização da biblioteca `requests` para realizar requisições `GET` a um endpoint externo.
   - Parsing de respostas em formato **JSON**, convertendo o texto recebido em objetos Python para manipulação dentro da aplicação.

#### 7. **Organização de Código em Módulos**
   - Separação de responsabilidades em diferentes arquivos (`.py`) para manter o código principal (`app.py`) limpo e focado na interação com o usuário.

## 📂 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o Sabor Express em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Lucas-Fiche/alura-python-saborexpress-OO.git](https://github.com/Lucas-Fiche/alura-python-saborexpress-OO.git)
    cd alura-python-saborexpress-OO
    ```
2.  **Crie um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    Este projeto utiliza algumas bibliotecas, como a `requests`. Instale-as com o pip.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python app.py 
    ```

5.  **Interaja com a aplicação:**

## 👨‍💻 Autor

Projeto desenvolvido por **Lucas Fiche** como parte dos estudos na plataforma Alura.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucas-fiche-76aa24201)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Lucas-Fiche)