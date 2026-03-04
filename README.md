# Lista Telefônica

Aplicação simples em Python para gerenciar uma agenda de contatos no terminal.

## Funcionalidades

- Consultar telefones por nome
- Incluir telefone para contato existente
- Incluir novo contato quando não encontrado
- Excluir telefone específico de um contato
- Excluir contato completo
- Remover automaticamente o contato quando ficar sem telefones

## Tecnologias

- Python 3

## Como executar

1. Clone o repositório:

```bash
git clone git@github.com:GiordanoBruno-dev/Lista-Telef-nica.git
```

2. Acesse a pasta do projeto:

```bash
cd Lista-Telef-nica
```

3. Execute o programa:

```bash
python exe.py
```

## Como usar

Ao iniciar, o programa exibe um menu com as opções:

- `[1]` Consultar Telefone
- `[2]` Incluir Telefone
- `[3]` Excluir Telefone
- `[4]` Excluir Nome
- `[5]` Sair

Basta digitar a opção desejada e seguir as instruções no terminal.

## Estrutura do projeto

```text
Lista-Telef-nica/
├── exe.py
├── README.md
└── LICENSE
```

## Observações

- O contato inicial `João` é inserido automaticamente com dois telefones para facilitar testes.
- O sistema evita cadastrar telefone duplicado para o mesmo contato.

## Melhorias futuras

- Persistência em arquivo (JSON/CSV)
- Validação de formato de telefone
- Interface gráfica
