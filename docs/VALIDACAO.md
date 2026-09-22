# Validação desta implementação

Executada em 22/09/2026, antes do PR.

## O que foi executado

- 15 testes unittest locais em Windows/Python 3.13, todos passaram. Incluem dois perfis fictícios, criação/reexecução de perfil e primeiro projeto, prévia sem gravação, recusa de sobrescrita, perfil legado parcial, caminhos com espaços/acentos, conflitos de caminho, symlink, preservação de notas/.git/.obsidian, entradas de skills e verificação de página.
- 19 skills canônicas e 19 entradas Codex passaram no validador da skill-creator; referências locais de Markdown foram conferidas sem destinos ausentes. As duas bases Anthropic foram comparadas aos arquivos da versão fixada.
- Verificador de preparo executado somente com cenários simulados Windows e macOS sem code no PATH. Não instala nada nem confere login/habilitação automaticamente.
- Em pastas isoladas fora do checkout, os dois exemplos geraram perfil e nota de projeto, preservados ao repetir. Páginas de demonstração usaram apenas esses dados fictícios, não representam pesquisa ou oferta comercial real.
- Uma página de demonstração foi servida em 127.0.0.1 somente a partir de site/. Navegador: HTTP 200, larguras 1440 e 390 sem rolagem horizontal, âncora funcional, campos/botão desabilitados, nenhuma requisição externa ou exceção JavaScript. Pedido de perfil.json retornou 404. O navegador também solicitou favicon inexistente, sem impacto na página.
- Conferência de HTML bloqueou scripts, rastreadores conhecidos, CSS que carrega imagens/importações, iframes, recursos remotos, formulário ativo, destino não aprovado e imagens fora da pasta.

## O que isso não comprova

Não executamos instaladores, login, cobrança, publicação de página do participante, sessão automatizada com modelo Claude/Codex ou teste de usabilidade com pessoa iniciante. O teste de discovery confere diretórios, frontmatter e destinos das entradas, não a interface de cada versão da extensão. As instruções de fluxo receberam revisão de conteúdo; não são prova de que toda resposta futura de IA será correta.

A simulação macOS não é um teste da interface nativa. A checagem de HTML é conservadora para a rota sem scripts e não substitui inspeção de rede, conteúdo, destinos e direitos dos materiais. O exemplo pesquisa-sem-web mostra limites honestos, não dados reais de mercado.

## Revisão antes de distribuir

Abrir ZIP da branch da PR numa pasta nova; conferir setup e primeiro projeto com dados fictícios; depois testar com uma pessoa iniciante e observar hesitações. Só após merge/validação do download principal atualizar o manual público de planejado para disponível. A versão principal não é alterada pela abertura do PR.
