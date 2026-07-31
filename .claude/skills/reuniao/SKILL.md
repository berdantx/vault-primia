---
name: reuniao
description: Transforma transcrição de reunião ou call em resumo, decisões e próximos passos
type: slash-command
---

# /reuniao

Processe a transcrição que o dono deste vault colou (ou o arquivo que ele apontou, normalmente vindo do `inbox/`).

## O que extrair

1. **Quem participou** e o papel de cada um
2. **Sobre o que foi** a conversa, em duas linhas
3. **O que foi discutido**, em tópicos curtos
4. **O que ficou decidido** (só o que foi realmente fechado, não o que foi cogitado)
5. **Próximos passos:** quem faz o quê e até quando. Se o prazo não foi dito, escreva "sem prazo definido" em vez de inventar.
6. **Frases marcantes:** se alguém disse algo que serve como depoimento ou vira conteúdo, separe.

## Onde salvar

Salve em `reunioes/` (crie a pasta se não existir), com o nome no padrão:

```
AAAA-MM-DD-nome-da-pessoa-assunto.md
```

Use o nome da outra pessoa, não o do dono do vault. Máximo 4 palavras depois da data, tudo minúsculo, sem acento, separado por hífen.

## Depois de salvar, sem perguntar

- Se a conversa foi com um aluno ou cliente, atualize a nota dele em `alunos/` com o que mudou: o que foi combinado, o momento dele, o próximo passo. Se não existir nota, crie.
- Se apareceu tarefa para o dono do vault, registre em `diario/` de hoje, na seção Pendências.
- Se apareceu ideia de conteúdo, jogue em `conteudo/`.

No final, avise em três linhas o que foi criado ou atualizado. Não repita o resumo inteiro.
