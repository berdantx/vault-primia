---
name: diario
description: Abre o dia — lê pendências, revisa ontem e define o foco
type: slash-command
---

# /diario

Abra o dia de trabalho do dono deste vault:

1. Verifique se já existe o arquivo de hoje em `diario/` (formato `AAAA-MM-DD.md`). Se não existir, crie com as seções: **Foco do dia**, **Pendências**, **Registros**.
2. Leia o diário do último dia útil e traga o que ficou em aberto.
3. Olhe a pasta `inbox/` e liste o que ainda não foi processado.
4. Olhe `lancamentos/` e `alunos/` e liste até 5 pontos que precisam de ação, do mais urgente ao menos.
5. Com base nisso, sugira UM foco principal para hoje e pergunte se ele concorda ou quer trocar.
6. Registre a decisão no diário de hoje.

Seja direto: o dia começa em 2 minutos, não com um relatório.
