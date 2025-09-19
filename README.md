# Sabor Express | Curso "Python: Avançando na Orientação a Objetos"

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=yellow)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Evolução do projeto Sabor Express, desenvolvido durante o curso **"Python: Avançando na Orientação a Objetos"** da [Alura](https://www.alura.com.br). O foco principal foi refatorar a aplicação inicial para o paradigma de Programação Orientada a Objetos (POO), aplicando conceitos como classes, objetos, encapsulamento e herança para criar um código mais robusto, organizado e reutilizável.

## 🚀 Sobre o Projeto

O Sabor Express continua sendo uma aplicação de console para gerenciamento de restaurantes. No entanto, sua arquitetura interna foi completamente remodelada. Em vez de dicionários e funções isoladas, a aplicação agora utiliza **classes** para modelar os restaurantes e suas funcionalidades. Cada restaurante no sistema é um **objeto**, com seus próprios dados (atributos) e comportamentos (métodos).

### ✨ Funcionalidades

* Exibição de um menu de opções interativo.
* Cadastro de novos restaurantes como objetos da classe `Restaurante`.
* Listagem de todos os restaurantes cadastrados, exibindo suas informações formatadas através de métodos.
* Alternância do estado de ativação de um restaurante de forma encapsulada.
* Atribuição de notas a um restaurante específico, utilizando métodos da classe.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal, com foco na aplicação do paradigma de Orientação a Objetos.

## 🧠 Principais Aprendizados e Conceitos Aplicados

Este projeto foi fundamental para solidificar meu entendimento sobre Programação Orientada a Objetos em Python. Os principais tópicos abordados foram:

#### 1. **Classes e Objetos**
   - Criação da classe `Restaurante` para servir como um molde, definindo a estrutura que todo restaurante no sistema deve ter.
   - Instanciação de **objetos** a partir da classe `Restaurante`, onde cada objeto representa um restaurante único na aplicação.

#### 2. **Atributos e Métodos**
   - Uso de **atributos de instância** (como `_nome`, `_categoria`, `_ativo`) para armazenar o estado de cada objeto.
   - Implementação de **métodos** (como `receber_avaliacao` e `alternar_estado`) para definir os comportamentos associados a um restaurante.

#### 3. **Abstração e Encapsulamento**
   - Aplicação do conceito de **abstração** ao modelar a entidade "Restaurante", focando em seus atributos e comportamentos essenciais.
   - Uso de **encapsulamento** para proteger os dados. Os atributos foram definidos como "privados" (usando `_`) para que o acesso a eles seja controlado por métodos e propriedades.

#### 4. **Properties (Propriedades)**
   - Utilização do decorator `@property` para criar getters, permitindo o acesso a atributos "privados" de forma controlada e elegante, como se fossem atributos públicos.

#### 5. **Métodos Mágicos (Dunder Methods)**
   - Implementação do método `__str__` para fornecer uma representação textual e legível do objeto `Restaurante`, facilitando a listagem e a depuração.

#### 6. **Organização de Código em Módulos**
   - Separação das responsabilidades em diferentes arquivos (`.py`). A classe `Restaurante` foi movida para seu próprio módulo, e o arquivo principal (`app.py`) ficou responsável apenas por interagir com o usuário e orquestrar os objetos.

## 📂 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o Sabor Express em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Lucas-Fiche/alura-python-saborexpress-OO.git](https://github.com/Lucas-Fiche/alura-python-saborexpress-OO.git)
    cd alura-python-saborexpress-OO
    ```

2.  **Execute a aplicação:**
    Não é necessário instalar dependências. Basta ter o Python instalado e executar o arquivo principal da aplicação.
    ```bash
    python app.py 
    ```

3.  **Interaja com a aplicação:**
    O menu de opções será exibido no seu terminal. Siga as instruções para usar o programa.

## 👨‍💻 Autor

Projeto desenvolvido por **Lucas Fiche** como parte dos estudos na plataforma Alura.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/lucas-fiche-76aa24201)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Lucas-Fiche)