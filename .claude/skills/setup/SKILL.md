---
name: setup
description: Configura ou revisa o perfil do negócio preservando dados existentes e preparando o primeiro projeto.
---

# Configurar o perfil

Leia INSTRUCOES.md, modelos/perfil.json e arquivos existentes. Não instale programas nem apague Git.

1. Se existe perfil.json, leia e resuma. Se apenas repetiu setup, preserve e siga ao projeto. Se pediu mudança, pergunte apenas o que quer mudar. Perfil preenchido no CLAUDE.md antigo pede migração revisada mantendo o original; alguns campos vazios não tornam o restante descartável.
2. Na base nova, aproveite o que já contou. Peça só o que falta: nome/negócio, público, serviço atual ou produto a desenvolver, região se pertinente, objetivos, tom e escopo trabalho/pessoal. Aceite “a definir”. Não infira preço, credenciais ou estratégia.
3. Mostre perfil e mapa de pastas. Use projetos/ e clientes/ como padrão. Se já há conteúdo em alunos/ e lancamentos/, ofereça manter no mapa em vez de mover. Só ajuste nomes escolhidos explicitamente.
4. Após confirmação, salve perfil.json conforme modelo. Pode usar scripts/vault.py (`perfil --entrada "arquivo revisado.json" --confirmar`) se Python 3.10+ estiver disponível; sem Python, escreva o JSON com as mesmas regras. O auxiliar recusa sobrescrever: mudança posterior exige revisão e cópia anterior em arquivo/. Não personalize os carregadores CLAUDE.md/AGENTS.md de uma base nova. Crie só pastas faltantes. Nenhum plugin Obsidian é necessário.
5. Confira o perfil salvo. Não crie diário como primeira entrega. Use projeto para registrar serviço/produto escolhido. Se não escolheu, pergunte qual; se já informou, reaproveite.

Skill ausente: confira pasta aberta, confiança do workspace, reinicie a sessão e use o pedido por extenso. Não prometa sincronizar conversas internas.
