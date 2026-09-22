# Instalação e recuperação

## Windows e Mac

Use VS Code atual em Windows 64 bits suportado pela Microsoft ou macOS ainda com atualizações de segurança da Apple. Claude Code informa mínimo de 4 GB de RAM, x64/ARM64, Windows 10 1809+ ou macOS 13+; o computador precisa atender também ao VS Code atual. Internet e acesso elegível à conta são necessários. Confira [VS Code](https://code.visualstudio.com/docs/supporting/requirements) e [Claude Code](https://code.claude.com/docs/en/setup).

Windows: baixe instaladores oficiais do VS Code e Obsidian e execute seguindo as telas. Mac: abra o download e mova os aplicativos para Aplicativos conforme indicado. [VS Code Windows](https://code.visualstudio.com/docs/setup/windows), [VS Code Mac](https://code.visualstudio.com/docs/setup/mac), [Obsidian](https://obsidian.md/help/install).

As extensões ficam em VS Code → Extensões (Ctrl+Shift+X no Windows, Cmd+Shift+X no Mac):

- [Claude Code for VS Code, Anthropic](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code): instalar/habilitar, abrir o painel, login pessoal e mensagem de teste. Conta gratuita Claude não inclui Claude Code; confira plano elegível ou cobrança separada Console na [documentação](https://code.claude.com/docs/en/vs-code). Não configure API paga só para contornar um erro sem decidir esse uso.
- [Live Server, Ritwick Dey](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): instalar/habilitar, sem conta. Go Live é testado com site/index.html.
- [Codex, OpenAI](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt): opcional; login com sua conta ChatGPT e limites do seu plano. [Guia](https://developers.openai.com/codex/ide). Windows nativo é suportado, WSL não é requisito; siga [orientação atual](https://developers.openai.com/codex/windows) se houver configuração de ambiente protegido.

A extensão Claude inclui o necessário ao painel, mas não garante o comando claude no terminal. O mesmo cuidado vale para Codex. Não instale CLI/WSL como pré-requisito desta aula. Obsidian é gratuito para uso local e não exige Sync/Publish: [condições](https://obsidian.md/pricing).

## Conferência opcional, sem instalar nada

Se Python 3.10+ já está disponível, você ou o assistente podem executar na pasta do kit:

```text
python scripts/verificar_preparo.py
```

No Mac, normalmente `python3`. O script só procura aplicativos e, se code está disponível no PATH, consulta `code --list-extensions`. Não instala, faz login, muda configurações nem comprova habilitação/compatibilidade. Mostra a próxima conferência de cada item. Code ausente no PATH não significa VS Code ausente; use a interface. Linux não é o alvo desse verificador; siga a conferência manual/documentação do fornecedor.

Não é preciso instalar Python só para isso. COMECE-AQUI.md e o guia público cobrem todo o preparo manual. Os scripts de perfil/projeto/HTML também são opcionais.

## Problemas comuns

- **Comando ausente:** confira pasta contendo .claude/skills e CLAUDE.md, expanda a árvore, confira confiança do workspace e reinicie a sessão após baixar o kit. Um comando pessoal com o mesmo nome pode ter precedência; leia a skill local explicitamente para evitar confusão. Não assuma que toda falha é pasta errada.
- **Codex:** abra a mesma pasta, use seletor de skills ou `$setup`. Entradas em .agents/skills apontam à fonte canônica. Não espere compartilhar histórico interno do Claude.
- **Login/limite:** confira conta e acesso no painel; aguarde renovação indicada ou peça apoio. Não compartilhe segredos.
- **Empresa bloqueia instalação:** registre a mensagem e peça apoio à TI. Não altere política de segurança por conta própria.
- **Perfil existente:** o auxiliar não sobrescreve. Leia, proponha só alterações necessárias e preserve versão anterior antes de atualizar após aprovação. Um CLAUDE.md antigo com perfil também exige migração revisada.
- **Git clone já feito:** não apague .git automaticamente. Use nova cópia ZIP ou trate uma desvinculação explicitamente. Não envie suas notas ao template.
- **Atualizar kit usado:** não extraia outro ZIP por cima. Compare numa pasta nova, faça cópia de segurança do acervo e traga só instruções aprovadas. Preserve perfil, pastas configuradas, skills próprias e .obsidian.
- **Go Live não aparece:** confira extensão habilitada, arquivo salvo e pasta site aberta. Botão direito → Open with Live Server. Veja docs/PAGINA-LOCAL.md.
- **Ainda travou:** use modelos/acompanhar-sem-ia.md; o primeiro projeto pode ser preenchido sem conta ou instalação.

Nenhum plugin Obsidian é distribuído/ativado. Ativação de plugin comunitário futuro será explícita. Esta revisão não altera os manuais públicos para dizer que main já recebeu a mudança antes do merge.
