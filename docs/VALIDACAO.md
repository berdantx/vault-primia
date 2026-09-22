# Validação desta implementação

Executada em 22/09/2026, durante a implementação e a revisão da [PR #1](https://github.com/berdantx/vault-primia/pull/1).

## O que foi executado

- 15 testes unittest locais em Windows/Python 3.13, todos passaram. Incluem dois perfis fictícios, criação/reexecução de perfil e primeiro projeto, prévia sem gravação, recusa de sobrescrita, perfil legado parcial, caminhos com espaços/acentos, conflitos de caminho, symlink, preservação de notas/.git/.obsidian, entradas de skills e verificação de página.
- Os mesmos 15 testes, sincronização das skills e conferência do HTML passaram também no GitHub Actions com Python 3.11 em Windows, macOS e Linux no commit 8447bfd. [Execução da PR](https://github.com/berdantx/vault-primia/actions/runs/35683193196). A primeira execução revelou uma comparação de caminhos temporários não resolvidos no teste; a comparação foi corrigida sem alterar o comportamento de gravação.
- O ZIP público do commit 8447bfd foi baixado e extraído numa pasta nova. As 19 skills e 19 entradas Codex estavam presentes, sem perfil pessoal na raiz, .git ou .obsidian. Sincronização e 15 testes passaram dentro do pacote extraído. SHA-256 do ZIP: c6207888e186a816a4190fbf39d4b762315475bfddc6d18f039d281c15a1f6a2.
- 19 skills canônicas e 19 entradas Codex passaram no validador da skill-creator; referências locais de Markdown foram conferidas sem destinos ausentes. As duas bases Anthropic foram comparadas aos arquivos da versão fixada.
- Verificador de preparo executado somente com cenários simulados Windows e macOS sem code no PATH. Não instala nada nem confere login/habilitação automaticamente.
- Em pastas isoladas fora do checkout, os dois exemplos geraram perfil e nota de projeto, preservados ao repetir. Páginas de demonstração usaram apenas esses dados fictícios, não representam pesquisa ou oferta comercial real.
- Uma página de demonstração foi servida em 127.0.0.1 somente a partir de site/. Navegador: HTTP 200, larguras 1440 e 390 sem rolagem horizontal, âncora funcional, campos/botão desabilitados, nenhuma requisição externa ou exceção JavaScript. Pedido de perfil.json retornou 404. O navegador também solicitou favicon inexistente, sem impacto na página.
- Conferência de HTML bloqueou scripts, rastreadores conhecidos, CSS que carrega imagens/importações, iframes, recursos remotos, formulário ativo, destino não aprovado e imagens fora da pasta.

## O que isso não comprova

Não executamos instaladores, login, cobrança, publicação de página do participante, sessão automatizada com modelo Claude/Codex ou teste de usabilidade com pessoa iniciante. O teste de discovery confere diretórios, frontmatter e destinos das entradas, não a interface de cada versão da extensão. As instruções de fluxo receberam revisão de conteúdo; não são prova de que toda resposta futura de IA será correta.

A simulação de preparo e a execução dos scripts no macOS não testam a interface nativa de VS Code, Obsidian ou assistentes. A checagem de HTML é conservadora para a rota sem scripts e não substitui inspeção de rede, conteúdo, destinos e direitos dos materiais. O exemplo pesquisa-sem-web mostra limites honestos, não dados reais de mercado.

## Revisão antes de distribuir

Abrir ZIP da branch da PR numa pasta nova; conferir setup e primeiro projeto com dados fictícios; depois testar com uma pessoa iniciante e observar hesitações. Só após merge/validação do download principal atualizar o manual público de planejado para disponível. A versão principal não é alterada pela abertura do PR.
